from dotenv import dotenv_values

def load_settings():
    return dotenv_values(".env")

