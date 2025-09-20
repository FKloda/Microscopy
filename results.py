
import argparse
import numpy as np
from skimage import io
import csv
from pathlib import Path
import os

def load_binary_mask(path):
    """Read image and convert to boolean mask of non-zero pixels."""
    img = io.imread(path)
    return img > 0

def compute_metrics(gt, pred):
    """
    Compute agreement metrics between two boolean masks.
    Returns a dictionary with Dice, IoU, precision, recall, F1 and counts.
    """
    tp = np.logical_and(gt, pred).sum()
    fp = np.logical_and(~gt, pred).sum()
    fn = np.logical_and(gt, ~pred).sum()
    tn = np.logical_and(~gt, ~pred).sum()

    dice   = 2 * tp / (2 * tp + fp + fn) if (2 * tp + fp + fn) else 1.0
    iou    = tp / (tp + fp + fn)         if (tp + fp + fn) else 1.0
    prec   = tp / (tp + fp)              if (tp + fp) else 1.0
    recall = tp / (tp + fn)              if (tp + fn) else 1.0
    f1     = 2 * prec * recall / (prec + recall) if (prec + recall) else 1.0
    percentage = (tp + tn) / (tp + tn + fp + fn)

    return dict(
        dice=dice,
        iou=iou,
        precision=prec,
        recall=recall,
        f1=f1,
        tp=tp, fp=fp, fn=fn, tn=tn
        ,percentage=percentage
    )

def absoluteFilePaths(directory):
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))

def main():
    predictions = absoluteFilePaths("C:/Skola/Microscopy/testing/predictions")
    masks = absoluteFilePaths("C:/Skola/Microscopy/testing/masks")
    results = []
    out_path = "C:/Skola/Microscopy/testing/results.csv"

    for pred, mask in zip(predictions, masks):
        mask_a = load_binary_mask(mask)
        mask_b = load_binary_mask(pred)

        metrics = compute_metrics(mask_a, mask_b)
        # metrics["name"] = pred.name
        results.append(metrics)

    fieldnames = ["dice", "iou", "precision", "recall", "f1",
                  "tp", "fp", "fn", "tn", "percentage"]
    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            writer.writerow(r)
    #
    # pred = "C:\\Skola\\Microscopy\\testing\\predictions\\IXMtest_A09_s1_w1CE70AD49-290D-4312-82E6-CDC717F32637.tif"
    # mask = "C:\\Skola\\Microscopy\\testing\\masks\\IXMtest_A09_s1_w1CE70AD49-290D-4312-82E6-CDC717F32637.png"
    # mask_a = load_binary_mask(mask)
    # mask_b = load_binary_mask(pred)
    # if mask_a.shape != mask_b.shape:
    #     raise ValueError(
    #         f"Shape mismatch: {mask_a.shape} vs {mask_b.shape}"
    #     )
    #
    # metrics = compute_metrics(mask_a, mask_b)


    # print("\nAgreement metrics between masks")
    # print("--------------------------------")
    # for k, v in metrics.items():
    #     if k in ("tp", "fp", "fn", "tn"):
    #         print(f"{k.upper():>8}: {v}")
    #     else:
    #         print(f"{k.capitalize():>8}: {v:.4f}")

    total_tp = sum(r["tp"] for r in results)
    total_fp = sum(r["fp"] for r in results)
    total_fn = sum(r["fn"] for r in results)

    global_dice = 2 * total_tp / (2 * total_tp + total_fp + total_fn)
    global_iou = total_tp / (total_tp + total_fp + total_fn)
    global_prec = total_tp / (total_tp + total_fp) if (total_tp + total_fp) else 1.0
    global_rec = total_tp / (total_tp + total_fn) if (total_tp + total_fn) else 1.0
    global_f1 = 2 * global_prec * global_rec / (global_prec + global_rec)

    print("\nSummary across all pairs")
    print("------------------------")
    print(f"Dice:      {global_dice:.4f}")
    print(f"IoU:       {global_iou:.4f}")
    print(f"Precision: {global_prec:.4f}")
    print(f"Recall:    {global_rec:.4f}")
    print(f"F1 score:  {global_f1:.4f}")
    print(f"Files processed: {len(results)}")
    print(f"Detailed per-file metrics saved to: {out_path}")

if __name__ == "__main__":
    main()