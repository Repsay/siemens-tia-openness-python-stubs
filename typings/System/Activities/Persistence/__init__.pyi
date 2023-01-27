# encoding: utf-8
# module System.Activities.Persistence calls itself Persistence
# from System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
"""The following names are not found in the module: (
    IPersistencePipelineModule)
"""

# no functions
# classes

class PersistenceParticipant(IPersistencePipelineModule): # skipped bases: <type 'object'>
    """ no doc """
    def CollectValues(self, *args): #cannot find CLR method
        """ CollectValues(self: PersistenceParticipant) -> (IDictionary[XName, object], IDictionary[XName, object]) """
        ...

    def MapValues(self, *args): #cannot find CLR method
        """ MapValues(self: PersistenceParticipant, readWriteValues: IDictionary[XName, object], writeOnlyValues: IDictionary[XName, object]) -> IDictionary[XName, object] """
        ...

    def PublishValues(self, *args): #cannot find CLR method
        """ PublishValues(self: PersistenceParticipant, readWriteValues: IDictionary[XName, object]) """
        ...


class PersistenceIOParticipant(PersistenceParticipant): # skipped bases: <type 'IPersistencePipelineModule'>, <type 'object'>
    """ no doc """
    def Abort(self, *args): #cannot find CLR method
        """ Abort(self: PersistenceIOParticipant) """
        ...

    def BeginOnLoad(self, *args): #cannot find CLR method
        """ BeginOnLoad(self: PersistenceIOParticipant, readWriteValues: IDictionary[XName, object], timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginOnSave(self, *args): #cannot find CLR method
        """ BeginOnSave(self: PersistenceIOParticipant, readWriteValues: IDictionary[XName, object], writeOnlyValues: IDictionary[XName, object], timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndOnLoad(self, *args): #cannot find CLR method
        """ EndOnLoad(self: PersistenceIOParticipant, result: IAsyncResult) """
        ...

    def EndOnSave(self, *args): #cannot find CLR method
        """ EndOnSave(self: PersistenceIOParticipant, result: IAsyncResult) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, isSaveTransactionRequired: bool, isLoadTransactionRequired: bool) """
        ...


