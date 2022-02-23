import os
import streamlit as st
import pandas as pd 
import numpy as np
import regex as re


@st.cache(suppress_st_warning=True)
def load_score_table():
    data = pd.read_csv('data/tabela_correcao.csv', sep=',')
    return data

@st.cache(suppress_st_warning=True)
def load_afir(afirm, num):
    tabela = load_score_table()
    score_fix = tabela.iloc[int(re.findall(r'(\d)', afirm)[0])-1, num-1]
    return score_fix

@st.cache(suppress_st_warning=True)
def compulsivity_score(score_final):
    if score_final > 26:
        return 'Compulsão Alimentar Periódica Grave'
    elif score_final <= 17:
        return 'Não Possui Compulsão Alimentar Periódica'
    else:
        return 'Compulsão Alimentar Periódica Moderada'
    

def main():
    st.title('''Escala de Compulsão Alimentar Periódica''')         
    st.subheader(
        '''
            Você encontrará abaixo grupos de afirmações numeradas. Leia todas as afirmações em cada grupo e marque aquela que melhor descreve o modo como você se sente em relação aos problemas que tem para controlar seu comportamento alimentar.
        '''
    )

    afirmacao1 = st.radio(
        "#1",
        ('1. Eu não me sinto constrangido(a) com o meu peso ou o tamanho do meu corpo quando estou com outras pessoas.',
        '2. Eu me sinto preocupado(a) em como pareço para os outros, mas isto, normalmente, não me faz sentir desapontado(a) comigo mesmo(a).',
        '3. Eu fico mesmo constrangido(a) com a minha aparência e o meu peso, o que me faz sentir desapontado(a) comigo mesmo(a).',
        '4. Eu me sinto muito constrangido(a) com o meu peso e, frequentemente, sinto muita vergonha e desprezo por mim mesmo(a). Tento evitar contatos sociais por causa desse constrangimento.')
    )
    score1 =+ load_afir(afirmacao1, 1)

    afirmacao2 = st.radio(
        "#2",
        ('1. Eu não tenho nenhuma dificuldade para comer devagar, de maneira apropriada',
        '2. Embora pareça que eu devore os alimentos, não acabo me sentindo empanturrado(a) por comer demais.',
        '3. Às vezes tendo a comer rapidamente, sentindo-me então desconfortavelmente cheio(a) depois.',
        '4. Eu tenho o hábito de engolir minha comida sem realmente mastigá la. Quando isto acontece, em geral me sinto desconfortavelmente empanturrado(a) por ter comido demais.')
    )
    score2 =+ load_afir(afirmacao2, 2)

    score_final = score1 + score2
    classificacao = compulsivity_score(score_final)
    st.write(classificacao)

if __name__=='__main__':
    main()
