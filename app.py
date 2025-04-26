import streamlit as st
import random
import time

# Title and Introduction
st.title("🎯 Growth Mindset Adventure 🌱")
st.markdown(""" 
Welcome to the **Growth Mindset Adventure**!  
Get ready for an exciting journey to discover if you're a growth explorer or a fixed thinker. 🌍 Let's dive into it! 🚀 
""")

# Pool of possible questions (more variety)
questions_pool = [
    {
        "question": "When faced with a tough challenge, I believe that:",
        "options": [
            "With effort and learning, I can conquer it! 🏆",
            "I should probably back off before it gets too hard. 😕"
        ],
        "answer": 0
    },
    {
        "question": "I think intelligence is:",
        "options": [
            "Like a muscle — the more I work on it, the stronger it gets! 💪",
            "A fixed gift that I either have or I don't. 🤷‍♂️"
        ],
        "answer": 0
    },
    {
        "question": "When I make a mistake, I usually:",
        "options": [
            "Learn, adapt, and try again like a pro! 🔄",
            "Get discouraged and think I'm not cut out for this. 😓"
        ],
        "answer": 0
    },
    {
        "question": "I prefer tasks that are:",
        "options": [
            "Challenging! I want to grow through the experience. 🌱",
            "Easy and quick! No need to struggle. 💤"
        ],
        "answer": 0
    },
    {
        "question": "When I get feedback, I:",
        "options": [
            "See it as a chance to level up and improve! 📈",
            "Feel like it’s a sign I’m failing. 😬"
        ],
        "answer": 0
    },
    {
        "question": "Effort is:",
        "options": [
            "The secret sauce for success! 🍝",
            "A sign that I’m not naturally good at something. 🤔"
        ],
        "answer": 0
    },
    {
        "question": "If I fail, I think:",
        "options": [
            "Failure is just another step towards success! 🏃‍♀️💨",
            "Maybe I’m just not meant for this. 😔"
        ],
        "answer": 0
    }
]

# Randomly select 4 questions from the pool
selected_questions = random.sample(questions_pool, 4)

# Keep track of the user's answers
user_answers = []

# Display the randomly selected questions and options
for idx, q in enumerate(selected_questions):
    st.subheader(f"💬 {q['question']}")
    choice = st.radio("Choose your answer:", q["options"], key=idx)
    if choice == q["options"][0]:
        user_answers.append(0)
    else:
        user_answers.append(1)

# Submit button
if st.button("Submit 🏁"):
    with st.spinner('Calculating your mindset... ⏳'):
        time.sleep(2)

    # Calculate the score
    score = sum(user_answers)

    # Display the result based on the score
    if score == 0:
        st.success("🎉 You’re a Growth Mindset Champion! 🌟")
        st.markdown("""
        You’re all about learning, growing, and embracing challenges. Keep pushing your limits and exploring new territories! 🧗‍♂️💫
        """)
        
    else:
        st.warning("⚠️ Oops! Looks like you're in Fixed Mindset territory. Let's work on that! 💪")
        st.markdown("""
        It's okay to be here! But don't worry, you can unlock a growth mindset by staying open to learning, trying new things, and embracing failure as a chance to grow! 🚀
        Let's level up together! 🌱
        """)
        