import streamlit as st
import matplotlib.pyplot as plt

# Função para analisar as respostas e gerar recomendações
def analyze_answers(responses):
    # Esta função deve ser expandida com lógica específica para analisar as respostas e gerar recomendações.
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
        "Falta de Comprometimento Pessoal": st.slider("Falta de Comprometimento Pessoal:", 1, 5, 3),
        "Expectativas Irrealistas": st.slider("Expectativas Irrealistas:", 1, 5, 3),
        "Dificuldade de Adaptação": st.slider("Dificuldade de Adaptação:", 1, 5, 3),
        "Falta de Suporte Social": st.slider("Falta de Suporte Social:", 1, 5, 3),
        "Custos Financeiros": st.slider("Custos Financeiros:", 1, 5, 3),
        "Impaciência": st.slider("Impaciência:", 1, 5, 3),
        "Falta de Acompanhamento Personalizado": st.slider("Falta de Acompanhamento Personalizado:", 1, 5, 3),
    }
    submit_button = st.form_submit_button("Analisar Respostas")

# Quando o usuário submeter o formulário, analise as respostas e apresente os resultados
if submit_button:
    st.write(f"## Respostas de {name}:")
    st.write(f"Idade: {age}, Sexo: {gender}, Profissão: {profession}")
    st.write("Avaliações para os motivos de abandono:")
    for reason, value in reasons.items():
        st.write(f"{reason}: {value}")
    
    # Analisando as respostas e gerando recomendações (a lógica aqui deve ser expandida conforme necessário)
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
    



