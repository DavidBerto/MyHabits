from PIL import Image, ImageDraw, ImageFont

# Create a blank image

img = Image.new('RGB', (200, 250), color='white')

# Create an ImageDraw object

d = ImageDraw.Draw(img)

# Load a font

fnt = ImageFont.truetype('arial.ttf', 10)

# Write text on the image

d.text((10, 10), "          Agendamentos  \n"
                  "11:00 - 12:00 - Joana Silva\n"
                  "13:00 - 14:00 - Pedro Cabral\n"
                  "15:00 - 16:00 - João Batista", font=fnt, fill=(0, 0, 0))

# Save the image

img.save('text_image.png')