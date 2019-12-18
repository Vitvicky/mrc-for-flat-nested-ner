#!/usr/bin/env bash 
# -*- coding: utf-8 -*- 



config_path=mrc-for-flat-nested-ner/configs/zh_bert.json
data_dir=/data/nfsdata2/xiaoya/data_repo/query_ner/msra
base_path=/home/lixiaoya/query_ner
bert_model=/data/nfsdata/nlp/BERT_BASE_DIR/chinese_L-12_H-768_A-12
task_name=ner
max_seq_length=150
train_batch_size=36
dev_batch_size=72
test_batch_size=72
checkpoint=1300
learning_rate=1e-5
num_train_epochs=5
warmup_proportion=-1
seed=3306
export_model=/data/train_logs/msra_output_bs${train_batch_size}_lr${learning_rate}_epochs${num_train_epochs}_pos512_gpu6
output_dir=${export_model}
data_sign=msra
gradient_accumulation_steps=1


python3 ${base_path}/run/run_query_ner.py \
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
