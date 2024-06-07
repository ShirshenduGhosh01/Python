from PIL import Image
import random

# Load the nine images
img1 = Image.open("image1.png")
img2 = Image.open("image2.png")
img3 = Image.open("image3.png")
img4 = Image.open("image4.png")
img5 = Image.open("image5.png")
img6 = Image.open("image6.png")
img7 = Image.open("image7.png")
img8 = Image.open("image8.png")
img9 = Image.open("image9.png")

# Create a list of the images
image_list = [img1, img2, img3, img4, img5, img6, img7, img8, img9]

# Shuffle the list
random.shuffle(image_list)

# Select three random images
password = image_list[:3]

# Save the password images
for i in range(3):
    password[i].save(f"password{i+1}.png")