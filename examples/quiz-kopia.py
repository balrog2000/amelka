import streamlit as quiz
quiz.title("Quiz o Amelce")
quiz.write('o której godz.się urodziłam?')
quiz.radio('Odpowiedź:', ['12:45', '11:35', '14:25'],index=None)
quiz.write('jakie jest moje ulubione zwierzę?')
quiz.radio('Odp:',['pies','kot','królik'],index=None)
quiz.write('jaki jest mój ulubiony sport?')
quiz.radio('Odp:',['siatkówka',' speedball','badminton'],index=None)
quiz.write('jak bym nazwała swojego kota?')
quiz.radio('Odp:',['Sylwester','Pikolo','Lucian'],index=None)
quiz.write('jakie są moje ulubione kolory ?')
quiz.radio('Odp:',['beżowy i pastelowy zielony','fioletowy i biały','zielony i biały'],index=None)



