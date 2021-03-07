from typing import List

from .ImporterInterface import ImportInterface
from .Cat import Cat
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter
from .PDFImporter import PDFImporter
from .TXTImporter import TXTImporter


class Importer(ImportInterface):
    importers = [DocxImporter, CSVImporter, PDFImporter, TXTImporter]
 
    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)