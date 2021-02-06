import json

class Config:
    def __init__(self, filename: str):
        self.file = open(filename, 'r+', encoding='utf-8')
        self.data = {}
        self._load()

    def _load(self):
        self.data = json.load(self.file)


    # public getters
    def getColumns(self) -> int:
        return int(self.data['columns'])

    def getRows(self) -> int:
        return int(self.data['rows'])
