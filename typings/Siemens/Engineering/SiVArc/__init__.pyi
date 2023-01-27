# encoding: utf-8
# module Siemens.Engineering.SiVArc calls itself SiVArc
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringComposition, IEngineeringObject, 
    IEngineeringService)

from Siemens.Engineering.Library.MasterCopies import MasterCopy

from System import DateTime, Enum, IEquatable

from System.Collections import IEnumerable

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

# no functions
# classes

class AlarmRule(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents alarm rule object """
    @property
    def Comment(self) -> str:
        """
        Alarm rule comment
        Get: Comment(self: AlarmRule) -> str
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Alarm rule condition
        Get: Condition(self: AlarmRule) -> str
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether alarm rule is selected
        Get: Enabled(self: AlarmRule) -> bool
        """
        ...

    @property
    def Name(self) -> str:
        """
        Alarm rule name
        Get: Name(self: AlarmRule) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: AlarmRule) -> IEngineeringObject
        """
        ...


    def Delete(self): # -> 
        """
        Delete(self: AlarmRule)
            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: AlarmRule) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: AlarmRule) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AlarmRuleComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Collection of immediate alarm rules """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: AlarmRuleComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, ruleMasterCopy:MasterCopy, createOption:CreateOptions = ...) -> AlarmRule:
        """
        CreateFrom(self: AlarmRuleComposition, ruleMasterCopy: MasterCopy) -> AlarmRule
            Copy alarm rule from library to project with default replace option
            ruleMasterCopy: Alarm rule master copy
            Returns: Siemens.Engineering.SiVArc.AlarmRule
        CreateFrom(self: AlarmRuleComposition, ruleMasterCopy: MasterCopy, createOption: CreateOptions) -> AlarmRule
            Copy alarm rule from library to project with create options
            ruleMasterCopy: Alarm rule master copy
            createOption: Create option
            Returns: Siemens.Engineering.SiVArc.AlarmRule
        """
        ...

    def Find(self, name:str) -> AlarmRule:
        """
        Find(self: AlarmRuleComposition, name: str) -> AlarmRule
            Finds alarm rule based on name
            name: Alarm rule name
            Returns: Siemens.Engineering.SiVArc.AlarmRule
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: AlarmRuleComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: AlarmRuleComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[AlarmRule](enumerable: IEnumerable[AlarmRule], value: AlarmRule) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AlarmRuleGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents alarm rule group """
    @property
    def Comment(self) -> str:
        """
        Alarm rule group comment
        Get: Comment(self: AlarmRuleGroup) -> str
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Alarm rule group condition
        Get: Condition(self: AlarmRuleGroup) -> str
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether alarm rule group is selected
        Get: Enabled(self: AlarmRuleGroup) -> bool
        """
        ...

    @property
    def Groups(self) -> AlarmRuleGroupComposition:
        """
        Collection of immediate groups
        Get: Groups(self: AlarmRuleGroup) -> AlarmRuleGroupComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        Alarm rule group name
        Get: Name(self: AlarmRuleGroup) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: AlarmRuleGroup) -> IEngineeringObject
        """
        ...

    @property
    def Rules(self) -> AlarmRuleComposition:
        """
        Collection of immediate rules
        Get: Rules(self: AlarmRuleGroup) -> AlarmRuleComposition
        """
        ...


    def Delete(self): # -> 
        """
        Delete(self: AlarmRuleGroup)
            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: AlarmRuleGroup) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: AlarmRuleGroup) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AlarmRuleGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Collection of immediate alarm rule groups """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: AlarmRuleGroupComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, groupMasterCopy:MasterCopy, createOption:CreateOptions = ...) -> AlarmRuleGroup:
        """
        CreateFrom(self: AlarmRuleGroupComposition, groupMasterCopy: MasterCopy) -> AlarmRuleGroup
            Copy alarm rule group from library to project with default replace option
            groupMasterCopy: Alarm rule group master copy
            Returns: Siemens.Engineering.SiVArc.AlarmRuleGroup
        CreateFrom(self: AlarmRuleGroupComposition, groupMasterCopy: MasterCopy, createOption: CreateOptions) -> AlarmRuleGroup
            Copy alarm rule group from library to project with create options
            groupMasterCopy: Alarm rule group master copy
            createOption: Create option
            Returns: Siemens.Engineering.SiVArc.AlarmRuleGroup
        """
        ...

    def Find(self, name:str) -> AlarmRuleGroup:
        """
        Find(self: AlarmRuleGroupComposition, name: str) -> AlarmRuleGroup
            Finds alarm rule group based on name
            name: Alarm rule group name
            Returns: Siemens.Engineering.SiVArc.AlarmRuleGroup
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: AlarmRuleGroupComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: AlarmRuleGroupComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[AlarmRuleGroup](enumerable: IEnumerable[AlarmRuleGroup], value: AlarmRuleGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AlarmRules(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents alarm rules editor """
    @property
    def Groups(self) -> AlarmRuleGroupComposition:
        """
        Navigate to all immediate alarm rule groups
        Get: Groups(self: AlarmRules) -> AlarmRuleGroupComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: AlarmRules) -> IEngineeringObject
        """
        ...

    @property
    def Rules(self) -> AlarmRuleComposition:
        """
        Navigate to all immediate alarm rules
        Get: Rules(self: AlarmRules) -> AlarmRuleComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: AlarmRules) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: AlarmRules) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CopyRule(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents copy rule object """
    @property
    def Comment(self) -> str:
        """
        Copy rule comment
        Get: Comment(self: CopyRule) -> str
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether copy rule is selected
        Get: Enabled(self: CopyRule) -> bool
        """
        ...

    @property
    def Name(self) -> str:
        """
        Copy rule name
        Get: Name(self: CopyRule) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: CopyRule) -> IEngineeringObject
        """
        ...


    def Delete(self): # -> 
        """
        Delete(self: CopyRule)
            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CopyRule) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CopyRule) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CopyRuleComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Collection of immediate copy rules """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: CopyRuleComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, ruleMasterCopy:MasterCopy, createOption:CreateOptions = ...) -> CopyRule:
        """
        CreateFrom(self: CopyRuleComposition, ruleMasterCopy: MasterCopy) -> CopyRule
            Copy the copy rule from library to project with default replace option
            ruleMasterCopy: Copy rule master copy
            Returns: Siemens.Engineering.SiVArc.CopyRule
        CreateFrom(self: CopyRuleComposition, ruleMasterCopy: MasterCopy, createOption: CreateOptions) -> CopyRule
            Copy the copy rule from library to project with create options
            ruleMasterCopy: Copy rule master copy
            createOption: Create option
            Returns: Siemens.Engineering.SiVArc.CopyRule
        """
        ...

    def Find(self, name:str) -> CopyRule:
        """
        Find(self: CopyRuleComposition, name: str) -> CopyRule
            Finds copy rule based on name
            name: Copy rule name
            Returns: Siemens.Engineering.SiVArc.CopyRule
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CopyRuleComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CopyRuleComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CopyRule](enumerable: IEnumerable[CopyRule], value: CopyRule) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CopyRuleGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents copy rule group """
    @property
    def Comment(self) -> str:
        """
        Copy rule group comment
        Get: Comment(self: CopyRuleGroup) -> str
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether copy rule group is selected
        Get: Enabled(self: CopyRuleGroup) -> bool
        """
        ...

    @property
    def Groups(self) -> CopyRuleGroupComposition:
        """
        Collection of immediate groups
        Get: Groups(self: CopyRuleGroup) -> CopyRuleGroupComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        Copy rule group name
        Get: Name(self: CopyRuleGroup) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: CopyRuleGroup) -> IEngineeringObject
        """
        ...

    @property
    def Rules(self) -> CopyRuleComposition:
        """
        Collection of immediate rules
        Get: Rules(self: CopyRuleGroup) -> CopyRuleComposition
        """
        ...


    def Delete(self): # -> 
        """
        Delete(self: CopyRuleGroup)
            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CopyRuleGroup) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CopyRuleGroup) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CopyRuleGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Collection of immediate copy rule groups """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: CopyRuleGroupComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, groupMasterCopy:MasterCopy, createOption:CreateOptions = ...) -> CopyRuleGroup:
        """
        CreateFrom(self: CopyRuleGroupComposition, groupMasterCopy: MasterCopy) -> CopyRuleGroup
            Copy the copy rule group from library to project with default replace option
            groupMasterCopy: Copy rule group master copy
            Returns: Siemens.Engineering.SiVArc.CopyRuleGroup
        CreateFrom(self: CopyRuleGroupComposition, groupMasterCopy: MasterCopy, createOption: CreateOptions) -> CopyRuleGroup
            Copy the copy rule group from library to project with create options
            groupMasterCopy: Copy rule group master copy
            createOption: Create option
            Returns: Siemens.Engineering.SiVArc.CopyRuleGroup
        """
        ...

    def Find(self, name:str) -> CopyRuleGroup:
        """
        Find(self: CopyRuleGroupComposition, name: str) -> CopyRuleGroup
            Finds copy rule group based on name
            name: Copy rule group name
            Returns: Siemens.Engineering.SiVArc.CopyRuleGroup
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CopyRuleGroupComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CopyRuleGroupComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CopyRuleGroup](enumerable: IEnumerable[CopyRuleGroup], value: CopyRuleGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CopyRules(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents copy rules editor """
    @property
    def Groups(self) -> CopyRuleGroupComposition:
        """
        Navigate to all immediate copy rule groups
        Get: Groups(self: CopyRules) -> CopyRuleGroupComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: CopyRules) -> IEngineeringObject
        """
        ...

    @property
    def Rules(self) -> CopyRuleComposition:
        """
        Navigate to all immediate copy rules
        Get: Rules(self: CopyRules) -> CopyRuleComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CopyRules) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CopyRules) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CreateOptions(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Indicates the kind of create options
    enum CreateOptions, values: Rename (1), Replace (0)
    """
    Rename: CreateOptions = ...
    Replace: CreateOptions = ...
    value__ = ...


class GenerationOptions(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Indicates the kind of generation options
    enum (flags) GenerationOptions, values: AllTags (1), FullGeneration (4), None (0), UsedHmiTags (2)
    """
    AllTags: GenerationOptions = ...
    FullGeneration: GenerationOptions = ...
    UsedHmiTags: GenerationOptions = ...
    value__ = ...


class MessageType(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Message type
    enum MessageType, values: Error (0), Information (2), Warning (1)
    """
    Error: MessageType = ...
    Information: MessageType = ...
    value__ = ...
    Warning: MessageType = ...


class ScreenRule(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents screen rule object """
    @property
    def Comment(self) -> str:
        """
        Screen rule comment
        Get: Comment(self: ScreenRule) -> str
        Set: Comment(self: ScreenRule) = value
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Screen rule condition
        Get: Condition(self: ScreenRule) -> str
        Set: Condition(self: ScreenRule) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether screen rule is selected
        Get: Enabled(self: ScreenRule) -> bool
        Set: Enabled(self: ScreenRule) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Screen rule name
        Get: Name(self: ScreenRule) -> str
        Set: Name(self: ScreenRule) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: ScreenRule) -> IEngineeringObject
        """
        ...


    def Delete(self): # -> 
        """
        Delete(self: ScreenRule)
            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenRule) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenRule) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenRuleComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Collection of immediate screen rules """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: ScreenRuleComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, ruleMasterCopy:MasterCopy, createOption:CreateOptions = ...) -> ScreenRule:
        """
        CreateFrom(self: ScreenRuleComposition, ruleMasterCopy: MasterCopy) -> ScreenRule
            Copy screen rule from library to project with default replace option
            ruleMasterCopy: Screen rule master copy
            Returns: Siemens.Engineering.SiVArc.ScreenRule
        CreateFrom(self: ScreenRuleComposition, ruleMasterCopy: MasterCopy, createOption: CreateOptions) -> ScreenRule
            Copy screen rule from library to project with create options
            ruleMasterCopy: Screen rule master copy
            createOption: Create option
            Returns: Siemens.Engineering.SiVArc.ScreenRule
        """
        ...

    def Find(self, name:str) -> ScreenRule:
        """
        Find(self: ScreenRuleComposition, name: str) -> ScreenRule
            Finds screen rule based on name
            name: Screen rule name
            Returns: Siemens.Engineering.SiVArc.ScreenRule
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenRuleComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenRuleComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ScreenRule](enumerable: IEnumerable[ScreenRule], value: ScreenRule) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenRuleGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents screen rule group """
    @property
    def Comment(self) -> str:
        """
        Screen rule group comment
        Get: Comment(self: ScreenRuleGroup) -> str
        Set: Comment(self: ScreenRuleGroup) = value
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Screen rule group condition
        Get: Condition(self: ScreenRuleGroup) -> str
        Set: Condition(self: ScreenRuleGroup) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether screen rule group is selected
        Get: Enabled(self: ScreenRuleGroup) -> bool
        Set: Enabled(self: ScreenRuleGroup) = value
        """
        ...

    @property
    def Groups(self) -> ScreenRuleGroupComposition:
        """
        Collection of immediate groups
        Get: Groups(self: ScreenRuleGroup) -> ScreenRuleGroupComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        Screen rule group name
        Get: Name(self: ScreenRuleGroup) -> str
        Set: Name(self: ScreenRuleGroup) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: ScreenRuleGroup) -> IEngineeringObject
        """
        ...

    @property
    def Rules(self) -> ScreenRuleComposition:
        """
        Collection of immediate rules
        Get: Rules(self: ScreenRuleGroup) -> ScreenRuleComposition
        """
        ...


    def Delete(self): # -> 
        """
        Delete(self: ScreenRuleGroup)
            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenRuleGroup) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenRuleGroup) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenRuleGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Collection of immediate screen rule groups """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: ScreenRuleGroupComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, groupMasterCopy:MasterCopy, createOption:CreateOptions = ...) -> ScreenRuleGroup:
        """
        CreateFrom(self: ScreenRuleGroupComposition, groupMasterCopy: MasterCopy) -> ScreenRuleGroup
            Copy screen rule group from library to project with default replace option
            groupMasterCopy: Screen rule group master copy
            Returns: Siemens.Engineering.SiVArc.ScreenRuleGroup
        CreateFrom(self: ScreenRuleGroupComposition, groupMasterCopy: MasterCopy, createOption: CreateOptions) -> ScreenRuleGroup
            Copy screen rule group from library to project with create options
            groupMasterCopy: Screen rule group master copy
            createOption: Create option
            Returns: Siemens.Engineering.SiVArc.ScreenRuleGroup
        """
        ...

    def Find(self, name:str) -> ScreenRuleGroup:
        """
        Find(self: ScreenRuleGroupComposition, name: str) -> ScreenRuleGroup
            Finds screen rule group based on name
            name: Screen rule group name
            Returns: Siemens.Engineering.SiVArc.ScreenRuleGroup
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenRuleGroupComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenRuleGroupComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ScreenRuleGroup](enumerable: IEnumerable[ScreenRuleGroup], value: ScreenRuleGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenRules(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents screen rules editor """
    @property
    def Groups(self) -> ScreenRuleGroupComposition:
        """
        Navigate to all immediate screen rule groups
        Get: Groups(self: ScreenRules) -> ScreenRuleGroupComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: ScreenRules) -> IEngineeringObject
        """
        ...

    @property
    def Rules(self) -> ScreenRuleComposition:
        """
        Navigate to all immediate screen rules
        Get: Rules(self: ScreenRules) -> ScreenRuleComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenRules) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenRules) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Sivarc(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents SiVArc folder """
    @property
    def AlarmRules(self) -> AlarmRules:
        """
        Alarm rules editor
        Get: AlarmRules(self: Sivarc) -> AlarmRules
        """
        ...

    @property
    def CopyRules(self) -> CopyRules:
        """
        Copy rules editor
        Get: CopyRules(self: Sivarc) -> CopyRules
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: Sivarc) -> IEngineeringObject
        """
        ...

    @property
    def ScreenRules(self) -> ScreenRules:
        """
        Screen rules editor
        Get: ScreenRules(self: Sivarc) -> ScreenRules
        """
        ...

    @property
    def TagRules(self) -> TagRules:
        """
        Tag rules editor
        Get: TagRules(self: Sivarc) -> TagRules
        """
        ...

    @property
    def TextlistRules(self) -> TextlistRules:
        """
        Textlist rules editor
        Get: TextlistRules(self: Sivarc) -> TextlistRules
        """
        ...


    def Generate(self, deviceName:str, plcs:IEnumerable, generationOptions:GenerationOptions) -> SivarcGenerationResult:
        """ Generate(self: Sivarc, deviceName: str, plcs: IEnumerable[str], generationOptions: GenerationOptions) -> SivarcGenerationResult """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: Sivarc) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: Sivarc) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SivarcFeedbackMessage(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Generation result message """
    @property
    def DateTime(self) -> DateTime:
        """
        Date and time for generation message
        Get: DateTime(self: SivarcFeedbackMessage) -> DateTime
        """
        ...

    @property
    def Description(self) -> str:
        """
        Description of a generation message
        Get: Description(self: SivarcFeedbackMessage) -> str
        """
        ...

    @property
    def ErrorCount(self) -> int:
        """
        Number of errors of generation message
        Get: ErrorCount(self: SivarcFeedbackMessage) -> int
        """
        ...

    @property
    def Messages(self) -> SivarcFeedbackMessageComposition:
        """
        Access to the child messages for a given scenario
        Get: Messages(self: SivarcFeedbackMessage) -> SivarcFeedbackMessageComposition
        """
        ...

    @property
    def MessageType(self) -> MessageType:
        """
        Message type of a generation message
        Get: MessageType(self: SivarcFeedbackMessage) -> MessageType
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: SivarcFeedbackMessage) -> IEngineeringObject
        """
        ...

    @property
    def Path(self) -> str:
        """
        Path to a generation message
        Get: Path(self: SivarcFeedbackMessage) -> str
        """
        ...

    @property
    def WarningCount(self) -> int:
        """
        Number of warnings of generation message
        Get: WarningCount(self: SivarcFeedbackMessage) -> int
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SivarcFeedbackMessage) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SivarcFeedbackMessage) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SivarcFeedbackMessageComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of GeneratedResultMessages """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: SivarcFeedbackMessageComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SivarcFeedbackMessageComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SivarcFeedbackMessageComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SivarcFeedbackMessage](enumerable: IEnumerable[SivarcFeedbackMessage], value: SivarcFeedbackMessage) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SivarcGenerationResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Sivarc generation result """
    @property
    def ErrorCount(self) -> int:
        """
        Error count
        Get: ErrorCount(self: SivarcGenerationResult) -> int
        """
        ...

    @property
    def IsGenerationSuccessful(self) -> bool:
        """
        Checks whether generation is successful or not
        Get: IsGenerationSuccessful(self: SivarcGenerationResult) -> bool
        """
        ...

    @property
    def Messages(self) -> SivarcFeedbackMessageComposition:
        """
        Collection of messages
        Get: Messages(self: SivarcGenerationResult) -> SivarcFeedbackMessageComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: SivarcGenerationResult) -> IEngineeringObject
        """
        ...

    @property
    def WarningCount(self) -> int:
        """
        Warning Count
        Get: WarningCount(self: SivarcGenerationResult) -> int
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SivarcGenerationResult) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SivarcGenerationResult) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TagRule(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents tag rule object """
    @property
    def Comment(self) -> str:
        """
        Tag rule comment
        Get: Comment(self: TagRule) -> str
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Tag rule condition
        Get: Condition(self: TagRule) -> str
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether tag rule is selected
        Get: Enabled(self: TagRule) -> bool
        """
        ...

    @property
    def Name(self) -> str:
        """
        Tag rule name
        Get: Name(self: TagRule) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: TagRule) -> IEngineeringObject
        """
        ...


    def Delete(self): # -> 
        """
        Delete(self: TagRule)
            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TagRule) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TagRule) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TagRuleComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Collection of immediate tag rules """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: TagRuleComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, ruleMasterCopy:MasterCopy, createOption:CreateOptions = ...) -> TagRule:
        """
        CreateFrom(self: TagRuleComposition, ruleMasterCopy: MasterCopy) -> TagRule
            Copy tag rule from library to project with default replace option
            ruleMasterCopy: Tag rule master copy
            Returns: Siemens.Engineering.SiVArc.TagRule
        CreateFrom(self: TagRuleComposition, ruleMasterCopy: MasterCopy, createOption: CreateOptions) -> TagRule
            Copy tag rule from library to project with create options
            ruleMasterCopy: Tag rule master copy
            createOption: Create option
            Returns: Siemens.Engineering.SiVArc.TagRule
        """
        ...

    def Find(self, name:str) -> TagRule:
        """
        Find(self: TagRuleComposition, name: str) -> TagRule
            Finds tag rule based on name
            name: Tag rule name
            Returns: Siemens.Engineering.SiVArc.TagRule
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TagRuleComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TagRuleComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TagRule](enumerable: IEnumerable[TagRule], value: TagRule) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TagRuleGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents tag rule group """
    @property
    def Comment(self) -> str:
        """
        Tag rule group comment
        Get: Comment(self: TagRuleGroup) -> str
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Tag rule group condition
        Get: Condition(self: TagRuleGroup) -> str
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether tag rule group is selected
        Get: Enabled(self: TagRuleGroup) -> bool
        """
        ...

    @property
    def Groups(self) -> TagRuleGroupComposition:
        """
        Collection of immediate groups
        Get: Groups(self: TagRuleGroup) -> TagRuleGroupComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        Tag rule group name
        Get: Name(self: TagRuleGroup) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: TagRuleGroup) -> IEngineeringObject
        """
        ...

    @property
    def Rules(self) -> TagRuleComposition:
        """
        Collection of immediate rules
        Get: Rules(self: TagRuleGroup) -> TagRuleComposition
        """
        ...


    def Delete(self): # -> 
        """
        Delete(self: TagRuleGroup)
            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TagRuleGroup) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TagRuleGroup) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TagRuleGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Collection of immediate tag rule groups """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: TagRuleGroupComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, groupMasterCopy:MasterCopy, createOption:CreateOptions = ...) -> TagRuleGroup:
        """
        CreateFrom(self: TagRuleGroupComposition, groupMasterCopy: MasterCopy) -> TagRuleGroup
            Copy tag rule group from library to project with default replace option
            groupMasterCopy: Tag rule group master copy
            Returns: Siemens.Engineering.SiVArc.TagRuleGroup
        CreateFrom(self: TagRuleGroupComposition, groupMasterCopy: MasterCopy, createOption: CreateOptions) -> TagRuleGroup
            Copy tag rule group from library to project with create options
            groupMasterCopy: Tag rule group master copy
            createOption: Create option
            Returns: Siemens.Engineering.SiVArc.TagRuleGroup
        """
        ...

    def Find(self, name:str) -> TagRuleGroup:
        """
        Find(self: TagRuleGroupComposition, name: str) -> TagRuleGroup
            Finds tag rule group based on name
            name: Tag rule group name
            Returns: Siemens.Engineering.SiVArc.TagRuleGroup
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TagRuleGroupComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TagRuleGroupComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TagRuleGroup](enumerable: IEnumerable[TagRuleGroup], value: TagRuleGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TagRules(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents tag rules editor """
    @property
    def Groups(self) -> TagRuleGroupComposition:
        """
        Navigate to all immediate tag rule groups
        Get: Groups(self: TagRules) -> TagRuleGroupComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: TagRules) -> IEngineeringObject
        """
        ...

    @property
    def Rules(self) -> TagRuleComposition:
        """
        Navigate to all immediate tag rules
        Get: Rules(self: TagRules) -> TagRuleComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TagRules) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TagRules) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TextlistRule(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents textlist rule object """
    @property
    def Comment(self) -> str:
        """
        Textlist rule comment
        Get: Comment(self: TextlistRule) -> str
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Textlist rule condition
        Get: Condition(self: TextlistRule) -> str
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether textlist rule is selected
        Get: Enabled(self: TextlistRule) -> bool
        """
        ...

    @property
    def Name(self) -> str:
        """
        Textlist rule name
        Get: Name(self: TextlistRule) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: TextlistRule) -> IEngineeringObject
        """
        ...


    def Delete(self): # -> 
        """
        Delete(self: TextlistRule)
            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TextlistRule) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TextlistRule) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TextlistRuleComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Collection of immediate textlist rules """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: TextlistRuleComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, ruleMasterCopy:MasterCopy, createOption:CreateOptions = ...) -> TextlistRule:
        """
        CreateFrom(self: TextlistRuleComposition, ruleMasterCopy: MasterCopy) -> TextlistRule
            Copy textlist rule from library to project with default replace option
            ruleMasterCopy: Textlist rule master copy
            Returns: Siemens.Engineering.SiVArc.TextlistRule
        CreateFrom(self: TextlistRuleComposition, ruleMasterCopy: MasterCopy, createOption: CreateOptions) -> TextlistRule
            Copy textlist rule from library to project with create options
            ruleMasterCopy: Textlist rule master copy
            createOption: Create option
            Returns: Siemens.Engineering.SiVArc.TextlistRule
        """
        ...

    def Find(self, name:str) -> TextlistRule:
        """
        Find(self: TextlistRuleComposition, name: str) -> TextlistRule
            Finds textlist rule based on name
            name: Textlist rule name
            Returns: Siemens.Engineering.SiVArc.TextlistRule
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TextlistRuleComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TextlistRuleComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TextlistRule](enumerable: IEnumerable[TextlistRule], value: TextlistRule) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TextlistRuleGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents textlist rule group """
    @property
    def Comment(self) -> str:
        """
        Textlist rule group comment
        Get: Comment(self: TextlistRuleGroup) -> str
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Textlist rule group condition
        Get: Condition(self: TextlistRuleGroup) -> str
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether textlist rule group is selected
        Get: Enabled(self: TextlistRuleGroup) -> bool
        """
        ...

    @property
    def Groups(self) -> TextlistRuleGroupComposition:
        """
        Collection of immediate groups
        Get: Groups(self: TextlistRuleGroup) -> TextlistRuleGroupComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        Textlist rule group name
        Get: Name(self: TextlistRuleGroup) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: TextlistRuleGroup) -> IEngineeringObject
        """
        ...

    @property
    def Rules(self) -> TextlistRuleComposition:
        """
        Collection of immediate rules
        Get: Rules(self: TextlistRuleGroup) -> TextlistRuleComposition
        """
        ...


    def Delete(self): # -> 
        """
        Delete(self: TextlistRuleGroup)
            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TextlistRuleGroup) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TextlistRuleGroup) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TextlistRuleGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Collection of immediate textlist rule groups """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: TextlistRuleGroupComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, groupMasterCopy:MasterCopy, createOption:CreateOptions = ...) -> TextlistRuleGroup:
        """
        CreateFrom(self: TextlistRuleGroupComposition, groupMasterCopy: MasterCopy) -> TextlistRuleGroup
            Copy textlist rule group from library to project with default replace option
            groupMasterCopy: Textlist rule group master copy
            Returns: Siemens.Engineering.SiVArc.TextlistRuleGroup
        CreateFrom(self: TextlistRuleGroupComposition, groupMasterCopy: MasterCopy, createOption: CreateOptions) -> TextlistRuleGroup
            Copy textlist rule group from library to project with create options
            groupMasterCopy: Textlist rule group master copy
            createOption: Create option
            Returns: Siemens.Engineering.SiVArc.TextlistRuleGroup
        """
        ...

    def Find(self, name:str) -> TextlistRuleGroup:
        """
        Find(self: TextlistRuleGroupComposition, name: str) -> TextlistRuleGroup
            Finds textlist rule group based on name
            name: Textlist rule group name
            Returns: Siemens.Engineering.SiVArc.TextlistRuleGroup
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TextlistRuleGroupComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TextlistRuleGroupComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TextlistRuleGroup](enumerable: IEnumerable[TextlistRuleGroup], value: TextlistRuleGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TextlistRules(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents textlist rules editor """
    @property
    def Groups(self) -> TextlistRuleGroupComposition:
        """
        Navigate to all immediate textlist rule groups
        Get: Groups(self: TextlistRules) -> TextlistRuleGroupComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: TextlistRules) -> IEngineeringObject
        """
        ...

    @property
    def Rules(self) -> TextlistRuleComposition:
        """
        Navigate to all immediate textlist rules
        Get: Rules(self: TextlistRules) -> TextlistRuleComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TextlistRules) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TextlistRules) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


