from PIL import Image, ImageEnhance

image = Image.open('Images\\FirstImg.jpg')

# Making a enhancer
ColorEnchancer = ImageEnhance.Color(image)
ContrastEnchancer = ImageEnhance.Contrast(image)
BrightnessEnchancer = ImageEnhance.Brightness(image)
SharpnessEnchancer = ImageEnhance.Sharpness(image)

# Applying the Enchance
EnhancedImage = ColorEnchancer.enhance(8) # Changes Vibrance
ContrastImage = ContrastEnchancer.enhance(4) # Changes Contrast
BrightnessImage = BrightnessEnchancer.enhance(1.4) # Changes Brightness
SharpnessImage = SharpnessEnchancer.enhance(5) # Changes Sharpness

# EnhancedImage.show()
# ContrastImage.show()
# BrightnessImage.show()
# SharpnessImage.show()