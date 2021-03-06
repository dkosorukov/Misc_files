from typing import List
import pandas

from .ImporterInterface import ImportInterface
from .Cat import Cat

class CSVImporter(ImportInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")

        cats = []
        df = pandas.read_csv(path, header=0)

        for idx, row in df.iterrows():
            new_cat = Cat(row['Name'], row['Age'], row['isIndoor'])
            cats.append(new_cat)
        
        return cats
