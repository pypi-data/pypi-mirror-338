# -*- coding: utf-8 -*-

"""
    python_Testing_Utilities
    ~~~~~~~~
    python_Testing_Utilities
    :copyright: (c) 2019 by Robert Metcalf.
    :license: MIT, see LICENSE for more details.
"""

from .callService import callService, callGetService, callPostService, callPutService, callDeleteService, callServiceSendMultiPartFiles, callServiceSendMultiPartFilesAndData
from .pythonObjCompare import objectsEqual, assertObjectsEqual
from .assertMultiLineStringsEqual import areMultiLinesStringsEqual, assertMultiLineStringsEqual

#Exceptions
from .pythonObjCompare import DataObjectToComplexToCompare

from . import _version
__version__ = _version.get_versions()['version']
