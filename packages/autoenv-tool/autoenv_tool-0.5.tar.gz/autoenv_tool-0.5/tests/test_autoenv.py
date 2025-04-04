# tests/test_autoenv.py
import os
import pytest
from autoenv_tool.utils.env import read_env, create_env


@pytest.fixture
def env_file(tmpdir):
    """ Temporary .env faylini yaratish uchun fixture """
    env_path = tmpdir.join(".env")
    env_path.write("BOT_TOKEN=my_token_value")
    return env_path


def test_read_env(env_file):
    """ .env faylini to'g'ri o'qish """
    env_data = read_env(str(env_file))
    assert env_data == {"BOT_TOKEN": "my_token_value"}


def test_create_env(tmpdir):
    """ .env faylini yaratish """
    env_path = tmpdir.join(".env")
    create_env(str(env_path))
    assert os.path.exists(str(env_path))
    with open(str(env_path), "r") as f:
        content = f.read()
    assert content == "# .env fayli\n"
