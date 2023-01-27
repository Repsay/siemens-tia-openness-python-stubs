# encoding: utf-8
# module System.Activities.ExpressionParser calls itself ExpressionParser
# from System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Collections import IEnumerable

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class SourceExpressionException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SourceExpressionException()
    SourceExpressionException(message: str)
    SourceExpressionException(message: str, innerException: Exception)
    SourceExpressionException(message: str, errors: CompilerErrorCollection)
    """
    @property
    def Errors(self) -> IEnumerable:
        """ Get: Errors(self: SourceExpressionException) -> IEnumerable[CompilerError] """
        ...


    SerializeObjectState = ...


