import cv2


# Create our body classifier
faceCascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 5)
    
    
    # Extract bounding boxes for any bodies identified
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

    cv2.imshow("hello", frame)

cap.release()
cv2.destroyAllWindows()



















import cv2

img = cv2.imread("4f.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = faceCascade.detectMultiScale(gray)
print(len(faces))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    imgArray = img[y:y+h, x:x+w]
    cv2.imwrite("fac.jpg", imgArray)

cv2.imshow("boy", img)
cv2.waitKey(0)