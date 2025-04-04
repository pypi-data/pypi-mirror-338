"""Paquete de SmartGO para compartir modelos entre aplicaciones"""

__version__ = '0.1.3'
__author__ = 'Vanda Dev'
__email__ = 'kevins.villatoro@vanda.cl'


from .models.entidad import Entidad
from .models.test import Message


__all__ = ['Entidad', 'Message']