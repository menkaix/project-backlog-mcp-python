from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_feature_to_story_body import AddFeatureToStoryBody
from ...types import Response


def _get_kwargs(
    story: str,
    *,
    body: AddFeatureToStoryBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/feature-command/{story}/add",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, str]]:
    if response.status_code == 201:
        response_201 = cast(str, response.json())
        return response_201
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    story: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddFeatureToStoryBody,
) -> Response[Union[Any, str]]:
    """Add a feature to a story

    Args:
        story (str):
        body (AddFeatureToStoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, str]]
    """

    kwargs = _get_kwargs(
        story=story,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    story: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddFeatureToStoryBody,
) -> Optional[Union[Any, str]]:
    """Add a feature to a story

    Args:
        story (str):
        body (AddFeatureToStoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, str]
    """

    return sync_detailed(
        story=story,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    story: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddFeatureToStoryBody,
) -> Response[Union[Any, str]]:
    """Add a feature to a story

    Args:
        story (str):
        body (AddFeatureToStoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, str]]
    """

    kwargs = _get_kwargs(
        story=story,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    story: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddFeatureToStoryBody,
) -> Optional[Union[Any, str]]:
    """Add a feature to a story

    Args:
        story (str):
        body (AddFeatureToStoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, str]
    """

    return (
        await asyncio_detailed(
            story=story,
            client=client,
            body=body,
        )
    ).parsed
