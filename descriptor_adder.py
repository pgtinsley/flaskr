#!/usr/bin/env python3

import os
import sys
import numpy as np
import datetime
import simplejson
import getopt
import base64
import zlib
from PIL import Image
import traceback

import torch
from torchvision.transforms import functional as F
from facenet_pytorch import MTCNN, InceptionResnetV1
from facenet_pytorch import extract_face

from turbojpeg import TurboJPEG

import zmq

import pickle
import pandas as pd

#
# Usage: descriptor_adder [-h host] [-i port] [-o port]
#

# set up VGGface2 network
#
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print('Running on device: {}'.format(device))
resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)
jpeg = TurboJPEG()

host = '127.0.0.1'
iport = 9776
# oport = 9777

try:
#     opts, args = getopt.getopt(sys.argv[1:], "h:i:o:")
    opts, args = getopt.getopt(sys.argv[1:], "h:i:")
except getopt.GetoptError as err:
  # print help information and exit:
  print(err) # will print something like "option -a not recognized"
  sys.exit(-1)

for o, a in opts:
  print('processing option {0} and arg {1}'.format(o,a))
  if o == '-i': iport = int(a)
  elif o == '-h': host = a
#   elif o == '-o': oport = int(a)

# set up ZMQ - we are subscribing to output of the detector,
# and publishing the same detections with a feature vector added to
# each detection

context = zmq.Context()
isocket = context.socket(zmq.SUB)
isocket.connect('tcp://{0}:{1}'.format(host,iport))
isocket.setsockopt_string(zmq.SUBSCRIBE,'')

# osocket = context.socket(zmq.PUB)
# osocket.bind('tcp://*:{0}'.format(oport))

nf = 0
nd = 0

j_list = []

print('Extractor running (listening to port {})...'.format(iport))
while True:
  # get frame info
  line = isocket.recv_string()
  j = simplejson.loads(line)
  dets = j['detections']
  imgs = []
  # assemble all detected chips into an array
  for d in dets:
    chip = base64.b64decode(d['chip'])
    #fn = 'frame{0}.index{1}.conf{2}.jpg'.format(j['frame'],d['index'],d['conf'])
    #with open(fn,'wb') as f:
      #f.write(chip)
    img = jpeg.decode(chip)
    imgs.append(F.to_tensor(np.float32(img)))
  # batch-compute embeddings for all chips
  aligned = torch.stack(imgs).to(device)
  embeddings = resnet(aligned).detach().cpu().numpy()
  # store the embeddings in the dictionary we read from the detector
  for i,e in enumerate(embeddings):
    j['detections'][i]['embedding'] = e.tolist()
    j_list.append( [ nf, j['detections'][i]['chip'], e.tolist() ] )
    #print(j['detections'][i])
    #print(e) 
    #print('\n') 
  #print('sending [{0}]'.format(j))
  # publish send detections-with-embeddings
  # osocket.send_string(simplejson.dumps(j)+'\n')
  nf += 1
  nd += len(dets)
  # print('\t\t\t{0}: {1} frames processed, {2} detections'.format('-\|/'[nf%4],nf,nd),end='\r')
  if nf % 300 == 0:
    with open('./data/df_at_f{}.pkl'.format(nf),'wb') as f:
        print('Saving data snapshot to ./data/df_at_f{}.pkl'.format(nf))
        pickle.dump(pd.DataFrame(j_list, columns=['frame','chip','embedding']), f)

print('\n')
