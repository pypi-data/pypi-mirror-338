import os
import sys
from autoenv_tool.utils.env import (
    read_env, create_env, create_env_file, create_utils_folder, create_env_py, create_init_py
)

# Rang kodlari
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


def check_env_changes():
    """ .env va env.py dagi o‘zgaruvchilarni solishtiradi """
    env_file = ".env"
    env_py_file = "utils/env.py"

    if not os.path.exists(env_file) or not os.path.exists(env_py_file):
        return True  # Agar fayllardan biri yo‘q bo‘lsa, yangilanish kerak
    
    env_data = read_env(env_file)  # .env dagi o‘zgaruvchilar
    env_py_data = {}

    with open(env_py_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "=" in line and "env(" in line:  
                parts = line.split("=")
                key = parts[0].strip()
                value = parts[1].strip().replace("env(", "").replace(")", "").replace('"', "").replace("'", "")
                env_py_data[key] = value  

    return env_data != env_py_data  


def autoenv():
    """ Terminaldan `autoenv` deb yozilganda ishga tushadi """
    env_file = ".env"
    
    if not check_env_changes():
        print(YELLOW + "⚠️  Yangilanish yo‘q, barcha o‘zgaruvchilar avval yuklangan." + RESET)
        return

    if not os.path.exists(env_file):
        print(RED + ".env fayli mavjud emas!" + RESET)
        return 

    env_data = read_env(env_file)

    if not env_data:
        return  

    

    print(BLUE + "\n🔹 .env dagi o‘zgaruvchilar:" + RESET)
    for key, value in env_data.items():
        print(f"{YELLOW}{key}{RESET} = {GREEN}{value}{RESET}")

    confirm = input(YELLOW + "\n♻️  Ushbu o‘zgaruvchilarni yuklashni istaysizmi? (y/n): " + RESET).strip().lower()


    if confirm == "y": 
        for key, value in env_data.items():
            os.environ[key] = value
        print(GREEN + "✅ O‘zgaruvchilar yuklandi!" + RESET)
    else:
        print(RED + "❌ Yuklash bekor qilindi." + RESET)


        
def create():
    """ `autoenv` paketini o'rnatish uchun yordamchi funksiya """
    create_env_file()
    create_utils_folder()
    create_env_py()
    create_init_py()


create()
