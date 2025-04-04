from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_core.language_models import BaseLanguageModel
from langchain_core.retrievers import BaseRetriever

from igbot_base.retriever import Retriever, RetrieverResponse


class MultiQuery(Retriever):

    def __init__(
            self,
            retriever: BaseRetriever,
            model: BaseLanguageModel):
        super().__init__()
        self.__retriever = MultiQueryRetriever.from_llm(retriever=retriever, llm=model)

    def get_relevant_data(self, query: str):
        return RetrieverResponse(self.__retriever.invoke(input=query))

