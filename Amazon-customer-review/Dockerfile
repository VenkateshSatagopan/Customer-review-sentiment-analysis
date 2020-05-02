#Use python as base image
FROM python:3.7-slim

#Use working directory /app
WORKDIR /app

#Copy all the content of current directory to /app
ADD . /app

#Installing required packages
RUN pip install tensorflow
RUN pip install Flask
RUN pip install py-healthcheck
RUN pip install tensorflow-datasets
RUN pip install Flask-Bootstrap

#Open port 4000
EXPOSE 4000

#Set environment variable
ENV NAME OpentoAll

#Run python program
CMD ["python","sentiment_analysis_final.py"]
