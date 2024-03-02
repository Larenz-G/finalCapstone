# Import spacy for natural language processing and to complete sentiment analysis
import spacy

# Import pandas as pd to read in dataframe
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob

# Load spacy and language model 'en_core_web_md'
nlp = spacy.load('en_core_web_md')
nlp.add_pipe('spacytextblob')

# Create all functions needed for analysis 

# Create tect cleaning function
def text_clean(complete_data):
    clean_reviews = []
    
    for review in complete_data:
        doc = nlp(review)
        clean_text = ' '.join([token.text.lower() for token in doc if not token.is_stop and token.text.strip()])
        clean_reviews.append(clean_text)
    
    return clean_reviews

# Create function to predict the sentiment 
def predict_sentiment(clean_reviews, review_names):
    # Use ._.polarity to get sentiment score
    for idx, review in enumerate(clean_reviews):
        doc = nlp(review)
        polarity = doc._.blob.polarity
        # sort reviws into positive/neutral/negative 
        sentiment_label = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
        print(f"Review '{review_names[idx]}': {review_df.at[idx, 'reviews.text']} - Sentiment: {sentiment_label} (Polarity: {polarity})\n" )

# Create function to compare the similarity 
def compare_similarity(review_one,review_two):
    similarity_answer = nlp(review_one).similarity(nlp(review_two))
    return similarity_answer

# Read in CSV file and place it in a variable named review_df.
# Add delimiter taking in ',' and set low memory to false
review_df = pd.read_csv("amazon_product_reviews.csv", delimiter=',', low_memory=False)

# Clean data, use .dropna to remove any NA values for the reviews.text column
clean_data = review_df.dropna(subset=['reviews.text'])

# Create a variable that holds a test sample using the iloc function 
sample_data = clean_data['reviews.text'].iloc[:10]  # Adjust the number as needed
review_names = clean_data['name'].iloc[:10]  # select the name column

# Call functions
clean_reviews = text_clean(sample_data)
predict_sentiment(clean_reviews, review_names)


# Review similarity 

my_review_of_choice_one = review_df['reviews.text'][200]
my_review_of_choice_two = review_df['reviews.text'][457]

print(f'Review one:{my_review_of_choice_one} \nReview two:{my_review_of_choice_two} \nThe similarity between both of these reviews are {compare_similarity(my_review_of_choice_one,my_review_of_choice_two)}')

