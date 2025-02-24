# Depression_Detection

# Mental Wellness Project

## Objective
This project aims to classify social media posts as **suicidal or non-suicidal** to detect individuals struggling with mental health issues and provide timely intervention.

---

## Model Flow

### 1. Data Cleaning
✔ **Remove Unnecessary Columns**  
✔ **Null and Duplicate Check:**  
   - Remove rows with missing text or class values.  
   - Drop duplicate text entries to prevent bias in training.  

### 2. Class Balance Check
💡 **Why?** Imbalanced classes can bias the model towards the majority class.  
✅ **Method:** Check if the number of suicidal and non-suicidal texts is significantly different.  

### 3. Feature Engineering
- **Word Count Column:** Compute word count to analyze length distribution.  
- **Outlier Removal:**  
  - **Why?** Extreme text lengths can skew model performance.  
  - **Method:** Remove texts below the 20th percentile and above the 80th percentile.  
  - **Action:** Limited length between **50-150 words**.  
- **Variance Reduction:**  
  - Ensures word count distribution across classes is similar.  
  - **Observations:**  
    - **Before:** Suicide - 36.70, Non-Suicide - 46.61  
    - **After:** Suicide - 20.54, Non-Suicide - 21.81  
  - **Impact:** If variance becomes too similar, additional features (e.g., sentiment analysis, phrase patterns) are required.  

### 4. Text Preprocessing
✔ Convert text to lowercase  
✔ Remove punctuation & stopwords (e.g., “the”, “is”, “in”)  
✔ Tokenization (split text into words)  
✔ Lemmatization & Stemming  

### 5. Label Encoding
Convert categorical labels into numerical values:  
- **Suicide → 1**  
- **Non-Suicide → 0**  

### 6. Text Vectorization
Convert text into numerical form for model training using:  
- **Unigrams** (single words as features)  
- **Bigrams (20,000 features)** (two consecutive words)  
- **Trigrams (10,000 features)** (three consecutive words)  
✅ **Used a combination of unigram and bigram**  

### 7. Model Selection
✅ **Random Forest Classifier**  

### 8. Model Performance
🎯 **Achieved 88% accuracy** in classifying suicidal vs. non-suicidal posts.  

---

## Advantages
✔ **Effective Data Cleaning & Preprocessing** – Ensures high-quality input.  
✔ **Feature Engineering** – Word count analysis and variance adjustment improve text representation.  
✔ **Balanced Class Distribution** – Prevents model bias.  
✔ **Efficient Vectorization** – Combination of unigrams and bigrams captures context.  
✔ **Good Performance** – **88% accuracy** in classification.  

---

## Disadvantages
✖ **Limited Features** – Lacks **sentiment analysis, NER, or topic modeling**.  
✖ **Outlier Removal Risk** – May discard **critical texts**.  
✖ **Basic Label Encoding** – Word embeddings (e.g., **BERT**) could improve results.  
✖ **Random Forest Not Ideal for Text** – **LSTMs or Transformers** may work better.  
✖ **Limited Explainability** – Deep learning models provide better insights.  

---

## Conclusion
The model is **structured and performs well**, but **adding semantic features** (e.g., sentiment analysis) and **using deep learning (BERT, LSTMs)** could **further enhance accuracy and contextual understanding**.  
