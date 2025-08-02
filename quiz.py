import streamlit as quiz
quiz.title("Quiz o Amelce")
wiek_amelki = 10 
quiz.write(2*wiek_amelki)
with quiz.form('quiz_form'):
    quiz.write('o której godz.się urodziłam?')
    odp1 = quiz.radio('Odp:', ['12:45', '11:35', '14:25'],index=None)
    quiz.write('jakie jest moje ulubione zwierzę?')
    odp2 = quiz.radio('Odp:',['pies','kot','królik'],index=None)
    quiz.write('jaki jest mój ulubiony sport?')
    odp3 = quiz.radio('Odp:',['siatkówka',' speedball','badminton'],index=None)
    quiz.write('jak bym nazwała swojego kota?')
    odp4 = quiz.radio('Odp:',['Sylwester','Pikolo','Lucian'],index=None)
    quiz.write('jakie są moje ulubione kolory ?')
    odp5 = quiz.radio('Odp:',['beżowy i pastelowy zielony','fioletowy i biały','zielony i biały'],index=None)
    quiz.form_submit_button('Sprawdź odpowiedzi!')
    quiz.write('Odpowiedź 1: ' + odp1)
    quiz.write('Odpowiedź 2: ' + odp2)
    quiz.write('Odpowiedź 3: ' + odp3)
    quiz.write('Odpowiedź 4: ' + odp4)
    quiz.write('Odpowiedź 5: ' + odp5)
    wynik = 0
    if odp1 == '12:45':
        wynik = 1
    
    
    if odp2 == 'kot':
        wynik = wynik + 1
    if odp3 == 'badminton':
        wynik =wynik + 1
    if odp4 == 'Pikolo':
        wynik = wynik + 1
    if odp5 == 'beżowy i pastelowy zielony':
        wynik = wynik + 1
    quiz.write('twój wynik '+ str(wynik))
    if wynik == 5:
        quiz.balloons()




