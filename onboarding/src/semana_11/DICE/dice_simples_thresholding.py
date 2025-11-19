from pathlib import Path
import os
import cv2
from sklearn import metrics 
import metrics_DICE as md

path = r"C:\UFU\IC\onboarding\src\semana_11\imagens_e_resultados\Original ROI images\healthy"
path_mask = r"C:\UFU\IC\onboarding\src\semana_11\imagens_e_resultados\Gold_Standard_Semantic_Segmentation\healthy"
output_path = r"C:\UFU\IC\onboarding\src\semana_11\imagens_e_resultados\Results_Combined"

salvar = md.create_metrics(output_path)

for filename in os.listdir(path):
    
    img = cv2.imread(os.path.join(path, filename))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    blurred = cv2.GaussianBlur(gray, (5, 5), 0) 
    
    (T, threshInv) = cv2.threshold(blurred, 155, 255, cv2. THRESH_BINARY_INV)
   
    base = os.path.splitext(filename)[0]
    mask_filename = base + ".png"
    mk_path = os.path.join(path_mask, mask_filename)

    if os.path.exists(mk_path):
        mask = cv2.imread(mk_path, cv2.IMREAD_GRAYSCALE)
        dice = md.dice_coefficient(threshInv, mask)
        md.add_result(
            metrics=salvar,
            filename=filename,
            method_name="Simple Threshold",
            dice=dice,
        )

md.save_csv(salvar,'simple_threshold_results.csv')