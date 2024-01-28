import os
from mlopsProject.logging import logger 
from transformers import AutoTokenizer
from datasets import DatasetDict, load_from_disk, concatenate_datasets
from mlopsProject.entity import DataPreprocessingConfig
from mlopsProject.utils.common import read_jsonl_to_dataset

class DataPreprocessing:
    
    def __init__(self,config: DataPreprocessingConfig):
        self.config = config 
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)
    
    def create_DatasetDict(self):
        raw_dataset = DatasetDict({
            "train": read_jsonl_to_dataset(self.config.data_path + "/train.jsonl"),
            "test": read_jsonl_to_dataset(self.config.data_path + "/test.jsonl"),
            "validation": read_jsonl_to_dataset(self.config.data_path + "/validation.jsonl")
            })
        raw_dataset.save_to_disk(self.config.data_path)

    def process(self):
        raw_data = load_from_disk(self.config.data_path)
        tokenized_inputs = concatenate_datasets(
            [raw_data["train"],raw_data["validation"],raw_data["test"]]
            ).map(lambda x: self.tokenizer(x["paragraph"], truncation=True), batched=True, remove_columns=['answers', 'questions', 'paragraph', 'questions_answers'])
        tokenized_targets = concatenate_datasets(
            [raw_data["train"],raw_data["validation"],raw_data["test"]]
            ).map(lambda x: self.tokenizer(x["questions_answers"], truncation=True), batched=True, remove_columns=['answers', 'questions', 'paragraph', 'questions_answers'])

        tok_input_max = max([len(x) for x in tokenized_inputs["input_ids"]])
        tok_target_max = max([len(x) for x in tokenized_targets["input_ids"]])
        
        def preprocess_function(sample,padding = "max_length"):
            
            inputs = ["Generate question and answer: " + item for item in sample["paragraph"]]

            model_inputs = self.tokenizer(inputs, max_length=tok_input_max, padding=padding, truncation=True)

            labels = self.tokenizer(text_target=sample["questions_answers"], max_length=tok_target_max, padding=padding, truncation=True)

            if padding == "max_length":
                labels["input_ids"] = [
                    [(l if l != self.tokenizer.pad_token_id else -100) for l in label] for label in labels["input_ids"]
                ]

            model_inputs["labels"] = labels["input_ids"]
            return model_inputs

        tokenized_dataset = raw_data.map(preprocess_function, batched=True, remove_columns=["paragraph", "questions_answers", "answers","questions"])
        tokenized_dataset.save_to_disk(os.path.join(self.config.root_dir, "tokenized_dataset"))
    