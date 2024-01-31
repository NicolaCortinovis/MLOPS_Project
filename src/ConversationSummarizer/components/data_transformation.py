import os
from transformers import AutoTokenizer
from datasets import load_from_disk
from ConversationSummarizer.logging import logger
from ConversationSummarizer.entity import DataTransformationConfig
from ConversationSummarizer.constants import MAX_INPUT_LENGTH, MAX_TARGET_LENGTH

class DataTransformation:
    
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        # Load the tokenizer from the pretrained model specified in the config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)
    
    
    def convert_examples_to_features(self,example_batch):
        """
        Convert a batch of examples to model features.

        Args:
            example_batch: A batch of examples.
                Each example is a dictionary with 'dialogue' and 'summary' keys.

        Returns:
            Dict: A dictionary with keys 'input_ids', 'attention_mask', and 'labels'.
                Each value is a list of tokenized inputs.

        Raises:
            ValueError: If 'dialogue' or 'summary' keys are not in example_batch.
        """
        if 'dialogue' not in example_batch or 'summary' not in example_batch:
            raise ValueError("'dialogue' and 'summary' keys must be in example_batch")

        # Tokenize the 'dialogue' field of each example in the batch.
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length = MAX_INPUT_LENGTH, truncation=True)

        # Use the tokenizer as a target tokenizer.
        with self.tokenizer.as_target_tokenizer():
            # Tokenize the 'summary' field of each example in the batch.
            target_encodings = self.tokenizer(example_batch['summary'], max_length = MAX_TARGET_LENGTH, truncation=True)

        # Return a dictionary containing the input IDs, attention masks, and labels for each example in the batch.
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
        
    def convert(self):
        # Load the dataset from the specified path
        samsum_dataset = load_from_disk(self.config.data_path)

        # Apply the function 'convert_examples_to_features' to all elements in the dataset
        # The 'map' function applies the specified function to each element in the dataset
        # The 'batched=True' argument means that the function is applied to batches of elements, not individual elements
        samsum_dataset_processed = samsum_dataset.map(self.convert_examples_to_features, batched=True)

        # Save the processed dataset to the specified path
        # The 'os.path.join' function is used to create the path by joining the root directory and the file name
        samsum_dataset_processed.save_to_disk(os.path.join(self.config.root_dir, 'samsum_dataset_processed'))
                