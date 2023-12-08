from rembg import remove
from PIL import Image

input_path = 'image/image.jpg'
output_path = 'image/image.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
