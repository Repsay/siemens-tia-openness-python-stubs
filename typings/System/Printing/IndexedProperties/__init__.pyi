# encoding: utf-8
# module System.Printing.IndexedProperties calls itself IndexedProperties
# from System.Printing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import IDisposable

from System.Collections import Hashtable

from System.Runtime.Serialization import IDeserializationCallback


# no functions
# classes

class PrintProperty(IDisposable, IDeserializationCallback): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsDisposed(self):
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PrintProperty) -> str """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: PrintProperty) -> object
        Set: Value(self: PrintProperty) = value
        """
        ...


    def InternalDispose(self, *args): #cannot find CLR method
        """ InternalDispose(self: PrintProperty, disposing: bool) """
        ...


class PrintBooleanProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintBooleanProperty(attributeName: str, attributeValue: object)
    PrintBooleanProperty(attributeName: str)
    """
    pass

class PrintByteArrayProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintByteArrayProperty(attributeName: str, attributeValue: object)
    PrintByteArrayProperty(attributeName: str)
    """
    pass

class PrintDateTimeProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintDateTimeProperty(attributeName: str, attributeValue: object)
    PrintDateTimeProperty(attributeName: str)
    """
    pass

class PrintDriverProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintDriverProperty(attributeName: str, attributeValue: object)
    PrintDriverProperty(attributeName: str)
    """
    pass

class PrintInt32Property(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintInt32Property(attributeName: str, attributeValue: object)
    PrintInt32Property(attributeName: str)
    """
    def __int__(self, *args): #cannot find CLR method
        """ __int__(attribRef: PrintInt32Property) -> int """
        ...

    def __long__(self, *args): #cannot find CLR method
        """ __int__(attribRef: PrintInt32Property) -> int """
        ...


class PrintJobPriorityProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintJobPriorityProperty(attributeName: str, attributeValue: object)
    PrintJobPriorityProperty(attributeName: str)
    """
    pass

class PrintJobStatusProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintJobStatusProperty(attributeName: str, attributeValue: object)
    PrintJobStatusProperty(attributeName: str)
    """
    pass

class PrintPortProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintPortProperty(attributeName: str, attributeValue: object)
    PrintPortProperty(attributeName: str)
    """
    pass

class PrintProcessorProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintProcessorProperty(attributeName: str, attributeValue: object)
    PrintProcessorProperty(attributeName: str)
    """
    pass

class PrintPropertyDictionary(IDisposable, Hashtable): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'IDeserializationCallback'>, <type 'ISerializable'>, <type 'ICollection'>, <type 'object'>
    """ PrintPropertyDictionary() """
    def GetProperty(self, attribName:str) -> PrintProperty:
        """ GetProperty(self: PrintPropertyDictionary, attribName: str) -> PrintProperty """
        ...

    def SetProperty(self, attribName:str, attribValue:PrintProperty): # -> 
        """ SetProperty(self: PrintPropertyDictionary, attribName: str, attribValue: PrintProperty) """
        ...


class PrintQueueAttributeProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintQueueAttributeProperty(attributeName: str, attributeValue: object)
    PrintQueueAttributeProperty(attributeName: str)
    """
    pass

class PrintQueueProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintQueueProperty(attributeName: str, attributeValue: object)
    PrintQueueProperty(attributeName: str)
    """
    pass

class PrintQueueStatusProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintQueueStatusProperty(attributeName: str, attributeValue: object)
    PrintQueueStatusProperty(attributeName: str)
    """
    pass

class PrintServerLoggingProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintServerLoggingProperty(attributeName: str, attributeValue: object)
    PrintServerLoggingProperty(attributeName: str)
    """
    pass

class PrintServerProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintServerProperty(attributeName: str, attributeValue: object)
    PrintServerProperty(attributeName: str)
    """
    pass

class PrintStreamProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintStreamProperty(attributeName: str, attributeValue: object)
    PrintStreamProperty(attributeName: str)
    """
    pass

class PrintStringProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintStringProperty(attributeName: str, attributeValue: object)
    PrintStringProperty(attributeName: str)
    """
    pass

class PrintSystemTypeProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintSystemTypeProperty(attributeName: str, attributeValue: object)
    PrintSystemTypeProperty(attributeName: str)
    """
    pass

class PrintThreadPriorityProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintThreadPriorityProperty(attributeName: str, attributeValue: object)
    PrintThreadPriorityProperty(attributeName: str)
    """
    pass

class PrintTicketProperty(PrintProperty): # skipped bases: <type 'IDisposable'>, <type 'IDeserializationCallback'>, <type 'object'>
    """
    PrintTicketProperty(attributeName: str, attributeValue: object)
    PrintTicketProperty(attributeName: str)
    """
    pass

