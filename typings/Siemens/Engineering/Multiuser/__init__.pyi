# encoding: utf-8
# module Siemens.Engineering.Multiuser calls itself Multiuser
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (EngineeringTargetInvocationException,
    IEngineeringComposition, IEngineeringObject, ProjectBase)

from System import Enum, IEquatable

from System.Collections import IList

from System.IO import DirectoryInfo, FileInfo

"""The following names are not found in the module: (BoundEvent,
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class LocalSession(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents a Local Session """
    @property
    def MarkingService(self) -> MarkingService:
        """
        Marking Service

        Get: MarkingService(self: LocalSession) -> MarkingService
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: LocalSession) -> IEngineeringObject
        """
        ...

    @property
    def Project(self) -> MultiuserProject:
        """
        Gives access to the project information

        Get: Project(self: LocalSession) -> MultiuserProject
        """
        ...


    def Close(self): # ->
        """
        Close(self: LocalSession)

            Performs a close operation of Multiuser localSession.
        """
        ...

    def CloseAndCommit(self, comment:str) -> int:
        """
        CloseAndCommit(self: LocalSession, comment: str) -> int

            Performs a commit of opened server project changes.

            comment: The comment for changes being committed.

            Returns: System.Int32
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: LocalSession) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def IsUptoDate(self) -> bool:
        """
        IsUptoDate(self: LocalSession) -> bool

            Gets the value that Session is Up-to-date or not.

            Returns: System.Boolean
        """
        ...

    def Save(self): # ->
        """
        Save(self: LocalSession)

            Performs a save of opened session.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: LocalSession) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LocalSessionComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of Local sessions """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: LocalSessionComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: LocalSessionComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Open(self, localSessionPath:FileInfo) -> LocalSession:
        """
        Open(self: LocalSessionComposition, localSessionPath: FileInfo) -> LocalSession

            Performs a open operation of Multiuser localSession.

            localSessionPath: The path of local session.

            Returns: Siemens.Engineering.Multiuser.LocalSession
        """
        ...

    def OpenServerProject(self, localSessionPath:FileInfo) -> LocalSession:
        """
        OpenServerProject(self: LocalSessionComposition, localSessionPath: FileInfo) -> LocalSession

            Performs a open operation of Multiuser Server Project.

            localSessionPath: The path of local session.

            Returns: Siemens.Engineering.Multiuser.LocalSession
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: LocalSessionComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[LocalSession](enumerable: IEnumerable[LocalSession], value: LocalSession) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LocalSessionInfo(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents information about a local session """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: LocalSessionInfo) -> IEngineeringObject
        """
        ...

    @property
    def ProjectFileInfo(self) -> FileInfo:
        """
        The location of the local session.

        Get: ProjectFileInfo(self: LocalSessionInfo) -> FileInfo
        """
        ...

    @property
    def SessionId(self) -> int:
        """
        The Unique identifier of a Local Session

        Get: SessionId(self: LocalSessionInfo) -> int
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: LocalSessionInfo) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: LocalSessionInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LockStateProvider(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Provides information about Lock on a project. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: LockStateProvider) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: LockStateProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def GetLockOwner(self) -> str:
        """
        GetLockOwner(self: LockStateProvider) -> str

            Gets the information about lock owner.

            Returns: System.String
        """
        ...

    def IsProjectLocked(self) -> bool:
        """
        IsProjectLocked(self: LockStateProvider) -> bool

            Gets the value that Project is locked or not.

            Returns: System.Boolean
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: LockStateProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Marking(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents a non deleted marking. """
    @property
    def MarkedObject(self) -> IEngineeringObject:
        """
        Gets the marked non deleted engineering object.

        Get: MarkedObject(self: Marking) -> IEngineeringObject
        """
        ...

    @property
    def MarkState(self) -> MarkState:
        """
        Gets the mark state of the marked non deleted engineering object.

        Get: MarkState(self: Marking) -> MarkState
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: Marking) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: Marking) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: Marking) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MarkingComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of markings. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: MarkingComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: MarkingComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: MarkingComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Marking](enumerable: IEnumerable[Marking], value: Marking) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Markings(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents non deleted markings. """
    @property
    def AllMarkings(self) -> MarkingComposition:
        """
        Gets all the non deleted markings.

        Get: AllMarkings(self: Markings) -> MarkingComposition
        """
        ...

    @property
    def ConflictedMarkings(self) -> MarkingComposition:
        """
        Gets all the non deleted conflicted markings.

        Get: ConflictedMarkings(self: Markings) -> MarkingComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: Markings) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: Markings) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: Markings) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MarkingService(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents the marking service navigator. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: MarkingService) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: MarkingService) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def GetMarkings(self) -> Markings:
        """
        GetMarkings(self: MarkingService) -> Markings

            Gets the markings from the opened local session.

            Returns: Siemens.Engineering.Multiuser.Markings
        """
        ...

    def GetMarkStateInfo(self, engineeringObject:IEngineeringObject) -> MarkStateInfo:
        """
        GetMarkStateInfo(self: MarkingService, engineeringObject: IEngineeringObject) -> MarkStateInfo

            Gets the marking related information.

            engineeringObject: The engineering object for which the marking information has to be fetched.

            Returns: Siemens.Engineering.Multiuser.MarkStateInfo
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: MarkingService) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MarkState(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Status of the marked engineering object

    enum (flags) MarkState, values: IsMarkedByMe (2), IsMarkedByOthers (4), IsUptoDate (1), None (0)
    """
    IsMarkedByMe: MarkState = ...
    IsMarkedByOthers: MarkState = ...
    IsUptoDate: MarkState = ...
    value__ = ...


class MarkStateInfo(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents information about the markstate of an engineering object. """
    @property
    def IsMarkable(self) -> bool:
        """
        Is the engineering object a markable object.True for a whitelisted object, False for a blacklisted object.

        Get: IsMarkable(self: MarkStateInfo) -> bool
        """
        ...

    @property
    def MarkState(self) -> MarkState:
        """
        Represents the MarkSate types such as IsMarkedByMe, IsMarkedByOthers and IsUptoDate

        Get: MarkState(self: MarkStateInfo) -> MarkState
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: MarkStateInfo) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: MarkStateInfo) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: MarkStateInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MultiuserException(EngineeringTargetInvocationException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>, <type 'object'>
    """
    This exception indicates that exception occured during execution of Multiuser-Openness API call

    MultiuserException()

    MultiuserException(text: str)

    MultiuserException(text: str, exception: Exception)

    MultiuserException(text: str, *detailTexts: Array[str])
    """
    SerializeObjectState = ...


class MultiuserProject(ProjectBase): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IMasterCopyTarget'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringServiceProvider'>, <type 'ITransactionSupport'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IServiceProvider'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents a multiuser project """
    pass

class ProjectServer(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents Project Server """
    @property
    def Host(self) -> str:
        """
        Host of the server.

        Get: Host(self: ProjectServer) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ProjectServer) -> IEngineeringObject
        """
        ...

    @property
    def Port(self) -> int:
        """
        Port of the server.

        Get: Port(self: ProjectServer) -> int
        """
        ...

    @property
    def ServerName(self) -> str:
        """
        Alias name of the server.

        Get: ServerName(self: ProjectServer) -> str
        """
        ...


    def AddProjectToServer(self, projectFileInfo:FileInfo): # ->
        """
        AddProjectToServer(self: ProjectServer, projectFileInfo: FileInfo)

            Adds project to Multiuser server

            projectFileInfo: The FileInfo containing the path of the single user project.
        """
        ...

    def CreateLocalSession(self, serverProjectInfo:ServerProjectInfo, localSessionName:str, localSessionPath:DirectoryInfo, sessionCreationMode:SessionCreationMode) -> LocalSessionInfo:
        """
        CreateLocalSession(self: ProjectServer, serverProjectInfo: ServerProjectInfo, localSessionName: str, localSessionPath: DirectoryInfo, sessionCreationMode: SessionCreationMode) -> LocalSessionInfo

            Perform creation of Multiuser Local Session.

            serverProjectInfo: The information about the server project.

            localSessionName: Name of the local session.

            localSessionPath: Path of the local session.

            sessionCreationMode: Mode of session creation.

            Returns: Siemens.Engineering.Multiuser.LocalSessionInfo
        """
        ...

    def DeleteConnection(self): # ->
        """
        DeleteConnection(self: ProjectServer)

            Delete project server connection
        """
        ...

    def DeleteLocalSessionFromServer(self, serverProjectInfo:ServerProjectInfo, localSessionInfo:LocalSessionInfo): # ->
        """
        DeleteLocalSessionFromServer(self: ProjectServer, serverProjectInfo: ServerProjectInfo, localSessionInfo: LocalSessionInfo)

            Perform deletion of Multiuser Local Session.

            serverProjectInfo: The information about the server project.

            localSessionInfo: The information about the local session.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ProjectServer) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def GetLocalSessions(self, serverProjectInfo:ServerProjectInfo) -> IList:
        """
        GetLocalSessions(self: ProjectServer, serverProjectInfo: ServerProjectInfo) -> IList[LocalSessionInfo]

            Performs a get operation of all available local session for the given ServerProjectInfo.

            serverProjectInfo: The information about the server project.

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Multiuser.LocalSessionInfo>
        """
        ...

    def GetLockStateProvider(self, serverProjectInfo:ServerProjectInfo) -> LockStateProvider:
        """
        GetLockStateProvider(self: ProjectServer, serverProjectInfo: ServerProjectInfo) -> LockStateProvider

            Performs a get operation of LockStateProvider.

            serverProjectInfo: The information about the server project.

            Returns: Siemens.Engineering.Multiuser.LockStateProvider
        """
        ...

    def GetServerProjects(self) -> IList:
        """
        GetServerProjects(self: ProjectServer) -> IList[ServerProjectInfo]

            Retrieves the available projects info from a specified server.

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Multiuser.ServerProjectInfo>
        """
        ...

    def SetHostName(self, hostName:str): # ->
        """
        SetHostName(self: ProjectServer, hostName: str)

            Set the host name.

            hostName: Host name of the server.
        """
        ...

    def SetPort(self, port:int): # ->
        """
        SetPort(self: ProjectServer, port: int)

            Set the port value.

            port: Port number of the server.
        """
        ...

    def SetProtocol(self, protocol:Protocol): # ->
        """
        SetProtocol(self: ProjectServer, protocol: Protocol)

            Set the protocal value.

            protocol: Protocol of the server.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ProjectServer) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ProjectServerComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of Project Server """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ProjectServerComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ProjectServerComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ProjectServerComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ProjectServer](enumerable: IEnumerable[ProjectServer], value: ProjectServer) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Protocol(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Protocol

    enum Protocol, values: Http (1), Https (0)
    """
    Http: Protocol = ...
    Https: Protocol = ...
    value__ = ...


class ServerProjectInfo(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents information about a server project """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ServerProjectInfo) -> IEngineeringObject
        """
        ...

    @property
    def ProjectName(self) -> str:
        """
        The name of the project.

        Get: ProjectName(self: ServerProjectInfo) -> str
        """
        ...

    @property
    def ServerAlias(self) -> str:
        """
        Alias name of the server where project exist.

        Get: ServerAlias(self: ServerProjectInfo) -> str
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ServerProjectInfo) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ServerProjectInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SessionCreationMode(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Local session creation mode

    enum SessionCreationMode, values: Exclusive (1), Multiuser (0)
    """
    Exclusive: SessionCreationMode = ...
    Multiuser: SessionCreationMode = ...
    value__ = ...
