import mne

import numpy as np

import os



#%%

epoch_out_path=('C:/Users/mca/Downloads/') #file path

epochs_fname=os.path.join(epoch_out_path,'AB_1_SEI-epo.fif')

epochs=mne.read_epochs(epochs_fname) #reading the epochs/ictal/



#%%

##check the atributes of the epochs, using, epochs.info

data=epochs.get_data() #data is of shape: number of trials x number of channels x data points (or time points or sample points)



data1=data[0,:,:] ## use only the data for 19 channels

np.savetxt("C:/Users/mca/Downloads/file1.txt", data1,delimiter=',') ##saves in .text seperated by comma

##loading the .txt data

xx= np.loadtxt('C:/Users/mca/Downloads/file1.txt', delimiter=',', unpack=True)
