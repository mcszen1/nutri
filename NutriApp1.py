from langchain.llms import OpenAI
import streamlit as st
import pandas as pd
import os
from openai import OpenAI

client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )
promptbase="""
No marketing digital, o conceito de "persona" refere-se a uma representação fictícia do público-alvo de uma empresa ou marca ou serviço. 
Uma persona é criada com base em informações demográficas, comportamentais, psicográficas e outras características relevantes que descrevem um segmento específico do público que a empresa deseja atingir. 
A criação de personas ajuda as empresas a entenderem melhor quem são seus potenciais clientes e como podem direcionar suas estratégias de marketing de maneira mais eficaz.
Você é um nutricionista e quer conhecer melhor seus possíveis novos pacientes através de alguns dados que eles vão fornecer e que vou descrever a seguir.
Com esses dados sua missão será desenvolver e descrever uma persona que resuma os problemas que enfrentam.
Você vai realizar uma lista de tarefas que vou descrever abaixo em indiretamente , em todas vai sempre incentiver e destacar a importância do acompanhamento do profissional nutricionista nas atividades.
A partir desses dados você terá informações básicas como nome [name] , idade [age], gênero [gender] e profissão [profession]. Além disso você terá também uma lista com os principais fatores que tem levado 
estes pacientes a abandonarem o acompanhamento nutricional cada um com um nível de importãncia descritos em [comple] . 
Com esse material deve definir os seguintes itens e apresentá-los no formato de um relatório indicando os tópicos. Use no nome informado para se referir à persona e os outros dados para criá-la com mais
precisão de forma a que o paciente que forneceu os dados se sinta representado por ela: 
a) Definição do problema que a persona tem a partir dos fatores indicados em [comple], considerando os indices númericos para definição dos mais importantes;
b) Descrição dos fatores que incomodam a persona em função dos problemas que relatou, observe que cada fator tem um índice entre 1 e 5 que representam uma escala de maior ou menor importância,
na sua resposta nesta tarefa, considere os pesos diferentes e desenvolve seus arguementos proprocionalmente a maior ou menor importância que os valores indicados de 1 a 5 vão mostrar; 
c) o OBJETIVOs da persona diante do problema 
d) possíveis gatilhos que dispararam na persona a vontade de buscar uma solução 
e) uma lista de possíveis procedimentos para que a pessoa possa enfrentar e minimizar os problemas que relatou em [comple]
f) os benefícios que a persona busca na solução que procura 
Formate suas respostas usando apenas os tópicos de cada tarefa [Problema, DORES, OBJETIVOS, GATILHOS, PROCEDIMENTOS PARA AJUDAR, BENEFÍCIOS]. 
Inicie sempre como se estivesse contanto uma história sobre a persona usando o nome [name] que ela indicou, bem como seus outros dados pessoais coletados.
"""

#openai_api_key = st.text_input('OpenAI API Key', type='password')
os.environ["OPENAI_API_KEY"] == st.secrets["OPENAI_API_KEY"]
#openai_api_key=st.secrets["openai_api_key"]
resposta=""
def generate_response(input_text):

  response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": input_text
    },
    {
      "role": "user",
      "content": "Analise esse paciente e execute as tarefas que está programado para executar"
    }
  ],
  temperature=0.8,
  max_tokens=1024,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

  return completion.choices[0].message

# Função para analisar as respostas e gerar recomendações
def analyze_answers(responses):
    persona = "Persona básica baseada nas respostas fornecidas."
    recommendations = "Recomendações personalizadas baseadas nas respostas fornecidas."
    return persona, recommendations

# Logo

st.image("logonutri2.jpg",use_column_width="False")
# Título do Aplicativo
st.title('CONQUISTE UMA VIDA SAUDÁVEL')

# Introdução/Descrição do Aplicativo
st.header("Faça essa auto-avaliação e crie uma persona que vai tentar representar a sua situação.") 
st.write("Se o acompanhamento nutricional que fez antes não deu certo, quero te conhecer melhor e também te ajudar a retomar sua caminhada para uma vida mais saudável.")
st.write("Nossa jornada juntos começa agora. Avalie a persona e venha me falar mais sobre você em @jv_nutrijansen")
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
        comple=str(list(reasons.items()))
        input_text=promptbase+name+str(age)+gender+profession+comple
        generate_response(input_text)

        
