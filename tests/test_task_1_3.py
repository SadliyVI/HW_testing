import pytest
from arvhive import Archive


class TestArchive:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.archive = Archive()
        self.archive.documents = [
            {'type': 'passport', 'number': '2207 876234',
             'name': 'Василий Гупкин'},
            {'type': 'invoice', 'number': '11-2',
             'name': 'Геннадий Покемонов'},
            {'type': 'insurance', 'number': '10006',
             'name': 'Аристарх Павлов'},
            {'type': 'driver license', 'number': '5455 028765',
             'name': 'Василий Иванов'},
        ]
        self.archive.directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        }

    def teardown_method(self):
        del self.archive

    def test_get_name_existing_doc(self):
        assert self.archive.get_name('10006') == 'Аристарх Павлов'

    def test_get_name_non_existing_doc(self):
        assert self.archive.get_name('999') == 'Документ не найден'


    @pytest.mark.parametrize('doc_number, expected_dir', [
        ('2207 876234', '1'),
        ('10006', '2'),
        ('999', 'Полки с таким документом не найдено')
    ])
    def test_get_directory(self, doc_number, expected_dir):
        assert self.archive.get_directory(doc_number) == expected_dir

    @pytest.mark.parametrize('doc_type, number, name, shelf_num', [
        ('passport', '12345', 'Иван Петров', '1'),
        ('insurance', '67890', 'Мария Сидорова', '4')
    ])
    def test_add_document(self, doc_type, number, name, shelf_num):
        initial_docs_count = len(self.archive.documents)
        initial_shelf_count = len(self.archive.directories.get(shelf_num, []))
        self.archive.add(doc_type, number, name, shelf_num)
        # Проверка, что документ добавился
        assert len(self.archive.documents) == initial_docs_count + 1
        assert any(doc['number'] == number for doc in self.archive.documents)
        # Проверка, что документ добавился на полку
        assert len(self.archive.directories[shelf_num]) == initial_shelf_count + 1