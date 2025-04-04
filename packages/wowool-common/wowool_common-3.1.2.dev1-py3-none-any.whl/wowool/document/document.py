from wowool.document.document_interface import DocumentInterface
from wowool.document.factory import Factory, _resolve__pass_thru, DEFAULT_TEXT_DATA_TYPE
from pathlib import Path
from wowool.document.defines import WJ_ID, WJ_DATA, WJ_DATA_TYPE, WJ_METADATA


class Document(DocumentInterface):
    """
    :class:`DocumentInterface` is an interface utility to handle data input.
    """

    DEFAULT_TEXT_DATA_TYPE = DEFAULT_TEXT_DATA_TYPE

    def __init__(self, data: str | bytes, id: Path | str | None = None, data_type: str = "", metadata: dict = {}, encoding="utf8"):
        self.input_provider = Factory.create(
            id=id,
            data=data,
            provider_type=data_type,
            encoding=encoding,
            metadata=metadata,
        )
        self._metadata = metadata

    @property
    def id(self) -> str:
        """
        :return: Unique document identifier
        :rtype: ``str``
        """
        return self.input_provider.id

    @property
    def data_type(self) -> str:
        """
        :return: Document type
        :rtype: ``str``
        """
        return self.input_provider.data_type

    @property
    def data(self) -> str | bytes:
        """
        :return: Document content
        :rtype: ``str`` or ``bytes``
        """
        return self.input_provider.data

    @property
    def metadata(self) -> dict:
        """
        :return: Document content
        :rtype: ``str`` or ``bytes``
        """
        return self._metadata

    @staticmethod
    def deserialize(document: dict):
        """
        Deserialize a document from JSON format.
        :param document: JSON representation of the document.
        :return: Document object.
        :rtype: ``Document``
        """
        from wowool.document.serialize import deserialize

        return deserialize(document)

    @staticmethod
    def from_json(
        document: dict,
    ):
        return Factory.from_json(
            id=document[WJ_ID], data=document[WJ_DATA], provider_type=document[WJ_DATA_TYPE], metadata=document.get(WJ_METADATA, {})
        )

    @staticmethod
    def create(
        data: str | bytes | None = None,
        id: Path | str | None = None,
        data_type: str = "",
        encoding="utf8",
        raw: bool = False,
        **kwargs,
    ):
        return Factory.create(
            id=id,
            data=data,
            provider_type=data_type,
            encoding=encoding,
            raw=raw,
            **kwargs,
        )

    @staticmethod
    def from_file(
        file: Path | str | None = None,
        data: str | bytes | None = None,
        data_type: str = "",
        encoding="utf8",
        **kwargs,
    ):
        return Factory.create(
            id=file,
            data=data,
            provider_type=data_type,
            encoding=encoding,
            **kwargs,
        )

    @staticmethod
    def glob(
        folder: Path | str,
        pattern: str = "**/*.txt",
        provider_type: str = "",
        resolve=_resolve__pass_thru,
        raw: bool = False,
        **kwargs,
    ):
        yield from Factory.glob(folder, pattern=pattern, provider_type=provider_type, resolve=resolve, raw=raw, **kwargs)
