# EmojiPrediction

This is the final project for CMPT413 by Tony Ho, called Emoji Prediction from Tweets.


The data_gathering.ipynb notebook is what gathers all the data from Twitter. It uses functions in data_process.py to clean it up.


The training.ipynb notebook is what is used to build the neural network and start training and evaluations.


The visualizations.ipynb is used to generate graphs and visuals.


From the abstact of the report:


This document outlines the approach that was used in creating an emoji prediction model. Text segments that proceeded one of the top 5 most used emojis on Twitter were extracted from Twitter tweets and were used build a dataset. The dataset was used to fine tune a DistilBERT model for text classification with the emoji as the label. This work differs from previous work as it uses tweets from everyday people instead of the subgroup of celebrities. The best performing model shows an average F1-score of 58.5\%. Analysis on model prediction for self generated text shows that model predication performance is about the same.

![image](https://user-images.githubusercontent.com/4165980/213034378-24750a2e-538e-4011-9ee1-b6de611486fe.png)

![image](https://user-images.githubusercontent.com/4165980/213034651-f16b1ef4-ed3c-43c7-b011-753b680e3a35.png)
