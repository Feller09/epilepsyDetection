import os 
import os.path as op 

from download import download
import numpy as np 
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import  StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline 

from mne_features.feature_extraction import FeatureExtractor 

print(__doc__)


def download_bonn_ieeg(path,verbos=False):
    base_url='http://epileptologie-bonn.de/cms/upload/workgroup/lehnertz/'
    urls=[
            ('setC','N.zip'),('setD','F.zip'),('setE','S.zip')
            ]
    paths=list()
    for set_name ,url_suffix in urls:
        _path= download(op.join(base_url,url_suffix),op.join(path,set_name),kind='zip',
                replace=False,verbose=verbose)
        paths.append(_path)
    return paths 

paths=download_bonn_ieeg('./bonn_data')

data_segments=list()
labels=list()
sfreq=173.61

for path in paths:
    fnames=[s for s in os.listdir(path) if s.lower().endswith('.txt')]
    for fname in fnames:
        _data=pd.read_csv(op.join(path,fname),sep='\n',header=None)
        data_segments.append(_data.values.T[None,...])
    if 'setE' in path:
        labels.append(np.ones((len(fnames),)))
    else:
        labels.append(np.zeroes((len(fnames),)))

data=np.concatenate(data_segments)
y=np.concatenate(labels,axis=0)

#shape of the extraceted data 
print(data.shape)







