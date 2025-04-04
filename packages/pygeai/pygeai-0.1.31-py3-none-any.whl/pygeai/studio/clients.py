import json
from json import JSONDecodeError
from typing import Any, Union

from pygeai.core.base.clients import BaseClient
from pygeai.core.common.exceptions import MissingRequirementException
from pygeai.core.services.rest import ApiService
from pygeai.studio.endpoints import CREATE_AGENT_V2, LIST_AGENTS_V2


class AIStudioClient(BaseClient):

    def __init__(self, api_key: str = None, base_url: str = None, alias: str = "default", studio_url: str = None):
        super().__init__(api_key, base_url, alias)
        studio_url = self.session.studio_url if not studio_url else None
        if not studio_url:
            raise MissingRequirementException("STUDIO URL must be defined in order to use the AI Studio.")

        self.session.studio_url = studio_url
        self.api_service = ApiService(base_url=self.session.studio_url, token=self.session.api_key)

    def list_agents(
            self,
            project_id: str,
            status: str = "",
            start: int = "",
            count: int = "",
            access_scope: str = "public",
            allow_drafts: bool = True,
            allow_external: bool = False
    ):
        """
        Retrieves a list of agents associated with the specified project.

        :param project_id: str - Unique identifier of the project.
        :param status: str - Status of the agents to filter by. Defaults to "" (no filtering).
        :param start: int - Starting index for pagination. Defaults to "" (no offset).
        :param count: int - Number of agents to retrieve. Defaults to "" (no limit).
        :param access_scope: str - Access scope of the agents, either "public" or "private". Defaults to "public".
        :param allow_drafts: bool - Whether to include draft agents. Defaults to True.
        :param allow_external: bool - Whether to include external agents. Defaults to False.
        :return: dict or str - JSON response containing the list of agents if successful, otherwise the raw response text.
        """
        endpoint = LIST_AGENTS_V2
        headers = {
            "ProjectId": project_id
        }

        response = self.api_service.get(
            endpoint=endpoint,
            headers=headers,
            params={
                "status": status,
                "start": start,
                "count": count,
                "accessScope": access_scope,
                "allowDrafts": allow_drafts,
                "allowExternal": allow_external
            }
        )
        try:
            result = response.json()
        except JSONDecodeError as e:
            result = response.text

        return result

    def create_agent(
            self,
            project_id: str,
            name: str,
            access_scope: str,
            public_name: str,
            job_description: str,
            avatar_image: str,
            description: str,
            agent_data_prompt: dict,
            agent_data_llm_config: dict,
            agent_data_models: list,
            automatic_publish: bool = False
    ) -> dict:
        """
        Creates a new agent in the specified project.

        :param project_id: str - Unique identifier of the project.
        :param name: str - Name of the agent.
        :param access_scope: str - Access scope of the agent, either "public" or "private".
        :param public_name: str - Public name of the agent.
        :param job_description: str - Job description of the agent.
        :param avatar_image: str - URL or identifier of the agent's avatar image.
        :param description: str - Detailed description of the agent.
        :param agent_data_prompt: dict - Prompt instructions, inputs, outputs, and examples for the agent.
        :param agent_data_llm_config: dict - Configuration parameters for the LLM, such as max tokens, timeout, temperature, topK, and topP.
        :param agent_data_models: list - List of models available for the agent.
        :param automatic_publish: bool - Whether to automatically publish the agent after creation. Defaults to False.
        :return: dict - JSON response containing the created agent details if successful, otherwise the raw response text.
        """
        data = {
            "agentDefinition": {
                "name": name,
                "accessScope": access_scope,
                "publicName": public_name,
                "jobDescription": job_description,
                "avatarImage": avatar_image,
                "description": description,
                "agentData": {
                    "prompt": agent_data_prompt,
                    "llmConfig": agent_data_llm_config,
                    "models": agent_data_models
                }
            }
        }
        if automatic_publish:
            endpoint = f"{CREATE_AGENT_V2}?automaticPublish=true"
        else:
            endpoint = CREATE_AGENT_V2

        headers = {
            "ProjectId": project_id
        }

        response = self.api_service.post(
            endpoint=endpoint,
            headers=headers,
            data=data
        )

        try:
            result = response.json()
        except JSONDecodeError as e:
            result = response.text

        return result

