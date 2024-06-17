import spacy

# Create the English nlp object
nlp = spacy.blank("en")

# Process a text
doc = nlp("This is a sentence and this is a number 11")


for token in doc:
    if token.like_num:
        print(token)


# print(first_token.text)

# python -m spacy download en_core_web_lg