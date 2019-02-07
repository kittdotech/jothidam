from flask import Flask
import pytest

@pytest.fixture
def app():
    app = Flask('Jothidam Test')
    return app