import random
import streamlit as st

st.title("🎯 Number Guessing Game")

levels = {
    "Easy": 50,
    "Medium": 100,
    "Hard": 500,
    "Extreme": 1000
}

difficulty = st.selectbox("Select Difficulty", list(levels.keys()))
max_num = levels[difficulty]

if "started" not in st.session_state:
    st.session_state.started = False

if "num" not in st.session_state:
    st.session_state.num = random.randint(1, max_num)

if "count" not in st.session_state:
    st.session_state.count = 0

if "won" not in st.session_state:
    st.session_state.won = False

if st.button("Start Game"):
    st.session_state.started = True
    st.session_state.num = random.randint(1, max_num)
    st.session_state.count = 0
    st.session_state.won = False

if st.session_state.started:
    st.write(f"Guess a number between **1 and {max_num}**")

    guess = st.number_input(
        "Enter your guess",
        min_value=1,
        max_value=max_num,
        step=1
    )

    if st.button("Submit Guess") and not st.session_state.won:
        st.session_state.count += 1

        if guess < st.session_state.num:
            st.warning("⬆️ Number is higher!")

        elif guess > st.session_state.num:
            st.warning("⬇️ Number is lower!")

        else:
            st.success("🎉 Congratulations! You guessed it right!")
            st.balloons()
            st.markdown(f"You took **{st.session_state.count} attempts**")
            st.session_state.won = True

        diff = abs(guess - st.session_state.num)
        if diff <= 2 and guess != st.session_state.num:
            st.info("🔥 Very close!")

    st.write("Attempts:", st.session_state.count)

    if st.button("Restart Game"):
        st.session_state.num = random.randint(1, max_num)
        st.session_state.count = 0
        st.session_state.won = False
        st.rerun()

