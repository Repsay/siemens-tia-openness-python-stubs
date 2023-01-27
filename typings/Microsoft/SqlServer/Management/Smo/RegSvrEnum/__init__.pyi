# encoding: utf-8
# module Microsoft.SqlServer.Management.Smo.RegSvrEnum calls itself RegSvrEnum
# from Microsoft.SqlServer.RegSvrEnum, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Common import (IRenewableToken, 
    ServerVersion)

from System import ApplicationException, Guid, IComparable, Int64

from System.Collections.Generic import List

from System.Collections.Specialized import NameValueCollection

from System.Xml import XmlReader, XmlWriter

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class RegisteredServerException(ApplicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RegisteredServerException(message: str, previous: Exception)
    RegisteredServerException(message: str)
    RegisteredServerException()
    """
    SerializeObjectState = ...


class UIConnectionGroupInfo(List): # skipped bases: <type 'IEnumerable[UIConnectionInfo]'>, <type 'IReadOnlyList[UIConnectionInfo]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[UIConnectionInfo]'>, <type 'IList[UIConnectionInfo]'>, <type 'IReadOnlyCollection[UIConnectionInfo]'>, <type 'ICollection'>, <type 'object'>
    """
    UIConnectionGroupInfo()
    UIConnectionGroupInfo(collection: IEnumerable[UIConnectionInfo])
    UIConnectionGroupInfo(capacity: int)
    UIConnectionGroupInfo(other: UIConnectionGroupInfo)
    UIConnectionGroupInfo(connectionInfo: UIConnectionInfo)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: UIConnectionGroupInfo) -> str
        Set: Name(self: UIConnectionGroupInfo) = value
        """
        ...


    def DeepCopy(self, withNewConnectionIds:bool) -> UIConnectionGroupInfo:
        """ DeepCopy(self: UIConnectionGroupInfo, withNewConnectionIds: bool) -> UIConnectionGroupInfo """
        ...

    def ShallowCopy(self) -> UIConnectionGroupInfo:
        """ ShallowCopy(self: UIConnectionGroupInfo) -> UIConnectionGroupInfo """
        ...


class UIConnectionInfo(IComparable): # skipped bases: <type 'object'>
    """
    UIConnectionInfo()
    UIConnectionInfo(lhs: UIConnectionInfo, generateNewId: bool)
    UIConnectionInfo(lhs: UIConnectionInfo)
    """
    @property
    def AdvancedOptions(self) -> NameValueCollection:
        """ Get: AdvancedOptions(self: UIConnectionInfo) -> NameValueCollection """
        ...

    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: UIConnectionInfo) -> str
        Set: ApplicationName(self: UIConnectionInfo) = value
        """
        ...

    @property
    def AuthenticationType(self) -> int:
        """
        Get: AuthenticationType(self: UIConnectionInfo) -> int
        Set: AuthenticationType(self: UIConnectionInfo) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: UIConnectionInfo) -> str
        Set: DisplayName(self: UIConnectionInfo) = value
        """
        ...

    @property
    def EncryptedPassword(self) -> str:
        """
        Get: EncryptedPassword(self: UIConnectionInfo) -> str
        Set: EncryptedPassword(self: UIConnectionInfo) = value
        """
        ...

    @property
    def Id(self) -> Int64:
        """ Get: Id(self: UIConnectionInfo) -> Int64 """
        ...

    @property
    def OtherParams(self) -> str:
        """
        Get: OtherParams(self: UIConnectionInfo) -> str
        Set: OtherParams(self: UIConnectionInfo) = value
        """
        ...

    @property
    def Password(self) -> str:
        """
        Get: Password(self: UIConnectionInfo) -> str
        Set: Password(self: UIConnectionInfo) = value
        """
        ...

    @property
    def PersistPassword(self) -> bool:
        """
        Get: PersistPassword(self: UIConnectionInfo) -> bool
        Set: PersistPassword(self: UIConnectionInfo) = value
        """
        ...

    @property
    def RenewableToken(self) -> IRenewableToken:
        """
        Get: RenewableToken(self: UIConnectionInfo) -> IRenewableToken
        Set: RenewableToken(self: UIConnectionInfo) = value
        """
        ...

    @property
    def ServerName(self) -> str:
        """
        Get: ServerName(self: UIConnectionInfo) -> str
        Set: ServerName(self: UIConnectionInfo) = value
        """
        ...

    @property
    def ServerNameNoDot(self) -> str:
        """ Get: ServerNameNoDot(self: UIConnectionInfo) -> str """
        ...

    @property
    def ServerType(self) -> Guid:
        """
        Get: ServerType(self: UIConnectionInfo) -> Guid
        Set: ServerType(self: UIConnectionInfo) = value
        """
        ...

    @property
    def ServerVersion(self) -> ServerVersion:
        """
        Get: ServerVersion(self: UIConnectionInfo) -> ServerVersion
        Set: ServerVersion(self: UIConnectionInfo) = value
        """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: UIConnectionInfo) -> str
        Set: UserName(self: UIConnectionInfo) = value
        """
        ...


    def Copy(self) -> UIConnectionInfo:
        """ Copy(self: UIConnectionInfo) -> UIConnectionInfo """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: UIConnectionInfo, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: UIConnectionInfo) -> int """
        ...

    @staticmethod
    def LoadFromStream(reader:XmlReader) -> UIConnectionInfo:
        """ LoadFromStream(reader: XmlReader) -> UIConnectionInfo """
        ...

    def SaveToStream(self, writer:XmlWriter, saveName:bool): # -> 
        """ SaveToStream(self: UIConnectionInfo, writer: XmlWriter, saveName: bool) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    XmlAdvancedOptions: str = ...
    XmlAuthenticationType: str = ...
    XmlDisplayName: str = ...
    XmlItemTypeAttribute: str = ...
    XmlPassword: str = ...
    XmlServerName: str = ...
    XmlServerType: str = ...
    XmlStart: str = ...
    XmlUserName: str = ...


