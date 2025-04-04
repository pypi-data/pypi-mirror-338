# NER Data Processor

[![Python Version](https://img.shields.io/pypi/pyversions/ner-data-processor.svg)](https://pypi.org/project/ner-data-processor/)
[![PyPI version](https://badge.fury.io/py/ner-data-processor.svg)](https://pypi.org/project/ner-data-processor/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**NER Data Processor** is a Python library to help you easily prepare datasets for Named Entity Recognition (NER) and Coreference Resolution tasks. It transforms raw text into formats ready for training token classification models using Hugging Face or other frameworks.

---

## 📚 Documentation

- [GitHub Repository](https://github.com/rajboopathiking/ner-data-processor)
- [PyPI Package](https://pypi.org/project/ner-data-processor)

---

## 📦 Installation

### ✅ From PyPI (Recommended)

```bash
pip install ner-data-processor
```

### 🛠️ From GitHub

```bash
git clone https://github.com/rajboopathiking/NER_DATA_PREPROCESSING.git
cd NER_DATA_PREPROCESSING
pip install -r requirements.txt
```

---

## 🚀 Getting Started

```python
from ner_data_processor.Ner_Data_Preparation import Custom_Ner_Dataset

ner = Custom_Ner_Dataset()
```

---

## 📊 Dataset Format

Input should be a **pandas DataFrame** with two columns:
- `text`: Sentence or paragraph
- `entities`: List of labeled entities with their tags

Example:

| text | entities |
|------|----------|
| Arun Kumar Jagatramka vs Ultrabulk AS on 22 Sept | [Arun Kumar Jagatramka - PLAINTIFF, Ultrabulk AS - Defender] |
| Author Biren Vaishnav | [Biren Vaishnav - PERSON] |

---

## ⚙️ API Overview

### `extract_DataFrame(df)`

Convert the annotated DataFrame into span-based entity format.

```python
data = ner.extract_DataFrame(df)
```

**Output:**

| text | entities |
|------|----------|
| Arun Kumar Jagatramka vs Ultrabulk AS on... | [(0, 21, PLAINTIFF), (25, 37, Defender)] |
| Author Biren Vaishnav | [(7, 21, PERSON)] |

---

### `to_dataset(data)`

Convert span-format data into token-label format for model training.

```python
import pandas as pd
df = pd.DataFrame(ner.to_dataset(data))
```

**Output:**

| id | tokens | ner_tags |
|----|--------|----------|
| 0 | [Arun, Kumar, Jagatramka, ...] | [B-PLAINTIFF, I-PLAINTIFF, I-PLAINTIFF, ...] |
| 1 | [Author, Biren, Vaishnav] | [O, B-PERSON, I-PERSON] |

---

### `create _label_maps`

```python
labels = []
for i in df["ner_tags"]:
    labels.extend(i)
labels = np.unique(labels).tolist()
```

**Output:**

```python
['B-DATE', 'B-Defender', 'B-LOC', 'B-ORG', 'B-PERSON', 'B-PLAINTIFF',
 'I-DATE', 'I-Defender', 'I-LOC', 'I-ORG', 'I-PERSON', 'I-PLAINTIFF', 'O']
```

---

### `to_huggingface_dataset(df, labels)`

Convert your processed DataFrame into Hugging Face `DatasetDict`.

```python
dataset = ner.to_huggingface_dataset(df, labels)
dataset = dataset.train_test_split(test_size=0.1)
```

**Output:**

```python
DatasetDict({
    train: Dataset({
        features: ['id', 'tokens', 'ner_tags'],
        num_rows: 3
    }),
    test: Dataset({
        features: ['id', 'tokens', 'ner_tags'],
        num_rows: 1
    })
})
```

---

### `coreference_model(text)`

Basic coreference resolution model.

```python
text = "John is Victim. He is Innocent"
result = ner.coreference_model(text)
```

**Output:**

```json
{
  "mentions": [
    {
      "text": "He",
      "refers_to": "John",
      "span": [13, 15]
    }
  ]
}
```

---

## 🪪 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---
