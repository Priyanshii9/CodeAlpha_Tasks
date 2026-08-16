import streamlit as st
import random

# Word list
words = ["apple", "banana", "python", "game", "code", "streamlit", "hangman", "india", "lucknow"]
word = random.choice(words)
guessed_letters = []
attempts = 6

st.title("🎮 Hangman Game")

# Show blanks
display_word = "".join([letter if letter in guessed_letters else "_ " for letter in word])
st.write("Word: ", display_word)

# Show attempts counter
st.metric("Attempts left", attempts)

# Show guessed letters
st.write("Guessed letters:", guessed_letters)

# User input
guess = st.text_input("Enter a letter:").lower()

if guess:
    if guess in guessed_letters:
        st.warning("You already guessed that letter!")
    elif guess in word:
        guessed_letters.append(guess)
        st.success(f"Good guess! '{guess}' is in the word.")
    else:
        attempts -= 1
        st.error(f"Wrong guess! Attempts left: {attempts}")

    # Update word display
    display_word = "".join([letter if letter in guessed_letters else "_ " for letter in word])
    st.write("Word: ", display_word)

    # Check win/lose
    if all(letter in guessed_letters for letter in word):
        st.success("🎉 Congratulations! You guessed the word!")
    elif attempts == 0:
        st.error(f"Game Over! The word was '{word}'.")

# Restart button
if st.button("Restart Game"):
    st.experimental_rerun()
