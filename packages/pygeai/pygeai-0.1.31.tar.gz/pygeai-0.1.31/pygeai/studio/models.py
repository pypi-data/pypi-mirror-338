from typing import Literal, Optional, List

from pydantic import BaseModel, model_validator, Field

from pygeai.core.base.models import Project, LlmSettings
from pygeai.core import CustomBaseModel


class Agent(CustomBaseModel):
    """
    Represents an AI agent within a project.

    :param id: str - Unique identifier of the agent.
    :param project: Project - The project that owns the agent.
    :param status: Literal["active", "inactive"] - The current status of the agent.
    """
    id: str = Field(..., alias="agentId")
    project: Project = Field(..., alias="agentProject")
    status: Literal["active", "inactive"] = Field(..., alias="agentStatus")


class Model(CustomBaseModel):
    """
    Represents a language model configuration used by an agent.

    :param name: str - The unique name identifying the model.
    :param llm_config: LlmConfiguration, optional - Overrides default agent settings.
    :param prompt: str - A tailored prompt specific to this model.
    """
    name: str = Field(..., alias="name")
    llm_config: Optional[LlmSettings] = Field(None, alias="llmConfig")
    prompt: str = Field(..., alias="prompt")


class Tool(BaseModel):
    """
    Represents a tool available for an agent's resource pool.

    :param name: str - The name of the tool used.
    :param version: str - The version of the tool used.
    """
    name: str
    version: str    # TODO -> Review if necessary to create ToolVersion


class ResourcePool(BaseModel):
    """
    Defines a resource pool containing tools and assistants accessible to an agent.

    :param name: str - The name of the resource pool.
    :param tools: List[Tool] - The list of tools available in the pool.
    :param assistants: List[Agent] - A list of agents that can be called upon.
    """
    name: str
    tools: List[Tool]
    assistants: List[Agent]


class AgentRevisionData(BaseModel):
    """
   Contains detailed configuration data for an agent revision.

   :param strategy_name: str - The name of the reasoning strategy used.
   :param prompt: str - The main prompt associated with the agent.
   :param llm_config: LlmConfiguration - The language model configuration.
   :param models: List[Model] - The list of models assigned to the agent.
   :param resource_pool: List[ResourcePool] - The agent's available resource pools.
   """
    strategy_name: str
    prompt: str
    llm_config: LlmSettings
    models: List[Model]
    resource_pool: List[ResourcePool]


class AgentRevision(CustomBaseModel):
    """
    Represents a revision of an AI agent with versioned configurations.

    :param agent: Agent - The agent to which this revision belongs.
    :param name: str - The unique name identifying this revision.
    :param access_scope: Literal["public", "private"] - Determines if the agent is public or private.
    :param public_name: str, optional - Required if access_scope is "public"; must be globally unique.
    :param avatar_image: str, optional - An image representing the agent.
    :param description: str - A description of the agent's role.
    :param job_description: str - A short summary displayed in UI previews.
    :param agent_data: AgentRevisionData - The configuration details of the agent revision.
    """
    agent: Agent = Field(..., alias="agent")
    name: str = Field(..., alias="name")
    access_scope: Literal["public", "private"] = Field("private", alias="accessScope")
    public_name: Optional[str] = Field(None, alias="publicName")
    avatar_image: Optional[str] = Field(None, alias="avatarImage")
    description: str = Field(..., alias="description")
    job_description: str = Field(..., alias="jobDescription")
    agent_data: AgentRevisionData = Field(..., alias="agentData")

    @model_validator(mode="after")
    def check_public_name(self, values):
        """
        Validates that public_name is provided if access_scope is set to "public".

        :raises ValueError: If access_scope is "public" but public_name is missing or improperly formatted.
        """
        if values.access_scope == "public" and not values.public_name:
            raise ValueError("public_name is required if access_scope is public and the name can only contain"
                             " characters in lowercase, numbers, period, dash and underscore.")
