# encoding: utf-8
# module System.Windows.Xps calls itself Xps
# from System.Printing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum

"""The following names are not found in the module: (BoundEvent, 
    SerializerWriter, SerializerWriterCollator, field#)
"""

# no functions
# classes

class VisualsToXpsDocument(SerializerWriterCollator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class XpsDocumentNotificationLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XpsDocumentNotificationLevel, values: None (0), ReceiveNotificationDisabled (2), ReceiveNotificationEnabled (1) """
    ReceiveNotificationDisabled: XpsDocumentNotificationLevel = ...
    ReceiveNotificationEnabled: XpsDocumentNotificationLevel = ...
    value__ = ...


class XpsDocumentWriter(SerializerWriter): # skipped bases: <type 'object'>
    """ no doc """
    WritingCancelled = ...
    WritingCompleted = ...
    WritingPrintTicketRequired = ...
    WritingProgressChanged = ...


class XpsWriterException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XpsWriterException(message: str, innerException: Exception)
    XpsWriterException(message: str)
    XpsWriterException()
    """
    SerializeObjectState = ...


