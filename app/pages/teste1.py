from PIL import Image
import os

def optimize_image(image_path, output_size=(800, 600), quality=85, format='JPEG'):
    with Image.open(image_path) as img:
        img.thumbnail(output_size)
        img.save(image_path, format=format, quality=quality, optimize=True)
        img.info = {}  # Remover metadados

# Diretório com as imagens
image_dir = 'images'

image_path = "C:/Users/david/OneDrive/Projetos/MyHabits/data/images/WhatsApp Image 2024-09-25 at 21.27.22.jpeg"
for filename in os.listdir(image_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(image_dir, filename) 

        optimize_image(image_path)