import operator
from typing_extensions import Optional, Annotated, List, Sequence 

from langchain_core.messages import BaseMessage
from langgraph.graph import MessageState
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field

'''
AgentInputState class serves as a type-safe inut schema for LangGraph. It validates the incoming data and maps the user input to Agentstate["messages"]
'''
class AgentInputState(MessageState):
    '''
    Input state for the full agent. Only contains messages from the user input.
    '''
    pass

class AgentState(MessageState):
    '''
    Main state for the full agent. 
    '''

    # Research prompt generated after analyzing user intent. 
    # Optional[str] is equivalent to Union[str, None] from typing
    research_prompt: Optional[str]

    # Supervisor oversees the entire task and manages multi-agent researchers
    # Annotated: extra metadata for the type
    # Sequence: an ordered collection of items
    supervisor_message: Annotated[Sequence[BaseMessage], add_messages]

    # Raw unprocess research notes collected
    raw_notes: Annotated[List[str], operator.add]

    # Processed and structured notes for report generation
    notes: Annotated[List[str], operator.add]
    
    # Final report
    final_report: Optional[str]
