from collections import Counter
from sklearn.cluster import KMeans
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pandas as pd
import pytesseract
import sys
import os

#pip install:
#sklearn
#matplotlib
#tesseract
#opencv-python
#-U scikit-learn

image_name = '/oplab.jpg'
image = cv2.imread(sys.path[0]+f'{image_name}',1)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#plt.imshow(image)


def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        i = int(i)
        hex_color += ("{:02x}".format(i))
    return hex_color

def prep_image(raw_img):
    modified_img = cv2.resize(raw_img, (900, 600), interpolation = cv2.INTER_AREA)
    modified_img = modified_img.reshape(modified_img.shape[0]*modified_img.shape[1], 3)
    return modified_img

def text_extractor(img):
    #pytesseract.pytesseract.tesseract_cmd = r'__YT__/Lib/site-packages/Tesseract-OCR/tesseract.exe'
    #if getattr(sys, 'frozen', False):
    #    _path = os.path.join(sys._MEIPASS, r'__YT__/Lib/site-packages/Tesseract-OCR/tesseract.exe')
    #    print(_path)
    #    pytesseract.pytesseract.tesseract_cmd =_path
    #    # the .exe will look here
    #else:
    #    #print('limit _path')
    #    pytesseract.pytesseract.tesseract_cmd = r"__YT__/Lib/site-packages/Tesseract-OCR/tesseract.exe"
    ##ruta donde se encuentre su tresseract
    config = r'--oem 3 --psm 6'
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

    text_imag = pytesseract.image_to_string(thresh1, config = config)
    global text_image
    text_image = str(text_imag)
    print (f'Texto na imagem: \n{text_image}')
    return text_image

def face_detection(img):
    #while True:
        class_face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = img
        typing = type(gray)
        
        #print(typing)
        
        #colormap = plt.get_cmap('inferno')
        #heatmap = (colormap(gray) * 2**16).astype(np.uint16)[:,:,:3]
        #heatmap = cv2.cvtColor(heatmap, cv2.COLOR_RGB2BGR)
        #cv2.imshow('heatmap', heatmap)
        
        #######################################################
        
        #heatmap = cv2.applyColorMap(gray, cv2.COLORMAP_HOT)
        
        gray1 = cv2.resize(gray1, (img.shape[1], img.shape[0]))
        
        (thresh, gray1) = cv2.threshold(gray1, 127, 255, cv2.THRESH_TOZERO_INV)

        heatmap = cv2.applyColorMap(gray1, cv2.COLORMAP_HOT)
        fin = cv2.addWeighted(heatmap, 0.7, img, 0.3, 0)
        
        #cv2.imshow('heatmap', fin)
        
        detect = class_face.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=8,
                    minSize=(25, 25)
                )
        faces = class_face.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30)
                    #flags = cv2.CV_HAAR_SCALE_IMAGE
                )
        faces_photos = len(faces)
        global faces_photo
        faces_photo = faces_photos
        print("Found {0} faces!".format(faces_photo))

        for(x, y, l, a) in faces:
            cv2.rectangle(gray, (x, y), (x + l, y + a), (255, 0, 0), 2)

            counter = str(faces.shape[0])

            cv2.putText(gray, counter, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.putText(gray, "Face Quantity: " + counter, (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            #cv2.putText(gray, "Face Quantity: " + str(detect.shape[0]), (0, gray.shape[0] - 10),
                        #cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), 1)

        #cv2.imshow("", gray)

        #if cv2.waitKey(1) == ord('f'):
        #    break
        return faces_photo, fin

def color_analysis(img, fin, *args, **kwargs):
    clf = KMeans(n_clusters = 5)
    color_labels = clf.fit_predict(img)
    center_colors = clf.cluster_centers_
    counts = Counter(color_labels)
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]

    colors = []
    for count, hex_color in zip(counts, hex_colors):
        colors.append({'counts':count, 'hex_colors':hex_color, 'bubble_size':count})

    df = pd.DataFrame(colors)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    global text_image
    global faces_photo
    fig.suptitle('Image parse: \n Faces = {} \n Text = {}'.format(faces_photo, text_image))
    plt.figure(figsize = (12, 8))
    countsII = counts.values()
    ax2.imshow(image)
    ax1.imshow(fin)
    #ax1.scatter(
    #    'counts',
    #    'hex_colors',
    #    c = 'hex_colors',
    #    label = f'{hex_colors}',
    #    s='bubble_size',
    #    alpha = 0.5, data=df
    #    )
    ax3.pie(
        'counts',
        labels = 'hex_colors',
        colors = 'hex_colors',
        data=df
        )
    ax4.pie(
        counts.values(),
        labels = hex_colors,
        colors = hex_colors
        )
    pastel = plt.savefig("color_analysis_report.png")
    plt.show()
    print(hex_colors)



modified_image = prep_image(image)
text_image = text_extractor(image)
a,b = face_detection(image)
color_analysis(modified_image, b)