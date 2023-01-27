# encoding: utf-8
# module Siemens.Engineering.SW.WatchAndForceTables calls itself WatchAndForceTables
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (ExportOptions, IEngineeringComposition,
    IEngineeringObject, IShowable, ImportOptions)

from Siemens.Engineering.Library.MasterCopies import MasterCopy

from System import Enum, IEquatable

from System.Collections import IList

from System.IO import FileInfo

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class PlcForceTable(IShowable, IEngineeringObject, IEquatable, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Plc force table """
    @property
    def Entries(self) -> PlcTableCommentEntryComposition:
        """
        Composition of ForceTable Entries

        Get: Entries(self: PlcForceTable) -> PlcTableCommentEntryComposition
        """
        ...

    @property
    def IsConsistent(self) -> bool:
        """
        Table is consistent or not

        Get: IsConsistent(self: PlcForceTable) -> bool
        """
        ...

    @property
    def Name(self) -> str:
        """
        Name of the ForceTable

        Get: Name(self: PlcForceTable) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: PlcForceTable) -> IEngineeringObject
        """
        ...


    def Export(self, path:FileInfo, exportOptions:ExportOptions): # ->
        """
        Export(self: PlcForceTable, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a Plc force table

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcForceTable) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcForceTable) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcForceTableComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of PlcForceTables """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: PlcForceTableComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> PlcForceTable:
        """
        Find(self: PlcForceTableComposition, name: str) -> PlcForceTable

            Find force table by name

            name: Name of the force table

            Returns: Siemens.Engineering.SW.WatchAndForceTables.PlcForceTable
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcForceTableComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path:FileInfo, importOptions:ImportOptions) -> IList:
        """
        Import(self: PlcForceTableComposition, path: FileInfo, importOptions: ImportOptions) -> IList[PlcForceTable]

            Import Plc force table from Simatic ML

            path: Path of the Simatic ML which will be imported

            importOptions: Options to use for import from Simatic ML

            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.WatchAndForceTables.PlcForceTable>
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcForceTableComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcForceTable](enumerable: IEnumerable[PlcForceTable], value: PlcForceTable) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcTableCommentEntry(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Plc Force\\Watch table comment entry """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: PlcTableCommentEntry) -> IEngineeringObject
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: PlcTableCommentEntry)

            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcTableCommentEntry) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcTableCommentEntry) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcForceTableEntry(PlcTableCommentEntry): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Plc force table entry """
    pass

class PlcTableCommentEntryComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Plc Force\\Watch table comment entries """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: PlcTableCommentEntryComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcTableCommentEntryComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcTableCommentEntryComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcTableCommentEntry](enumerable: IEnumerable[PlcTableCommentEntry], value: PlcTableCommentEntry) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcWatchAndForceTableDisplayFormat(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Enum for DisplayFormat

    enum PlcWatchAndForceTableDisplayFormat, values: Any_pointer (1), BCD (2), Bin (3), Block_number (13), Bool (4), Character (5), Character_sequence (6), Counter (17), Date (7), DATE_AND_TIME (8), DEC_sequence (9), DEC_signed (10), DEC_unsigned (11), Float (16), Hex (12), Octal (14), Pointer (15), SIMATIC_Time (18), String (19), Time (20), TIME_OF_DAY (21), Undef (0), Unicode_character (22), Unicode_character_sequence (23), Unicode_string (24)
    """
    Any_pointer: PlcWatchAndForceTableDisplayFormat = ...
    BCD: PlcWatchAndForceTableDisplayFormat = ...
    Bin: PlcWatchAndForceTableDisplayFormat = ...
    Block_number: PlcWatchAndForceTableDisplayFormat = ...
    Bool: PlcWatchAndForceTableDisplayFormat = ...
    Character: PlcWatchAndForceTableDisplayFormat = ...
    Character_sequence: PlcWatchAndForceTableDisplayFormat = ...
    Counter: PlcWatchAndForceTableDisplayFormat = ...
    Date: PlcWatchAndForceTableDisplayFormat = ...
    DATE_AND_TIME: PlcWatchAndForceTableDisplayFormat = ...
    DEC_sequence: PlcWatchAndForceTableDisplayFormat = ...
    DEC_signed: PlcWatchAndForceTableDisplayFormat = ...
    DEC_unsigned: PlcWatchAndForceTableDisplayFormat = ...
    Float: PlcWatchAndForceTableDisplayFormat = ...
    Hex: PlcWatchAndForceTableDisplayFormat = ...
    Octal: PlcWatchAndForceTableDisplayFormat = ...
    Pointer: PlcWatchAndForceTableDisplayFormat = ...
    SIMATIC_Time: PlcWatchAndForceTableDisplayFormat = ...
    String: PlcWatchAndForceTableDisplayFormat = ...
    Time: PlcWatchAndForceTableDisplayFormat = ...
    TIME_OF_DAY: PlcWatchAndForceTableDisplayFormat = ...
    Undef: PlcWatchAndForceTableDisplayFormat = ...
    Unicode_character: PlcWatchAndForceTableDisplayFormat = ...
    Unicode_character_sequence: PlcWatchAndForceTableDisplayFormat = ...
    Unicode_string: PlcWatchAndForceTableDisplayFormat = ...
    value__ = ...


class PlcWatchAndForceTableGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Group contatining Plc watch tables """
    @property
    def ForceTables(self) -> PlcForceTableComposition:
        """
        Composition of PlcWatchTables

        Get: ForceTables(self: PlcWatchAndForceTableGroup) -> PlcForceTableComposition
        """
        ...

    @property
    def Groups(self) -> PlcWatchAndForceTableUserGroupComposition:
        """
        Composition of User Groups

        Get: Groups(self: PlcWatchAndForceTableGroup) -> PlcWatchAndForceTableUserGroupComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the Plc watch table group

        Get: Name(self: PlcWatchAndForceTableGroup) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: PlcWatchAndForceTableGroup) -> IEngineeringObject
        """
        ...

    @property
    def WatchTables(self) -> PlcWatchTableComposition:
        """
        Composition of PlcWatchTables

        Get: WatchTables(self: PlcWatchAndForceTableGroup) -> PlcWatchTableComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcWatchAndForceTableGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcWatchAndForceTableGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcWatchAndForceTablePreDefinedTrigger(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Enum for PreDefinedTrigger

    enum PlcWatchAndForceTablePreDefinedTrigger, values: OnceOnlyAtEnd (4), OnceOnlyAtStart (2), OnceOnlyAtStop (6), Permanent (0), PermanentAtEnd (3), PermanentAtStart (1), PermanentAtStop (5), Undef (7)
    """
    OnceOnlyAtEnd: PlcWatchAndForceTablePreDefinedTrigger = ...
    OnceOnlyAtStart: PlcWatchAndForceTablePreDefinedTrigger = ...
    OnceOnlyAtStop: PlcWatchAndForceTablePreDefinedTrigger = ...
    Permanent: PlcWatchAndForceTablePreDefinedTrigger = ...
    PermanentAtEnd: PlcWatchAndForceTablePreDefinedTrigger = ...
    PermanentAtStart: PlcWatchAndForceTablePreDefinedTrigger = ...
    PermanentAtStop: PlcWatchAndForceTablePreDefinedTrigger = ...
    Undef: PlcWatchAndForceTablePreDefinedTrigger = ...
    value__ = ...


class PlcWatchAndForceTableSystemGroup(PlcWatchAndForceTableGroup): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ System group containing Plc watch tables and Plc force tables and user group containing these """
    pass

class PlcWatchAndForceTableUserGroup(PlcWatchAndForceTableGroup): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ User group containing Plc watch tables """
    def Delete(self): # ->
        """
        Delete(self: PlcWatchAndForceTableUserGroup)

            Deletes this instance.
        """
        ...


class PlcWatchAndForceTableUserGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of PlcWatchTableUserGroups """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: PlcWatchAndForceTableUserGroupComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy:MasterCopy) -> PlcWatchAndForceTableUserGroup:
        """
        CreateFrom(self: PlcWatchAndForceTableUserGroupComposition, sourceMasterCopy: MasterCopy) -> PlcWatchAndForceTableUserGroup

            Create PlcBlockUserGroup from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.SW.WatchAndForceTables.PlcWatchAndForceTableUserGroup
        """
        ...

    def Find(self, name:str) -> PlcWatchAndForceTableUserGroup:
        """
        Find(self: PlcWatchAndForceTableUserGroupComposition, name: str) -> PlcWatchAndForceTableUserGroup

            Finds given Plc watch table user group

            name: Name of the Plcwatchtable group to search for

            Returns: Siemens.Engineering.SW.WatchAndForceTables.PlcWatchAndForceTableUserGroup
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcWatchAndForceTableUserGroupComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcWatchAndForceTableUserGroupComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcWatchAndForceTableUserGroup](enumerable: IEnumerable[PlcWatchAndForceTableUserGroup], value: PlcWatchAndForceTableUserGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcWatchTable(IShowable, IEngineeringObject, IEquatable, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Plc watch table """
    @property
    def Entries(self) -> PlcTableCommentEntryComposition:
        """
        Composition of WatchTable Entries

        Get: Entries(self: PlcWatchTable) -> PlcTableCommentEntryComposition
        """
        ...

    @property
    def IsConsistent(self) -> bool:
        """
        Table is consistent or not

        Get: IsConsistent(self: PlcWatchTable) -> bool
        """
        ...

    @property
    def Name(self) -> str:
        """
        Name of the WatchTable

        Get: Name(self: PlcWatchTable) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: PlcWatchTable) -> IEngineeringObject
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: PlcWatchTable)

            Deletes this instance.
        """
        ...

    def Export(self, path:FileInfo, exportOptions:ExportOptions): # ->
        """
        Export(self: PlcWatchTable, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a Plc watch table

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcWatchTable) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcWatchTable) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcWatchTableComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of PlcWatchTables """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: PlcWatchTableComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> PlcWatchTable:
        """
        Find(self: PlcWatchTableComposition, name: str) -> PlcWatchTable

            Finds a given Plc watch table

            name: The name of the WatchTable

            Returns: Siemens.Engineering.SW.WatchAndForceTables.PlcWatchTable
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcWatchTableComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path:FileInfo, importOptions:ImportOptions) -> IList:
        """
        Import(self: PlcWatchTableComposition, path: FileInfo, importOptions: ImportOptions) -> IList[PlcWatchTable]

            Import Plc watch table from Simatic ML

            path: Path of the Simatic ML which will be imported

            importOptions: Options to use for import from Simatic ML

            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.WatchAndForceTables.PlcWatchTable>
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcWatchTableComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcWatchTable](enumerable: IEnumerable[PlcWatchTable], value: PlcWatchTable) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcWatchTableEntry(PlcTableCommentEntry): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Plc watch table entry """
    pass
