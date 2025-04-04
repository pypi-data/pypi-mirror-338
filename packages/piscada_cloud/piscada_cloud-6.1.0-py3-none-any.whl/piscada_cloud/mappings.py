"""
Classes and functions related to the mappings-manager service.

The mappings-manager service is used to map concrete controller/tag combinations to abstract meanings,
which can then be use to run an abstractly defined cloud-function on multiple concrete mapping definitions.
"""
import logging
import os
from copy import deepcopy
from typing import List, Optional, Tuple
from uuid import UUID

import requests

from piscada_cloud.manipulations import get_first_or_default


class Tag:
    """
    A tag on a specific controller.

    Attributes
    ----------
    controller_id : UUID
        The ID of the controller this tag belongs to.
    name : str
        The tag's name/id.
    """

    def __init__(self, controller_id: UUID, name: str):
        self.controller_id: UUID = controller_id
        self.name: str = name

    def __str__(self):
        return str(self.controller_id) + "|" + self.name

    def __repr__(self):
        return self.__str__()

    def __key(self):
        return (self.controller_id, self.name)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Tag):
            return self.__key() == other.__key()  # pylint: disable=W0212
        return NotImplemented


class Mapping:
    """A collection of meanings which are used to uniquely identify inputs and outputs in cloud functions."""

    def __init__(self, title: str, uuid: UUID):
        self.title: str = title
        self.uuid: UUID = uuid
        self.meanings: List[Meaning] = []

    def __str__(self):
        return f"{self.title}: {self.meanings}"

    def __repr__(self):
        return f"{self.title} ({self.uuid}): {self.meanings}"


class Meaning:
    """A meaning uniquely identifies andd input or output in cloud functions."""

    def __init__(self, title: str, uuid: UUID):
        self.title: str = title
        self.uuid: UUID = uuid

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"{self.title} ({self.uuid})"


class TagMapping:
    """A mapping from meaning to a controller/tag combination."""

    def __init__(self, meaning_uuid: UUID, controller_id: UUID, tag: str):
        self.meaning_uuid: UUID = meaning_uuid
        self.meaning_title: str
        self.controller_id: UUID = controller_id
        self.tag: str = tag

    def __str__(self):
        return f"{self.meaning_uuid}: {self.controller_id}|{self.tag}"

    def __repr__(self):
        return f"{self.meaning_uuid}:{self.controller_id}|{self.tag}"


class MappingTable:
    """A collections of TagMappings which connect meanings to concrete tags on specific controllers."""

    def __init__(self, title: str, uuid: UUID):
        self.title: str = title
        self.uuid: UUID = uuid
        self.tag_mappings: List[TagMapping] = []

    def __str__(self):
        return f"{self.title}: {self.tag_mappings}"

    def __repr__(self):
        return f"{self.title} ({self.uuid}): {self.tag_mappings}"

    def get_tag_mapping(self, meaning_uuid: UUID) -> Optional[TagMapping]:
        """Get the tag-mapping with the provided UUID from the mapping-table or None if not found."""
        tag_mapping: Optional[TagMapping] = get_first_or_default([tm for tm in self.tag_mappings if tm.meaning_uuid == meaning_uuid], None)
        if tag_mapping:
            if not tag_mapping.controller_id or not tag_mapping.tag:
                return None
        return tag_mapping

    def get_tag(self, meaning_uuid: UUID) -> Optional[Tag]:
        """Get a tag for a tag-mapping."""
        tag_mapping = self.get_tag_mapping(meaning_uuid)
        if tag_mapping:
            return Tag(tag_mapping.controller_id, tag_mapping.tag)
        return None

    def get_tags(self, meaning_uuid: UUID) -> List[Tag]:
        """Get multiple tags for a comma-separated tag-mapping."""
        tag_mapping = self.get_tag_mapping(meaning_uuid)
        if tag_mapping:
            return [Tag(tag_mapping.controller_id, tag.strip()) for tag in tag_mapping.tag.split(",")]
        return []


def _check_env_vars() -> Tuple[str, str]:
    host = os.getenv("MAPPINGSMANAGER_HOST")
    token = os.getenv("MAPPINGSMANAGER_TOKEN")
    if not host or not token:
        raise RuntimeError("Both environment variables MAPPINGSMANAGER_HOST and MAPPINGSMANAGER_TOKEN need to be defined.")
    return host, token


def get_mapping_tables(app_id: UUID) -> List[MappingTable]:
    """Retrieve the mapping tables for a given app_id from the mappings-manager service."""
    host, token = _check_env_vars()
    header = {"Authorization": "Bearer " + token}
    response = requests.get(f"https://{host}/v0/mapping-tables/{app_id}", headers=header)
    mapping_tables: List[MappingTable] = []
    if response and response.status_code == 200:
        mapping_tables_json = response.json()
        for mapping_table_json in mapping_tables_json:
            mapping_table = MappingTable(mapping_table_json["title"], UUID(mapping_table_json["uuid"]))
            for tag_mapping_json in mapping_table_json["tag-mappings"]:
                try:
                    controller_id: UUID = UUID(tag_mapping_json["controller-id"])
                except ValueError:
                    logging.error("Invalid controller-id: %s", tag_mapping_json["controller-id"])
                else:
                    mapping_table.tag_mappings.append(TagMapping(UUID(tag_mapping_json["meaning-uuid"]), controller_id, tag_mapping_json["tag"]))
            mapping_tables.append(mapping_table)
    else:
        logging.error("No mapping tables received: %s", response.content)
    return mapping_tables


def get_mappings() -> List[Mapping]:
    """Retrieve the mappings for a given app_id from the mappings-manager service."""
    host, token = _check_env_vars()
    header = {"Authorization": "Bearer " + token}
    response = requests.get(f"https://{host}/v0/mappings", headers=header)
    mappings: List[Mapping] = []
    if response and response.status_code == 200:
        mappings_json = response.json()
        for mapping_json in mappings_json:
            mapping = Mapping(mapping_json["title"], UUID(mapping_json["uuid"]))
            for meaning_json in mapping_json["meanings"]:
                mapping.meanings.append(Meaning(meaning_json["title"], UUID(meaning_json["uuid"])))
            mappings.append(mapping)
    else:
        logging.error("No mapping tables received: %s", response.content)
    return mappings


def add_meaning_titles(mapping_tables: List[MappingTable], mappings: List[Mapping]) -> List[MappingTable]:
    """Add meaning title to the tag-mappings within the given mapping-tables."""
    new_mapping_tables: List[MappingTable] = deepcopy(mapping_tables)
    all_meanings = [meaning for mapping in mappings for meaning in mapping.meanings]
    for mapping_table in new_mapping_tables:
        for tag_mapping in mapping_table.tag_mappings:
            tag_mapping.meaning_title = get_first_or_default([meaning.title for meaning in all_meanings if meaning.uuid == tag_mapping.meaning_uuid], None)
    return new_mapping_tables
