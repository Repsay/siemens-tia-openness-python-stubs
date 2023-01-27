# encoding: utf-8
# module System.ServiceProcess.Design calls itself Design
# from System.ServiceProcess, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum

from System.Web.UI.MobileControls import Form

"""The following names are not found in the module: (ComponentDesigner, 
    field#)
"""

# no functions
# classes

class ServiceControllerDesigner(ComponentDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ ServiceControllerDesigner() """
    pass

class ServiceInstallerDialog(Form): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """ ServiceInstallerDialog() """
    @property
    def Password(self) -> str:
        """
        Get: Password(self: ServiceInstallerDialog) -> str
        Set: Password(self: ServiceInstallerDialog) = value
        """
        ...

    @property
    def Result(self) -> ServiceInstallerDialogResult:
        """ Get: Result(self: ServiceInstallerDialog) -> ServiceInstallerDialogResult """
        ...

    @property
    def Username(self) -> str:
        """
        Get: Username(self: ServiceInstallerDialog) -> str
        Set: Username(self: ServiceInstallerDialog) = value
        """
        ...


    @staticmethod
    def Main(): # -> 
        """ Main() """
        ...


class ServiceInstallerDialogResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ServiceInstallerDialogResult, values: Canceled (2), OK (0), UseSystem (1) """
    Canceled: ServiceInstallerDialogResult = ...
    OK: ServiceInstallerDialogResult = ...
    UseSystem: ServiceInstallerDialogResult = ...
    value__ = ...


