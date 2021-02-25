#!/usr/bin/env python
# coding: utf-8

# Off-Platform Project: Classifying Tweets
# In this off-platform project, you will use a Naive Bayes Classifier to find patterns in real tweets.
# We've given you three files: `new_york.json`, `london.json`, and `paris.json`. These three files contain tweets that we gathered from those locations.
# The goal is to create a classification algorithm that can classify any tweet (or sentence) and predict whether that sentence came from New York, London, or Paris.

# 1: Investigate the Data

import pandas as pd

new_york_tweets = pd.read_json("new_york.json", lines=True)
print(len(new_york_tweets))
print(new_york_tweets.columns)
print(new_york_tweets.loc[12]["text"])


# 2: In the code block below, load the London and Paris tweets into DataFrames named `london_tweets` and `paris_tweets`.
# How many London tweets are there? How many Paris ones are there?

london_tweets = pd.read_json("london.json", lines=True)
paris_tweets = pd.read_json("paris.json", lines=True)
print(len(london_tweets))
print(len(paris_tweets))


# 2: Classifying using language: Naive Bayes Classifier
# We're going to create a Naive Bayes Classifier! Let's begin by looking at the way language is used differently in these three locations.
# Let's grab the text of all of the tweets and make it one big list. In the code block below, we've created a list of all the New York tweets.

# Do the same for `london_tweets` and `paris_tweets`.
# Then combine all three into a variable named `all_tweets` by using the `+` operator. For example, `all_tweets = new_york_text + london_text + ...`
# Let's also make the labels associated with those tweets. `0` represents a New York tweet, `1`  represents a London tweet, and `2` represents a Paris tweet. Finish the definition of `labels`.

new_york_text = new_york_tweets["text"].tolist()
london_text = london_tweets["text"].tolist()
paris_text = paris_tweets["text"].tolist()

all_tweets = new_york_text + london_text + paris_text
labels = [0] * len(new_york_text) + [1] * len(london_text) + [2] * len(paris_text)


# 3: Making a Training and Test Set
# 
# We can now break our data into a training set and a test set. We'll use scikit-learn's `train_test_split` function to do this split.
# This function takes two required parameters: It takes the data, followed by the labels. Set the optional parameter `test_size` to be `0.2`.
# Finally, set the optional parameter `random_state` to `1`. This will make it so your data is split in the same way as the data in our solution code. 

# Store the results in variables named `train_data`, `test_data`, `train_labels`, and `test_labels`.
# Print the length of `train_data` and the length of `test_data`.

from sklearn.model_selection import train_test_split

train_data, test_data, train_labels,test_labels = train_test_split(all_tweets, labels, test_size=0.2, random_state=1)

print(len(train_data),len(test_data))


# 4: Making the Count Vectors
# To use a Naive Bayes Classifier, we need to transform our lists of words into count vectors.
# Recall that this changes the sentence `"I love New York, New York"` into a list that contains:
# 
# * Two `1`s because the words `"I"` and `"love"` each appear once.
# * Two `2`s because the words `"New"` and `"York"` each appear twice.
# * Many `0`s because every other word in the training set didn't appear at all.
# 
# To start, create a `CountVectorizer` named `counter`.
# 
# Next, call the `.fit()` method using `train_data` as a parameter. This teaches the counter our vocabulary.
# 
# Finally, let's transform `train_data` and `test_data` into Count Vectors.
# Call `counter`'s `.transform()` method using `train_data` as a parameter and store the result in `train_counts`.
# Do the same for `test_data` and store the result in `test_counts`.
# Print `train_data[3]` and `train_counts[3]` to see what a tweet looks like as a Count Vector.

from sklearn.feature_extraction.text import CountVectorizer

counter = CountVectorizer()
counter.fit(train_data)

train_counts = counter.transform(train_data)
test_counts = counter.transform(test_data)

print(train_data[3], train_counts[3])


# 5: Train and Test the Naive Bayes Classifier
# We now have the inputs to our classifier. Let's use the CountVectors to train and test the Naive Bayes Classifier!
# 
# First, make a `MultinomialNB` named `classifier`.
# Next, call `classifier`'s `.fit()` method. This method takes two parameters &mdash; the training data and the training labels.
# `train_counts` contains the training data and `train_labels` containts the labels for that data.
# Calling `.fit()` calculates all of the probabilities used in Bayes Theorem. The model is now ready to quickly predict the location of a new tweet. 
#  let's test our model. `classifier`'s `.predict()` method using `test_counts` as a parameter. Store the results in a variable named `predictions`.

from sklearn.naive_bayes import MultinomialNB

classifier = MultinomialNB()
classifier.fit(train_counts, train_labels)

predictions = classifier.predict(test_counts)


# 6: Evaluating Your Model
# 
# Now that the classifier has made its predictions, let's see how well it did. Let's look at two different ways to do this. First, call scikit-learn's `accuracy_score` function. This function should take two parameters &mdash;  the `test_labels` and your `predictions`. Print the results. This prints the percentage of tweets in the test set that the classifier correctly classified.

from sklearn.metrics import accuracy_score

print(accuracy_score(test_labels, predictions))

# The other way you can evaluate your model is by looking at the **confusion matrix**. A confusion matrix is a table that describes how your classifier made its predictions.
# For example, if there were two labels, A and B, a confusion matrix might look like this:
# 
# ```
# 9 1
# 3 5
# ```
# 
# In this example, the first row shows how the classifier classified the true A's. It guessed that 9 of them were A's and 1 of them was a B.
# The second row shows how the classifier did on the true B's. It guessed that 3 of them were A's and 5 of them were B's.
# For our project using tweets, there were three classes &mdash; `0` for New York, `1` for London, and `2` for Paris.
# You can see the confustion matrix by printing the result of the `confusion_matrix` function using `test_labels` and `predictions` as parameters.

from sklearn.metrics import confusion_matrix

print(confusion_matrix(test_labels, predictions))

# 7: Test Your Own Tweet
# The confusion matrix should line up with your intuition. The classifier predicts tweets that were actually from New York as either New York tweets or London tweets, but almost never Paris tweets.
# Similarly, the classifier rarely misclassifies the tweets that were actually from Paris. Tweets coming from two English speaking countries are harder to distinguish than tweets in different languages.

# Now it's your chance to write a tweet and see how the classifier works! Create a string and store it in a variable named `tweet`. 
# Call `counter`'s `.transform()` method using `[tweet]` as a parameter. Save the result as `tweet_counts`.
# Notice that your variable has to be in an array &mdash; `.transform()` can't take just a string, it must be a list. 
# Finally, pass `tweet_counts` as parameter to `classifier`'s `.predict()` method. Print the result. This should give you the prediction for the tweet.
# Remember a `0` represents New York, a `1` represents London, and a `2` represents Paris. Can you write different tweets that the classifier predicts as being from New York, London, and Paris?

tweet ="Le cruciform de tante Jeanne pulse fébrilement"
tweet_counts = counter.transform([tweet])
print(classifier.predict(tweet_counts))

