from dataclasses import dataclass


# 1. Clase de Prueba
@dataclass
class Message:
    contenido: str = ""
    idioma: str = ""