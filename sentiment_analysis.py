import pandas as pd
from textblob import TextBlob

file_path = r'C:\Users\HP\Desktop\data\merge-csv.com__6853d1f34c30b.csv'
df = pd.read_csv(file_path, encoding='latin1') 

feedback_column = 'feedback' 

if feedback_column not in df.columns:
    print(f"Column '{feedback_column}' not found in CSV file. Available columns: {df.columns.tolist()}")
else:
    feedbacks = df[feedback_column].dropna()

    def classify_sentiment(text):
        analysis = TextBlob(str(text))
        if analysis.sentiment.polarity > 0.1:
            return 'Positive review'
        elif analysis.sentiment.polarity < -0.1:
            return 'Negative review'
        else:
            return 'Neutral review'

    df['Sentiment'] = feedbacks.apply(classify_sentiment)

    for feedback, sentiment in zip(feedbacks, df['Sentiment']):
        print(f'Feedback: {feedback}\nSentiment: {sentiment}\n')
        
    output_df = pd.DataFrame({'Feedback': feedbacks, 'Sentiment': df.loc[feedbacks.index, 'Sentiment']})
    output_df.to_csv(r'C:\Users\HP\Desktop\data\sentiment_output.csv', index=False)
