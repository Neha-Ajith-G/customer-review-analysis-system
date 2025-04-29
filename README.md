# customer-review-analysis-system

This application analyzes customer reviews to determine sentiment (positive or negative) and generates appropriate email responses. It uses Google Generative AI via LangChain for natural language processing and sentiment analysis.

Features:
1. Sentiment Analysis: Determines whether a review is positive or negative.
2. Email Generation:
  a)It generates a thank-you email for positive reviews and recommends a new product.
  b)For negative reviews, it creates an apology email and drafts an internal email for escalation.
3. File Upload: Accepts a reviews.json file containing customer reviews.
4. Processed Output: Displays generated emails and saves processed reviews with sentiment analysis to reviews_with_sentiment.json.

   
How It Works:

1. Upload a JSON file containing customer reviews.
2. The system processes each review using a pre-defined prompt and AI model.
3. Emails are generated and displayed for each review.
4. The processed reviews are saved to a new JSON file.

   
Requirements:
1.  Python
2.  Streamlit
3.  LangChain
4.  Google Generative AI
5.  dotenv
