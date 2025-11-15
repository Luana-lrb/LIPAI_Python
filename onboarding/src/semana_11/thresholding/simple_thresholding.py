import numpy as np
from pathlib import Path
import os
import argparse 
import cv2 

"""
# Simple Thresholding - Limiarização Simples

ap = argparse.ArgumentParser() 
ap.add_argument("-i", "--image", required = True, help = "Path to the image") 
args = vars(ap.parse_args()) 
image = cv2.imread(args["image"]) 
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
blurred = cv2.GaussianBlur(image, (5, 5), 0) 
cv2.imshow("Image", image)
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2. THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)
cv2.imshow("Coins", cv2.bitwise_and(image, image, mask = threshInv)) 
cv2.waitKey(0)

"""
path = r"C:\UFU\IC\onboarding\src\semana_11\thresholding\Original ROI images\healthy"
salvar = r"C:\UFU\IC\onboarding\src\semana_11\thresholding\Processed_healthy"

#Se não existir, criar a pasta
Path(salvar).mkdir(parents=True, exist_ok=True)

for filename in os.listdir(path):
    
    img = cv2.imread(os.path.join(path, filename))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    blurred = cv2.GaussianBlur(gray, (5, 5), 0) 
    
    (T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
    
    (T, threshInv) = cv2.threshold(blurred, 155, 255, cv2. THRESH_BINARY_INV)
    
    result = cv2.bitwise_and(gray, gray, mask = threshInv)
    
    base_name = os.path.splitext(filename)[0]
    cv2.imwrite(os.path.join(salvar, f"{base_name}_original.png"), gray)
    cv2.imwrite(os.path.join(salvar, f"{base_name}_threshold.png"), thresh)
    cv2.imwrite(os.path.join(salvar, f"{base_name}_threshold_inv.png"), threshInv)
    cv2.imwrite(os.path.join(salvar, f"{base_name}_result.png"), result)