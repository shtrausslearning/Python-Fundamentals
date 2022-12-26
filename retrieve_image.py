
# option 1
import urllib.request
url = 'https://i.imgur.com/SdGxz2D.jpg'
fpath = 'SdGxz2D.jpg'
urllib.request.urlretrieve(url, fpath)
img = Image.open(fpath)
img = img.resize((224, 224), Image.ANTIALIAS)

# option 2
from PIL import Image
import PIL.ImageOps  
import requests
import io

imgUrl = 'https://i.imgur.com/SdGxz2D.jpg'
r = requests.get(imgUrl, stream=True)
img = Image.open(io.BytesIO(r.content))
img = img.resize((224, 224), Image.ANTIALIAS)
