from dataclasses import dataclass
from typing import Dict
from datetime import datetime

# 1. Clase Usuario
@dataclass
class Usuario:
    id: int = 0
    uuid: str = ""
    usuario: str = ""
    imagen: str = ""

# 2. Clase Registro
@dataclass
class Registro:
    usuario: Usuario = None
    ts: datetime = None

# 3. Clase Base 
@dataclass
class Base:
    id: int = 0
    uuid: str = ""
    codigo: str = ""
    descripcion: str = ""
    atributos: Dict = None
    creado_por: Registro = None
    modificado_por: Registro = None

# 4. Clase Entidad 
@dataclass
class Entidad(Base):
    entidad: str = ""
    idTipoEntidad: int = 0
    idClasificacion: int = 0
    idCategoria: int = 0
    idEstado: int = 0
    usuarios: Dict = None
    contactos: Dict = None
    adjuntos: Dict = None
    direcciones: Dict = None
    relaciones: Dict = None
    asociaciones: Dict = None

    def __post_init__(self):
        self.codigo = self.codigo or "E001"
        self.descripcion = self.descripcion or "Esta es una entidad"
        self.atributos = self.atributos or {"atrib 1": "at1"}
        self.entidad = self.entidad or "Entidad por defecto"
        self.idTipoEntidad = self.idTipoEntidad or 1
        self.idClasificacion = self.idClasificacion or 1
        self.idCategoria = self.idCategoria or 1
        self.idEstado = self.idEstado or 1
        self.usuarios = self.usuarios or {"user 1": "usr1"}
        self.contactos = self.contactos or {"user 1": "usr1"}
        self.adjuntos = self.adjuntos or {"archivo 1": "file.pdf"}
        self.direcciones = self.direcciones or {"x": "12345", "y": "6789"}
        self.relaciones = self.relaciones or {"relac 1": "rlc1"}
        self.asociaciones = self.asociaciones or {"asoc 1": "asc1"}
