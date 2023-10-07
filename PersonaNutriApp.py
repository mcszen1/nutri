import streamlit as st

# Função para analisar as respostas e gerar recomendações
def analyze_answers(responses):
    persona = "Persona básica baseada nas respostas fornecidas."
    recommendations = "Recomendações personalizadas baseadas nas respostas fornecidas."
    return persona, recommendations

# Título do Aplicativo
st.title('Aplicativo de Acompanhamento Nutricional')

# Introdução/Descrição do Aplicativo
st.write("Este aplicativo visa ajudar a entender os desafios enfrentados durante o acompanhamento nutricional e fornecer recomendações personalizadas.")

# Formulário para coletar informações do usuário
with st.form("user_input_form"):
    st.write("## Por favor, preencha as informações abaixo:")
    name = st.text_input("Nome do Paciente:", "")
    age = st.number_input("Idade:", min_value=1, max_value=100)
    gender = st.selectbox("Sexo:", options=["", "Feminino", "Masculino", "Outro"])
    profession = st.text_input("Profissão:", "")
    
    st.write("## Avalie os seguintes motivos para abandonar o acompanhamento nutricional em uma escala de 1 a 5:")
    reasons = {
        "Falta de Comprometimento Pessoal": st.selectbox("Falta de Comprometimento Pessoal:", [1, 2, 3, 4, 5]),
        "Expectativas Irrealistas": st.selectbox("Expectativas Irrealistas:", [1, 2, 3, 4, 5]),
        "Dificuldade de Adaptação": st.selectbox("Dificuldade de Adaptação:", [1, 2, 3, 4, 5]),
        "Falta de Suporte Social": st.selectbox("Falta de Suporte Social:", [1, 2, 3, 4, 5]),
        "Custos Financeiros": st.selectbox("Custos Financeiros:", [1, 2, 3, 4, 5]),
        "Impaciência": st.selectbox("Impaciência:", [1, 2, 3, 4, 5]),
        "Falta de Acompanhamento Personalizado": st.selectbox("Falta de Acompanhamento Personalizado:", [1, 2, 3, 4, 5]),
    }
    submit_button = st.form_submit_button("Analisar Respostas")

# Quando o usuário submeter o formulário, analise as respostas e apresente os resultados
if submit_button:
    st.write(f"## Respostas de {name}:")
    st.write(f"Idade: {age}, Sexo: {gender}, Profissão: {profession}")
    st.write("Avaliações para os motivos de abandono:")
    for reason, value in reasons.items():
        st.write(f"{reason}: {value}")
    
    persona, recommendations = analyze_answers({
        "name": name,
        "age": age,
        "gender": gender,
        "profession": profession,
        "reasons": reasons
    })
    
    # Apresentando a persona e as recomendações ao usuário
    st.write("## Persona Criada:")
    st.write(persona)
    st.write("## Recomendações:")
    st.write(recommendations)
    
    # Gerando um gráfico para visualizar as avaliações dos motivos de abandono usando a funcionalidade nativa de gráficos do Streamlit
    st.bar_chart(data=reasons, height=400)



