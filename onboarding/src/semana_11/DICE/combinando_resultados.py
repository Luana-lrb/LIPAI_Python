import pandas as pd
from pathlib import Path
import os
import metrics_DICE as md

output_path = r"C:\UFU\IC\onboarding\src\semana_11\imagens_e_resultados\Results_Combined"

csv_files = [
    os.path.join(output_path, 'simple_threshold_results.csv'),
    os.path.join(output_path, 'adaptive_threshold_results.csv'),
    os.path.join(output_path, 'otsu_and_riddler_threshold_results.csv'),
]

combined_csv = os.path.join(output_path, 'all_methods_combined.csv')

combinado = md.combine_results(csv_files, combined_csv)

best_method = combinado.groupby('Method')['DICE'].mean().idxmax()
best_dice = combinado.groupby('Method')['DICE'].mean().max()
worst_method = combinado.groupby('Method')['DICE'].mean().idxmin()
worst_dice = combinado.groupby('Method')['DICE'].mean().min()

print(f"\nMelhor método (DICE médio):  {best_method} ({best_dice:.4f})")
print(f"Pior método (DICE médio):   {worst_method} ({worst_dice:.4f})")
print(f"Diferença:                   {(best_dice - worst_dice):.4f}")
