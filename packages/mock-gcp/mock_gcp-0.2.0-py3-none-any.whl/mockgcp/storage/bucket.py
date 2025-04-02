from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, NoReturn
from unittest import mock
from urllib.parse import urlsplit

from google.api_core import page_iterator
from google.cloud.exceptions import NotFound
from google.cloud.storage._helpers import _PropertyMixin, _validate_name
from google.cloud.storage.constants import _DEFAULT_TIMEOUT
from google.cloud.storage.retry import (
    DEFAULT_RETRY,
    DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
)

from mockgcp.storage.blob import MockBlob

if TYPE_CHECKING:
    from mockgcp.storage.client import MockClient


class MockBucket(_PropertyMixin):
    def __init__(self, client: MockClient, name=None, user_project=None) -> None:
        name = _validate_name(name)
        super().__init__(name)
        self._client = client
        self._user_project = user_project

    def __repr__(self) -> str:
        return f"<Bucket: {self.name}>"

    @property
    def client(self) -> MockClient:
        return self._client

    @property
    def blobs(self):
        return self.client.backend.blobs[self.name]

    @property
    def data_dir(self) -> Path:
        return self.client.backend.data_dir / self.name

    @property
    def user_project(self):
        return self._user_project

    @classmethod
    def from_string(cls, uri, client=None):
        scheme, netloc, path, query, frag = urlsplit(uri)

        if scheme != "gs":
            msg = "URI scheme must be gs"
            raise ValueError(msg)

        return cls(client, name=netloc)

    def blob(
        self,
        blob_name,
        chunk_size=None,
        encryption_key=None,
        kms_key_name=None,
        generation=None,
    ):
        return MockBlob(
            blob_name, self, chunk_size, encryption_key, kms_key_name, generation
        )

    def notification(
        self,
        topic_name,
        topic_project=None,
        custom_attributes=None,
        event_types=None,
        blob_name_prefix=None,
        # payload_format=NONE_PAYLOAD_FORMAT,
    ) -> NoReturn:
        raise NotImplementedError

    def exists(self, client=None):
        return self.name in self.client.buckets

    def create(
        self,
        client=None,
        project=None,
        location=None,
        predefined_acl=None,
        predefined_default_object_acl=None,
        enable_object_retention=False,
        timeout=_DEFAULT_TIMEOUT,
        retry=DEFAULT_RETRY,
    ) -> None:
        client = self._require_client(client)
        client.create_bucket(
            self.name,
            project=project,
            location=location,
            predefined_acl=predefined_acl,
            predefined_default_object_acl=predefined_default_object_acl,
            enable_object_retention=enable_object_retention,
            timeout=timeout,
            retry=retry,
        )

    def patch(self, client=None) -> NoReturn:
        raise NotImplementedError

    @property
    def acl(self) -> NoReturn:
        raise NotImplementedError

    @property
    def default_object_acl(self) -> NoReturn:
        raise NotImplementedError

    @staticmethod
    def path_helper(bucket_name):
        return "/b/" + bucket_name

    @property
    def path(self):
        if not self.name:
            msg = "Cannot determine path without bucket name."
            raise ValueError(msg)

        return self.path_helper(self.name)

    def get_blob(
        self, blob_name, client=None, encryption_key=None, generation=None, **kwargs
    ):
        return self.client.backend.blobs.get(self.name, {}).get(blob_name)

    def list_blobs(
        self,
        max_results=None,
        page_token=None,
        prefix=None,
        delimiter=None,
        start_offset=None,
        end_offset=None,
        include_trailing_delimiter=None,
        versions=None,
        projection="noAcl",
        fields=None,
        client=None,
        timeout=_DEFAULT_TIMEOUT,
        retry=DEFAULT_RETRY,
        match_glob=None,
        include_folders_as_prefixes=None,
        soft_deleted=None,
        page_size=None,
    ):
        if isinstance(max_results, int):
            blobs = list(self.client.backend.blobs[self.name].values())[:max_results]
        else:
            blobs = list(self.client.backend.blobs[self.name].values())

        if isinstance(delimiter, str):
            raise NotImplementedError

        if isinstance(prefix, str):
            blobs = [
                blob for blob in blobs if Path(blob.name).is_relative_to(Path(prefix))
            ]

        extra_params = {"projection": projection}

        path = "/foo"
        page_response = {"items": blobs}
        api_request = mock.Mock(return_value=page_response)

        iterator = page_iterator.HTTPIterator(
            mock.sentinel.client,
            api_request,
            path=path,
            item_to_value=page_iterator._item_to_value_identity,
            max_results=max_results,
            page_token=mock.sentinel.token,
            extra_params=extra_params,
        )
        iterator.prefixes = set()
        iterator.bucket = self
        return iterator

    def delete(self):
        for blob in list(self.blobs.values()):
            blob.delete()
        del self.client.buckets[self.name]

    def delete_blob(
        self,
        blob_name,
        client=None,
        generation=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        timeout=_DEFAULT_TIMEOUT,
        retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
    ) -> None:
        if blob_name in self.blobs:
            blob = self.blobs.pop(blob_name)
            blob.file_name.unlink(missing_ok=True)
        else:
            msg = f"404 GET https://storage.googleapis.com/storage/v1/b/{self.name}/o/{blob_name}?projection=noAcl"
            raise NotFound(msg)
