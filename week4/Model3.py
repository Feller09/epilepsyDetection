#import tensorflow as tf 
import numpy as np 
#from keras.models import Sequential 
#from keras.utils import np_utils 
#from keras.layers import Dense,Activation,LSTM,Dropout,AveragePooling3D 
import pandas as pd 
import matplotlib.pyplot as plt 
#from tensorflow import keras
import torch 
import torch.nn as nn 
import torch.nn.functional as F

df=pd.read_csv('data.csv')
print(df.head())

x=df.values 
x=x[:,1:-1]
x = np.asarray(x).astype(np.float32)

from sklearn.model_selection import train_test_split 

##taking 20% for test ## replace x with y as it will half for testing and half for training for ybased 
y=np.array(df['y'])
y=np_utils.to_categorical(y)
print(y.shape)
print(x.shape)
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.20,random_state=1)



class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        # 1 input image channel, 6 output channels, 3x3 square convolution
        # kernel
        self.conv1 = nn.Conv2d(1, 6, 3)
        self.conv2 = nn.Conv2d(6, 16, 3)
        # an affine operation: y = Wx + b
        self.fc1 = nn.Linear(16 * 6 * 6, 120)  # 6*6 from image dimension
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # Max pooling over a (2, 2) window
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        # If the size is a square you can only specify a single number
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


net = Net()
print(net)