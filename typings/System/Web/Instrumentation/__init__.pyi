# encoding: utf-8
# module System.Web.Instrumentation calls itself Instrumentation
# from System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Collections import IList

from System.IO import TextWriter


# no functions
# classes

class PageExecutionContext: # skipped bases: <type 'object'>, <type 'object'>
    """ PageExecutionContext() """
    @property
    def IsLiteral(self) -> bool:
        """
        Get: IsLiteral(self: PageExecutionContext) -> bool
        Set: IsLiteral(self: PageExecutionContext) = value
        """
        ...

    @property
    def Length(self) -> int:
        """
        Get: Length(self: PageExecutionContext) -> int
        Set: Length(self: PageExecutionContext) = value
        """
        ...

    @property
    def StartPosition(self) -> int:
        """
        Get: StartPosition(self: PageExecutionContext) -> int
        Set: StartPosition(self: PageExecutionContext) = value
        """
        ...

    @property
    def TextWriter(self) -> TextWriter:
        """
        Get: TextWriter(self: PageExecutionContext) -> TextWriter
        Set: TextWriter(self: PageExecutionContext) = value
        """
        ...

    @property
    def VirtualPath(self) -> str:
        """
        Get: VirtualPath(self: PageExecutionContext) -> str
        Set: VirtualPath(self: PageExecutionContext) = value
        """
        ...



class PageExecutionListener: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def BeginContext(self, context:PageExecutionContext): # -> 
        """ BeginContext(self: PageExecutionListener, context: PageExecutionContext) """
        ...

    def EndContext(self, context:PageExecutionContext): # -> 
        """ EndContext(self: PageExecutionListener, context: PageExecutionContext) """
        ...


class PageInstrumentationService: # skipped bases: <type 'object'>, <type 'object'>
    """ PageInstrumentationService() """
    @property
    def ExecutionListeners(self) -> IList:
        """ Get: ExecutionListeners(self: PageInstrumentationService) -> IList[PageExecutionListener] """
        ...

    @property
    def IsEnabled(self) -> bool:
        """
        Get: IsEnabled() -> bool
        Set: IsEnabled() = value
        """
        ...




