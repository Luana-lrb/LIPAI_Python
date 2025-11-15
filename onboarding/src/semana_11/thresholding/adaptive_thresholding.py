import numpy as np
import argparse
import cv2
from pathlib import Path
import os

"""
# Adaptive Thresholding - Limiarização Adaptativa

ap = argparse.ArgumentParser() 
ap.add_argument("-i", "--image", required = True,  help = "Path to the image") 
args = vars(ap.parse_args()) 
image = cv2.imread(args["image"]) 
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
blurred = cv2.GaussianBlur(image, (5, 5), 0) 
cv2.imshow("Image", image) 
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4) 
cv2.imshow("Mean Thresh", thresh) 
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3) 
cv2.imshow("Gaussian Thresh", thresh)
cv2.waitKey(0)

"""
path = r"C:\UFU\IC\onboarding\src\semana_11\thresholding\Original ROI images\healthy"
salvar = r"C:\UFU\IC\onboarding\src\semana_11\thresholding\Processed_healthy_adaptive"

#Se não existir, criar a pasta
Path(salvar).mkdir(parents=True, exist_ok=True)

for filename in os.listdir(path):
    
    img = cv2.imread(os.path.join(path, filename))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    blurred = cv2.GaussianBlur(gray, (5, 5), 0) 
    
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
    threshGaussian = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
    
    base_name = os.path.splitext(filename)[0]
    cv2.imwrite(os.path.join(salvar, f"{base_name}_original.png"), gray)
    cv2.imwrite(os.path.join(salvar, f"{base_name}_mean_adaptive.png"), thresh)
    cv2.imwrite(os.path.join(salvar, f"{base_name}_gaussian_adaptive.png"), threshGaussian)
    