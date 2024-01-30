import torch
import os
from transformers import Seq2SeqTrainingArguments, Seq2SeqTrainer, DataCollatorForSeq2Seq, AutoTokenizer, AutoModelForSeq2SeqLM 
from datasets import load_from_disk
from mlopsProject.entity import ModelTrainerConfig


class ModelTrainer:
    
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer = tokenizer, model = model, label_pad_token_id=-100, pad_to_multiple_of=8)
        trainer_args = Seq2SeqTrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_eval_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            predict_with_generate=self.config.predict_with_generate
            
        )

        tokenized_data = load_from_disk(self.config.data_path)

        trainer = Seq2SeqTrainer(
            model = model,
            args = trainer_args,
            tokenizer = tokenizer,
            data_collator = seq2seq_data_collator,
            train_dataset = tokenized_data["train"],
            eval_dataset = tokenized_data["validation"].shuffle(seed=42).select(range(self.config.eval_dataset_dimension))
        )

        trainer.train()

        model.save_pretrained(os.path.join(self.config.root_dir,"trainer_model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"trainer_tokenizer"))
