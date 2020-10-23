import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import nltk

nltk.download('punkt')

data = pd.read_csv("corona_news.csv", error_bad_lines=False, index_col="id")
headline_words = []
tokenizer = nltk.RegexpTokenizer(r"\w+")
for index, headline in data["title"].items():
    headline_words = headline_words + tokenizer.tokenize(str(headline))
print(headline_words)
text = open("title_tokenized.txt", "w")
text.write(" ".join(headline_words))
text.close()