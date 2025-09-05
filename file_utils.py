# file_utils.py

import os

def ensure_directory(path: str) -> None:
    """
    Stellt sicher, dass das Verzeichnis existiert.
    Falls nicht, wird es erstellt.
    """
    os.makedirs(path, exist_ok=True)


def get_filename_without_extension(file_path: str) -> str:
    """
    Gibt den Dateinamen ohne Extension zurück.
    """
    return os.path.splitext(os.path.basename(file_path))[0]
