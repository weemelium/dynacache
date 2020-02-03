# -*- coding: utf-8 -*-
import cv2
import argparse
import sys
import os
from polygondrawer import PolygonDrawer
import numpy as np
import pyblur

def blurareas(frame, points):
    """
    floute les zones à l'intérieur des polygones
    :param frame: frame
    :param points: list of points 2D
    :return: frame with blur eras
    """
    for pts in points:
        polygon = np.asarray(pts)
        if len(pts) > 0:
            frame = pyblur.BlurContours(frame, [[polygon]], 17, 5)
    return frame

def getimagesfromdir(dirpath):
    """
    Filtre les fichiers images dans un répertoire
    :param dirpath: folder path
    :return: image file names
    """
    imgfiles = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f))]
    for fichier in reversed(imgfiles):
        if not (fichier.endswith((".jpg", ".jpeg", ".png"))):
            imgfiles.remove(fichier)

    return imgfiles

def main():
    parser = argparse.ArgumentParser()
    filetypeparser = parser.add_mutually_exclusive_group(required=True)
    filetypeparser.add_argument("-f", action="store_true", help="if image file")
    filetypeparser.add_argument("-v", action="store_true", help="if video file")
    # filetypeparser.add_argument("-d", action="store_true", help="if folder")
    parser.add_argument("-i", "--fileinput", help="Input video or image file", required=True)
    parser.add_argument("-o", "--fileoutput", help="Output video or image file")
    args = parser.parse_args()

    filetype = ""
    if args.v: #video
        filetype = "v"
    elif args.f:#image file
        filetype = "f"
    # elif args.d:#folder
    #     filetype = "d"

    abspathfileinput = os.path.abspath(args.fileinput)
    if not os.path.isfile(abspathfileinput):
        print("input file not exist!")
        sys.exit()

    fileoutput = args.fileoutput

    absdirpathoutput = ""
    if fileoutput is None:# or not os.path.isfile(fileoutput):
        dirnameinput = os.path.dirname(abspathfileinput)
        basenameinput = os.path.basename(abspathfileinput)
        basenameoutput = "out_" + basenameinput
        absdirpathoutput = os.path.join(dirnameinput, basenameoutput)
        print(abspathfileinput)
    else:
        absdirpathoutput = os.path.abspath(fileoutput)


    if filetype == "v":
        #Capture et get width/height/fps
        cap = cv2.VideoCapture(abspathfileinput)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # float
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # float
        fps = int(cap.get(cv2.CAP_PROP_FPS))

        #video out
        #fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        outvideo = cv2.VideoWriter(absdirpathoutput, 0x00000020, fps, (width, height))

        if not cap.isOpened():
            print("Not video file format")
            sys.exit()

        while (cap.isOpened()):
            ret, frame = cap.read()

            #affichage de l'image pour tracage du polygone
            if 'pd' not in locals():
                pd = PolygonDrawer(frame)

            #blur
            out = blurareas(frame, pd.points)

            outvideo.write(cv2.convertScaleAbs(out))
            cv2.imshow("frame", cv2.convertScaleAbs(out))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                outvideo.release()
                cv2.destroyAllWindows()
                sys.exit()

        cap.release()
        outvideo.release()
        cv2.destroyAllWindows()

    else:
        img = cv2.imread(abspathfileinput)
        if img is None:
            print("Not image file format")
            sys.exit()

        # affichage de l'image pour tracage du polygone
        if 'pd' not in locals():
            pd = PolygonDrawer(img)

        out = blurareas(img, pd.points)
        cv2.imwrite(absdirpathoutput, cv2.convertScaleAbs(out))
        cv2.imshow("image", cv2.convertScaleAbs(out))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()