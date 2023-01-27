# encoding: utf-8
# module Siemens.Engineering.SW.OpcUa calls itself OpcUa
# from Siemens.Engineering, Version=16.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringComposition, IEngineeringObject,
    IEngineeringService, MultilingualText)

from System import DateTime, IEquatable

from System.IO import FileInfo

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class OpcUaCommunicationGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Top level OpcUa Communication folder """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: OpcUaCommunicationGroup) -> IEngineeringObject
        """
        ...

    @property
    def ServerInterfaceGroup(self) -> ServerInterfaceGroup:
        """
        OPCUA Server Interface Folder

        Get: ServerInterfaceGroup(self: OpcUaCommunicationGroup) -> ServerInterfaceGroup
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: OpcUaCommunicationGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: OpcUaCommunicationGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class OpcUaProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ OpcUa Provider """
    @property
    def CommunicationGroup(self) -> OpcUaCommunicationGroup:
        """
        Access the OpcUa Communication Folder

        Get: CommunicationGroup(self: OpcUaProvider) -> OpcUaCommunicationGroup
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: OpcUaProvider) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: OpcUaProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: OpcUaProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ReferenceNamespace(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ OpcUa Reference Namespace """
    @property
    def Author(self) -> str:
        """
        Author

        Get: Author(self: ReferenceNamespace) -> str

        Set: Author(self: ReferenceNamespace) = value
        """
        ...

    @property
    def Comment(self) -> MultilingualText:
        """
        Comment

        Get: Comment(self: ReferenceNamespace) -> MultilingualText
        """
        ...

    @property
    def CreationTime(self) -> DateTime:
        """
        Creation time

        Get: CreationTime(self: ReferenceNamespace) -> DateTime
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Enable reference namespace and download to PLC

        Get: Enabled(self: ReferenceNamespace) -> bool

        Set: Enabled(self: ReferenceNamespace) = value
        """
        ...

    @property
    def LastModified(self) -> DateTime:
        """
        Last modified time

        Get: LastModified(self: ReferenceNamespace) -> DateTime
        """
        ...

    @property
    def Name(self) -> str:
        """
        Name

        Get: Name(self: ReferenceNamespace) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ReferenceNamespace) -> IEngineeringObject
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: ReferenceNamespace)

            Deletes this instance.
        """
        ...

    def Export(self, filePath:FileInfo): # ->
        """
        Export(self: ReferenceNamespace, filePath: FileInfo)

            Exports the original XML File

            filePath: Path to the location to save
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ReferenceNamespace) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, filePath:FileInfo): # ->
        """
        Import(self: ReferenceNamespace, filePath: FileInfo)

            Import file

            filePath: Path to file
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ReferenceNamespace) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ReferenceNamespaceComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of Reference Namespaces """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ReferenceNamespaceComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ReferenceNamespaceComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ReferenceNamespaceComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ReferenceNamespace](enumerable: IEnumerable[ReferenceNamespace], value: ReferenceNamespace) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ServerInterface(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ OpcUa Server Interface """
    @property
    def Author(self) -> str:
        """
        Author

        Get: Author(self: ServerInterface) -> str

        Set: Author(self: ServerInterface) = value
        """
        ...

    @property
    def Comment(self) -> MultilingualText:
        """
        Comment

        Get: Comment(self: ServerInterface) -> MultilingualText
        """
        ...

    @property
    def CreationTime(self) -> DateTime:
        """
        Creation time

        Get: CreationTime(self: ServerInterface) -> DateTime
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Enable server interface and download to PLC

        Get: Enabled(self: ServerInterface) -> bool

        Set: Enabled(self: ServerInterface) = value
        """
        ...

    @property
    def LastModified(self) -> DateTime:
        """
        Last modified time

        Get: LastModified(self: ServerInterface) -> DateTime
        """
        ...

    @property
    def Name(self) -> str:
        """
        Name

        Get: Name(self: ServerInterface) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ServerInterface) -> IEngineeringObject
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: ServerInterface)

            Deletes this instance.
        """
        ...

    def Export(self, filePath:FileInfo): # ->
        """
        Export(self: ServerInterface, filePath: FileInfo)

            Exports the original XML File

            filePath: Path to the location to save
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ServerInterface) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, filePath:FileInfo): # ->
        """
        Import(self: ServerInterface, filePath: FileInfo)

            Import file

            filePath: Path to file
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ServerInterface) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ServerInterfaceComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of Server Interfaces """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ServerInterfaceComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ServerInterfaceComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ServerInterfaceComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ServerInterface](enumerable: IEnumerable[ServerInterface], value: ServerInterface) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ServerInterfaceGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Contains Server Interfaces """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ServerInterfaceGroup) -> IEngineeringObject
        """
        ...

    @property
    def ReferenceNamespaces(self) -> ReferenceNamespaceComposition:
        """
        Returns a list of Server Interfaces

        Get: ReferenceNamespaces(self: ServerInterfaceGroup) -> ReferenceNamespaceComposition
        """
        ...

    @property
    def ServerInterfaces(self) -> ServerInterfaceComposition:
        """
        Returns a list of Server Interfaces

        Get: ServerInterfaces(self: ServerInterfaceGroup) -> ServerInterfaceComposition
        """
        ...

    @property
    def SimaticInterfaces(self) -> SimaticInterfaceComposition:
        """
        Returns a list of Server Interfaces

        Get: SimaticInterfaces(self: ServerInterfaceGroup) -> SimaticInterfaceComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ServerInterfaceGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ServerInterfaceGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SimaticInterface(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ OpcUa Simatic Interface """
    @property
    def Author(self) -> str:
        """
        Author

        Get: Author(self: SimaticInterface) -> str

        Set: Author(self: SimaticInterface) = value
        """
        ...

    @property
    def Comment(self) -> MultilingualText:
        """
        Comment

        Get: Comment(self: SimaticInterface) -> MultilingualText
        """
        ...

    @property
    def CreationTime(self) -> DateTime:
        """
        Creation time

        Get: CreationTime(self: SimaticInterface) -> DateTime
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Enable simatic interface and download to PLC

        Get: Enabled(self: SimaticInterface) -> bool

        Set: Enabled(self: SimaticInterface) = value
        """
        ...

    @property
    def LastModified(self) -> DateTime:
        """
        Last modified time

        Get: LastModified(self: SimaticInterface) -> DateTime
        """
        ...

    @property
    def Name(self) -> str:
        """
        Name

        Get: Name(self: SimaticInterface) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SimaticInterface) -> IEngineeringObject
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: SimaticInterface)

            Deletes this instance.
        """
        ...

    def Export(self, filePath:FileInfo): # ->
        """
        Export(self: SimaticInterface, filePath: FileInfo)

            Exports the original XML File

            filePath: Path to the location to save
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SimaticInterface) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SimaticInterface) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SimaticInterfaceComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of Simatic Interfaces """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: SimaticInterfaceComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SimaticInterfaceComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SimaticInterfaceComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SimaticInterface](enumerable: IEnumerable[SimaticInterface], value: SimaticInterface) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
