from PIL import Image
import cv2
import numpy as np
from keras.models import load_model 

model = load_model('my_mnist_model.h5')

def predict(path_image):
    data = []
    im = cv2.imread(path_image)
    im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thre = cv2.threshold(im_gray,220,255,cv2.THRESH_BINARY)
    im_not = cv2.bitwise_not(thre)
    _,contours,hierachy = cv2.findContours(im_not,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        roi = im_not[y:y+h,x:x+w]
        if (roi.shape[0]<28) and (roi.shape[1]<28):
            pass
        else:
            roi_resize = cv2.resize(roi,(22,22),interpolation = cv2.INTER_LINEAR)
            roi_padding = np.pad(roi_resize,(3,3),'constant',constant_values=(0,0))
            kernel = np.array([[0,1]],np.uint8)
            roi_dila = cv2.dilate(roi_padding,kernel)
            roi_reshape = roi_dila.reshape((1,28,28,1)).astype(np.float32)/255
            predict = model.predict_classes(roi_reshape)
            cv2.putText(im,str(int(predict)),(int((x)),int((y))),1,cv2.FONT_HERSHEY_COMPLEX,(0,255,0),1,cv2.LINE_AA)
            data.append([x,y,str(int(predict))])
    answer_str=[]
    for i in data:
        answer_str.append(str(i[-1]))
    return (int(''.join(answer_str)))
