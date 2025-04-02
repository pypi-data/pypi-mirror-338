from __future__ import annotations

from datetime import datetime
from io import BytesIO
from typing import TYPE_CHECKING, BinaryIO

from google.cloud._helpers import (
    _bytes_to_unicode,
    _to_bytes,
    _rfc3339_nanos_to_datetime,
    _datetime_to_rfc3339,
)
from google.cloud.exceptions import NotFound
from google.cloud.storage._helpers import _PropertyMixin
from google.cloud.storage.constants import _DEFAULT_TIMEOUT
from google.cloud.storage.retry import (
    DEFAULT_RETRY,
    DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
)

if TYPE_CHECKING:
    from pathlib import Path

    from mockgcp.storage.bucket import MockBucket


class MockBlob(_PropertyMixin):
    def __init__(
        self,
        name,
        bucket: MockBucket,
        chunk_size=None,
        encryption_key=None,
        kms_key_name=None,
        generation=None,
    ) -> None:
        name = _bytes_to_unicode(name)
        super().__init__(name)

        self.chunk_size = chunk_size  # Check that setter accepts value.
        self._bucket = bucket
        # self._acl = ObjectACL(self)
        if encryption_key is not None and kms_key_name is not None:
            msg = "Pass at most one of 'encryption_key' and 'kms_key_name'"
            raise ValueError(msg)

        self._encryption_key = encryption_key

        if kms_key_name is not None:
            self._properties["kmsKeyName"] = kms_key_name

        if generation is not None:
            self._properties["generation"] = generation

    @property
    def bucket(self) -> MockBucket:
        """Bucket which contains the object.

        :rtype: :class:`~google.cloud.storage.bucket.Bucket`
        :returns: The object's bucket.
        """
        return self._bucket

    @property
    def client(self):
        """The client bound to this blob."""
        return self.bucket.client

    @property
    def file_name(self) -> Path:
        return self.bucket.data_dir / self.name

    def exists(
        self,
        client=None,
        if_etag_match=None,
        if_etag_not_match=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        timeout=_DEFAULT_TIMEOUT,
        retry=DEFAULT_RETRY,
        soft_deleted=None,
    ) -> bool:
        return self.name in self.bucket.blobs

    def exists_or_raise(self, client=None, **kwargs) -> bool:
        if self.exists(client=client, **kwargs):
            return True
        msg = f"404 GET https://storage.googleapis.com/storage/v1/b/{self.bucket.name}/o/{self.name}?projection=noAcl"
        raise NotFound(msg)

    def delete(
        self,
        client=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        timeout=_DEFAULT_TIMEOUT,
        retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
    ) -> None:
        self.bucket.delete_blob(
            self.name,
            client=client,
            if_generation_match=if_generation_match,
            if_generation_not_match=if_generation_not_match,
            if_metageneration_match=if_metageneration_match,
            if_metageneration_not_match=if_metageneration_not_match,
            timeout=timeout,
            retry=retry,
        )

    def download_to_file(
        self,
        file_obj,
        client=None,
        start=None,
        end=None,
        raw_download=False,
        checksum="md5",
        **kwargs,
    ) -> None:
        file_obj.write(
            self.download_as_bytes(
                client,
                start=start,
                end=end,
                raw_download=raw_download,
                checksum=checksum,
                **kwargs,
            )
        )

    def download_to_filename(
        self,
        filename,
        client=None,
        start=None,
        end=None,
        raw_download=False,
        checksum="md5",
        **kwargs,
    ) -> None:
        with open(filename, "wb") as f:
            self.download_to_file(
                file_obj=f,
                start=start,
                end=end,
                raw_download=raw_download,
                checksum=checksum,
                **kwargs,
            )

    def download_as_bytes(
        self,
        client=None,
        start=None,
        end=None,
        raw_download=False,
        checksum="md5",
        **kwargs,
    ) -> bytes:
        self.exists_or_raise(client=client, **kwargs)
        data = self.file_name.read_bytes()
        if end is not None:
            data = data[:end]
        if start is not None:
            data = data[start:]
        return data

    def download_as_string(
        self,
        client=None,
        start=None,
        end=None,
        raw_download=False,
        checksum="md5",
        **kwargs,
    ) -> str:
        return self.download_as_text(
            client,
            start=start,
            end=end,
            raw_download=raw_download,
            checksum=checksum,
            **kwargs,
        )

    def download_as_text(
        self,
        client=None,
        start=None,
        end=None,
        raw_download=False,
        checksum="md5",
        **kwargs,
    ) -> str:
        data = self.download_as_bytes(
            client,
            start=start,
            end=end,
            raw_download=raw_download,
            checksum=checksum,
            **kwargs,
        )
        return data.decode("utf-8")

    def upload_from_file(
        self,
        file_obj: BinaryIO,
        rewind=False,
        size=None,
        content_type=None,
        num_retries=None,
        client=None,
        predefined_acl=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        timeout=_DEFAULT_TIMEOUT,
        checksum=None,
        retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
    ) -> None:
        self.file_name.parent.mkdir(parents=True, exist_ok=True)
        self.file_name.write_bytes(file_obj.read())
        self._properties["updated"] = _datetime_to_rfc3339(datetime.utcnow())
        self.bucket.blobs[self.name] = self

    def upload_from_filename(self, filename, **kwargs) -> None:
        with open(filename, "rb") as f:
            self.upload_from_file(f, **kwargs)

    def upload_from_string(self, data, **kwargs) -> None:
        data = _to_bytes(data, encoding="utf-8")
        string_buffer = BytesIO(data)
        self.upload_from_file(string_buffer, **kwargs)

    @property
    def updated(self):
        value = self._properties.get("updated")
        if value is not None:
            return _rfc3339_nanos_to_datetime(value)
