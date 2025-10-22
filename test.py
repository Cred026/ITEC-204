import tensorflow_hub as hub
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 1. Pre-load the embedding model
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# 2. Fruit corpus with descriptions
fruits = [
    "Apple: A sweet, crunchy fruit that is red, green, or yellow.",
    "Banana: A long, yellow fruit that is soft and sweet inside.",
    "Orange: A citrus fruit with a tough, bright orange skin.",
    "Strawberry: A small, red fruit that is juicy and sweet.",
    "Blueberry: Tiny, round, blue-purple berries that are sweet and tart.",
    "Grapes: Small, round fruits that grow in clusters and can be green, red, or purple.",
    "Watermelon: A large green fruit with sweet, juicy, red flesh and black seeds.",
    "Pineapple: A tropical fruit with spiky skin and sweet, tangy yellow flesh.",
    "Mango: A tropical fruit with smooth skin, orange flesh, and sweet flavor.",
    "Kiwi: A small brown fruit with fuzzy skin and bright green, tangy flesh.",
    "Peach: A soft, round fruit with fuzzy skin and sweet, juicy flesh.",
    "Plum: A small, round fruit with smooth skin and sweet, sometimes tart flesh.",
    "Cherry: A small, round red fruit that is sweet or tart.",
    "Lemon: A yellow citrus fruit that is sour and tangy.",
    "Lime: A small green citrus fruit that is sour and tart.",
    "Papaya: A tropical fruit with orange flesh and black seeds, sweet and soft.",
    "Pear: A soft, sweet fruit with green or yellow skin.",
    "Raspberry: Small, red, sweet and tart berries that grow in clusters.",
    "Blackberry: Dark purple-black berries that are sweet and juicy.",
    "Cantaloupe: A melon with orange flesh and a rough, netted skin.",
    "Honeydew: A melon with smooth, pale green skin and sweet, green flesh.",
    "Pomegranate: A round fruit with tough skin and many juicy red seeds inside."
]

# 3. Precompute embeddings for the fruit descriptions
fruit_embeddings = embed(fruits)

# 4. Semantic search function
def semantic_search(query, embeddings=fruit_embeddings, items=fruits, top_k=1):
    query_embedding = embed([query])
    similarities = cosine_similarity(query_embedding, embeddings)
    top_indices = np.argsort(similarities[0])[::-1][:top_k]
    return [(items[i], float(similarities[0][i])) for i in top_indices]

# 5. Example query
# query = "A red fruit that is juicy and sweet"
# results = semantic_search(query, top_k=2)

while True:
    inputs = input("Enter the description: ")
    results = semantic_search(inputs, top_k=10)
    for fruit, score in results:
        print(f"Score: {score:.4f} | {fruit}")

    if inputs.lower() == "y":
        break
