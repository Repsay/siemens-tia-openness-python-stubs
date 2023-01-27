# encoding: utf-8
# module System.Messaging.Design calls itself Design
# from System.Messaging, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import EventArgs, IServiceProvider

from System.Drawing.Design import UITypeEditor

from System.Messaging import MessageQueue

from System.Web.UI.MobileControls import Form

from typing import Self

"""The following names are not found in the module: ComponentDesigner
"""

# no functions
# classes

class MessageDesigner(ComponentDesigner): # skipped bases: <type 'IDisposable'>, <type 'IDesignerFilter'>, <type 'IDesigner'>, <type 'IComponentInitializer'>, <type 'ITreeDesigner'>, <type 'object'>
    """ MessageDesigner() """
    pass

class QueuePathDialog(Form): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IViewObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'IContainerControl'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IOleObject'>, <type 'object'>
    """
    QueuePathDialog(provider: IServiceProvider)
    QueuePathDialog(uiService: IUIService)
    """
    @property
    def Path(self) -> str:
        """ Get: Path(self: QueuePathDialog) -> str """
        ...


    def ChoosePath(self): # -> 
        """ ChoosePath(self: QueuePathDialog) """
        ...

    def DoubleClicked(self, source:object, e:EventArgs): # -> 
        """ DoubleClicked(self: QueuePathDialog, source: object, e: EventArgs) """
        ...

    def SelectQueue(self, queue:MessageQueue): # -> 
        """ SelectQueue(self: QueuePathDialog, queue: MessageQueue) """
        ...

    def __new__(cls, *__args:IServiceProvider) -> Self:
        """
        __new__(cls: type, provider: IServiceProvider)
        __new__(cls: type, uiService: IUIService)
        """
        ...


class QueuePathEditor(UITypeEditor): # skipped bases: <type 'object'>
    """ QueuePathEditor() """
    pass

