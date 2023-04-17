from rembg import remove
from PIL import Image
input = 'image.jpg'
output = 'image.jpg'
in = Image.open(input)
out = remove(in)
out.save(output)