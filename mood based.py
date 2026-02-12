import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Mood-Based Productivity Assistant", page_icon="🧠")

st.title("🧠 Mood-Based Productivity Assistant")
st.write("Type how you feel in your own words — I’ll suggest helpful actions")

# -------------------------
# USER NAME
# -------------------------
name = st.text_input("Enter your name")
if name:
    st.success(f"Welcome {name} 🌸")

# -------------------------
# USER MOOD TEXT INPUT
# -------------------------
user_mood_text = st.text_input("How are you feeling today? (in your own words)")

# -------------------------
# MOOD DETECTION FUNCTION
# -------------------------
def detect_mood(text):
    text = text.lower()

    if any(word in text for word in ["happy", "good", "great", "excited", "awesome"]):
        return "Happy 😊"

    elif any(word in text for word in ["sad", "down", "upset", "cry", "hurt"]):
        return "Sad 😔"

    elif any(word in text for word in ["stress", "busy", "pressure", "overload"]):
        return "Stressed 😫"

    elif any(word in text for word in ["tired", "sleepy", "exhausted", "low energy"]):
        return "Tired 😴"

    elif any(word in text for word in ["anxious", "worried", "nervous", "fear"]):
        return "Anxious 😟"

    elif any(word in text for word in ["lazy", "no mood", "unmotivated", "blank"]):
        return "Unmotivated 😶"

    else:
        return "Neutral 😐"


# -------------------------
# MOOD LEVEL
# -------------------------
mood_level = st.slider("Mood intensity", 1, 10, 5)

# -------------------------
# SUGGESTIONS DATA
# -------------------------
suggestions = {
    "Happy 😊": [
        "Work on creative tasks",
        "Start a mini side project",
        "Help someone today",
        "Learn something new"
    ],
    "Sad 😔": [
        "Listen to calm music",
        "Talk to a friend",
        "Go for a short walk",
        "Write your feelings"
    ],
    "Stressed 😫": [
        "Do deep breathing",
        "Take a short break",
        "List top 3 priorities",
        "Stretch your body"
    ],
    "Tired 😴": [
        "Take a 20-minute nap",
        "Drink water",
        "Light stretching",
        "Step outside briefly"
    ],
    "Anxious 😟": [
        "Try box breathing",
        "Grounding exercise 5-4-3-2-1",
        "Reduce screen time",
        "Talk to someone"
    ],
    "Unmotivated 😶": [
        "Start a 5-minute task",
        "Clean your desk",
        "Review your goals",
        "Break work into tiny steps"
    ],
    "Neutral 😐": [
        "Plan your day",
        "Organize tasks",
        "Learn something small",
        "Do one productive action"
    ]
}

feel_good_tips = [
    "Drink water 💧",
    "Take 10 deep breaths 🌿",
    "Listen to your favorite song 🎵",
    "Sit in sunlight ☀️",
    "Message a friend ❤️",
    "Write gratitude list ✍️",
    "Smile intentionally 🙂"
]

quotes = [
    "Small progress is still progress 🚀",
    "You are stronger than you think 💪",
    "One step at a time 🌱",
    "Keep going — you got this 🔥"
]

# -------------------------
# SESSION HISTORY
# -------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------
# BUTTON ACTION
# -------------------------
if st.button("Analyze Mood & Suggest") and user_mood_text:

    detected_mood = detect_mood(user_mood_text)
    st.session_state.history.append(detected_mood)

    st.subheader("🧭 Detected Mood")
    st.write(detected_mood)

    st.subheader("✨ Recommended Activity")
    st.success(random.choice(suggestions[detected_mood]))

    st.subheader("🌿 Feel Good Tip")
    st.info(random.choice(feel_good_tips))

    st.subheader("💬 Motivation")
    st.warning(random.choice(quotes))

    if mood_level >= 8 and detected_mood in ["Sad 😔", "Stressed 😫", "Anxious 😟"]:
        st.error("High mood intensity detected — please take extra care and rest ❤️")

# -------------------------
# JOURNAL
# -------------------------
st.subheader("📓 Journal")
journal = st.text_area("Write your thoughts")
if st.button("Save Journal"):
    st.success("Saved for this session ✅")

# -------------------------
# TODO LIST
# -------------------------
st.subheader("📝 To-Do")
tasks = st.text_area("Enter tasks (one per line)")
if tasks:
    for t in tasks.split("\n"):
        st.checkbox(t)

# -------------------------
# MOOD CHART
# -------------------------
st.subheader("📊 Mood History")
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history, columns=["Mood"])
    st.bar_chart(df["Mood"].value_counts())

st.caption("Mini Project — Mood Based Productivity Assistant 🚀")
