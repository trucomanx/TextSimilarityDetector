#!/usr/bin/python3

import nltk
nltk.download('punkt_tab') # needed to use sent_tokenize
from nltk.tokenize import sent_tokenize # A função é usada para dividir um texto em sentenças ou frases.  

def split_texts_in_sentences(text_list):
    # divide o texto em sentenças
    text = []
    for text_data in text_list:
        text.extend(sent_tokenize(text_data))
    
    return text
    


if __name__ == '__main__':

    text = """
__main__ é o nome do ambiente principal no qual o código é executado. “Ambiente de código principal” é o primeiro módulo Python definido pelo usuário que começa a ser executado. É considerado principal porque ele importa todos os outros módulos que o programa precisa. As vezes, “ambiente principal” também pode ser chamado de “ponto de entrada” da aplicação.
    """
    
    sentence_list = split_texts_in_sentences([text])
    
    for sentence in sentence_list:
        print(sentence)
