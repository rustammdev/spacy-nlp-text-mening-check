import spacy

nlp = spacy.load("en_core_web_sm")

text = "What Programming languages do I need to know to join Google?"

# Process the text
doc = nlp(text)

# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)