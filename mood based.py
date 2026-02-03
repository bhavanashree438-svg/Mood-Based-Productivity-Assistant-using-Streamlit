import streamlit as st
import random

st.set_page_config(page_title="Mood-Based Productivity Assistant")

st.title("🧠 Mood-Based Productivity Assistant")
st.write("A unique mini project using Streamlit")

mood = st.selectbox(
    "How are you feeling today?",
    ["Happy 😊", "Sad 😔", "Stressed 😫", "Tired 😴"]
)

suggestions = {
    "Happy 😊": [
        "Work on creative tasks",
        "Learn a new skill",
        "Help someone today"
    ],
    "Sad 😔": [
        "Listen to calm music",
        "Talk to a friend",
        "Take a short walk"
    ],
    "Stressed 😫": [
        "Do deep breathing",
        "Take a 10-minute break",
        "Write a to-do list"
    ],
    "Tired 😴": [
        "Power nap for 20 minutes",
        "Drink water",
        "Do light stretching"
    ]
}

quotes = [
    "Believe in yourself 🌱",
    "Small steps every day 💪",
    "You are doing great 🌟",
    "Progress, not perfection 🚀"
]

if st.button("Get Suggestions"):
    st.subheader("✨ Recommended Activity")
    st.success(random.choice(suggestions[mood]))

    st.subheader("💬 Motivation Quote")
    st.info(random.choice(quotes))
