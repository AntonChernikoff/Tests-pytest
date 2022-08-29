import pytest
import functions

class Test_Functions:
    # def setup(self):
    #     print("метод setup")
    # def teardown(self):
    #     print("метод teardown")

    def test_add_document(self):
        document_number = "test-123"
        document_type = "test type"
        document_owner = "test module"
        document_storage = "3"
        res = f"    Документ {document_type} № \"{document_number}\" принадлежит \"{document_owner}\" Сохранет на {document_storage} полке."
        assert functions.document_add(document_number,document_type,document_owner,document_storage) == res

    def test_search_by_storage(self):
        document_number = "test-123"
        res = f"    Документ № {document_number} хранится на полке №-3"
        assert functions.search_by_storage(document_number, functions.directories) == res

    def test_owner_by_document(self):
        document_number = "test-123"
        document_owner = "test module"
        res = f"    Документ № {document_number} принадлежит {document_owner}"
        assert functions.owner_by_document(document_number, functions.documents) == res

    def test_search_by_storage(self):
        document_number = "test-123"
        document_storage = "3"
        res = f"    Документ № {document_number} хранится на полке №-{document_storage}"
        assert functions.search_by_storage(document_number,functions.directories) == res

    def test_move_document(self):
        document_number = "test-123"
        document_type = "test type"
        document_owner = "test module"
        document_storage = "1"
        res = f"    Документ {document_type} № \"{document_number}\" принадлежит \"{document_owner}\" Сохранет на {document_storage} полке."
        assert functions.move_document(document_number, document_storage) == res

    def test_document_del(self):
        document_number = "test-123"
        document_storage = "1"
        res = f"    Документ №{document_number} удален с полки №-{document_storage}/n"
        res += f"    Документ с номером № {document_number} удален из системы."
        assert functions.document_del(document_number) == res

    def test_search_by_storage_end(self):
        document_number = "test-123"
        res = f"    Указанный документ № {document_number} не найден на полках."
        assert functions.search_by_storage(document_number,functions.directories) == res