import streamlit as st

with st.form("quiz_form"):
    st.title("🐾 Zwierzakowy Quiz!")
    st.write("**Pytanie 1:** Czy koty śpią 16 godzin dziennie?")
    answer1 = st.radio("Odpowiedź:", ["Tak", "Nie", "Nie wiem"], key="q1", index=None)
    st.write("**Pytanie 2:** Czy pies to ssak?")
    answer2 = st.radio("Odpowiedź:", ["Tak", "Nie", "Nie wiem"], key="q2", index=None)
    st.write("**Pytanie 3:** Czy ryby mają skrzela?")
    answer3 = st.radio("Odpowiedź:", ["Tak", "Nie", "Nie wiem"], key="q3", index=None)
    submitted = st.form_submit_button("Sprawdź odpowiedzi!")

if submitted:
    st.write(f"Odpowiedź 1: {answer1}")
    st.write(f"Odpowiedź 2: {answer2}")
    st.write(f"Odpowiedź 3: {answer3}")
        