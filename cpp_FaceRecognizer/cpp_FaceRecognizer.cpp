#include "opencv2/opencv.hpp"
#include <iostream>

using namespace std;
using namespace cv;

class MainApp {
private:
    string argument, username;

    void detectAndDraw(Mat& img, CascadeClassifier& cascade, double scale)
    {
        vector<Rect> faces, faces2;
        Mat gray, smallImg;

        cvtColor(img, gray, COLOR_BGR2GRAY); // Convert to Gray Scale 
        double fx = 1 / scale;

        // Resize the Grayscale Image  
        resize(gray, smallImg, Size(), fx, fx, INTER_LINEAR);
        equalizeHist(smallImg, smallImg);

        // Detect faces of different sizes using cascade classifier  
        cascade.detectMultiScale(smallImg, faces, 1.1, 2, 0 | CASCADE_SCALE_IMAGE, Size(30, 30));

        // Draw circles around the faces 
        for (size_t i = 0; i < faces.size(); i++) {
            Rect r = faces[i];
            Scalar color = Scalar(0, 255, 0);
            rectangle(img, Point(cvRound(r.x * scale), cvRound(r.y * scale)), Point(cvRound((r.x + r.width - 1) * scale), cvRound((r.y + r.height - 1) * scale)), color, 3, 8, 0);
        }

        // Show Processed Image with detected faces 
        imshow("Face Detection", img);
    }

public:
    int CaptureVideo() {
        // Create a VideoCapture object and use camera to capture the video
        VideoCapture cap(0);

        // Check if camera opened successfully
        if (!cap.isOpened())
        {
            cout << "Error opening video stream" << endl;
            return -1;
        }

        // Default resolution of the frame is obtained.The default resolution is system dependent. 
        int frame_width = cap.get(CAP_PROP_FRAME_WIDTH);
        int frame_height = cap.get(CAP_PROP_FRAME_HEIGHT);

        // Define the codec and create VideoWriter object.The output is stored in 'outcpp.avi' file. 
        string filename = getUser() + ".avi";
        VideoWriter video(filename, VideoWriter::fourcc('M', 'J', 'P', 'G'), 10, Size(frame_width, frame_height));
        while (1)
        {
            Mat frame;

            // Capture frame-by-frame 
            cap >> frame;

            // If the frame is empty, break immediately
            if (frame.empty())
                break;

            // Write the frame into the file 'outcpp.avi'
            video.write(frame);

            // Display the resulting frame    
            imshow("Frame", frame);

            // Press  ESC on keyboard to  exit
            char c = (char)waitKey(1);
            if (c == 27)
                break;
        }

        cap.release();
        destroyAllWindows();
    }

    void getArgument() {
        cout << "~widya/AIengineer/Face-App/command: ";
        std::getline(std::cin, argument);
    }

    void WebCam() {
        VideoCapture capture;
        Mat frame, image;
        // PreDefined trained XML classifiers with facial features 
        CascadeClassifier cascade;
        double scale = 1;
        // Change path before execution  
        cascade.load("D:\\codes\\cpp\\cpp_FaceRecognizer\\data\\haarcascade_frontalface_default.xml");
        // Start Video..1) 0 for WebCam 2) "Path to Video" for a Local Video 
        capture.open(0);
        if (capture.isOpened())
        {
            // Capture frames from video and detect faces 
            cout << "Face Detection Started...." << endl;
            while (1)
            {
                capture >> frame;
                if (frame.empty())
                    break;
                Mat frame1 = frame.clone();
                detectAndDraw(frame1, cascade, scale);
                char c = (char)waitKey(10);

                // Press q to exit from window 
                if (c == 27 || c == 'q' || c == 'Q')
                    break;
            }
        }
        // Closes all the frames
        capture.release();
        destroyAllWindows();
    }

    void execute_Argument() {
        if (argument == "capture") { CaptureVideo(); }
        if (argument == "webcam") { WebCam(); }
        if (argument == "get-user") { getUser(); }
    }

    string getUser() {
        std::getline(std::cin, username);
        return username;
    }

    void print() {
        cout << argument << endl;
    }
};

int main(int argc, char** argv)
{
    cout << "  WIDYA AI ENGINEER - REIZKIAN YESAYA .R" << endl;
    cout << "  ********* 2 september 2020  **********" << endl;
    cout << "" << endl;

    while (1) {
        MainApp face;
        face.getArgument();
        face.execute_Argument();
    }
}