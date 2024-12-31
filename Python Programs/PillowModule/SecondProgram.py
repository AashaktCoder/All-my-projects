from PIL import Image

image = Image.open('Images\\FirstImg.jpg')

# Rotating the Image
imageRotate = image.rotate(45, expand=True, fillcolor=(0, 255, 155))

# Cropping the Image
imageCrop = image.crop((0,50,200,230))

# Flipping the Image
imageFlipHorizontal = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
imageFlipVertical = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

# Resizing the Image (ruins aspect ratio of image)
imageResize = image.resize((800, 300))

# Resizing the Image (does not ruin aspect ratio of image)
imageResizeBetter = image.resize((image.size[0] * 2, image.size[1] * 2))

# imageRotate.show()
# imageCrop.show()
# imageFlipHorizontal.show()
# imageFlipVertical.show()
imageResizeBetter.show()