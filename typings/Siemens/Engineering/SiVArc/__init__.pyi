# encoding: utf-8
# module Siemens.Engineering.SiVArc calls itself SiVArc
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringComposition, IEngineeringObject,
    IEngineeringService, MultilingualText)

from Siemens.Engineering.Library.MasterCopies import MasterCopy

from System import DateTime, Enum, IEquatable

from System.Collections import IEnumerable

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class AlarmRule(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents alarm rule object """
    @property
    def AlarmLibraryItem(self) -> ISivarcLibraryMasterCopy:
        """
        Alarm library item

        Get: AlarmLibraryItem(self: AlarmRule) -> ISivarcLibraryMasterCopy

        Set: AlarmLibraryItem(self: AlarmRule) = value
        """
        ...

    @property
    def Comment(self) -> str:
        """
        Alarm rule comment

        Get: Comment(self: AlarmRule) -> str

        Set: Comment(self: AlarmRule) = value
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Alarm rule condition

        Get: Condition(self: AlarmRule) -> str

        Set: Condition(self: AlarmRule) = value
        """
        ...

    @property
    def ConditionOperator(self) -> ConditionOperator:
        """
        Condition Operator for rule object

        Get: ConditionOperator(self: AlarmRule) -> ConditionOperator

        Set: ConditionOperator(self: AlarmRule) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether alarm rule is selected

        Get: Enabled(self: AlarmRule) -> bool

        Set: Enabled(self: AlarmRule) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Alarm rule name

        Get: Name(self: AlarmRule) -> str

        Set: Name(self: AlarmRule) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: AlarmRule) -> IEngineeringObject
        """
        ...

    @property
    def ProgramBlock(self) -> ISivarcProgramBlockSource:
        """
        Alarm rule program block

        Get: ProgramBlock(self: AlarmRule) -> ISivarcProgramBlockSource

        Set: ProgramBlock(self: AlarmRule) = value
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


class AlarmRuleComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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


class AlarmRuleGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents alarm rule group """
    @property
    def Comment(self) -> str:
        """
        Alarm rule group comment

        Get: Comment(self: AlarmRuleGroup) -> str

        Set: Comment(self: AlarmRuleGroup) = value
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Alarm rule group condition

        Get: Condition(self: AlarmRuleGroup) -> str

        Set: Condition(self: AlarmRuleGroup) = value
        """
        ...

    @property
    def ConditionOperator(self) -> ConditionOperator:
        """
        Condition operator for rule group object

        Get: ConditionOperator(self: AlarmRuleGroup) -> ConditionOperator

        Set: ConditionOperator(self: AlarmRuleGroup) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether alarm rule group is selected

        Get: Enabled(self: AlarmRuleGroup) -> bool

        Set: Enabled(self: AlarmRuleGroup) = value
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

        Set: Name(self: AlarmRuleGroup) = value
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


class AlarmRuleGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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


class AlarmRules(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
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


class ConditionOperator(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Condition Operator for rule objects

    enum ConditionOperator, values: And (1), Equal (2), GreaterThan (4), GreaterThanOrEqual (5), LessThan (6), LessThanOrEqual (7), None (0), NotEqual (3)
    """
    And: ConditionOperator = ...
    Equal: ConditionOperator = ...
    GreaterThan: ConditionOperator = ...
    GreaterThanOrEqual: ConditionOperator = ...
    LessThan: ConditionOperator = ...
    LessThanOrEqual: ConditionOperator = ...
    NotEqual: ConditionOperator = ...
    value__ = ...


class CopyRule(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents copy rule object """
    @property
    def Comment(self) -> str:
        """
        Copy rule comment

        Get: Comment(self: CopyRule) -> str

        Set: Comment(self: CopyRule) = value
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Copy rule condition

        Get: Condition(self: CopyRule) -> str

        Set: Condition(self: CopyRule) = value
        """
        ...

    @property
    def ConditionOperator(self) -> ConditionOperator:
        """
        Condition Operator for rule object

        Get: ConditionOperator(self: CopyRule) -> ConditionOperator

        Set: ConditionOperator(self: CopyRule) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether copy rule is selected

        Get: Enabled(self: CopyRule) -> bool

        Set: Enabled(self: CopyRule) = value
        """
        ...

    @property
    def FolderStructure(self) -> str:
        """
        Name of generated folder structure

        Get: FolderStructure(self: CopyRule) -> str

        Set: FolderStructure(self: CopyRule) = value
        """
        ...

    @property
    def LibraryObject(self) -> ISivarcLibraryItem:
        """
        Copy rule library object

        Get: LibraryObject(self: CopyRule) -> ISivarcLibraryItem

        Set: LibraryObject(self: CopyRule) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Copy rule name

        Get: Name(self: CopyRule) -> str

        Set: Name(self: CopyRule) = value
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


class CopyRuleComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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


class CopyRuleGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents copy rule group """
    @property
    def Comment(self) -> str:
        """
        Copy rule group comment

        Get: Comment(self: CopyRuleGroup) -> str

        Set: Comment(self: CopyRuleGroup) = value
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Copy rule group condition

        Get: Condition(self: CopyRuleGroup) -> str

        Set: Condition(self: CopyRuleGroup) = value
        """
        ...

    @property
    def ConditionOperator(self) -> ConditionOperator:
        """
        Condition Operator for rule object

        Get: ConditionOperator(self: CopyRuleGroup) -> ConditionOperator

        Set: ConditionOperator(self: CopyRuleGroup) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether copy rule group is selected

        Get: Enabled(self: CopyRuleGroup) -> bool

        Set: Enabled(self: CopyRuleGroup) = value
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

        Set: Name(self: CopyRuleGroup) = value
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


class CopyRuleGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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


class CopyRules(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
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


class CreateOptions(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Indicates the kind of create options

    enum CreateOptions, values: Rename (1), Replace (0)
    """
    Rename: CreateOptions = ...
    Replace: CreateOptions = ...
    value__ = ...


class GenerationOptions(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Indicates the kind of generation options

    enum (flags) GenerationOptions, values: AllTags (1), FullGeneration (4), None (0), UsedHmiTags (2)
    """
    AllTags: GenerationOptions = ...
    FullGeneration: GenerationOptions = ...
    UsedHmiTags: GenerationOptions = ...
    value__ = ...


class ISivarcLibraryItem: # skipped bases: <type 'object'>
    """ Sivarc interface implemented by library master copy and type """
    pass

class ISivarcLibraryMasterCopy: # skipped bases: <type 'object'>
    """ Sivarc interface implemented by library master copy """
    pass

class ISivarcProgramBlockSource: # skipped bases: <type 'object'>
    """ Sivarc interface implemented by code block, library master copy and type """
    pass

class MessageType(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Message type

    enum MessageType, values: Error (0), Information (2), Warning (1)
    """
    Error: MessageType = ...
    Information: MessageType = ...
    value__ = ...
    Warning: MessageType = ...


class ScreenRule(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
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
    def ConditionOperator(self) -> ConditionOperator:
        """
        Condition Operator for rule object

        Get: ConditionOperator(self: ScreenRule) -> ConditionOperator

        Set: ConditionOperator(self: ScreenRule) = value
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
    def LayoutField(self) -> str:
        """
        Layout field of Screen rule

        Get: LayoutField(self: ScreenRule) -> str

        Set: LayoutField(self: ScreenRule) = value
        """
        ...

    @property
    def LibraryScreen(self) -> ISivarcLibraryItem:
        """
        Screen master copy or screen type

        Get: LibraryScreen(self: ScreenRule) -> ISivarcLibraryItem

        Set: LibraryScreen(self: ScreenRule) = value
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

    @property
    def ProgramBlock(self) -> ISivarcProgramBlockSource:
        """
        Screen rule program block

        Get: ProgramBlock(self: ScreenRule) -> ISivarcProgramBlockSource

        Set: ProgramBlock(self: ScreenRule) = value
        """
        ...

    @property
    def ScreenLibraryItem(self) -> ISivarcLibraryMasterCopy:
        """
        Screen master copy

        Get: ScreenLibraryItem(self: ScreenRule) -> ISivarcLibraryMasterCopy

        Set: ScreenLibraryItem(self: ScreenRule) = value
        """
        ...

    @property
    def ScreenObjectLibraryItem(self) -> ISivarcLibraryItem:
        """
        Screen object library item

        Get: ScreenObjectLibraryItem(self: ScreenRule) -> ISivarcLibraryItem

        Set: ScreenObjectLibraryItem(self: ScreenRule) = value
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

    def GetLayoutFields(self) -> IEnumerable:
        """
        GetLayoutFields(self: ScreenRule) -> IEnumerable[str]

            Get all layout fields applicable for the rule

            Returns: System.Collections.Generic.IEnumerable<System.String>
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


class ScreenRuleComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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


class ScreenRuleGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
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
    def ConditionOperator(self) -> ConditionOperator:
        """
        Condition operator for rule group object

        Get: ConditionOperator(self: ScreenRuleGroup) -> ConditionOperator

        Set: ConditionOperator(self: ScreenRuleGroup) = value
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


class ScreenRuleGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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


class ScreenRules(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
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


class Sivarc(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
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


    def Generate(self, *__args) -> SivarcGenerationResult:
        """
        Generate(self: Sivarc, devices: IEnumerable[str], plcs: IEnumerable[str], generationOptions: GenerationOptions) -> SivarcGenerationResult

        Generate(self: Sivarc, deviceName: str, plcs: IEnumerable[str], generationOptions: GenerationOptions) -> SivarcGenerationResult
        """
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


class SivarcDataProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Sivarc data provider for blocks and compile units """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SivarcDataProvider) -> IEngineeringObject
        """
        ...

    @property
    def TagDefinitions(self) -> TagDefinitionComposition:
        """
        Collection of user defined tag definitions

        Get: TagDefinitions(self: SivarcDataProvider) -> TagDefinitionComposition
        """
        ...

    @property
    def TextDefinitions(self) -> TextDefinitionComposition:
        """
        Collection of user defined text definitions

        Get: TextDefinitions(self: SivarcDataProvider) -> TextDefinitionComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SivarcDataProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SivarcDataProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SivarcFeedbackMessage(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
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


class SivarcFeedbackMessageComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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


class SivarcGenerationResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
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


class TagDefinition(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ User defined tag definition """
    @property
    def Comment(self) -> str:
        """
        Tag definition comment

        Get: Comment(self: TagDefinition) -> str

        Set: Comment(self: TagDefinition) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Tag definition name

        Get: Name(self: TagDefinition) -> str

        Set: Name(self: TagDefinition) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: TagDefinition) -> IEngineeringObject
        """
        ...

    @property
    def Value(self) -> str:
        """
        Tag definition value

        Get: Value(self: TagDefinition) -> str

        Set: Value(self: TagDefinition) = value
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: TagDefinition)

            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TagDefinition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TagDefinition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TagDefinitionComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Collection of user defined tag definitions """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: TagDefinitionComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> TagDefinition:
        """
        Find(self: TagDefinitionComposition, name: str) -> TagDefinition

            Find the tag definition for provided name

            name: Tag definition name

            Returns: Siemens.Engineering.SiVArc.TagDefinition
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TagDefinitionComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TagDefinitionComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TagDefinition](enumerable: IEnumerable[TagDefinition], value: TagDefinition) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TagRule(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents tag rule object """
    @property
    def Comment(self) -> str:
        """
        Tag rule comment

        Get: Comment(self: TagRule) -> str

        Set: Comment(self: TagRule) = value
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Tag rule condition

        Get: Condition(self: TagRule) -> str

        Set: Condition(self: TagRule) = value
        """
        ...

    @property
    def ConditionOperator(self) -> ConditionOperator:
        """
        Condition Operator for rule object

        Get: ConditionOperator(self: TagRule) -> ConditionOperator

        Set: ConditionOperator(self: TagRule) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether tag rule is selected

        Get: Enabled(self: TagRule) -> bool

        Set: Enabled(self: TagRule) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Tag rule name

        Get: Name(self: TagRule) -> str

        Set: Name(self: TagRule) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: TagRule) -> IEngineeringObject
        """
        ...

    @property
    def TagGroupHierarchy(self) -> str:
        """
        Tag group hierarchy expression

        Get: TagGroupHierarchy(self: TagRule) -> str

        Set: TagGroupHierarchy(self: TagRule) = value
        """
        ...

    @property
    def TagTable(self) -> str:
        """
        Tag table expression

        Get: TagTable(self: TagRule) -> str

        Set: TagTable(self: TagRule) = value
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


class TagRuleComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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


class TagRuleGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents tag rule group """
    @property
    def Comment(self) -> str:
        """
        Tag rule group comment

        Get: Comment(self: TagRuleGroup) -> str

        Set: Comment(self: TagRuleGroup) = value
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Tag rule group condition

        Get: Condition(self: TagRuleGroup) -> str

        Set: Condition(self: TagRuleGroup) = value
        """
        ...

    @property
    def ConditionOperator(self) -> ConditionOperator:
        """
        Condition operator for rule group object

        Get: ConditionOperator(self: TagRuleGroup) -> ConditionOperator

        Set: ConditionOperator(self: TagRuleGroup) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether tag rule group is selected

        Get: Enabled(self: TagRuleGroup) -> bool

        Set: Enabled(self: TagRuleGroup) = value
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

        Set: Name(self: TagRuleGroup) = value
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


class TagRuleGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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


class TagRules(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
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


class TextDefinition(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ User defined text definition """
    @property
    def Comment(self) -> str:
        """
        Text definition comment

        Get: Comment(self: TextDefinition) -> str

        Set: Comment(self: TextDefinition) = value
        """
        ...

    @property
    def Expression(self) -> str:
        """
        Text definition expression

        Get: Expression(self: TextDefinition) -> str

        Set: Expression(self: TextDefinition) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Text definition name

        Get: Name(self: TextDefinition) -> str

        Set: Name(self: TextDefinition) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: TextDefinition) -> IEngineeringObject
        """
        ...

    @property
    def Text(self) -> MultilingualText:
        """
        Text definition text

        Get: Text(self: TextDefinition) -> MultilingualText
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: TextDefinition)

            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TextDefinition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TextDefinition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TextDefinitionComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Collection of user defined text definitions """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: TextDefinitionComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> TextDefinition:
        """
        Find(self: TextDefinitionComposition, name: str) -> TextDefinition

            Find the text definition for provided name

            name: Text definition name

            Returns: Siemens.Engineering.SiVArc.TextDefinition
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TextDefinitionComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TextDefinitionComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TextDefinition](enumerable: IEnumerable[TextDefinition], value: TextDefinition) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TextlistRule(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents textlist rule object """
    @property
    def Comment(self) -> str:
        """
        Textlist rule comment

        Get: Comment(self: TextlistRule) -> str

        Set: Comment(self: TextlistRule) = value
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Textlist rule condition

        Get: Condition(self: TextlistRule) -> str

        Set: Condition(self: TextlistRule) = value
        """
        ...

    @property
    def ConditionOperator(self) -> ConditionOperator:
        """
        Condition Operator for rule object

        Get: ConditionOperator(self: TextlistRule) -> ConditionOperator

        Set: ConditionOperator(self: TextlistRule) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether textlist rule is selected

        Get: Enabled(self: TextlistRule) -> bool

        Set: Enabled(self: TextlistRule) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Textlist rule name

        Get: Name(self: TextlistRule) -> str

        Set: Name(self: TextlistRule) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: TextlistRule) -> IEngineeringObject
        """
        ...

    @property
    def ProgramBlock(self) -> ISivarcProgramBlockSource:
        """
        Textlist rule program block

        Get: ProgramBlock(self: TextlistRule) -> ISivarcProgramBlockSource

        Set: ProgramBlock(self: TextlistRule) = value
        """
        ...

    @property
    def TextlistLibraryItem(self) -> ISivarcLibraryMasterCopy:
        """
        Textlist master copy

        Get: TextlistLibraryItem(self: TextlistRule) -> ISivarcLibraryMasterCopy

        Set: TextlistLibraryItem(self: TextlistRule) = value
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


class TextlistRuleComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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


class TextlistRuleGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents textlist rule group """
    @property
    def Comment(self) -> str:
        """
        Textlist rule group comment

        Get: Comment(self: TextlistRuleGroup) -> str

        Set: Comment(self: TextlistRuleGroup) = value
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Textlist rule group condition

        Get: Condition(self: TextlistRuleGroup) -> str

        Set: Condition(self: TextlistRuleGroup) = value
        """
        ...

    @property
    def ConditionOperator(self) -> ConditionOperator:
        """
        Condition operator for rule group object

        Get: ConditionOperator(self: TextlistRuleGroup) -> ConditionOperator

        Set: ConditionOperator(self: TextlistRuleGroup) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Checks whether textlist rule group is selected

        Get: Enabled(self: TextlistRuleGroup) -> bool

        Set: Enabled(self: TextlistRuleGroup) = value
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

        Set: Name(self: TextlistRuleGroup) = value
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


class TextlistRuleGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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


class TextlistRules(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
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
