import os
from langgraph.graph import StateGraph
from typing import TypedDict
from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq


class GraphState(TypedDict, total=False):
    prompt: str
    response: str
    final_answer: str



def read_cvs(state: GraphState) -> GraphState:
    folder = 'cvs'
    pdf_files = [f for f in os.listdir(folder) if f.endswith('.pdf')]
    summaries = []
    llm = ChatGroq(model="moonshotai/kimi-k2-instruct", temperature=0.0)
    for pdf_file in pdf_files:
        loader = PyPDFLoader(os.path.join(folder, pdf_file))
        documents = loader.load()
        if documents:
            summaries.append({'name': pdf_file, 'content': documents[0].page_content})
    messages = [
        {"role": "system", "content": "you are my cv reviewer assistant, your task is to review all the cvs from all the candidates."
                                     " and extract the summary section of each CV. You dont need to summarise the content, just"
                                      "return the raw content of the summary section"
                                "You need to return a dictionary with the following structure: 'cv name': 'summary of the cv'."},
        {"role": "user", "content": str(summaries)}
    ]

    response = llm.invoke(messages)
    return {
        "response": response.content
    }


def summary(state: GraphState) -> GraphState:
    final_answer = state.get("response", "")

    if not final_answer:
        return {"Summary": "No summary."}

    prompt = f" Those are the CVS:\n\n{final_answer}"
    llm = ChatGroq(model="moonshotai/kimi-k2-instruct", temperature=0.0)

    messages = [
        {"role": "system", "content": "You are my CV assistant. You need to evaluate the best candidate based on its CV. "},
        {"role": "user", "content": prompt}
    ]

    response = llm.invoke(messages)


    return {
        "final_answer": response.content
    }



def build_graph():
    graph = StateGraph(GraphState)
    graph.add_node("read_cvs", read_cvs)
    graph.add_node("summary", summary)
    graph.add_edge("read_cvs", "summary")
    graph.set_entry_point("read_cvs")
    graph.set_finish_point("summary")
    return graph.compile()

