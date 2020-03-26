import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)

mask = cv2.imread('mhmask.jpg')

addMask = 0

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        dim = (roi_color.shape[1], roi_color.shape[0])
 
        mask = cv2.resize(mask, dim)
        addMask = cv2.addWeighted(roi_color,0.1,mask,0.6,1)
            
    screenSize = cv2.resize(addMask, (1000, 700))
    cv2.imshow('Eye Detection',screenSize)
    
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()