# encoding: utf-8
# module Siemens.Engineering.Hmi.TextGraphicList calls itself TextGraphicList
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (ExportOptions, IEngineeringComposition, 
    IEngineeringObject, ImportOptions)

from System import IEquatable

from System.Collections import IList

from System.IO import FileInfo

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess)
"""

# no functions
# classes

class GraphicList(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a graphic list """
    @property
    def Name(self) -> str:
        """
        The name of the graphic list
        Get: Name(self: GraphicList) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: GraphicList) -> IEngineeringObject
        """
        ...


    def Delete(self): # -> 
        """
        Delete(self: GraphicList)
            Deletes this instance.
        """
        ...

    def Export(self, path:FileInfo, exportOptions:ExportOptions): # -> 
        """
        Export(self: GraphicList, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of a graphic list
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: GraphicList) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: GraphicList) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class GraphicListComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of GraphicLists """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: GraphicListComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> GraphicList:
        """
        Find(self: GraphicListComposition, name: str) -> GraphicList
            Finds a given graphic list
            name: Name to find
            Returns: Siemens.Engineering.Hmi.TextGraphicList.GraphicList
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: GraphicListComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path:FileInfo, importOptions:ImportOptions) -> IList:
        """
        Import(self: GraphicListComposition, path: FileInfo, importOptions: ImportOptions) -> IList[GraphicList]
            Simatic ML import of a graphic list
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.TextGraphicList.GraphicList>
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: GraphicListComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[GraphicList](enumerable: IEnumerable[GraphicList], value: GraphicList) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TextList(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a text list """
    @property
    def Name(self) -> str:
        """
        The name of the text list
        Get: Name(self: TextList) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: TextList) -> IEngineeringObject
        """
        ...


    def Delete(self): # -> 
        """
        Delete(self: TextList)
            Deletes this instance.
        """
        ...

    def Export(self, path:FileInfo, exportOptions:ExportOptions): # -> 
        """
        Export(self: TextList, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of a text list
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TextList) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TextList) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TextListComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of TextLists """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: TextListComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> TextList:
        """
        Find(self: TextListComposition, name: str) -> TextList
            Finds a given text list
            name: Name to find
            Returns: Siemens.Engineering.Hmi.TextGraphicList.TextList
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TextListComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path:FileInfo, importOptions:ImportOptions) -> IList:
        """
        Import(self: TextListComposition, path: FileInfo, importOptions: ImportOptions) -> IList[TextList]
            Simatic ML import of a text list
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.TextGraphicList.TextList>
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TextListComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TextList](enumerable: IEnumerable[TextList], value: TextList) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


