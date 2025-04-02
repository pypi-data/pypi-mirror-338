from typing import List, Optional

from pydantic import TypeAdapter

from galileo_core.constants.request_method import RequestMethod
from galileo_core.constants.routes import Routes
from galileo_core.helpers.logger import logger
from galileo_core.schemas.base_config import GalileoConfig
from galileo_core.schemas.core.integration.base import (
    CreateIntegrationRequest,
    IntegrationResponse,
)
from galileo_core.schemas.core.integration.create_integration import CreateIntegrationModel


def list_integrations(config: Optional[GalileoConfig] = None) -> List[IntegrationResponse]:
    """
    Returns all integrations that the user has access to.

    Returns
    -------
    List[IntegrationResponse]
        A list of integrations.
    """
    config = config or GalileoConfig.get()
    integrations = [
        IntegrationResponse.model_validate(integration)
        for integration in config.api_client.request(RequestMethod.GET, Routes.integrations)
    ]
    logger.debug(f"Got {len(integrations)} integrations.")
    return integrations


def create_or_update_integration(
    integration: CreateIntegrationRequest, config: Optional[GalileoConfig] = None
) -> IntegrationResponse:
    """
    Create or update an integration.

    Parameters
    ----------
    integration : CreateIntegrationRequest
        A integration request to create.

    Returns
    -------
    IntegrationResponse
        Response object for the created or updated integration.
    """
    config = config or GalileoConfig.get()

    adapter: TypeAdapter[CreateIntegrationModel] = TypeAdapter(CreateIntegrationModel)
    validated_data = adapter.validate_python({"name": integration.name, **integration.data})

    response_dict = config.api_client.request(
        RequestMethod.PUT,
        Routes.create_update_integration.format(integration_name=integration.name),
        json=validated_data.model_dump(),
    )
    integration_response = IntegrationResponse.model_validate(response_dict)
    logger.debug(f"Created integration with name {integration_response.name}, ID {integration_response.id}.")
    return integration_response
