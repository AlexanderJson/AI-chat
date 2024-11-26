from gensim.downloader import load
import numpy as np
import random


glove_vector_test = load('glove-wiki-gigaword-300')




def tokenise_input():
    user_input = input("Enter a word: ")
    words = user_input.split()
    for word in words: 
        if word in glove_vector_test:
            print("Full matrix: ", glove_vector_test[words])
        else:
            print("word not in dictionary")
tokenise_input() ## en matris?

def calculate_attention(input):

    ## fixa input sedan
    ## input = input.sum(axis=1)

    ## column_size = 300

    ## multihead attention ide: 
    ## fixa så dessa två itererar x gånger (q,k,v)

    ## queryMatrices =  multiplyMatrices(input, weights, bias)
    ## keyMatrices = multiplyMatrices(input, weights, bias)
    ## valueMatrices = multiplyMatrices(input, weights, bias)

    ## attention = softmax(queryMatrices * keyMatrices.T)
    ## attention = attention * valueMatrices
    ## output = attention.sum(axis=1)


    return


def random_weights():
    return

def random_bias():
    return

def save_weights():
    return

def save_bias():
    return

def load_weights():
    return

def load_bias():
    return

def multiplyMatrices(layer, weights, bias):
    ## layer * weights + bias = new_layer[i]
    ## return new_layer[i]
    return

def softmax():
    return

def min_max_normalisation():
    return




## kolla sen:
    ## total_sum = 3
    ## for i in range total_ sum -> 
        ## init_weights(input, column_size)
        ## init_bias(column_size)
