from .Corefer import process_text
class Custom_Ner_Dataset:
    def __init__(self):
        import spacy
        from spacy.tokens import DocBin
        """Initialize an empty SpaCy model and a DocBin object."""
        self.nlp = spacy.blank("en")
        self.doc_bin = DocBin()

    def convert_to_docbin(self, train_data, docbin_save_dir=None, nlp_save_dir=None):
        from tqdm import tqdm
        """Convert labeled text data into SpaCy's DocBin format for training."""
        for data in train_data:
            doc = self.nlp.make_doc(data["text"])
            ents = []

            for start, end, label in tqdm(data["entities"], desc="Converting to doc-bin..."):
                span = doc.char_span(start, end, label=label, alignment_mode="contract")
                if span is None:
                    print(f"⚠️ Skipping entity '{data['text'][start:end]}' due to misalignment.")
                    continue
                ents.append(span)

            doc.ents = ents
            self.doc_bin.add(doc)

        # Save the DocBin and NLP model if specified
        if docbin_save_dir:
            self.doc_bin.to_disk(docbin_save_dir)
        if nlp_save_dir:
            self.nlp.to_disk(nlp_save_dir)
        return self.doc_bin, self.nlp

    def load_dataset(self, docbin_path, nlp_path):
        from tqdm import tqdm
        from spacy.tokens import DocBin
        """Load a saved DocBin dataset and SpaCy NLP model."""
        self.nlp = spacy.load(nlp_path)
        self.doc_bin = DocBin().from_disk(docbin_path)
        return self.docbin_to_dataset()

    def to_docbin(self, train_data, docbin_save_dir=None, nlp_save_dir=None):
        from tqdm import tqdm
        """Convert labeled text data into SpaCy's DocBin format for training."""
        for index,data in train_data.iterrows():
            doc = self.nlp.make_doc(data["text"])
            ents = []

            for start, end, label in tqdm(data["entities"], desc="Converting to doc-bin..."):
                span = doc.char_span(start, end, label=label, alignment_mode="contract")
                if span is None:
                    print(f"⚠️ Skipping entity '{data['text'][start:end]}' due to misalignment.")
                    continue
                ents.append(span)

            doc.ents = ents
            self.doc_bin.add(doc)

        # Save the DocBin and NLP model if specified
        if docbin_save_dir:
            self.doc_bin.to_disk(docbin_save_dir)
        if nlp_save_dir:
            self.nlp.to_disk(nlp_save_dir)
        return self.doc_bin, self.nlp

    def docbin_to_dataset(self,train_data,docbin_save_dir=None, nlp_save_dir=None):
        from tqdm import tqdm
        """Convert SpaCy's DocBin format into a structured dataset with tokenized labels."""
        doc_bin,nlp = self.convert_to_docbin(train_data,docbin_save_dir=None, nlp_save_dir=None)
        docs = list(doc_bin.get_docs(nlp.vocab))
        dataset = []

        for idx, doc in tqdm(enumerate(docs), desc="Dataset Creation Begin..."):
            tokens = [token.text for token in doc]
            labels = ["O"] * len(tokens)

            for ent in doc.ents:
                start_idx = ent.start
                entity_label = ent.label_

                labels[start_idx] = f"B-{entity_label}"  # Start of entity
                for i in range(start_idx + 1, ent.end):
                    labels[i] = f"I-{entity_label}"  # Inside entity

            dataset.append({"id": idx, "tokens": tokens, "ner_tags": labels})

        return dataset
    
    def remove_duplicates(self,df):
      df['tokens'] = df['tokens'].apply(tuple)
      df["ner_tags"] = df["ner_tags"].apply(tuple)
      df = df.drop("id",axis=1)
      df.drop_duplicates(inplace=True)
      df.reset_index(inplace=True)
      df.columns = ["id","tokens","ner_tags"]
      df["tokens"] = df["tokens"].apply(lambda x: list(x))
      df["ner_tags"] = df["ner_tags"].apply(lambda x: list(x))
      return df
    

    def to_dataset(self,train_data,docbin_save_dir=None, nlp_save_dir=None):
        from tqdm import tqdm
        import pandas as pd
        import json
        """Convert SpaCy's DocBin format into a structured dataset with tokenized labels."""
        doc_bin,nlp = self.to_docbin(train_data,docbin_save_dir=None, nlp_save_dir=None)
        docs = list(doc_bin.get_docs(nlp.vocab))
        dataset = []

        for idx, doc in tqdm(enumerate(docs), desc="Dataset Creation Begin..."):
            tokens = [token.text for token in doc]
            labels = ["O"] * len(tokens)

            for ent in doc.ents:
                start_idx = ent.start
                entity_label = ent.label_

                labels[start_idx] = f"B-{entity_label}"  # Start of entity
                for i in range(start_idx + 1, ent.end):
                    labels[i] = f"I-{entity_label}"  # Inside entity

            dataset.append({"id": idx, "tokens": tokens, "ner_tags": labels})
        
        df = pd.DataFrame(dataset)
        df = self.remove_duplicates(df)
        df = df.to_json(orient="records")

        return json.loads(df)

    def to_huggingface_dataset(self, train_data,labels):
        from datasets import Dataset, Features, Value, Sequence, ClassLabel
        


        """Convert processed dataset into a Hugging Face `datasets.Dataset`."""
        dataset = Dataset.from_list(self.to_dataset(train_data))


        # Define dataset schema
        features = Features(
            {
                "id": Value("int64"),
                "tokens": Sequence(Value("string")),
                "ner_tags": Sequence(ClassLabel(names=labels)),
            }
        )

        return dataset.cast(features)

    def save_label_map(self, file_path="label_map.json"):
        import json
        """Save label mappings to a JSON file."""
        with open(file_path, "w") as f:
            json.dump({"id2label": self.id2label, "label2id": self.label2id}, f)

    def transform(self, train_data):
        """Transform raw text data into a tokenized dataset with numerical labels."""
        self.convert_to_docbin(train_data)
        dataset = self.docbin_to_dataset()

        # Convert label names to IDs
        for entry in dataset:
            entry["ner_tags"] = [self.label2id.get(tag, self.label2id["O"]) for tag in entry["ner_tags"]]

        return dataset  # ✅ Fixed Indentation

    def transform_to_huggingface_dataset(self, train_data,labels):
        from datasets import Dataset, Features, Value, Sequence, ClassLabel
        """Convert processed dataset into a Hugging Face `datasets.Dataset`."""

        train_data
        dataset = Dataset.from_list(self.transform(train_data))

        # Define dataset schema
        features = Features(
            {
                "id": Value("int64"),
                "tokens": Sequence(Value("string")),
                "ner_tags": Sequence(ClassLabel(names=labels)),
            }
        )

        return dataset.cast(features)

    def word_position(self, text: str, word: str):
        import re
        """
        Finds the position of a word in a text using regex (better than .index()).

        Args:
            text: The text to search within.
            word: The word to search for.

        Returns:
            A dictionary containing the length, index, and range of the word in the text,
            or None if the word is not found.
        """
        match = re.search(rf"\b{re.escape(word)}\b", text)  # Match whole words only
        if match:
            start = match.start()
            end = match.end()
            result = {
                "length": len(word),
                "index": start,
                "range": {"start": start, "end": end},
                "text": text[start:end],
            }
            self.result = result
            return start, end
        return None  # Return None if word not found

    def Raw_Dataset(self, text:str, extract_words : list, entities:list):
      entities_list = []
      for word,entity in zip(extract_words,entities):
        start,end = self.word_position(text, word)
        entities_list.append((start,end,entity))
      return {
          "text":text,
          "entities":entities_list
      }
    def Raw_Dataset_From_JSON_List(self,raw_data:list):
      dataset = []
      for data in raw_data:
        text = data["text"]
        extract_words = data["extract_words"]
        entities = data["entities"]
        dataset.append(self.Raw_Dataset(text,extract_words,entities))
      return dataset

    def Raw_Dataset_From_DataFrame(self,raw_data):
      dataset = []
      for index,row in raw_data.iterrows():
        text = row["text"]
        extract_words = row["extract_words"]
        entities = row["entities"]
        dataset.append(self.Raw_Dataset(text,extract_words,entities))
      return dataset

    def extract_from_labels(self,labels):
      """
      Extract Entities & Labels From Labels

      """
      entities = []
      extract_words = []
      for label in labels:
        extract_words.append(label.split("-")[0].strip())
        entities.append(label.split("-")[1].strip())
      return extract_words,entities

    def extract_DataFrame(self,df):
      import pandas as pd
      dataset = []
      for index,row in df.iterrows():
        text = row["text"]
        labels = row["entities"]
        extract_words,entities = self.extract_from_labels(labels)
        dataset.append(self.Raw_Dataset(text,extract_words,entities))
      return pd.DataFrame(dataset)
    
    def coreference_model(self,text):
       return process_text(text)
        