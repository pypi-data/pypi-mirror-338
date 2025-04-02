from wowool.document.document_interface import DocumentInterface
from bs4 import BeautifulSoup
from io import StringIO


class HTMLFileInputProvider(DocumentInterface):
    DATA_TYPE = "html_"

    def __init__(self, fid, encoding="utf8"):
        self._id = str(fid)
        self.encoding = encoding

    @property
    def id(self) -> str:
        return self._id

    @property
    def data_type(self) -> str:
        return self.DATA_TYPE

    @property
    def text(self, **kwargs):
        with open(self.id(), "r", encoding=self.encoding) as f:
            html_data = f.read()
            soup = BeautifulSoup(html_data, "html.parser")
            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()  # rip it out

            # get text
            text = soup.get_text(" ")

            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())

            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            sio = StringIO()
            prevcontent = ""
            for mychunk in chunks:
                if mychunk == "":
                    continue
                if mychunk[-1:] != ".":
                    mychunk = mychunk + "."
                filecontent = mychunk + "\n"
                if filecontent != prevcontent:
                    sio.write(filecontent)
                    prevcontent = filecontent

            text = sio.getvalue()
            sio.close()
            return text
