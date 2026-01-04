import chromadb
from chromadb.errors import NotFoundError
import os
import json
import uuid

if __name__ == "__main__":
    db_path = os.path.join("..", "chromaDB_vec_db")
    chroma_client = chromadb.PersistentClient(path=db_path)
    
    try:
        chroma_client.delete_collection(name="movies_collection")
    except NotFoundError:
        pass
    collection = chroma_client.create_collection(name="movies_collection")

    filepath = os.path.join("json_data", "films_data_w_keywords.json")
    with open(filepath, "r", encoding="utf-8") as f:
        movies_json = json.load(f)


    documents = []
    metadatas = []
    ids = []
    
    for index, movie in enumerate(movies_json):
        movie_embeding = str(movie["original_title"]) + " " + str(movie["overview"]) + " " + str(movie["release_date"]) + " " + str(movie['key_words'])
        genres_str = ""

        for genre in movie['genre_ids']:
            movie_embeding += f" {genre}"
            genres_str += f"{genre} "

        movie_metadata = {
            "title": movie["original_title"],
            "description": movie["overview"],
            "genres": genres_str.strip(),
            "id": movie["id"],
        }
        ids.append(str(uuid.uuid4()))
        documents.append(movie_embeding)
        metadatas.append(movie_metadata)

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids,
    )