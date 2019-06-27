import pytest
from model.logi import Logi
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_Page(app):
    app.session.login(Logi(email="leha0793@mail.ru", password="qwerty12345"))
    app.notepad.create()
    app.notepad.add_page()
    app.notepad.delete()
    app.session.logout()

