from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk, load_metric
import torch
import pandas as pd
from tqdm import tqdm
from ConversationSummarizer.entity import ModelEvaluationConfig



class ModelEvaluation:
    # Initialize the ModelEvaluation with a configuration object
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    # Method to split a list into smaller batches
    def generate_batch_sized_chunks(self,list_of_elements, batch_size):
        """Yield successive batch-sized chunks from list_of_elements."""
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i : i + batch_size]

    # Method to calculate a metric on a test dataset
    def calculate_metric_on_test_ds(self,dataset, metric, model, tokenizer, 
                               batch_size=16, device="cuda" if torch.cuda.is_available() else "cpu", 
                               column_text="article", 
                               column_summary="highlights"):
        # Split the articles and targets into batches
        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size))
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size))

        # For each batch of articles and targets
        for article_batch, target_batch in tqdm(
            zip(article_batches, target_batches), total=len(article_batches)):
            
            # Tokenize the articles
            inputs = tokenizer(article_batch, max_length=1024,  truncation=True, 
                            padding="max_length", return_tensors="pt")
            
            # Generate summaries with the model
            summaries = model.generate(input_ids=inputs["input_ids"].to(device),
                            attention_mask=inputs["attention_mask"].to(device), 
                            length_penalty=0.8, num_beams=8, max_length=128)
            
            # Decode the generated summaries
            decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True, 
                                    clean_up_tokenization_spaces=True) 
                for s in summaries]      
            
            # Replace the  token in the decoded summaries
            decoded_summaries = [d.replace("", " ") for d in decoded_summaries]
            
            # Add the decoded summaries and the targets to the metric
            metric.add_batch(predictions=decoded_summaries, references=target_batch)
            
        # Compute and return the metric score
        score = metric.compute()
        return score

    # Method to evaluate the model
    def evaluate(self):
        # Determine the device to use
        device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Load the tokenizer and the model
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device)
       
        # Load the data
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # Define the names of the ROUGE metrics to compute
        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
  
        # Load the ROUGE metric
        rouge_metric = load_metric('rouge')

        # Calculate the ROUGE scores on the test dataset
        score = self.calculate_metric_on_test_ds(
        dataset_samsum_pt['test'][0:10], rouge_metric, model_pegasus, tokenizer, batch_size = 2, column_text = 'dialogue', column_summary= 'summary'
            )

        # Create a dictionary of the ROUGE scores
        rouge_dict = dict((rn, score[rn].mid.fmeasure ) for rn in rouge_names )

        # Create a DataFrame of the ROUGE scores and save it to a CSV file
        df = pd.DataFrame(rouge_dict, index = ['pegasus'] )
        df.to_csv(self.config.metric_file_name, index=False)
        

