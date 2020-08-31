import os
from PIL import Image
import numpy as np
import cv2
import pickle

"""
TRAIN IMAGES DATASET FROM DIRECTORY
1) OS walk searching for images
2) transform images data to tensor array, folder names as label (x_train,y_label)
3) save label dictionarry
4) train recognizer
5) save recognizer
"""

def TrainImages():
    # 1) OS walk
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR,'user\images')
    cascade_path = 'data/haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    current_id = 0
    label_ids = {}
    x_train = []
    y_labels = []
    filecsv = open("path.csv","w")
    number_of_images_data = 1
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpeg") or file.endswith("jpg"):
                path = os.path.join(root,file)
                label = os.path.basename(root).replace(" ","-").lower()
                print(number_of_images_data,label, path)
                filecsv.write(path+";"+label+"\n")
                #create label dictionarry
                if label in label_ids:
                    pass
                else:
                    label_ids[label] = current_id
                    current_id += 1
                id_ = label_ids[label]
                pil_image = Image.open(path).convert("L") # turn into grayscale
                image_array = np.array(pil_image, "uint8")
                faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
                # 2) transform images to tensor array
                for (x,y,w,h) in faces:
                    roi = image_array[y:y+h, x:x+w]
                    x_train.append(roi)
                    y_labels.append(id_)
                number_of_images_data += 1
    # 3) save label dictionarry   
    with open('./data/labels.pickle', 'wb') as f:
        pickle.dump(label_ids, f)
    # 4) train recognizer
    recognizer.train(x_train, np.array(y_labels))
    # 5) save recognizer
    recognizer.write("./data/trainer.yml")
    print(label_ids)