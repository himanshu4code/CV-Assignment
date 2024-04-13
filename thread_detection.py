import cv2
import imutils
def mark_thread_intersection(image_path: str) -> None:
    """Method to detect edge and mark intersection of threads

    Args:
        image_path (str): Image path of image file
    """
    color_img = cv2.imread(image_path)
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be read, check with os.path.exists()"
    blurred_img = cv2.GaussianBlur(img, (5, 5), 0) 
    edges = cv2.Canny(blurred_img,100,200)
    cnts = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cv2.imwrite("edges.jpg" ,edges)
    for c in cnts:
        polygon = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)     
        if len(polygon) in {6}:
            print(polygon)
            M = cv2.moments(c)
            if cv2.contourArea(c):
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                image = cv2.circle(color_img, (cX, cY), 1, (0, 0, 255), 2) 
                cv2.imwrite("intersection_image.jpg" ,image)
    
if __name__ == "__main__":
    #TODO Accuracy for detecting intersection via dot is not 100%
    image_path = "weaven_pattern.jpg"
    mark_thread_intersection(image_path)