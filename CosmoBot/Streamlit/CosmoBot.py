import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set up OpenAI client using environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define a function to interact with OpenAI API using the latest GPT-4o model
def get_cosmobot_response(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Updated to use the latest GPT-4o model
            messages=[
                {"role": "system", "content": "You are CosmoBot, an advanced astronomy and space exploration tutor powered by the latest GPT-4o model. Provide detailed, accurate, and engaging responses about space, astronomy, and related topics."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=300,  # Increased token limit for more detailed responses
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit UI for CosmoBot
st.markdown("<h1 style='text-align: center;'>Welcome to CosmoBot</h1>", unsafe_allow_html=True)
st.write("Ask me anything about space, astronomy, and beyond! I'm using the latest GPT-4o model for enhanced responses.")

# Input box for user to ask questions
user_input = st.text_input("Enter your question about astronomy:")

# Button to get response from CosmoBot
if st.button("Get Response"):
    if user_input:
        # Fetch response from OpenAI
        response = get_cosmobot_response(user_input)
        # Display the response
        st.write("**CosmoBot:**")
        st.write(response)
    else:
        st.warning("Please enter a question to get started.")

# Additional section to provide context about what CosmoBot can do
st.write("---")
st.write("**What can you ask CosmoBot?**")
st.write("- Learn about planets, stars, galaxies, and cosmic phenomena.")
st.write("- Explore past, current, and future space missions.")
st.write("- Understand complex concepts like black holes, dark matter, and exoplanets.")
st.write("- Get insights on the latest astronomical discoveries and space technology advancements.")
st.write("- Discuss theoretical concepts in astrophysics and cosmology.")