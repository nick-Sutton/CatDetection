#yolo task=detect mode=train epochs=200 data=dataset/dataset.yaml model=yolov8m.pt imgsz=640 batch=8

def cam():
    import cv2, cvzone, math
    from ultralytics import YOLO

    cap = cv2.VideoCapture(0)
    cap.set(3,1280)
    cap.set(4,720)
    model = YOLO("../yolov8m_custom.pt")

    classNames = ["Howl", "Munchie"]

    while True:
        rec, frame = cap.read()
        results = model(frame, stream=True, conf = 0.7)

        if not rec:
            "Could not connect to video source"
            exit()
            
        for i in results:
            boxes = i.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                w, h = x2-x1, y2-y1
                cvzone.cornerRect(frame, (x1,y1,w,h))
                conf = math.ceil(box.conf[0]*100)/100

                cls = int(box.cls[0])
                
                currentclass = classNames[cls]
                #if currentclass == "Howl" or currentclass == "Munchie":
                #    cv2.imwrite("img.jpg", frame)

                cvzone.putTextRect(frame,f"{currentclass} {conf}",(max(0,x1), max(35,y1)), scale=1, thickness=1, offset=3)
        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()