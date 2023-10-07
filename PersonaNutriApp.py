import streamlit as st
import pandas as pd

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
    
    # Lista de razões para serem avaliadas
    reason_list = [
        "Falta de Comprometimento Pessoal",
        "Expectativas Irrealistas",
        "Dificuldade de Adaptação",
        "Falta de Suporte Social",
        "Custos Financeiros",
        "Impaciência",
        "Falta de Acompanhamento Personalizado"
    ]
    
    # Inicializando um dicionário para armazenar as respostas
    reasons = {}
    
    # Opções para avaliação
    options = [1, 2, 3, 4, 5]
    
    # Adicionando uma opção de botão de rádio para cada motivo e organizando-os horizontalmente
    for reason in reason_list:
        reasons[reason] = st.radio(reason, options, help="Avalie dando uma nota de 1 a 5")
    
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
        
        # Convertendo o dicionário reasons em um DataFrame e gerando um gráfico de barras
        reasons_df = pd.DataFrame(list(reasons.items()), columns=['Reason', 'Value'])
        st.bar_chart(reasons_df.set_index('Reason'), height=400)

