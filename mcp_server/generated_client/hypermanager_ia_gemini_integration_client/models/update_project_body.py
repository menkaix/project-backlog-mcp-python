from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateProjectBody")


@_attrs_define
class UpdateProjectBody:
    """
    Attributes:
        name (Union[Unset, str]):
        code (Union[Unset, str]):
        client_name (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    client_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        code = self.code

        client_name = self.client_name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if client_name is not UNSET:
            field_dict["clientName"] = client_name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        code = d.pop("code", UNSET)

        client_name = d.pop("clientName", UNSET)

        description = d.pop("description", UNSET)

        update_project_body = cls(
            name=name,
            code=code,
            client_name=client_name,
            description=description,
        )

        update_project_body.additional_properties = d
        return update_project_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
