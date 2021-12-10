import cv2
import json
import requests
from lib import show_spline_on_img
from PIL import Image
from base64 import b64decode
import io
import numpy as np




imgp = "dog.jpg"
annp = "Spline/dog.jpg.json"


f = open(annp)
data = json.load(f)
ann = data['annotations'][0]['shape']
ann['packetID'] = "TestFlaskAPP2021"

url = 'http://127.0.0.1:5000/'
my_img = {'image': open(imgp, 'rb')}
r = requests.post(url, files=my_img, data=ann)
res = r.json()
print(res['packetID'])

img = res['resultImage']
img = np.array(img,dtype=np.uint8)
img = img.astype(np.uint8)

img = cv2.imdecode(img,flags=1)
cv2.imshow("points",img)    
cv2.waitKey(0)  
cv2.destroyAllWindows()  