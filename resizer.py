import cv2

image = cv2.imread(input("Enter Image Path : "), 1)
width = int(input("Width of new Image : "))
height = int(input("Height of new Image : "))
dim = (width, height)
new = cv2.resize(image, dim)
filename = input("New Filename (with extension): ")
cv2.imwrite(filename, new)
