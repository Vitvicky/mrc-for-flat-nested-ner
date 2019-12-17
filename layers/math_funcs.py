#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 



# Author: Xiaoy LI 
# Last update: 2019.04.30 
# First create: 2019.04.30 
# Description:
# math_funcs used in the pipeline 


import os 
import sys 


root_path = "/".join(os.path.realpath(__file__).split("/")[:-2])
if root_path not in sys.path:
    sys.path.insert(0, root_path)


import math 
import numpy as np 



def sigmoid(x):
    return 1/ (1 + math.exp(-x))



def sigmoid_lst(x):
    return [sigmoid(tmp) for tmp in x]



def sigmoid_batch(x):
    y = []
    for item in x:
        y_sigmoid = sigmoid_lst(item)
        y.append(y_sigmoid)
    return y 


def sigmoid2label(x, threshold=0.5):
    y = sigmoid_batch(x)
    label_lst = []
    for item in y:
        tmp_label = [1 if tmp >= threshold else 0 for tmp in item]
        label_lst.append(tmp_label)
    return label_lst 



if __name__ == "__main__":
    x = 0 
    result = sigmoid(x)
    print("check the result :")
    print(result)
