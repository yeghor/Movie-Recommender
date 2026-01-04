import os
import chromadb
import uuid


COLLECTION_NAME = "movies_collection"

chroma_database_path = os.path.join("chromaDB_vec_db")

class ChromaDBService:
    @staticmethod
    def valid_n_results(n_results):
        return 0 < n_results <= 50

    @staticmethod
    def validate_adding_data_is_list(data):
        return isinstance(data, list)

    @staticmethod
    def get_readable_list_results_from_metadata(results):
        readable = []
        for metadata in results["metadatas"][0]:
            readable.append(f"Title - {metadata['title']}\nDescription - {metadata['description']}\nGenres List - {metadata['genres']}")
        return readable

    @staticmethod
    def get_metadata_list(results):
        meta_list = []
        for metadata in results["metadatas"][0]:
            meta_list.append(metadata)
        return meta_list

    def validate_meta_doc_len(meta, docs):
        return len(meta) == len(docs)

    def __init__(self):
        self.__client = chromadb.PersistentClient(path=chroma_database_path)
        self.__collection = self.__client.get_collection(name=COLLECTION_NAME)

    def query(self, query_texts: str, genres: str, n_results: int = 3, contain: str = " "):
        
        if self.valid_n_results(n_results):
            results = self.__collection.query(
                query_texts=[query_texts + genres],
                n_results=n_results,
                # where_document={"$contains": contain}
            )

            return self.get_readable_list_results_from_metadata(results), self.get_metadata_list(results)
        else:
            raise ValueError(f"Invalid n_results: {n_results}. Must be between 1 and 50.")

    def add_film_data(self, docs: list, metadatas: list):
        ids = []
        if self.validate_meta_doc_len(metadatas, docs):
            for _ in range(len(docs)): ids.append(str(uuid.uuid4()))

            if self.validate_adding_data_is_list(docs) and self.validate_adding_data_is_list(metadatas) and self.validate_adding_data_is_list(ids):
                self.__add_film_data_directly(documents=docs, metadatas=metadatas, ids=ids)
            else:
                raise TypeError("Non valid data types. Expected: list")
        else:
            raise IndexError("Length of docs and metadatas are not equal")

    def __add_film_data_directly(self, documents: list, metadatas: list, ids:list):
        self.__collection.add(
            documents=documents,        
            metadatas=metadatas,        
            ids=ids,                        
        )

if __name__ == "__main__":
    service = ChromaDBService()

    readable, metadata = service.query(query_texts="I want a movie about space, phylosophy and contact with alliens")
    for data in readable:
        print(data, f"\n")