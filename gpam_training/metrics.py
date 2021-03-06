import numpy as np
from sklearn.metrics import classification_report, accuracy_score, \
                            f1_score, precision_score, recall_score, hamming_loss, \
                            jaccard_score


def hit_one(y_true, y_pred):
    score = []
    for pred, true in zip(y_pred, y_true):
        indexes = np.where(true == 1)
        if (pred[indexes] == true[indexes]).any():
            score.append(1)
        else:
            score.append(0)
    return sum(score) / len(score)

def mistake_one(y_true, y_pred):
    score = []
    for pred, true in zip(y_pred, y_true):
        indexes = np.where(true == 0)
        if (pred[indexes] != true[indexes]).any():
            score.append(1)
        else:
            score.append(0)
    return sum(score) / len(score)

def true_positive(y_true, y_pred):
    score = []
    for pred, true in zip(y_pred, y_true):
        indexes = np.where(true == 1)
        correct = sum(pred[indexes] == true[indexes].any())
        number_of_positives = len(true[indexes])
        if number_of_positives:
            score.append(correct / len(true[indexes]))
    return sum(score)/ len(score)

def true_negative(y_true, y_pred):
    score = []
    for pred, true in zip(y_pred, y_true):
        indexes = np.where(true == 0)
        correct = sum(pred[indexes] == true[indexes].any())
        number_of_positives = len(true[indexes])
        if number_of_positives:
            score.append(correct / len(true[indexes]))
    return sum(score)/ len(score)

def false_positive(y_true, y_pred):
    score = []
    for pred, true in zip(y_pred, y_true):
        indexes = np.where(true == 0)
        wrong = sum(pred[indexes] != true[indexes].any())
        number_of_negatives = len(true[indexes])
        if number_of_negatives:
            score.append(wrong / number_of_negatives)
        else:
            score.append(0)
    return sum(score) / len(score)

def false_negative(y_true, y_pred):
    score = []
    for pred, true in zip(y_pred, y_true):
        indexes = np.where(true == 1)
        wrong = sum(pred[indexes] != true[indexes].any())
        number_of_negatives = len(true[indexes])
        if number_of_negatives:
            score.append(wrong / number_of_negatives)
        else:
            score.append(0)
    return sum(score) / len(score)

def get_multilabel_metrics(y_test, y_pred_pac):
    one_hit = hit_one(y_test.values,y_pred_pac)
    one_mistake = mistake_one(y_test.values, y_pred_pac)
    tp = true_positive(y_test.values, y_pred_pac)
    fp = false_positive(y_test.values, y_pred_pac)
    tn = true_negative(y_test.values, y_pred_pac)
    fn = false_negative(y_test.values, y_pred_pac)
    hm = hamming_loss(y_test, y_pred_pac)
    print('Métricas para Passive Agressive Classifier:\n')
    print("Pelo menos uma verdadeiro positivo: {}".format(one_hit))
    print("Pelo menos um falso positivo: {}".format(one_mistake))
    print("True positives: {}".format(tp))
    print("False positives: {}".format(fp))
    print("True negatives: {}".format(tn))
    print("False negatives: {}".format(fn))
    print('Hamming loss:', hm)


    return {'One hit': one_hit, 'One mistake': one_mistake, 'TP': tp, 'FP': fp, 'TN':tn, 'FN':fn, 'HL': hm}
