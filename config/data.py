import os
import dotenv # позволяет загружать переменные окружения из файла .env вместо их жёсткого прописывания в коде


class Data:
    """
    Класс с переменными окружения, значения которых подтягиваются из .env
    """
    dotenv.load_dotenv()
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
