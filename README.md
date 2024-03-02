# finalCapstone
This is a repository which includes my capstone task where I implement the skills acquired within my bootcamp.

# Sentiment Analysis and Text Similarity
This repository contains a Python script for sentiment analysis and text similarity using the spaCy library for natural language processing. The script is designed to analyze sentiment in textual data and compare the similarity between two text samples.

## Installation
To run the code, you'll need to install the necessary dependencies. Use the following command to install them:

pip install spacy pandas spacytextblob

Additionally, download the spaCy English model with the medium size, which is required for the analysis:

python -m spacy download en_core_web_md

## Usage

Clone the repository:

git clone https://github.com/your-username/your-repo.git

Change into the project directory:

cd your-repo
Ensure you have the required CSV file (amazon_product_reviews.csv) in the same directory as the script.

Run the script:

python sentiment_analysis.py

## Description
The script performs sentiment analysis on a sample of Amazon product reviews and compares the similarity between two specific reviews. Here's an overview of the key functionalities:

#### 1. Sentiment Analysis
The script reads the provided CSV file (amazon_product_reviews.csv), cleans the data, and extracts a sample of reviews. It then uses spaCy for natural language processing, along with the TextBlob extension, to predict sentiment (Positive, Negative, or Neutral) for each review in the sample. The results are displayed along with the original reviews.

#### 2. Text Similarity
Two specific reviews from the dataset are chosen (my_review_of_choice_one and my_review_of_choice_two). The script calculates the similarity between these two reviews using spaCy's similarity function, and the result is printed.

## Functions
text_clean(complete_data)
Cleans the input textual data by removing stop words and converting text to lowercase.

predict_sentiment(clean_reviews, review_names)
Predicts the sentiment (Positive, Negative, or Neutral) for each cleaned review in the sample and prints the results.

compare_similarity(review_one, review_two)
Calculates the similarity between two input reviews using spaCy's similarity function.

## Dataset
The script assumes the presence of a CSV file (amazon_product_reviews.csv) containing product reviews. Make sure to adjust the file path or name if necessary.

Feel free to modify and customize the script to suit your specific requirements. Happy analyzing!
