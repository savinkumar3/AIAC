def analyze_sentiment():
    positive_words = {'awesome', 'excellent', 'good', 'great', 'fantastic', 'amazing', 'happy', 'love', 'wonderful'}
    negative_words = {'bad', 'terrible', 'awful', 'poor', 'sad', 'hate', 'horrible', 'worst', 'disappointing'}

    text = input("Enter your sentence: ").lower()
    sentiment = 'neutral'

    if any(word in text for word in positive_words):
        sentiment = 'positive'
    elif any(word in text for word in negative_words):
        sentiment = 'negative'

    print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    analyze_sentiment()