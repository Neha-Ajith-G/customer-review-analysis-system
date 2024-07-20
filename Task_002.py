import json
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

sys_template = '''
You are a helpful assistant tasked with creating a customer review analysis system. 
You must read each review and determine whether the customer sentiment is positive or negative. 
For positive reviews, you should email the customer {customer_name} a thank-you email and recommend a new product for them to try. 
If the review is negative, you should create an apology email to the customer and send an internal mail to a senior 
customer service representative to address the customer's concern.
'''

Prompt = ChatPromptTemplate.from_messages(
    [
        ("system", sys_template),
        ("user", "{item}")
    ]
)

out = StrOutputParser()

chain = Prompt | llm | out

def load_reviews(file_path):
    with open(file_path, 'r') as file:
        reviews = json.load(file)
    return reviews

products = [
    "Protective Carrying Case",
    "Earbud Tips Replacement Pack",
    "Wireless Charging Pad",
    "Waterproof Case"
]

def save_reviews(reviews, file_path):
    with open(file_path, 'w') as file:
        json.dump(reviews, file, indent=4)

st.title("Customer Review Analysis System")

reviews_file = st.file_uploader("Upload the reviews.json file", type="json")


if reviews_file :
    reviews = json.load(reviews_file)
    

    processed_reviews = []

    for review in reviews:
        chats = [HumanMessage(content=review['text'])]
        response = chain.invoke({"chats": chats, "item": review['text'],"customer_name":review['customer_name']})
        sentiment, email = response.split('\n', 1) 
        customer_name = review.get('customer_name', 'Valued Customer')  
        
        # Replace the placeholder in the email template with the actual customer name
        email_with_name = email.replace("{{customer_name}}", customer_name)

        st.write(f"Email to {review['customer_email']}:\n{email_with_name}")


        processed_reviews.append(review)

    save_reviews(processed_reviews, 'reviews_with_sentiment.json')

    st.success("Reviews have been processed and saved to reviews_with_sentiment.json")