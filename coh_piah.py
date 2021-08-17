import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    f = 0
    for i in range(0,6):
        f = f + abs(as_a[i] - as_b[i])
    return f / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    wal = wal_ass_b(texto)
    ttr = ttr_ass_b(texto)
    hlr = hlr_ass_b(texto)
    sal = sal_ass_b(texto)
    sac = sac_ass_b(texto)
    pal = pal_ass_b(texto)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    ass_comparada = []
    for i in range(len(textos)):
        texto = textos[i]
        as_b = calcula_assinatura(texto)
        ass_comparada.append(compara_assinatura(ass_cp, as_b))

    infectado = min(ass_comparada)
    for i in range(len(ass_comparada)):
        if infectado == ass_comparada[i]:
            return i+1

def wal_ass_b(texto):
    lista_palavras = organizando_palavra(texto)
    tamanho_palavra = 0
    for palavra in lista_palavras:
        tamanho_palavra += len(palavra)

    return tamanho_palavra / len(lista_palavras)

def ttr_ass_b(texto):
    lista_palavras = organizando_palavra(texto)
    return n_palavras_diferentes(lista_palavras) / len(lista_palavras)

def hlr_ass_b(texto):
    lista_palavras = organizando_palavra(texto)
    return n_palavras_unicas(lista_palavras) / len(lista_palavras)

def sal_ass_b(texto):
    sentenca = separa_sentencas(texto)
    sentencas = []
    caractere_sentenc = 0
    for i in range(len(sentenca)):
        sentencas.append(sentenca[i])
        caractere_sentenc = caractere_sentenc + len(sentenca[i])
    return caractere_sentenc / len(sentencas)

def sac_ass_b(texto):
    sentencas = separa_sentencas(texto)
    lista_frase = organizando_frase(texto)

    return len(lista_frase) / len(sentencas)

def pal_ass_b(texto):
    lista_frase = organizando_frase(texto)
    tamanho_frase = 0
    for frase in lista_frase:
        tamanho_frase += len(frase)

    return tamanho_frase / len(lista_frase)

def organizando_palavra(texto):
    lista_frases = organizando_frase(texto)

    lista_palavras = []
    for i in lista_frases:
        palavras_separadas = separa_palavras(i)
        for palavras in palavras_separadas:
            lista_palavras.append(palavras)

    return lista_palavras

def organizando_frase(texto):
    sentencas = separa_sentencas(texto)
    lista_frases = []
    for i in sentencas:
        frases_separadas = separa_frases(i)
        for frases in frases_separadas:
            lista_frases.append(frases)
    return lista_frases

def Main():
    print(f"O autor do texto {avalia_textos(le_textos(), le_assinatura())} está infectado com COH-PIA")

Main()
