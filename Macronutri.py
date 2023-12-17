import streamlit as st

def calcular_tmb(peso, altura, idade, sexo):
    if sexo == 'Homem':
        return 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
    else:
        return 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)

def calcular_macronutrientes(calorias_diarias):
    # Exemplo de distribuição: 50% carboidratos, 30% proteínas, 20% gorduras
    return {
        'Carboidratos': (calorias_diarias * 0.50) / 4,
        'Proteínas': (calorias_diarias * 0.30) / 4,
        'Gorduras': (calorias_diarias * 0.20) / 9
    }

# Interface Streamlit
st.title('Calculadora de Macronutrientes')

# Inputs do usuário
peso = st.number_input('Peso (kg)', min_value=1)
altura = st.number_input('Altura (cm)', min_value=1)
idade = st.number_input('Idade', min_value=1)
sexo = st.selectbox('Sexo', ['Homem', 'Mulher'])
nivel_atividade = st.selectbox('Nível de Atividade Física', 
                               ['Sedentário', 'Leve', 'Moderado', 'Ativo', 'Muito Ativo'])
objetivo = st.selectbox('Objetivo', ['Perder Peso', 'Manter Peso', 'Ganhar Massa'])

# Calculando TMB e calorias de manutenção
tmb = calcular_tmb(peso, altura, idade, sexo)
fatores_atividade = {'Sedentário': 1.2, 'Leve': 1.375, 'Moderado': 1.55, 'Ativo': 1.725, 'Muito Ativo': 1.9}
calorias_manutencao = tmb * fatores_atividade[nivel_atividade]

# Ajustando pelas metas
if objetivo == 'Perder Peso':
    calorias_diarias = calorias_manutencao - 500
elif objetivo == 'Ganhar Massa':
    calorias_diarias = calorias_manutencao + 500
else:
    calorias_diarias = calorias_manutencao

# Calculando macronutrientes
macronutrientes = calcular_macronutrientes(calorias_diarias)

# Mostrando resultados
if st.button('Calcular Macronutrientes'):
    st.write(f"Calorias para Manutenção: {calorias_manutencao:.2f} kcal")
    st.write(f"Calorias Diárias (com base no objetivo): {calorias_diarias:.2f} kcal")
    st.write("Distribuição de Macronutrientes:")
    st.write(f"Carboidratos: {macronutrientes['Carboidratos']:.2f}g")
    st.write(f"Proteínas: {macronutrientes['Proteínas']:.2f}g")
    st.write(f"Gorduras: {macronutrientes['Gorduras']:.2f}g")
