covid_headlines = open("title_tokenized.txt", "r")
headlines = covid_headlines.read().lower()

file = open("word_count.txt", "w")

for word in ["coronaviru", "covid", "say", "new", "case", "lockdown", "trump", "death", "pandemic"]:
    file.write("# Regarding the word " + word + ": \n")
    file.write("\tOccurences: \n")
    file.write("\t" + str(headlines.count(word)) + " / " + str(len(headlines.split())) + "\n")
    file.write("\tPercentage: \n")
    file.write("\t" + str(headlines.count(word) / len(headlines.split())) + "\n")
file.close()
