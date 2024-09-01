import nltk
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import ne_chunk

text = "Create a system to manage Financial module with roles of Asistant, Manager and Operator"
tokens = word_tokenize(text)

stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token.lower(), pos="v") for token in filtered_tokens]

pos_tags = nltk.pos_tag(lemmatized_tokens)

ner_tags = ne_chunk(pos_tags)
print(ner_tags)