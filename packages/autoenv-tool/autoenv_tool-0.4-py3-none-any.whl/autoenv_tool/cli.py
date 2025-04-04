import os
import sys
from autoenv_tool.utils.env import (
    read_env, create_env, create_env_file, create_utils_folder, create_env_py, create_init_py
)


def autoenv():
    """ Terminaldan `autoenv` deb yozilganda ishga tushadi """
    env_file = ".env"

    if not os.path.exists(env_file):
        ans = input(".env fayli mavjud emas. Yaratilsinmi? (y/n): ").strip().lower()
        if ans == "y":
            create_env(env_file)
            print(".env yaratildi!")
            return 
        else:
            print("Amal bekor qilindi.")
            sys.exit(0)

    env_data = read_env(env_file)
    
    if not env_data: 
        return  

    print("\n🔹 .env dagi o‘zgaruvchilar:")
    for key, value in env_data.items():
        print(f"{key} = {value}")

    confirm = input("\n♻️  Ushbu o‘zgaruvchilarni yuklashni istaysizmi? (y/n): ").strip().lower()
    if confirm == "y" or confirm == "": 
        for key, value in env_data.items():
            os.environ[key] = value
        print("✅ O‘zgaruvchilar yuklandi!")
    else:
        print("❌ Yuklash bekor qilindi.")
        
        
def create():
    """ `autoenv` paketini o'rnatish uchun yordamchi funksiya """
    create_env_file()
    create_utils_folder()
    create_env_py()
    create_init_py()


create()
