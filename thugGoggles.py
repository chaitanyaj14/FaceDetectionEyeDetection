import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

overlay = cv2.imread('tg.jpg')

addGoggles = 0

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        dim = (roi_color.shape[1], roi_color.shape[0])
 
        overlay = cv2.resize(overlay, dim)
        addGoggles = cv2.addWeighted(roi_color,0.3,overlay,0.6,1)
            
    resized_img = cv2.resize(addGoggles, (1000, 700))
    cv2.imshow('Thug Life Goggles',resized_img)
    
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()