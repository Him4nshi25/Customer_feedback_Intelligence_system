import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\HP\Desktop\data\sentiment_output.csv'

df = pd.read_csv(file_path)

sentiments = ['Positive review', 'Negative review', 'Neutral review']

# Create a DataFrame to hold cumulative counts for each sentiment
cumulative_counts = pd.DataFrame(index=df.index)
for sentiment in sentiments:
    cumulative_counts[sentiment] = (df['Sentiment'] == sentiment).cumsum()

# Plot the sentiment trends
plt.figure(figsize=(10, 6))
for sentiment in sentiments:
    plt.plot(cumulative_counts.index, cumulative_counts[sentiment], label=sentiment)

plt.title('Sentiment Trends Over Sequence of Feedbacks')
plt.xlabel('Feedback Sequence')
plt.ylabel('Cumulative Count')
plt.legend()
plt.tight_layout()
plt.show()
