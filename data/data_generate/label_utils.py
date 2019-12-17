#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 



# Author: Xiaoy LI 
# Last update: 2019.04.23 
# First create: 2019.02.03 
# Description:
# utilies for sequence tagging tasks 
# for entity-level tasks
# (such as: NER)



import os 
import sys 


root_path = "/".join(os.path.realpath(__file__).split("/")[:-3])
print("check the root_path :")
print(root_path)
if root_path not in sys.path:
    sys.path.insert(0, root_path)



def get_bmes(span_labels, length, encoding):
    tags = ["O" for _ in range(length)] 
    
    for start, end in span_labels:
        for i in range(start, end+1):
            tags[i] = "M" 
        if "E" in encoding:
            tags[end] = "E"
        if "B" in encoding:
            tags[start] = "B" 
        if "S" in encoding and start == end:
            tags[start] = "S"
    return tags 



def get_span_labels(sentence_tags, inv_label_mapping=None):
    """
    Desc:
        get from token_level labels to list of entities, 
        It DOESNOT matter tagging scheme is BMES or BIO or BIOUS 
    Return:
        a list of entities 
        [(start, end, labels), (start, end, labels)]
    """

    if inv_label_mapping:
        sentence_tags = [inv_label_mapping[i] for i in sentence_tags]

    span_labels = []
    last = "O"
    start = -1 
    for i, tag in enumerate(sentence_tags):
        pos, _ = (None, "O") if tag == "O" else tag.split("-")
        if (pos == "S" or pos == "B" or tag == "O") and last != "O":
            span_labels.append((start, i - 1, last.split("-")[-1]))
        if pos == "B" or pos == "S" or last == "O":
            start = i 
        last = tag 
    if sentence_tags[-1] != "O":
        span_labels.append((start, len(sentence_tags) - 1, 
            sentence_tags[-1].split("-")[-1]))

    return span_labels 



def get_tags(span_labels, length, encoding):
    """
    Desc:
        convert a list of entities to token-level labels based on the provided 
        encoding: (e.g.: BMOES)
        PLEASE notice that the left and right boundaries are involved. 
    """
    tags = ["O" for _ in range(length)]

    for start, end, tag in span_labels:
        for i in range(start, end + 1):
            tags[i] = "M-" + tag

        if "E" in encoding:
            tags[end] = "E-" + tag 
        if "B" in encoding:
            tags[start] = "B-" + tag  
        if "S" in encoding and start == end:
            tags[start] = "S-" + tag 
    return tags  



def iob_iobes(tags):
    """
    Desc:
        IOB -> IOBES
    """
    new_tags = []
    for i, tag in enumerate(tags):
        if tag == "O":
            new_tags.append(tag)
        elif tag.split("-")[0] == "B":
            if i + 1 != len(tags) and tags[i+1].split("-")[0] == "I":
                new_tags.append(tag)
            else:
                new_tags.append(tag.replace("B-", "S-"))
        elif tag.split("-")[0] == "I":
            if i + 1 < len(tags) and tags[i + 1].split("-")[0] == "I":
                new_tags.append(tag)
            else:
                new_tags.append(tag.replace("I-", "E-"))
        else:
            raise Exception("invalid IOB format !!")
    return new_tags 


if __name__ == "__main__":
    label_tags = ["O", "B-ORG", "M-ORG", "E-ORG", "O", "B-PER", "M-PER", "E-PER", "O"]
    span_labels = get_span_labels(label_tags, )
    print("check the content of span_labels")
    print(span_labels)
    # [(1, 2, "ORG"), (5, 7, "PER")]

    # -------------------------------------------------------
    # the output former step can used to produce the labeling result 
    # --------------------------------------------------------
    print("-*-"*10)
    print("check the content of producing tags : ")
    span_label = get_tags([(1, 3, "ORG"), (8, 10, "PER")], 20, "BIOES")
    print(span_label)
