from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import PathwayVectorClient

def get_agent():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    retriever = PathwayVectorClient(
        host="http://localhost",
        port=8754
    ).as_retriever()

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa
