from typing import Protocol, runtime_checkable, Any
from wowool.document.defines import WJ_ID, WJ_DATA, WJ_DATA_TYPE, WJ_METADATA
from typing import Literal

DataType = Literal[
    "text/utf8",
    "text/raw",
    "md/utf8",
    "html/utf8",
    "html/raw",
    "pdf/utf8",
    "pdf/raw",
    "docx/utf8",
    "docx/raw",
    "analysis/json",
]


@runtime_checkable
class DocumentInterface(Protocol):
    """
    :class:`DocumentInterface` is an interface utility to handle data input.
    """

    @property
    def id(self) -> str:
        pass

    @property
    def data_type(self) -> DataType:
        pass

    @property
    def data(self) -> Any:
        pass

    @property
    def metadata(self) -> dict[str, Any]:
        pass

    def serialize(self):
        """
        Convert the document to JSON format.
        :return: JSON representation of the document.
        :rtype: ``dict``
        """
        from wowool.document.serialize import serialize

        return serialize(self)
