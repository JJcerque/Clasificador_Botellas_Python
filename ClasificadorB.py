#importar librerias

import torch
import cv2
import numpy  as np
import serial, time

#leer modelo

# model = torch.hub.load('ultralytics/yolov5', 'custom',
#                        path = 'C:/Users/NITRO 5/Desktop/Vid/Modelo/P1yolov5x.pt' )

model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path = 'C:/Users/NITRO 5/Desktop/Clasificador/Modelo/Classifitor.pt')

#video capture
cap = cv2.VideoCapture(1)

while True:
    #lectura
    ret, frame = cap.read()

    #detecciones
    
    detect = model(frame)
    
    #FPS  
    Conteo = detect.pandas().xyxy[0].to_dict(orient='records')
    
    if len(Conteo) != 0:
        for result in Conteo:
            conf = result['confidence']
            if conf >= 0.60:
                cls = int(result['class'])
                xi = int(result['xmin'])
                yi = int(result['ymin'])
                xf = int(result['xmax'])
                yf = int(result['ymax'])
            
                if cls == 0:
                    print("Plástico")
                    arduino = serial.Serial("COM9", 9600)
                    time.sleep(3)
                    arduino.write(b'P')  #Plastico
                    time.sleep(15)
                    arduino.close()
                if cls == 1:
                    print("Tetrapack")
                    arduino = serial.Serial("COM9", 9600)
                    time.sleep(3)
                    arduino.write(b'T')  #Tetrapack
                    time.sleep(15)
                    arduino.close()

cap.release()
cv2.destroyAllWindows
