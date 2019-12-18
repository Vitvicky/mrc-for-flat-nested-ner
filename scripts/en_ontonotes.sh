#!/usr/bin/env bash 
# -*- coding: utf-8 -*- 



config_path=mrc-for-flat-nested-ner/configs/eng_large_case_bert.json
base_path=mrc-for-flat-nested-ner
bert_model=/data/nlp/BERT_BASE_DIR/cased_L-24_H-1024_A-16
task_name=ner
max_seq_length=150
num_train_epochs=4
warmup_proportion=-1
seed=3306
data_dir=/data/data_repo/eng_onto
data_sign=en_onto
checkpoint=28000
gradient_accumulation_steps=4
learning_rate=6e-6
train_batch_size=36
dev_batch_size=72
test_batch_size=72
smooth=2.0
export_model=/data/train_logs/engonto_output_bs${train_batch_size}_lr${learning_rate}_allow_imp_true_smooth${smooth}_gpu12
output_dir=${export_model}



CUDA_VISIBLE_DEVICES=2,3,4 python3 ${base_path}/run/run_query_ner.py \
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
