# autoenv/utils/env.py
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
    return env_data


def create_env(env_file):
    """ .env faylini yaratish """
    with open(env_file, "w") as f:
        f.write("# .env fayli\n")
    print(f"{env_file} yaratildi!")
    
    
    

def create_env_file():
    # Bosh papkani tekshirish va .env faylini yaratish
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write("BOT_TOKEN=dusddufa dsfgasdf7f67d6sfads\n")
            f.write("DATABASE_URL=postgres://user:password@localhost/dbname\n")
            # Boshqa misollar kiritilishi mumkin
        print("`.env` fayli yaratildi!")
    else:
        with open(".env", "r") as f:
            content = f.read()
            if not content.strip():  # Fayl bo'sh bo'lsa
                print("Qizil: `.env` faylini to'ldiring!")
            else:
                print("`.env` faylida ma'lumot mavjud.")

def create_utils_folder():
    if not os.path.exists("utils"):
        os.makedirs("utils")
        print("`utils` papkasi yaratildi.")
        

def create_env_py():
    env_py_path = os.path.join("utils", "env.py")
    if not os.path.exists(env_py_path):
        with open(env_py_path, "w") as f:
            f.write('''from environs import Env

env = Env()
env.read_env()

''')
            
            # .env faylidan barcha kalitlarni o'qib, har birini mos ravishda chaqiradi
            with open(".env", "r") as env_file:
                for line in env_file:
                    if '=' in line:
                        key = line.split('=')[0].strip()
                        f.write(f"{key} = env('{key}')\n")
        print("`env.py` fayli yaratildi.")

def main():
    create_env_file()
    create_utils_folder()
    create_env_py()

if __name__ == "__main__":
    main()

