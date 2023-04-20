import cv2
import numpy as np
# Load the image
baloon_img = cv2.imread('hotairbaloon.jpg')
#convert it into gray scale
gray = cv2.cvtColor(baloon_img, cv2.COLOR_BGR2GRAY)
# Apply Gaussian blur
img_blur = cv2.GaussianBlur(gray, (15, 11), 0)
# apply Canny edge detection
canny_edges = cv2.Canny(img_blur, 50, 150)
# HoughCircles method used to find hot air baloons
det_circle = cv2.HoughCircles(canny_edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=90,
                           param1=100, param2=35, minRadius=70, maxRadius=170)
# Iterate over each circle and draw it on the hotairbaloon with a different color
if det_circle is not None:
    det_circle = np.round(det_circle[0, :]).astype("int")
    for i, (x, y, r) in enumerate(det_circle):
        colors = np.random.randint(0,255,4)
        colors=colors.tolist()
        cv2.circle(baloon_img, (x, y), r, colors, 2)
        cv2.putText(baloon_img, f"{i+1}", (x-r, y-r), cv2.FONT_HERSHEY_SIMPLEX, 1, colors, 2)
# Print the number of detected balloons
print("Number of balloons:", len(det_circle))
# Display the results
cv2.imwrite("Circles.jpg", baloon_img)
cv2.namedWindow("OUTPUT", cv2.WINDOW_NORMAL)
# Resizing the image to fit in the window space
resize = cv2.imread("Circles.jpg")
cv2.imshow("OUTPUT",resize)
cv2.waitKey(0)
cv2.destroyAllWindows()