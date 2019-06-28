from model.logi import Logi


def test_add_Page(app):
    app.session.login(Logi(email="leha0793@mail.ru", password="qwerty12345"))
    app.notepad.create()
    app.notepad.add_page()
    app.notepad.delete()
    app.session.logout()

