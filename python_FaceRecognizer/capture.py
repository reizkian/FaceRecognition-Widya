import cv2
import os
"""
capture.py files contain CapImages and CapVid method.
capture data set in images file and video files.
"""
def CapImages(name):
    # create directory to save file
    path = "./user/images/"+name
    num_of_images = 0
    detector = cv2.CascadeClassifier("./data/haarcascade_frontalface_default.xml")
    try:
        os.makedirs(path)
    except:
        print('Directory Already Created')
    vid = cv2.VideoCapture(0)
    # color
    red = (0,0,255)
    green = (0,255,0)
    blue = (255,0,0)
    white = (255,255,255)
    black = (0,0,0)
    while True: # detect face, if true save the image
        ret, img = vid.read()
        new_img = None
        clear_img = img.copy()
        grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = detector.detectMultiScale(image=grayimg, scaleFactor=1.1, minNeighbors=5)
        for x, y, w, h in face: #draw rectangle for detected face
            cv2.rectangle(img, (x, y), (x+w, y+h), black, 2)
            cv2.putText(img, "Face Detected", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, red, 2, cv2.LINE_AA)
            cv2.putText(img, str(str(num_of_images)+" images captured"), (x, y+h+25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, red, 2, cv2.LINE_AA)
            new_img = img[y:y+h, x:x+w]
        cv2.imshow("Press 'Q' to quit", img)
        key = cv2.waitKey(1) & 0xFF
        try : # saving the images
            cv2.imwrite(str(path+"/"+"image_"+str(num_of_images)+name+".jpg"), clear_img)
            num_of_images += 1
        except :
            pass
        if key == ord("q") or key == 27 or num_of_images > 300:
            break
    cv2.destroyAllWindows()

def CapVideo(name): 
    # make directory for video file
    path_dir = "./user/videos/"+name
    path_vid = path_dir +"/"+ name + ".mp4"
    try:
        os.makedirs(path_dir)
    except:
        print('Directory Already Created')
    vid = cv2.VideoCapture(0)
    video = cv2.VideoCapture(0) 
    # check if camera opened
    if (video.isOpened() == False):  
        print("Error reading video file") 
    #setup
    frame_width = int(video.get(3)) 
    frame_height = int(video.get(4)) 
    size = (frame_width, frame_height) 
    result = cv2.VideoWriter(path_vid,  
                            cv2.VideoWriter_fourcc(*'MJPG'), 
                            10, size)         
    while(True): 
        ret, frame = video.read() 
        if ret == True:  
            result.write(frame) 
            cv2.imshow('Press "S" to stop capture video', frame) 
            # Press S on keyboard  
            # to stop the process 
            if cv2.waitKey(1) & 0xFF == ord('s'): 
                break
        # Break the loop 
        else: 
            break
    video.release() 
    result.release()    
    cv2.destroyAllWindows() 
    print("The video was successfully saved")
    # frame extraction from video
    try:
        vidcap = cv2.VideoCapture("./user/videos/"+name+"/"+name+".mp4")
    except:
        print("cannot read video dir")
    def getFrame(sec):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcap.read()
        if hasFrames:
            try:
                os.makedirs("./user/images/"+name)
            except:
                cv2.imwrite("./user/images/"+name+"/"+"vid_"+str(count)+name+".jpg", image)  # save frame as JPG file   
        return hasFrames
    sec = 0
    frameRate = 1 
    count=1
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec) 