Libraries used - 

profanity-check

profanity-check relies heavily on the excellent scikit-learn library. It's mostly powered by scikit-learn classes CountVectorizer, LinearSVC, and CalibratedClassifierCV. It uses a Bag-of-words model to vectorize input strings before feeding them to a linear classifier.

Dataset used -

Sentiment140: This popular dataset contains 160,000 tweets formatted with 6 fields: polarity, ID, tweet date, query, user, and the text. Emoticons have been pre-removed.

#predict() takes an array and returns a 1 for each string if it is offensive, else 0.
#predict_prob() takes an array and returns the probability each string is offensive
#Examples
print(predict(['fuck you']))
#[1]
print(predict_prob(['go to hell, you scum']))
#[0.7618861]