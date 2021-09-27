import pickle
import glob

for file in glob.glob('*.dat'):
    with open(f'{file}', 'rb') as pickle_in:
        load_file = pickle.load(pickle_in)
    print(load_file)
