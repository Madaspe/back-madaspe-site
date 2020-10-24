class DatabaseObject:
    def __init__(self):
        self._collection_name = "FlaskAppCol"
        self._database_name = "FlaskAppDb"

    @property
    def database_name(self):
        return self._database_name

    @property
    def collection_name(self):
        return self._collection_name


class File(DatabaseObject):
    def __init__(self, file_name: str, save_path: str):
        super().__init__()

        self.file_name = file_name
        self.save_path = save_path
        self.file_extension = None

        self.detect_file_extension()

    def detect_file_extension(self):
        splited_file_name = self.file_name.split('.')
        if len(splited_file_name) == 2:
            self.file_extension = splited_file_name[1]
