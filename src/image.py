import cv2, cvzone, math
from ultralytics import YOLO

def testImages():
    model = YOLO("../src/yolov8m_custom.pt")
    classNames = ["Howl", "Munchie"]

    fileName = input("File name: ")
    img = cv2.imread(r"./testImages/" + fileName)
    results = model(img, stream=True, conf = 0.7)

    for i in results:
        boxes = i.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            w, h = x2-x1, y2-y1
            cvzone.cornerRect(img, (x1,y1,w,h))
            conf = math.ceil(box.conf[0]*100)/100

            cls = int(box.cls[0])
                
            currentclass = classNames[cls]

            cvzone.putTextRect(img,f"{currentclass} {conf}",(max(0,x1), max(35,y1)), scale=1, thickness=1, offset=3)
        cv2.imshow(fileName, img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()