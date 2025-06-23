# Customer Feedback Intelligence System

This project processes customer feedback data to:

- **Classify sentiment** (Positive, Negative, Neutral) for each feedback using [TextBlob](https://textblob.readthedocs.io/en/dev/).
- **Extract product or company names** from each feedback using [spaCy](https://spacy.io/)’s Named Entity Recognition (NER).
- **Output enriched datasets** at each step for further analysis or reporting.

---

## File Structure

```
├── sentiment_analysis.py           # Script for sentiment classification
├── product.py                     # Script for product/company extraction
├── merge-csv.com__6853d1f34c30b.csv  # Original input CSV file
├── sentiment_output.csv           # Output after sentiment classification
├── sentiment_with_product.csv     # Final output with feedback, sentiment, and product/company name
```

---

## 1. Sentiment Analysis (`sentiment_analysis.py`)

**Purpose:**  
Classifies each feedback as "Positive review", "Negative review", or "Neutral review" using TextBlob.

**How it Works:**
- Reads the input CSV file.
- Checks for the existence of the specified feedback column.
- Applies a sentiment classification function to each feedback:
    - Polarity > 0.1: Positive review
    - Polarity < -0.1: Negative review
    - Otherwise: Neutral review
- Saves the result to a new CSV file.

**Output:**  
`sentiment_output.csv` with columns: `Feedback`, `Sentiment`

---

## 2. Product/Company Extraction (`product.py`)

**Purpose:**  
Identifies and extracts product or company names mentioned in each feedback using spaCy’s NER.

**How it Works:**
- Loads the sentiment-annotated CSV.
- Uses spaCy's English model to process each feedback.
- Extracts entities labeled as `PRODUCT` or `ORG`.
- Adds a new column `Product` with the extracted names (or "Unknown" if none found).
- Saves the enriched data to a new CSV.

**Output:**  
`sentiment_with_product.csv` with columns: `Feedback`, `Sentiment`, `Product`

---

## Requirements

- Python 3.x
- pandas
- textblob
- spacy
- spaCy English model (`en_core_web_sm`)

**Installation:**
```bash
pip install pandas textblob spacy
python -m spacy download en_core_web_sm
python -m textblob.download_corpora
```

## Customization

- **Change `feedback_column`** in `sentiment_analysis.py` if your CSV uses a different column name for feedback.
- **Entity Types:**  
  In `product.py`, you can adjust the entity types extracted (`PRODUCT`, `ORG`) as needed.
