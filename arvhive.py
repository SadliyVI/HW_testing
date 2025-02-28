class Archive:
    def __init__(self):
        self.documents = []
        self.directories = {}

    def get_name(self, doc_number: str) -> str:
        """Возвращает имя владельца документа по номеру."""
        for document in self.documents:
            if document["number"] == doc_number:
                return document["name"]
        return "Документ не найден"

    def get_directory(self, doc_number: str) -> str:
        """Возвращает номер полки по номеру документа."""
        for directory, numbers in self.directories.items():
            if doc_number in numbers:
                return directory
        return "Полки с таким документом не найдено"

    def add(self, document_type: str, number: str, name: str, shelf_number: str) -> None:
        """Добавляет документ на указанную полку."""
        if shelf_number not in self.directories:
            self.directories[shelf_number] = []
        if number not in [doc["number"] for doc in self.documents]:
            self.documents.append({"type": document_type, "number": number, "name": name})
            self.directories[shelf_number].append(number)