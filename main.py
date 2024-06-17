import spacy
from spacy.matcher import Matcher

# spaCy modelini yuklash
nlp = spacy.load('en_core_web_sm')

def extract_keywords_from_question(question):
    """
    Berilgan savoldan kalit so'zlarni ajratib oladi.
    """
    doc = nlp(question)
    matcher = Matcher(nlp.vocab)

    # Kalit so'zlarni aniqlash uchun pattern
    pattern = [
        {"POS": {"IN": ["NOUN", "PROPN"]}},
        {"POS": {"IN": ["VERB", "ADJ", "ADV"]}, "OP": "?"},
    ]
    
    matcher.add("KEYWORDS", [pattern])

    matches = matcher(doc)
    keywords = [doc[start:end].text for match_id, start, end in matches]
    
    return keywords

# Savollar ro'yxati
questions = [
    "What are the benefits of regular exercise?",
    "How to improve mental health?",
    "What are the best programming languages for web development?",
    "Can you explain the theory of relativity?",
    "How to start a successful business?",
    "What is the impact of climate change on marine life?",
]

# Har bir savoldan kalit so'zlarni ajratib olish
for question in questions:
    keywords = extract_keywords_from_question(question)
    print(f"Question: {question}")
    print(f"Keywords: {keywords}\n")