import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

df = pd.read_csv(r'C:\Users\HP\Desktop\data\sentiment_output.csv')

def extract_product(text):
    doc = nlp(str(text))
    products = [ent.text for ent in doc.ents if ent.label_ in ['PRODUCT', 'ORG']]
    return ', '.join(products) if products else 'Unknown'

df['Product'] = df['Feedback'].apply(extract_product)

df.to_csv(r'C:\Users\HP\Desktop\data\sentiment_with_product.csv', index=False)

print(df[['Feedback', 'Product', 'Sentiment']].head())
