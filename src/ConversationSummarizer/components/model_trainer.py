from transformers import Seq2SeqTrainer, Seq2SeqTrainingArguments
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk
from ConversationSummarizer.entity import ModelTrainerConfig
import torch
import os

class ModelTrainer:
    # Initialize the ModelTrainer with a ModelTrainerConfig object
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    # Method to train the model
    def train(self):
        # Determine the device to use for training
        device = "cuda" if torch.cuda.is_available() else "cpu"

        # Load the tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)

        # Create a data collator for sequence-to-sequence models
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        # Load the data for training and evaluation
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # Define the training arguments
        trainer_args = Seq2SeqTrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs, 
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps, 
            save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        ) 

        # Initialize the trainer
        trainer = Seq2SeqTrainer(model=model_pegasus, args=trainer_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=dataset_samsum_pt["train"], 
                  eval_dataset=dataset_samsum_pt["validation"])
        
        # Train the model
        trainer.train()

        # Save the trained model and tokenizer
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))