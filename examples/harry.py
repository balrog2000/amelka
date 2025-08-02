import streamlit as st

st.title("⚡ Quiz Czarodzieja")

name = st.text_input("Jak masz na imię, młody czarodzieju?")

if name:
    st.markdown(f"**Witaj w Hogwarcie, {name}!** 🏰")

    score = 0

    st.subheader("🧪 Pytanie 1")
    if st.radio("Jakiego koloru jest dom Gryffindoru?", ["Zielony", "Niebieski", "Czerwony"]) == "Czerwony":
        score += 1

    st.subheader("🧙 Pytanie 2")
    if st.radio("Jak nazywa się sowa Harry'ego?", ["Hedwiga", "Errol", "Kruk"]) == "Hedwiga":
        score += 1

    st.subheader("🧹 Pytanie 3")
    if st.radio("Na czym latają czarodzieje?", ["Miotła", "Zwierzę", "Chmura"]) == "Miotła":
        score += 1

    st.markdown(f"### ✨ Wynik: {score}/3")

    if score == 3:
        st.success("Gratulacje! Zdobywasz 100 punktów dla swojego domu! 🏆")
        st.balloons()
    elif score == 2:
        st.info("Nieźle! Ale musisz jeszcze trochę poćwiczyć zaklęcia...")
    else:
        st.warning("Hmm... czy jesteś pewien, że nie jesteś mugolem? 😅")