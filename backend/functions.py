import os
import glob
import time

import pickle
import numpy as np
import pandas as pd

from sklearn.cluster import MiniBatchKMeans, DBSCAN
from scipy.spatial import distance

def clusterN(n):
    
    ### LOAD IN DATA
    list_of_pkls = glob.glob('../data/df_at_*.pkl')
    if len(list_of_pkls)==0:
        return {'num_detections': 0, 'num_clusters': 0, 'breakdown': 0 }
    most_recent_file = max(list_of_pkls, key=os.path.getctime)
    
    with open(most_recent_file, 'rb') as f:
        df = pickle.load(f)
    
    ### CLUSTER DATA
    emb = df['embedding'].apply(pd.Series)
    model = MiniBatchKMeans(n_clusters=n).fit( emb.values )
    
    ### ASSIGN CLUSTER LABEL
    df['cluster'] = model.labels_

    ### WRITE OUT DATA
    with open('../data/df_to_display_known.pkl', 'wb') as f:
        pickle.dump(df, f)

    print('Done.')
    
    breakdown = []
    for i, x in enumerate(df['cluster'].value_counts()):
        breakdown.append({ 'id':i,'count':x })
    
    return {'num_detections': len(df), 'num_clusters': len(df['cluster'].unique()), 'breakdown': breakdown } 

def clusterUnknown():
    
    ### LOAD IN DATA
    list_of_pkls = glob.glob('../data/df_at_*.pkl')
    if len(list_of_pkls)==0:
        return {'num_detections': 0, 'num_clusters': 0, 'breakdown': 0 }
    most_recent_file = max(list_of_pkls, key=os.path.getctime)
    
    with open(most_recent_file, 'rb') as f:
        df = pickle.load(f)
    
    ### CLUSTER DATA
    emb = df['embedding'].apply(pd.Series)
    model = DBSCAN( eps=0.005 , min_samples=5 , metric='cosine' ).fit( emb.values )
    
    ### ASSIGN CLUSTER LABEL
    df['cluster'] = model.labels_

    ### WRITE OUT DATA
    with open('../data/df_to_display_unknown.pkl', 'wb') as f:
        pickle.dump(df, f)

    print('Done.')

    breakdown = []
    for i, x in enumerate(df['cluster'].value_counts()):
        breakdown.append({ 'id':i,'count':x })
    
    return {'num_detections': len(df), 'num_clusters': len(df['cluster'].unique()), 'breakdown': breakdown }
       
def getChips(known):

    if known==True:

        with open('../data/df_to_display_known.pkl', 'rb') as f:
            df = pickle.load(f)
    else:
        with open('../data/df_to_display_unknown.pkl', 'rb') as f:
            df = pickle.load(f)

    frame_nums = [str(v) for v in df['frame'].values]
    chips = list(df['chip'].values)
    cluster_labels = [str(x) for x in df['cluster'].values]

    id = 0
    tr = []
    for f, c, l in zip(frame_nums, chips, cluster_labels):
        tr.append({'id': id, 'frame_num': f, 'chip':c, 'cluster': l})
        id+=1 
            
    return {'data':tr}

    