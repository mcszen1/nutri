from langchain.llms import OpenAI
import streamlit as st
import pandas as pd
promptbase="""
No marketing digital, o conceito de "persona" refere-se a uma representação fictícia do público-alvo de uma empresa ou marca. Uma persona é criada com base em informações demográficas, comportamentais, psicográficas e outras características relevantes que descrevem um segmento específico do público que a empresa deseja atingir. A criação de personas ajuda as empresas a entenderem melhor quem são seus potenciais clientes e como podem direcionar suas estratégias de marketing de maneira mais eficaz.
Aqui estão alguns pontos-chave sobre o conceito de persona no marketing digital e por que ele é importante:
Compreensão do público-alvo: A criação de personas ajuda as empresas a obterem uma compreensão mais profunda de quem são seus clientes ideais, incluindo informações como idade, sexo, ocupação, interesses, hábitos de compra e muito mais.
Personalização de conteúdo: Com personas bem definidas, as empresas podem criar conteúdo mais relevante e direcionado que ressoa com seu público-alvo. Isso inclui a criação de mensagens, campanhas e produtos/serviços adaptados às necessidades e preferências específicas de cada persona.
Melhoria na segmentação: As personas permitem que as empresas segmentem suas campanhas de marketing de forma mais precisa. Isso ajuda a economizar recursos, concentrando-se nas pessoas que têm maior probabilidade de se tornarem clientes.
Desenvolvimento de estratégias eficazes: Com personas, as empresas podem elaborar estratégias de marketing mais eficazes, como a escolha dos canais de marketing certos, a criação de mensagens persuasivas e a definição de metas específicas.
Comunicação mais eficaz: A compreensão das personas permite que as empresas falem a língua de seus clientes e se comuniquem de maneira mais eficaz, aumentando a probabilidade de engajamento e conversão.
Avaliação de resultados: As personas também são úteis na avaliação do desempenho das campanhas de marketing, pois permitem que as empresas comparem o desempenho real com as expectativas em relação a grupos demográficos específicos.
A partir desses dados você deve definir os seguintes itens : 
a) Definição do problema que a persona tem ; 
b) Descrição das dores ou fatores que lhe incomodam por conta deste problema ; 
c) o OBJETIVO da persona diante do problema 
d)  o gatilho que disparou a persona a buscar uma solução e) as barreiras que a persona considera que atrapalham a solução do problema ; 
f) os benefícios que a persona busca na solução que procura 
Considere para a análise os dados sobre os motivos principais que tem feito a persona abandonar o acompanhamento nutricional utilizando os motivos e o indice maior ou menor de importância que ela relatou definidos em:
"""

openai_api_key = st.text_input('OpenAI API Key', type='password')
def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

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
        
       
        # Convertendo o dicionário reasons em um DataFrame e gerando um gráfico de barras
        reasons_df = pd.DataFrame(list(reasons.items()), columns=['Reason', 'Value'])
        st.bar_chart(reasons_df.set_index('Reason'), height=400)

        # Apresentando a persona e as recomendações ao usuário
        st.write("## Persona Criada:")
        st.write(persona)
        st.write("## Recomendações:")
        st.write(recommendations)
        input_text=promptbase+str(list(reasons.items()))
        generate_response(input_text)
        
