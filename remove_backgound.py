from rembg import remove
from PIL import Image

input_path = 'image/27277-EN000.jpg'
output_path = 'image/27277-EN000.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
