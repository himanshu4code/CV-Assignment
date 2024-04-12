import numpy as np
import cv2



def generate_image(no_of_threads_v: int, 
                   no_of_threads_h: int, 
                   thread_color: tuple, 
                   backgroud_color: tuple, 
                   thread_width: int= 40, 
                   distance_between_thread: int = 30, 
                   shape_of_thread: str="straight", 
                   layout_thread: str="simple"):
    """Method to generate image

    Args:
        no_of_threads_v (int): No. of threads vertical in pattern
        no_of_threads_h (int): No. of threads horizontal in pattern
        thread_color (tuple):  tuple of 3 value for color of thread eg: (0, 255, 255)
        backgroud_color (tuple): tuple of 3 value for color of thread eg: (0, 255, 255)
        thread_width (int):  Thread width
        distance_between_thread (int):  distance between thread
        shape_of_thread (str):  shape of thread straight or simple cubic spline
        layout_thread (str):  Layout of thread simple or simple cubic spline
    """
    columns = no_of_threads_h + (no_of_threads_h + 1)
    rows = no_of_threads_v + (no_of_threads_v + 1)
    width = no_of_threads_h*thread_width + (no_of_threads_h + 1)*distance_between_thread
    height = no_of_threads_v*thread_width + (no_of_threads_v + 1)*distance_between_thread
    pattern = np.zeros((height, width, 3), dtype=np.uint8)
    line_color = (0, 0, 0)

    for i in range(rows):
        index = 0
        for j in range(columns):
            x1 = j * width // columns
            y1 = i * height // rows
            x2 = (j + 1) * width // columns 
            y2 = (i + 1) * height // rows
            if i%2 != 0:
                cv2.rectangle(pattern, (x1, y1), (x2, y2), backgroud_color, -1)
                
                cv2.line(pattern, (x1, y1), (x2, y1), line_color, 1)
                cv2.line(pattern, (x1, y2), (x2, y2), line_color, 2)
                continue
            if (i + j) % 2 == 0:
                cv2.rectangle(pattern, (x1, y1), (x2, y2), thread_color, -1)
            else:
                cv2.rectangle(pattern, (x1, y1), (x2, y2), backgroud_color, -1)

    # Display the pattern
    cv2.imshow('Weave Pattern', pattern)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


no_of_threads_v = 4
no_of_threads_h = 3
thread_color =  (255, 0, 0) 
backgroud_color = (0, 255,255)
generate_image(no_of_threads_h=no_of_threads_h, no_of_threads_v=no_of_threads_v, thread_color=thread_color, backgroud_color=backgroud_color)
