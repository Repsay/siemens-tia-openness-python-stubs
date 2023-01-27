# encoding: utf-8
# module Microsoft.SqlServer.Management.Smo.Mail calls itself Mail
# from Microsoft.SqlServer.Smo, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Common import (IAlterable, ICreatable, 
    IDropIfExists, IDroppable, IRenamable)

from Microsoft.SqlServer.Management.Smo import (IScriptable, NamedSmoObject, 
    ScriptNameObjectBase, Server, SimpleObjectCollectionBase, SqlSmoObject)

from System import Array

from System.Data import DataTable

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ConfigurationValue(IAlterable, IScriptable, NamedSmoObject): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: ConfigurationValue) -> str
        Set: Description(self: ConfigurationValue) = value
        """
        ...

    @property
    def Parent(self) -> SqlMail:
        """ Get: Parent(self: ConfigurationValue) -> SqlMail """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: ConfigurationValue) -> str
        Set: Value(self: ConfigurationValue) = value
        """
        ...


    m_ExtendedProperties = ...
    singletonParent = ...


class ConfigurationValueCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> SqlMail:
        """ Get: Parent(self: ConfigurationValueCollection) -> SqlMail """
        ...


    def Add(self, configurationValue:ConfigurationValue): # -> 
        """ Add(self: ConfigurationValueCollection, configurationValue: ConfigurationValue) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ConfigurationValueCollection, array: Array[ConfigurationValue], index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class MailAccount(IDroppable, IAlterable, ICreatable, IScriptable, IRenamable, ScriptNameObjectBase, IDropIfExists): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    MailAccount()
    MailAccount(sqlMail: SqlMail, name: str)
    MailAccount(parent: SqlMail, name: str, description: str)
    MailAccount(parent: SqlMail, name: str, description: str, displayName: str, emailAddress: str)
    """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: MailAccount) -> str
        Set: Description(self: MailAccount) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: MailAccount) -> str
        Set: DisplayName(self: MailAccount) = value
        """
        ...

    @property
    def EmailAddress(self) -> str:
        """
        Get: EmailAddress(self: MailAccount) -> str
        Set: EmailAddress(self: MailAccount) = value
        """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: MailAccount) -> int """
        ...

    @property
    def IsBusyAccount(self) -> bool:
        """ Get: IsBusyAccount(self: MailAccount) -> bool """
        ...

    @property
    def MailServers(self) -> MailServerCollection:
        """ Get: MailServers(self: MailAccount) -> MailServerCollection """
        ...

    @property
    def Parent(self) -> SqlMail:
        """
        Get: Parent(self: MailAccount) -> SqlMail
        Set: Parent(self: MailAccount) = value
        """
        ...

    @property
    def ReplyToAddress(self) -> str:
        """
        Get: ReplyToAddress(self: MailAccount) -> str
        Set: ReplyToAddress(self: MailAccount) = value
        """
        ...


    def GetAccountProfileNames(self) -> Array:
        """ GetAccountProfileNames(self: MailAccount) -> Array[str] """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, sqlMail: SqlMail, name: str)
        __new__(cls: type, parent: SqlMail, name: str, description: str)
        __new__(cls: type, parent: SqlMail, name: str, description: str, displayName: str, emailAddress: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class MailAccountCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> SqlMail:
        """ Get: Parent(self: MailAccountCollection) -> SqlMail """
        ...


    def Add(self, mailAccount:MailAccount): # -> 
        """ Add(self: MailAccountCollection, mailAccount: MailAccount) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: MailAccountCollection, array: Array[MailAccount], index: int) """
        ...

    def ItemById(self, id:int) -> MailAccount:
        """ ItemById(self: MailAccountCollection, id: int) -> MailAccount """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class MailProfile(IDroppable, IAlterable, ICreatable, IScriptable, IRenamable, ScriptNameObjectBase, IDropIfExists): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    MailProfile()
    MailProfile(sqlMail: SqlMail, name: str)
    MailProfile(parent: SqlMail, name: str, description: str)
    """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: MailProfile) -> str
        Set: Description(self: MailProfile) = value
        """
        ...

    @property
    def ForceDeleteForActiveProfiles(self) -> bool:
        """
        Get: ForceDeleteForActiveProfiles(self: MailProfile) -> bool
        Set: ForceDeleteForActiveProfiles(self: MailProfile) = value
        """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: MailProfile) -> int """
        ...

    @property
    def IsBusyProfile(self) -> bool:
        """ Get: IsBusyProfile(self: MailProfile) -> bool """
        ...

    @property
    def Parent(self) -> SqlMail:
        """
        Get: Parent(self: MailProfile) -> SqlMail
        Set: Parent(self: MailProfile) = value
        """
        ...


    def AddAccount(self, accountName:str, sequenceNumber:int): # -> 
        """ AddAccount(self: MailProfile, accountName: str, sequenceNumber: int) """
        ...

    def AddPrincipal(self, principalName:str, isDefaultProfile:bool = ...): # -> 
        """ AddPrincipal(self: MailProfile, principalName: str)AddPrincipal(self: MailProfile, principalName: str, isDefaultProfile: bool) """
        ...

    def EnumAccounts(self) -> DataTable:
        """ EnumAccounts(self: MailProfile) -> DataTable """
        ...

    def EnumPrincipals(self) -> DataTable:
        """ EnumPrincipals(self: MailProfile) -> DataTable """
        ...

    def RemoveAccount(self, accountName:str): # -> 
        """ RemoveAccount(self: MailProfile, accountName: str) """
        ...

    def RemovePrincipal(self, principalName:str): # -> 
        """ RemovePrincipal(self: MailProfile, principalName: str) """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, sqlMail: SqlMail, name: str)
        __new__(cls: type, parent: SqlMail, name: str, description: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class MailProfileCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> SqlMail:
        """ Get: Parent(self: MailProfileCollection) -> SqlMail """
        ...


    def Add(self, mailProfile:MailProfile): # -> 
        """ Add(self: MailProfileCollection, mailProfile: MailProfile) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: MailProfileCollection, array: Array[MailProfile], index: int) """
        ...

    def ItemById(self, id:int) -> MailProfile:
        """ ItemById(self: MailProfileCollection, id: int) -> MailProfile """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class MailServer(ScriptNameObjectBase, IAlterable, IScriptable, IRenamable): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """ no doc """
    @property
    def EnableSsl(self) -> bool:
        """
        Get: EnableSsl(self: MailServer) -> bool
        Set: EnableSsl(self: MailServer) = value
        """
        ...

    @property
    def NoCredentialChange(self) -> bool:
        """
        Get: NoCredentialChange(self: MailServer) -> bool
        Set: NoCredentialChange(self: MailServer) = value
        """
        ...

    @property
    def Parent(self) -> MailAccount:
        """ Get: Parent(self: MailServer) -> MailAccount """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: MailServer) -> int
        Set: Port(self: MailServer) = value
        """
        ...

    @property
    def ServerType(self) -> str:
        """ Get: ServerType(self: MailServer) -> str """
        ...

    @property
    def UseDefaultCredentials(self) -> bool:
        """
        Get: UseDefaultCredentials(self: MailServer) -> bool
        Set: UseDefaultCredentials(self: MailServer) = value
        """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: MailServer) -> str
        Set: UserName(self: MailServer) = value
        """
        ...


    def SetAccount(self, userName:str, password:str): # -> 
        """ SetAccount(self: MailServer, userName: str, password: str)SetAccount(self: MailServer, userName: str, password: SecureString) """
        ...

    def SetPassword(self, password:str): # -> 
        """ SetPassword(self: MailServer, password: str)SetPassword(self: MailServer, password: SecureString) """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class MailServerCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> MailAccount:
        """ Get: Parent(self: MailServerCollection) -> MailAccount """
        ...


    def Add(self, mailServer:MailServer): # -> 
        """ Add(self: MailServerCollection, mailServer: MailServer) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: MailServerCollection, array: Array[MailServer], index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class SqlMail(SqlSmoObject, IScriptable): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """ no doc """
    @property
    def Accounts(self) -> MailAccountCollection:
        """ Get: Accounts(self: SqlMail) -> MailAccountCollection """
        ...

    @property
    def ConfigurationValues(self) -> ConfigurationValueCollection:
        """ Get: ConfigurationValues(self: SqlMail) -> ConfigurationValueCollection """
        ...

    @property
    def Parent(self) -> Server:
        """ Get: Parent(self: SqlMail) -> Server """
        ...

    @property
    def Profiles(self) -> MailProfileCollection:
        """ Get: Profiles(self: SqlMail) -> MailProfileCollection """
        ...


    m_ExtendedProperties = ...
    singletonParent = ...


