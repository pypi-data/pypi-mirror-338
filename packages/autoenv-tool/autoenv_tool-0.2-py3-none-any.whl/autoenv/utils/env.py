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
