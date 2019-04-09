from PIL import Image
import imagehash
import glob
import sys
import csv
import pickle
import os

#to read in the dict that I made
'''
pickle_in = open("dict.hashes","rb")
example_dict = pickle.load(pickle_in)
'''

img_paths = sys.argv[1]
hashes = {}

with open (img_paths, 'r') as f:
    names= f.readlines()
    for name in names:
        name = name[name.find('/ic'): name.find('JPG')+len('JPG')]
        if os.path.isfile(name):
            try:
                img_hash = imagehash.average_hash(Image.open(name), 8)
                print(str(name) + ';' + str(img_hash))
                hashes[name] = img_hash
            except OSError:
                continue

# To write in a dict format
pickle_out = open("dict.hash","wb")
pickle.dump(hashes, pickle_out)
pickle_out.close()

# To write in a csv format
'''
w = csv.writer(open("dict_hash", "w"))
for key, val in hashes.items():
    w.writerow([key, val])
'''
