import nltk
nltk.download('punkt')
from tika import parser
einleitung = False
raw = parser.from_file('iso_documents/ISO1101.PDF')
#print(raw['content'])
text = raw['content']
sent_text = nltk.sent_tokenize(text)
#tokenized_text = nltk.word_tokenize(sent_text.split)
#tagged = nltk.pos_tag(tokenized_text)
#match = text.concordance('Toleranz')
for text in sent_text:
    if "Toleranz" in text and einleitung is True:
        print(text)
    if "Einleitung" in text:
        einleitung = True