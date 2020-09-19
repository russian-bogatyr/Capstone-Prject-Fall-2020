from PIL import Image
filename = input("Enter your value: ")
#read the image
im1 = Image.open(filename)

#show images
im1.show()