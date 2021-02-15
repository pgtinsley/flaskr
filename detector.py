#!/usr/bin/env python3

import os
import sys
import cv2
import numpy as np
import jetson.inference
import jetson.utils
import datetime
import pafy
import urllib
import simplejson
import getopt
import base64
import zmq
from turbojpeg import TurboJPEG

import time

def py_clip(x,l,u): return (l if x < l else u if x > u else x)

# default values
netname = 'facenet-120'
conf_thresh = 0.5
uri = 'file:///home/blumb/tel.mkv'
port = 9776

# parse options
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:c:u:p:")
except getopt.GetoptError as err:
  # print help information and exit:
  print(err) # will print something like "option -a not recognized"
  sys.exit(-1)

for o, a in opts:
  print('processing option {0} and arg {1}'.format(o,a))
  if o == '-n': netname = a
  elif o == '-c': conf_thresh = float(a)
  elif o == '-u': uri = a
  elif o == '-p': port = int(a)

#print('Using ZMQ port {0}'.format(port))

net = jetson.inference.detectNet(netname,[],conf_thresh)

jpeg = TurboJPEG()

# get the video stream
# the URL below can be as short as the ID (e.g., 'iYhCn0jf46U')
# if the URL is a 'file://' URL, it is handled as a special case.

up = urllib.parse.urlparse(uri)
if up.scheme in ['file','rtsp']:
  cap_url = up.path
else:
  vPafy = pafy.new(URL)
  my_stream = vPafy.getbest()
  cap_url = my_stream.url
cap = cv2.VideoCapture(cap_url)

nf = 0
nd = 0


# set up the ZMQ publish facility
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://*:{0}'.format(port))

print('Detector running (streaming to port {})...'.format(port))
# loop over all frames
while True:
  ret,frame = cap.read()
  if (ret is None) or (frame is None): break
  #time.sleep(0.25)
  h,w,_ = frame.shape
  # detection network requires RGBA
  img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)
  img[:,:,3] = 255 
  # use GPU to perform detection
  im_cuda = jetson.utils.cudaFromNumpy(img)
  detections = net.Detect(im_cuda,w,h,'none')
  # process detections (if anything was found)
  if len(detections) > 0:
    # build dictionary of detection info for this frame
    analytics = {'frame':nf, 'detections':[]}
    for i,d in enumerate(detections):
      # generate info for the current detection in the current frame
      left = int(py_clip(d.Left,0,w-1))
      top = int(py_clip(d.Top,0,h-1))
      right = int(py_clip(d.Right,0,w-1))
      bottom = int(py_clip(d.Bottom,0,h-1))
      # extract and resize from original frame (without alpha)
      chip = cv2.resize(frame[top:bottom,left:right,:],(160,160),interpolation=cv2.INTER_AREA).copy()
      jchip = jpeg.encode(chip)
      # debug: uncomment the following 2 lines to write chips - should be 160x160
      #fn = 'frame{0}.det{1}.jpg'.format(nf,i)
      #with open(fn,'wb') as f: f.write(jchip)
      # convert chip to a character string using ASCII-85 encoding
      b64jchip = base64.b64encode(jchip)
      # assemble dictionary info for this detection
      an = {'index':i, 'conf':d.Confidence, 'left':d.Left, 'right':d.Right, 'top':d.Top, 'bottom':d.Bottom, 'chip':b64jchip,'classID':d.ClassID, 'instance':d.Instance}
      analytics['detections'].append(an)
    # now write all of the frame's detection info
    j=simplejson.dumps(analytics)+'\n'
    socket.send_string(j)
    nd += len(detections)
  # end of processing for this frame
  # print('{0}: frame {1} nd {2}'.format('|\-/'[nf%4],nf,nd),end='\r')
  nf += 1

print('\n')
