import nltk
nltk.download('punkt')
from tika import parser

raw = parser.from_file('iso_documents/ISO1101.PDF')
#print(raw['content'])
text = raw
sent_text = nltk.sent_tokenize(text)
#tokenized_text = nltk.word_tokenize(sent_text.split)
#tagged = nltk.pos_tag(tokenized_text)
#match = text.concordance('Toleranz')
#print(sent_text)