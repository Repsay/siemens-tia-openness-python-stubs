# encoding: utf-8
# module System.Windows.Threading calls itself Threading
# from System.Windows.Presentation, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Action, TimeSpan

from System.Threading.Tasks import Task

"""The following names are not found in the module: (Dispatcher, 
    DispatcherOperation, DispatcherOperationStatus, DispatcherPriority)
"""

# no functions
# classes

class DispatcherExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def BeginInvoke(dispatcher, action:Action, priority = ...): # -> DispatcherOperation # Not found arg types: {'priority': 'DispatcherPriority', 'dispatcher': 'Dispatcher'}
        """
        BeginInvoke(dispatcher: Dispatcher, action: Action) -> DispatcherOperation
        BeginInvoke(dispatcher: Dispatcher, action: Action, priority: DispatcherPriority) -> DispatcherOperation
        """
        ...

    @staticmethod
    def Invoke(dispatcher, action:Action, *__args): # ->  # Not found arg types: {'*__args': 'DispatcherPriority', 'dispatcher': 'Dispatcher'}
        """ Invoke(dispatcher: Dispatcher, action: Action)Invoke(dispatcher: Dispatcher, action: Action, priority: DispatcherPriority)Invoke(dispatcher: Dispatcher, action: Action, timeout: TimeSpan)Invoke(dispatcher: Dispatcher, action: Action, timeout: TimeSpan, priority: DispatcherPriority) """
        ...

    __all__: list = ...


class TaskExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def DispatcherOperationWait(this:Task, timeout:TimeSpan = ...): # -> DispatcherOperationStatus
        """
        DispatcherOperationWait(this: Task) -> DispatcherOperationStatus
        DispatcherOperationWait(this: Task, timeout: TimeSpan) -> DispatcherOperationStatus
        """
        ...

    @staticmethod
    def IsDispatcherOperationTask(this:Task) -> bool:
        """ IsDispatcherOperationTask(this: Task) -> bool """
        ...

    __all__: list = ...


