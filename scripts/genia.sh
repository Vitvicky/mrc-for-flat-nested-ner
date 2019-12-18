#!/usr/bin/env bash
# -*- coding: utf-8 -*-



config_path=mrc-for-flat-nested-ner/configs/eng_large_case_bert.json
base_path=mrc-for-flat-nested-ner
bert_model=/data/nlp/BERT_BASE_DIR/cased_L-12_H-768_A-12
task_name=ner
max_seq_length=150
num_train_epochs=10
warmup_proportion=-1
seed=3306
data_dir=/data/nlp/datasets/genia_ner
data_sign=genia 
checkpoint=304
gradient_accumulation_steps=1
learning_rate=1e-5
train_batch_size=36
dev_batch_size=72
test_batch_size=72
export_model=/data/train_logs/genia
output_dir=${export_model}



CUDA_VISIBLE_DEVICES=3 python3 ${base_path}/run/run_query_ner.py \
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

