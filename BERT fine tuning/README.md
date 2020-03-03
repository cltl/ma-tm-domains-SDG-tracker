You should be able to train the fine tuning model from the terminal by running:

python finetune_on_pregenerated.py --pregenerated_data training/ --bert_model bert-base-uncased --do_lower_case --train_batch_size 16  --output_dir finetuned_lm/ --epochs 2

You can change the batch_size in case of memory errors
