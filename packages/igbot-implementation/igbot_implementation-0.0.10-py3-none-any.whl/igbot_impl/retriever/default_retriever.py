from langchain_core.retrievers import BaseRetriever

from igbot_base.retriever import Retriever
from igbot_base.retriever import RetrieverResponse


class DefaultRetriever(Retriever):

    def __init__(
            self,
            retriever: BaseRetriever):
        super().__init__()
        self.__retriever = retriever

    def get_relevant_data(self, query: str) -> RetrieverResponse:
        return RetrieverResponse(self.__retriever.invoke(input=query))
