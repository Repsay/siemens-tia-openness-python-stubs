# encoding: utf-8
# module Microsoft.Vsa.Vb.CodeDOM calls itself CodeDOM
# from Microsoft.Vsa.Vb.CodeDOMProcessor, Version=8.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import UInt32

from System.CodeDom import CodeCompileUnit


# no functions
# classes

class CodeDOMProcessor(_CodeDOMProcessor): # skipped bases: <type 'object'>
    """ CodeDOMProcessor() """
    pass

class Location(_Location): # skipped bases: <type 'object'>
    """ Location() """
    pass

class _CodeDOMProcessor: # skipped bases: <type 'object'>
    """ no doc """
    def CodeDOMFromXML(self, xmlStream:str) -> CodeCompileUnit:
        """ CodeDOMFromXML(self: _CodeDOMProcessor, xmlStream: str) -> CodeCompileUnit """
        ...


class _Location: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BeginningColumn(self) -> UInt32:
        """
        Get: BeginningColumn(self: _Location) -> UInt32
        Set: BeginningColumn(self: _Location) = value
        """
        ...

    @property
    def BeginningLine(self) -> UInt32:
        """
        Get: BeginningLine(self: _Location) -> UInt32
        Set: BeginningLine(self: _Location) = value
        """
        ...

    @property
    def EndColumn(self) -> UInt32:
        """
        Get: EndColumn(self: _Location) -> UInt32
        Set: EndColumn(self: _Location) = value
        """
        ...

    @property
    def EndLine(self) -> UInt32:
        """
        Get: EndLine(self: _Location) -> UInt32
        Set: EndLine(self: _Location) = value
        """
        ...



