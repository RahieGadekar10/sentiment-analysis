import transformers
DEVICE = "cpu"
MAX_LEN = 64
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 2
BERT_PATH = "bert-base-uncased"
MODEL_PATH = "bert_base_uncased/model.bin"
TRAINING_FILE = "imdb_dataset.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(BERT_PATH, do_lower_case=True, return_dict=False)
MODEL_PATH1= "bert_base_uncased/model.bin1"
