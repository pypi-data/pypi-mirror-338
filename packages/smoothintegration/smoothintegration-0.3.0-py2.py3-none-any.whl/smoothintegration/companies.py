import uuid
from typing import Optional, TypedDict, cast

from smoothintegration import _http


class Company(TypedDict):
    id: uuid.UUID
    name: str


class GetCompanyResponse(TypedDict):
    message: str
    result: Company


class CreateCompanyPayload(TypedDict):
    name: str


class CreateCompanyResponse(TypedDict):
    message: str
    result: Company


def get_company(company_id: uuid.UUID) -> Optional[Company]:
    """
    Get an existing Company from SmoothIntegration.

    :param company_id: The ID of the company to retrieve.

    :returns: The URL to redirect the user to in order to get consent.
    :raises SIError: if the consent url could not be retrieved for any reason.
    """
    response = cast(
        GetCompanyResponse,
        _http.request("/v1/companies/" + str(company_id), method="GET"),
    )

    return response["result"]


def create_company(company: CreateCompanyPayload) -> Company:
    """
    Create a new Company in SmoothIntegration.

    :param company: An object containing details about the company to be created.
        - name (str): The name of the company.

    :returns: The URL to redirect the user to in order to get consent.
    :raises SIError: if the consent url could not be retrieved for any reason.
    """
    response = cast(
        CreateCompanyResponse,
        _http.request("/v1/companies", method="POST", json=company),
    )

    return response["result"]
