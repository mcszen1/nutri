import streamlit as st

def calcular_imc(peso, altura):
    altura1 = altura / 100  # Convertendo centímetros para metros
    return peso / (altura1 ** 2)


def calcular_tmb_harris_benedict(peso, altura, idade, sexo):
    if sexo == 'Masculino':
        return 66 + (13.8 * peso) + (5 * altura) - (6.8 * idade)
    else:
        return 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)

def calcular_tmb_mifflin_st_jeor(peso, altura, idade, sexo):
    if sexo == 'Masculino':
        return (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    else:
        return (10 * peso) + (6.25 * altura) - (5 * idade) - 161

def calcular_tmb_cunningham(lean_body_mass):
    return 500 + (22 * lean_body_mass)

def calcular_tmb_tinsley(lean_body_mass):
    # Esta é uma versão simplificada, pois a fórmula específica de Tinsley não é tão comum.
    return calcular_tmb_cunningham(lean_body_mass)

def calcular_necessidades_caloricas(tmb, nivel_atividade):
    # Aqui, você pode adicionar a lógica para calcular as necessidades calóricas com base no TMB e no nível de atividade
    pass

def distribuicao_macronutrientes(calorias):
    # Aqui, você pode adicionar a lógica para calcular a distribuição de macronutrientes
    pass

st.title('Aplicativo de Avaliação Nutricional')

peso = st.number_input('Peso (kg)', min_value=0.0, format="%.2f")
altura = st.number_input('Altura (cm)', min_value=0.0, format="%.2f")
idade = st.number_input('Idade', min_value=0, max_value=120, step=1)
sexo = st.selectbox('Sexo', ['Masculino', 'Feminino'])

formula_tmb = st.selectbox('Fórmula para TMB', ['Harris-Benedict', 'Mifflin-St Jeor', 'Cunningham', 'Tinsley'])

if st.button('Calcular'):
    imc = calcular_imc(peso, altura)
    
    if formula_tmb == 'Harris-Benedict':
        tmb = calcular_tmb_harris_benedict(peso, altura, idade, sexo)
    elif formula_tmb == 'Mifflin-St Jeor':
        tmb = calcular_tmb_mifflin_st_jeor(peso, altura, idade, sexo)
    elif formula_tmb in ['Cunningham', 'Tinsley']:
        lean_body_mass = st.number_input('Massa Corporal Magra (kg)', min_value=0.0, format="%.2f")
        if formula_tmb == 'Cunningham':
            tmb = calcular_tmb_cunningham(lean_body_mass)
        else:
            tmb = calcular_tmb_tinsley(lean_body_mass)

    st.write(f"IMC: {imc:.2f}")
    st.write(f"TMB: {tmb:.2f}")
    # Adicionar apresentação de outras métricas

# Aqui você pode continuar expandindo o aplicativo conforme necessário.
