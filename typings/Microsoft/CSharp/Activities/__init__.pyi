# encoding: utf-8
# module Microsoft.CSharp.Activities calls itself Activities
# from System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Activities import CodeActivity

from System.Activities.Expressions import ITextExpression

from typing import Self


# no functions
# classes

class CSharpReference(ITextExpression, CodeActivity): # skipped bases: <type 'object'>
    """
    CSharpReference[TResult]()
    CSharpReference[TResult](expressionText: str)
    """
    def __new__(cls, expressionText:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, expressionText: str)
        """
        ...


class CSharpValue(ITextExpression, CodeActivity): # skipped bases: <type 'object'>
    """
    CSharpValue[TResult]()
    CSharpValue[TResult](expressionText: str)
    """
    def __new__(cls, expressionText:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, expressionText: str)
        """
        ...


