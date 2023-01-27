# encoding: utf-8
# module Microsoft.PowerShell.Commands.Internal.Format calls itself Format
# from System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, IDisposable

from System.Management.Automation import PSCmdlet, PSObject, SwitchParameter


# no functions
# classes

class FrontEndCommandBase(IDisposable, PSCmdlet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InputObject(self) -> PSObject:
        """
        Get: InputObject(self: FrontEndCommandBase) -> PSObject
        Set: InputObject(self: FrontEndCommandBase) = value
        """
        ...


    def InputObjectCall(self, *args): #cannot find CLR method
        """ InputObjectCall(self: FrontEndCommandBase) -> PSObject """
        ...

    def InternalDispose(self, *args): #cannot find CLR method
        """ InternalDispose(self: FrontEndCommandBase) """
        ...

    def OuterCmdletCall(self, *args): #cannot find CLR method
        """ OuterCmdletCall(self: FrontEndCommandBase) -> PSCmdlet """
        ...

    def WriteObjectCall(self, *args): #cannot find CLR method
        """ WriteObjectCall(self: FrontEndCommandBase, value: object) """
        ...


class OuterFormatShapeCommandBase(FrontEndCommandBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ OuterFormatShapeCommandBase() """
    @property
    def DisplayError(self) -> SwitchParameter:
        """
        Get: DisplayError(self: OuterFormatShapeCommandBase) -> SwitchParameter
        Set: DisplayError(self: OuterFormatShapeCommandBase) = value
        """
        ...

    @property
    def Expand(self) -> str:
        """
        Get: Expand(self: OuterFormatShapeCommandBase) -> str
        Set: Expand(self: OuterFormatShapeCommandBase) = value
        """
        ...

    @property
    def Force(self) -> SwitchParameter:
        """
        Get: Force(self: OuterFormatShapeCommandBase) -> SwitchParameter
        Set: Force(self: OuterFormatShapeCommandBase) = value
        """
        ...

    @property
    def GroupBy(self) -> object:
        """
        Get: GroupBy(self: OuterFormatShapeCommandBase) -> object
        Set: GroupBy(self: OuterFormatShapeCommandBase) = value
        """
        ...

    @property
    def ShowError(self) -> SwitchParameter:
        """
        Get: ShowError(self: OuterFormatShapeCommandBase) -> SwitchParameter
        Set: ShowError(self: OuterFormatShapeCommandBase) = value
        """
        ...

    @property
    def View(self) -> str:
        """
        Get: View(self: OuterFormatShapeCommandBase) -> str
        Set: View(self: OuterFormatShapeCommandBase) = value
        """
        ...



class OuterFormatTableAndListBase(OuterFormatShapeCommandBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ OuterFormatTableAndListBase() """
    @property
    def Property(self) -> Array:
        """
        Get: Property(self: OuterFormatTableAndListBase) -> Array[object]
        Set: Property(self: OuterFormatTableAndListBase) = value
        """
        ...



class OuterFormatTableBase(OuterFormatTableAndListBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ OuterFormatTableBase() """
    @property
    def AutoSize(self) -> SwitchParameter:
        """
        Get: AutoSize(self: OuterFormatTableBase) -> SwitchParameter
        Set: AutoSize(self: OuterFormatTableBase) = value
        """
        ...

    @property
    def HideTableHeaders(self) -> SwitchParameter:
        """
        Get: HideTableHeaders(self: OuterFormatTableBase) -> SwitchParameter
        Set: HideTableHeaders(self: OuterFormatTableBase) = value
        """
        ...

    @property
    def RepeatHeader(self) -> SwitchParameter:
        """
        Get: RepeatHeader(self: OuterFormatTableBase) -> SwitchParameter
        Set: RepeatHeader(self: OuterFormatTableBase) = value
        """
        ...

    @property
    def Wrap(self) -> SwitchParameter:
        """
        Get: Wrap(self: OuterFormatTableBase) -> SwitchParameter
        Set: Wrap(self: OuterFormatTableBase) = value
        """
        ...



