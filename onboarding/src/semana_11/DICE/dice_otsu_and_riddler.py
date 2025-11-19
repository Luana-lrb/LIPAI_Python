from pathlib import Path
import os
import cv2 
import metrics_DICE as md
import mahotas as mh

path_images = r"C:\UFU\IC\onboarding\src\semana_11\imagens_e_resultados\Original ROI images\healthy"
path_mask = r"C:\UFU\IC\onboarding\src\semana_11\imagens_e_resultados\Gold_Standard_Semantic_Segmentation\healthy"
output_path = r"C:\UFU\IC\onboarding\src\semana_11\imagens_e_resultados\Results_Combined"

salvar = md.create_metrics(output_path)

for filename in os.listdir(path_images):
    
    img = cv2.imread(os.path.join(path_images, filename))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # vou usar do cv2 para comparar as mascaras
    T_otsu = mh.thresholding.otsu(blurred)
    threshOtsu =  (blurred > T_otsu).astype('uint8') * 255
    threshOtsuInv = (blurred <= T_otsu).astype('uint8') * 255

    T_riddler = mh.thresholding.rc(blurred)
    threshRiddler = (blurred > T_riddler).astype('uint8') * 255
    threshRiddlerInv = (blurred <= T_riddler).astype('uint8') * 255
    
    base = os.path.splitext(filename)[0]
    mask_filename = base + ".png"
    mk_path = os.path.join(path_mask, mask_filename)

    if os.path.exists(mk_path):
        mask = cv2.imread(mk_path, cv2.IMREAD_GRAYSCALE)
        dice = md.dice_coefficient(threshOtsuInv, mask)
        md.add_result(
            metrics=salvar,
            filename=filename,
            method_name="Otsu Threshold",
            dice=dice
        )

        dice_riddler = md.dice_coefficient(threshRiddlerInv, mask)
        md.add_result(
            metrics=salvar,
            filename=filename,
            method_name="Riddler Threshold",
            dice=dice_riddler
        )
md.save_csv(salvar,'otsu_and_riddler_threshold_results.csv')