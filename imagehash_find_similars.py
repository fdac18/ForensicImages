# we got image hash from https://github.com/JohannesBuchner/imagehash
#run it: python3 imagehash_find_similars.py images/1.JPG images

from PIL import Image
import imagehash
import glob
import sys


img_name = sys.argv[1]
img_dir = sys.argv[2]

hash_base = imagehash.average_hash(Image.open(img_name), 8)
for name in glob.glob(img_dir + '/*.JPG'):
    print(name)
    hash_comp = imagehash.average_hash(Image.open(name), 8)
    print(hash_base - hash_comp)
