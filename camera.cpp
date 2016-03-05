#include "opencv2\opencv.hpp"

using namespace cv;
int main()
{
    VideoCapture cap(0);
    if (!cap.isOpened())
    {
        return -1;
    }
    Mat frame;
    Mat edges;

    bool stop = false;
    while (!stop)
    {
        cap >> frame;
        //edges = frame;
        cvtColor(frame, edges, CV_BGR2GRAY);
        GaussianBlur(edges, edges, Size(7, 7), 1.5, 1.5);
        Canny(edges, edges, 0, 30, 3);
        imshow("当前视频", edges);
        if (waitKey(1) >= 0)
            stop = true;
    }
    return 0;
}

