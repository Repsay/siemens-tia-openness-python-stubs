# encoding: utf-8
# module Siemens.Engineering.SW.Blocks.Exceptions calls itself Exceptions
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import EngineeringTargetInvocationException

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class DataBlockCreationNotAllowedException(EngineeringTargetInvocationException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>, <type 'object'>
    """
    This exception indicates that exception occured during creation of DataBlock.
    DataBlockCreationNotAllowedException()
    DataBlockCreationNotAllowedException(text: str)
    DataBlockCreationNotAllowedException(text: str, exception: Exception)
    DataBlockCreationNotAllowedException(text: str, *detailTexts: Array[str])
    """
    SerializeObjectState = ...


