from typing import Protocol, runtime_checkable, Any
from wowool.document.defines import WJ_ID, WJ_DATA, WJ_DATA_TYPE, WJ_METADATA


@runtime_checkable
class DocumentInterface(Protocol):
    """
    :class:`DocumentInterface` is an interface utility to handle data input.
    """

    @property
    def id(self) -> str:
        pass

    @property
    def data_type(self) -> str:
        pass

    @property
    def data(self) -> Any:
        pass

    @property
    def metadata(self) -> dict:
        pass

    def to_json(self):
        """
        Convert the document to JSON format.
        :return: JSON representation of the document.
        :rtype: ``dict``
        """
        return {
            WJ_ID: self.id,
            WJ_DATA: self.data,
            WJ_DATA_TYPE: self.data_type,
            WJ_METADATA: self.metadata,
        }

    def serialize(self):
        """
        Convert the document to JSON format.
        :return: JSON representation of the document.
        :rtype: ``dict``
        """
        from wowool.document.serialize import serialize

        return serialize(self)
