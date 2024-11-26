from gensim.downloader import load


glove_vectors = load('glove-wiki-gigaword-300')

print("Embedding 1: ", glove_vectors['king'])

