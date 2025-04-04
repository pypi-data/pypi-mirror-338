# NER_DATA_PREPROCESSING :

### Collecting Data For NER:
 this tool helps to create a ner and corefer dataset easily . To train a Token classification and corefer resolution need a dataset.
it not like a raw dataset. we want to convert text (sentence) to required format. lets see how this framework/library used in your project. lets go ...


Step - 1:

 1) install via git

 Download :

     ```bash
     git clone https://github.com/rajboopathiking/NER_DATA_PREPROCESSING.git
     ```

  >> optional (if you already in correct folder)

     ```bash 
     cd NER_DATA_PREPROCESSING
     ```

 requirements.txt -->> installation :

    ```bash
    pip install requirements.txt
    ```

2 ) install via pypi

    ```bash
    pip install ner-data-processor
    ```
    ```python
    from ner-data-processor.Ner_Data_Preparation import Custom_Ner_Dataset
    ner = Custom_Ner_Dataset()
    ```
Step - 2:

DataSet Format :
pandas Dataframe with text(Arun Kumar Jagatramka vs Ultrabulk AS )  and exact word and entity (Arun Kumar Jagatramka - PLAINTIFF)
   
      text	                                               |             entities
    0	Arun Kumar Jagatramka vs Ultrabulk AS on 22 Se...	  | [Arun Kumar Jagatramka - PLAINTIFF, Ultrabulk ...
    1	Author Biren Vaishnav	                              |  [Biren Vaishnav - PERSON]
    2	The Supreme Court ruled in favor of Jane Smith.	    |   [Supreme Court - LOC, Jane Smith - PLAINTIFF]
    3	The Gujarat High Court issued a judgment in Ah...	  |  [Gujarat High Court - ORG, Ahmedabad - LOC]

  API Documentation :

  output for example only

  
  
  2) install via Github 

  1) extract_DataFrame(df) >>

     ```python
     ner = Custom_Ner_Dataset()
     data = ner.extract_DataFrame(df)
     ```

     output :
      
    text	entities
    0	Arun Kumar Jagatramka vs Ultrabulk AS on 22 Se...	[(0, 21, PLAINTIFF), (25, 37, Defender), (41, ...
    1	Author Biren Vaishnav	[(7, 21, PERSON)]
    2	The Supreme Court ruled in favor of Jane Smith.	[(4, 17, LOC), (36, 46, PLAINTIFF)]
    3	The Gujarat High Court issued a judgment in Ah...	[(4, 22, ORG), (44, 53, LOC)]

  2) to_dataset(data) >>

     ```python
     import pandas as pd
     import numpy as np
     df = pd.DataFrame(ner.to_dataset(data))

     ```

     output :
     
               id	                                                     tokens	ner_tags
          0	0	[Arun, Kumar, Jagatramka, vs, Ultrabulk, AS, o...	 [B-PLAINTIFF, I-PLAINTIFF, I-PLAINTIFF, O, B-D...
          1	1	[Author, Biren, Vaishnav]	[O, B-PERSON, I-PERSON]
          2	8	[The, Supreme, Court, ruled, in, favor, of, Ja...	  [O, B-LOC, I-LOC, O, O, O, O, B-PLAINTIFF, I-P...
          3	9	[The, Gujarat, High, Court, issued, a, judgmen...	  [O, B-ORG, I-ORG, I-ORG, O, O, O, O, B-LOC, O]

 4)  Create _label_maps to create Huggingface Dataset :

    ```python
    labels = []
    for i in df["ner_tags"].tolist():
      labels.extend(i)
    labels = np.unique(labels).tolist()
    labels
    ```

   output :
   
       ['B-DATE',
     'B-Defender',
     'B-LOC',
     'B-ORG',
     'B-PERSON',
     'B-PLAINTIFF',
     'I-DATE',
     'I-Defender',
     'I-LOC',
     'I-ORG',
     'I-PERSON',
     'I-PLAINTIFF',
     'O']
    

  5) to_huggingface_dataset(data,labels) >>

     ```python
     dataset = ner.to_huggingface_dataset(df,labels)
     dataset = dataset.train_test_split(test_size=0.1)
     dataset
     ```

     output :
     
          DatasetDict({
         train: Dataset({
             features: ['id', 'tokens', 'ner_tags'],
             num_rows: 3
         })
         test: Dataset({
             features: ['id', 'tokens', 'ner_tags'],
             num_rows: 1
         })
     })

     
   7) coreference_model(text) >>>

      ```python

      ner.coreference_model(text:str)  

      ```
          input : text = "John is Victim. He is Innocent"
          output : He mentions John it returns in json format which text,mentions,and span ...





