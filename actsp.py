import streamlit as st
from PIL import Image

image = Image.open('desenvolvimento.jpg')
st.image(image, caption='Web site em desenvolvimento')
st.header("Cursos Bootcamp")
st.sidebar.title('Menu')
paginaSelecionada = st.sidebar.selectbox('Selecione a Página', ['Bootcamps', 'Contato', 'Página 03'])
if paginaSelecionada == 'Bootcamps':
    st.title('Bootcamps - Descrição dos cursos')    
    cursoSelecionado = st.selectbox('Selecione uma opção: ', ['Ar Condicionado', 'Opção 2', 'Opção 3'])
    if cursoSelecionado == 'Ar Condicionado':
        st.title('Curso Rápido de Instalação de Ar Condicionado (Especialista Edmar - BHD Ar condicionado)')
        st.header('Curso de instalação ar condicionado SPLIT, com demonstração prática.')
        st.write('01)Introdução;')
        st.write('02)Normas Técnicas Relacionadas;')
        st.write('03)Primeiros Passos;')       
        st.write('04)Conhecendo o Equipamento;')
        st.write('05)Ferramentas e Equipamentos Necessários para Instalação;')
        st.write('06)Como escolher 0 Local Correto para instalar  a Unidade Interna;')
        st.write('07)Instalação do Suporte Para Fixar a Unidade Interna;')
        st.write('08)Instalação dos Tubos da Unidade Interna;')
        st.write('09)Como escolher 0 Local Correto para instalar Unidade Externa;')
        st.write('10)Ligação dos Tubos na Unidade Externa;')
        st.write('11)O Procedimento de Gerar Vácuo é Obrigatório na Instalação?')
        st.write('12)Como Gerar Vácuo nas Tubulações;')
        st.write('13)Ciclos de Refrigeração e Aquecimento do Ar Condicionado;')
        st.write('14)Instalação Elétrica;')
        st.write('15)Esquema Elétrico de Ligação;')
        st.write('16)Como Deverá ser Feita a Instalação Elétrica Residencial;')
        st.write('17)Ocorrências de Má Funcionamento do Equipamento')
        #https://certificadocursosonline.com/cursos/curso-de-instalacao-e-manutencao-de-ar-condicionado/      
    elif cursoSelecionado == 'Opção 2':    
        st.title('Título da Opção 2')
        st.write('Em desenvolvimento...')
    elif cursoSelecionado == 'Opção 3':
        st.title('Título da Opção 3')
        st.write('Em desenvolvimento...')
elif paginaSelecionada == 'Contato':    
    st.title('Informações de contato')
    st.write('Prof. Massaki de Oliveira Igarashi')
    st.write('Cel.: +55(11)9 8810-9797')
elif paginaSelecionada == 'Página 03':
    st.title('Título da Página 3')
    st.write('Desenvolvimento de minha 1ª Web Page Python - By Massaki Igarashi')