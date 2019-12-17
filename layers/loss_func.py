#!/usr/bin/env python3
# -*- coding: utf-8 -*- 



# Author: Xiaoy LI 
# Last update: 2019.03.23 
# First create: 2019.03.23 
# Description:
# loss_funcs_examples.py



import os 
import sys 
import numpy as np 



root_path = "/".join(os.path.realpath(__file__).split("/")[:-2])
if root_path not in sys.path:
    sys.path.insert(0, root_path)



import torch 
import torch.nn as nn 
from torch.nn import BCEWithLogitsLoss




def entity_span_loss_fct(start_logits, end_logits, span_embedding=None, span_match=None):
    """
    Args:
        start_logits: [batch_size, sequence_length, hidden_size]
        end_logits: [batch_size, sequence_length, hidden_size]
    Desc:
    """
    _, start_entity_mask = start_logits.max(-1)
    _, end_entity_mask = end_logits.max(-1)
    span_loss_fct = nn.CrossEntropyLoss()
    if span_embedding is None:
        span_loss = span_loss_fct(start_logits.view(-1, 2), start_positions.view(-1)) + span_loss_fct(start_logits.view(-1, 2), start_positions.view(-1))
    else:
        entity_span_logits = torch.concat(start_logits.view(-1, 2), end_logtis.view(-1, 2))
        span_loss = span_loss_fct(entity_span_logits, span_match)

    return span_loss


def nll_loss():
    # input size if N x C = 3 x 5 
    input = torch.randn(3, 5, requires_grad=True)
    # each element in target has to have 0 <= value < C 
    target = torch.tensor([1, 0, 4])
    output = F.nll_loss(F.log_softmax(input), target)
    output.backward()



def cross_entropy_loss():
    # loss 
    loss = nn.CrossEntropyLoss()
    input = torch.randn(3, 5, requires_grad=True)
    target = torch.empty(3, dtype=torch.long).random_(5)
    output = loss(input, target)
    output.backward()


def bce_logits_loss():
    """
    Desc:
        Input: math. (N, *) where * means, any number of additional dimensions 
        Target: math, (N, *) where the same shape as the input. 
    """
    loss = nn.BCEWithLogitsLoss()
    input = torch.randn(3, requires_grad=True)
    target = torch.empty(3).random_(2)
    output = loss(input, target)
    output.backward()
