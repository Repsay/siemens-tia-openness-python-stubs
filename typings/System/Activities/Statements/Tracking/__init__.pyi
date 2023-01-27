# encoding: utf-8
# module System.Activities.Statements.Tracking calls itself Tracking
# from System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Activities.Tracking import (CustomTrackingQuery, 
    CustomTrackingRecord)


# no functions
# classes

class StateMachineStateQuery(CustomTrackingQuery): # skipped bases: <type 'object'>
    """ StateMachineStateQuery() """
    pass

class StateMachineStateRecord(CustomTrackingRecord): # skipped bases: <type 'object'>
    """ StateMachineStateRecord() """
    @property
    def StateMachineName(self) -> str:
        """ Get: StateMachineName(self: StateMachineStateRecord) -> str """
        ...

    @property
    def StateName(self) -> str:
        """ Get: StateName(self: StateMachineStateRecord) -> str """
        ...



