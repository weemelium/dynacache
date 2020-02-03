import numpy as np
import cv2


FINAL_LINE_COLOR = (255, 255, 255)
WORKING_LINE_COLOR = (127, 127, 127)

class PolygonDrawer(object):
    """
    Permet de tracer des polygones definissant les zone a exclure des traitements
    """

    def __init__(self, frame):

        self.window_name = 'poly_draw'
        self.done = False
        self.current = (0,0)
        self.points = [[]]
        self.frame = frame
        self.npoly = len(self.points)
        self.new = False
        self.drawpolygon()



    def on_mouse(self, event, x, y, butons, user_param):

        if self.done:
            return

        if event == cv2.EVENT_MOUSEMOVE:
            self.current = (x, y)
        elif event == cv2.EVENT_LBUTTONDOWN:
            self.points[self.npoly - 1].append((x, y))
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.points.append([])
            self.new = True


    def drawpolygon(self):

        cv2.namedWindow(self.window_name, flags=cv2.WINDOW_GUI_NORMAL)
        cv2.imshow(self.window_name, self.frame)
        cv2.waitKey(1)
        cv2.setMouseCallback(self.window_name, self.on_mouse)

        while(not self.done):
            self.new = False
            while(not self.new):

                self.npoly = len(self.points)

                frame = self.frame.copy()

                for pts in self.points:
                    if (len(pts) > 0):
                        # Draw all the current polygon segments
                        cv2.polylines(frame, np.array([pts]), False, FINAL_LINE_COLOR, 2)
                        # And  also show what the current segment would look like
                if len(self.points[self.npoly-1]) > 0 :
                    cv2.line(frame, self.points[self.npoly-1][-1], self.current, WORKING_LINE_COLOR)

                cv2.imshow(self.window_name, frame)
                ch = 0xFF & cv2.waitKey(50)

                if ch in [97, 133, 27]:
                    self.new = True
                    self.done = True
        cv2.destroyWindow(self.window_name)

    def fillpoly(self, frame):

        for pts in self.points:
            if len(pts) > 0:
                cv2.fillPoly(frame, np.array([pts]), 0)

        return frame


