#!/usr/bin/env bash
# -*- coding: utf-8 -*-



base_path=mrc-for-flat-nested-ner
config_path=mrc-for-flat-nested-ner/configs/zh_bert.json
bert_model=/data/nlp/BERT_BASE_DIR/chinese_L-12_H-768_A-12
task_name=ner
max_seq_length=150
num_train_epochs=10
warmup_proportion=-1
seed=3306
data_dir=/data/zh_onto
data_sign=zh_onto  
checkpoint=400
gradient_accumulation_steps=1
learning_rate=6e-6
train_batch_size=36
dev_batch_size=72
test_batch_size=72
export_model=/data/train_logs/zhonto_${data_dir}_new2_0.5data_gpu12
output_dir=${export_model}



CUDA_VISIBLE_DEVICES=0 python3 ${base_path}/run/run_query_ner.py \
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
--gradient_accumulation_steps ${gradient_accumulation_steps} \
--allow_impossible=1 