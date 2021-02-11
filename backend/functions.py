import os
import glob

import pickle
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
    with open('./df_to_display.pkl', 'wb') as f:
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
    with open('../data/df_to_display.pkl', 'wb') as f:
        pickle.dump(df, f)

    print('Done.')

    breakdown = []
    for i, x in enumerate(df['cluster'].value_counts()):
        breakdown.append({ 'id':i,'count':x })
    
    return {'num_detections': len(df), 'num_clusters': len(df['cluster'].unique()), 'breakdown': breakdown }
    
    
# def thumbnail():
    
    
    