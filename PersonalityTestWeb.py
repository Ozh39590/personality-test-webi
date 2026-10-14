import streamlit as st

st.set_page_config(
    page_title="Personality Test",
    page_icon="✨",
    layout="centered"
)

st.title("PERSONALITY TEST")
st.write("Discover your personality in 10 questions!")
st.write("Choose the answer that fits you best.")

questions = [
    {
        "question": "What would you do on a completely free day?",
        "answers": [
            "Stay home and relax",
            "Hang out with friends",
            "Go somewhere I've never been",
            "Play games or try a creative hobby"
        ]
    },
    {
        "question": "Your friend has a problem. What do you do?",
        "answers": [
            "Listen carefully and give logical advice",
            "Try to cheer them up",
            "Help them find a practical solution",
            "Suggest doing something fun together"
        ]
    },
    {
        "question": "Which place would you rather visit?",
        "answers": [
            "A quiet library",
            "A huge music festival",
            "A mysterious old castle",
            "An art museum"
        ]
    },
    {
        "question": "When you have to make an important decision, you usually...",
        "answers": [
            "Follow my feelings",
            "Think about every possibility",
            "Ask my friends what they think",
            "Trust my instincts"
        ]
    },
    {
        "question": "You suddenly have $1,000. What would you do?",
        "answers": [
            "Save most of it",
            "Travel somewhere",
            "Buy something I've always wanted",
            "Start a new project or hobby"
        ]
    },
    {
        "question": "Which describes you best?",
        "answers": [
            "Curious",
            "Friendly",
            "Imaginative",
            "Calm and thoughtful"
        ]
    },
    {
        "question": "You're invited to a party where you don't know anyone. You...",
        "answers": [
            "Start talking to people immediately",
            "Stay quiet at first and observe",
            "Look for someone interesting to talk to",
            "Probably don't go"
        ]
    },
    {
        "question": "Which activity sounds the most exciting?",
        "answers": [
            "Skydiving",
            "Solving a difficult puzzle",
            "Making a short film",
            "Going on a road trip with friends"
        ]
    },
    {
        "question": "When something doesn't go according to plan, you...",
        "answers": [
            "Make a new plan",
            "Just go with the flow",
            "Ask someone for help",
            "Try to find a creative solution"
        ]
    },
    {
        "question": "If you could have one superpower, which would you choose?",
        "answers": [
            "Teleportation",
            "Reading minds",
            "Time travel",
            "Creating anything I imagine"
        ]
    }
]

personality_points = [
    ["thinker", "social", "adventurer", "creative"],
    ["social", "thinker", "creative", "adventurer"],
    ["thinker", "adventurer", "creative", "social"],
    ["social", "thinker", "adventurer", "creative"],
    ["thinker", "adventurer", "social", "creative"],
    ["adventurer", "social", "creative", "thinker"],
    ["social", "thinker", "creative", "adventurer"],
    ["adventurer", "thinker", "creative", "social"],
    ["thinker", "adventurer", "social", "creative"],
    ["adventurer", "thinker", "creative", "social"]
]

with st.form("personality_quiz"):
    name = st.text_input("What is your name?")

    answers_selected = []

    for i, item in enumerate(questions):
        st.subheader(f"Question {i + 1}")
        st.write(item["question"])

        answer = st.radio(
            "Choose one answer:",
            item["answers"],
            index=None,
            key=f"question_{i}",
            label_visibility="collapsed"
        )

        answers_selected.append(answer)

    submitted = st.form_submit_button("Show My Result")

if submitted:
    if not name.strip():
        st.warning("Please enter your name.")
    elif any(answer is None for answer in answers_selected):
        st.warning("Please answer all 10 questions.")
    else:
        scores = {
            "The Adventurer": 0,
            "The Creative": 0,
            "The Thinker": 0,
            "The Social": 0
        }

        for i, answer in enumerate(answers_selected):
            answer_index = questions[i]["answers"].index(answer)
            personality = personality_points[i][answer_index]

            if personality == "adventurer":
                scores["The Adventurer"] += 1
            elif personality == "creative":
                scores["The Creative"] += 1
            elif personality == "thinker":
                scores["The Thinker"] += 1
            elif personality == "social":
                scores["The Social"] += 1

        result = max(scores, key=scores.get)

        st.divider()
        st.header("YOUR RESULT")
        st.write(f"Nice to meet you, {name.strip()}!")
        st.subheader(result)

        descriptions = {
            "The Adventurer": "You love exploring, trying new things, and embracing new experiences.",
            "The Creative": "You enjoy imagination, original ideas, and expressing yourself.",
            "The Thinker": "You like analyzing situations, solving problems, and thinking carefully.",
            "The Social": "You value friendship, communication, and spending time with people."
        }

        st.write(descriptions[result])

        st.subheader("YOUR SCORES")

        for personality, score in scores.items():
            st.write(f"{personality}: {score}/10")
            st.progress(score / 10)

        st.caption("This is a fun personality quiz, not a scientific assessment.")
