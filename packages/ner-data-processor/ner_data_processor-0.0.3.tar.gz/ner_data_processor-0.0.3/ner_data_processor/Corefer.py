import spacy
import json
import subprocess

# Install the spacy model if not already installed
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading 'en_core_web_sm' model...")
    response = subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"], check=True)
    print({"output":response.stdout,
     "Error":response.stderr})
    nlp = spacy.load("en_core_web_sm")


# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to process text and extract coreferences
def process_text(text):
    doc = nlp(text)
    coref_data = []
    
    # Extract named entities and pronouns
    for ent in doc.ents:
        mentions = [token.text for token in doc if token.ent_type_ == ent.label_]
        if len(mentions) >= 1:
            coref_data.append({"text":text,"entity": ent.text, "mentions": mentions})

    return coref_data
