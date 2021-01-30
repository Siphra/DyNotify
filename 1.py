from PIL import image
import requests
import io





q = requests.get(https://images-na.ssl-images-amazon.com/images/I/71PGvPXpk5L._AC_SL1500_.jpg)

with image.open(io.bytes(q.content)) as image1:
    image1.save(I:\)

