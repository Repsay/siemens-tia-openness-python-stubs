# encoding: utf-8
# module System.AddIn.Contract.Collections calls itself Collections
# from System.AddIn.Contract, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array

from System.AddIn.Contract import IContract, RemoteArgument

"""The following names are not found in the module: C, field#
"""

# no functions
# classes

class IArrayContract(IEnumerableContract): # skipped bases: <type 'IContract'>, <type 'object'>
    """ no doc """
    def GetCount(self) -> int:
        """ GetCount(self: IArrayContract[C]) -> int """
        ...

    def GetItem(self, index):
        """ no doc """
        ...

    def SetItem(self, index:int, value): # ->  # Not found arg types: {'value': 'C'}
        """ SetItem(self: IArrayContract[C], index: int, value: C) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ICollectionContract(IEnumerableContract): # skipped bases: <type 'IContract'>, <type 'object'>
    """ no doc """
    def Add(self, item): # ->  # Not found arg types: {'item': 'C'}
        """ Add(self: ICollectionContract[C], item: C) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ICollectionContract[C]) """
        ...

    def Contains(self, item) -> bool: # Not found arg types: {'item': 'C'}
        """ Contains(self: ICollectionContract[C], item: C) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: ICollectionContract[C], array: Array[C], arrayIndex: int) """
        ...

    def GetCount(self) -> int:
        """ GetCount(self: ICollectionContract[C]) -> int """
        ...

    def GetIsReadOnly(self) -> bool:
        """ GetIsReadOnly(self: ICollectionContract[C]) -> bool """
        ...

    def Remove(self, item) -> bool: # Not found arg types: {'item': 'C'}
        """ Remove(self: ICollectionContract[C], item: C) -> bool """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class IEnumerableContract(IContract): # skipped bases: <type 'object'>
    """ no doc """
    def GetEnumeratorContract(self) -> IEnumeratorContract:
        """ GetEnumeratorContract(self: IEnumerableContract[C]) -> IEnumeratorContract[C] """
        ...


class IEnumeratorContract(IContract): # skipped bases: <type 'object'>
    """ no doc """
    def GetCurrent(self):
        """ no doc """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: IEnumeratorContract[C]) -> bool """
        ...

    def Reset(self): # -> 
        """ Reset(self: IEnumeratorContract[C]) """
        ...


class IListContract(ICollectionContract): # skipped bases: <type 'IEnumerableContract[C]'>, <type 'IContract'>, <type 'object'>
    """ no doc """
    def GetItem(self, index):
        """ no doc """
        ...

    def IndexOf(self, item) -> int: # Not found arg types: {'item': 'C'}
        """ IndexOf(self: IListContract[C], item: C) -> int """
        ...

    def Insert(self, index:int, item): # ->  # Not found arg types: {'item': 'C'}
        """ Insert(self: IListContract[C], index: int, item: C) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: IListContract[C], index: int) """
        ...

    def SetItem(self, index:int, value): # ->  # Not found arg types: {'value': 'C'}
        """ SetItem(self: IListContract[C], index: int, value: C) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IRemoteArgumentEnumerableContract(IContract): # skipped bases: <type 'object'>
    """ no doc """
    def GetEnumeratorContract(self) -> IRemoteArgumentEnumeratorContract:
        """ GetEnumeratorContract(self: IRemoteArgumentEnumerableContract) -> IRemoteArgumentEnumeratorContract """
        ...


class IRemoteArgumentCollectionContract(IRemoteArgumentEnumerableContract): # skipped bases: <type 'IContract'>, <type 'object'>
    """ no doc """
    def GetCount(self) -> int:
        """ GetCount(self: IRemoteArgumentCollectionContract) -> int """
        ...


class IRemoteArgumentArrayContract(IRemoteArgumentCollectionContract): # skipped bases: <type 'IContract'>, <type 'IRemoteArgumentEnumerableContract'>, <type 'object'>
    """ no doc """
    def GetItem(self, index:int) -> RemoteArgument:
        """ GetItem(self: IRemoteArgumentArrayContract, index: int) -> RemoteArgument """
        ...

    def SetItem(self, index:int, value:RemoteArgument): # -> 
        """ SetItem(self: IRemoteArgumentArrayContract, index: int, value: RemoteArgument) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IRemoteArgumentArrayListContract(IRemoteArgumentArrayContract): # skipped bases: <type 'IContract'>, <type 'IRemoteArgumentCollectionContract'>, <type 'IRemoteArgumentEnumerableContract'>, <type 'object'>
    """ no doc """
    def Add(self, newItem:RemoteArgument): # -> 
        """ Add(self: IRemoteArgumentArrayListContract, newItem: RemoteArgument) """
        ...

    def Clear(self): # -> 
        """ Clear(self: IRemoteArgumentArrayListContract) """
        ...

    def Contains(self, item:RemoteArgument) -> bool:
        """ Contains(self: IRemoteArgumentArrayListContract, item: RemoteArgument) -> bool """
        ...

    def IndexOf(self, item:RemoteArgument) -> int:
        """ IndexOf(self: IRemoteArgumentArrayListContract, item: RemoteArgument) -> int """
        ...

    def Insert(self, index:int, item:RemoteArgument): # -> 
        """ Insert(self: IRemoteArgumentArrayListContract, index: int, item: RemoteArgument) """
        ...

    def Remove(self, item:RemoteArgument): # -> 
        """ Remove(self: IRemoteArgumentArrayListContract, item: RemoteArgument) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: IRemoteArgumentArrayListContract, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class IRemoteArgumentDictionaryContract(IRemoteArgumentCollectionContract): # skipped bases: <type 'IContract'>, <type 'IRemoteArgumentEnumerableContract'>, <type 'object'>
    """ no doc """
    def Add(self, key:RemoteArgument, value:RemoteArgument): # -> 
        """ Add(self: IRemoteArgumentDictionaryContract, key: RemoteArgument, value: RemoteArgument) """
        ...

    def Clear(self): # -> 
        """ Clear(self: IRemoteArgumentDictionaryContract) """
        ...

    def ContainsKey(self, key:RemoteArgument) -> bool:
        """ ContainsKey(self: IRemoteArgumentDictionaryContract, key: RemoteArgument) -> bool """
        ...

    def GetEnumeratorContract(self) -> IRemoteArgumentDictionaryEnumeratorContract:
        """ GetEnumeratorContract(self: IRemoteArgumentDictionaryContract) -> IRemoteArgumentDictionaryEnumeratorContract """
        ...

    def GetItem(self, key:RemoteArgument) -> RemoteArgument:
        """ GetItem(self: IRemoteArgumentDictionaryContract, key: RemoteArgument) -> RemoteArgument """
        ...

    def GetKeys(self) -> IRemoteArgumentCollectionContract:
        """ GetKeys(self: IRemoteArgumentDictionaryContract) -> IRemoteArgumentCollectionContract """
        ...

    def GetValues(self) -> IRemoteArgumentCollectionContract:
        """ GetValues(self: IRemoteArgumentDictionaryContract) -> IRemoteArgumentCollectionContract """
        ...

    def Remove(self, key:RemoteArgument) -> bool:
        """ Remove(self: IRemoteArgumentDictionaryContract, key: RemoteArgument) -> bool """
        ...

    def SetItem(self, key:RemoteArgument, value:RemoteArgument): # -> 
        """ SetItem(self: IRemoteArgumentDictionaryContract, key: RemoteArgument, value: RemoteArgument) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IRemoteArgumentEnumeratorContract(IContract): # skipped bases: <type 'object'>
    """ no doc """
    def GetCurrent(self) -> RemoteArgument:
        """ GetCurrent(self: IRemoteArgumentEnumeratorContract) -> RemoteArgument """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: IRemoteArgumentEnumeratorContract) -> bool """
        ...

    def Reset(self): # -> 
        """ Reset(self: IRemoteArgumentEnumeratorContract) """
        ...


class IRemoteArgumentDictionaryEnumeratorContract(IRemoteArgumentEnumeratorContract): # skipped bases: <type 'IContract'>, <type 'object'>
    """ no doc """
    def GetEntry(self) -> RemoteArgumentDictionaryEntry:
        """ GetEntry(self: IRemoteArgumentDictionaryEnumeratorContract) -> RemoteArgumentDictionaryEntry """
        ...

    def GetKey(self) -> RemoteArgument:
        """ GetKey(self: IRemoteArgumentDictionaryEnumeratorContract) -> RemoteArgument """
        ...

    def GetValue(self) -> RemoteArgument:
        """ GetValue(self: IRemoteArgumentDictionaryEnumeratorContract) -> RemoteArgument """
        ...


class RemoteArgumentDictionaryEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ RemoteArgumentDictionaryEntry(key: RemoteArgument, value: RemoteArgument) """
    Key = ...
    Value = ...


