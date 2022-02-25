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

    afirmacao3 = st.radio(
        "#3",
        ('1. Eu me sinto capaz de controlar meus impulsos para comer, quando eu quero.',
         '2. Eu sinto que tenho falhado em controlar meu comportamento alimentar mais do que a média das pessoas.',
         '3. Eu me sinto totalmente incapaz de controlar meus impulsos para comer.',
         '4. Por me sentir tão incapaz de controlar meu comportamento alimentar, entro em desespero tentando manter o controle.')
    )
    score3 =+ load_afir(afirmacao3, 3)

    afirmacao4 = st.radio(
        "#4",
        ('1. Eu não tenho o hábito de comer quando estou chateado(a).',
         '2. Às vezes eu como quando estou chateado(a) mas, frequentemente, sou capaz de me ocupar e afastar minha mente da comida.',
         '3. Eu tenho o hábito regular de comer quando estou chateado(a) mas, de vez em quando, posso usar alguma outra atividade para afastar minha mente da comida.',
         '4. Eu tenho o forte hábito de comer quando estou chateado(a). Nada parece me ajudar a parar com esse hábito.')
    )
    score4 =+ load_afir(afirmacao4, 4)

    afirmacao5 = st.radio(
        "#5",
        ('1. Normalmente quando como alguma coisa é porque estou fisicamente com fome.',
         '2. De vez em quando como alguma coisa por impulso, mesmo quando não estou realmente com fome.',
         '3. Eu tenho o hábito regular de comer alimentos que realmente não aprecio para satisfazer uma sensação de fome, mesmo que fisicamente eu não necessite de comida.',
         '4. Mesmo que não esteja fisicamente com fome, tenho uma sensação de fome em minha boca que somente parece ser satisfeita quando eu como um alimento, tipo um sanduíche, que enche a minha boca. Às vezes, quando eu como o alimento para satisfazer minha “fome na boca”, em seguida eu o cuspo, assim não ganharei peso.'),
    )
    score5 =+ load_afir(afirmacao5, 5)

    afirmacao6 = st.radio(
        "#6",
        ('1. Eu não sinto qualquer culpa ou ódio de mim mesmo(a) depois de comer demais.',
         '2. De vez em quando sinto culpa ou ódio de mim mesmo(a) depois de comer demais.',
         '3. Quase o tempo todo sinto muita culpa ou ódio de mim mesmo(a) depois de comer demais.'),
    )
    score6 =+ load_afir(afirmacao6, 6)
        
    afirmacao7 = st.radio(
        "#7",
        ('1. Eu não perco o controle total da minha alimentação quando estou em dieta, mesmo após períodos em que como demais.',
         '2. Às vezes, quando estou em dieta e como um alimento proibido, sinto como se tivesse estragado tudo e como ainda mais.',
         '3. Frequentemente, quando como demais durante uma dieta, tenho o hábito de dizer para mim mesmo(a): “agora que estraguei tudo, porque não irei até o fim”. Quando isto acontece, eu como ainda mais.',
         '4. Eu tenho o hábito regular de começar dietas rigorosas por mim mesmo(a), mas quebro as dietas entrando numa compulsão alimentar. Minha vida parece ser “uma festa” ou “um morrer de fome”.'),
    )
    score7 =+ load_afir(afirmacao7, 7)
            
    afirmacao8 = st.radio(
        "#8",
        ('1. Eu raramente como tanta comida a ponto de me sentir desconfortavelmente empanturrado(a) depois.',
         '2. Normalmente, cerca de uma vez por mês, como uma tal quantidade de comida que acabo me sentindo muito empanturrado(a).',
         '3. Eu tenho períodos regulares durante o mês, quando como grandes quantidades de comida, seja na hora das refeições, seja nos lanches.',
         '4. Eu como tanta comida que, regularmente, me sinto bastante desconfortável depois de comer e, algumas vezes, um pouco enjoado(a).')
    )
    score8 =+ load_afir(afirmacao8, 8)

    afirmacao9 = st.radio(
        "#9",
        ('1. Em geral, minha ingesta calórica não sobe a níveis muito altos, nem desce a níveis muito baixos.',
         '2. Às vezes, depois de comer demais, tento reduzir minha ingesta calórica para quase nada, para compensar o excesso de calorias que ingeri.',
         '3. Eu tenho o hábito regular de comer demais durante a noite. Parece que a minha rotina não é estar com fome de manhã, mas comer demais à noite', 
         '4. Na minha vida adulta tenho tido períodos, que duram semanas, nos quais praticamente me mato de fome. Isto se segue a períodos em que como demais. Parece que vivo uma vida de “festa” ou de “morrer de fome”.')
    )
    score9 =+ load_afir(afirmacao9, 9)

    afirmacao10 = st.radio(
        "#10",
        ('1. Normalmente eu sou capaz de parar de comer quando quero. Eu sei quando “já chega”.',
         '2. De vez em quando, eu tenho uma compulsão para comer que parece que não posso controlar.',
         '3. Frequentemente tenho fortes impulsos para comer que parece que não sou capaz de controlar, mas, em outras ocasiões, posso controlar meus impulsos para comer.',
         '4. Eu me sinto incapaz de controlar impulsos para comer. Eu tenho medo de não ser capaz de parar de comer por vontade própria.'),
    )
    score10 =+ load_afir(afirmacao10, 10)

    afirmacao11 = st.radio(
        "#11",
        ('1. Eu não tenho problema algum para parar de comer quando me sinto cheio(a).',
         '2. Eu, normalmente, posso parar de comer quando me sinto cheio(a) mas, de vez em quando, comer demais me deixa desconfortavelmente empanturrado(a).',
         '3. Eu tenho um problema para parar de comer uma vez que eu tenha começado e, normalmente, sinto-me desconfortavelmente empanturrado(a) depois que faço uma refeição',
         '4. Por eu ter o problema de não ser capaz de parar de comer quando quero, às vezes tenho que provocar o vômito, usar laxativos e/ou diuréticos para aliviar minha sensação de empanturramento.')
    )
    score11 =+ load_afir(afirmacao11, 11)

    afirmacao12 = st.radio(
        "#12",
        ('1. Parece que eu como tanto quando estou com os outros (reuniões familiares, sociais), como quando estou sozinho(a).',
         '2. Às vezes, quando eu estou com outras pessoas, não como tanto quanto eu quero comer porque me sinto constrangido(a) com o meu comportamento alimentar.',
         '3. Frequentemente eu como só uma pequena quantidade de comida quando outros estão presentes, pois me sinto muito embaraçado(a) com o meu comportamento alimentar.',
         '4. Eu me sinto tão envergonhado(a) por comer demais que escolho horas para comer demais quando sei que ninguém me verá. Eu me sinto como uma pessoa que se esconde para comer.')
    )
    score12 =+ load_afir(afirmacao12, 12)

    afirmacao13 = st.radio(
        "#13",
        ('1. Eu faço três refeições ao dia com apenas um lanche ocasional entre as refeições',
         '2. Eu faço três refeições ao dia mas, normalmente, também lancho entre as refeições.',
         '3. Quando eu faço lanches pesados, tenho o hábito de pular as refeições regulares.',
         '4. Há períodos regulares em que parece que eu estou continuamente comendo, sem refeições planejadas.')
    )
    score13 =+ load_afir(afirmacao13, 13)

    afirmacao14 = st.radio(
        "#14",
        ('1. Eu não penso muito em tentar controlar impulsos indesejáveis para comer',
         '2. Pelo menos, em algum momento, sinto que meus pensamentos estão “pré-ocupados” com tentar controlar meus impulsos para comer.',
         '3. Frequentemente, sinto que gasto muito tempo pensando no quanto comi ou tentando não comer mais.',
         '4. Parece, para mim, que a maior parte das horas que passo acordado(a) estão “preocupadas” por pensamentos sobre comer ou não comer. Sinto como se eu estivesse constantemente lutando para não comer.')
    )
    score14 =+ load_afir(afirmacao14, 14)

    afirmacao15 = st.radio(
        "#15",
        ('1. Eu não penso muito sobre comida.',
         '2. Eu tenho fortes desejos por comida, mas eles só duram curtos períodos de tempo.',
         '3. Há dias em que parece que eu não posso pensar em mais nada a não ser comida.',
         '4. Na maioria dos dias, meus pensamentos parecem estar “pré-ocupados” com comida. Sinto como se eu vivesse para comer.')
    )
    score15 =+ load_afir(afirmacao15, 15)

    afirmacao16 = st.radio(
        "#16",
        ('1. Eu normalmente sei se estou ou não fisicamente com fome. Eu como a porção certa de comida para me satisfazer.',
         '2. De vez em quando eu me sinto em dúvida para saber se estou ou não fisicamente com fome. Nessas ocasiões é difícil saber quanto eu deveria comer para me satisfazer.',
         '3. Mesmo que se eu pudesse saber quantas calorias eu deveria ingerir, não teria idéia alguma de qual seria a quantidade “normal” de comida para mim.')
    )
    score16 =+ load_afir(afirmacao16, 16)

    score_final = (
        score1 + 
        score2 +
        score3 +
        score4 + 
        score5 +
        score6 +
        score7 + 
        score8 +
        score9 +
        score10 + 
        score11 +
        score12 +
        score13 +
        score14 +
        score15 +
        score16
    )

    classificacao = compulsivity_score(score_final)
    st.write(classificacao)

if __name__=='__main__':
    main()
