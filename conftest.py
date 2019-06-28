import pytest
from fixture.application import Application


def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



# @pytest.fixture(scope="session") // если нужно все тесты делать не закрывая браузер, тоесть за одну сессию, создается только одна фикстура
# def app(request):
#     fixture = Application()
#     fixture.session.login(Logi(email="leha0793@mail.ru", password="qwerty12345")) // если все делается в одном логине
#     def fin():
#         fixture.session.logout()
#         fixture.destroy()
#     request.addfinalizer(fin)
#     return fixture
