# encoding: utf-8
# module System.Management.Automation.Host calls itself Host
# from System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import (Array, Char, ConsoleColor, Enum, Guid, Int64, Type, 
    Version)

from System.Collections import IEnumerable

from System.Collections.Generic import Dictionary

from System.Globalization import CultureInfo

from System.Management.Automation import (InformationRecord, PSCredential, 
    PSCredentialTypes, PSCredentialUIOptions, PSObject, ProgressRecord, 
    RuntimeException)

from System.Management.Automation.Runspaces import Runspace

from System.Security import SecureString

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class BufferCell: # skipped bases: <type 'object'>, <type 'object'>
    """ BufferCell(character: Char, foreground: ConsoleColor, background: ConsoleColor, bufferCellType: BufferCellType) """
    @property
    def BackgroundColor(self) -> ConsoleColor:
        """
        Get: BackgroundColor(self: BufferCell) -> ConsoleColor
        Set: BackgroundColor(self: BufferCell) = value
        """
        ...

    @property
    def BufferCellType(self) -> BufferCellType:
        """
        Get: BufferCellType(self: BufferCell) -> BufferCellType
        Set: BufferCellType(self: BufferCell) = value
        """
        ...

    @property
    def Character(self) -> Char:
        """
        Get: Character(self: BufferCell) -> Char
        Set: Character(self: BufferCell) = value
        """
        ...

    @property
    def ForegroundColor(self) -> ConsoleColor:
        """
        Get: ForegroundColor(self: BufferCell) -> ConsoleColor
        Set: ForegroundColor(self: BufferCell) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: BufferCell, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: BufferCell) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: BufferCell) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class BufferCellType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BufferCellType, values: Complete (0), Leading (1), Trailing (2) """
    Complete: BufferCellType = ...
    Leading: BufferCellType = ...
    Trailing: BufferCellType = ...
    value__ = ...


class ChoiceDescription: # skipped bases: <type 'object'>, <type 'object'>
    """
    ChoiceDescription(label: str)
    ChoiceDescription(label: str, helpMessage: str)
    """
    @property
    def HelpMessage(self) -> str:
        """
        Get: HelpMessage(self: ChoiceDescription) -> str
        Set: HelpMessage(self: ChoiceDescription) = value
        """
        ...

    @property
    def Label(self) -> str:
        """ Get: Label(self: ChoiceDescription) -> str """
        ...



class ControlKeyStates(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ControlKeyStates, values: CapsLockOn (128), EnhancedKey (256), LeftAltPressed (2), LeftCtrlPressed (8), NumLockOn (32), RightAltPressed (1), RightCtrlPressed (4), ScrollLockOn (64), ShiftPressed (16) """
    CapsLockOn: ControlKeyStates = ...
    EnhancedKey: ControlKeyStates = ...
    LeftAltPressed: ControlKeyStates = ...
    LeftCtrlPressed: ControlKeyStates = ...
    NumLockOn: ControlKeyStates = ...
    RightAltPressed: ControlKeyStates = ...
    RightCtrlPressed: ControlKeyStates = ...
    ScrollLockOn: ControlKeyStates = ...
    ShiftPressed: ControlKeyStates = ...
    value__ = ...


class Coordinates: # skipped bases: <type 'object'>, <type 'object'>
    """ Coordinates(x: int, y: int) """
    @property
    def X(self) -> int:
        """
        Get: X(self: Coordinates) -> int
        Set: X(self: Coordinates) = value
        """
        ...

    @property
    def Y(self) -> int:
        """
        Get: Y(self: Coordinates) -> int
        Set: Y(self: Coordinates) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Coordinates, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Coordinates) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Coordinates) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class FieldDescription: # skipped bases: <type 'object'>, <type 'object'>
    """ FieldDescription(name: str) """
    @property
    def Attributes(self) -> Collection:
        """ Get: Attributes(self: FieldDescription) -> Collection[Attribute] """
        ...

    @property
    def DefaultValue(self) -> PSObject:
        """
        Get: DefaultValue(self: FieldDescription) -> PSObject
        Set: DefaultValue(self: FieldDescription) = value
        """
        ...

    @property
    def HelpMessage(self) -> str:
        """
        Get: HelpMessage(self: FieldDescription) -> str
        Set: HelpMessage(self: FieldDescription) = value
        """
        ...

    @property
    def IsMandatory(self) -> bool:
        """
        Get: IsMandatory(self: FieldDescription) -> bool
        Set: IsMandatory(self: FieldDescription) = value
        """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: FieldDescription) -> str
        Set: Label(self: FieldDescription) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: FieldDescription) -> str """
        ...

    @property
    def ParameterAssemblyFullName(self) -> str:
        """ Get: ParameterAssemblyFullName(self: FieldDescription) -> str """
        ...

    @property
    def ParameterTypeFullName(self) -> str:
        """ Get: ParameterTypeFullName(self: FieldDescription) -> str """
        ...

    @property
    def ParameterTypeName(self) -> str:
        """ Get: ParameterTypeName(self: FieldDescription) -> str """
        ...


    def SetParameterType(self, parameterType:Type): # -> 
        """ SetParameterType(self: FieldDescription, parameterType: Type) """
        ...


class HostException(RuntimeException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    HostException()
    HostException(message: str)
    HostException(message: str, innerException: Exception)
    HostException(message: str, innerException: Exception, errorId: str, errorCategory: ErrorCategory)
    """
    SerializeObjectState = ...


class IHostSupportsInteractiveSession: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsRunspacePushed(self) -> bool:
        """ Get: IsRunspacePushed(self: IHostSupportsInteractiveSession) -> bool """
        ...

    @property
    def Runspace(self) -> Runspace:
        """ Get: Runspace(self: IHostSupportsInteractiveSession) -> Runspace """
        ...


    def PopRunspace(self): # -> 
        """ PopRunspace(self: IHostSupportsInteractiveSession) """
        ...

    def PushRunspace(self, runspace:Runspace): # -> 
        """ PushRunspace(self: IHostSupportsInteractiveSession, runspace: Runspace) """
        ...


class IHostUISupportsMultipleChoiceSelection: # skipped bases: <type 'object'>
    """ no doc """
    def PromptForChoice(self, caption:str, message:str, choices:Collection, defaultChoices:IEnumerable) -> Collection:
        """ PromptForChoice(self: IHostUISupportsMultipleChoiceSelection, caption: str, message: str, choices: Collection[ChoiceDescription], defaultChoices: IEnumerable[int]) -> Collection[int] """
        ...


class KeyInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ KeyInfo(virtualKeyCode: int, ch: Char, controlKeyState: ControlKeyStates, keyDown: bool) """
    @property
    def Character(self) -> Char:
        """
        Get: Character(self: KeyInfo) -> Char
        Set: Character(self: KeyInfo) = value
        """
        ...

    @property
    def ControlKeyState(self) -> ControlKeyStates:
        """
        Get: ControlKeyState(self: KeyInfo) -> ControlKeyStates
        Set: ControlKeyState(self: KeyInfo) = value
        """
        ...

    @property
    def KeyDown(self) -> bool:
        """
        Get: KeyDown(self: KeyInfo) -> bool
        Set: KeyDown(self: KeyInfo) = value
        """
        ...

    @property
    def VirtualKeyCode(self) -> int:
        """
        Get: VirtualKeyCode(self: KeyInfo) -> int
        Set: VirtualKeyCode(self: KeyInfo) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: KeyInfo, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: KeyInfo) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: KeyInfo) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PromptingException(HostException): # skipped bases: <type 'IContainsErrorRecord'>, <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PromptingException()
    PromptingException(message: str)
    PromptingException(message: str, innerException: Exception)
    PromptingException(message: str, innerException: Exception, errorId: str, errorCategory: ErrorCategory)
    """
    SerializeObjectState = ...


class PSHost: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CurrentCulture(self) -> CultureInfo:
        """ Get: CurrentCulture(self: PSHost) -> CultureInfo """
        ...

    @property
    def CurrentUICulture(self) -> CultureInfo:
        """ Get: CurrentUICulture(self: PSHost) -> CultureInfo """
        ...

    @property
    def DebuggerEnabled(self) -> bool:
        """
        Get: DebuggerEnabled(self: PSHost) -> bool
        Set: DebuggerEnabled(self: PSHost) = value
        """
        ...

    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: PSHost) -> Guid """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PSHost) -> str """
        ...

    @property
    def PrivateData(self) -> PSObject:
        """ Get: PrivateData(self: PSHost) -> PSObject """
        ...

    @property
    def UI(self) -> PSHostUserInterface:
        """ Get: UI(self: PSHost) -> PSHostUserInterface """
        ...

    @property
    def Version(self) -> Version:
        """ Get: Version(self: PSHost) -> Version """
        ...


    def EnterNestedPrompt(self): # -> 
        """ EnterNestedPrompt(self: PSHost) """
        ...

    def ExitNestedPrompt(self): # -> 
        """ ExitNestedPrompt(self: PSHost) """
        ...

    def NotifyBeginApplication(self): # -> 
        """ NotifyBeginApplication(self: PSHost) """
        ...

    def NotifyEndApplication(self): # -> 
        """ NotifyEndApplication(self: PSHost) """
        ...

    def SetShouldExit(self, exitCode:int): # -> 
        """ SetShouldExit(self: PSHost, exitCode: int) """
        ...


class PSHostRawUserInterface: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BackgroundColor(self) -> ConsoleColor:
        """
        Get: BackgroundColor(self: PSHostRawUserInterface) -> ConsoleColor
        Set: BackgroundColor(self: PSHostRawUserInterface) = value
        """
        ...

    @property
    def BufferSize(self) -> Size:
        """
        Get: BufferSize(self: PSHostRawUserInterface) -> Size
        Set: BufferSize(self: PSHostRawUserInterface) = value
        """
        ...

    @property
    def CursorPosition(self) -> Coordinates:
        """
        Get: CursorPosition(self: PSHostRawUserInterface) -> Coordinates
        Set: CursorPosition(self: PSHostRawUserInterface) = value
        """
        ...

    @property
    def CursorSize(self) -> int:
        """
        Get: CursorSize(self: PSHostRawUserInterface) -> int
        Set: CursorSize(self: PSHostRawUserInterface) = value
        """
        ...

    @property
    def ForegroundColor(self) -> ConsoleColor:
        """
        Get: ForegroundColor(self: PSHostRawUserInterface) -> ConsoleColor
        Set: ForegroundColor(self: PSHostRawUserInterface) = value
        """
        ...

    @property
    def KeyAvailable(self) -> bool:
        """ Get: KeyAvailable(self: PSHostRawUserInterface) -> bool """
        ...

    @property
    def MaxPhysicalWindowSize(self) -> Size:
        """ Get: MaxPhysicalWindowSize(self: PSHostRawUserInterface) -> Size """
        ...

    @property
    def MaxWindowSize(self) -> Size:
        """ Get: MaxWindowSize(self: PSHostRawUserInterface) -> Size """
        ...

    @property
    def WindowPosition(self) -> Coordinates:
        """
        Get: WindowPosition(self: PSHostRawUserInterface) -> Coordinates
        Set: WindowPosition(self: PSHostRawUserInterface) = value
        """
        ...

    @property
    def WindowSize(self) -> Size:
        """
        Get: WindowSize(self: PSHostRawUserInterface) -> Size
        Set: WindowSize(self: PSHostRawUserInterface) = value
        """
        ...

    @property
    def WindowTitle(self) -> str:
        """
        Get: WindowTitle(self: PSHostRawUserInterface) -> str
        Set: WindowTitle(self: PSHostRawUserInterface) = value
        """
        ...


    def FlushInputBuffer(self): # -> 
        """ FlushInputBuffer(self: PSHostRawUserInterface) """
        ...

    def GetBufferContents(self, rectangle:Rectangle) -> Array:
        """ GetBufferContents(self: PSHostRawUserInterface, rectangle: Rectangle) -> Array[BufferCell] """
        ...

    def LengthInBufferCells(self, source:str, offset:int = ...) -> int:
        """
        LengthInBufferCells(self: PSHostRawUserInterface, source: str, offset: int) -> int
        LengthInBufferCells(self: PSHostRawUserInterface, source: str) -> int
        LengthInBufferCells(self: PSHostRawUserInterface, source: Char) -> int
        """
        ...

    def NewBufferCellArray(self, *__args) -> Array:
        """
        NewBufferCellArray(self: PSHostRawUserInterface, size: Size, contents: BufferCell) -> Array[BufferCell]
        NewBufferCellArray(self: PSHostRawUserInterface, contents: Array[str], foregroundColor: ConsoleColor, backgroundColor: ConsoleColor) -> Array[BufferCell]
        NewBufferCellArray(self: PSHostRawUserInterface, width: int, height: int, contents: BufferCell) -> Array[BufferCell]
        """
        ...

    def ReadKey(self, options:ReadKeyOptions = ...) -> KeyInfo:
        """
        ReadKey(self: PSHostRawUserInterface) -> KeyInfo
        ReadKey(self: PSHostRawUserInterface, options: ReadKeyOptions) -> KeyInfo
        """
        ...

    def ScrollBufferContents(self, source:Rectangle, destination:Coordinates, clip:Rectangle, fill:BufferCell): # -> 
        """ ScrollBufferContents(self: PSHostRawUserInterface, source: Rectangle, destination: Coordinates, clip: Rectangle, fill: BufferCell) """
        ...

    def SetBufferContents(self, *__args): # -> 
        """ SetBufferContents(self: PSHostRawUserInterface, origin: Coordinates, contents: Array[BufferCell])SetBufferContents(self: PSHostRawUserInterface, rectangle: Rectangle, fill: BufferCell) """
        ...


class PSHostUserInterface: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def RawUI(self) -> PSHostRawUserInterface:
        """ Get: RawUI(self: PSHostUserInterface) -> PSHostRawUserInterface """
        ...

    @property
    def SupportsVirtualTerminal(self) -> bool:
        """ Get: SupportsVirtualTerminal(self: PSHostUserInterface) -> bool """
        ...


    def Prompt(self, caption:str, message:str, descriptions:Collection) -> Dictionary:
        """ Prompt(self: PSHostUserInterface, caption: str, message: str, descriptions: Collection[FieldDescription]) -> Dictionary[str, PSObject] """
        ...

    def PromptForChoice(self, caption:str, message:str, choices:Collection, defaultChoice:int) -> int:
        """ PromptForChoice(self: PSHostUserInterface, caption: str, message: str, choices: Collection[ChoiceDescription], defaultChoice: int) -> int """
        ...

    def PromptForCredential(self, caption:str, message:str, userName:str, targetName:str, allowedCredentialTypes:PSCredentialTypes = ..., options:PSCredentialUIOptions = ...) -> PSCredential:
        """
        PromptForCredential(self: PSHostUserInterface, caption: str, message: str, userName: str, targetName: str) -> PSCredential
        PromptForCredential(self: PSHostUserInterface, caption: str, message: str, userName: str, targetName: str, allowedCredentialTypes: PSCredentialTypes, options: PSCredentialUIOptions) -> PSCredential
        """
        ...

    def ReadLine(self) -> str:
        """ ReadLine(self: PSHostUserInterface) -> str """
        ...

    def ReadLineAsSecureString(self) -> SecureString:
        """ ReadLineAsSecureString(self: PSHostUserInterface) -> SecureString """
        ...

    def Write(self, *__args:str): # -> 
        """ Write(self: PSHostUserInterface, value: str)Write(self: PSHostUserInterface, foregroundColor: ConsoleColor, backgroundColor: ConsoleColor, value: str) """
        ...

    def WriteDebugLine(self, message:str): # -> 
        """ WriteDebugLine(self: PSHostUserInterface, message: str) """
        ...

    def WriteErrorLine(self, value:str): # -> 
        """ WriteErrorLine(self: PSHostUserInterface, value: str) """
        ...

    def WriteInformation(self, record:InformationRecord): # -> 
        """ WriteInformation(self: PSHostUserInterface, record: InformationRecord) """
        ...

    def WriteLine(self, *__args:str): # -> 
        """ WriteLine(self: PSHostUserInterface)WriteLine(self: PSHostUserInterface, value: str)WriteLine(self: PSHostUserInterface, foregroundColor: ConsoleColor, backgroundColor: ConsoleColor, value: str) """
        ...

    def WriteProgress(self, sourceId:Int64, record:ProgressRecord): # -> 
        """ WriteProgress(self: PSHostUserInterface, sourceId: Int64, record: ProgressRecord) """
        ...

    def WriteVerboseLine(self, message:str): # -> 
        """ WriteVerboseLine(self: PSHostUserInterface, message: str) """
        ...

    def WriteWarningLine(self, message:str): # -> 
        """ WriteWarningLine(self: PSHostUserInterface, message: str) """
        ...


class ReadKeyOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ReadKeyOptions, values: AllowCtrlC (1), IncludeKeyDown (4), IncludeKeyUp (8), NoEcho (2) """
    AllowCtrlC: ReadKeyOptions = ...
    IncludeKeyDown: ReadKeyOptions = ...
    IncludeKeyUp: ReadKeyOptions = ...
    NoEcho: ReadKeyOptions = ...
    value__ = ...


class Rectangle: # skipped bases: <type 'object'>, <type 'object'>
    """
    Rectangle(left: int, top: int, right: int, bottom: int)
    Rectangle(upperLeft: Coordinates, lowerRight: Coordinates)
    """
    @property
    def Bottom(self) -> int:
        """
        Get: Bottom(self: Rectangle) -> int
        Set: Bottom(self: Rectangle) = value
        """
        ...

    @property
    def Left(self) -> int:
        """
        Get: Left(self: Rectangle) -> int
        Set: Left(self: Rectangle) = value
        """
        ...

    @property
    def Right(self) -> int:
        """
        Get: Right(self: Rectangle) -> int
        Set: Right(self: Rectangle) = value
        """
        ...

    @property
    def Top(self) -> int:
        """
        Get: Top(self: Rectangle) -> int
        Set: Top(self: Rectangle) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Rectangle, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Rectangle) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Rectangle) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Size: # skipped bases: <type 'object'>, <type 'object'>
    """ Size(width: int, height: int) """
    @property
    def Height(self) -> int:
        """
        Get: Height(self: Size) -> int
        Set: Height(self: Size) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: Size) -> int
        Set: Width(self: Size) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Size, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Size) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Size) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


