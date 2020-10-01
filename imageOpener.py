from PIL import Image
import random
import os

os.chdir(os.path.join(os.path.dirname(os.curdir), 'csv_files'))

filename = random.choice(os.listdir(os.curdir))
#read the image
im1 = Image.open(filename)

#show images
im1.show()