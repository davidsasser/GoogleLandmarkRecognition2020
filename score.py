from evaluations.kaggle_2020 import global_average_precision_score
import csv

y_true = {}
with open('./input/metadata/landmark-recognition-2020/test.csv', 'r') as f:
    i = 0
    for x in f:
        if(i == 0):
            i += 1
            continue
        y_true[x.split(',')[0]] = int(x.split(',')[1].rstrip())
        i += 1

y_pred = {}
with open('./submission(2).csv', 'r') as f:
    j = 0
    for x in f:
        if(j == 0):
            j += 1
            continue
        y_pred[x.split(',')[0]] = (int(x.split(',')[1].rstrip().split(' ')[
            0]), float(x.split(',')[1].rstrip().split(' ')[1]))
        j += 1

print(global_average_precision_score(y_true, y_pred))
