import sys
import os

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from NER_DATA_PREPROCESSING.Ner_Data_Preparation import Custom_Ner_Dataset
import pandas as pd

ner_ = Custom_Ner_Dataset()
data = {"text":["Arun Kumar Jagatramka vs Ultrabulk AS"],
    "entities":[["Arun Kumar Jagatramka - PLAINTIFF"]]}

df = pd.DataFrame(data)

extract_df = ner_.extract_DataFrame(df=df)

print(extract_df)

### to dataset

dataset = ner_.to_dataset(extract_df)

print(
    {
        "Raw _ dataset": dataset,
        "DataFrame": pd.DataFrame(dataset)
    }
)

text = "John is Victim. He is Innocent"

print(ner_.coreference_model(text))
