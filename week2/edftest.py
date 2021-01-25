from edf2csv import EDF 
## depends on eegtools too 

def convert(subject):
	edf=EDF(subject)

	signal=edf.signal()
	info=edf.info()

	print(signal.shape)
	print(info)

	edf.ann_to_csv()
	edf.signal_to_csv()


def main():
	print('*** edf2csv conversion ***')
	subject=input('Enter the name of the edf file to csv file :- ')
	print('*** END ***')

main()


