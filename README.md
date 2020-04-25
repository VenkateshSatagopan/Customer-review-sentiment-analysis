# Customer-review-sentiment-analysis using LSTM
Amazon personal health care customer review sentiment analysis, GUI development using flask and model deployment using docker

Data Collection:

Data collected from Amazon personal health care products customer reviews. Sentiment analysis is done on the collected data to decide whether particular review is positive or negative.

Main Contributions in the project:

1. Data Preparation, Bidirectional LSTM based sentiment analysis model training (This part is inspired from the videos on scaling machine learning models by srivatsan srinivasn sir https://www.youtube.com/playlist?list=PL3N9eeOlCrP7_vt6jq7GdJz6CSFmtTBpI) 

2. Creating a Flask based GUI to deploy the model.

3. Containerize the application using Docker 
Steps to run the docker can be found from docker-running-steps.txt
https://github.com/VenkateshSatagopan/Customer-review-sentiment-analysis/blob/master/Amazon-customer-review/docker-running-steps.txt

sentiment-analysis-final.py contains the code for testing the LSTM model using Flask GUI. The Web-GUI looks as shown below:

![Sentiment analyser GUI](https://github.com/VenkateshSatagopan/Customer-review-sentiment-analysis/blob/master/Amazon-customer-review/Final-page.PNG)






