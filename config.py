import json

class Config:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, filename: str = 'settings.json'):
        self.filename = filename
        self._data = {}
        self._load()

    def _load(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            self._data = json.load(file)

    def _save(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.seek(0)
            json.dump(self._data, file, indent=4)
            file.truncate()


    # GETTERS
    # def getColumns(self) -> int:
    #     return int(self.data['columns'])
    #
    # def getRows(self) -> int:
    #     return int(self.data['rows'])

    def getDevice(self):
        return self._data.get('device')

    # SETTERS
    def setDevice(self, device: int):
        self._data['device'] = device
        self._save()