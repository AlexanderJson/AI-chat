from gensim.downloader import load

glove_vector_test = load('glove-wiki-gigaword-300')


# print("king: ", glove_vector_test['king'])


def tokenise_input():
    user_input = input("Enter a word: ")
    words = user_input.split()
    for word in words: 
        if word in glove_vector_test:
            print("word: ", glove_vector_test[word])
        else:
            print("word not in dictionary")


tokenise_input()