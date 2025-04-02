from __future__ import annotations

import abc
import logging
import os
from typing import Any, Iterable, List, Optional

import sqlalchemy as sa
from sqlalchemy.engine import Row
from sqlalchemy.exc import OperationalError, ProgrammingError

from ckan.exceptions import CkanConfigurationException

from ckanext.drupal_idp import config, utils

log = logging.getLogger(__name__)


def db_url() -> str:
    url = config.db_url()
    if not url:
        raise CkanConfigurationException(
            f"drupal_idp plugin requires {config.CONFIG_DB_URL} config option."
        )
    return url


class BaseDrupal(metaclass=abc.ABCMeta):
    def __init__(self, url: str):
        self.engine = sa.create_engine(url)

    @abc.abstractmethod
    def get_uid_by_sid(self, sid: str) -> Optional[utils.DrupalId]:
        ...

    @abc.abstractmethod
    def get_user_by_uid(self, uid: utils.DrupalId) -> Row | None:
        ...

    @abc.abstractmethod
    def get_user_roles(self, uid: utils.DrupalId) -> List[str]:
        ...

    @abc.abstractmethod
    def get_avatar(self, uid: utils.DrupalId) -> Optional[str]:
        ...

    @abc.abstractmethod
    def get_field(self, uid: utils.DrupalId, field: str) -> list[Any]:
        ...

    def get_fields(
        self, uid: utils.DrupalId, fields: Iterable[str]
    ) -> dict[str, list[Any]]:
        return {field: self.get_field(uid, field) for field in fields}


class Drupal9(BaseDrupal):
    def get_uid_by_sid(self, sid: str) -> utils.DrupalId | None:
        try:
            user = self.engine.execute(
                """
            SELECT d.uid id
            FROM users_field_data d
            JOIN sessions s
            ON s.uid = d.uid
            WHERE s.sid = %s
            """,
                [sid],
            ).first()
        except OperationalError as e:
            log.error("Cannot get a user from Drupal's database: %s", e)
            return

        if user:
            return user.id

    def get_user_by_uid(self, uid: utils.DrupalId) -> Row | None:
        try:
            user = self.engine.execute(
                """
            SELECT d.name "name", d.mail email, d.uid id
            FROM users_field_data d
            WHERE d.uid = %s
            """,
                [uid],
            ).first()
        except OperationalError as e:
            log.error("Cannot get a user from Drupal's database: %s", e)
            return
        # check if session has username,
        # otherwise is unauthenticated user session
        if user and user.name:
            return user

    def get_user_roles(self, uid: utils.DrupalId) -> List[str]:
        query = self.engine.execute(
            """
                 SELECT roles_target_id "name"
                 FROM user__roles
                 WHERE bundle = 'user' AND entity_id = %s
                 """,
            [uid],
        )
        return [role.name for role in query]

    def get_avatar(self, uid: utils.DrupalId):
        query = self.engine.execute(
            """
            SELECT fm.uri
            FROM file_managed fm
            JOIN user__user_picture up
            ON up.user_picture_target_id = fm.fid
            WHERE up.entity_id = %s
            LIMIT 1;
            """,
            [uid],
        )
        path = query.scalar()
        if not path:
            log.debug("User %s has no avatar", uid)
            return None

        public_prefix = "public://"
        if path.startswith(public_prefix):
            path = os.path.join(
                config.public_path().rstrip("/"),
                path[len(public_prefix) :],
            )
        return path

    def get_field(self, uid: utils.DrupalId, field: str) -> list[Any]:
        try:
            query = self.engine.execute(
                f"""
                SELECT {field}_value
                FROM user__{field}
                WHERE bundle = 'user' AND entity_id = %s AND deleted = 0
                """,
                [uid],
            )
        except ProgrammingError as e:
            log.error("Cannot get a user from Drupal's database: %s", e)
            return []

        return [r[0] for r in query]


_mapping = {"9": Drupal9, "10": Drupal9, "11": Drupal9}


def get_adapter(version: str) -> BaseDrupal:
    return _mapping[version](db_url())
