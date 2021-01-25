from __future__ import division, print_function, absolute_import
import os
import pyedflib

def printInfo():
    data_dir = os.path.join('.', 'data')
    file1=input('Enter file name :- ')
    test_data_file = os.path.join(data_dir, file1)
    f = pyedflib.EdfReader(test_data_file)
    print("\nlibrary version: %s" % pyedflib.version.version)

    print("\ngeneral header:\n")

    print("File duration: %i seconds" % f.file_duration)
    print("Startdate: %i-%i-%i" % (f.getStartdatetime().day,f.getStartdatetime().month,f.getStartdatetime().year))
    print("Starttime: %i:%02i:%02i" % (f.getStartdatetime().hour,f.getStartdatetime().minute,f.getStartdatetime().second))
    print("Recording_additional: %s" % f.getRecordingAdditional())
    print("Datarecord duration: %f seconds" % f.getFileDuration())
    print("Number of datarecords in the file: %i" % f.datarecords_in_file)
    print("Number of annotations in the file: %i" % f.annotations_in_file)

    channel = 3
    print("\nSignal parameters for the %drd channel:\n\n" % channel)

    print("Label: %s" % f.getLabel(channel))
    print("Samples in file: %i" % f.getNSamples()[channel])
    print("Physical Maximum: %f" % f.getPhysicalMaximum(channel))
    print("Physical Minimum: %f" % f.getPhysicalMinimum(channel))
    print("Digital Maximum: %i" % f.getDigitalMaximum(channel))
    print("Digital Minimum: %i" % f.getDigitalMinimum(channel))
    print("Physical Dimension: %s" % f.getPhysicalDimension(channel))
    print("Sample Frequency: %f" % f.getSampleFrequency(channel))
    print("Maximum Value in Dataset: %f" %f.getDigitalMaximum(channel))
    print("Minimum Value in Dataset: %f" %f.getDigitalMinimum(channel))
    
def main():
    printInfo()

if __name__=='__main__':
    main()