# coding: utf-8

from __future__ import unicode_literals

__author__ = 'Filipe Ximenes'
__email__ = 'filipeximenes@gmail.com'
__version__ = 'fix-iterator-list'


from .adapters import (
    generate_wrapper_from_adapter,
    TapiocaAdapter,
    FormAdapterMixin, JSONAdapterMixin)
