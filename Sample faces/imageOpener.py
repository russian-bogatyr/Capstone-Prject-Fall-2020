from PIL import Image
import random
import os

"""
filename = input("Enter your value: ")
"""
"""
dir = 'Users\super\Documents\GitHub\Machine-Learing-Nose-Jobs\Sample faces'
"""
filename = random.choice(os.listdir("C:/Users/super/Documents/GitHub/Machine-Learing-Nose-Jobs/Sample faces"))
#read the image
im1 = Image.open(filename)

#show images
im1.show()