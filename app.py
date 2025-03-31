try:
    import streamlit as st
    import random
except ModuleNotFoundError:
    print("Error: The 'streamlit' module is not installed. Please install it using 'pip install streamlit' and try again.")
    exit()

def get_response(user_input):
    greetings = ["Hello! How are you feeling today?", "Hi there! Hope you're having a wonderful day!", "Good to see you! What's on your mind?"]
    health_tips = ["Don't forget to drink enough water today!", "A short walk will keep you healthy!", "Time for some brain exercises. Want to try a memory game?"]
    companionship = ["Would you like to hear a story?", "I can play your favorite old songs. Let me know what you love!", "How about some relaxation exercises?"]
    
    if "hello" in user_input.lower() or "hi" in user_input.lower():
        return random.choice(greetings)
    elif "health" in user_input.lower() or "reminder" in user_input.lower():
        return random.choice(health_tips)
    elif "lonely" in user_input.lower() or "bored" in user_input.lower():
        return random.choice(companionship)
    else:
        return "I'm here for you! Tell me more about your day."

# Streamlit UI
st.title("👵 AI-Powered Elderly Companion")
st.write("A friendly AI assistant for elderly users!")

# User Input
user_input = st.text_input("Say something:")
if user_input:
    response = get_response(user_input)
    st.write("🤖 AI Assistant: ", response)

st.sidebar.header("Features")
st.sidebar.write("✔ Personalized greetings")
st.sidebar.write("✔ Health & wellness reminders")
st.sidebar.write("✔ Companionship & entertainment")

st.sidebar.write("👩‍⚕️ Designed to provide emotional support and cognitive engagement.")
