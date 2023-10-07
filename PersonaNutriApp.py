
import streamlit as st

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
    reasons = st.multiselect("Motivos para Abandonar o Acompanhamento Anterior:",
                             options=["Falta de Comprometimento Pessoal",
                                      "Expectativas Irrealistas",
                                      "Dificuldade de Adaptação",
                                      "Falta de Suporte Social",
                                      "Custos Financeiros",
                                      "Impaciência",
                                      "Falta de Acompanhamento Personalizado"],
                             default=None)
    submit_button = st.form_submit_button("Analisar Respostas")

# Quando o usuário submeter o formulário, analise as respostas e apresente os resultados
if submit_button:
    st.write(f"## Respostas de {name}:")
    st.write(f"Idade: {age}, Sexo: {gender}, Profissão: {profession}")
    st.write(f"Motivos para Abandonar o Acompanhamento Anterior: {', '.join(reasons) if reasons else 'Nenhum motivo selecionado'}")
    
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
