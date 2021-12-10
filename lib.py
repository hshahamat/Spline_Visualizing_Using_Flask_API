import numpy as np
import scipy.interpolate as si
import cv2


def bspline(cv, n=100, degree=3):
    """ Calculate n samples on a bspline

        cv :      Array ov control vertices
        n  :      Number of samples to return
        degree:   Curve degree
    """
    cv = np.asarray(cv)
    count = cv.shape[0]

    # Prevent degree from exceeding count-1, otherwise splev will crash
    degree = np.clip(degree,1,count-1)

    # Calculate knot vector
    kv = np.array([0]*degree + list(range(count-degree+1)) + [count-degree]*degree,dtype='int')

    # Calculate query range
    u = np.linspace(0,(count-degree),n)

    # Calculate result
    return np.array(si.splev(u, (kv,cv.T,degree))).T



def show_spline_on_img(img,ann):
    pts = np.array(ann['c'], np.int32)
    for p in pts:
        cv2.circle(img,(p[0],p[1]), 5, (0,255,0), -1)
    
    pts = np.array(ann['c'], np.int32)
    pts = pts.reshape((-1, 1, 2))
    
    isClosed = False
    color = (255, 0, 0)
    thickness = 1
    cv2.polylines(img, [pts],isClosed, color, thickness,lineType = cv2.LINE_AA)
    p = bspline(pts,n=100)[:,0,:]    
    color = (0, 0, 255)
    thickness = 2
    cv2.polylines(img, [p.astype(np.int32)],isClosed, color, thickness,  lineType = cv2.LINE_AA)
    return img



