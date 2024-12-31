# Importing the Module
from PIL import Image

# Importing a new Image
image = Image.open('Images\\FirstImg.jpg')

# Creating a new Image
newImg = Image.new('RGBA', (600, 600))

# show the image
image.show()

# Saving the Image (and converting into png)
image.save('Images\\ImgSave.png')