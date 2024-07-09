import streamlit as st

# Título
st.write('# Cadastro de dados')

# Atribuições
cont = 1
numero = cont
button2 = False


while True:
    # Nome
    nome = st.text_input('Informe seu nome completo: ', value='', key=f'nome {numero}').strip()

    cont_nome = len(nome)
    if cont_nome <= 3:
        if nome:
            st.write('O nome informado é muito pequeno!\n')

    # Idade
    idade = st.number_input('Informe sua idade: ', step=1, min_value=0, max_value=150, key=f'idade {numero}')

    if idade < 0 or idade > 150:
        if idade:
            st.write('Informe uma idade válida!\n')

    # Salário
    salario = st.number_input('Informe o seu salário mensal: ', min_value=0, key=f'salario {numero}')

    if salario < 0:
        if salario:
            st.write('Digite um valor válido!\n')

    # Sexo
    sexo = st.selectbox('Informe seu sexo:', ('', 'Masculino', 'Feminino'), 0, key=f'sexo {numero}')

    # Estado Civil
    civil = st.selectbox('Informe seu estado civil:', ('', 'Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viuvo(a)'), 0,
                         key=f'civil {numero}')

    # Finalização
    button = st.button('Salvar')

    if button:
        button2 = st.button('Novo cadastro')

        st.write('\n\nSeus dados foram registrados com sucesso!\n')
        st.write(f'Nome: {nome}')
        st.write(f'Idade: {idade}')
        st.write(f'Salário: {salario}')
        st.write(f'Sexo: {sexo}')
        st.write(f'Estado civil: {civil}')
        st.write(cont)

        with open(f'Arquivos\{cont}.txt', 'w') as txt:
            txt.write(f'{nome} {idade} {salario} {sexo} {civil}')

    if button2:
        cont += 1
        pass
    elif button2 is False:
        break
