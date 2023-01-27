# encoding: utf-8
# module Siemens.Engineering.Umac calls itself Umac
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringAssociation,
    IEngineeringComposition, IEngineeringObject, IEngineeringService)

from System import Enum, EventArgs, IEquatable

from System.Collections import IList

from System.Security import SecureString

"""The following names are not found in the module: (BoundEvent,
    IInternalAssociationAccess, IInternalCompositionAccess,
    IInternalObjectAccess, field#)
"""

from Siemens import IInternalAssociationAccess, IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class AuthenticationType(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Represents the Authentication Type of a Project User

    enum AuthenticationType, values: Password (0), Radius (1)
    """
    Password: AuthenticationType = ...
    Radius: AuthenticationType = ...
    value__ = ...


class DeviceFunctionRight(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Device function right """
    @property
    def Group(self) -> str:
        """
        Device function right group name

        Get: Group(self: DeviceFunctionRight) -> str
        """
        ...

    @property
    def Identifier(self) -> str:
        """
        Device function right OpennessId

        Get: Identifier(self: DeviceFunctionRight) -> str
        """
        ...

    @property
    def Name(self) -> str:
        """
        Device function right name

        Get: Name(self: DeviceFunctionRight) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: DeviceFunctionRight) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: DeviceFunctionRight) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: DeviceFunctionRight) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CustomDeviceFunctionRight(DeviceFunctionRight): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Custom Device Function Right """
    @property
    def Comment(self) -> str:
        """
        Device function right comment

        Get: Comment(self: CustomDeviceFunctionRight) -> str
        """
        ...


    def SetName(self, name:str): # ->
        """
        SetName(self: CustomDeviceFunctionRight, name: str)

            Updates the name of custom device function right

            name: Updates the custom device function right name
        """
        ...


class CustomDeviceFunctionRightComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Custom device function right composition """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: CustomDeviceFunctionRightComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> CustomDeviceFunctionRight:
        """
        Find(self: CustomDeviceFunctionRightComposition, name: str) -> CustomDeviceFunctionRight

            Fetches custom device function right.

            name: Custom device function right name

            Returns: Siemens.Engineering.Umac.CustomDeviceFunctionRight
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CustomDeviceFunctionRightComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CustomDeviceFunctionRightComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CustomDeviceFunctionRight](enumerable: IEnumerable[CustomDeviceFunctionRight], value: CustomDeviceFunctionRight) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Role(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents an abstract UMAC Role object """
    @property
    def Identifier(self) -> str:
        """
        Role Openness Id

        Get: Identifier(self: Role) -> str
        """
        ...

    @property
    def Name(self) -> str:
        """
        Name on the user defined role

        Get: Name(self: Role) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: Role) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: Role) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: Role) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CustomRole(Role): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Provides User Defined Role with associated attributes """
    @property
    def AssignedEngineeringRights(self) -> EngineeringFunctionRightAssociation:
        """
        Fetches assigned engineering rights for custom role

        Get: AssignedEngineeringRights(self: CustomRole) -> EngineeringFunctionRightAssociation
        """
        ...

    @property
    def Comment(self) -> str:
        """
        Project user comment

        Get: Comment(self: CustomRole) -> str

        Set: Comment(self: CustomRole) = value
        """
        ...

    @property
    def SessionTimeOut(self) -> int:
        """
        Project user session timeout

        Get: SessionTimeOut(self: CustomRole) -> int

        Set: SessionTimeOut(self: CustomRole) = value
        """
        ...


    def AssignDeviceFunctionRight(self, umacDevice:UmacDevice, deviceFunctionRight:DeviceFunctionRight): # ->
        """
        AssignDeviceFunctionRight(self: CustomRole, umacDevice: UmacDevice, deviceFunctionRight: DeviceFunctionRight)

            Add a Device Function Rights to Custom Role

            umacDevice: Umac Device

            deviceFunctionRight: Device function right
        """
        ...

    def Delete(self): # ->
        """
        Delete(self: CustomRole)

            Deletes this instance.
        """
        ...

    def GetAssignedDeviceFunctionRights(self, device:UmacDevice) -> IList:
        """
        GetAssignedDeviceFunctionRights(self: CustomRole, device: UmacDevice) -> IList[DeviceFunctionRight]

            Gets all the assigned device function rights on the present role object for the given device

            device: Umac Device

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Umac.DeviceFunctionRight>
        """
        ...

    def SetName(self, name:str): # ->
        """
        SetName(self: CustomRole, name: str)

            Updates the name of the custom role

            name: new name to be assigned to custom role
        """
        ...

    def UnAssignDeviceFunctionRight(self, device:UmacDevice, deviceFunctionRight:DeviceFunctionRight): # ->
        """
        UnAssignDeviceFunctionRight(self: CustomRole, device: UmacDevice, deviceFunctionRight: DeviceFunctionRight)

            UnAssign a Device Function Rights from Custom Role

            device: Umac Device

            deviceFunctionRight: Device function right
        """
        ...


class CustomRoleComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Custom Role Composition """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: CustomRoleComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> CustomRole:
        """
        Find(self: CustomRoleComposition, name: str) -> CustomRole

            Fetches custom role

            name: Custom role name to Find

            Returns: Siemens.Engineering.Umac.CustomRole
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CustomRoleComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CustomRoleComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CustomRole](enumerable: IEnumerable[CustomRole], value: CustomRole) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DeviceFunctionRightAssociation(IEquatable, IEngineeringAssociation, IInternalAssociationAccess): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Device function right association """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent..

        Get: Parent(self: DeviceFunctionRightAssociation) -> IEngineeringObject
        """
        ...


    def Find(self, identifier:str) -> DeviceFunctionRight:
        """
        Find(self: DeviceFunctionRightAssociation, identifier: str) -> DeviceFunctionRight

            Fetches corresponding device function right

            identifier: Identifier is the search key to get the corresponding right

            Returns: Siemens.Engineering.Umac.DeviceFunctionRight
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: DeviceFunctionRightAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: DeviceFunctionRightAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[DeviceFunctionRight](enumerable: IEnumerable[DeviceFunctionRight], value: DeviceFunctionRight) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class EngineeringFunctionRight(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents an abstract UMAC Engineering Function Right object """
    @property
    def Identifier(self) -> str:
        """
        Engineering Function Right Openness Identifier. This identifier will be used for find purpose

        Get: Identifier(self: EngineeringFunctionRight) -> str
        """
        ...

    @property
    def Name(self) -> str:
        """
        Engineering function right name

        Get: Name(self: EngineeringFunctionRight) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: EngineeringFunctionRight) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: EngineeringFunctionRight) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: EngineeringFunctionRight) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class EngineeringFunctionRightAssociation(IEquatable, IEngineeringAssociation, IInternalAssociationAccess): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Associated Engineering function rights """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent..

        Get: Parent(self: EngineeringFunctionRightAssociation) -> IEngineeringObject
        """
        ...


    def Add(self, item:EngineeringFunctionRight): # ->
        """
        Add(self: EngineeringFunctionRightAssociation, item: EngineeringFunctionRight)

            Adds an item.

            item: The item to be added.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: EngineeringFunctionRightAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Remove(self, item:EngineeringFunctionRight) -> bool:
        """
        Remove(self: EngineeringFunctionRightAssociation, item: EngineeringFunctionRight) -> bool

            Removes an item.

            item: The item to be removed.

            Returns: true if the item was removed; otherwise false.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: EngineeringFunctionRightAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[EngineeringFunctionRight](enumerable: IEnumerable[EngineeringFunctionRight], value: EngineeringFunctionRight) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class EngineeringFunctionRightComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Gets all UMAC Engineering Function Right """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: EngineeringFunctionRightComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> EngineeringFunctionRight:
        """
        Find(self: EngineeringFunctionRightComposition, name: str) -> EngineeringFunctionRight

            Find UMAC Engineering Function Right corresponding to the name passed

            name: Engineering function right name

            Returns: Siemens.Engineering.Umac.EngineeringFunctionRight
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: EngineeringFunctionRightComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: EngineeringFunctionRightComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[EngineeringFunctionRight](enumerable: IEnumerable[EngineeringFunctionRight], value: EngineeringFunctionRight) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class User(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents an abstract User object """
    @property
    def Name(self) -> str:
        """
        Name of the user.

        Get: Name(self: User) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: User) -> IEngineeringObject
        """
        ...

    @property
    def Roles(self) -> RoleAssociation:
        """
        Roles assigned to the user.

        Get: Roles(self: User) -> RoleAssociation
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: User) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: User) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ProjectUser(User): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents a UMAC Project User object """
    @property
    def Comment(self) -> str:
        """
        Project user comment

        Get: Comment(self: ProjectUser) -> str

        Set: Comment(self: ProjectUser) = value
        """
        ...

    @property
    def IsActive(self) -> bool:
        """
        Project user is active or not

        Get: IsActive(self: ProjectUser) -> bool
        """
        ...

    @property
    def ProjectUserAuthenticationType(self) -> AuthenticationType:
        """
        Project user authentication type

        Get: ProjectUserAuthenticationType(self: ProjectUser) -> AuthenticationType

        Set: ProjectUserAuthenticationType(self: ProjectUser) = value
        """
        ...

    @property
    def SessionTimeOut(self) -> int:
        """
        Project user session timeout

        Get: SessionTimeOut(self: ProjectUser) -> int

        Set: SessionTimeOut(self: ProjectUser) = value
        """
        ...


    def Activate(self): # ->
        """
        Activate(self: ProjectUser)

            Activate project user
        """
        ...

    def Deactivate(self): # ->
        """
        Deactivate(self: ProjectUser)

            Deactivate project user
        """
        ...

    def Delete(self): # ->
        """
        Delete(self: ProjectUser)

            Deletes this instance.
        """
        ...

    def SetName(self, name:str): # ->
        """
        SetName(self: ProjectUser, name: str)

            Updates the name of the project user

            name: new name to be assigned to project user
        """
        ...

    def SetPassword(self, securePassword:SecureString): # ->
        """
        SetPassword(self: ProjectUser, securePassword: SecureString)

            UnAssign role to project user

            securePassword: new password for project user
        """
        ...


class ProjectUserComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Project user composition """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ProjectUserComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> ProjectUser:
        """
        Find(self: ProjectUserComposition, name: str) -> ProjectUser

            Fetches project user

            name: Project user name to Find

            Returns: Siemens.Engineering.Umac.ProjectUser
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ProjectUserComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ProjectUserComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ProjectUser](enumerable: IEnumerable[ProjectUser], value: ProjectUser) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RoleAssociation(IEquatable, IEngineeringAssociation, IInternalAssociationAccess): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Roles assigned to the Users and Umc user groups. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent..

        Get: Parent(self: RoleAssociation) -> IEngineeringObject
        """
        ...


    def Add(self, item:Role): # ->
        """
        Add(self: RoleAssociation, item: Role)

            Adds an item.

            item: The item to be added.
        """
        ...

    def Find(self, identifier:str) -> Role:
        """
        Find(self: RoleAssociation, identifier: str) -> Role

            Find Role corresponding to the Openness ID

            identifier: Identifier is the search key to get the corresponding Role

            Returns: Siemens.Engineering.Umac.Role
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: RoleAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Remove(self, item:Role) -> bool:
        """
        Remove(self: RoleAssociation, item: Role) -> bool

            Removes an item.

            item: The item to be removed.

            Returns: true if the item was removed; otherwise false.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: RoleAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Role](enumerable: IEnumerable[Role], value: Role) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SystemDeviceFunctionRight(DeviceFunctionRight): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Custom Device Function Right """
    @property
    def Comment(self) -> str:
        """
        System device function right comment

        Get: Comment(self: SystemDeviceFunctionRight) -> str
        """
        ...



class SystemDeviceFunctionRightComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ System device function right composition """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: SystemDeviceFunctionRightComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> SystemDeviceFunctionRight:
        """
        Find(self: SystemDeviceFunctionRightComposition, name: str) -> SystemDeviceFunctionRight

            Fetches system device function right.

            name: System device function right name

            Returns: Siemens.Engineering.Umac.SystemDeviceFunctionRight
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SystemDeviceFunctionRightComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SystemDeviceFunctionRightComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SystemDeviceFunctionRight](enumerable: IEnumerable[SystemDeviceFunctionRight], value: SystemDeviceFunctionRight) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SystemRole(Role): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents a UMAC System Role object """
    @property
    def AssignedEngineeringRights(self) -> EngineeringFunctionRightAssociation:
        """
        Fetches assigned engineering rights

        Get: AssignedEngineeringRights(self: SystemRole) -> EngineeringFunctionRightAssociation
        """
        ...


    def GetAssignedSystemDeviceFunctionRights(self, device:UmacDevice) -> IList:
        """
        GetAssignedSystemDeviceFunctionRights(self: SystemRole, device: UmacDevice) -> IList[DeviceFunctionRight]

            Gets all the assigned system device function rights on the present role object for the given device

            device: Umac Device

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Umac.DeviceFunctionRight>
        """
        ...


class SystemRoleComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Gets all System Roles """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: SystemRoleComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> SystemRole:
        """
        Find(self: SystemRoleComposition, name: str) -> SystemRole

            Fetches system role

            name: System role name

            Returns: Siemens.Engineering.Umac.SystemRole
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SystemRoleComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SystemRoleComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SystemRole](enumerable: IEnumerable[SystemRole], value: SystemRole) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UmacConfigurator(IEquatable, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'object'>
    """ Provides UMAC entities like Users, Roles and Function Rights """
    @property
    def AnonymousUser(self) -> ProjectUser:
        """
        Gets Project user

        Get: AnonymousUser(self: UmacConfigurator) -> ProjectUser
        """
        ...

    @property
    def CustomDeviceFunctionRights(self) -> CustomDeviceFunctionRightComposition:
        """
        Gets all the Custom Device Function Rights

        Get: CustomDeviceFunctionRights(self: UmacConfigurator) -> CustomDeviceFunctionRightComposition
        """
        ...

    @property
    def CustomRoles(self) -> CustomRoleComposition:
        """
        Get all the custom roles

        Get: CustomRoles(self: UmacConfigurator) -> CustomRoleComposition
        """
        ...

    @property
    def EngineeringFunctionRights(self) -> EngineeringFunctionRightComposition:
        """
        Get all the engineering function rights

        Get: EngineeringFunctionRights(self: UmacConfigurator) -> EngineeringFunctionRightComposition
        """
        ...

    @property
    def ProjectUsers(self) -> ProjectUserComposition:
        """
        Get all project users

        Get: ProjectUsers(self: UmacConfigurator) -> ProjectUserComposition
        """
        ...

    @property
    def SystemRoles(self) -> SystemRoleComposition:
        """
        Get all the system roles

        Get: SystemRoles(self: UmacConfigurator) -> SystemRoleComposition
        """
        ...

    @property
    def UmcUserGroups(self) -> UmcUserGroupComposition:
        """
        Get all Umc User Groups imported in TiaProject

        Get: UmcUserGroups(self: UmacConfigurator) -> UmcUserGroupComposition
        """
        ...

    @property
    def UmcUsers(self) -> UmcUserComposition:
        """
        Get all Umc Users

        Get: UmcUsers(self: UmacConfigurator) -> UmcUserComposition
        """
        ...


    def ActivateAnonymousUser(self): # ->
        """
        ActivateAnonymousUser(self: UmacConfigurator)

            Activates anonymous user
        """
        ...

    def DeactivateAnonymousUser(self): # ->
        """
        DeactivateAnonymousUser(self: UmacConfigurator)

            Deactivates anonymous user
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UmacConfigurator) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UmacConfigurator) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UmacDevice(IEquatable, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'object'>
    """ The class for getting Umac Device """
    @property
    def AvailableDeviceFunctionRights(self) -> DeviceFunctionRightAssociation:
        """
        fetches available device function rights for corresponding umac device

        Get: AvailableDeviceFunctionRights(self: UmacDevice) -> DeviceFunctionRightAssociation
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UmacDevice) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UmacDevice) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UmcAuthenticationEventArgs(IInternalObjectAccess, IEngineeringObject, IEquatable, EventArgs): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ EventArgs for the UmcAuthentication. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: UmcAuthenticationEventArgs) -> IEngineeringObject
        """
        ...

    @property
    def UmcCredentials(self) -> UmcCredentials:
        """
        Credentials for Umc Authentication.

        Get: UmcCredentials(self: UmcAuthenticationEventArgs) -> UmcCredentials

        Set: UmcCredentials(self: UmcAuthenticationEventArgs) = value
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UmcAuthenticationEventArgs) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UmcAuthenticationEventArgs) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class UmcCredentials(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Object that is used to authenticate user. """
    @property
    def Name(self) -> str:
        """
        User name.

        Get: Name(self: UmcCredentials) -> str

        Set: Name(self: UmcCredentials) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: UmcCredentials) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UmcCredentials) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def SetPassword(self, password:SecureString): # ->
        """
        SetPassword(self: UmcCredentials, password: SecureString)

            Set password.

            password: Password
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UmcCredentials) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UmcServer(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Provides UMC entities like UmcUsers and UmcGroups etc. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: UmcServer) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UmcServer) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def GetUserByName(self, userName:str) -> UmcUserInfo:
        """
        GetUserByName(self: UmcServer, userName: str) -> UmcUserInfo

            Get umc user from Umc server for the specified name

            userName: Name of Umc user to be retrieved from Umc server

            Returns: Siemens.Engineering.Umac.UmcUserInfo
        """
        ...

    def GetUserGroupByName(self, userGroupName:str) -> UmcUserGroupInfo:
        """
        GetUserGroupByName(self: UmcServer, userGroupName: str) -> UmcUserGroupInfo

            Gets the Umc User group from UMC server

            userGroupName: The name of the umc user group to get

            Returns: Siemens.Engineering.Umac.UmcUserGroupInfo
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UmcServer) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Authentication = ...


class UmcServerConfigurator(IEquatable, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'object'>
    """ Provides UMC Server Navigator. """
    @property
    def UmcServer(self) -> UmcServer:
        """
        A single navigator UmcServer representing a Umc Server

        Get: UmcServer(self: UmcServerConfigurator) -> UmcServer
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UmcServerConfigurator) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UmcServerConfigurator) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UmcUser(User): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ UmcUser represents a imported UmcUser in Project """
    @property
    def IsActive(self) -> bool:
        """
        Indicates whether the UmcUser is Active.

        Get: IsActive(self: UmcUser) -> bool
        """
        ...


    def Activate(self): # ->
        """
        Activate(self: UmcUser)

            Activate umc user
        """
        ...

    def Deactivate(self): # ->
        """
        Deactivate(self: UmcUser)

            Deactivate umc user
        """
        ...

    def Delete(self): # ->
        """
        Delete(self: UmcUser)

            Deletes this instance.
        """
        ...


class UmcUserComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Umc User Composition """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: UmcUserComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> UmcUser:
        """
        Find(self: UmcUserComposition, name: str) -> UmcUser

            Finds the Umc user in the project

            name: The name of the Umc user in the project

            Returns: Siemens.Engineering.Umac.UmcUser
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UmcUserComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UmcUserComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[UmcUser](enumerable: IEnumerable[UmcUser], value: UmcUser) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UmcUserGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ It represents a imported UmcUser group in Project """
    @property
    def Description(self) -> str:
        """
        Description of the Umc User group

        Get: Description(self: UmcUserGroup) -> str
        """
        ...

    @property
    def IsActive(self) -> bool:
        """
        Project user is active or not

        Get: IsActive(self: UmcUserGroup) -> bool
        """
        ...

    @property
    def Name(self) -> str:
        """
        Name of the Umc Usergroup

        Get: Name(self: UmcUserGroup) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: UmcUserGroup) -> IEngineeringObject
        """
        ...

    @property
    def Roles(self) -> RoleAssociation:
        """
        Roles assigned to the umc user group.

        Get: Roles(self: UmcUserGroup) -> RoleAssociation
        """
        ...


    def Activate(self): # ->
        """
        Activate(self: UmcUserGroup)

            Activate umc user group
        """
        ...

    def Deactivate(self): # ->
        """
        Deactivate(self: UmcUserGroup)

            Deactivate umc user group
        """
        ...

    def Delete(self): # ->
        """
        Delete(self: UmcUserGroup)

            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UmcUserGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UmcUserGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UmcUserGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Umc User Group Composition """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: UmcUserGroupComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> UmcUserGroup:
        """
        Find(self: UmcUserGroupComposition, name: str) -> UmcUserGroup

            Finds the Umc user group in the project

            name: The name of the Umc user group in the project

            Returns: Siemens.Engineering.Umac.UmcUserGroup
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UmcUserGroupComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UmcUserGroupComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[UmcUserGroup](enumerable: IEnumerable[UmcUserGroup], value: UmcUserGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UmcUserGroupInfo(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Umc user group on the Umc Server """
    @property
    def Description(self) -> str:
        """
        Description of umc user group

        Get: Description(self: UmcUserGroupInfo) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: UmcUserGroupInfo) -> IEngineeringObject
        """
        ...

    @property
    def UserGroupName(self) -> str:
        """
        Name of umc user group

        Get: UserGroupName(self: UmcUserGroupInfo) -> str
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UmcUserGroupInfo) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UmcUserGroupInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UmcUserInfo(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents a umc user on a Umc Server """
    @property
    def Name(self) -> str:
        """
        Name of umc user

        Get: Name(self: UmcUserInfo) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: UmcUserInfo) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UmcUserInfo) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UmcUserInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
