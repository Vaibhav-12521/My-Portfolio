from PIL import Image

# Open the PNG image
png_image = Image.open('testimonial1.png')

# Convert the image to RGB (JPG doesn't support transparency)
rgb_image = png_image.convert('RGB')

# Save the image as JPG
rgb_image.save('output_image.jpg', 'JPEG')

print("Image successfully converted from PNG to JPG!")
