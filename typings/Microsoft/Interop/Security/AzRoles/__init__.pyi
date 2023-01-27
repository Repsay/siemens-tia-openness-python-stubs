# encoding: utf-8
# module Microsoft.Interop.Security.AzRoles calls itself AzRoles
# from Microsoft.Interop.Security.AzRoles, Version=2.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, UInt32, UInt64

from System.Collections import IEnumerable

from typing import Tuple as Tuple_

"""The following names are not found in the module: __ComObject, field#
"""

# no functions
# classes

class IAzAuthorizationStore: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApplicationData(self) -> str:
        """
        Get: ApplicationData(self: IAzAuthorizationStore) -> str
        Set: ApplicationData(self: IAzAuthorizationStore) = value
        """
        ...

    @property
    def ApplicationGroups(self) -> IAzApplicationGroups:
        """ Get: ApplicationGroups(self: IAzAuthorizationStore) -> IAzApplicationGroups """
        ...

    @property
    def Applications(self) -> IAzApplications:
        """ Get: Applications(self: IAzAuthorizationStore) -> IAzApplications """
        ...

    @property
    def ApplyStoreSacl(self) -> int:
        """
        Get: ApplyStoreSacl(self: IAzAuthorizationStore) -> int
        Set: ApplyStoreSacl(self: IAzAuthorizationStore) = value
        """
        ...

    @property
    def DelegatedPolicyUsers(self) -> object:
        """ Get: DelegatedPolicyUsers(self: IAzAuthorizationStore) -> object """
        ...

    @property
    def DelegatedPolicyUsersName(self) -> object:
        """ Get: DelegatedPolicyUsersName(self: IAzAuthorizationStore) -> object """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: IAzAuthorizationStore) -> str
        Set: Description(self: IAzAuthorizationStore) = value
        """
        ...

    @property
    def DomainTimeout(self) -> int:
        """
        Get: DomainTimeout(self: IAzAuthorizationStore) -> int
        Set: DomainTimeout(self: IAzAuthorizationStore) = value
        """
        ...

    @property
    def GenerateAudits(self) -> int:
        """
        Get: GenerateAudits(self: IAzAuthorizationStore) -> int
        Set: GenerateAudits(self: IAzAuthorizationStore) = value
        """
        ...

    @property
    def MaxScriptEngines(self) -> int:
        """
        Get: MaxScriptEngines(self: IAzAuthorizationStore) -> int
        Set: MaxScriptEngines(self: IAzAuthorizationStore) = value
        """
        ...

    @property
    def PolicyAdministrators(self) -> object:
        """ Get: PolicyAdministrators(self: IAzAuthorizationStore) -> object """
        ...

    @property
    def PolicyAdministratorsName(self) -> object:
        """ Get: PolicyAdministratorsName(self: IAzAuthorizationStore) -> object """
        ...

    @property
    def PolicyReaders(self) -> object:
        """ Get: PolicyReaders(self: IAzAuthorizationStore) -> object """
        ...

    @property
    def PolicyReadersName(self) -> object:
        """ Get: PolicyReadersName(self: IAzAuthorizationStore) -> object """
        ...

    @property
    def ScriptEngineTimeout(self) -> int:
        """
        Get: ScriptEngineTimeout(self: IAzAuthorizationStore) -> int
        Set: ScriptEngineTimeout(self: IAzAuthorizationStore) = value
        """
        ...

    @property
    def TargetMachine(self) -> str:
        """ Get: TargetMachine(self: IAzAuthorizationStore) -> str """
        ...

    @property
    def Writable(self) -> int:
        """ Get: Writable(self: IAzAuthorizationStore) -> int """
        ...


    def AddDelegatedPolicyUser(self, bstrDelegatedPolicyUser:str, varReserved:object): # -> 
        """ AddDelegatedPolicyUser(self: IAzAuthorizationStore, bstrDelegatedPolicyUser: str, varReserved: object) """
        ...

    def AddDelegatedPolicyUserName(self, bstrDelegatedPolicyUser:str, varReserved:object): # -> 
        """ AddDelegatedPolicyUserName(self: IAzAuthorizationStore, bstrDelegatedPolicyUser: str, varReserved: object) """
        ...

    def AddPolicyAdministrator(self, bstrAdmin:str, varReserved:object): # -> 
        """ AddPolicyAdministrator(self: IAzAuthorizationStore, bstrAdmin: str, varReserved: object) """
        ...

    def AddPolicyAdministratorName(self, bstrAdmin:str, varReserved:object): # -> 
        """ AddPolicyAdministratorName(self: IAzAuthorizationStore, bstrAdmin: str, varReserved: object) """
        ...

    def AddPolicyReader(self, bstrReader:str, varReserved:object): # -> 
        """ AddPolicyReader(self: IAzAuthorizationStore, bstrReader: str, varReserved: object) """
        ...

    def AddPolicyReaderName(self, bstrReader:str, varReserved:object): # -> 
        """ AddPolicyReaderName(self: IAzAuthorizationStore, bstrReader: str, varReserved: object) """
        ...

    def AddPropertyItem(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ AddPropertyItem(self: IAzAuthorizationStore, lPropId: int, varProp: object, varReserved: object) """
        ...

    def CloseApplication(self, bstrApplicationName:str, lFlag:int): # -> 
        """ CloseApplication(self: IAzAuthorizationStore, bstrApplicationName: str, lFlag: int) """
        ...

    def CreateApplication(self, bstrApplicationName:str, varReserved:object) -> IAzApplication:
        """ CreateApplication(self: IAzAuthorizationStore, bstrApplicationName: str, varReserved: object) -> IAzApplication """
        ...

    def CreateApplicationGroup(self, bstrGroupName:str, varReserved:object) -> IAzApplicationGroup:
        """ CreateApplicationGroup(self: IAzAuthorizationStore, bstrGroupName: str, varReserved: object) -> IAzApplicationGroup """
        ...

    def Delete(self, varReserved:object): # -> 
        """ Delete(self: IAzAuthorizationStore, varReserved: object) """
        ...

    def DeleteApplication(self, bstrApplicationName:str, varReserved:object): # -> 
        """ DeleteApplication(self: IAzAuthorizationStore, bstrApplicationName: str, varReserved: object) """
        ...

    def DeleteApplicationGroup(self, bstrGroupName:str, varReserved:object): # -> 
        """ DeleteApplicationGroup(self: IAzAuthorizationStore, bstrGroupName: str, varReserved: object) """
        ...

    def DeleteDelegatedPolicyUser(self, bstrDelegatedPolicyUser:str, varReserved:object): # -> 
        """ DeleteDelegatedPolicyUser(self: IAzAuthorizationStore, bstrDelegatedPolicyUser: str, varReserved: object) """
        ...

    def DeleteDelegatedPolicyUserName(self, bstrDelegatedPolicyUser:str, varReserved:object): # -> 
        """ DeleteDelegatedPolicyUserName(self: IAzAuthorizationStore, bstrDelegatedPolicyUser: str, varReserved: object) """
        ...

    def DeletePolicyAdministrator(self, bstrAdmin:str, varReserved:object): # -> 
        """ DeletePolicyAdministrator(self: IAzAuthorizationStore, bstrAdmin: str, varReserved: object) """
        ...

    def DeletePolicyAdministratorName(self, bstrAdmin:str, varReserved:object): # -> 
        """ DeletePolicyAdministratorName(self: IAzAuthorizationStore, bstrAdmin: str, varReserved: object) """
        ...

    def DeletePolicyReader(self, bstrReader:str, varReserved:object): # -> 
        """ DeletePolicyReader(self: IAzAuthorizationStore, bstrReader: str, varReserved: object) """
        ...

    def DeletePolicyReaderName(self, bstrReader:str, varReserved:object): # -> 
        """ DeletePolicyReaderName(self: IAzAuthorizationStore, bstrReader: str, varReserved: object) """
        ...

    def DeletePropertyItem(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ DeletePropertyItem(self: IAzAuthorizationStore, lPropId: int, varProp: object, varReserved: object) """
        ...

    def GetProperty(self, lPropId:int, varReserved:object) -> object:
        """ GetProperty(self: IAzAuthorizationStore, lPropId: int, varReserved: object) -> object """
        ...

    def Initialize(self, lFlags:int, bstrPolicyURL:str, varReserved:object): # -> 
        """ Initialize(self: IAzAuthorizationStore, lFlags: int, bstrPolicyURL: str, varReserved: object) """
        ...

    def OpenApplication(self, bstrApplicationName:str, varReserved:object) -> IAzApplication:
        """ OpenApplication(self: IAzAuthorizationStore, bstrApplicationName: str, varReserved: object) -> IAzApplication """
        ...

    def OpenApplicationGroup(self, bstrGroupName:str, varReserved:object) -> IAzApplicationGroup:
        """ OpenApplicationGroup(self: IAzAuthorizationStore, bstrGroupName: str, varReserved: object) -> IAzApplicationGroup """
        ...

    def SetProperty(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ SetProperty(self: IAzAuthorizationStore, lPropId: int, varProp: object, varReserved: object) """
        ...

    def Submit(self, lFlags:int, varReserved:object): # -> 
        """ Submit(self: IAzAuthorizationStore, lFlags: int, varReserved: object) """
        ...

    def UpdateCache(self, varReserved:object): # -> 
        """ UpdateCache(self: IAzAuthorizationStore, varReserved: object) """
        ...


class AzAuthorizationStore(IAzAuthorizationStore): # skipped bases: <type 'object'>
    """ no doc """
    pass

class AzAuthorizationStoreClass(IAzAuthorizationStore3, __ComObject, AzAuthorizationStore): # skipped bases: <type 'IAzAuthorizationStore2'>, <type 'IAzAuthorizationStore'>, <type 'object'>
    """ AzAuthorizationStoreClass() """
    @property
    def IAzAuthorizationStore2_ApplicationData(self) -> str:
        """
        Get: IAzAuthorizationStore2_ApplicationData(self: AzAuthorizationStoreClass) -> str
        Set: IAzAuthorizationStore2_ApplicationData(self: AzAuthorizationStoreClass) = value
        """
        ...

    @property
    def IAzAuthorizationStore2_ApplicationGroups(self) -> IAzApplicationGroups:
        """ Get: IAzAuthorizationStore2_ApplicationGroups(self: AzAuthorizationStoreClass) -> IAzApplicationGroups """
        ...

    @property
    def IAzAuthorizationStore2_Applications(self) -> IAzApplications:
        """ Get: IAzAuthorizationStore2_Applications(self: AzAuthorizationStoreClass) -> IAzApplications """
        ...

    @property
    def IAzAuthorizationStore2_ApplyStoreSacl(self) -> int:
        """
        Get: IAzAuthorizationStore2_ApplyStoreSacl(self: AzAuthorizationStoreClass) -> int
        Set: IAzAuthorizationStore2_ApplyStoreSacl(self: AzAuthorizationStoreClass) = value
        """
        ...

    @property
    def IAzAuthorizationStore2_DelegatedPolicyUsers(self) -> object:
        """ Get: IAzAuthorizationStore2_DelegatedPolicyUsers(self: AzAuthorizationStoreClass) -> object """
        ...

    @property
    def IAzAuthorizationStore2_DelegatedPolicyUsersName(self) -> object:
        """ Get: IAzAuthorizationStore2_DelegatedPolicyUsersName(self: AzAuthorizationStoreClass) -> object """
        ...

    @property
    def IAzAuthorizationStore2_Description(self) -> str:
        """
        Get: IAzAuthorizationStore2_Description(self: AzAuthorizationStoreClass) -> str
        Set: IAzAuthorizationStore2_Description(self: AzAuthorizationStoreClass) = value
        """
        ...

    @property
    def IAzAuthorizationStore2_DomainTimeout(self) -> int:
        """
        Get: IAzAuthorizationStore2_DomainTimeout(self: AzAuthorizationStoreClass) -> int
        Set: IAzAuthorizationStore2_DomainTimeout(self: AzAuthorizationStoreClass) = value
        """
        ...

    @property
    def IAzAuthorizationStore2_GenerateAudits(self) -> int:
        """
        Get: IAzAuthorizationStore2_GenerateAudits(self: AzAuthorizationStoreClass) -> int
        Set: IAzAuthorizationStore2_GenerateAudits(self: AzAuthorizationStoreClass) = value
        """
        ...

    @property
    def IAzAuthorizationStore2_MaxScriptEngines(self) -> int:
        """
        Get: IAzAuthorizationStore2_MaxScriptEngines(self: AzAuthorizationStoreClass) -> int
        Set: IAzAuthorizationStore2_MaxScriptEngines(self: AzAuthorizationStoreClass) = value
        """
        ...

    @property
    def IAzAuthorizationStore2_PolicyAdministrators(self) -> object:
        """ Get: IAzAuthorizationStore2_PolicyAdministrators(self: AzAuthorizationStoreClass) -> object """
        ...

    @property
    def IAzAuthorizationStore2_PolicyAdministratorsName(self) -> object:
        """ Get: IAzAuthorizationStore2_PolicyAdministratorsName(self: AzAuthorizationStoreClass) -> object """
        ...

    @property
    def IAzAuthorizationStore2_PolicyReaders(self) -> object:
        """ Get: IAzAuthorizationStore2_PolicyReaders(self: AzAuthorizationStoreClass) -> object """
        ...

    @property
    def IAzAuthorizationStore2_PolicyReadersName(self) -> object:
        """ Get: IAzAuthorizationStore2_PolicyReadersName(self: AzAuthorizationStoreClass) -> object """
        ...

    @property
    def IAzAuthorizationStore2_ScriptEngineTimeout(self) -> int:
        """
        Get: IAzAuthorizationStore2_ScriptEngineTimeout(self: AzAuthorizationStoreClass) -> int
        Set: IAzAuthorizationStore2_ScriptEngineTimeout(self: AzAuthorizationStoreClass) = value
        """
        ...

    @property
    def IAzAuthorizationStore2_TargetMachine(self) -> str:
        """ Get: IAzAuthorizationStore2_TargetMachine(self: AzAuthorizationStoreClass) -> str """
        ...

    @property
    def IAzAuthorizationStore2_Writable(self) -> int:
        """ Get: IAzAuthorizationStore2_Writable(self: AzAuthorizationStoreClass) -> int """
        ...

    @property
    def IAzAuthorizationStore3_ApplicationData(self) -> str:
        """
        Get: IAzAuthorizationStore3_ApplicationData(self: AzAuthorizationStoreClass) -> str
        Set: IAzAuthorizationStore3_ApplicationData(self: AzAuthorizationStoreClass) = value
        """
        ...

    @property
    def IAzAuthorizationStore3_ApplicationGroups(self) -> IAzApplicationGroups:
        """ Get: IAzAuthorizationStore3_ApplicationGroups(self: AzAuthorizationStoreClass) -> IAzApplicationGroups """
        ...

    @property
    def IAzAuthorizationStore3_Applications(self) -> IAzApplications:
        """ Get: IAzAuthorizationStore3_Applications(self: AzAuthorizationStoreClass) -> IAzApplications """
        ...

    @property
    def IAzAuthorizationStore3_ApplyStoreSacl(self) -> int:
        """
        Get: IAzAuthorizationStore3_ApplyStoreSacl(self: AzAuthorizationStoreClass) -> int
        Set: IAzAuthorizationStore3_ApplyStoreSacl(self: AzAuthorizationStoreClass) = value
        """
        ...

    @property
    def IAzAuthorizationStore3_DelegatedPolicyUsers(self) -> object:
        """ Get: IAzAuthorizationStore3_DelegatedPolicyUsers(self: AzAuthorizationStoreClass) -> object """
        ...

    @property
    def IAzAuthorizationStore3_DelegatedPolicyUsersName(self) -> object:
        """ Get: IAzAuthorizationStore3_DelegatedPolicyUsersName(self: AzAuthorizationStoreClass) -> object """
        ...

    @property
    def IAzAuthorizationStore3_Description(self) -> str:
        """
        Get: IAzAuthorizationStore3_Description(self: AzAuthorizationStoreClass) -> str
        Set: IAzAuthorizationStore3_Description(self: AzAuthorizationStoreClass) = value
        """
        ...

    @property
    def IAzAuthorizationStore3_DomainTimeout(self) -> int:
        """
        Get: IAzAuthorizationStore3_DomainTimeout(self: AzAuthorizationStoreClass) -> int
        Set: IAzAuthorizationStore3_DomainTimeout(self: AzAuthorizationStoreClass) = value
        """
        ...

    @property
    def IAzAuthorizationStore3_GenerateAudits(self) -> int:
        """
        Get: IAzAuthorizationStore3_GenerateAudits(self: AzAuthorizationStoreClass) -> int
        Set: IAzAuthorizationStore3_GenerateAudits(self: AzAuthorizationStoreClass) = value
        """
        ...

    @property
    def IAzAuthorizationStore3_MaxScriptEngines(self) -> int:
        """
        Get: IAzAuthorizationStore3_MaxScriptEngines(self: AzAuthorizationStoreClass) -> int
        Set: IAzAuthorizationStore3_MaxScriptEngines(self: AzAuthorizationStoreClass) = value
        """
        ...

    @property
    def IAzAuthorizationStore3_PolicyAdministrators(self) -> object:
        """ Get: IAzAuthorizationStore3_PolicyAdministrators(self: AzAuthorizationStoreClass) -> object """
        ...

    @property
    def IAzAuthorizationStore3_PolicyAdministratorsName(self) -> object:
        """ Get: IAzAuthorizationStore3_PolicyAdministratorsName(self: AzAuthorizationStoreClass) -> object """
        ...

    @property
    def IAzAuthorizationStore3_PolicyReaders(self) -> object:
        """ Get: IAzAuthorizationStore3_PolicyReaders(self: AzAuthorizationStoreClass) -> object """
        ...

    @property
    def IAzAuthorizationStore3_PolicyReadersName(self) -> object:
        """ Get: IAzAuthorizationStore3_PolicyReadersName(self: AzAuthorizationStoreClass) -> object """
        ...

    @property
    def IAzAuthorizationStore3_ScriptEngineTimeout(self) -> int:
        """
        Get: IAzAuthorizationStore3_ScriptEngineTimeout(self: AzAuthorizationStoreClass) -> int
        Set: IAzAuthorizationStore3_ScriptEngineTimeout(self: AzAuthorizationStoreClass) = value
        """
        ...

    @property
    def IAzAuthorizationStore3_TargetMachine(self) -> str:
        """ Get: IAzAuthorizationStore3_TargetMachine(self: AzAuthorizationStoreClass) -> str """
        ...

    @property
    def IAzAuthorizationStore3_Writable(self) -> int:
        """ Get: IAzAuthorizationStore3_Writable(self: AzAuthorizationStoreClass) -> int """
        ...


    def IAzAuthorizationStore2_AddDelegatedPolicyUser(self, bstrDelegatedPolicyUser:str, varReserved:object): # -> 
        """ IAzAuthorizationStore2_AddDelegatedPolicyUser(self: AzAuthorizationStoreClass, bstrDelegatedPolicyUser: str, varReserved: object) """
        ...

    def IAzAuthorizationStore2_AddDelegatedPolicyUserName(self, bstrDelegatedPolicyUser:str, varReserved:object): # -> 
        """ IAzAuthorizationStore2_AddDelegatedPolicyUserName(self: AzAuthorizationStoreClass, bstrDelegatedPolicyUser: str, varReserved: object) """
        ...

    def IAzAuthorizationStore2_AddPolicyAdministrator(self, bstrAdmin:str, varReserved:object): # -> 
        """ IAzAuthorizationStore2_AddPolicyAdministrator(self: AzAuthorizationStoreClass, bstrAdmin: str, varReserved: object) """
        ...

    def IAzAuthorizationStore2_AddPolicyAdministratorName(self, bstrAdmin:str, varReserved:object): # -> 
        """ IAzAuthorizationStore2_AddPolicyAdministratorName(self: AzAuthorizationStoreClass, bstrAdmin: str, varReserved: object) """
        ...

    def IAzAuthorizationStore2_AddPolicyReader(self, bstrReader:str, varReserved:object): # -> 
        """ IAzAuthorizationStore2_AddPolicyReader(self: AzAuthorizationStoreClass, bstrReader: str, varReserved: object) """
        ...

    def IAzAuthorizationStore2_AddPolicyReaderName(self, bstrReader:str, varReserved:object): # -> 
        """ IAzAuthorizationStore2_AddPolicyReaderName(self: AzAuthorizationStoreClass, bstrReader: str, varReserved: object) """
        ...

    def IAzAuthorizationStore2_AddPropertyItem(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ IAzAuthorizationStore2_AddPropertyItem(self: AzAuthorizationStoreClass, lPropId: int, varProp: object, varReserved: object) """
        ...

    def IAzAuthorizationStore2_CloseApplication(self, bstrApplicationName:str, lFlag:int): # -> 
        """ IAzAuthorizationStore2_CloseApplication(self: AzAuthorizationStoreClass, bstrApplicationName: str, lFlag: int) """
        ...

    def IAzAuthorizationStore2_CreateApplication(self, bstrApplicationName:str, varReserved:object) -> IAzApplication:
        """ IAzAuthorizationStore2_CreateApplication(self: AzAuthorizationStoreClass, bstrApplicationName: str, varReserved: object) -> IAzApplication """
        ...

    def IAzAuthorizationStore2_CreateApplicationGroup(self, bstrGroupName:str, varReserved:object) -> IAzApplicationGroup:
        """ IAzAuthorizationStore2_CreateApplicationGroup(self: AzAuthorizationStoreClass, bstrGroupName: str, varReserved: object) -> IAzApplicationGroup """
        ...

    def IAzAuthorizationStore2_Delete(self, varReserved:object): # -> 
        """ IAzAuthorizationStore2_Delete(self: AzAuthorizationStoreClass, varReserved: object) """
        ...

    def IAzAuthorizationStore2_DeleteApplication(self, bstrApplicationName:str, varReserved:object): # -> 
        """ IAzAuthorizationStore2_DeleteApplication(self: AzAuthorizationStoreClass, bstrApplicationName: str, varReserved: object) """
        ...

    def IAzAuthorizationStore2_DeleteApplicationGroup(self, bstrGroupName:str, varReserved:object): # -> 
        """ IAzAuthorizationStore2_DeleteApplicationGroup(self: AzAuthorizationStoreClass, bstrGroupName: str, varReserved: object) """
        ...

    def IAzAuthorizationStore2_DeleteDelegatedPolicyUser(self, bstrDelegatedPolicyUser:str, varReserved:object): # -> 
        """ IAzAuthorizationStore2_DeleteDelegatedPolicyUser(self: AzAuthorizationStoreClass, bstrDelegatedPolicyUser: str, varReserved: object) """
        ...

    def IAzAuthorizationStore2_DeleteDelegatedPolicyUserName(self, bstrDelegatedPolicyUser:str, varReserved:object): # -> 
        """ IAzAuthorizationStore2_DeleteDelegatedPolicyUserName(self: AzAuthorizationStoreClass, bstrDelegatedPolicyUser: str, varReserved: object) """
        ...

    def IAzAuthorizationStore2_DeletePolicyAdministrator(self, bstrAdmin:str, varReserved:object): # -> 
        """ IAzAuthorizationStore2_DeletePolicyAdministrator(self: AzAuthorizationStoreClass, bstrAdmin: str, varReserved: object) """
        ...

    def IAzAuthorizationStore2_DeletePolicyAdministratorName(self, bstrAdmin:str, varReserved:object): # -> 
        """ IAzAuthorizationStore2_DeletePolicyAdministratorName(self: AzAuthorizationStoreClass, bstrAdmin: str, varReserved: object) """
        ...

    def IAzAuthorizationStore2_DeletePolicyReader(self, bstrReader:str, varReserved:object): # -> 
        """ IAzAuthorizationStore2_DeletePolicyReader(self: AzAuthorizationStoreClass, bstrReader: str, varReserved: object) """
        ...

    def IAzAuthorizationStore2_DeletePolicyReaderName(self, bstrReader:str, varReserved:object): # -> 
        """ IAzAuthorizationStore2_DeletePolicyReaderName(self: AzAuthorizationStoreClass, bstrReader: str, varReserved: object) """
        ...

    def IAzAuthorizationStore2_DeletePropertyItem(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ IAzAuthorizationStore2_DeletePropertyItem(self: AzAuthorizationStoreClass, lPropId: int, varProp: object, varReserved: object) """
        ...

    def IAzAuthorizationStore2_GetProperty(self, lPropId:int, varReserved:object) -> object:
        """ IAzAuthorizationStore2_GetProperty(self: AzAuthorizationStoreClass, lPropId: int, varReserved: object) -> object """
        ...

    def IAzAuthorizationStore2_Initialize(self, lFlags:int, bstrPolicyURL:str, varReserved:object): # -> 
        """ IAzAuthorizationStore2_Initialize(self: AzAuthorizationStoreClass, lFlags: int, bstrPolicyURL: str, varReserved: object) """
        ...

    def IAzAuthorizationStore2_OpenApplication(self, bstrApplicationName:str, varReserved:object) -> IAzApplication:
        """ IAzAuthorizationStore2_OpenApplication(self: AzAuthorizationStoreClass, bstrApplicationName: str, varReserved: object) -> IAzApplication """
        ...

    def IAzAuthorizationStore2_OpenApplicationGroup(self, bstrGroupName:str, varReserved:object) -> IAzApplicationGroup:
        """ IAzAuthorizationStore2_OpenApplicationGroup(self: AzAuthorizationStoreClass, bstrGroupName: str, varReserved: object) -> IAzApplicationGroup """
        ...

    def IAzAuthorizationStore2_SetProperty(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ IAzAuthorizationStore2_SetProperty(self: AzAuthorizationStoreClass, lPropId: int, varProp: object, varReserved: object) """
        ...

    def IAzAuthorizationStore2_Submit(self, lFlags:int, varReserved:object): # -> 
        """ IAzAuthorizationStore2_Submit(self: AzAuthorizationStoreClass, lFlags: int, varReserved: object) """
        ...

    def IAzAuthorizationStore2_UpdateCache(self, varReserved:object): # -> 
        """ IAzAuthorizationStore2_UpdateCache(self: AzAuthorizationStoreClass, varReserved: object) """
        ...

    def IAzAuthorizationStore3_AddDelegatedPolicyUser(self, bstrDelegatedPolicyUser:str, varReserved:object): # -> 
        """ IAzAuthorizationStore3_AddDelegatedPolicyUser(self: AzAuthorizationStoreClass, bstrDelegatedPolicyUser: str, varReserved: object) """
        ...

    def IAzAuthorizationStore3_AddDelegatedPolicyUserName(self, bstrDelegatedPolicyUser:str, varReserved:object): # -> 
        """ IAzAuthorizationStore3_AddDelegatedPolicyUserName(self: AzAuthorizationStoreClass, bstrDelegatedPolicyUser: str, varReserved: object) """
        ...

    def IAzAuthorizationStore3_AddPolicyAdministrator(self, bstrAdmin:str, varReserved:object): # -> 
        """ IAzAuthorizationStore3_AddPolicyAdministrator(self: AzAuthorizationStoreClass, bstrAdmin: str, varReserved: object) """
        ...

    def IAzAuthorizationStore3_AddPolicyAdministratorName(self, bstrAdmin:str, varReserved:object): # -> 
        """ IAzAuthorizationStore3_AddPolicyAdministratorName(self: AzAuthorizationStoreClass, bstrAdmin: str, varReserved: object) """
        ...

    def IAzAuthorizationStore3_AddPolicyReader(self, bstrReader:str, varReserved:object): # -> 
        """ IAzAuthorizationStore3_AddPolicyReader(self: AzAuthorizationStoreClass, bstrReader: str, varReserved: object) """
        ...

    def IAzAuthorizationStore3_AddPolicyReaderName(self, bstrReader:str, varReserved:object): # -> 
        """ IAzAuthorizationStore3_AddPolicyReaderName(self: AzAuthorizationStoreClass, bstrReader: str, varReserved: object) """
        ...

    def IAzAuthorizationStore3_AddPropertyItem(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ IAzAuthorizationStore3_AddPropertyItem(self: AzAuthorizationStoreClass, lPropId: int, varProp: object, varReserved: object) """
        ...

    def IAzAuthorizationStore3_CloseApplication(self, bstrApplicationName:str, lFlag:int): # -> 
        """ IAzAuthorizationStore3_CloseApplication(self: AzAuthorizationStoreClass, bstrApplicationName: str, lFlag: int) """
        ...

    def IAzAuthorizationStore3_CreateApplication(self, bstrApplicationName:str, varReserved:object) -> IAzApplication:
        """ IAzAuthorizationStore3_CreateApplication(self: AzAuthorizationStoreClass, bstrApplicationName: str, varReserved: object) -> IAzApplication """
        ...

    def IAzAuthorizationStore3_CreateApplication2(self, bstrApplicationName:str, varReserved:object) -> IAzApplication2:
        """ IAzAuthorizationStore3_CreateApplication2(self: AzAuthorizationStoreClass, bstrApplicationName: str, varReserved: object) -> IAzApplication2 """
        ...

    def IAzAuthorizationStore3_CreateApplicationGroup(self, bstrGroupName:str, varReserved:object) -> IAzApplicationGroup:
        """ IAzAuthorizationStore3_CreateApplicationGroup(self: AzAuthorizationStoreClass, bstrGroupName: str, varReserved: object) -> IAzApplicationGroup """
        ...

    def IAzAuthorizationStore3_Delete(self, varReserved:object): # -> 
        """ IAzAuthorizationStore3_Delete(self: AzAuthorizationStoreClass, varReserved: object) """
        ...

    def IAzAuthorizationStore3_DeleteApplication(self, bstrApplicationName:str, varReserved:object): # -> 
        """ IAzAuthorizationStore3_DeleteApplication(self: AzAuthorizationStoreClass, bstrApplicationName: str, varReserved: object) """
        ...

    def IAzAuthorizationStore3_DeleteApplicationGroup(self, bstrGroupName:str, varReserved:object): # -> 
        """ IAzAuthorizationStore3_DeleteApplicationGroup(self: AzAuthorizationStoreClass, bstrGroupName: str, varReserved: object) """
        ...

    def IAzAuthorizationStore3_DeleteDelegatedPolicyUser(self, bstrDelegatedPolicyUser:str, varReserved:object): # -> 
        """ IAzAuthorizationStore3_DeleteDelegatedPolicyUser(self: AzAuthorizationStoreClass, bstrDelegatedPolicyUser: str, varReserved: object) """
        ...

    def IAzAuthorizationStore3_DeleteDelegatedPolicyUserName(self, bstrDelegatedPolicyUser:str, varReserved:object): # -> 
        """ IAzAuthorizationStore3_DeleteDelegatedPolicyUserName(self: AzAuthorizationStoreClass, bstrDelegatedPolicyUser: str, varReserved: object) """
        ...

    def IAzAuthorizationStore3_DeletePolicyAdministrator(self, bstrAdmin:str, varReserved:object): # -> 
        """ IAzAuthorizationStore3_DeletePolicyAdministrator(self: AzAuthorizationStoreClass, bstrAdmin: str, varReserved: object) """
        ...

    def IAzAuthorizationStore3_DeletePolicyAdministratorName(self, bstrAdmin:str, varReserved:object): # -> 
        """ IAzAuthorizationStore3_DeletePolicyAdministratorName(self: AzAuthorizationStoreClass, bstrAdmin: str, varReserved: object) """
        ...

    def IAzAuthorizationStore3_DeletePolicyReader(self, bstrReader:str, varReserved:object): # -> 
        """ IAzAuthorizationStore3_DeletePolicyReader(self: AzAuthorizationStoreClass, bstrReader: str, varReserved: object) """
        ...

    def IAzAuthorizationStore3_DeletePolicyReaderName(self, bstrReader:str, varReserved:object): # -> 
        """ IAzAuthorizationStore3_DeletePolicyReaderName(self: AzAuthorizationStoreClass, bstrReader: str, varReserved: object) """
        ...

    def IAzAuthorizationStore3_DeletePropertyItem(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ IAzAuthorizationStore3_DeletePropertyItem(self: AzAuthorizationStoreClass, lPropId: int, varProp: object, varReserved: object) """
        ...

    def IAzAuthorizationStore3_GetProperty(self, lPropId:int, varReserved:object) -> object:
        """ IAzAuthorizationStore3_GetProperty(self: AzAuthorizationStoreClass, lPropId: int, varReserved: object) -> object """
        ...

    def IAzAuthorizationStore3_Initialize(self, lFlags:int, bstrPolicyURL:str, varReserved:object): # -> 
        """ IAzAuthorizationStore3_Initialize(self: AzAuthorizationStoreClass, lFlags: int, bstrPolicyURL: str, varReserved: object) """
        ...

    def IAzAuthorizationStore3_OpenApplication(self, bstrApplicationName:str, varReserved:object) -> IAzApplication:
        """ IAzAuthorizationStore3_OpenApplication(self: AzAuthorizationStoreClass, bstrApplicationName: str, varReserved: object) -> IAzApplication """
        ...

    def IAzAuthorizationStore3_OpenApplication2(self, bstrApplicationName:str, varReserved:object) -> IAzApplication2:
        """ IAzAuthorizationStore3_OpenApplication2(self: AzAuthorizationStoreClass, bstrApplicationName: str, varReserved: object) -> IAzApplication2 """
        ...

    def IAzAuthorizationStore3_OpenApplicationGroup(self, bstrGroupName:str, varReserved:object) -> IAzApplicationGroup:
        """ IAzAuthorizationStore3_OpenApplicationGroup(self: AzAuthorizationStoreClass, bstrGroupName: str, varReserved: object) -> IAzApplicationGroup """
        ...

    def IAzAuthorizationStore3_SetProperty(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ IAzAuthorizationStore3_SetProperty(self: AzAuthorizationStoreClass, lPropId: int, varProp: object, varReserved: object) """
        ...

    def IAzAuthorizationStore3_Submit(self, lFlags:int, varReserved:object): # -> 
        """ IAzAuthorizationStore3_Submit(self: AzAuthorizationStoreClass, lFlags: int, varReserved: object) """
        ...

    def IAzAuthorizationStore3_UpdateCache(self, varReserved:object): # -> 
        """ IAzAuthorizationStore3_UpdateCache(self: AzAuthorizationStoreClass, varReserved: object) """
        ...


class IAzBizRuleContext: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BusinessRuleResult(self): # -> 
        """ Set: BusinessRuleResult(self: IAzBizRuleContext) = value """
        ...

    @property
    def BusinessRuleString(self) -> str:
        """
        Get: BusinessRuleString(self: IAzBizRuleContext) -> str
        Set: BusinessRuleString(self: IAzBizRuleContext) = value
        """
        ...


    def GetParameter(self, bstrParameterName:str) -> object:
        """ GetParameter(self: IAzBizRuleContext, bstrParameterName: str) -> object """
        ...


class AzBizRuleContext(IAzBizRuleContext): # skipped bases: <type 'object'>
    """ no doc """
    pass

class AzBizRuleContextClass(AzBizRuleContext, __ComObject): # skipped bases: <type 'IAzBizRuleContext'>, <type 'object'>
    """ AzBizRuleContextClass() """
    @property
    def BusinessRuleResult(self): # -> 
        """ Set: BusinessRuleResult(self: AzBizRuleContextClass) = value """
        ...

    @property
    def BusinessRuleString(self) -> str:
        """
        Get: BusinessRuleString(self: AzBizRuleContextClass) -> str
        Set: BusinessRuleString(self: AzBizRuleContextClass) = value
        """
        ...


    def GetParameter(self, bstrParameterName:str) -> object:
        """ GetParameter(self: AzBizRuleContextClass, bstrParameterName: str) -> object """
        ...


class IAzPrincipalLocator: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def NameResolver(self) -> IAzNameResolver:
        """ Get: NameResolver(self: IAzPrincipalLocator) -> IAzNameResolver """
        ...

    @property
    def ObjectPicker(self) -> IAzObjectPicker:
        """ Get: ObjectPicker(self: IAzPrincipalLocator) -> IAzObjectPicker """
        ...



class AzPrincipalLocator(IAzPrincipalLocator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class AzPrincipalLocatorClass(AzPrincipalLocator, __ComObject): # skipped bases: <type 'IAzPrincipalLocator'>, <type 'object'>
    """ AzPrincipalLocatorClass() """
    @property
    def NameResolver(self) -> IAzNameResolver:
        """ Get: NameResolver(self: AzPrincipalLocatorClass) -> IAzNameResolver """
        ...

    @property
    def ObjectPicker(self) -> IAzObjectPicker:
        """ Get: ObjectPicker(self: AzPrincipalLocatorClass) -> IAzObjectPicker """
        ...



class IAzApplication: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApplicationData(self) -> str:
        """
        Get: ApplicationData(self: IAzApplication) -> str
        Set: ApplicationData(self: IAzApplication) = value
        """
        ...

    @property
    def ApplicationGroups(self) -> IAzApplicationGroups:
        """ Get: ApplicationGroups(self: IAzApplication) -> IAzApplicationGroups """
        ...

    @property
    def ApplyStoreSacl(self) -> int:
        """
        Get: ApplyStoreSacl(self: IAzApplication) -> int
        Set: ApplyStoreSacl(self: IAzApplication) = value
        """
        ...

    @property
    def AuthzInterfaceClsid(self) -> str:
        """
        Get: AuthzInterfaceClsid(self: IAzApplication) -> str
        Set: AuthzInterfaceClsid(self: IAzApplication) = value
        """
        ...

    @property
    def DelegatedPolicyUsers(self) -> object:
        """ Get: DelegatedPolicyUsers(self: IAzApplication) -> object """
        ...

    @property
    def DelegatedPolicyUsersName(self) -> object:
        """ Get: DelegatedPolicyUsersName(self: IAzApplication) -> object """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: IAzApplication) -> str
        Set: Description(self: IAzApplication) = value
        """
        ...

    @property
    def GenerateAudits(self) -> int:
        """
        Get: GenerateAudits(self: IAzApplication) -> int
        Set: GenerateAudits(self: IAzApplication) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: IAzApplication) -> str
        Set: Name(self: IAzApplication) = value
        """
        ...

    @property
    def Operations(self) -> IAzOperations:
        """ Get: Operations(self: IAzApplication) -> IAzOperations """
        ...

    @property
    def PolicyAdministrators(self) -> object:
        """ Get: PolicyAdministrators(self: IAzApplication) -> object """
        ...

    @property
    def PolicyAdministratorsName(self) -> object:
        """ Get: PolicyAdministratorsName(self: IAzApplication) -> object """
        ...

    @property
    def PolicyReaders(self) -> object:
        """ Get: PolicyReaders(self: IAzApplication) -> object """
        ...

    @property
    def PolicyReadersName(self) -> object:
        """ Get: PolicyReadersName(self: IAzApplication) -> object """
        ...

    @property
    def Roles(self) -> IAzRoles:
        """ Get: Roles(self: IAzApplication) -> IAzRoles """
        ...

    @property
    def Scopes(self) -> IAzScopes:
        """ Get: Scopes(self: IAzApplication) -> IAzScopes """
        ...

    @property
    def Tasks(self) -> IAzTasks:
        """ Get: Tasks(self: IAzApplication) -> IAzTasks """
        ...

    @property
    def Version(self) -> str:
        """
        Get: Version(self: IAzApplication) -> str
        Set: Version(self: IAzApplication) = value
        """
        ...

    @property
    def Writable(self) -> int:
        """ Get: Writable(self: IAzApplication) -> int """
        ...


    def AddDelegatedPolicyUser(self, bstrDelegatedPolicyUser:str, varReserved:object): # -> 
        """ AddDelegatedPolicyUser(self: IAzApplication, bstrDelegatedPolicyUser: str, varReserved: object) """
        ...

    def AddDelegatedPolicyUserName(self, bstrDelegatedPolicyUser:str, varReserved:object): # -> 
        """ AddDelegatedPolicyUserName(self: IAzApplication, bstrDelegatedPolicyUser: str, varReserved: object) """
        ...

    def AddPolicyAdministrator(self, bstrAdmin:str, varReserved:object): # -> 
        """ AddPolicyAdministrator(self: IAzApplication, bstrAdmin: str, varReserved: object) """
        ...

    def AddPolicyAdministratorName(self, bstrAdmin:str, varReserved:object): # -> 
        """ AddPolicyAdministratorName(self: IAzApplication, bstrAdmin: str, varReserved: object) """
        ...

    def AddPolicyReader(self, bstrReader:str, varReserved:object): # -> 
        """ AddPolicyReader(self: IAzApplication, bstrReader: str, varReserved: object) """
        ...

    def AddPolicyReaderName(self, bstrReader:str, varReserved:object): # -> 
        """ AddPolicyReaderName(self: IAzApplication, bstrReader: str, varReserved: object) """
        ...

    def AddPropertyItem(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ AddPropertyItem(self: IAzApplication, lPropId: int, varProp: object, varReserved: object) """
        ...

    def CreateApplicationGroup(self, bstrGroupName:str, varReserved:object) -> IAzApplicationGroup:
        """ CreateApplicationGroup(self: IAzApplication, bstrGroupName: str, varReserved: object) -> IAzApplicationGroup """
        ...

    def CreateOperation(self, bstrOperationName:str, varReserved:object) -> IAzOperation:
        """ CreateOperation(self: IAzApplication, bstrOperationName: str, varReserved: object) -> IAzOperation """
        ...

    def CreateRole(self, bstrRoleName:str, varReserved:object) -> IAzRole:
        """ CreateRole(self: IAzApplication, bstrRoleName: str, varReserved: object) -> IAzRole """
        ...

    def CreateScope(self, bstrScopeName:str, varReserved:object) -> IAzScope:
        """ CreateScope(self: IAzApplication, bstrScopeName: str, varReserved: object) -> IAzScope """
        ...

    def CreateTask(self, bstrTaskName:str, varReserved:object) -> IAzTask:
        """ CreateTask(self: IAzApplication, bstrTaskName: str, varReserved: object) -> IAzTask """
        ...

    def DeleteApplicationGroup(self, bstrGroupName:str, varReserved:object): # -> 
        """ DeleteApplicationGroup(self: IAzApplication, bstrGroupName: str, varReserved: object) """
        ...

    def DeleteDelegatedPolicyUser(self, bstrDelegatedPolicyUser:str, varReserved:object): # -> 
        """ DeleteDelegatedPolicyUser(self: IAzApplication, bstrDelegatedPolicyUser: str, varReserved: object) """
        ...

    def DeleteDelegatedPolicyUserName(self, bstrDelegatedPolicyUser:str, varReserved:object): # -> 
        """ DeleteDelegatedPolicyUserName(self: IAzApplication, bstrDelegatedPolicyUser: str, varReserved: object) """
        ...

    def DeleteOperation(self, bstrOperationName:str, varReserved:object): # -> 
        """ DeleteOperation(self: IAzApplication, bstrOperationName: str, varReserved: object) """
        ...

    def DeletePolicyAdministrator(self, bstrAdmin:str, varReserved:object): # -> 
        """ DeletePolicyAdministrator(self: IAzApplication, bstrAdmin: str, varReserved: object) """
        ...

    def DeletePolicyAdministratorName(self, bstrAdmin:str, varReserved:object): # -> 
        """ DeletePolicyAdministratorName(self: IAzApplication, bstrAdmin: str, varReserved: object) """
        ...

    def DeletePolicyReader(self, bstrReader:str, varReserved:object): # -> 
        """ DeletePolicyReader(self: IAzApplication, bstrReader: str, varReserved: object) """
        ...

    def DeletePolicyReaderName(self, bstrReader:str, varReserved:object): # -> 
        """ DeletePolicyReaderName(self: IAzApplication, bstrReader: str, varReserved: object) """
        ...

    def DeletePropertyItem(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ DeletePropertyItem(self: IAzApplication, lPropId: int, varProp: object, varReserved: object) """
        ...

    def DeleteRole(self, bstrRoleName:str, varReserved:object): # -> 
        """ DeleteRole(self: IAzApplication, bstrRoleName: str, varReserved: object) """
        ...

    def DeleteScope(self, bstrScopeName:str, varReserved:object): # -> 
        """ DeleteScope(self: IAzApplication, bstrScopeName: str, varReserved: object) """
        ...

    def DeleteTask(self, bstrTaskName:str, varReserved:object): # -> 
        """ DeleteTask(self: IAzApplication, bstrTaskName: str, varReserved: object) """
        ...

    def GetProperty(self, lPropId:int, varReserved:object) -> object:
        """ GetProperty(self: IAzApplication, lPropId: int, varReserved: object) -> object """
        ...

    def InitializeClientContextFromName(self, ClientName:str, DomainName:str, varReserved:object) -> IAzClientContext:
        """ InitializeClientContextFromName(self: IAzApplication, ClientName: str, DomainName: str, varReserved: object) -> IAzClientContext """
        ...

    def InitializeClientContextFromStringSid(self, SidString:str, lOptions:int, varReserved:object) -> IAzClientContext:
        """ InitializeClientContextFromStringSid(self: IAzApplication, SidString: str, lOptions: int, varReserved: object) -> IAzClientContext """
        ...

    def InitializeClientContextFromToken(self, ullTokenHandle:UInt64, varReserved:object) -> IAzClientContext:
        """ InitializeClientContextFromToken(self: IAzApplication, ullTokenHandle: UInt64, varReserved: object) -> IAzClientContext """
        ...

    def OpenApplicationGroup(self, bstrGroupName:str, varReserved:object) -> IAzApplicationGroup:
        """ OpenApplicationGroup(self: IAzApplication, bstrGroupName: str, varReserved: object) -> IAzApplicationGroup """
        ...

    def OpenOperation(self, bstrOperationName:str, varReserved:object) -> IAzOperation:
        """ OpenOperation(self: IAzApplication, bstrOperationName: str, varReserved: object) -> IAzOperation """
        ...

    def OpenRole(self, bstrRoleName:str, varReserved:object) -> IAzRole:
        """ OpenRole(self: IAzApplication, bstrRoleName: str, varReserved: object) -> IAzRole """
        ...

    def OpenScope(self, bstrScopeName:str, varReserved:object) -> IAzScope:
        """ OpenScope(self: IAzApplication, bstrScopeName: str, varReserved: object) -> IAzScope """
        ...

    def OpenTask(self, bstrTaskName:str, varReserved:object) -> IAzTask:
        """ OpenTask(self: IAzApplication, bstrTaskName: str, varReserved: object) -> IAzTask """
        ...

    def SetProperty(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ SetProperty(self: IAzApplication, lPropId: int, varProp: object, varReserved: object) """
        ...

    def Submit(self, lFlags:int, varReserved:object): # -> 
        """ Submit(self: IAzApplication, lFlags: int, varReserved: object) """
        ...


class IAzApplication2(IAzApplication): # skipped bases: <type 'object'>
    """ no doc """
    def InitializeClientContext2(self, IdentifyingString:str, varReserved:object) -> IAzClientContext2:
        """ InitializeClientContext2(self: IAzApplication2, IdentifyingString: str, varReserved: object) -> IAzClientContext2 """
        ...

    def InitializeClientContextFromToken2(self, ulTokenHandleLowPart:UInt32, ulTokenHandleHighPart:UInt32, varReserved:object) -> IAzClientContext2:
        """ InitializeClientContextFromToken2(self: IAzApplication2, ulTokenHandleLowPart: UInt32, ulTokenHandleHighPart: UInt32, varReserved: object) -> IAzClientContext2 """
        ...


class IAzApplication3(IAzApplication2): # skipped bases: <type 'IAzApplication'>, <type 'object'>
    """ no doc """
    @property
    def BizRulesEnabled(self) -> bool:
        """
        Get: BizRulesEnabled(self: IAzApplication3) -> bool
        Set: BizRulesEnabled(self: IAzApplication3) = value
        """
        ...

    @property
    def RoleAssignments(self) -> IAzRoleAssignments:
        """ Get: RoleAssignments(self: IAzApplication3) -> IAzRoleAssignments """
        ...

    @property
    def RoleDefinitions(self) -> IAzRoleDefinitions:
        """ Get: RoleDefinitions(self: IAzApplication3) -> IAzRoleDefinitions """
        ...


    def CreateRoleAssignment(self, bstrRoleAssignmentName:str) -> IAzRoleAssignment:
        """ CreateRoleAssignment(self: IAzApplication3, bstrRoleAssignmentName: str) -> IAzRoleAssignment """
        ...

    def CreateRoleDefinition(self, bstrRoleDefinitionName:str) -> IAzRoleDefinition:
        """ CreateRoleDefinition(self: IAzApplication3, bstrRoleDefinitionName: str) -> IAzRoleDefinition """
        ...

    def CreateScope2(self, bstrScopeName:str) -> IAzScope2:
        """ CreateScope2(self: IAzApplication3, bstrScopeName: str) -> IAzScope2 """
        ...

    def DeleteRoleAssignment(self, bstrRoleAssignmentName:str): # -> 
        """ DeleteRoleAssignment(self: IAzApplication3, bstrRoleAssignmentName: str) """
        ...

    def DeleteRoleDefinition(self, bstrRoleDefinitionName:str): # -> 
        """ DeleteRoleDefinition(self: IAzApplication3, bstrRoleDefinitionName: str) """
        ...

    def DeleteScope2(self, bstrScopeName:str): # -> 
        """ DeleteScope2(self: IAzApplication3, bstrScopeName: str) """
        ...

    def OpenRoleAssignment(self, bstrRoleAssignmentName:str) -> IAzRoleAssignment:
        """ OpenRoleAssignment(self: IAzApplication3, bstrRoleAssignmentName: str) -> IAzRoleAssignment """
        ...

    def OpenRoleDefinition(self, bstrRoleDefinitionName:str) -> IAzRoleDefinition:
        """ OpenRoleDefinition(self: IAzApplication3, bstrRoleDefinitionName: str) -> IAzRoleDefinition """
        ...

    def OpenScope2(self, bstrScopeName:str) -> IAzScope2:
        """ OpenScope2(self: IAzApplication3, bstrScopeName: str) -> IAzScope2 """
        ...

    def ScopeExists(self, bstrScopeName:str) -> bool:
        """ ScopeExists(self: IAzApplication3, bstrScopeName: str) -> bool """
        ...


class IAzApplicationGroup: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AppMembers(self) -> object:
        """ Get: AppMembers(self: IAzApplicationGroup) -> object """
        ...

    @property
    def AppNonMembers(self) -> object:
        """ Get: AppNonMembers(self: IAzApplicationGroup) -> object """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: IAzApplicationGroup) -> str
        Set: Description(self: IAzApplicationGroup) = value
        """
        ...

    @property
    def LdapQuery(self) -> str:
        """
        Get: LdapQuery(self: IAzApplicationGroup) -> str
        Set: LdapQuery(self: IAzApplicationGroup) = value
        """
        ...

    @property
    def Members(self) -> object:
        """ Get: Members(self: IAzApplicationGroup) -> object """
        ...

    @property
    def MembersName(self) -> object:
        """ Get: MembersName(self: IAzApplicationGroup) -> object """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: IAzApplicationGroup) -> str
        Set: Name(self: IAzApplicationGroup) = value
        """
        ...

    @property
    def NonMembers(self) -> object:
        """ Get: NonMembers(self: IAzApplicationGroup) -> object """
        ...

    @property
    def NonMembersName(self) -> object:
        """ Get: NonMembersName(self: IAzApplicationGroup) -> object """
        ...

    @property
    def Type(self) -> int:
        """
        Get: Type(self: IAzApplicationGroup) -> int
        Set: Type(self: IAzApplicationGroup) = value
        """
        ...

    @property
    def Writable(self) -> int:
        """ Get: Writable(self: IAzApplicationGroup) -> int """
        ...


    def AddAppMember(self, bstrProp:str, varReserved:object): # -> 
        """ AddAppMember(self: IAzApplicationGroup, bstrProp: str, varReserved: object) """
        ...

    def AddAppNonMember(self, bstrProp:str, varReserved:object): # -> 
        """ AddAppNonMember(self: IAzApplicationGroup, bstrProp: str, varReserved: object) """
        ...

    def AddMember(self, bstrProp:str, varReserved:object): # -> 
        """ AddMember(self: IAzApplicationGroup, bstrProp: str, varReserved: object) """
        ...

    def AddMemberName(self, bstrProp:str, varReserved:object): # -> 
        """ AddMemberName(self: IAzApplicationGroup, bstrProp: str, varReserved: object) """
        ...

    def AddNonMember(self, bstrProp:str, varReserved:object): # -> 
        """ AddNonMember(self: IAzApplicationGroup, bstrProp: str, varReserved: object) """
        ...

    def AddNonMemberName(self, bstrProp:str, varReserved:object): # -> 
        """ AddNonMemberName(self: IAzApplicationGroup, bstrProp: str, varReserved: object) """
        ...

    def AddPropertyItem(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ AddPropertyItem(self: IAzApplicationGroup, lPropId: int, varProp: object, varReserved: object) """
        ...

    def DeleteAppMember(self, bstrProp:str, varReserved:object): # -> 
        """ DeleteAppMember(self: IAzApplicationGroup, bstrProp: str, varReserved: object) """
        ...

    def DeleteAppNonMember(self, bstrProp:str, varReserved:object): # -> 
        """ DeleteAppNonMember(self: IAzApplicationGroup, bstrProp: str, varReserved: object) """
        ...

    def DeleteMember(self, bstrProp:str, varReserved:object): # -> 
        """ DeleteMember(self: IAzApplicationGroup, bstrProp: str, varReserved: object) """
        ...

    def DeleteMemberName(self, bstrProp:str, varReserved:object): # -> 
        """ DeleteMemberName(self: IAzApplicationGroup, bstrProp: str, varReserved: object) """
        ...

    def DeleteNonMember(self, bstrProp:str, varReserved:object): # -> 
        """ DeleteNonMember(self: IAzApplicationGroup, bstrProp: str, varReserved: object) """
        ...

    def DeleteNonMemberName(self, bstrProp:str, varReserved:object): # -> 
        """ DeleteNonMemberName(self: IAzApplicationGroup, bstrProp: str, varReserved: object) """
        ...

    def DeletePropertyItem(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ DeletePropertyItem(self: IAzApplicationGroup, lPropId: int, varProp: object, varReserved: object) """
        ...

    def GetProperty(self, lPropId:int, varReserved:object) -> object:
        """ GetProperty(self: IAzApplicationGroup, lPropId: int, varReserved: object) -> object """
        ...

    def SetProperty(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ SetProperty(self: IAzApplicationGroup, lPropId: int, varProp: object, varReserved: object) """
        ...

    def Submit(self, lFlags:int, varReserved:object): # -> 
        """ Submit(self: IAzApplicationGroup, lFlags: int, varReserved: object) """
        ...


class IAzApplicationGroup2(IAzApplicationGroup): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BizRule(self) -> str:
        """
        Get: BizRule(self: IAzApplicationGroup2) -> str
        Set: BizRule(self: IAzApplicationGroup2) = value
        """
        ...

    @property
    def BizRuleImportedPath(self) -> str:
        """
        Get: BizRuleImportedPath(self: IAzApplicationGroup2) -> str
        Set: BizRuleImportedPath(self: IAzApplicationGroup2) = value
        """
        ...

    @property
    def BizRuleLanguage(self) -> str:
        """
        Get: BizRuleLanguage(self: IAzApplicationGroup2) -> str
        Set: BizRuleLanguage(self: IAzApplicationGroup2) = value
        """
        ...


    def RoleAssignments(self, bstrScopeName:str, bRecursive:bool) -> IAzRoleAssignments:
        """ RoleAssignments(self: IAzApplicationGroup2, bstrScopeName: str, bRecursive: bool) -> IAzRoleAssignments """
        ...


class IAzApplicationGroups(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: IAzApplicationGroups) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IAzApplications(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: IAzApplications) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IAzAuthorizationStore2(IAzAuthorizationStore): # skipped bases: <type 'object'>
    """ no doc """
    def CreateApplication2(self, bstrApplicationName:str, varReserved:object) -> IAzApplication2:
        """ CreateApplication2(self: IAzAuthorizationStore2, bstrApplicationName: str, varReserved: object) -> IAzApplication2 """
        ...

    def OpenApplication2(self, bstrApplicationName:str, varReserved:object) -> IAzApplication2:
        """ OpenApplication2(self: IAzAuthorizationStore2, bstrApplicationName: str, varReserved: object) -> IAzApplication2 """
        ...


class IAzAuthorizationStore3(IAzAuthorizationStore2): # skipped bases: <type 'IAzAuthorizationStore'>, <type 'object'>
    """ no doc """
    def BizruleGroupSupported(self) -> bool:
        """ BizruleGroupSupported(self: IAzAuthorizationStore3) -> bool """
        ...

    def GetSchemaVersion(self, plMajorVersion, plMinorVersion) -> Tuple_[int, int]:
        """ GetSchemaVersion(self: IAzAuthorizationStore3) -> (int, int) """
        ...

    def IsFunctionalLevelUpgradeSupported(self, lFunctionalLevel:int) -> bool:
        """ IsFunctionalLevelUpgradeSupported(self: IAzAuthorizationStore3, lFunctionalLevel: int) -> bool """
        ...

    def IsUpdateNeeded(self) -> bool:
        """ IsUpdateNeeded(self: IAzAuthorizationStore3) -> bool """
        ...

    def UpgradeStoresFunctionalLevel(self, lFunctionalLevel:int): # -> 
        """ UpgradeStoresFunctionalLevel(self: IAzAuthorizationStore3, lFunctionalLevel: int) """
        ...


class IAzBizRuleInterfaces: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> UInt32:
        """ Get: Count(self: IAzBizRuleInterfaces) -> UInt32 """
        ...


    def AddInterface(self, bstrInterfaceName:str, lInterfaceFlag:int, varInterface:object): # -> 
        """ AddInterface(self: IAzBizRuleInterfaces, bstrInterfaceName: str, lInterfaceFlag: int, varInterface: object) """
        ...

    def AddInterfaces(self, varInterfaceNames:object, varInterfaceFlags:object, varInterfaces:object): # -> 
        """ AddInterfaces(self: IAzBizRuleInterfaces, varInterfaceNames: object, varInterfaceFlags: object, varInterfaces: object) """
        ...

    def GetInterfaceValue(self, bstrInterfaceName, lInterfaceFlag, varInterface) -> Tuple_[int, object]:
        """ GetInterfaceValue(self: IAzBizRuleInterfaces, bstrInterfaceName: str) -> (int, object) """
        ...

    def Remove(self, bstrInterfaceName:str): # -> 
        """ Remove(self: IAzBizRuleInterfaces, bstrInterfaceName: str) """
        ...

    def RemoveAll(self): # -> 
        """ RemoveAll(self: IAzBizRuleInterfaces) """
        ...


class IAzBizRuleParameters: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> UInt32:
        """ Get: Count(self: IAzBizRuleParameters) -> UInt32 """
        ...


    def AddParameter(self, bstrParameterName:str, varParameterValue:object): # -> 
        """ AddParameter(self: IAzBizRuleParameters, bstrParameterName: str, varParameterValue: object) """
        ...

    def AddParameters(self, varParameterNames:object, varParameterValues:object): # -> 
        """ AddParameters(self: IAzBizRuleParameters, varParameterNames: object, varParameterValues: object) """
        ...

    def GetParameterValue(self, bstrParameterName:str) -> object:
        """ GetParameterValue(self: IAzBizRuleParameters, bstrParameterName: str) -> object """
        ...

    def Remove(self, varParameterName:str): # -> 
        """ Remove(self: IAzBizRuleParameters, varParameterName: str) """
        ...

    def RemoveAll(self): # -> 
        """ RemoveAll(self: IAzBizRuleParameters) """
        ...


class IAzClientContext: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RoleForAccessCheck(self) -> str:
        """
        Get: RoleForAccessCheck(self: IAzClientContext) -> str
        Set: RoleForAccessCheck(self: IAzClientContext) = value
        """
        ...

    @property
    def UserCanonical(self) -> str:
        """ Get: UserCanonical(self: IAzClientContext) -> str """
        ...

    @property
    def UserDisplay(self) -> str:
        """ Get: UserDisplay(self: IAzClientContext) -> str """
        ...

    @property
    def UserDn(self) -> str:
        """ Get: UserDn(self: IAzClientContext) -> str """
        ...

    @property
    def UserDnsSamCompat(self) -> str:
        """ Get: UserDnsSamCompat(self: IAzClientContext) -> str """
        ...

    @property
    def UserGuid(self) -> str:
        """ Get: UserGuid(self: IAzClientContext) -> str """
        ...

    @property
    def UserSamCompat(self) -> str:
        """ Get: UserSamCompat(self: IAzClientContext) -> str """
        ...

    @property
    def UserUpn(self) -> str:
        """ Get: UserUpn(self: IAzClientContext) -> str """
        ...


    def AccessCheck(self, bstrObjectName:str, varScopeNames:object, varOperations:object, varParameterNames:object, varParameterValues:object, varInterfaceNames:object, varInterfaceFlags:object, varInterfaces:object) -> object:
        """ AccessCheck(self: IAzClientContext, bstrObjectName: str, varScopeNames: object, varOperations: object, varParameterNames: object, varParameterValues: object, varInterfaceNames: object, varInterfaceFlags: object, varInterfaces: object) -> object """
        ...

    def GetBusinessRuleString(self) -> str:
        """ GetBusinessRuleString(self: IAzClientContext) -> str """
        ...

    def GetProperty(self, lPropId:int, varReserved:object) -> object:
        """ GetProperty(self: IAzClientContext, lPropId: int, varReserved: object) -> object """
        ...

    def GetRoles(self, bstrScopeName:str) -> object:
        """ GetRoles(self: IAzClientContext, bstrScopeName: str) -> object """
        ...


class IAzClientContext2(IAzClientContext): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LDAPQueryDN(self) -> str:
        """
        Get: LDAPQueryDN(self: IAzClientContext2) -> str
        Set: LDAPQueryDN(self: IAzClientContext2) = value
        """
        ...


    def AddApplicationGroups(self, varApplicationGroups:object): # -> 
        """ AddApplicationGroups(self: IAzClientContext2, varApplicationGroups: object) """
        ...

    def AddRoles(self, varRoles:object, bstrScopeName:str): # -> 
        """ AddRoles(self: IAzClientContext2, varRoles: object, bstrScopeName: str) """
        ...

    def AddStringSids(self, varStringSids:object): # -> 
        """ AddStringSids(self: IAzClientContext2, varStringSids: object) """
        ...

    def GetAssignedScopesPage(self, lOptions, PageSize, pvarCursor) -> Tuple_[object, object]:
        """ GetAssignedScopesPage(self: IAzClientContext2, lOptions: int, PageSize: int) -> (object, object) """
        ...


class IAzClientContext3(IAzClientContext2): # skipped bases: <type 'IAzClientContext'>, <type 'object'>
    """ no doc """
    @property
    def BizRuleInterfaces(self) -> IAzBizRuleInterfaces:
        """ Get: BizRuleInterfaces(self: IAzClientContext3) -> IAzBizRuleInterfaces """
        ...

    @property
    def BizRuleParameters(self) -> IAzBizRuleParameters:
        """ Get: BizRuleParameters(self: IAzClientContext3) -> IAzBizRuleParameters """
        ...

    @property
    def Sids(self) -> object:
        """ Get: Sids(self: IAzClientContext3) -> object """
        ...


    def AccessCheck2(self, bstrObjectName:str, bstrScopeName:str, lOperation:int) -> UInt32:
        """ AccessCheck2(self: IAzClientContext3, bstrObjectName: str, bstrScopeName: str, lOperation: int) -> UInt32 """
        ...

    def GetGroups(self, bstrScopeName:str, ulOptions:UInt32) -> object:
        """ GetGroups(self: IAzClientContext3, bstrScopeName: str, ulOptions: UInt32) -> object """
        ...

    def GetOperations(self, bstrScopeName:str) -> IAzOperations:
        """ GetOperations(self: IAzClientContext3, bstrScopeName: str) -> IAzOperations """
        ...

    def GetTasks(self, bstrScopeName:str) -> IAzTasks:
        """ GetTasks(self: IAzClientContext3, bstrScopeName: str) -> IAzTasks """
        ...

    def IsInRoleAssignment(self, bstrScopeName:str, bstrRoleName:str) -> bool:
        """ IsInRoleAssignment(self: IAzClientContext3, bstrScopeName: str, bstrRoleName: str) -> bool """
        ...


class IAzNameResolver: # skipped bases: <type 'object'>
    """ no doc """
    def NameFromSid(self, bstrSid, pSidType) -> Tuple_[str, int]:
        """ NameFromSid(self: IAzNameResolver, bstrSid: str) -> (str, int) """
        ...

    def NamesFromSids(self, vSids, pvSidTypes) -> Tuple_[object, object]:
        """ NamesFromSids(self: IAzNameResolver, vSids: object) -> (object, object) """
        ...


class IAzObjectPicker: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: IAzObjectPicker) -> str """
        ...


    def GetPrincipals(self, hParentWnd, bstrTitle, pvSidTypes, pvNames) -> Tuple_[object, _RemotableHandle, object, object]:
        """ GetPrincipals(self: IAzObjectPicker, hParentWnd: _RemotableHandle, bstrTitle: str) -> (object, _RemotableHandle, object, object) """
        ...


class IAzOperation: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApplicationData(self) -> str:
        """
        Get: ApplicationData(self: IAzOperation) -> str
        Set: ApplicationData(self: IAzOperation) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: IAzOperation) -> str
        Set: Description(self: IAzOperation) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: IAzOperation) -> str
        Set: Name(self: IAzOperation) = value
        """
        ...

    @property
    def OperationID(self) -> int:
        """
        Get: OperationID(self: IAzOperation) -> int
        Set: OperationID(self: IAzOperation) = value
        """
        ...

    @property
    def Writable(self) -> int:
        """ Get: Writable(self: IAzOperation) -> int """
        ...


    def GetProperty(self, lPropId:int, varReserved:object) -> object:
        """ GetProperty(self: IAzOperation, lPropId: int, varReserved: object) -> object """
        ...

    def SetProperty(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ SetProperty(self: IAzOperation, lPropId: int, varProp: object, varReserved: object) """
        ...

    def Submit(self, lFlags:int, varReserved:object): # -> 
        """ Submit(self: IAzOperation, lFlags: int, varReserved: object) """
        ...


class IAzOperation2(IAzOperation): # skipped bases: <type 'object'>
    """ no doc """
    def RoleAssignments(self, bstrScopeName:str, bRecursive:bool) -> IAzRoleAssignments:
        """ RoleAssignments(self: IAzOperation2, bstrScopeName: str, bRecursive: bool) -> IAzRoleAssignments """
        ...


class IAzOperations(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: IAzOperations) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IAzRole: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApplicationData(self) -> str:
        """
        Get: ApplicationData(self: IAzRole) -> str
        Set: ApplicationData(self: IAzRole) = value
        """
        ...

    @property
    def AppMembers(self) -> object:
        """ Get: AppMembers(self: IAzRole) -> object """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: IAzRole) -> str
        Set: Description(self: IAzRole) = value
        """
        ...

    @property
    def Members(self) -> object:
        """ Get: Members(self: IAzRole) -> object """
        ...

    @property
    def MembersName(self) -> object:
        """ Get: MembersName(self: IAzRole) -> object """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: IAzRole) -> str
        Set: Name(self: IAzRole) = value
        """
        ...

    @property
    def Operations(self) -> object:
        """ Get: Operations(self: IAzRole) -> object """
        ...

    @property
    def Tasks(self) -> object:
        """ Get: Tasks(self: IAzRole) -> object """
        ...

    @property
    def Writable(self) -> int:
        """ Get: Writable(self: IAzRole) -> int """
        ...


    def AddAppMember(self, bstrProp:str, varReserved:object): # -> 
        """ AddAppMember(self: IAzRole, bstrProp: str, varReserved: object) """
        ...

    def AddMember(self, bstrProp:str, varReserved:object): # -> 
        """ AddMember(self: IAzRole, bstrProp: str, varReserved: object) """
        ...

    def AddMemberName(self, bstrProp:str, varReserved:object): # -> 
        """ AddMemberName(self: IAzRole, bstrProp: str, varReserved: object) """
        ...

    def AddOperation(self, bstrProp:str, varReserved:object): # -> 
        """ AddOperation(self: IAzRole, bstrProp: str, varReserved: object) """
        ...

    def AddPropertyItem(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ AddPropertyItem(self: IAzRole, lPropId: int, varProp: object, varReserved: object) """
        ...

    def AddTask(self, bstrProp:str, varReserved:object): # -> 
        """ AddTask(self: IAzRole, bstrProp: str, varReserved: object) """
        ...

    def DeleteAppMember(self, bstrProp:str, varReserved:object): # -> 
        """ DeleteAppMember(self: IAzRole, bstrProp: str, varReserved: object) """
        ...

    def DeleteMember(self, bstrProp:str, varReserved:object): # -> 
        """ DeleteMember(self: IAzRole, bstrProp: str, varReserved: object) """
        ...

    def DeleteMemberName(self, bstrProp:str, varReserved:object): # -> 
        """ DeleteMemberName(self: IAzRole, bstrProp: str, varReserved: object) """
        ...

    def DeleteOperation(self, bstrProp:str, varReserved:object): # -> 
        """ DeleteOperation(self: IAzRole, bstrProp: str, varReserved: object) """
        ...

    def DeletePropertyItem(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ DeletePropertyItem(self: IAzRole, lPropId: int, varProp: object, varReserved: object) """
        ...

    def DeleteTask(self, bstrProp:str, varReserved:object): # -> 
        """ DeleteTask(self: IAzRole, bstrProp: str, varReserved: object) """
        ...

    def GetProperty(self, lPropId:int, varReserved:object) -> object:
        """ GetProperty(self: IAzRole, lPropId: int, varReserved: object) -> object """
        ...

    def SetProperty(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ SetProperty(self: IAzRole, lPropId: int, varProp: object, varReserved: object) """
        ...

    def Submit(self, lFlags:int, varReserved:object): # -> 
        """ Submit(self: IAzRole, lFlags: int, varReserved: object) """
        ...


class IAzRoleAssignment(IAzRole): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RoleDefinitions(self) -> IAzRoleDefinitions:
        """ Get: RoleDefinitions(self: IAzRoleAssignment) -> IAzRoleDefinitions """
        ...

    @property
    def Scope(self) -> IAzScope:
        """ Get: Scope(self: IAzRoleAssignment) -> IAzScope """
        ...


    def AddRoleDefinition(self, bstrRoleDefinition:str): # -> 
        """ AddRoleDefinition(self: IAzRoleAssignment, bstrRoleDefinition: str) """
        ...

    def DeleteRoleDefinition(self, bstrRoleDefinition:str): # -> 
        """ DeleteRoleDefinition(self: IAzRoleAssignment, bstrRoleDefinition: str) """
        ...


class IAzRoleAssignments(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: IAzRoleAssignments) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IAzTask: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApplicationData(self) -> str:
        """
        Get: ApplicationData(self: IAzTask) -> str
        Set: ApplicationData(self: IAzTask) = value
        """
        ...

    @property
    def BizRule(self) -> str:
        """
        Get: BizRule(self: IAzTask) -> str
        Set: BizRule(self: IAzTask) = value
        """
        ...

    @property
    def BizRuleImportedPath(self) -> str:
        """
        Get: BizRuleImportedPath(self: IAzTask) -> str
        Set: BizRuleImportedPath(self: IAzTask) = value
        """
        ...

    @property
    def BizRuleLanguage(self) -> str:
        """
        Get: BizRuleLanguage(self: IAzTask) -> str
        Set: BizRuleLanguage(self: IAzTask) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: IAzTask) -> str
        Set: Description(self: IAzTask) = value
        """
        ...

    @property
    def IsRoleDefinition(self) -> int:
        """
        Get: IsRoleDefinition(self: IAzTask) -> int
        Set: IsRoleDefinition(self: IAzTask) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: IAzTask) -> str
        Set: Name(self: IAzTask) = value
        """
        ...

    @property
    def Operations(self) -> object:
        """ Get: Operations(self: IAzTask) -> object """
        ...

    @property
    def Tasks(self) -> object:
        """ Get: Tasks(self: IAzTask) -> object """
        ...

    @property
    def Writable(self) -> int:
        """ Get: Writable(self: IAzTask) -> int """
        ...


    def AddOperation(self, bstrOp:str, varReserved:object): # -> 
        """ AddOperation(self: IAzTask, bstrOp: str, varReserved: object) """
        ...

    def AddPropertyItem(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ AddPropertyItem(self: IAzTask, lPropId: int, varProp: object, varReserved: object) """
        ...

    def AddTask(self, bstrTask:str, varReserved:object): # -> 
        """ AddTask(self: IAzTask, bstrTask: str, varReserved: object) """
        ...

    def DeleteOperation(self, bstrOp:str, varReserved:object): # -> 
        """ DeleteOperation(self: IAzTask, bstrOp: str, varReserved: object) """
        ...

    def DeletePropertyItem(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ DeletePropertyItem(self: IAzTask, lPropId: int, varProp: object, varReserved: object) """
        ...

    def DeleteTask(self, bstrTask:str, varReserved:object): # -> 
        """ DeleteTask(self: IAzTask, bstrTask: str, varReserved: object) """
        ...

    def GetProperty(self, lPropId:int, varReserved:object) -> object:
        """ GetProperty(self: IAzTask, lPropId: int, varReserved: object) -> object """
        ...

    def SetProperty(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ SetProperty(self: IAzTask, lPropId: int, varProp: object, varReserved: object) """
        ...

    def Submit(self, lFlags:int, varReserved:object): # -> 
        """ Submit(self: IAzTask, lFlags: int, varReserved: object) """
        ...


class IAzRoleDefinition(IAzTask): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RoleDefinitions(self) -> IAzRoleDefinitions:
        """ Get: RoleDefinitions(self: IAzRoleDefinition) -> IAzRoleDefinitions """
        ...


    def AddRoleDefinition(self, bstrRoleDefinition:str): # -> 
        """ AddRoleDefinition(self: IAzRoleDefinition, bstrRoleDefinition: str) """
        ...

    def DeleteRoleDefinition(self, bstrRoleDefinition:str): # -> 
        """ DeleteRoleDefinition(self: IAzRoleDefinition, bstrRoleDefinition: str) """
        ...

    def RoleAssignments(self, bstrScopeName:str, bRecursive:bool) -> IAzRoleAssignments:
        """ RoleAssignments(self: IAzRoleDefinition, bstrScopeName: str, bRecursive: bool) -> IAzRoleAssignments """
        ...


class IAzRoleDefinitions(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: IAzRoleDefinitions) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IAzRoles(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: IAzRoles) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IAzScope: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApplicationData(self) -> str:
        """
        Get: ApplicationData(self: IAzScope) -> str
        Set: ApplicationData(self: IAzScope) = value
        """
        ...

    @property
    def ApplicationGroups(self) -> IAzApplicationGroups:
        """ Get: ApplicationGroups(self: IAzScope) -> IAzApplicationGroups """
        ...

    @property
    def BizrulesWritable(self) -> int:
        """ Get: BizrulesWritable(self: IAzScope) -> int """
        ...

    @property
    def CanBeDelegated(self) -> int:
        """ Get: CanBeDelegated(self: IAzScope) -> int """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: IAzScope) -> str
        Set: Description(self: IAzScope) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: IAzScope) -> str
        Set: Name(self: IAzScope) = value
        """
        ...

    @property
    def PolicyAdministrators(self) -> object:
        """ Get: PolicyAdministrators(self: IAzScope) -> object """
        ...

    @property
    def PolicyAdministratorsName(self) -> object:
        """ Get: PolicyAdministratorsName(self: IAzScope) -> object """
        ...

    @property
    def PolicyReaders(self) -> object:
        """ Get: PolicyReaders(self: IAzScope) -> object """
        ...

    @property
    def PolicyReadersName(self) -> object:
        """ Get: PolicyReadersName(self: IAzScope) -> object """
        ...

    @property
    def Roles(self) -> IAzRoles:
        """ Get: Roles(self: IAzScope) -> IAzRoles """
        ...

    @property
    def Tasks(self) -> IAzTasks:
        """ Get: Tasks(self: IAzScope) -> IAzTasks """
        ...

    @property
    def Writable(self) -> int:
        """ Get: Writable(self: IAzScope) -> int """
        ...


    def AddPolicyAdministrator(self, bstrAdmin:str, varReserved:object): # -> 
        """ AddPolicyAdministrator(self: IAzScope, bstrAdmin: str, varReserved: object) """
        ...

    def AddPolicyAdministratorName(self, bstrAdmin:str, varReserved:object): # -> 
        """ AddPolicyAdministratorName(self: IAzScope, bstrAdmin: str, varReserved: object) """
        ...

    def AddPolicyReader(self, bstrReader:str, varReserved:object): # -> 
        """ AddPolicyReader(self: IAzScope, bstrReader: str, varReserved: object) """
        ...

    def AddPolicyReaderName(self, bstrReader:str, varReserved:object): # -> 
        """ AddPolicyReaderName(self: IAzScope, bstrReader: str, varReserved: object) """
        ...

    def AddPropertyItem(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ AddPropertyItem(self: IAzScope, lPropId: int, varProp: object, varReserved: object) """
        ...

    def CreateApplicationGroup(self, bstrGroupName:str, varReserved:object) -> IAzApplicationGroup:
        """ CreateApplicationGroup(self: IAzScope, bstrGroupName: str, varReserved: object) -> IAzApplicationGroup """
        ...

    def CreateRole(self, bstrRoleName:str, varReserved:object) -> IAzRole:
        """ CreateRole(self: IAzScope, bstrRoleName: str, varReserved: object) -> IAzRole """
        ...

    def CreateTask(self, bstrTaskName:str, varReserved:object) -> IAzTask:
        """ CreateTask(self: IAzScope, bstrTaskName: str, varReserved: object) -> IAzTask """
        ...

    def DeleteApplicationGroup(self, bstrGroupName:str, varReserved:object): # -> 
        """ DeleteApplicationGroup(self: IAzScope, bstrGroupName: str, varReserved: object) """
        ...

    def DeletePolicyAdministrator(self, bstrAdmin:str, varReserved:object): # -> 
        """ DeletePolicyAdministrator(self: IAzScope, bstrAdmin: str, varReserved: object) """
        ...

    def DeletePolicyAdministratorName(self, bstrAdmin:str, varReserved:object): # -> 
        """ DeletePolicyAdministratorName(self: IAzScope, bstrAdmin: str, varReserved: object) """
        ...

    def DeletePolicyReader(self, bstrReader:str, varReserved:object): # -> 
        """ DeletePolicyReader(self: IAzScope, bstrReader: str, varReserved: object) """
        ...

    def DeletePolicyReaderName(self, bstrReader:str, varReserved:object): # -> 
        """ DeletePolicyReaderName(self: IAzScope, bstrReader: str, varReserved: object) """
        ...

    def DeletePropertyItem(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ DeletePropertyItem(self: IAzScope, lPropId: int, varProp: object, varReserved: object) """
        ...

    def DeleteRole(self, bstrRoleName:str, varReserved:object): # -> 
        """ DeleteRole(self: IAzScope, bstrRoleName: str, varReserved: object) """
        ...

    def DeleteTask(self, bstrTaskName:str, varReserved:object): # -> 
        """ DeleteTask(self: IAzScope, bstrTaskName: str, varReserved: object) """
        ...

    def GetProperty(self, lPropId:int, varReserved:object) -> object:
        """ GetProperty(self: IAzScope, lPropId: int, varReserved: object) -> object """
        ...

    def OpenApplicationGroup(self, bstrGroupName:str, varReserved:object) -> IAzApplicationGroup:
        """ OpenApplicationGroup(self: IAzScope, bstrGroupName: str, varReserved: object) -> IAzApplicationGroup """
        ...

    def OpenRole(self, bstrRoleName:str, varReserved:object) -> IAzRole:
        """ OpenRole(self: IAzScope, bstrRoleName: str, varReserved: object) -> IAzRole """
        ...

    def OpenTask(self, bstrTaskName:str, varReserved:object) -> IAzTask:
        """ OpenTask(self: IAzScope, bstrTaskName: str, varReserved: object) -> IAzTask """
        ...

    def SetProperty(self, lPropId:int, varProp:object, varReserved:object): # -> 
        """ SetProperty(self: IAzScope, lPropId: int, varProp: object, varReserved: object) """
        ...

    def Submit(self, lFlags:int, varReserved:object): # -> 
        """ Submit(self: IAzScope, lFlags: int, varReserved: object) """
        ...


class IAzScope2(IAzScope): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RoleAssignments(self) -> IAzRoleAssignments:
        """ Get: RoleAssignments(self: IAzScope2) -> IAzRoleAssignments """
        ...

    @property
    def RoleDefinitions(self) -> IAzRoleDefinitions:
        """ Get: RoleDefinitions(self: IAzScope2) -> IAzRoleDefinitions """
        ...


    def CreateRoleAssignment(self, bstrRoleAssignmentName:str) -> IAzRoleAssignment:
        """ CreateRoleAssignment(self: IAzScope2, bstrRoleAssignmentName: str) -> IAzRoleAssignment """
        ...

    def CreateRoleDefinition(self, bstrRoleDefinitionName:str) -> IAzRoleDefinition:
        """ CreateRoleDefinition(self: IAzScope2, bstrRoleDefinitionName: str) -> IAzRoleDefinition """
        ...

    def DeleteRoleAssignment(self, bstrRoleAssignmentName:str): # -> 
        """ DeleteRoleAssignment(self: IAzScope2, bstrRoleAssignmentName: str) """
        ...

    def DeleteRoleDefinition(self, bstrRoleDefinitionName:str): # -> 
        """ DeleteRoleDefinition(self: IAzScope2, bstrRoleDefinitionName: str) """
        ...

    def OpenRoleAssignment(self, bstrRoleAssignmentName:str) -> IAzRoleAssignment:
        """ OpenRoleAssignment(self: IAzScope2, bstrRoleAssignmentName: str) -> IAzRoleAssignment """
        ...

    def OpenRoleDefinition(self, bstrRoleDefinitionName:str) -> IAzRoleDefinition:
        """ OpenRoleDefinition(self: IAzScope2, bstrRoleDefinitionName: str) -> IAzRoleDefinition """
        ...


class IAzScopes(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: IAzScopes) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IAzTask2(IAzTask): # skipped bases: <type 'object'>
    """ no doc """
    def RoleAssignments(self, bstrScopeName:str, bRecursive:bool) -> IAzRoleAssignments:
        """ RoleAssignments(self: IAzTask2, bstrScopeName: str, bRecursive: bool) -> IAzRoleAssignments """
        ...


class IAzTasks(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: IAzTasks) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class tagAZ_PROP_CONSTANTS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum tagAZ_PROP_CONSTANTS, values: AZ_AZSTORE_DEFAULT_DOMAIN_TIMEOUT (15000), AZ_AZSTORE_DEFAULT_MAX_SCRIPT_ENGINES (120), AZ_AZSTORE_DEFAULT_SCRIPT_ENGINE_TIMEOUT (45000), AZ_AZSTORE_FLAG_AUDIT_IS_CRITICAL (8), AZ_AZSTORE_FLAG_BATCH_UPDATE (4), AZ_AZSTORE_FLAG_CREATE (1), AZ_AZSTORE_FLAG_MANAGE_ONLY_PASSIVE_SUBMIT (32768), AZ_AZSTORE_FLAG_MANAGE_STORE_ONLY (2), AZ_AZSTORE_FORCE_APPLICATION_CLOSE (16), AZ_AZSTORE_MIN_DOMAIN_TIMEOUT (500), AZ_AZSTORE_MIN_SCRIPT_ENGINE_TIMEOUT (5000), AZ_AZSTORE_NT6_FUNCTION_LEVEL (32), AZ_CLIENT_CONTEXT_GET_GROUP_RECURSIVE (2), AZ_CLIENT_CONTEXT_GET_GROUPS_STORE_LEVEL_ONLY (2), AZ_CLIENT_CONTEXT_SKIP_GROUP (1), AZ_CLIENT_CONTEXT_SKIP_LDAP_QUERY (1), AZ_GROUPTYPE_BASIC (2), AZ_GROUPTYPE_BIZRULE (3), AZ_GROUPTYPE_LDAP_QUERY (1), AZ_MAX_APPLICATION_DATA_LENGTH (4096), AZ_MAX_APPLICATION_NAME_LENGTH (512), AZ_MAX_APPLICATION_VERSION_LENGTH (512), AZ_MAX_BIZRULE_STRING (65536), AZ_MAX_DESCRIPTION_LENGTH (1024), AZ_MAX_GROUP_BIZRULE_IMPORTED_PATH_LENGTH (512), AZ_MAX_GROUP_BIZRULE_LANGUAGE_LENGTH (64), AZ_MAX_GROUP_BIZRULE_LENGTH (65536), AZ_MAX_GROUP_LDAP_QUERY_LENGTH (4096), AZ_MAX_GROUP_NAME_LENGTH (64), AZ_MAX_NAME_LENGTH (65536), AZ_MAX_OPERATION_NAME_LENGTH (64), AZ_MAX_POLICY_URL_LENGTH (65536), AZ_MAX_ROLE_NAME_LENGTH (64), AZ_MAX_SCOPE_NAME_LENGTH (65536), AZ_MAX_TASK_BIZRULE_IMPORTED_PATH_LENGTH (512), AZ_MAX_TASK_BIZRULE_LANGUAGE_LENGTH (64), AZ_MAX_TASK_BIZRULE_LENGTH (65536), AZ_MAX_TASK_NAME_LENGTH (64), AZ_PROP_APPLICATION_AUTHZ_INTERFACE_CLSID (800), AZ_PROP_APPLICATION_BIZRULE_ENABLED (803), AZ_PROP_APPLICATION_DATA (4), AZ_PROP_APPLICATION_NAME (802), AZ_PROP_APPLICATION_VERSION (801), AZ_PROP_APPLY_STORE_SACL (900), AZ_PROP_AZSTORE_DOMAIN_TIMEOUT (100), AZ_PROP_AZSTORE_MAJOR_VERSION (103), AZ_PROP_AZSTORE_MAX_SCRIPT_ENGINES (102), AZ_PROP_AZSTORE_MINOR_VERSION (104), AZ_PROP_AZSTORE_SCRIPT_ENGINE_TIMEOUT (101), AZ_PROP_AZSTORE_TARGET_MACHINE (105), AZ_PROP_AZTORE_IS_ADAM_INSTANCE (106), AZ_PROP_CHILD_CREATE (5), AZ_PROP_CLIENT_CONTEXT_LDAP_QUERY_DN (709), AZ_PROP_CLIENT_CONTEXT_ROLE_FOR_ACCESS_CHECK (708), AZ_PROP_CLIENT_CONTEXT_USER_CANONICAL (704), AZ_PROP_CLIENT_CONTEXT_USER_DISPLAY (702), AZ_PROP_CLIENT_CONTEXT_USER_DN (700), AZ_PROP_CLIENT_CONTEXT_USER_DNS_SAM_COMPAT (707), AZ_PROP_CLIENT_CONTEXT_USER_GUID (703), AZ_PROP_CLIENT_CONTEXT_USER_SAM_COMPAT (701), AZ_PROP_CLIENT_CONTEXT_USER_UPN (705), AZ_PROP_DELEGATED_POLICY_USERS (904), AZ_PROP_DELEGATED_POLICY_USERS_NAME (907), AZ_PROP_DESCRIPTION (2), AZ_PROP_GENERATE_AUDITS (901), AZ_PROP_GROUP_APP_MEMBERS (401), AZ_PROP_GROUP_APP_NON_MEMBERS (402), AZ_PROP_GROUP_BIZRULE (408), AZ_PROP_GROUP_BIZRULE_IMPORTED_PATH (410), AZ_PROP_GROUP_BIZRULE_LANGUAGE (409), AZ_PROP_GROUP_LDAP_QUERY (403), AZ_PROP_GROUP_MEMBERS (404), AZ_PROP_GROUP_MEMBERS_NAME (406), AZ_PROP_GROUP_NON_MEMBERS (405), AZ_PROP_GROUP_NON_MEMBERS_NAME (407), AZ_PROP_GROUP_TYPE (400), AZ_PROP_NAME (1), AZ_PROP_OPERATION_ID (200), AZ_PROP_POLICY_ADMINS (902), AZ_PROP_POLICY_ADMINS_NAME (905), AZ_PROP_POLICY_READERS (903), AZ_PROP_POLICY_READERS_NAME (906), AZ_PROP_ROLE_APP_MEMBERS (500), AZ_PROP_ROLE_MEMBERS (501), AZ_PROP_ROLE_MEMBERS_NAME (505), AZ_PROP_ROLE_OPERATIONS (502), AZ_PROP_ROLE_TASKS (504), AZ_PROP_SCOPE_BIZRULES_WRITABLE (600), AZ_PROP_SCOPE_CAN_BE_DELEGATED (601), AZ_PROP_TASK_BIZRULE (301), AZ_PROP_TASK_BIZRULE_IMPORTED_PATH (304), AZ_PROP_TASK_BIZRULE_LANGUAGE (302), AZ_PROP_TASK_IS_ROLE_DEFINITION (305), AZ_PROP_TASK_OPERATIONS (300), AZ_PROP_TASK_TASKS (303), AZ_PROP_WRITABLE (3), AZ_SUBMIT_FLAG_ABORT (1), AZ_SUBMIT_FLAG_FLUSH (2) """
    AZ_AZSTORE_DEFAULT_DOMAIN_TIMEOUT: tagAZ_PROP_CONSTANTS = ...
    AZ_AZSTORE_DEFAULT_MAX_SCRIPT_ENGINES: tagAZ_PROP_CONSTANTS = ...
    AZ_AZSTORE_DEFAULT_SCRIPT_ENGINE_TIMEOUT: tagAZ_PROP_CONSTANTS = ...
    AZ_AZSTORE_FLAG_AUDIT_IS_CRITICAL: tagAZ_PROP_CONSTANTS = ...
    AZ_AZSTORE_FLAG_BATCH_UPDATE: tagAZ_PROP_CONSTANTS = ...
    AZ_AZSTORE_FLAG_CREATE: tagAZ_PROP_CONSTANTS = ...
    AZ_AZSTORE_FLAG_MANAGE_ONLY_PASSIVE_SUBMIT: tagAZ_PROP_CONSTANTS = ...
    AZ_AZSTORE_FLAG_MANAGE_STORE_ONLY: tagAZ_PROP_CONSTANTS = ...
    AZ_AZSTORE_FORCE_APPLICATION_CLOSE: tagAZ_PROP_CONSTANTS = ...
    AZ_AZSTORE_MIN_DOMAIN_TIMEOUT: tagAZ_PROP_CONSTANTS = ...
    AZ_AZSTORE_MIN_SCRIPT_ENGINE_TIMEOUT: tagAZ_PROP_CONSTANTS = ...
    AZ_AZSTORE_NT6_FUNCTION_LEVEL: tagAZ_PROP_CONSTANTS = ...
    AZ_CLIENT_CONTEXT_GET_GROUPS_STORE_LEVEL_ONLY: tagAZ_PROP_CONSTANTS = ...
    AZ_CLIENT_CONTEXT_GET_GROUP_RECURSIVE: tagAZ_PROP_CONSTANTS = ...
    AZ_CLIENT_CONTEXT_SKIP_GROUP: tagAZ_PROP_CONSTANTS = ...
    AZ_CLIENT_CONTEXT_SKIP_LDAP_QUERY: tagAZ_PROP_CONSTANTS = ...
    AZ_GROUPTYPE_BASIC: tagAZ_PROP_CONSTANTS = ...
    AZ_GROUPTYPE_BIZRULE: tagAZ_PROP_CONSTANTS = ...
    AZ_GROUPTYPE_LDAP_QUERY: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_APPLICATION_DATA_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_APPLICATION_NAME_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_APPLICATION_VERSION_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_BIZRULE_STRING: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_DESCRIPTION_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_GROUP_BIZRULE_IMPORTED_PATH_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_GROUP_BIZRULE_LANGUAGE_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_GROUP_BIZRULE_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_GROUP_LDAP_QUERY_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_GROUP_NAME_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_NAME_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_OPERATION_NAME_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_POLICY_URL_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_ROLE_NAME_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_SCOPE_NAME_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_TASK_BIZRULE_IMPORTED_PATH_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_TASK_BIZRULE_LANGUAGE_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_TASK_BIZRULE_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_MAX_TASK_NAME_LENGTH: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_APPLICATION_AUTHZ_INTERFACE_CLSID: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_APPLICATION_BIZRULE_ENABLED: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_APPLICATION_DATA: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_APPLICATION_NAME: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_APPLICATION_VERSION: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_APPLY_STORE_SACL: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_AZSTORE_DOMAIN_TIMEOUT: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_AZSTORE_MAJOR_VERSION: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_AZSTORE_MAX_SCRIPT_ENGINES: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_AZSTORE_MINOR_VERSION: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_AZSTORE_SCRIPT_ENGINE_TIMEOUT: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_AZSTORE_TARGET_MACHINE: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_AZTORE_IS_ADAM_INSTANCE: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_CHILD_CREATE: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_CLIENT_CONTEXT_LDAP_QUERY_DN: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_CLIENT_CONTEXT_ROLE_FOR_ACCESS_CHECK: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_CLIENT_CONTEXT_USER_CANONICAL: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_CLIENT_CONTEXT_USER_DISPLAY: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_CLIENT_CONTEXT_USER_DN: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_CLIENT_CONTEXT_USER_DNS_SAM_COMPAT: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_CLIENT_CONTEXT_USER_GUID: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_CLIENT_CONTEXT_USER_SAM_COMPAT: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_CLIENT_CONTEXT_USER_UPN: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_DELEGATED_POLICY_USERS: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_DELEGATED_POLICY_USERS_NAME: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_DESCRIPTION: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_GENERATE_AUDITS: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_GROUP_APP_MEMBERS: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_GROUP_APP_NON_MEMBERS: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_GROUP_BIZRULE: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_GROUP_BIZRULE_IMPORTED_PATH: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_GROUP_BIZRULE_LANGUAGE: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_GROUP_LDAP_QUERY: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_GROUP_MEMBERS: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_GROUP_MEMBERS_NAME: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_GROUP_NON_MEMBERS: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_GROUP_NON_MEMBERS_NAME: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_GROUP_TYPE: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_NAME: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_OPERATION_ID: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_POLICY_ADMINS: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_POLICY_ADMINS_NAME: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_POLICY_READERS: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_POLICY_READERS_NAME: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_ROLE_APP_MEMBERS: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_ROLE_MEMBERS: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_ROLE_MEMBERS_NAME: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_ROLE_OPERATIONS: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_ROLE_TASKS: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_SCOPE_BIZRULES_WRITABLE: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_SCOPE_CAN_BE_DELEGATED: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_TASK_BIZRULE: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_TASK_BIZRULE_IMPORTED_PATH: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_TASK_BIZRULE_LANGUAGE: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_TASK_IS_ROLE_DEFINITION: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_TASK_OPERATIONS: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_TASK_TASKS: tagAZ_PROP_CONSTANTS = ...
    AZ_PROP_WRITABLE: tagAZ_PROP_CONSTANTS = ...
    AZ_SUBMIT_FLAG_ABORT: tagAZ_PROP_CONSTANTS = ...
    AZ_SUBMIT_FLAG_FLUSH: tagAZ_PROP_CONSTANTS = ...
    value__ = ...


class _RemotableHandle: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    fContext = ...
    u = ...


class __MIDL_IWinTypes_0009: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    hInproc = ...
    hRemote = ...


