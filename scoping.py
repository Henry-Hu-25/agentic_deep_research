import operator
from typing_extensions import Optional, Annotated, List, Sequence 

from langchain_core.messages import BaseMessage
from langgraph.graph import MessageState
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field


class ClarifyWithUser(BaseModel):
    '''
    Schema for user clarification decision and questions
    '''

    need_clarification: bool = Field(
        description="Wheter the user needs to be asked a clarification question."
    )

    question: str = Field(
        description="A clarifying question to ask the user"
    )

    verification: str = Field(
        description="A verification message signaling that the research will start after the user has provided the necessary information"
    )

class ResearchQuestion(BaseModel):
    '''
    
    '''