from wordcloud import WordCloud, STOPWORDS

covid_headlines = open("title_tokenized.txt", "r")
headlines = covid_headlines.read()

wordcloud_gen = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black', colormap='Set2', collocations=False, stopwords = STOPWORDS, max_words=125).generate(headlines).to_file("Covid News Headlines.png")