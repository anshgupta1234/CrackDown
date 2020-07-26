from nltk.sentiment.vader import SentimentIntensityAnalyzer


sld = SentimentIntensityAnalyzer()
print(sld.polarity_scores("bruh you're actually a retard")["neg"])