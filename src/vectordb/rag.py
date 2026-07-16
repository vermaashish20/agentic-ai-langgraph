from vectordb.embed import vectorstore

# Expose a retriever interface that fetches the top 2 most relevant documents
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
