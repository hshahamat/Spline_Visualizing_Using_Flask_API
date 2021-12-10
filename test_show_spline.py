import cv2
import json
from lib import show_spline_on_img





imgp = "dog.jpg"
annp = "Spline/dog.jpg.json"

img = cv2.imread(imgp)
f = open(annp)
data = json.load(f)
ann = data['annotations'][0]['shape']

img = show_spline_on_img(img, ann)


cv2.imwrite('result.jpg',img)       
cv2.imshow("points",img)    
cv2.waitKey(0)  
cv2.destroyAllWindows()


