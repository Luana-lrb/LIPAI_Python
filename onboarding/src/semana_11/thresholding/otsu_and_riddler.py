from __future__ import print_function
import cv2
import numpy as np
import argparse
import os
from pathlib import Path
import mahotas as mt
"""
# Otsu's and Riddler's Thresholding - Limiarização de Otsu e Riddler

ap = argparse.ArgumentParser() 
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args()) 
image = cv2.imread(args["image"]) 
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
blurred = cv2.GaussianBlur(image, (5, 5), 0) 
cv2.imshow("Image", image) 
T = mt.thresholding.otsu(blurred) 
print("Otsu’s threshold: {}".format(T))
thresh = image.copy() 
thresh[thresh > T] = 255
thresh[thresh < 255] = 0 
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh) 
T = mt.thresholding.rc(blurred)
print("Riddler-Calvard: {}".format(T))
thresh = image.copy()
thresh[thresh > T] = 255 
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh) 
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)
"""
path = r"C:\UFU\IC\onboarding\src\semana_11\imagens_e_resultados\Original ROI images\healthy"
salvar = r"C:\UFU\IC\onboarding\src\semana_11\imagens_e_resultados\Processed_healthy_otsu_riddler"

#Se não existir, criar a pasta
Path(salvar).mkdir(parents=True, exist_ok=True)

for filename in os.listdir(path):
    
    img = cv2.imread(os.path.join(path, filename))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    blurred = cv2.GaussianBlur(gray, (5, 5), 0) 
    
    T = mt.thresholding.otsu(blurred) 
    threshOtsu = gray.copy() 
    threshOtsu[threshOtsu > T] = 255
    threshOtsu[threshOtsu < 255] = 0 
    threshOtsu = cv2.bitwise_not(threshOtsu)
    
    T = mt.thresholding.rc(blurred)
    threshRiddler = gray.copy()
    threshRiddler[threshRiddler > T] = 255 
    threshRiddler[threshRiddler < 255] = 0
    threshRiddler = cv2.bitwise_not(threshRiddler) 
    
    base_name = os.path.splitext(filename)[0]
    cv2.imwrite(os.path.join(salvar, f"{base_name}_original.png"), gray)
    cv2.imwrite(os.path.join(salvar, f"{base_name}_otsu.png"), threshOtsu)
    cv2.imwrite(os.path.join(salvar, f"{base_name}_riddler.png"), threshRiddler)
    