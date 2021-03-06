import numpy as np
from sklearn.metrics import roc_auc_score
import math
# y_true = np.array([0, 0, 1, 1])
# y_scores = np.array([0.1, 0.4, 0.35, 0.8])
# roc_auc_score(y_true, y_scores)
# 0.75
def calculatePrecision(tp, fp):

    return float(tp)/(float(tp) + float(fp))


def calculateRecall(tp, fn):

    return float(tp)/(float(tp) + float(fn))


def calculateF1Score(tp, fp, fn):
    precision = calculatePrecision(tp, fp)
    recall = calculateRecall(tp, fn)

    return (2.0*precision*recall)/(precision+recall)


def calculateAccuracy(tp, fp, tn, fn):
    return (float(tp) + float(tn)) / (float(tp) + float(fp) + float(tn) + float(fn))

def calculateMCC(tp, fp, tn, fn):

    return (tp * tn - fp * fn) / (math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)))
