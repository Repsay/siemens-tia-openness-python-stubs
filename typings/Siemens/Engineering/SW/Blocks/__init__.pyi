# encoding: utf-8
# module Siemens.Engineering.SW.Blocks calls itself Blocks
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (ExportOptions, IEngineeringComposition, 
    IEngineeringObject, IEngineeringService, IEngineeringServiceProvider, 
    IShowable, ImportOptions)

from Siemens.Engineering.AdvancedProtection import ProtectionProviderBase

from Siemens.Engineering.Library.MasterCopies import (IMasterCopySource, 
    IMasterCopyTarget, MasterCopy)

from Siemens.Engineering.Library.Types import (
    ILibraryTypeInstantiationTarget, LibraryType, LibraryTypeVersion)

from Siemens.Engineering.SW import SWImportOptions

from Siemens.Engineering.SW.ExternalSources import IGenerateSource

from System import DateTime, Enum, IEquatable, Version

from System.Collections import IList

from System.IO import DirectoryInfo, FileInfo

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

# no functions
# classes

class PlcBlock(IInternalObjectAccess, IEngineeringServiceProvider, IShowable, IEngineeringObject, IGenerateSource, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IServiceProvider'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Plc block """
    @property
    def AutoNumber(self) -> bool:
        """
        Determines if the block gets the block number automatically or manually
        Get: AutoNumber(self: PlcBlock) -> bool
        Set: AutoNumber(self: PlcBlock) = value
        """
        ...

    @property
    def CodeModifiedDate(self) -> DateTime:
        """
        Last code modification date
        Get: CodeModifiedDate(self: PlcBlock) -> DateTime
        """
        ...

    @property
    def CompileDate(self) -> DateTime:
        """
        Last compilation date
        Get: CompileDate(self: PlcBlock) -> DateTime
        """
        ...

    @property
    def CreationDate(self) -> DateTime:
        """
        Creation date of this Plc block
        Get: CreationDate(self: PlcBlock) -> DateTime
        """
        ...

    @property
    def HeaderAuthor(self) -> str:
        """
        PLC header attribute author
        Get: HeaderAuthor(self: PlcBlock) -> str
        """
        ...

    @property
    def HeaderFamily(self) -> str:
        """
        PLC header attribute family
        Get: HeaderFamily(self: PlcBlock) -> str
        """
        ...

    @property
    def HeaderName(self) -> str:
        """
        PLC header attribute name
        Get: HeaderName(self: PlcBlock) -> str
        """
        ...

    @property
    def HeaderVersion(self) -> Version:
        """
        PLC header attribute version
        Get: HeaderVersion(self: PlcBlock) -> Version
        """
        ...

    @property
    def InterfaceModifiedDate(self) -> DateTime:
        """
        Last interface modification
        Get: InterfaceModifiedDate(self: PlcBlock) -> DateTime
        """
        ...

    @property
    def IsConsistent(self) -> bool:
        """
        True if block and used data is consistent
        Get: IsConsistent(self: PlcBlock) -> bool
        """
        ...

    @property
    def IsKnowHowProtected(self) -> bool:
        """
        Gets the know-how protection status of the block
        Get: IsKnowHowProtected(self: PlcBlock) -> bool
        """
        ...

    @property
    def MemoryLayout(self) -> MemoryLayout:
        """
        Indicates if a block has been optimized
        Get: MemoryLayout(self: PlcBlock) -> MemoryLayout
        """
        ...

    @property
    def ModifiedDate(self) -> DateTime:
        """
        Last modification date including e.g. comments
        Get: ModifiedDate(self: PlcBlock) -> DateTime
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the Plc block
        Get: Name(self: PlcBlock) -> str
        Set: Name(self: PlcBlock) = value
        """
        ...

    @property
    def Number(self) -> int:
        """
        The number of this Plc block
        Get: Number(self: PlcBlock) -> int
        Set: Number(self: PlcBlock) = value
        """
        ...

    @property
    def ParameterModified(self) -> DateTime:
        """
        Date of the last parameter modification
        Get: ParameterModified(self: PlcBlock) -> DateTime
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: PlcBlock) -> IEngineeringObject
        """
        ...

    @property
    def ProgrammingLanguage(self) -> ProgrammingLanguage:
        """
        The language of this block
        Get: ProgrammingLanguage(self: PlcBlock) -> ProgrammingLanguage
        """
        ...

    @property
    def StructureModified(self) -> DateTime:
        """
        Date of the last structure modification
        Get: StructureModified(self: PlcBlock) -> DateTime
        """
        ...


    def Delete(self): # -> 
        """
        Delete(self: PlcBlock)
            Deletes this instance.
        """
        ...

    def Export(self, path:FileInfo, exportOptions:ExportOptions): # -> 
        """
        Export(self: PlcBlock, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of a Plc block
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcBlock) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcBlock) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DataBlock(PlcBlock, IMasterCopySource): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IShowable'>, <type 'IEngineeringInstance'>, <type 'IEngineeringServiceProvider'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IGenerateSource'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Class representing a data block """
    pass

class ArrayDB(DataBlock): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringServiceProvider'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IMasterCopySource'>, <type 'IGenerateSource'>, <type 'IInternalBaseAccess'>, <type 'IShowable'>, <type 'object'>
    """ Class representing array DBs """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: ArrayDB) -> IEngineeringObject
        """
        ...



class BlockType(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    The list of possible IECPL block types
    enum BlockType, values: FB (1), FBT (4), SDT (5), SFB (2), UDT (3), Undef (0)
    """
    FB: BlockType = ...
    FBT: BlockType = ...
    SDT: BlockType = ...
    SFB: BlockType = ...
    UDT: BlockType = ...
    Undef: BlockType = ...
    value__ = ...


class CodeBlock(PlcBlock, IMasterCopySource): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IShowable'>, <type 'IEngineeringInstance'>, <type 'IEngineeringServiceProvider'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IGenerateSource'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Class representing a code block """
    def ExportProDIAGInfo(self, path:DirectoryInfo): # -> 
        """
        ExportProDIAGInfo(self: CodeBlock, path: DirectoryInfo)
            Exports prodiag alarm information
            path: path where the file gets exported
        """
        ...


class CodeBlockLibraryType(LibraryType): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Class representing a code block library type """
    pass

class CodeBlockLibraryTypeVersion(LibraryTypeVersion): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Class representing a code block library type version """
    pass

class FB(CodeBlock): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringServiceProvider'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IMasterCopySource'>, <type 'IGenerateSource'>, <type 'IInternalBaseAccess'>, <type 'IShowable'>, <type 'object'>
    """ Represents an FB """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: FB) -> IEngineeringObject
        """
        ...

    @property
    def Supervisions(self) -> SupervisionComposition:
        """
        Get supervisions
        Get: Supervisions(self: FB) -> SupervisionComposition
        """
        ...



class FC(CodeBlock): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringServiceProvider'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IMasterCopySource'>, <type 'IGenerateSource'>, <type 'IInternalBaseAccess'>, <type 'IShowable'>, <type 'object'>
    """ Represents an FC """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: FC) -> IEngineeringObject
        """
        ...



class GlobalDB(DataBlock): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringServiceProvider'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IMasterCopySource'>, <type 'IGenerateSource'>, <type 'IInternalBaseAccess'>, <type 'IShowable'>, <type 'object'>
    """ Represents a global DB """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: GlobalDB) -> IEngineeringObject
        """
        ...



class InstanceDB(DataBlock): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringServiceProvider'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IMasterCopySource'>, <type 'IGenerateSource'>, <type 'IInternalBaseAccess'>, <type 'IShowable'>, <type 'object'>
    """ Represents an instance DB """
    @property
    def InstanceOfName(self): # -> 
        """
        The block name of the father instance (FB/SFB/UDT/SDT)
        Get: InstanceOfName(self: InstanceDB) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: InstanceDB) -> IEngineeringObject
        """
        ...



class InterfaceSnapshot(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Provides Snapshot Value functionality. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: InterfaceSnapshot) -> IEngineeringObject
        """
        ...


    def Export(self, path:FileInfo, exportOptions:ExportOptions): # -> 
        """
        Export(self: InterfaceSnapshot, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of snapshot values.
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: InterfaceSnapshot) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: InterfaceSnapshot) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MemoryLayout(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Determines if a block access is optimized or not
    enum MemoryLayout, values: Optimized (1), Standard (0)
    """
    Optimized: MemoryLayout = ...
    Standard: MemoryLayout = ...
    value__ = ...


class OB(CodeBlock): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringServiceProvider'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IMasterCopySource'>, <type 'IGenerateSource'>, <type 'IInternalBaseAccess'>, <type 'IShowable'>, <type 'object'>
    """ Represents an OB """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: OB) -> IEngineeringObject
        """
        ...

    @property
    def SecondaryType(self) -> str:
        """
        Additional information about the type
        Get: SecondaryType(self: OB) -> str
        """
        ...



class OBDataExchangeMode(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Enum for OBDataExchangeMode
    enum OBDataExchangeMode, values: Cyclic (1), None (0), Synchronous (2)
    """
    Cyclic: OBDataExchangeMode = ...
    Synchronous: OBDataExchangeMode = ...
    value__ = ...


class OBExecution(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Enum for Execution
    enum OBExecution, values: Daily (4), End_of_month (8), Every_minute (2), Hourly (3), Monthly (6), Never (0), Once (1), Weekly (5), Yearly (7)
    """
    Daily: OBExecution = ...
    End_of_month: OBExecution = ...
    Every_minute: OBExecution = ...
    Hourly: OBExecution = ...
    Monthly: OBExecution = ...
    Never: OBExecution = ...
    Once: OBExecution = ...
    value__ = ...
    Weekly: OBExecution = ...
    Yearly: OBExecution = ...


class OBTimeMode(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Enum for TimeMode
    enum OBTimeMode, values: Local (1), None (0), System (2)
    """
    Local: OBTimeMode = ...
    System: OBTimeMode = ...
    value__ = ...


class PlcBlockComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of PlcBlocks """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: PlcBlockComposition) -> IEngineeringObject
        """
        ...


    def CreateFB(self, name:str, isAutoNumbered:bool, number:int, programmingLanguage:ProgrammingLanguage) -> FB:
        """
        CreateFB(self: PlcBlockComposition, name: str, isAutoNumbered: bool, number: int, programmingLanguage: ProgrammingLanguage) -> FB
            Creates a block.
            name: Name of the block.
            isAutoNumbered: Indicates if block is autonumbered.
            number: Number of the block.
            programmingLanguage: Language of the block.
            Returns: Siemens.Engineering.SW.Blocks.FB
        """
        ...

    def CreateFrom(self, *__args:MasterCopy) -> PlcBlock:
        """
        CreateFrom(self: PlcBlockComposition, sourceMasterCopy: MasterCopy) -> PlcBlock
            Create PlcBlock from MasterCopy
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.Blocks.PlcBlock
        CreateFrom(self: PlcBlockComposition, libraryTypeVersion: CodeBlockLibraryTypeVersion) -> PlcBlock
            Create from version
            libraryTypeVersion: type version
            Returns: Siemens.Engineering.SW.Blocks.PlcBlock
        """
        ...

    def CreateInstanceDB(self, name:str, isAutoNumbered:bool, number:int, instanceOfName:str) -> InstanceDB:
        """
        CreateInstanceDB(self: PlcBlockComposition, name: str, isAutoNumbered: bool, number: int, instanceOfName: str) -> InstanceDB
            Creates an instance DB for Prodiag block.
            name: Name of the block.
            isAutoNumbered: Indicates if block is autonumbered.
            number: Number of the block.
            instanceOfName: Name of the block where db belongs to.
            Returns: Siemens.Engineering.SW.Blocks.InstanceDB
        """
        ...

    def Find(self, name:str) -> PlcBlock:
        """
        Find(self: PlcBlockComposition, name: str) -> PlcBlock
            Finds a given Plc block
            name: Name to find
            Returns: Siemens.Engineering.SW.Blocks.PlcBlock
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcBlockComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path:FileInfo, importOptions:ImportOptions, swImportOptions:SWImportOptions = ...) -> IList:
        """
        Import(self: PlcBlockComposition, path: FileInfo, importOptions: ImportOptions) -> IList[PlcBlock]
            Simatic ML import of a Plc block
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Blocks.PlcBlock>
        Import(self: PlcBlockComposition, path: FileInfo, importOptions: ImportOptions, swImportOptions: SWImportOptions) -> IList[PlcBlock]
            Simatic ML import of a Plc block with ignore flags.
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
            swImportOptions: Sw import options to use for Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Blocks.PlcBlock>
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcBlockComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcBlock](enumerable: IEnumerable[PlcBlock], value: PlcBlock) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcBlockGroup(IEquatable, IEngineeringObject, IEngineeringServiceProvider, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IServiceProvider'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Group containing Plc blocks & Plc block user groups """
    @property
    def Blocks(self) -> PlcBlockComposition:
        """
        Composition of Plc blocks
        Get: Blocks(self: PlcBlockGroup) -> PlcBlockComposition
        """
        ...

    @property
    def Groups(self) -> PlcBlockUserGroupComposition:
        """
        Composition of Plc block user groups
        Get: Groups(self: PlcBlockGroup) -> PlcBlockUserGroupComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the Plc block group
        Get: Name(self: PlcBlockGroup) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: PlcBlockGroup) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcBlockGroup) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcBlockGroup) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcBlockProtectionProvider(ProtectionProviderBase): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringService'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'object'>
    """ Provides protection services. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: PlcBlockProtectionProvider) -> IEngineeringObject
        """
        ...



class PlcBlockSystemGroup(PlcBlockGroup, ILibraryTypeInstantiationTarget, IMasterCopyTarget): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringServiceProvider'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ System group containing Plc blocks & Plc block user groups """
    @property
    def SystemBlockGroups(self) -> PlcSystemBlockGroupComposition:
        """
        Composition of Plc system block groups
        Get: SystemBlockGroups(self: PlcBlockSystemGroup) -> PlcSystemBlockGroupComposition
        """
        ...



class PlcBlockUserGroup(PlcBlockGroup, ILibraryTypeInstantiationTarget, IMasterCopySource, IMasterCopyTarget): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringServiceProvider'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ User group containing Plc blocks & Plc block user groups """
    def Delete(self): # -> 
        """
        Delete(self: PlcBlockUserGroup)
            Deletes this instance.
        """
        ...


class PlcBlockUserGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of PlcBlockUserGroups """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: PlcBlockUserGroupComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy:MasterCopy) -> PlcBlockUserGroup:
        """
        CreateFrom(self: PlcBlockUserGroupComposition, sourceMasterCopy: MasterCopy) -> PlcBlockUserGroup
            Create PlcBlockUserGroup from MasterCopy
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.Blocks.PlcBlockUserGroup
        """
        ...

    def Find(self, name:str) -> PlcBlockUserGroup:
        """
        Find(self: PlcBlockUserGroupComposition, name: str) -> PlcBlockUserGroup
            Finds a given Plc block user group
            name: Name to find
            Returns: Siemens.Engineering.SW.Blocks.PlcBlockUserGroup
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcBlockUserGroupComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcBlockUserGroupComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcBlockUserGroup](enumerable: IEnumerable[PlcBlockUserGroup], value: PlcBlockUserGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcSystemBlockGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Group containing Plc system blocks & Plc system block groups """
    @property
    def Blocks(self) -> PlcBlockComposition:
        """
        Composition of Plc system blocks
        Get: Blocks(self: PlcSystemBlockGroup) -> PlcBlockComposition
        """
        ...

    @property
    def Groups(self) -> PlcSystemBlockGroupComposition:
        """
        Composition of Plc system block groups
        Get: Groups(self: PlcSystemBlockGroup) -> PlcSystemBlockGroupComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the Plc system block group
        Get: Name(self: PlcSystemBlockGroup) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: PlcSystemBlockGroup) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcSystemBlockGroup) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcSystemBlockGroup) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcSystemBlockGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of PlcSystemBlockGroups """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: PlcSystemBlockGroupComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> PlcSystemBlockGroup:
        """
        Find(self: PlcSystemBlockGroupComposition, name: str) -> PlcSystemBlockGroup
            Finds a given Plc system block group
            name: Name to find
            Returns: Siemens.Engineering.SW.Blocks.PlcSystemBlockGroup
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcSystemBlockGroupComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcSystemBlockGroupComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcSystemBlockGroup](enumerable: IEnumerable[PlcSystemBlockGroup], value: PlcSystemBlockGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ProgrammingLanguage(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    The list of possible creation languages of programming blocks
    enum ProgrammingLanguage, values: CFC (8), CPU_DB (7), DB (5), F_CALL (26), F_DB (18), F_FBD (17), F_FBD_LIB (20), F_LAD (16), F_LAD_LIB (19), F_STL (15), FBD (3), FBD_IEC (10), FCP (21), FLD (22), GRAPH (6), LAD (2), LAD_IEC (11), Motion_DB (25), ProDiag (23), ProDiag_OB (24), RSE (14), S7_PDIAG (13), SCL (4), SDB (12), SFC (9), STL (1), Undef (0)
    """
    CFC: ProgrammingLanguage = ...
    CPU_DB: ProgrammingLanguage = ...
    DB: ProgrammingLanguage = ...
    FBD: ProgrammingLanguage = ...
    FBD_IEC: ProgrammingLanguage = ...
    FCP: ProgrammingLanguage = ...
    FLD: ProgrammingLanguage = ...
    F_CALL: ProgrammingLanguage = ...
    F_DB: ProgrammingLanguage = ...
    F_FBD: ProgrammingLanguage = ...
    F_FBD_LIB: ProgrammingLanguage = ...
    F_LAD: ProgrammingLanguage = ...
    F_LAD_LIB: ProgrammingLanguage = ...
    F_STL: ProgrammingLanguage = ...
    GRAPH: ProgrammingLanguage = ...
    LAD: ProgrammingLanguage = ...
    LAD_IEC: ProgrammingLanguage = ...
    Motion_DB: ProgrammingLanguage = ...
    ProDiag: ProgrammingLanguage = ...
    ProDiag_OB: ProgrammingLanguage = ...
    RSE: ProgrammingLanguage = ...
    S7_PDIAG: ProgrammingLanguage = ...
    SCL: ProgrammingLanguage = ...
    SDB: ProgrammingLanguage = ...
    SFC: ProgrammingLanguage = ...
    STL: ProgrammingLanguage = ...
    Undef: ProgrammingLanguage = ...
    value__ = ...


class Supervision(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Supervision """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: Supervision) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: Supervision) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: Supervision) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SupervisionComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Supervisions of the block """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: SupervisionComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SupervisionComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SupervisionComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Supervision](enumerable: IEnumerable[Supervision], value: Supervision) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


