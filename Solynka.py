import time
import pytest
from logi import Logi
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_Page(app):
    app.login(Logi(email="leha0793@mail.ru", password="qwerty12345"))
    app.create_notepad()
    app.add_page()
    app.delete_notepad()
    app.logout()
    time.sleep(5)
