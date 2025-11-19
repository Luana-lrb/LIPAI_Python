import numpy as np
import pandas as pd
import os
from pathlib import Path

def dice_coefficient(pred, gt):
    """
    Calcula o coeficiente DICE entre predição e ground truth(mascara): DICE = 2 * |A ∩ B| / (|A| + |B|)
    """
    pred = (pred > 0).astype(np.uint8)
    gt = (gt > 0).astype(np.uint8)
  
    intersection = np.sum(pred * gt)
    pred_sum = np.sum(pred)
    gt_sum = np.sum(gt)
  
    if pred_sum + gt_sum == 0:
        return 1.0 if intersection == 0 else 0.0
    
    dice = (2.0 * intersection) / (pred_sum + gt_sum)
    return dice

def create_metrics(output_dir):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    return {
        "output_dir": output_dir,
        "results": []
    }


def add_result(metrics, filename, method_name, dice):
    metrics["results"].append({
        "Filename": filename,
        "Method": method_name,
        "DICE": dice,
    })


def save_csv(metrics, filename='results.csv'):
    if not metrics["results"]:
        return
    
    df = pd.DataFrame(metrics["results"])
    csv_path = os.path.join(metrics["output_dir"], filename)
    df.to_csv(csv_path, index=False)
    return df


def combine_results(csv_files, output_path):
    dfs = []
    
    for csv_file in csv_files:
        if os.path.exists(csv_file):
            df = pd.read_csv(csv_file)
            dfs.append(df)
    
    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)
        combined_df.to_csv(output_path, index=False)
        return combined_df
    else: return None