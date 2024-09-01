import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
# Initialize Python porter stemmer
ps = PorterStemmer()
text = "Natural Language Processing is a subfield of artificial intelligence that focuses on the interaction between humans and computers using natural language."
tokens = word_tokenize(text)

stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Perform stemming
print("{0:20}{1:20}".format("--Word--","--Stem--"))
for word in filtered_tokens:
   print ("{0:20}{1:20}".format(word, ps.stem(word)))

lemmatized_tokens = [ps.stem(word) for word in filtered_tokens]

print(lemmatized_tokens)


