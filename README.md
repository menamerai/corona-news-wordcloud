# Wordcloud Generator for COVID-19 News Headlines

This is a wordcloud generator, using Python to process the vast number
of Covid headlines to create a wordcloud, along with a top 10 list.

*Note: This is not meant for usage, it should be purely for referrencing purposes.*

## main.py

This is where I tokenize the headlines using the NLTK tokenizer
(which can take up to 3 hours), and write the results to a mesh
at "title_tokenized.txt".

## wordcloudgen.py

From the previously acquired tokenized keywords of the COVID-19
headlines, I use the wordcloud Python library to generate the 
top 125 words, and saved it to a .png file

## wordcounter.py

This is an extra module which counts the top ten words from the
mesh file, then output the infomation to wordcount.txt
