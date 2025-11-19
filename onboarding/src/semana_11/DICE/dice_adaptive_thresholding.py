from pathlib import Path
import os
import cv2
from torch import mean 
import metrics_DICE as md

path_images = r"C:\UFU\IC\onboarding\src\semana_11\imagens_e_resultados\Original ROI images\healthy"
path_mask = r"C:\UFU\IC\onboarding\src\semana_11\imagens_e_resultados\Gold_Standard_Semantic_Segmentation\healthy"
output_path = r"C:\UFU\IC\onboarding\src\semana_11\imagens_e_resultados\Results_Combined"

salvar = md.create_metrics(output_path)

for filename in os.listdir(path_images):
    
    img = cv2.imread(os.path.join(path_images, filename))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    threshMean = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                        cv2.THRESH_BINARY_INV, 11, 4)
    threshGaussian = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY_INV, 15, 3)
    
    base = os.path.splitext(filename)[0]
    mask_filename = base + ".png"
    mk_path = os.path.join(path_mask, mask_filename)

    if os.path.exists(mk_path):
        mask = cv2.imread(mk_path, cv2.IMREAD_GRAYSCALE)
        dice = md.dice_coefficient(threshGaussian, mask)
        md.add_result(
            metrics=salvar,
            filename=filename,
            method_name="Adaptive Threshold Gaussian",
            dice=dice,
        )
        mean_dice = md.dice_coefficient(threshMean, mask)
        md.add_result(
            metrics=salvar,
            filename=filename,
            method_name="Adaptive Threshold Mean",
            dice=mean_dice,
        )
        
        
md.save_csv(salvar,'adaptive_threshold_results.csv')