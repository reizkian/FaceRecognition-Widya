import cv2
import pickle

"""
REALTIME PREDICTION ON OPENED WEB CAM
"""

def predict():
        cascade_path = './data/haarcascade_frontalface_default.xml'
        face_cascade = cv2.CascadeClassifier(cascade_path)
        # trained recognizer
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('./data/trainer.yml')
        print("recognizer has been loaded")
        # load label
        label ={"person_name":1}
        with open('./data/labels.pickle', 'rb') as f:
            og_label = pickle.load(f)
            label = {v:k for k,v in og_label.items()}
        captureVideo = cv2.VideoCapture(0)
        while(True):
            # capture video frame by frame
            ret, frame = captureVideo.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,
                                                scaleFactor= 1.5,
                                                minNeighbors=5)
            for (x,y,w,h) in faces:
                # identifying region of interest (ROI)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                # predict using trained recognizer
                id_, conf = recognizer.predict(roi_gray)
                print(label[id_], "confidence:",conf, "  ", "position:",x, y, w, h,)
                # put text
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = label[id_]
                color = (0,255,0)
                stroke = 2
                cv2.putText(frame, name, (x,y-15), font, 1, color, stroke, cv2.LINE_AA)
                # rectangle mark
                color = (0,255,0)
                stroke = 2
                cv2.rectangle(frame, (x,y), (x+w,y+h), color, stroke)
            # display resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        captureVideo.release()
        cv2.destroyAllWindows()