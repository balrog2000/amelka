import streamlit as st


st.title("🐾 Zwierzakowy Quiz!")
st.image('https://www.harrypotter.com/assets/_next/static/images/logo-gold-600-7a7e89b6db1ffeaab025f2091d21b645.png')

# Initialize session state
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False


with st.form("quiz_form"):
    # st.write(f"**Witaj w Hogwarcie, {st.session_state.name}!** 🏰")     
        
    st.write("**Pytanie 1:** Czy koty śpią 16 godzin dziennie?")
    answer1 = st.radio("Odpowiedź:", ["Tak", "Nie"], key="q1", index=None)
    
    st.write("**Pytanie 2:** Czy pies to ssak?")
    answer2 = st.radio("Odpowiedź:", ["Tak", "Nie"], key="q2", index=None)
    
    st.write("**Pytanie 3:** Czy ryby mają skrzela?")
    answer3 = st.radio("Odpowiedź:", ["Tak", "Nie"], key="q3", index=None)
    
    submitted = st.form_submit_button("Sprawdź odpowiedzi!")
    
    if submitted:
        # Calculate score only after form submission
        score = 0
        
        if answer1 == "Tak":
            score += 1
        if answer2 == "Tak":
            score += 1
        if answer3 == "Tak":
            score += 1
        
        st.markdown(f"## Twój wynik: {score}/3")
        
        if score == 3:
            st.balloons()
            st.image("https://images.unsplash.com/photo-1507146426996-ef05306b995a?q=80&w=3570&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", caption="Brawo, Zwierzakowy Mistrzu!")
            st.write("Nagroda dla Ciebie!")
            st.audio('expecto.mp3')
        elif score == 2:
            st.success("Bardzo dobrze! Prawie perfekcyjnie!")
        elif score == 1:
            st.info("Nieźle! Możesz lepiej!")
            st.snow()
        else:
            st.warning("Spróbuj ponownie!")