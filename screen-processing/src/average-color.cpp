#include "../lib/core.hpp"
#include "../lib/highgui.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main() {

  Mat image;
  image = imread("../img/test.png", CV_LOAD_IMAGE_COLOR); // Read the file

  namedWindow("Display window", WINDOW_AUTOSIZE); //Create a window
  imshow("Display window", image);

  waitKey(0);
  return 0;
}
