import os

def read_env(env_file):
    """ .env faylidan o'zgaruvchilarni o'qish """
    env_data = {}
    with open(env_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                env_data[key] = value


def create_env(env_file):
    """ .env faylini yaratish """
    with open(env_file, "w") as f:
        f.write("# .env fayli\n")
    print("\033[92m" + f"{env_file} yaratildi!" + "\033[0m")  # Yashil rang
    
    
def create_init_py():
    """ utils/__init__.py faylini yaratish va ichiga `from . import env` yozish """
    init_py_path = os.path.join("utils", "__init__.py")
    with open(init_py_path, "w") as f:
        f.write("from . import env\n")


def create_env_file():
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write("")  
        print("\033[92m" + "`.env` fayli yaratildi!" + "\033[0m")  # Yashil rang

def create_utils_folder():
    if not os.path.exists("utils"):
        os.makedirs("utils")
        print("\033[92m" + "`utils` papkasi yaratildi." + "\033[0m")  # Yashil rang


def create_env_py():
    env_py_path = os.path.join("utils", "env.py")
    with open(".env", "r") as env_file:
        lines = env_file.readlines()

    if not lines:  # Agar .env bo'sh bo'lsa
        print("\033[91m" + ".env bo'sh!" + "\033[0m")  # Qizil rang
        return

    with open(env_py_path, "w") as f:
        f.write('''from environs import Env

env = Env()
env.read_env()

''')
        for line in lines:
            if '=' in line:
                key = line.split('=')[0].strip()
                f.write(f"{key} = env('{key}')\n")

    print("\033[93m" + "`env.py` yangilandi." + "\033[0m")  # Sariq rang
