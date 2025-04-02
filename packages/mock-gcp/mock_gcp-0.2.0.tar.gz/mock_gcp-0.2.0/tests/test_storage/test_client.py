from __future__ import annotations

import tempfile
from unittest.mock import patch

import pytest
from google.api_core import page_iterator
from google.cloud import storage
from google.cloud.exceptions import Conflict, NotFound

from mockgcp import mock_storage
from mockgcp.storage.bucket import MockBucket
from mockgcp.storage.client import MockClient


class TestBucketConstructor:
    @mock_storage
    def test_with_valid_name(self) -> None:
        client = storage.Client()
        assert isinstance(client, MockClient)

        bucket = client.bucket("test-bucket-name")

        assert isinstance(bucket, MockBucket)
        assert bucket.name == "test-bucket-name"

    @mock_storage
    def test_with_invalid_name(self) -> None:
        client = storage.Client()
        with pytest.raises(
            ValueError, match="Bucket names must start and end with a number or letter."
        ):
            client.bucket("test-bucket-name-")


class TestGetBucket:
    @mock_storage
    def test_with_existing_bucket_name(self) -> None:
        client = storage.Client()
        bucket = client.create_bucket("test-bucket-name")

        assert client.get_bucket("test-bucket-name") is bucket

    @mock_storage
    def test_with_non_existing_bucket_name(self) -> None:
        client = storage.Client()
        with pytest.raises(NotFound):
            client.get_bucket("test-bucket-name")


class TestLookupBucket:
    @mock_storage
    def test_wiht_existing_bucket_name(self) -> None:
        client = storage.Client()
        bucket = client.create_bucket("test-bucket-name")

        assert client.lookup_bucket("test-bucket-name") is bucket

    @mock_storage
    def test_wiht_non_existing_bucket_name(self) -> None:
        client = storage.Client()

        assert client.lookup_bucket("test-bucket-name") is None


class TestCreateBucket:
    @mock_storage
    def test_simple(self) -> None:
        client = storage.Client()
        bucket = client.create_bucket("test-bucket-name")

        assert isinstance(bucket, MockBucket)
        assert list(client.list_buckets()) == [bucket]

    @mock_storage
    def test_with_existing_bucket_name(self) -> None:
        client = storage.Client()
        bucket = client.create_bucket("test-bucket-name")

        with pytest.raises(Conflict):
            client.create_bucket("test-bucket-name")

        with pytest.raises(Conflict):
            bucket.create()


class TestListBlobs:
    @mock_storage
    def test_simple(self) -> None:
        client = storage.Client()
        bucket = client.create_bucket("test-bucket-name")
        bucket.list_blobs()


class TestListBuckets:
    @mock_storage
    def test_with_no_bucket(self) -> None:
        client = storage.Client()
        buckets = client.list_buckets()

        assert isinstance(buckets, page_iterator.HTTPIterator)
        assert list(buckets) == []

    @mock_storage
    def test_with_one_bucket(self) -> None:
        client = storage.Client()
        bucket = client.create_bucket("test-bucket-name")
        buckets = client.list_buckets()

        assert list(buckets) == [bucket]

    @mock_storage
    def test_with_max_results(self) -> None:
        client = storage.Client()
        client.create_bucket("test-bucket-name-n1")
        client.create_bucket("test-bucket-name-n2")

        assert len(list(client.list_buckets(max_results=1))) == 1

    @mock_storage
    def test_with_prefix(self) -> None:
        client = storage.Client()
        bucket_test = client.create_bucket("test-bucket-name")
        client.create_bucket("other-bucket-name")

        assert list(client.list_buckets(prefix="test")) == [bucket_test]


class TestDeleteBucket:
    @mock_storage
    def test_delete_bucket(self) -> None:
        client = storage.Client()
        bucket_test = client.create_bucket("test-bucket-name")
        bucket_test.delete()


class TestBlobs:
    @classmethod
    def setup_class(cls):
        cls.patcher = patch("google.cloud.storage.Client", MockClient)
        cls.patcher.start()
        cls.client = storage.Client()
        cls.bucket = cls.client.create_bucket("test-bucket-name")
        cls.file = tempfile.NamedTemporaryFile()
        cls.file.write(b"test")

        cls.new_file = tempfile.NamedTemporaryFile()

    @classmethod
    def teardown_class(cls) -> None:
        cls.bucket.delete()
        cls.file.close()
        cls.new_file.close()

        del cls.client
        cls.patcher.stop()

    class TestFilename:
        def test_upload(self) -> None:
            blob = self.bucket.blob("dir/dir/dir/file.bin")
            blob.upload_from_filename(self.file.name)

        def test_download(self) -> None:
            blob = self.bucket.blob("dir/dir/dir/file.bin")
            blob.download_to_filename(self.new_file.name)
            assert self.new_file.read() == self.file.read()

    class TestText:
        def test_upload(self) -> None:
            blob = self.bucket.blob("dir/dir/dir/file.txt")
            blob.upload_from_string("Some text")

        def test_download(self) -> None:
            blob = self.bucket.blob("dir/dir/dir/file.txt")
            assert blob.download_as_string() == "Some text"
