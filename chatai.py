from gensim.downloader import load

glove_vector_test = load('glove-wiki-gigaword-300')

print(glove_vector_test.most_similar('king'))
print(glove_vector_test.most_similar('queen'))

print("king: ", glove_vector_test['king'])