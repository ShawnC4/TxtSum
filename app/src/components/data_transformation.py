import os
from src.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from src.entity import DataTransformationConfig

class DataTransformation:
    
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
    

    def convert_examples_to_features(self, example_batch):
        # Tokenize the input text
        input_encodings = self.tokenizer(
            example_batch['dialogue'],
            max_length=1024,
            truncation=True,
        )

        # Tokenize the target/summary text using `text_target`
        target_encodings = self.tokenizer(
            text_target=example_batch['summary'],
            max_length=128,
            truncation=True,
        )

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)

        split_lengths = [len(dataset_samsum[split])for split in dataset_samsum]

        print(f"Split lengths: {split_lengths}")
        print(f"Features: {dataset_samsum['train'].column_names}")
        print("\nDialogue:")

        print(dataset_samsum["test"][1]["dialogue"])

        print("\nSummary:")

        print(dataset_samsum["test"][1]["summary"])

        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))
        logger.info(f"Dataset transformed and saved to: {os.path.join(self.config.root_dir, "samsum_dataset")}\n")