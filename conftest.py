import pytest
from fixture.application import Application

# @pytest.fixture(scope="session") // если нужно все тесты делать не закрывая браузер, тоесть за одну сессию
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
