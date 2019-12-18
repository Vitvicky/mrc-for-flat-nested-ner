#!/usr/bin/env bash
# -*- coding: utf-8 -*-



config_path=mrc-for-flat-nested-ner/configs/eng_large_case_bert.json
base_path=mrc-for-flat-nested-ner
bert_model=/data/nlp/BERT_BASE_DIR/cased_L-24_H-1024_A-16
task_name=ner
max_seq_length=150
num_train_epochs=10
warmup_proportion=-1
seed=3306
data_dir=/data/google_conll03
data_sign=conll03  
checkpoint=900
gradient_accumulation_steps=4
learning_rate=6e-5
train_batch_size=64
dev_batch_size=64
test_batch_size=64
export_model=/data/train_logs/conll03_output_bs${train_batch_size}_lr${learning_rate}_epochs${num_train_epochs}_google_gpu6
output_dir=${export_model}


CUDA_VISIBLE_DEVICES=0,1,2 python3 ${base_path}/run/run_query_ner.py \
--config_path ${config_path} \
--data_dir ${data_dir} \
--bert_model ${bert_model} \
--max_seq_length ${max_seq_length} \
--train_batch_size ${train_batch_size} \
--dev_batch_size ${dev_batch_size} \
--test_batch_size ${test_batch_size} \
--checkpoint ${checkpoint} \
--learning_rate ${learning_rate} \
--num_train_epochs ${num_train_epochs} \
--warmup_proportion ${warmup_proportion} \
--export_model ${export_model} \
--output_dir ${output_dir} \
--data_sign ${data_sign} \
--gradient_accumulation_steps ${gradient_accumulation_steps} 
