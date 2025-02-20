# python app.py



from flask import Flask, render_template, request, jsonify
import pickle
import string


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd
from urllib.parse import quote


# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained model and vectorizer
with open('model.pkl', 'rb') as model_file:
    rf = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Initialize the Porter Stemmer
stemmer = PorterStemmer()


# Preprocessing function
def preprocess_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize text
    tokens = word_tokenize(text)

    # Remove stop words and apply stemming
    stop_words = set(stopwords.words('english'))
    cleaned_tokens = [stemmer.stem(word.lower()) for word in tokens if
                      word.isalpha() and word.lower() not in stop_words]

    # Join the cleaned tokens into a single string
    return ' '.join(cleaned_tokens)
@app.route('/bdi')
def bdi():
    return render_template('BDI.html')

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')




# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text'].lower()

        # Preprocess the input text
        preprocessed_text = preprocess_text(text)

        # Create a DataFrame for the new data
        data1 = pd.DataFrame({'text': [preprocessed_text]})

        # Transform the new data using the vectorizer
        X1 = vectorizer.transform(data1['text']).toarray()

        # Make predictions on the new data
        new_predictions = rf.predict(X1)
        new_probabilities = rf.predict_proba(X1)

        # Get the probability of suicide
        probability_suicide = new_probabilities[0][1]
        label = "suicide" if probability_suicide >= 0.5 else "non-suicide"

        # Return the result as JSON
        return jsonify({
            'prediction': label,
            'probability_suicide': f'{probability_suicide:.4f}'
        })


if __name__ == '__main__':
    app.run(debug=True)
