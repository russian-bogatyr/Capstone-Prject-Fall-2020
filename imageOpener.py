from PIL import Image
import random
import os

"""
filename = input("Enter your value: ")
"""
filename = random.choice(os.listdir(os.path.join(os.path.dirname(os.curdir), 'Sample faces')))
#read the image
im1 = Image.open(filename)

#show images
im1.show()