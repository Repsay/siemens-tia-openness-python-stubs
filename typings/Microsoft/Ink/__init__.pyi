# encoding: utf-8
# module Microsoft.Ink calls itself Ink
# from Microsoft.Ink, Version=6.1.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Byte, Char, Enum, EventArgs, Guid, 
    IAsyncResult, ICloneable, IDisposable, IntPtr, MulticastDelegate, Single)

from System.Collections import CollectionBase, ICollection

from System.ComponentModel import CancelEventArgs

from System.Drawing import Color, Graphics, Rectangle

from System.Drawing.Drawing2D import Matrix

from System.Web.UI import Control

from System.Windows.Forms import (IDataObject, KeyEventArgs, MouseEventArgs, 
    PaintEventArgs, PictureBox, RichTextBox)

from typing import Self, Tuple as Tuple_

from Windows.Foundation import Point

"""The following names are not found in the module: (BoundEvent, 
    CursorButtonsEnumerator, CursorsEnumerator, CustomStrokesEnumerator, 
    ExtendedPropertiesEnumerator, InkDivisionUnitsEnumerator, 
    RecognitionAlternatesEnumerator, RecognizersEnumerator, StrokesEnumerator, 
    TabletsEnumerator, field#)
"""

# no functions
# classes

class ApplicationGesture(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ApplicationGesture, values: AllGestures (0), ArrowDown (61497), ArrowLeft (61498), ArrowRight (61499), ArrowUp (61496), Check (61445), ChevronDown (61489), ChevronLeft (61490), ChevronRight (61491), ChevronUp (61488), Circle (61472), Curlicue (61456), DoubleCircle (61473), DoubleCurlicue (61457), DoubleTap (61681), Down (61529), DownLeft (61546), DownLeftLong (61542), DownRight (61547), DownRightLong (61543), DownUp (61537), Exclamation (61604), Left (61530), LeftDown (61549), LeftRight (61538), LeftUp (61548), NoGesture (61440), Right (61531), RightDown (61551), RightLeft (61539), RightUp (61550), Scratchout (61441), SemiCircleLeft (61480), SemiCircleRight (61481), Square (61443), Star (61444), Tap (61680), Triangle (61442), Up (61528), UpDown (61536), UpLeft (61544), UpLeftLong (61540), UpRight (61545), UpRightLong (61541) """
    AllGestures: ApplicationGesture = ...
    ArrowDown: ApplicationGesture = ...
    ArrowLeft: ApplicationGesture = ...
    ArrowRight: ApplicationGesture = ...
    ArrowUp: ApplicationGesture = ...
    Check: ApplicationGesture = ...
    ChevronDown: ApplicationGesture = ...
    ChevronLeft: ApplicationGesture = ...
    ChevronRight: ApplicationGesture = ...
    ChevronUp: ApplicationGesture = ...
    Circle: ApplicationGesture = ...
    Curlicue: ApplicationGesture = ...
    DoubleCircle: ApplicationGesture = ...
    DoubleCurlicue: ApplicationGesture = ...
    DoubleTap: ApplicationGesture = ...
    Down: ApplicationGesture = ...
    DownLeft: ApplicationGesture = ...
    DownLeftLong: ApplicationGesture = ...
    DownRight: ApplicationGesture = ...
    DownRightLong: ApplicationGesture = ...
    DownUp: ApplicationGesture = ...
    Exclamation: ApplicationGesture = ...
    Left: ApplicationGesture = ...
    LeftDown: ApplicationGesture = ...
    LeftRight: ApplicationGesture = ...
    LeftUp: ApplicationGesture = ...
    NoGesture: ApplicationGesture = ...
    Right: ApplicationGesture = ...
    RightDown: ApplicationGesture = ...
    RightLeft: ApplicationGesture = ...
    RightUp: ApplicationGesture = ...
    Scratchout: ApplicationGesture = ...
    SemiCircleLeft: ApplicationGesture = ...
    SemiCircleRight: ApplicationGesture = ...
    Square: ApplicationGesture = ...
    Star: ApplicationGesture = ...
    Tap: ApplicationGesture = ...
    Triangle: ApplicationGesture = ...
    Up: ApplicationGesture = ...
    UpDown: ApplicationGesture = ...
    UpLeft: ApplicationGesture = ...
    UpLeftLong: ApplicationGesture = ...
    UpRight: ApplicationGesture = ...
    UpRightLong: ApplicationGesture = ...
    value__ = ...


class BoundingBoxMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BoundingBoxMode, values: CurveFit (2), Default (0), NoCurveFit (1), PointsOnly (3), Union (4) """
    CurveFit: BoundingBoxMode = ...
    Default: BoundingBoxMode = ...
    NoCurveFit: BoundingBoxMode = ...
    PointsOnly: BoundingBoxMode = ...
    Union: BoundingBoxMode = ...
    value__ = ...


class CancelMouseEventArgs(MouseEventArgs): # skipped bases: <type 'object'>
    """ CancelMouseEventArgs(mb: MouseButtons, clicks: int, x: int, y: int, delta: int, cancel: bool) """
    @property
    def Cancel(self) -> bool:
        """
        Get: Cancel(self: CancelMouseEventArgs) -> bool
        Set: Cancel(self: CancelMouseEventArgs) = value
        """
        ...



class CollectionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CollectionMode, values: GestureOnly (1), InkAndGesture (2), InkOnly (0) """
    GestureOnly: CollectionMode = ...
    InkAndGesture: CollectionMode = ...
    InkOnly: CollectionMode = ...
    value__ = ...


class CompressionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CompressionMode, values: Default (0), Maximum (1), NoCompression (2) """
    Default: CompressionMode = ...
    Maximum: CompressionMode = ...
    NoCompression: CompressionMode = ...
    value__ = ...


class Cursor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Buttons(self) -> CursorButtons:
        """ Get: Buttons(self: Cursor) -> CursorButtons """
        ...

    @property
    def DrawingAttributes(self) -> DrawingAttributes:
        """
        Get: DrawingAttributes(self: Cursor) -> DrawingAttributes
        Set: DrawingAttributes(self: Cursor) = value
        """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: Cursor) -> int """
        ...

    @property
    def Inverted(self) -> bool:
        """ Get: Inverted(self: Cursor) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Cursor) -> str """
        ...

    @property
    def Tablet(self) -> Tablet:
        """ Get: Tablet(self: Cursor) -> Tablet """
        ...


    def ToString(self) -> str:
        """ ToString(self: Cursor) -> str """
        ...


class CursorButton: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Id(self) -> Guid:
        """ Get: Id(self: CursorButton) -> Guid """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: CursorButton) -> str """
        ...

    @property
    def State(self) -> CursorButtonState:
        """ Get: State(self: CursorButton) -> CursorButtonState """
        ...


    def ToString(self) -> str:
        """ ToString(self: CursorButton) -> str """
        ...


class CursorButtons(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def CursorButtonsEnumerator(self, *args): #cannot find CLR method
        """ CursorButtonsEnumerator(cursorButtons: CursorButtons) """
        ...

    def GetEnumerator(self): # -> CursorButtonsEnumerator
        """ GetEnumerator(self: CursorButtons) -> CursorButtonsEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class CursorButtonState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CursorButtonState, values: Down (2), Unavailable (0), Up (1) """
    Down: CursorButtonState = ...
    Unavailable: CursorButtonState = ...
    Up: CursorButtonState = ...
    value__ = ...


class Cursors(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def CursorsEnumerator(self, *args): #cannot find CLR method
        """ CursorsEnumerator(c: Cursors) """
        ...

    def GetEnumerator(self): # -> CursorsEnumerator
        """ GetEnumerator(self: Cursors) -> CursorsEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class CustomStrokes(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsFixedSize(self) -> bool:
        """ Get: IsFixedSize(self: CustomStrokes) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: CustomStrokes) -> bool """
        ...


    def Add(self, name:str, strokes:Strokes): # -> 
        """ Add(self: CustomStrokes, name: str, strokes: Strokes) """
        ...

    def Clear(self): # -> 
        """ Clear(self: CustomStrokes) """
        ...

    def CustomStrokesEnumerator(self, *args): #cannot find CLR method
        """ CustomStrokesEnumerator(cs: CustomStrokes) """
        ...

    def GetEnumerator(self): # -> CustomStrokesEnumerator
        """ GetEnumerator(self: CustomStrokes) -> CustomStrokesEnumerator """
        ...

    def Remove(self, s:str): # -> 
        """ Remove(self: CustomStrokes, s: str) """
        ...

    def RemoveAt(self, i:int): # -> 
        """ RemoveAt(self: CustomStrokes, i: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class Divider(IDisposable): # skipped bases: <type 'object'>
    """
    Divider()
    Divider(strokes: Strokes)
    Divider(strokes: Strokes, recognizerContext: RecognizerContext)
    """
    @property
    def LineHeight(self) -> int:
        """
        Get: LineHeight(self: Divider) -> int
        Set: LineHeight(self: Divider) = value
        """
        ...

    @property
    def RecognizerContext(self) -> RecognizerContext:
        """
        Get: RecognizerContext(self: Divider) -> RecognizerContext
        Set: RecognizerContext(self: Divider) = value
        """
        ...

    @property
    def Strokes(self) -> Strokes:
        """
        Get: Strokes(self: Divider) -> Strokes
        Set: Strokes(self: Divider) = value
        """
        ...


    def Divide(self) -> DivisionResult:
        """ Divide(self: Divider) -> DivisionResult """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...


class DivisionResult: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Strokes(self) -> Strokes:
        """ Get: Strokes(self: DivisionResult) -> Strokes """
        ...


    def ResultByType(self, divisionType:InkDivisionType) -> DivisionUnits:
        """ ResultByType(self: DivisionResult, divisionType: InkDivisionType) -> DivisionUnits """
        ...


class DivisionUnit: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DivisionType(self) -> InkDivisionType:
        """ Get: DivisionType(self: DivisionUnit) -> InkDivisionType """
        ...

    @property
    def RecognitionString(self) -> str:
        """ Get: RecognitionString(self: DivisionUnit) -> str """
        ...

    @property
    def Strokes(self) -> Strokes:
        """ Get: Strokes(self: DivisionUnit) -> Strokes """
        ...

    @property
    def Transform(self) -> Matrix:
        """ Get: Transform(self: DivisionUnit) -> Matrix """
        ...


    def ToString(self) -> str:
        """ ToString(self: DivisionUnit) -> str """
        ...


class DivisionUnits(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self): # -> InkDivisionUnitsEnumerator
        """ GetEnumerator(self: DivisionUnits) -> InkDivisionUnitsEnumerator """
        ...

    def InkDivisionUnitsEnumerator(self, *args): #cannot find CLR method
        """ InkDivisionUnitsEnumerator(a: DivisionUnits) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class DrawingAttributes(ICloneable): # skipped bases: <type 'object'>
    """
    DrawingAttributes()
    DrawingAttributes(color: Color)
    DrawingAttributes(width: Single)
    DrawingAttributes(pen: Pen)
    """
    @property
    def AntiAliased(self) -> bool:
        """
        Get: AntiAliased(self: DrawingAttributes) -> bool
        Set: AntiAliased(self: DrawingAttributes) = value
        """
        ...

    @property
    def Color(self) -> Color:
        """
        Get: Color(self: DrawingAttributes) -> Color
        Set: Color(self: DrawingAttributes) = value
        """
        ...

    @property
    def ExtendedProperties(self) -> ExtendedProperties:
        """ Get: ExtendedProperties(self: DrawingAttributes) -> ExtendedProperties """
        ...

    @property
    def FitToCurve(self) -> bool:
        """
        Get: FitToCurve(self: DrawingAttributes) -> bool
        Set: FitToCurve(self: DrawingAttributes) = value
        """
        ...

    @property
    def Height(self) -> Single:
        """
        Get: Height(self: DrawingAttributes) -> Single
        Set: Height(self: DrawingAttributes) = value
        """
        ...

    @property
    def IgnorePressure(self) -> bool:
        """
        Get: IgnorePressure(self: DrawingAttributes) -> bool
        Set: IgnorePressure(self: DrawingAttributes) = value
        """
        ...

    @property
    def PenTip(self) -> PenTip:
        """
        Get: PenTip(self: DrawingAttributes) -> PenTip
        Set: PenTip(self: DrawingAttributes) = value
        """
        ...

    @property
    def RasterOperation(self) -> RasterOperation:
        """
        Get: RasterOperation(self: DrawingAttributes) -> RasterOperation
        Set: RasterOperation(self: DrawingAttributes) = value
        """
        ...

    @property
    def Transparency(self) -> Byte:
        """
        Get: Transparency(self: DrawingAttributes) -> Byte
        Set: Transparency(self: DrawingAttributes) = value
        """
        ...

    @property
    def Width(self) -> Single:
        """
        Get: Width(self: DrawingAttributes) -> Single
        Set: Width(self: DrawingAttributes) = value
        """
        ...



class ExtendedProperties(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsFixedSize(self) -> bool:
        """ Get: IsFixedSize(self: ExtendedProperties) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: ExtendedProperties) -> bool """
        ...


    def Add(self, id:Guid, data:object) -> ExtendedProperty:
        """ Add(self: ExtendedProperties, id: Guid, data: object) -> ExtendedProperty """
        ...

    def Clear(self): # -> 
        """ Clear(self: ExtendedProperties) """
        ...

    def Contains(self, *__args:ExtendedProperty) -> bool:
        """
        Contains(self: ExtendedProperties, ep: ExtendedProperty) -> bool
        Contains(self: ExtendedProperties, id: Guid) -> bool
        """
        ...

    def DoesPropertyExist(self, id:Guid) -> bool:
        """ DoesPropertyExist(self: ExtendedProperties, id: Guid) -> bool """
        ...

    def ExtendedPropertiesEnumerator(self, *args): #cannot find CLR method
        """ ExtendedPropertiesEnumerator(p: ExtendedProperties) """
        ...

    def GetEnumerator(self): # -> ExtendedPropertiesEnumerator
        """ GetEnumerator(self: ExtendedProperties) -> ExtendedPropertiesEnumerator """
        ...

    def IndexOf(self, *__args:ExtendedProperty) -> int:
        """
        IndexOf(self: ExtendedProperties, ep: ExtendedProperty) -> int
        IndexOf(self: ExtendedProperties, id: Guid) -> int
        """
        ...

    def Remove(self, *__args:Guid): # -> 
        """ Remove(self: ExtendedProperties, id: Guid)Remove(self: ExtendedProperties, ep: ExtendedProperty) """
        ...

    def RemoveAt(self, i:int): # -> 
        """ RemoveAt(self: ExtendedProperties, i: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class ExtendedProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Data(self) -> object:
        """
        Get: Data(self: ExtendedProperty) -> object
        Set: Data(self: ExtendedProperty) = value
        """
        ...

    @property
    def Id(self) -> Guid:
        """ Get: Id(self: ExtendedProperty) -> Guid """
        ...



class ExtractFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ExtractFlags, values: CopyFromOriginal (0), Default (1), RemoveFromOriginal (1) """
    CopyFromOriginal: ExtractFlags = ...
    Default: ExtractFlags = ...
    RemoveFromOriginal: ExtractFlags = ...
    value__ = ...


class Factoid: # skipped bases: <type 'object'>, <type 'object'>
    """ Factoid() """
    Bopomofo: str = ...
    ChineseSimpleCommon: str = ...
    ChineseTraditionalCommon: str = ...
    Currency: str = ...
    Date: str = ...
    Default: str = ...
    Digit: str = ...
    Email: str = ...
    Filename: str = ...
    HangulCommon: str = ...
    HangulRare: str = ...
    Hiragana: str = ...
    Jamo: str = ...
    JapaneseCommon: str = ...
    KanjiCommon: str = ...
    KanjiRare: str = ...
    Katakana: str = ...
    KoreanCommon: str = ...
    LowerChar: str = ...
    Number: str = ...
    NumberSimple: str = ...
    OneChar: str = ...
    Percent: str = ...
    PostalCode: str = ...
    PuncChar: str = ...
    SystemDictionary: str = ...
    Telephone: str = ...
    Time: str = ...
    UpperChar: str = ...
    Web: str = ...
    WordList: str = ...


class Gesture: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Confidence(self) -> RecognitionConfidence:
        """ Get: Confidence(self: Gesture) -> RecognitionConfidence """
        ...

    @property
    def HotPoint(self) -> Point:
        """ Get: HotPoint(self: Gesture) -> Point """
        ...

    @property
    def Id(self) -> ApplicationGesture:
        """ Get: Id(self: Gesture) -> ApplicationGesture """
        ...



class Ink(IDisposable, ICloneable): # skipped bases: <type 'object'>
    """ Ink() """
    @property
    def CustomStrokes(self) -> CustomStrokes:
        """ Get: CustomStrokes(self: Ink) -> CustomStrokes """
        ...

    @property
    def Dirty(self) -> bool:
        """
        Get: Dirty(self: Ink) -> bool
        Set: Dirty(self: Ink) = value
        """
        ...

    @property
    def ExtendedProperties(self) -> ExtendedProperties:
        """ Get: ExtendedProperties(self: Ink) -> ExtendedProperties """
        ...

    @property
    def Strokes(self) -> Strokes:
        """ Get: Strokes(self: Ink) -> Strokes """
        ...


    def AddStrokesAtRectangle(self, strokes:Strokes, destinationRectangle:Rectangle): # -> 
        """ AddStrokesAtRectangle(self: Ink, strokes: Strokes, destinationRectangle: Rectangle) """
        ...

    def CanPaste(self, dataObject:object = ...) -> bool:
        """
        CanPaste(self: Ink) -> bool
        CanPaste(self: Ink, dataObject: object) -> bool
        """
        ...

    def Clip(self, r:Rectangle): # -> 
        """ Clip(self: Ink, r: Rectangle) """
        ...

    def ClipboardCopy(self, *__args) -> IDataObject:
        """
        ClipboardCopy(self: Ink, formats: InkClipboardFormats, modes: InkClipboardModes) -> IDataObject
        ClipboardCopy(self: Ink, strokes: Strokes, formats: InkClipboardFormats, modes: InkClipboardModes) -> IDataObject
        ClipboardCopy(self: Ink, copyRectangle: Rectangle, formats: InkClipboardFormats, modes: InkClipboardModes) -> IDataObject
        """
        ...

    def ClipboardPaste(self, pt:Point = ..., dataObject:object = ...) -> Strokes:
        """
        ClipboardPaste(self: Ink) -> Strokes
        ClipboardPaste(self: Ink, pt: Point) -> Strokes
        ClipboardPaste(self: Ink, pt: Point, dataObject: object) -> Strokes
        """
        ...

    def CreateStroke(self, *__args:Array) -> Stroke:
        """
        CreateStroke(self: Ink, points: Array[Point]) -> Stroke
        CreateStroke(self: Ink, packetData: Array[int], tabletPropertyDescriptionCollection: TabletPropertyDescriptionCollection) -> Stroke
        """
        ...

    def CreateStrokes(self, ids:Array = ...) -> Strokes:
        """
        CreateStrokes(self: Ink) -> Strokes
        CreateStrokes(self: Ink, ids: Array[int]) -> Strokes
        """
        ...

    def DeleteStroke(self, stroke:Stroke): # -> 
        """ DeleteStroke(self: Ink, stroke: Stroke) """
        ...

    def DeleteStrokes(self, strokes:Strokes = ...): # -> 
        """ DeleteStrokes(self: Ink, strokes: Strokes)DeleteStrokes(self: Ink) """
        ...

    def ExtractStrokes(self, *__args:Strokes) -> Ink:
        """
        ExtractStrokes(self: Ink, strokes: Strokes, extractionFlags: ExtractFlags) -> Ink
        ExtractStrokes(self: Ink, strokes: Strokes) -> Ink
        ExtractStrokes(self: Ink) -> Ink
        ExtractStrokes(self: Ink, extractionRectangle: Rectangle, extractionFlags: ExtractFlags) -> Ink
        ExtractStrokes(self: Ink, extractionRectangle: Rectangle) -> Ink
        """
        ...

    def GetBoundingBox(self, mode:BoundingBoxMode = ...) -> Rectangle:
        """
        GetBoundingBox(self: Ink, mode: BoundingBoxMode) -> Rectangle
        GetBoundingBox(self: Ink) -> Rectangle
        """
        ...

    def HitTest(self, *__args) -> Strokes:
        """
        HitTest(self: Ink, selectionRectangle: Rectangle, percentIntersect: Single) -> Strokes
        HitTest(self: Ink, points: Array[Point], percentIntersect: Single) -> (Strokes, Array[Point])
        HitTest(self: Ink, points: Array[Point], percentIntersect: Single) -> Strokes
        HitTest(self: Ink, point: Point, radius: Single) -> Strokes
        """
        ...

    def Load(self, inkdata:Array): # -> 
        """ Load(self: Ink, inkdata: Array[Byte]) """
        ...

    def NearestPoint(self, point, pointOnStroke=None, distanceFromPacket=None) -> Stroke:
        """
        NearestPoint(self: Ink, point: Point) -> Stroke
        NearestPoint(self: Ink, point: Point) -> (Stroke, Single)
        NearestPoint(self: Ink, point: Point) -> (Stroke, Single, Single)
        """
        ...

    def Save(self, p:PersistenceFormat = ..., c:CompressionMode = ...) -> Array:
        """
        Save(self: Ink, p: PersistenceFormat, c: CompressionMode) -> Array[Byte]
        Save(self: Ink, p: PersistenceFormat) -> Array[Byte]
        Save(self: Ink) -> Array[Byte]
        """
        ...

    InkAdded = ...
    InkDeleted = ...
    InkSerializedFormat: str = ...


class InkClipboardFormats(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) InkClipboardFormats, values: Bitmap (64), CopyMask (127), Default (127), EnhancedMetafile (8), InkSerializedFormat (1), Metafile (32), None (0), PasteMask (7), SketchInk (2), TextInk (6) """
    Bitmap: InkClipboardFormats = ...
    CopyMask: InkClipboardFormats = ...
    Default: InkClipboardFormats = ...
    EnhancedMetafile: InkClipboardFormats = ...
    InkSerializedFormat: InkClipboardFormats = ...
    Metafile: InkClipboardFormats = ...
    PasteMask: InkClipboardFormats = ...
    SketchInk: InkClipboardFormats = ...
    TextInk: InkClipboardFormats = ...
    value__ = ...


class InkClipboardModes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) InkClipboardModes, values: Copy (0), Cut (1), Default (0), DelayedCopy (32), ExtractOnly (48) """
    Copy: InkClipboardModes = ...
    Cut: InkClipboardModes = ...
    Default: InkClipboardModes = ...
    DelayedCopy: InkClipboardModes = ...
    ExtractOnly: InkClipboardModes = ...
    value__ = ...


class InkCollector(IDisposable): # skipped bases: <type 'object'>
    """
    InkCollector()
    InkCollector(handle: IntPtr)
    InkCollector(attachedControl: Control)
    InkCollector(handle: IntPtr, useMouseForInput: bool)
    InkCollector(attachedControl: Control, useMouseForInput: bool)
    InkCollector(handle: IntPtr, tablet: Tablet)
    InkCollector(attachedControl: Control, tablet: Tablet)
    """
    @property
    def AttachedControl(self) -> Control:
        """
        Get: AttachedControl(self: InkCollector) -> Control
        Set: AttachedControl(self: InkCollector) = value
        """
        ...

    @property
    def AutoRedraw(self) -> bool:
        """
        Get: AutoRedraw(self: InkCollector) -> bool
        Set: AutoRedraw(self: InkCollector) = value
        """
        ...

    @property
    def CollectingInk(self) -> bool:
        """ Get: CollectingInk(self: InkCollector) -> bool """
        ...

    @property
    def CollectionMode(self) -> CollectionMode:
        """
        Get: CollectionMode(self: InkCollector) -> CollectionMode
        Set: CollectionMode(self: InkCollector) = value
        """
        ...

    @property
    def Cursor(self) -> Cursor:
        """
        Get: Cursor(self: InkCollector) -> Cursor
        Set: Cursor(self: InkCollector) = value
        """
        ...

    @property
    def Cursors(self) -> Cursors:
        """ Get: Cursors(self: InkCollector) -> Cursors """
        ...

    @property
    def DefaultDrawingAttributes(self) -> DrawingAttributes:
        """
        Get: DefaultDrawingAttributes(self: InkCollector) -> DrawingAttributes
        Set: DefaultDrawingAttributes(self: InkCollector) = value
        """
        ...

    @property
    def DesiredPacketDescription(self) -> Array:
        """
        Get: DesiredPacketDescription(self: InkCollector) -> Array[Guid]
        Set: DesiredPacketDescription(self: InkCollector) = value
        """
        ...

    @property
    def DynamicRendering(self) -> bool:
        """
        Get: DynamicRendering(self: InkCollector) -> bool
        Set: DynamicRendering(self: InkCollector) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: InkCollector) -> bool
        Set: Enabled(self: InkCollector) = value
        """
        ...

    @property
    def Handle(self) -> IntPtr:
        """
        Get: Handle(self: InkCollector) -> IntPtr
        Set: Handle(self: InkCollector) = value
        """
        ...

    @property
    def Ink(self) -> Ink:
        """
        Get: Ink(self: InkCollector) -> Ink
        Set: Ink(self: InkCollector) = value
        """
        ...

    @property
    def MarginX(self) -> int:
        """
        Get: MarginX(self: InkCollector) -> int
        Set: MarginX(self: InkCollector) = value
        """
        ...

    @property
    def MarginY(self) -> int:
        """
        Get: MarginY(self: InkCollector) -> int
        Set: MarginY(self: InkCollector) = value
        """
        ...

    @property
    def Renderer(self) -> Renderer:
        """
        Get: Renderer(self: InkCollector) -> Renderer
        Set: Renderer(self: InkCollector) = value
        """
        ...

    @property
    def SupportHighContrastInk(self) -> bool:
        """
        Get: SupportHighContrastInk(self: InkCollector) -> bool
        Set: SupportHighContrastInk(self: InkCollector) = value
        """
        ...

    @property
    def Tablet(self) -> Tablet:
        """ Get: Tablet(self: InkCollector) -> Tablet """
        ...


    def GetGestureStatus(self, gesture:ApplicationGesture) -> bool:
        """ GetGestureStatus(self: InkCollector, gesture: ApplicationGesture) -> bool """
        ...

    def GetWindowInputRectangle(self, windowInputRectangle) -> Rectangle:
        """ GetWindowInputRectangle(self: InkCollector) -> Rectangle """
        ...

    def OnCursorButtonDown(self, *args): #cannot find CLR method
        """ OnCursorButtonDown(self: InkCollector, e: InkCollectorCursorButtonDownEventArgs) """
        ...

    def OnCursorButtonUp(self, *args): #cannot find CLR method
        """ OnCursorButtonUp(self: InkCollector, e: InkCollectorCursorButtonUpEventArgs) """
        ...

    def OnCursorDown(self, *args): #cannot find CLR method
        """ OnCursorDown(self: InkCollector, e: InkCollectorCursorDownEventArgs) """
        ...

    def OnCursorInRange(self, *args): #cannot find CLR method
        """ OnCursorInRange(self: InkCollector, e: InkCollectorCursorInRangeEventArgs) """
        ...

    def OnCursorOutOfRange(self, *args): #cannot find CLR method
        """ OnCursorOutOfRange(self: InkCollector, e: InkCollectorCursorOutOfRangeEventArgs) """
        ...

    def OnDoubleClick(self, *args): #cannot find CLR method
        """ OnDoubleClick(self: InkCollector, e: CancelEventArgs) """
        ...

    def OnGesture(self, *args): #cannot find CLR method
        """ OnGesture(self: InkCollector, e: InkCollectorGestureEventArgs) """
        ...

    def OnMouseDown(self, *args): #cannot find CLR method
        """ OnMouseDown(self: InkCollector, e: CancelMouseEventArgs) """
        ...

    def OnMouseMove(self, *args): #cannot find CLR method
        """ OnMouseMove(self: InkCollector, e: CancelMouseEventArgs) """
        ...

    def OnMouseUp(self, *args): #cannot find CLR method
        """ OnMouseUp(self: InkCollector, e: CancelMouseEventArgs) """
        ...

    def OnMouseWheel(self, *args): #cannot find CLR method
        """ OnMouseWheel(self: InkCollector, e: CancelMouseEventArgs) """
        ...

    def OnNewInAirPackets(self, *args): #cannot find CLR method
        """ OnNewInAirPackets(self: InkCollector, e: InkCollectorNewInAirPacketsEventArgs) """
        ...

    def OnNewPackets(self, *args): #cannot find CLR method
        """ OnNewPackets(self: InkCollector, e: InkCollectorNewPacketsEventArgs) """
        ...

    def OnStroke(self, *args): #cannot find CLR method
        """ OnStroke(self: InkCollector, e: InkCollectorStrokeEventArgs) """
        ...

    def OnSystemGesture(self, *args): #cannot find CLR method
        """ OnSystemGesture(self: InkCollector, e: InkCollectorSystemGestureEventArgs) """
        ...

    def OnTabletAdded(self, *args): #cannot find CLR method
        """ OnTabletAdded(self: InkCollector, e: InkCollectorTabletAddedEventArgs) """
        ...

    def OnTabletRemoved(self, *args): #cannot find CLR method
        """ OnTabletRemoved(self: InkCollector, e: InkCollectorTabletRemovedEventArgs) """
        ...

    def SetAllTabletsMode(self, useMouseForInput:bool = ...): # -> 
        """ SetAllTabletsMode(self: InkCollector)SetAllTabletsMode(self: InkCollector, useMouseForInput: bool) """
        ...

    def SetGestureStatus(self, gesture:ApplicationGesture, listening:bool): # -> 
        """ SetGestureStatus(self: InkCollector, gesture: ApplicationGesture, listening: bool) """
        ...

    def SetSingleTabletIntegratedMode(self, tablet:Tablet): # -> 
        """ SetSingleTabletIntegratedMode(self: InkCollector, tablet: Tablet) """
        ...

    def SetWindowInputRectangle(self, windowInputRectangle:Rectangle): # -> 
        """ SetWindowInputRectangle(self: InkCollector, windowInputRectangle: Rectangle) """
        ...

    ClipInkToMargin = ...
    CursorButtonDown = ...
    CursorButtonUp = ...
    CursorDown = ...
    CursorInRange = ...
    CursorOutOfRange = ...
    DefaultMargin = ...
    DoubleClick = ...
    Gesture = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...
    MouseWheel = ...
    NewInAirPackets = ...
    NewPackets = ...
    Stroke = ...
    SystemGesture = ...
    TabletAdded = ...
    TabletRemoved = ...


class InkCollectorCursorButtonDownEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkCollectorCursorButtonDownEventArgs(cursor: Cursor, button: CursorButton) """
    @property
    def Button(self) -> CursorButton:
        """ Get: Button(self: InkCollectorCursorButtonDownEventArgs) -> CursorButton """
        ...

    @property
    def Cursor(self) -> Cursor:
        """ Get: Cursor(self: InkCollectorCursorButtonDownEventArgs) -> Cursor """
        ...


    def __new__(cls, cursor:Cursor, button:CursorButton) -> Self:
        """ __new__(cls: type, cursor: Cursor, button: CursorButton) """
        ...


class InkCollectorCursorButtonDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorCursorButtonDownEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkCollectorCursorButtonDownEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorCursorButtonDownEventHandler, sender: object, e: InkCollectorCursorButtonDownEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorCursorButtonDownEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkCollectorCursorButtonDownEventArgs): # -> 
        """ Invoke(self: InkCollectorCursorButtonDownEventHandler, sender: object, e: InkCollectorCursorButtonDownEventArgs) """
        ...


class InkCollectorCursorButtonUpEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkCollectorCursorButtonUpEventArgs(cursor: Cursor, button: CursorButton) """
    @property
    def Button(self) -> CursorButton:
        """ Get: Button(self: InkCollectorCursorButtonUpEventArgs) -> CursorButton """
        ...

    @property
    def Cursor(self) -> Cursor:
        """ Get: Cursor(self: InkCollectorCursorButtonUpEventArgs) -> Cursor """
        ...


    def __new__(cls, cursor:Cursor, button:CursorButton) -> Self:
        """ __new__(cls: type, cursor: Cursor, button: CursorButton) """
        ...


class InkCollectorCursorButtonUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorCursorButtonUpEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkCollectorCursorButtonUpEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorCursorButtonUpEventHandler, sender: object, e: InkCollectorCursorButtonUpEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorCursorButtonUpEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkCollectorCursorButtonUpEventArgs): # -> 
        """ Invoke(self: InkCollectorCursorButtonUpEventHandler, sender: object, e: InkCollectorCursorButtonUpEventArgs) """
        ...


class InkCollectorCursorDownEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkCollectorCursorDownEventArgs(cursor: Cursor, stroke: Stroke) """
    @property
    def Cursor(self) -> Cursor:
        """ Get: Cursor(self: InkCollectorCursorDownEventArgs) -> Cursor """
        ...

    @property
    def Stroke(self) -> Stroke:
        """ Get: Stroke(self: InkCollectorCursorDownEventArgs) -> Stroke """
        ...


    def __new__(cls, cursor:Cursor, stroke:Stroke) -> Self:
        """ __new__(cls: type, cursor: Cursor, stroke: Stroke) """
        ...


class InkCollectorCursorDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorCursorDownEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkCollectorCursorDownEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorCursorDownEventHandler, sender: object, e: InkCollectorCursorDownEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorCursorDownEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkCollectorCursorDownEventArgs): # -> 
        """ Invoke(self: InkCollectorCursorDownEventHandler, sender: object, e: InkCollectorCursorDownEventArgs) """
        ...


class InkCollectorCursorInRangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkCollectorCursorInRangeEventArgs(cursor: Cursor, newCursor: bool, buttonStates: Array[CursorButtonState]) """
    @property
    def ButtonStates(self) -> Array:
        """ Get: ButtonStates(self: InkCollectorCursorInRangeEventArgs) -> Array[CursorButtonState] """
        ...

    @property
    def Cursor(self) -> Cursor:
        """ Get: Cursor(self: InkCollectorCursorInRangeEventArgs) -> Cursor """
        ...

    @property
    def NewCursor(self) -> bool:
        """ Get: NewCursor(self: InkCollectorCursorInRangeEventArgs) -> bool """
        ...


    def __new__(cls, cursor:Cursor, newCursor:bool, buttonStates:Array) -> Self:
        """ __new__(cls: type, cursor: Cursor, newCursor: bool, buttonStates: Array[CursorButtonState]) """
        ...


class InkCollectorCursorInRangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorCursorInRangeEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkCollectorCursorInRangeEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorCursorInRangeEventHandler, sender: object, e: InkCollectorCursorInRangeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorCursorInRangeEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkCollectorCursorInRangeEventArgs): # -> 
        """ Invoke(self: InkCollectorCursorInRangeEventHandler, sender: object, e: InkCollectorCursorInRangeEventArgs) """
        ...


class InkCollectorCursorOutOfRangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkCollectorCursorOutOfRangeEventArgs(cursor: Cursor) """
    @property
    def Cursor(self) -> Cursor:
        """ Get: Cursor(self: InkCollectorCursorOutOfRangeEventArgs) -> Cursor """
        ...


    def __new__(cls, cursor:Cursor) -> Self:
        """ __new__(cls: type, cursor: Cursor) """
        ...


class InkCollectorCursorOutOfRangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorCursorOutOfRangeEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkCollectorCursorOutOfRangeEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorCursorOutOfRangeEventHandler, sender: object, e: InkCollectorCursorOutOfRangeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorCursorOutOfRangeEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkCollectorCursorOutOfRangeEventArgs): # -> 
        """ Invoke(self: InkCollectorCursorOutOfRangeEventHandler, sender: object, e: InkCollectorCursorOutOfRangeEventArgs) """
        ...


class InkCollectorDoubleClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorDoubleClickEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:CancelEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorDoubleClickEventHandler, sender: object, e: CancelEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorDoubleClickEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:CancelEventArgs): # -> 
        """ Invoke(self: InkCollectorDoubleClickEventHandler, sender: object, e: CancelEventArgs) """
        ...


class InkCollectorGestureEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ InkCollectorGestureEventArgs(cursor: Cursor, strokes: Strokes, gestures: Array[Gesture], cancel: bool) """
    @property
    def Cursor(self) -> Cursor:
        """ Get: Cursor(self: InkCollectorGestureEventArgs) -> Cursor """
        ...

    @property
    def Gestures(self) -> Array:
        """ Get: Gestures(self: InkCollectorGestureEventArgs) -> Array[Gesture] """
        ...

    @property
    def Strokes(self) -> Strokes:
        """ Get: Strokes(self: InkCollectorGestureEventArgs) -> Strokes """
        ...



class InkCollectorGestureEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorGestureEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkCollectorGestureEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorGestureEventHandler, sender: object, e: InkCollectorGestureEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorGestureEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkCollectorGestureEventArgs): # -> 
        """ Invoke(self: InkCollectorGestureEventHandler, sender: object, e: InkCollectorGestureEventArgs) """
        ...


class InkCollectorMouseDownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorMouseDownEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:CancelMouseEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorMouseDownEventHandler, sender: object, e: CancelMouseEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorMouseDownEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:CancelMouseEventArgs): # -> 
        """ Invoke(self: InkCollectorMouseDownEventHandler, sender: object, e: CancelMouseEventArgs) """
        ...


class InkCollectorMouseMoveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorMouseMoveEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:CancelMouseEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorMouseMoveEventHandler, sender: object, e: CancelMouseEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorMouseMoveEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:CancelMouseEventArgs): # -> 
        """ Invoke(self: InkCollectorMouseMoveEventHandler, sender: object, e: CancelMouseEventArgs) """
        ...


class InkCollectorMouseUpEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorMouseUpEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:CancelMouseEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorMouseUpEventHandler, sender: object, e: CancelMouseEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorMouseUpEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:CancelMouseEventArgs): # -> 
        """ Invoke(self: InkCollectorMouseUpEventHandler, sender: object, e: CancelMouseEventArgs) """
        ...


class InkCollectorMouseWheelEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorMouseWheelEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:CancelMouseEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorMouseWheelEventHandler, sender: object, e: CancelMouseEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorMouseWheelEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:CancelMouseEventArgs): # -> 
        """ Invoke(self: InkCollectorMouseWheelEventHandler, sender: object, e: CancelMouseEventArgs) """
        ...


class InkCollectorNewInAirPacketsEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkCollectorNewInAirPacketsEventArgs(cursor: Cursor, packetCount: int, packetData: Array[int]) """
    @property
    def Cursor(self) -> Cursor:
        """ Get: Cursor(self: InkCollectorNewInAirPacketsEventArgs) -> Cursor """
        ...

    @property
    def PacketCount(self) -> int:
        """ Get: PacketCount(self: InkCollectorNewInAirPacketsEventArgs) -> int """
        ...

    @property
    def PacketData(self) -> Array:
        """ Get: PacketData(self: InkCollectorNewInAirPacketsEventArgs) -> Array[int] """
        ...


    def __new__(cls, cursor:Cursor, packetCount:int, packetData:Array) -> Self:
        """ __new__(cls: type, cursor: Cursor, packetCount: int, packetData: Array[int]) """
        ...


class InkCollectorNewInAirPacketsEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorNewInAirPacketsEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkCollectorNewInAirPacketsEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorNewInAirPacketsEventHandler, sender: object, e: InkCollectorNewInAirPacketsEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorNewInAirPacketsEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkCollectorNewInAirPacketsEventArgs): # -> 
        """ Invoke(self: InkCollectorNewInAirPacketsEventHandler, sender: object, e: InkCollectorNewInAirPacketsEventArgs) """
        ...


class InkCollectorNewPacketsEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkCollectorNewPacketsEventArgs(cursor: Cursor, stroke: Stroke, packetCount: int, packetData: Array[int]) """
    @property
    def Cursor(self) -> Cursor:
        """ Get: Cursor(self: InkCollectorNewPacketsEventArgs) -> Cursor """
        ...

    @property
    def PacketCount(self) -> int:
        """ Get: PacketCount(self: InkCollectorNewPacketsEventArgs) -> int """
        ...

    @property
    def PacketData(self) -> Array:
        """ Get: PacketData(self: InkCollectorNewPacketsEventArgs) -> Array[int] """
        ...

    @property
    def Stroke(self) -> Stroke:
        """ Get: Stroke(self: InkCollectorNewPacketsEventArgs) -> Stroke """
        ...


    def __new__(cls, cursor:Cursor, stroke:Stroke, packetCount:int, packetData:Array) -> Self:
        """ __new__(cls: type, cursor: Cursor, stroke: Stroke, packetCount: int, packetData: Array[int]) """
        ...


class InkCollectorNewPacketsEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorNewPacketsEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkCollectorNewPacketsEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorNewPacketsEventHandler, sender: object, e: InkCollectorNewPacketsEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorNewPacketsEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkCollectorNewPacketsEventArgs): # -> 
        """ Invoke(self: InkCollectorNewPacketsEventHandler, sender: object, e: InkCollectorNewPacketsEventArgs) """
        ...


class InkCollectorStrokeEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ InkCollectorStrokeEventArgs(cursor: Cursor, stroke: Stroke, cancel: bool) """
    @property
    def Cursor(self) -> Cursor:
        """ Get: Cursor(self: InkCollectorStrokeEventArgs) -> Cursor """
        ...

    @property
    def Stroke(self) -> Stroke:
        """ Get: Stroke(self: InkCollectorStrokeEventArgs) -> Stroke """
        ...



class InkCollectorStrokeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorStrokeEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkCollectorStrokeEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorStrokeEventHandler, sender: object, e: InkCollectorStrokeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorStrokeEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkCollectorStrokeEventArgs): # -> 
        """ Invoke(self: InkCollectorStrokeEventHandler, sender: object, e: InkCollectorStrokeEventArgs) """
        ...


class InkCollectorSystemGestureEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkCollectorSystemGestureEventArgs(cursor: Cursor, id: SystemGesture, pt: Point, modifier: int, c: Char, mode: int) """
    @property
    def Character(self) -> Char:
        """ Get: Character(self: InkCollectorSystemGestureEventArgs) -> Char """
        ...

    @property
    def Cursor(self) -> Cursor:
        """ Get: Cursor(self: InkCollectorSystemGestureEventArgs) -> Cursor """
        ...

    @property
    def CursorMode(self) -> int:
        """ Get: CursorMode(self: InkCollectorSystemGestureEventArgs) -> int """
        ...

    @property
    def Id(self) -> SystemGesture:
        """ Get: Id(self: InkCollectorSystemGestureEventArgs) -> SystemGesture """
        ...

    @property
    def Modifier(self) -> int:
        """ Get: Modifier(self: InkCollectorSystemGestureEventArgs) -> int """
        ...

    @property
    def Point(self) -> Point:
        """ Get: Point(self: InkCollectorSystemGestureEventArgs) -> Point """
        ...


    def __new__(cls, cursor:Cursor, id:SystemGesture, pt:Point, modifier:int, c:Char, mode:int) -> Self:
        """ __new__(cls: type, cursor: Cursor, id: SystemGesture, pt: Point, modifier: int, c: Char, mode: int) """
        ...


class InkCollectorSystemGestureEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorSystemGestureEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkCollectorSystemGestureEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorSystemGestureEventHandler, sender: object, e: InkCollectorSystemGestureEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorSystemGestureEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkCollectorSystemGestureEventArgs): # -> 
        """ Invoke(self: InkCollectorSystemGestureEventHandler, sender: object, e: InkCollectorSystemGestureEventArgs) """
        ...


class InkCollectorTabletAddedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkCollectorTabletAddedEventArgs(tablet: Tablet) """
    @property
    def Tablet(self) -> Tablet:
        """ Get: Tablet(self: InkCollectorTabletAddedEventArgs) -> Tablet """
        ...


    def __new__(cls, tablet:Tablet) -> Self:
        """ __new__(cls: type, tablet: Tablet) """
        ...


class InkCollectorTabletAddedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorTabletAddedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkCollectorTabletAddedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorTabletAddedEventHandler, sender: object, e: InkCollectorTabletAddedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorTabletAddedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkCollectorTabletAddedEventArgs): # -> 
        """ Invoke(self: InkCollectorTabletAddedEventHandler, sender: object, e: InkCollectorTabletAddedEventArgs) """
        ...


class InkCollectorTabletRemovedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkCollectorTabletRemovedEventArgs(tabletId: int) """
    @property
    def TabletId(self) -> int:
        """ Get: TabletId(self: InkCollectorTabletRemovedEventArgs) -> int """
        ...


    def __new__(cls, tabletId:int) -> Self:
        """ __new__(cls: type, tabletId: int) """
        ...


class InkCollectorTabletRemovedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkCollectorTabletRemovedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkCollectorTabletRemovedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkCollectorTabletRemovedEventHandler, sender: object, e: InkCollectorTabletRemovedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkCollectorTabletRemovedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkCollectorTabletRemovedEventArgs): # -> 
        """ Invoke(self: InkCollectorTabletRemovedEventHandler, sender: object, e: InkCollectorTabletRemovedEventArgs) """
        ...


class InkDisplayMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InkDisplayMode, values: Ink (0), Text (1) """
    Ink: InkDisplayMode = ...
    Text: InkDisplayMode = ...
    value__ = ...


class InkDivisionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InkDivisionType, values: Drawing (3), Line (1), Paragraph (2), Segment (0) """
    Drawing: InkDivisionType = ...
    Line: InkDivisionType = ...
    Paragraph: InkDivisionType = ...
    Segment: InkDivisionType = ...
    value__ = ...


class InkEdit(RichTextBox): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IOleObject'>, <type 'IPersistStorage'>, <type 'IViewObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IViewObject2'>, <type 'IOleInPlaceObject'>, <type 'object'>
    """ InkEdit() """
    @property
    def Cursor(self) -> Cursor:
        """
        Get: Cursor(self: InkEdit) -> Cursor
        Set: Cursor(self: InkEdit) = value
        """
        ...

    @property
    def Disposing(self) -> bool:
        """ Get: Disposing(self: InkEdit) -> bool """
        ...

    @property
    def DrawingAttributes(self) -> DrawingAttributes:
        """
        Get: DrawingAttributes(self: InkEdit) -> DrawingAttributes
        Set: DrawingAttributes(self: InkEdit) = value
        """
        ...

    @property
    def Factoid(self) -> str:
        """
        Get: Factoid(self: InkEdit) -> str
        Set: Factoid(self: InkEdit) = value
        """
        ...

    @property
    def InkInsertMode(self) -> InkInsertMode:
        """
        Get: InkInsertMode(self: InkEdit) -> InkInsertMode
        Set: InkInsertMode(self: InkEdit) = value
        """
        ...

    @property
    def InkMode(self) -> InkMode:
        """
        Get: InkMode(self: InkEdit) -> InkMode
        Set: InkMode(self: InkEdit) = value
        """
        ...

    @property
    def Recognizer(self) -> Recognizer:
        """
        Get: Recognizer(self: InkEdit) -> Recognizer
        Set: Recognizer(self: InkEdit) = value
        """
        ...

    @property
    def RecoTimeout(self) -> int:
        """
        Get: RecoTimeout(self: InkEdit) -> int
        Set: RecoTimeout(self: InkEdit) = value
        """
        ...

    @property
    def SelInks(self) -> Array:
        """
        Get: SelInks(self: InkEdit) -> Array[Ink]
        Set: SelInks(self: InkEdit) = value
        """
        ...

    @property
    def SelInksDisplayMode(self) -> InkDisplayMode:
        """
        Get: SelInksDisplayMode(self: InkEdit) -> InkDisplayMode
        Set: SelInksDisplayMode(self: InkEdit) = value
        """
        ...

    @property
    def Status(self) -> InkEditStatus:
        """ Get: Status(self: InkEdit) -> InkEditStatus """
        ...

    @property
    def UseMouseForInput(self) -> bool:
        """
        Get: UseMouseForInput(self: InkEdit) -> bool
        Set: UseMouseForInput(self: InkEdit) = value
        """
        ...


    def GetGestureStatus(self, gesture:ApplicationGesture) -> bool:
        """ GetGestureStatus(self: InkEdit, gesture: ApplicationGesture) -> bool """
        ...

    def OnGesture(self, *args): #cannot find CLR method
        """ OnGesture(self: InkEdit, e: InkEditGestureEventArgs) """
        ...

    def OnRecognition(self, *args): #cannot find CLR method
        """ OnRecognition(self: InkEdit, e: InkEditRecognitionEventArgs) """
        ...

    def OnStroke(self, *args): #cannot find CLR method
        """ OnStroke(self: InkEdit, e: InkEditStrokeEventArgs) """
        ...

    def Recognize(self): # -> 
        """ Recognize(self: InkEdit) """
        ...

    def SetGestureStatus(self, gesture:ApplicationGesture, listening:bool): # -> 
        """ SetGestureStatus(self: InkEdit, gesture: ApplicationGesture, listening: bool) """
        ...

    Gesture = ...
    Recognition = ...
    Stroke = ...


class InkEditGestureEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ InkEditGestureEventArgs(cursor: Cursor, strokes: Strokes, gestures: Array[Gesture], cancel: bool) """
    @property
    def Cursor(self) -> Cursor:
        """ Get: Cursor(self: InkEditGestureEventArgs) -> Cursor """
        ...

    @property
    def Gestures(self) -> Array:
        """ Get: Gestures(self: InkEditGestureEventArgs) -> Array[Gesture] """
        ...

    @property
    def Strokes(self) -> Strokes:
        """ Get: Strokes(self: InkEditGestureEventArgs) -> Strokes """
        ...



class InkEditGestureEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkEditGestureEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkEditGestureEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkEditGestureEventHandler, sender: object, e: InkEditGestureEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkEditGestureEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkEditGestureEventArgs): # -> 
        """ Invoke(self: InkEditGestureEventHandler, sender: object, e: InkEditGestureEventArgs) """
        ...


class InkEditRecognitionEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkEditRecognitionEventArgs(recognitionResult: RecognitionResult) """
    @property
    def RecognitionResult(self) -> RecognitionResult:
        """ Get: RecognitionResult(self: InkEditRecognitionEventArgs) -> RecognitionResult """
        ...


    def __new__(cls, recognitionResult:RecognitionResult) -> Self:
        """ __new__(cls: type, recognitionResult: RecognitionResult) """
        ...


class InkEditRecognitionEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkEditRecognitionEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkEditRecognitionEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkEditRecognitionEventHandler, sender: object, e: InkEditRecognitionEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkEditRecognitionEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkEditRecognitionEventArgs): # -> 
        """ Invoke(self: InkEditRecognitionEventHandler, sender: object, e: InkEditRecognitionEventArgs) """
        ...


class InkEditStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InkEditStatus, values: Collecting (1), Idle (0), Recognizing (2) """
    Collecting: InkEditStatus = ...
    Idle: InkEditStatus = ...
    Recognizing: InkEditStatus = ...
    value__ = ...


class InkEditStrokeEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ InkEditStrokeEventArgs(cursor: Cursor, stroke: Stroke, cancel: bool) """
    @property
    def Cursor(self) -> Cursor:
        """ Get: Cursor(self: InkEditStrokeEventArgs) -> Cursor """
        ...

    @property
    def Stroke(self) -> Stroke:
        """ Get: Stroke(self: InkEditStrokeEventArgs) -> Stroke """
        ...



class InkEditStrokeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkEditStrokeEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkEditStrokeEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkEditStrokeEventHandler, sender: object, e: InkEditStrokeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkEditStrokeEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkEditStrokeEventArgs): # -> 
        """ Invoke(self: InkEditStrokeEventHandler, sender: object, e: InkEditStrokeEventArgs) """
        ...


class InkInsertMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InkInsertMode, values: InsertAsInk (1), InsertAsText (0) """
    InsertAsInk: InkInsertMode = ...
    InsertAsText: InkInsertMode = ...
    value__ = ...


class InkMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InkMode, values: Disabled (0), Ink (1), InkAndGesture (2) """
    Disabled: InkMode = ...
    Ink: InkMode = ...
    InkAndGesture: InkMode = ...
    value__ = ...


class InkOverlay(IDisposable): # skipped bases: <type 'object'>
    """
    InkOverlay()
    InkOverlay(handle: IntPtr)
    InkOverlay(attachedControl: Control)
    InkOverlay(handle: IntPtr, useMouseForInput: bool)
    InkOverlay(attachedControl: Control, useMouseForInput: bool)
    InkOverlay(handle: IntPtr, tablet: Tablet)
    InkOverlay(attachedControl: Control, tablet: Tablet)
    """
    @property
    def AttachedControl(self) -> Control:
        """
        Get: AttachedControl(self: InkOverlay) -> Control
        Set: AttachedControl(self: InkOverlay) = value
        """
        ...

    @property
    def AttachMode(self) -> InkOverlayAttachMode:
        """
        Get: AttachMode(self: InkOverlay) -> InkOverlayAttachMode
        Set: AttachMode(self: InkOverlay) = value
        """
        ...

    @property
    def AutoRedraw(self) -> bool:
        """
        Get: AutoRedraw(self: InkOverlay) -> bool
        Set: AutoRedraw(self: InkOverlay) = value
        """
        ...

    @property
    def CollectingInk(self) -> bool:
        """ Get: CollectingInk(self: InkOverlay) -> bool """
        ...

    @property
    def CollectionMode(self) -> CollectionMode:
        """
        Get: CollectionMode(self: InkOverlay) -> CollectionMode
        Set: CollectionMode(self: InkOverlay) = value
        """
        ...

    @property
    def Cursor(self) -> Cursor:
        """
        Get: Cursor(self: InkOverlay) -> Cursor
        Set: Cursor(self: InkOverlay) = value
        """
        ...

    @property
    def Cursors(self) -> Cursors:
        """ Get: Cursors(self: InkOverlay) -> Cursors """
        ...

    @property
    def DefaultDrawingAttributes(self) -> DrawingAttributes:
        """
        Get: DefaultDrawingAttributes(self: InkOverlay) -> DrawingAttributes
        Set: DefaultDrawingAttributes(self: InkOverlay) = value
        """
        ...

    @property
    def DesiredPacketDescription(self) -> Array:
        """
        Get: DesiredPacketDescription(self: InkOverlay) -> Array[Guid]
        Set: DesiredPacketDescription(self: InkOverlay) = value
        """
        ...

    @property
    def DynamicRendering(self) -> bool:
        """
        Get: DynamicRendering(self: InkOverlay) -> bool
        Set: DynamicRendering(self: InkOverlay) = value
        """
        ...

    @property
    def EditingMode(self) -> InkOverlayEditingMode:
        """
        Get: EditingMode(self: InkOverlay) -> InkOverlayEditingMode
        Set: EditingMode(self: InkOverlay) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: InkOverlay) -> bool
        Set: Enabled(self: InkOverlay) = value
        """
        ...

    @property
    def EraserMode(self) -> InkOverlayEraserMode:
        """
        Get: EraserMode(self: InkOverlay) -> InkOverlayEraserMode
        Set: EraserMode(self: InkOverlay) = value
        """
        ...

    @property
    def EraserWidth(self) -> int:
        """
        Get: EraserWidth(self: InkOverlay) -> int
        Set: EraserWidth(self: InkOverlay) = value
        """
        ...

    @property
    def Handle(self) -> IntPtr:
        """
        Get: Handle(self: InkOverlay) -> IntPtr
        Set: Handle(self: InkOverlay) = value
        """
        ...

    @property
    def Ink(self) -> Ink:
        """
        Get: Ink(self: InkOverlay) -> Ink
        Set: Ink(self: InkOverlay) = value
        """
        ...

    @property
    def MarginX(self) -> int:
        """
        Get: MarginX(self: InkOverlay) -> int
        Set: MarginX(self: InkOverlay) = value
        """
        ...

    @property
    def MarginY(self) -> int:
        """
        Get: MarginY(self: InkOverlay) -> int
        Set: MarginY(self: InkOverlay) = value
        """
        ...

    @property
    def Renderer(self) -> Renderer:
        """
        Get: Renderer(self: InkOverlay) -> Renderer
        Set: Renderer(self: InkOverlay) = value
        """
        ...

    @property
    def Selection(self) -> Strokes:
        """
        Get: Selection(self: InkOverlay) -> Strokes
        Set: Selection(self: InkOverlay) = value
        """
        ...

    @property
    def SupportHighContrastInk(self) -> bool:
        """
        Get: SupportHighContrastInk(self: InkOverlay) -> bool
        Set: SupportHighContrastInk(self: InkOverlay) = value
        """
        ...

    @property
    def SupportHighContrastSelectionUI(self) -> bool:
        """
        Get: SupportHighContrastSelectionUI(self: InkOverlay) -> bool
        Set: SupportHighContrastSelectionUI(self: InkOverlay) = value
        """
        ...

    @property
    def Tablet(self) -> Tablet:
        """ Get: Tablet(self: InkOverlay) -> Tablet """
        ...


    def Draw(self, rDrawRect:Rectangle): # -> 
        """ Draw(self: InkOverlay, rDrawRect: Rectangle) """
        ...

    def GetGestureStatus(self, gesture:ApplicationGesture) -> bool:
        """ GetGestureStatus(self: InkOverlay, gesture: ApplicationGesture) -> bool """
        ...

    def GetWindowInputRectangle(self, windowInputRectangle) -> Rectangle:
        """ GetWindowInputRectangle(self: InkOverlay) -> Rectangle """
        ...

    def HitTestSelection(self, X:int, Y:int) -> SelectionHitResult:
        """ HitTestSelection(self: InkOverlay, X: int, Y: int) -> SelectionHitResult """
        ...

    def OnCursorButtonDown(self, *args): #cannot find CLR method
        """ OnCursorButtonDown(self: InkOverlay, e: InkCollectorCursorButtonDownEventArgs) """
        ...

    def OnCursorButtonUp(self, *args): #cannot find CLR method
        """ OnCursorButtonUp(self: InkOverlay, e: InkCollectorCursorButtonUpEventArgs) """
        ...

    def OnCursorDown(self, *args): #cannot find CLR method
        """ OnCursorDown(self: InkOverlay, e: InkCollectorCursorDownEventArgs) """
        ...

    def OnCursorInRange(self, *args): #cannot find CLR method
        """ OnCursorInRange(self: InkOverlay, e: InkCollectorCursorInRangeEventArgs) """
        ...

    def OnCursorOutOfRange(self, *args): #cannot find CLR method
        """ OnCursorOutOfRange(self: InkOverlay, e: InkCollectorCursorOutOfRangeEventArgs) """
        ...

    def OnDoubleClick(self, *args): #cannot find CLR method
        """ OnDoubleClick(self: InkOverlay, e: CancelEventArgs) """
        ...

    def OnGesture(self, *args): #cannot find CLR method
        """ OnGesture(self: InkOverlay, e: InkCollectorGestureEventArgs) """
        ...

    def OnMouseDown(self, *args): #cannot find CLR method
        """ OnMouseDown(self: InkOverlay, e: CancelMouseEventArgs) """
        ...

    def OnMouseMove(self, *args): #cannot find CLR method
        """ OnMouseMove(self: InkOverlay, e: CancelMouseEventArgs) """
        ...

    def OnMouseUp(self, *args): #cannot find CLR method
        """ OnMouseUp(self: InkOverlay, e: CancelMouseEventArgs) """
        ...

    def OnMouseWheel(self, *args): #cannot find CLR method
        """ OnMouseWheel(self: InkOverlay, e: CancelMouseEventArgs) """
        ...

    def OnNewInAirPackets(self, *args): #cannot find CLR method
        """ OnNewInAirPackets(self: InkOverlay, e: InkCollectorNewInAirPacketsEventArgs) """
        ...

    def OnNewPackets(self, *args): #cannot find CLR method
        """ OnNewPackets(self: InkOverlay, e: InkCollectorNewPacketsEventArgs) """
        ...

    def OnPainted(self, *args): #cannot find CLR method
        """ OnPainted(self: InkOverlay, e: PaintEventArgs) """
        ...

    def OnPainting(self, *args): #cannot find CLR method
        """ OnPainting(self: InkOverlay, e: InkOverlayPaintingEventArgs) """
        ...

    def OnSelectionChanged(self, *args): #cannot find CLR method
        """ OnSelectionChanged(self: InkOverlay, e: EventArgs) """
        ...

    def OnSelectionChanging(self, *args): #cannot find CLR method
        """ OnSelectionChanging(self: InkOverlay, e: InkOverlaySelectionChangingEventArgs) """
        ...

    def OnSelectionMoved(self, *args): #cannot find CLR method
        """ OnSelectionMoved(self: InkOverlay, e: InkOverlaySelectionMovedEventArgs) """
        ...

    def OnSelectionMoving(self, *args): #cannot find CLR method
        """ OnSelectionMoving(self: InkOverlay, e: InkOverlaySelectionMovingEventArgs) """
        ...

    def OnSelectionResized(self, *args): #cannot find CLR method
        """ OnSelectionResized(self: InkOverlay, e: InkOverlaySelectionResizedEventArgs) """
        ...

    def OnSelectionResizing(self, *args): #cannot find CLR method
        """ OnSelectionResizing(self: InkOverlay, e: InkOverlaySelectionResizingEventArgs) """
        ...

    def OnStroke(self, *args): #cannot find CLR method
        """ OnStroke(self: InkOverlay, e: InkCollectorStrokeEventArgs) """
        ...

    def OnStrokesDeleted(self, *args): #cannot find CLR method
        """ OnStrokesDeleted(self: InkOverlay, e: EventArgs) """
        ...

    def OnStrokesDeleting(self, *args): #cannot find CLR method
        """ OnStrokesDeleting(self: InkOverlay, e: InkOverlayStrokesDeletingEventArgs) """
        ...

    def OnSystemGesture(self, *args): #cannot find CLR method
        """ OnSystemGesture(self: InkOverlay, e: InkCollectorSystemGestureEventArgs) """
        ...

    def OnTabletAdded(self, *args): #cannot find CLR method
        """ OnTabletAdded(self: InkOverlay, e: InkCollectorTabletAddedEventArgs) """
        ...

    def OnTabletRemoved(self, *args): #cannot find CLR method
        """ OnTabletRemoved(self: InkOverlay, e: InkCollectorTabletRemovedEventArgs) """
        ...

    def SetAllTabletsMode(self, useMouseForInput:bool = ...): # -> 
        """ SetAllTabletsMode(self: InkOverlay)SetAllTabletsMode(self: InkOverlay, useMouseForInput: bool) """
        ...

    def SetGestureStatus(self, gesture:ApplicationGesture, listening:bool): # -> 
        """ SetGestureStatus(self: InkOverlay, gesture: ApplicationGesture, listening: bool) """
        ...

    def SetSingleTabletIntegratedMode(self, tablet:Tablet): # -> 
        """ SetSingleTabletIntegratedMode(self: InkOverlay, tablet: Tablet) """
        ...

    def SetWindowInputRectangle(self, windowInputRectangle:Rectangle): # -> 
        """ SetWindowInputRectangle(self: InkOverlay, windowInputRectangle: Rectangle) """
        ...

    ClipInkToMargin = ...
    CursorButtonDown = ...
    CursorButtonUp = ...
    CursorDown = ...
    CursorInRange = ...
    CursorOutOfRange = ...
    DefaultMargin = ...
    DoubleClick = ...
    Gesture = ...
    MouseDown = ...
    MouseMove = ...
    MouseUp = ...
    MouseWheel = ...
    NewInAirPackets = ...
    NewPackets = ...
    Painted = ...
    Painting = ...
    SelectionChanged = ...
    SelectionChanging = ...
    SelectionMoved = ...
    SelectionMoving = ...
    SelectionResized = ...
    SelectionResizing = ...
    Stroke = ...
    StrokesDeleted = ...
    StrokesDeleting = ...
    SystemGesture = ...
    TabletAdded = ...
    TabletRemoved = ...


class InkOverlayAttachMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InkOverlayAttachMode, values: Behind (0), InFront (1) """
    Behind: InkOverlayAttachMode = ...
    InFront: InkOverlayAttachMode = ...
    value__ = ...


class InkOverlayEditingMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InkOverlayEditingMode, values: Delete (1), Ink (0), Select (2) """
    Delete: InkOverlayEditingMode = ...
    Ink: InkOverlayEditingMode = ...
    Select: InkOverlayEditingMode = ...
    value__ = ...


class InkOverlayEraserMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InkOverlayEraserMode, values: PointErase (1), StrokeErase (0) """
    PointErase: InkOverlayEraserMode = ...
    StrokeErase: InkOverlayEraserMode = ...
    value__ = ...


class InkOverlayPaintedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkOverlayPaintedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:PaintEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkOverlayPaintedEventHandler, sender: object, e: PaintEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkOverlayPaintedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:PaintEventArgs): # -> 
        """ Invoke(self: InkOverlayPaintedEventHandler, sender: object, e: PaintEventArgs) """
        ...


class InkOverlayPaintingEventArgs(CancelEventArgs, IDisposable): # skipped bases: <type 'object'>
    """ InkOverlayPaintingEventArgs(graphics: Graphics, clipRectangle: Rectangle, Allow: bool) """
    @property
    def ClipRectangle(self) -> Rectangle:
        """ Get: ClipRectangle(self: InkOverlayPaintingEventArgs) -> Rectangle """
        ...

    @property
    def Graphics(self) -> Graphics:
        """ Get: Graphics(self: InkOverlayPaintingEventArgs) -> Graphics """
        ...



class InkOverlayPaintingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkOverlayPaintingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkOverlayPaintingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkOverlayPaintingEventHandler, sender: object, e: InkOverlayPaintingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkOverlayPaintingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkOverlayPaintingEventArgs): # -> 
        """ Invoke(self: InkOverlayPaintingEventHandler, sender: object, e: InkOverlayPaintingEventArgs) """
        ...


class InkOverlaySelectionChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkOverlaySelectionChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:EventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkOverlaySelectionChangedEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkOverlaySelectionChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:EventArgs): # -> 
        """ Invoke(self: InkOverlaySelectionChangedEventHandler, sender: object, e: EventArgs) """
        ...


class InkOverlaySelectionChangingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkOverlaySelectionChangingEventArgs(newSelection: Strokes) """
    @property
    def NewSelection(self) -> Strokes:
        """ Get: NewSelection(self: InkOverlaySelectionChangingEventArgs) -> Strokes """
        ...


    def __new__(cls, newSelection:Strokes) -> Self:
        """ __new__(cls: type, newSelection: Strokes) """
        ...


class InkOverlaySelectionChangingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkOverlaySelectionChangingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkOverlaySelectionChangingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkOverlaySelectionChangingEventHandler, sender: object, e: InkOverlaySelectionChangingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkOverlaySelectionChangingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkOverlaySelectionChangingEventArgs): # -> 
        """ Invoke(self: InkOverlaySelectionChangingEventHandler, sender: object, e: InkOverlaySelectionChangingEventArgs) """
        ...


class InkOverlaySelectionMovedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkOverlaySelectionMovedEventArgs(oldSelectionBoundingRect: Rectangle) """
    @property
    def OldSelectionBoundingRect(self) -> Rectangle:
        """ Get: OldSelectionBoundingRect(self: InkOverlaySelectionMovedEventArgs) -> Rectangle """
        ...


    def __new__(cls, oldSelectionBoundingRect:Rectangle) -> Self:
        """ __new__(cls: type, oldSelectionBoundingRect: Rectangle) """
        ...


class InkOverlaySelectionMovedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkOverlaySelectionMovedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkOverlaySelectionMovedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkOverlaySelectionMovedEventHandler, sender: object, e: InkOverlaySelectionMovedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkOverlaySelectionMovedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkOverlaySelectionMovedEventArgs): # -> 
        """ Invoke(self: InkOverlaySelectionMovedEventHandler, sender: object, e: InkOverlaySelectionMovedEventArgs) """
        ...


class InkOverlaySelectionMovingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkOverlaySelectionMovingEventArgs(newPixelRect: Rectangle) """
    @property
    def NewPixelRect(self) -> Rectangle:
        """ Get: NewPixelRect(self: InkOverlaySelectionMovingEventArgs) -> Rectangle """
        ...


    def __new__(cls, newPixelRect:Rectangle) -> Self:
        """ __new__(cls: type, newPixelRect: Rectangle) """
        ...


class InkOverlaySelectionMovingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkOverlaySelectionMovingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkOverlaySelectionMovingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkOverlaySelectionMovingEventHandler, sender: object, e: InkOverlaySelectionMovingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkOverlaySelectionMovingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkOverlaySelectionMovingEventArgs): # -> 
        """ Invoke(self: InkOverlaySelectionMovingEventHandler, sender: object, e: InkOverlaySelectionMovingEventArgs) """
        ...


class InkOverlaySelectionResizedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkOverlaySelectionResizedEventArgs(oldSelectionBoundingRect: Rectangle) """
    @property
    def OldSelectionBoundingRect(self) -> Rectangle:
        """ Get: OldSelectionBoundingRect(self: InkOverlaySelectionResizedEventArgs) -> Rectangle """
        ...


    def __new__(cls, oldSelectionBoundingRect:Rectangle) -> Self:
        """ __new__(cls: type, oldSelectionBoundingRect: Rectangle) """
        ...


class InkOverlaySelectionResizedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkOverlaySelectionResizedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkOverlaySelectionResizedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkOverlaySelectionResizedEventHandler, sender: object, e: InkOverlaySelectionResizedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkOverlaySelectionResizedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkOverlaySelectionResizedEventArgs): # -> 
        """ Invoke(self: InkOverlaySelectionResizedEventHandler, sender: object, e: InkOverlaySelectionResizedEventArgs) """
        ...


class InkOverlaySelectionResizingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkOverlaySelectionResizingEventArgs(newPixelRect: Rectangle) """
    @property
    def NewPixelRect(self) -> Rectangle:
        """ Get: NewPixelRect(self: InkOverlaySelectionResizingEventArgs) -> Rectangle """
        ...


    def __new__(cls, newPixelRect:Rectangle) -> Self:
        """ __new__(cls: type, newPixelRect: Rectangle) """
        ...


class InkOverlaySelectionResizingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkOverlaySelectionResizingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkOverlaySelectionResizingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkOverlaySelectionResizingEventHandler, sender: object, e: InkOverlaySelectionResizingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkOverlaySelectionResizingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkOverlaySelectionResizingEventArgs): # -> 
        """ Invoke(self: InkOverlaySelectionResizingEventHandler, sender: object, e: InkOverlaySelectionResizingEventArgs) """
        ...


class InkOverlayStrokesDeletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkOverlayStrokesDeletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:EventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkOverlayStrokesDeletedEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkOverlayStrokesDeletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:EventArgs): # -> 
        """ Invoke(self: InkOverlayStrokesDeletedEventHandler, sender: object, e: EventArgs) """
        ...


class InkOverlayStrokesDeletingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InkOverlayStrokesDeletingEventArgs(strokesToDelete: Strokes) """
    @property
    def StrokesToDelete(self) -> Strokes:
        """ Get: StrokesToDelete(self: InkOverlayStrokesDeletingEventArgs) -> Strokes """
        ...


    def __new__(cls, strokesToDelete:Strokes) -> Self:
        """ __new__(cls: type, strokesToDelete: Strokes) """
        ...


class InkOverlayStrokesDeletingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InkOverlayStrokesDeletingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InkOverlayStrokesDeletingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InkOverlayStrokesDeletingEventHandler, sender: object, e: InkOverlayStrokesDeletingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InkOverlayStrokesDeletingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InkOverlayStrokesDeletingEventArgs): # -> 
        """ Invoke(self: InkOverlayStrokesDeletingEventHandler, sender: object, e: InkOverlayStrokesDeletingEventArgs) """
        ...


class InkPicture(PictureBox): # skipped bases: <type 'IWin32Window'>, <type 'IPersistStreamInit'>, <type 'IOleInPlaceObject'>, <type 'IViewObject2'>, <type 'IOleObject'>, <type 'IArrangedElement'>, <type 'IOleWindow'>, <type 'IKeyboardToolTip'>, <type 'ISupportInitialize'>, <type 'IPersist'>, <type 'ISynchronizeInvoke'>, <type 'IDisposable'>, <type 'IPersistPropertyBag'>, <type 'IQuickActivate'>, <type 'IComponent'>, <type 'IOleControl'>, <type 'IDropTarget'>, <type 'IBindableComponent'>, <type 'ISupportOleDropSource'>, <type 'IOleInPlaceActiveObject'>, <type 'IPersistStorage'>, <type 'IViewObject'>, <type 'object'>
    """ InkPicture() """
    @property
    def AutoRedraw(self) -> bool:
        """
        Get: AutoRedraw(self: InkPicture) -> bool
        Set: AutoRedraw(self: InkPicture) = value
        """
        ...

    @property
    def CollectingInk(self) -> bool:
        """ Get: CollectingInk(self: InkPicture) -> bool """
        ...

    @property
    def CollectionMode(self) -> CollectionMode:
        """
        Get: CollectionMode(self: InkPicture) -> CollectionMode
        Set: CollectionMode(self: InkPicture) = value
        """
        ...

    @property
    def Cursor(self) -> Cursor:
        """
        Get: Cursor(self: InkPicture) -> Cursor
        Set: Cursor(self: InkPicture) = value
        """
        ...

    @property
    def Cursors(self) -> Cursors:
        """ Get: Cursors(self: InkPicture) -> Cursors """
        ...

    @property
    def DefaultDrawingAttributes(self) -> DrawingAttributes:
        """
        Get: DefaultDrawingAttributes(self: InkPicture) -> DrawingAttributes
        Set: DefaultDrawingAttributes(self: InkPicture) = value
        """
        ...

    @property
    def DesiredPacketDescription(self) -> Array:
        """
        Get: DesiredPacketDescription(self: InkPicture) -> Array[Guid]
        Set: DesiredPacketDescription(self: InkPicture) = value
        """
        ...

    @property
    def Disposing(self) -> bool:
        """ Get: Disposing(self: InkPicture) -> bool """
        ...

    @property
    def DynamicRendering(self) -> bool:
        """
        Get: DynamicRendering(self: InkPicture) -> bool
        Set: DynamicRendering(self: InkPicture) = value
        """
        ...

    @property
    def EditingMode(self) -> InkOverlayEditingMode:
        """
        Get: EditingMode(self: InkPicture) -> InkOverlayEditingMode
        Set: EditingMode(self: InkPicture) = value
        """
        ...

    @property
    def EraserMode(self) -> InkOverlayEraserMode:
        """
        Get: EraserMode(self: InkPicture) -> InkOverlayEraserMode
        Set: EraserMode(self: InkPicture) = value
        """
        ...

    @property
    def EraserWidth(self) -> int:
        """
        Get: EraserWidth(self: InkPicture) -> int
        Set: EraserWidth(self: InkPicture) = value
        """
        ...

    @property
    def Ink(self) -> Ink:
        """
        Get: Ink(self: InkPicture) -> Ink
        Set: Ink(self: InkPicture) = value
        """
        ...

    @property
    def InkEnabled(self) -> bool:
        """
        Get: InkEnabled(self: InkPicture) -> bool
        Set: InkEnabled(self: InkPicture) = value
        """
        ...

    @property
    def MarginX(self) -> int:
        """
        Get: MarginX(self: InkPicture) -> int
        Set: MarginX(self: InkPicture) = value
        """
        ...

    @property
    def MarginY(self) -> int:
        """
        Get: MarginY(self: InkPicture) -> int
        Set: MarginY(self: InkPicture) = value
        """
        ...

    @property
    def Renderer(self) -> Renderer:
        """
        Get: Renderer(self: InkPicture) -> Renderer
        Set: Renderer(self: InkPicture) = value
        """
        ...

    @property
    def Selection(self) -> Strokes:
        """
        Get: Selection(self: InkPicture) -> Strokes
        Set: Selection(self: InkPicture) = value
        """
        ...

    @property
    def SupportHighContrastInk(self) -> bool:
        """
        Get: SupportHighContrastInk(self: InkPicture) -> bool
        Set: SupportHighContrastInk(self: InkPicture) = value
        """
        ...

    @property
    def SupportHighContrastSelectionUI(self) -> bool:
        """
        Get: SupportHighContrastSelectionUI(self: InkPicture) -> bool
        Set: SupportHighContrastSelectionUI(self: InkPicture) = value
        """
        ...

    @property
    def Tablet(self) -> Tablet:
        """ Get: Tablet(self: InkPicture) -> Tablet """
        ...


    def GetGestureStatus(self, gesture:ApplicationGesture) -> bool:
        """ GetGestureStatus(self: InkPicture, gesture: ApplicationGesture) -> bool """
        ...

    def GetWindowInputRectangle(self, windowInputRectangle) -> Rectangle:
        """ GetWindowInputRectangle(self: InkPicture) -> Rectangle """
        ...

    def HitTestSelection(self, X:int, Y:int) -> SelectionHitResult:
        """ HitTestSelection(self: InkPicture, X: int, Y: int) -> SelectionHitResult """
        ...

    def OnCursorButtonDown(self, *args): #cannot find CLR method
        """ OnCursorButtonDown(self: InkPicture, e: InkCollectorCursorButtonDownEventArgs) """
        ...

    def OnCursorButtonUp(self, *args): #cannot find CLR method
        """ OnCursorButtonUp(self: InkPicture, e: InkCollectorCursorButtonUpEventArgs) """
        ...

    def OnCursorDown(self, *args): #cannot find CLR method
        """ OnCursorDown(self: InkPicture, e: InkCollectorCursorDownEventArgs) """
        ...

    def OnCursorInRange(self, *args): #cannot find CLR method
        """ OnCursorInRange(self: InkPicture, e: InkCollectorCursorInRangeEventArgs) """
        ...

    def OnCursorOutOfRange(self, *args): #cannot find CLR method
        """ OnCursorOutOfRange(self: InkPicture, e: InkCollectorCursorOutOfRangeEventArgs) """
        ...

    def OnGesture(self, *args): #cannot find CLR method
        """ OnGesture(self: InkPicture, e: InkCollectorGestureEventArgs) """
        ...

    def OnNewInAirPackets(self, *args): #cannot find CLR method
        """ OnNewInAirPackets(self: InkPicture, e: InkCollectorNewInAirPacketsEventArgs) """
        ...

    def OnNewPackets(self, *args): #cannot find CLR method
        """ OnNewPackets(self: InkPicture, e: InkCollectorNewPacketsEventArgs) """
        ...

    def OnPainted(self, *args): #cannot find CLR method
        """ OnPainted(self: InkPicture, e: PaintEventArgs) """
        ...

    def OnPainting(self, *args): #cannot find CLR method
        """ OnPainting(self: InkPicture, e: InkOverlayPaintingEventArgs) """
        ...

    def OnSelectionChanged(self, *args): #cannot find CLR method
        """ OnSelectionChanged(self: InkPicture, e: EventArgs) """
        ...

    def OnSelectionChanging(self, *args): #cannot find CLR method
        """ OnSelectionChanging(self: InkPicture, e: InkOverlaySelectionChangingEventArgs) """
        ...

    def OnSelectionMoved(self, *args): #cannot find CLR method
        """ OnSelectionMoved(self: InkPicture, e: InkOverlaySelectionMovedEventArgs) """
        ...

    def OnSelectionMoving(self, *args): #cannot find CLR method
        """ OnSelectionMoving(self: InkPicture, e: InkOverlaySelectionMovingEventArgs) """
        ...

    def OnSelectionResized(self, *args): #cannot find CLR method
        """ OnSelectionResized(self: InkPicture, e: InkOverlaySelectionResizedEventArgs) """
        ...

    def OnSelectionResizing(self, *args): #cannot find CLR method
        """ OnSelectionResizing(self: InkPicture, e: InkOverlaySelectionResizingEventArgs) """
        ...

    def OnStroke(self, *args): #cannot find CLR method
        """ OnStroke(self: InkPicture, e: InkCollectorStrokeEventArgs) """
        ...

    def OnStrokesDeleted(self, *args): #cannot find CLR method
        """ OnStrokesDeleted(self: InkPicture, e: EventArgs) """
        ...

    def OnStrokesDeleting(self, *args): #cannot find CLR method
        """ OnStrokesDeleting(self: InkPicture, e: InkOverlayStrokesDeletingEventArgs) """
        ...

    def OnSystemGesture(self, *args): #cannot find CLR method
        """ OnSystemGesture(self: InkPicture, e: InkCollectorSystemGestureEventArgs) """
        ...

    def OnTabletAdded(self, *args): #cannot find CLR method
        """ OnTabletAdded(self: InkPicture, e: InkCollectorTabletAddedEventArgs) """
        ...

    def OnTabletRemoved(self, *args): #cannot find CLR method
        """ OnTabletRemoved(self: InkPicture, e: InkCollectorTabletRemovedEventArgs) """
        ...

    def SetAllTabletsMode(self, useMouseForInput:bool = ...): # -> 
        """ SetAllTabletsMode(self: InkPicture)SetAllTabletsMode(self: InkPicture, useMouseForInput: bool) """
        ...

    def SetGestureStatus(self, gesture:ApplicationGesture, listening:bool): # -> 
        """ SetGestureStatus(self: InkPicture, gesture: ApplicationGesture, listening: bool) """
        ...

    def SetSingleTabletIntegratedMode(self, tablet:Tablet): # -> 
        """ SetSingleTabletIntegratedMode(self: InkPicture, tablet: Tablet) """
        ...

    def SetWindowInputRectangle(self, windowInputRectangle:Rectangle): # -> 
        """ SetWindowInputRectangle(self: InkPicture, windowInputRectangle: Rectangle) """
        ...

    ClipInkToMargin = ...
    CursorButtonDown = ...
    CursorButtonUp = ...
    CursorDown = ...
    CursorInRange = ...
    CursorOutOfRange = ...
    DefaultMargin = ...
    Gesture = ...
    NewInAirPackets = ...
    NewPackets = ...
    Painted = ...
    Painting = ...
    SelectionChanged = ...
    SelectionChanging = ...
    SelectionMoved = ...
    SelectionMoving = ...
    SelectionResized = ...
    SelectionResizing = ...
    Stroke = ...
    StrokesDeleted = ...
    StrokesDeleting = ...
    SystemGesture = ...
    TabletAdded = ...
    TabletRemoved = ...


class Line: # skipped bases: <type 'object'>, <type 'object'>
    """ Line(beginPoint: Point, endPoint: Point) """
    @property
    def BeginPoint(self) -> Point:
        """
        Get: BeginPoint(self: Line) -> Point
        Set: BeginPoint(self: Line) = value
        """
        ...

    @property
    def EndPoint(self) -> Point:
        """
        Get: EndPoint(self: Line) -> Point
        Set: EndPoint(self: Line) = value
        """
        ...



class PacketProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ PacketProperty() """
    AltitudeOrientation: Guid = ...
    AzimuthOrientation: Guid = ...
    ButtonPressure: Guid = ...
    Height: Guid = ...
    NormalPressure: Guid = ...
    PacketStatus: Guid = ...
    PitchRotation: Guid = ...
    RollRotation: Guid = ...
    SerialNumber: Guid = ...
    SystemTouch: Guid = ...
    TangentPressure: Guid = ...
    TimerTick: Guid = ...
    TwistOrientation: Guid = ...
    Width: Guid = ...
    X: Guid = ...
    XTiltOrientation: Guid = ...
    Y: Guid = ...
    YawRotation: Guid = ...
    YTiltOrientation: Guid = ...
    Z: Guid = ...


class PanelType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PanelType, values: Default (0), Handwriting (2), Inactive (1), Keyboard (3) """
    Default: PanelType = ...
    Handwriting: PanelType = ...
    Inactive: PanelType = ...
    Keyboard: PanelType = ...
    value__ = ...


class PenInputPanel(IDisposable): # skipped bases: <type 'object'>
    """
    PenInputPanel()
    PenInputPanel(attachHandle: IntPtr)
    PenInputPanel(attachControl: Control)
    """
    @property
    def AttachedEditControl(self) -> Control:
        """
        Get: AttachedEditControl(self: PenInputPanel) -> Control
        Set: AttachedEditControl(self: PenInputPanel) = value
        """
        ...

    @property
    def AttachedEditWindow(self) -> IntPtr:
        """
        Get: AttachedEditWindow(self: PenInputPanel) -> IntPtr
        Set: AttachedEditWindow(self: PenInputPanel) = value
        """
        ...

    @property
    def AutoShow(self) -> bool:
        """
        Get: AutoShow(self: PenInputPanel) -> bool
        Set: AutoShow(self: PenInputPanel) = value
        """
        ...

    @property
    def Busy(self) -> bool:
        """ Get: Busy(self: PenInputPanel) -> bool """
        ...

    @property
    def CurrentPanel(self) -> PanelType:
        """
        Get: CurrentPanel(self: PenInputPanel) -> PanelType
        Set: CurrentPanel(self: PenInputPanel) = value
        """
        ...

    @property
    def DefaultPanel(self) -> PanelType:
        """
        Get: DefaultPanel(self: PenInputPanel) -> PanelType
        Set: DefaultPanel(self: PenInputPanel) = value
        """
        ...

    @property
    def Factoid(self) -> str:
        """
        Get: Factoid(self: PenInputPanel) -> str
        Set: Factoid(self: PenInputPanel) = value
        """
        ...

    @property
    def Height(self) -> int:
        """ Get: Height(self: PenInputPanel) -> int """
        ...

    @property
    def HorizontalOffset(self) -> int:
        """
        Get: HorizontalOffset(self: PenInputPanel) -> int
        Set: HorizontalOffset(self: PenInputPanel) = value
        """
        ...

    @property
    def Left(self) -> int:
        """ Get: Left(self: PenInputPanel) -> int """
        ...

    @property
    def Top(self) -> int:
        """ Get: Top(self: PenInputPanel) -> int """
        ...

    @property
    def VerticalOffset(self) -> int:
        """
        Get: VerticalOffset(self: PenInputPanel) -> int
        Set: VerticalOffset(self: PenInputPanel) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: PenInputPanel) -> bool
        Set: Visible(self: PenInputPanel) = value
        """
        ...

    @property
    def Width(self) -> int:
        """ Get: Width(self: PenInputPanel) -> int """
        ...


    def CommitPendingInput(self): # -> 
        """ CommitPendingInput(self: PenInputPanel) """
        ...

    def EnableTsf(self, enable:bool): # -> 
        """ EnableTsf(self: PenInputPanel, enable: bool) """
        ...

    def MoveTo(self, left:int, top:int): # -> 
        """ MoveTo(self: PenInputPanel, left: int, top: int) """
        ...

    def OnInputFailed(self, *args): #cannot find CLR method
        """ OnInputFailed(self: PenInputPanel, e: PenInputPanelInputFailedEventArgs) """
        ...

    def OnPanelChanged(self, *args): #cannot find CLR method
        """ OnPanelChanged(self: PenInputPanel, e: PenInputPanelChangedEventArgs) """
        ...

    def OnPanelMoving(self, *args): #cannot find CLR method
        """ OnPanelMoving(self: PenInputPanel, e: PenInputPanelMovingEventArgs) """
        ...

    def OnVisibleChanged(self, *args): #cannot find CLR method
        """ OnVisibleChanged(self: PenInputPanel, e: PenInputPanelVisibleChangedEventArgs) """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: PenInputPanel) """
        ...

    InputFailed = ...
    PanelChanged = ...
    PanelMoving = ...
    VisibleChanged = ...


class PenInputPanelChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ PenInputPanelChangedEventArgs(newPanelType: PanelType) """
    @property
    def NewPanelType(self) -> PanelType:
        """ Get: NewPanelType(self: PenInputPanelChangedEventArgs) -> PanelType """
        ...


    def __new__(cls, newPanelType:PanelType) -> Self:
        """ __new__(cls: type, newPanelType: PanelType) """
        ...


class PenInputPanelChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PenInputPanelChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:PenInputPanelChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PenInputPanelChangedEventHandler, sender: object, e: PenInputPanelChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PenInputPanelChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:PenInputPanelChangedEventArgs): # -> 
        """ Invoke(self: PenInputPanelChangedEventHandler, sender: object, e: PenInputPanelChangedEventArgs) """
        ...


class PenInputPanelInputFailedEventArgs(KeyEventArgs): # skipped bases: <type 'object'>
    """ PenInputPanelInputFailedEventArgs(handle: IntPtr, keyData: Keys, text: str) """
    @property
    def Handle(self) -> IntPtr:
        """ Get: Handle(self: PenInputPanelInputFailedEventArgs) -> IntPtr """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: PenInputPanelInputFailedEventArgs) -> str """
        ...



class PenInputPanelInputFailedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PenInputPanelInputFailedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:PenInputPanelInputFailedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PenInputPanelInputFailedEventHandler, sender: object, e: PenInputPanelInputFailedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PenInputPanelInputFailedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:PenInputPanelInputFailedEventArgs): # -> 
        """ Invoke(self: PenInputPanelInputFailedEventHandler, sender: object, e: PenInputPanelInputFailedEventArgs) """
        ...


class PenInputPanelMovingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ PenInputPanelMovingEventArgs(left: int, top: int) """
    @property
    def Left(self) -> int:
        """
        Get: Left(self: PenInputPanelMovingEventArgs) -> int
        Set: Left(self: PenInputPanelMovingEventArgs) = value
        """
        ...

    @property
    def Top(self) -> int:
        """
        Get: Top(self: PenInputPanelMovingEventArgs) -> int
        Set: Top(self: PenInputPanelMovingEventArgs) = value
        """
        ...


    def __new__(cls, left:int, top:int) -> Self:
        """ __new__(cls: type, left: int, top: int) """
        ...


class PenInputPanelMovingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PenInputPanelMovingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:PenInputPanelMovingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PenInputPanelMovingEventHandler, sender: object, e: PenInputPanelMovingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PenInputPanelMovingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:PenInputPanelMovingEventArgs): # -> 
        """ Invoke(self: PenInputPanelMovingEventHandler, sender: object, e: PenInputPanelMovingEventArgs) """
        ...


class PenInputPanelVisibleChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ PenInputPanelVisibleChangedEventArgs(newVisibility: bool) """
    @property
    def NewVisibility(self) -> bool:
        """ Get: NewVisibility(self: PenInputPanelVisibleChangedEventArgs) -> bool """
        ...


    def __new__(cls, newVisibility:bool) -> Self:
        """ __new__(cls: type, newVisibility: bool) """
        ...


class PenInputPanelVisibleChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PenInputPanelVisibleChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:PenInputPanelVisibleChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PenInputPanelVisibleChangedEventHandler, sender: object, e: PenInputPanelVisibleChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PenInputPanelVisibleChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:PenInputPanelVisibleChangedEventArgs): # -> 
        """ Invoke(self: PenInputPanelVisibleChangedEventHandler, sender: object, e: PenInputPanelVisibleChangedEventArgs) """
        ...


class PenTip(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PenTip, values: Ball (0), Rectangle (1) """
    Ball: PenTip = ...
    Rectangle: PenTip = ...
    value__ = ...


class PersistenceFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PersistenceFormat, values: Base64Gif (3), Base64InkSerializedFormat (1), Gif (2), InkSerializedFormat (0) """
    Base64Gif: PersistenceFormat = ...
    Base64InkSerializedFormat: PersistenceFormat = ...
    Gif: PersistenceFormat = ...
    InkSerializedFormat: PersistenceFormat = ...
    value__ = ...


class RasterOperation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RasterOperation, values: Black (1), CopyPen (13), MakePenNot (5), MaskNotPen (3), MaskPen (9), MergeNotPen (12), MergePen (15), MergePenNot (14), NoOperation (11), Not (6), NotCopyPen (4), NotMaskPen (8), NotMergePen (2), NotXOrPen (10), White (16), XOrPen (7) """
    Black: RasterOperation = ...
    CopyPen: RasterOperation = ...
    MakePenNot: RasterOperation = ...
    MaskNotPen: RasterOperation = ...
    MaskPen: RasterOperation = ...
    MergeNotPen: RasterOperation = ...
    MergePen: RasterOperation = ...
    MergePenNot: RasterOperation = ...
    NoOperation: RasterOperation = ...
    Not: RasterOperation = ...
    NotCopyPen: RasterOperation = ...
    NotMaskPen: RasterOperation = ...
    NotMergePen: RasterOperation = ...
    NotXOrPen: RasterOperation = ...
    value__ = ...
    White: RasterOperation = ...
    XOrPen: RasterOperation = ...


class RecognitionAlternate: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Ascender(self) -> Line:
        """ Get: Ascender(self: RecognitionAlternate) -> Line """
        ...

    @property
    def Baseline(self) -> Line:
        """ Get: Baseline(self: RecognitionAlternate) -> Line """
        ...

    @property
    def Confidence(self) -> RecognitionConfidence:
        """ Get: Confidence(self: RecognitionAlternate) -> RecognitionConfidence """
        ...

    @property
    def ConfidenceAlternates(self) -> RecognitionAlternates:
        """ Get: ConfidenceAlternates(self: RecognitionAlternate) -> RecognitionAlternates """
        ...

    @property
    def Descender(self) -> Line:
        """ Get: Descender(self: RecognitionAlternate) -> Line """
        ...

    @property
    def LineAlternates(self) -> RecognitionAlternates:
        """ Get: LineAlternates(self: RecognitionAlternate) -> RecognitionAlternates """
        ...

    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: RecognitionAlternate) -> int """
        ...

    @property
    def Midline(self) -> Line:
        """ Get: Midline(self: RecognitionAlternate) -> Line """
        ...

    @property
    def Strokes(self) -> Strokes:
        """ Get: Strokes(self: RecognitionAlternate) -> Strokes """
        ...


    def AlternatesWithConstantPropertyValues(self, g:Guid) -> RecognitionAlternates:
        """ AlternatesWithConstantPropertyValues(self: RecognitionAlternate, g: Guid) -> RecognitionAlternates """
        ...

    def GetPropertyValue(self, g:Guid) -> Array:
        """ GetPropertyValue(self: RecognitionAlternate, g: Guid) -> Array[Byte] """
        ...

    def GetStrokesFromStrokeRanges(self, s:Strokes) -> Strokes:
        """ GetStrokesFromStrokeRanges(self: RecognitionAlternate, s: Strokes) -> Strokes """
        ...

    def GetStrokesFromTextRange(self, selectionStart:int, selectionLength:int) -> Tuple_[Strokes, int, int]:
        """ GetStrokesFromTextRange(self: RecognitionAlternate, selectionStart: int, selectionLength: int) -> (Strokes, int, int) """
        ...

    def GetTextRangeFromStrokes(self, s:Strokes, selectionStart:int, selectionLength:int) -> Tuple_[int, int]:
        """ GetTextRangeFromStrokes(self: RecognitionAlternate, s: Strokes, selectionStart: int, selectionLength: int) -> (int, int) """
        ...

    def ToString(self) -> str:
        """ ToString(self: RecognitionAlternate) -> str """
        ...


class RecognitionAlternates(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Strokes(self) -> Strokes:
        """ Get: Strokes(self: RecognitionAlternates) -> Strokes """
        ...


    def GetEnumerator(self): # -> RecognitionAlternatesEnumerator
        """ GetEnumerator(self: RecognitionAlternates) -> RecognitionAlternatesEnumerator """
        ...

    def RecognitionAlternatesEnumerator(self, *args): #cannot find CLR method
        """ RecognitionAlternatesEnumerator(a: RecognitionAlternates) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class RecognitionConfidence(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RecognitionConfidence, values: Intermediate (1), Poor (2), Strong (0) """
    Intermediate: RecognitionConfidence = ...
    Poor: RecognitionConfidence = ...
    Strong: RecognitionConfidence = ...
    value__ = ...


class RecognitionModes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) RecognitionModes, values: AutoSpace (64), Coerce (2), DisablePersonalization (32), LineMode (16), None (0), PrefixOk (8), TopInkBreaksOnly (4), WordMode (1) """
    AutoSpace: RecognitionModes = ...
    Coerce: RecognitionModes = ...
    DisablePersonalization: RecognitionModes = ...
    LineMode: RecognitionModes = ...
    PrefixOk: RecognitionModes = ...
    TopInkBreaksOnly: RecognitionModes = ...
    value__ = ...
    WordMode: RecognitionModes = ...


class RecognitionProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ RecognitionProperty() """
    ConfidenceLevel: Guid = ...
    HotPoint: Guid = ...
    LineMetrics: Guid = ...
    LineNumber: Guid = ...
    MaximumStrokeCount: Guid = ...
    PointsPerInch: Guid = ...
    Segmentation: Guid = ...


class RecognitionResult: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Strokes(self) -> Strokes:
        """ Get: Strokes(self: RecognitionResult) -> Strokes """
        ...

    @property
    def TopAlternate(self) -> RecognitionAlternate:
        """ Get: TopAlternate(self: RecognitionResult) -> RecognitionAlternate """
        ...

    @property
    def TopConfidence(self) -> RecognitionConfidence:
        """ Get: TopConfidence(self: RecognitionResult) -> RecognitionConfidence """
        ...

    @property
    def TopString(self) -> str:
        """ Get: TopString(self: RecognitionResult) -> str """
        ...


    def GetAlternatesFromSelection(self, selectionStart:int = ..., selectionLength:int = ..., maximumAlternates:int = ...) -> RecognitionAlternates:
        """
        GetAlternatesFromSelection(self: RecognitionResult, selectionStart: int, selectionLength: int, maximumAlternates: int) -> RecognitionAlternates
        GetAlternatesFromSelection(self: RecognitionResult, selectionStart: int, selectionLength: int) -> RecognitionAlternates
        GetAlternatesFromSelection(self: RecognitionResult) -> RecognitionAlternates
        """
        ...

    def ModifyTopAlternate(self, alternate:RecognitionAlternate): # -> 
        """ ModifyTopAlternate(self: RecognitionResult, alternate: RecognitionAlternate) """
        ...

    def SetResultOnStrokes(self): # -> 
        """ SetResultOnStrokes(self: RecognitionResult) """
        ...

    def ToString(self) -> str:
        """ ToString(self: RecognitionResult) -> str """
        ...

    DefaultMaximumRecognitionAlternates: int = ...


class RecognitionStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) RecognitionStatus, values: InkAddedFailed (4), Interrupted (1), NoError (0), ProcessFailed (2), SetAutoCompletionModeFailed (8), SetFactoidFailed (128), SetFlagsFailed (64), SetGuideFailed (32), SetPrefixSuffixFailed (256), SetStrokesFailed (16), SetWordListFailed (512) """
    InkAddedFailed: RecognitionStatus = ...
    Interrupted: RecognitionStatus = ...
    NoError: RecognitionStatus = ...
    ProcessFailed: RecognitionStatus = ...
    SetAutoCompletionModeFailed: RecognitionStatus = ...
    SetFactoidFailed: RecognitionStatus = ...
    SetFlagsFailed: RecognitionStatus = ...
    SetGuideFailed: RecognitionStatus = ...
    SetPrefixSuffixFailed: RecognitionStatus = ...
    SetStrokesFailed: RecognitionStatus = ...
    SetWordListFailed: RecognitionStatus = ...
    value__ = ...


class Recognizer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Capabilities(self) -> RecognizerCapabilities:
        """ Get: Capabilities(self: Recognizer) -> RecognizerCapabilities """
        ...

    @property
    def Id(self) -> Guid:
        """ Get: Id(self: Recognizer) -> Guid """
        ...

    @property
    def Languages(self) -> Array:
        """ Get: Languages(self: Recognizer) -> Array[Int16] """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Recognizer) -> str """
        ...

    @property
    def PreferredPacketDescription(self) -> Array:
        """ Get: PreferredPacketDescription(self: Recognizer) -> Array[Guid] """
        ...

    @property
    def SupportedProperties(self) -> Array:
        """ Get: SupportedProperties(self: Recognizer) -> Array[Guid] """
        ...

    @property
    def Vendor(self) -> str:
        """ Get: Vendor(self: Recognizer) -> str """
        ...


    def CreateRecognizerContext(self) -> RecognizerContext:
        """ CreateRecognizerContext(self: Recognizer) -> RecognizerContext """
        ...

    def GetUnicodeRanges(self) -> Array:
        """ GetUnicodeRanges(self: Recognizer) -> Array[UnicodeRange] """
        ...

    def ToString(self) -> str:
        """ ToString(self: Recognizer) -> str """
        ...


class RecognizerCapabilities(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) RecognizerCapabilities, values: AdviseInkChange (4096), Alpha (1048576), ArbitraryAngle (1024), Beta (2097152), BoxedInput (16), CharacterAutoCompletionInput (32), Cursive (262144), DontCare (1), DownAndLeft (256), DownAndRight (512), FreeInput (4), Lattice (2048), LeftAndDown (128), LinedInput (8), Object (2), Personalizable (16384), PrefersArbitraryAngle (32768), PrefersParagraphBreaking (65536), PrefersSegmentation (131072), RightAndDown (64), StrokeReorder (8192), TextPrediction (524288) """
    AdviseInkChange: RecognizerCapabilities = ...
    Alpha: RecognizerCapabilities = ...
    ArbitraryAngle: RecognizerCapabilities = ...
    Beta: RecognizerCapabilities = ...
    BoxedInput: RecognizerCapabilities = ...
    CharacterAutoCompletionInput: RecognizerCapabilities = ...
    Cursive: RecognizerCapabilities = ...
    DontCare: RecognizerCapabilities = ...
    DownAndLeft: RecognizerCapabilities = ...
    DownAndRight: RecognizerCapabilities = ...
    FreeInput: RecognizerCapabilities = ...
    Lattice: RecognizerCapabilities = ...
    LeftAndDown: RecognizerCapabilities = ...
    LinedInput: RecognizerCapabilities = ...
    Object: RecognizerCapabilities = ...
    Personalizable: RecognizerCapabilities = ...
    PrefersArbitraryAngle: RecognizerCapabilities = ...
    PrefersParagraphBreaking: RecognizerCapabilities = ...
    PrefersSegmentation: RecognizerCapabilities = ...
    RightAndDown: RecognizerCapabilities = ...
    StrokeReorder: RecognizerCapabilities = ...
    TextPrediction: RecognizerCapabilities = ...
    value__ = ...


class RecognizerCharacterAutoCompletionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RecognizerCharacterAutoCompletionMode, values: Full (0), Prefix (1), Random (2) """
    Full: RecognizerCharacterAutoCompletionMode = ...
    Prefix: RecognizerCharacterAutoCompletionMode = ...
    Random: RecognizerCharacterAutoCompletionMode = ...
    value__ = ...


class RecognizerContext(IDisposable, ICloneable): # skipped bases: <type 'object'>
    """ RecognizerContext() """
    @property
    def CharacterAutoCompletion(self) -> RecognizerCharacterAutoCompletionMode:
        """
        Get: CharacterAutoCompletion(self: RecognizerContext) -> RecognizerCharacterAutoCompletionMode
        Set: CharacterAutoCompletion(self: RecognizerContext) = value
        """
        ...

    @property
    def Factoid(self) -> str:
        """
        Get: Factoid(self: RecognizerContext) -> str
        Set: Factoid(self: RecognizerContext) = value
        """
        ...

    @property
    def Guide(self) -> RecognizerGuide:
        """
        Get: Guide(self: RecognizerContext) -> RecognizerGuide
        Set: Guide(self: RecognizerContext) = value
        """
        ...

    @property
    def PrefixText(self) -> str:
        """
        Get: PrefixText(self: RecognizerContext) -> str
        Set: PrefixText(self: RecognizerContext) = value
        """
        ...

    @property
    def RecognitionFlags(self) -> RecognitionModes:
        """
        Get: RecognitionFlags(self: RecognizerContext) -> RecognitionModes
        Set: RecognitionFlags(self: RecognizerContext) = value
        """
        ...

    @property
    def Recognizer(self) -> Recognizer:
        """ Get: Recognizer(self: RecognizerContext) -> Recognizer """
        ...

    @property
    def Strokes(self) -> Strokes:
        """
        Get: Strokes(self: RecognizerContext) -> Strokes
        Set: Strokes(self: RecognizerContext) = value
        """
        ...

    @property
    def SuffixText(self) -> str:
        """
        Get: SuffixText(self: RecognizerContext) -> str
        Set: SuffixText(self: RecognizerContext) = value
        """
        ...

    @property
    def WordList(self) -> WordList:
        """
        Get: WordList(self: RecognizerContext) -> WordList
        Set: WordList(self: RecognizerContext) = value
        """
        ...


    def BackgroundRecognize(self, customData:object = ...): # -> 
        """ BackgroundRecognize(self: RecognizerContext, customData: object)BackgroundRecognize(self: RecognizerContext) """
        ...

    def BackgroundRecognizeWithAlternates(self, customData:object = ...): # -> 
        """ BackgroundRecognizeWithAlternates(self: RecognizerContext, customData: object)BackgroundRecognizeWithAlternates(self: RecognizerContext) """
        ...

    def EndInkInput(self): # -> 
        """ EndInkInput(self: RecognizerContext) """
        ...

    def GetEnabledUnicodeRanges(self) -> Array:
        """ GetEnabledUnicodeRanges(self: RecognizerContext) -> Array[UnicodeRange] """
        ...

    def IsStringSupported(self, s:str) -> bool:
        """ IsStringSupported(self: RecognizerContext, s: str) -> bool """
        ...

    def Recognize(self, recognitionStatus) -> Tuple_[RecognitionResult, RecognitionStatus]:
        """ Recognize(self: RecognizerContext) -> (RecognitionResult, RecognitionStatus) """
        ...

    def SetEnabledUnicodeRanges(self, ranges:Array): # -> 
        """ SetEnabledUnicodeRanges(self: RecognizerContext, ranges: Array[UnicodeRange]) """
        ...

    def StopBackgroundRecognition(self): # -> 
        """ StopBackgroundRecognition(self: RecognizerContext) """
        ...

    Recognition = ...
    RecognitionWithAlternates = ...


class RecognizerContextRecognitionEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ RecognizerContextRecognitionEventArgs(text: str, customData: object, recognitionStatus: RecognitionStatus) """
    @property
    def CustomData(self) -> object:
        """ Get: CustomData(self: RecognizerContextRecognitionEventArgs) -> object """
        ...

    @property
    def RecognitionStatus(self) -> RecognitionStatus:
        """ Get: RecognitionStatus(self: RecognizerContextRecognitionEventArgs) -> RecognitionStatus """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: RecognizerContextRecognitionEventArgs) -> str """
        ...


    def __new__(cls, text:str, customData:object, recognitionStatus:RecognitionStatus) -> Self:
        """ __new__(cls: type, text: str, customData: object, recognitionStatus: RecognitionStatus) """
        ...


class RecognizerContextRecognitionEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ RecognizerContextRecognitionEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:RecognizerContextRecognitionEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: RecognizerContextRecognitionEventHandler, sender: object, e: RecognizerContextRecognitionEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: RecognizerContextRecognitionEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:RecognizerContextRecognitionEventArgs): # -> 
        """ Invoke(self: RecognizerContextRecognitionEventHandler, sender: object, e: RecognizerContextRecognitionEventArgs) """
        ...


class RecognizerContextRecognitionWithAlternatesEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ RecognizerContextRecognitionWithAlternatesEventArgs(result: RecognitionResult, customData: object, recognitionStatus: RecognitionStatus) """
    @property
    def CustomData(self) -> object:
        """ Get: CustomData(self: RecognizerContextRecognitionWithAlternatesEventArgs) -> object """
        ...

    @property
    def RecognitionStatus(self) -> RecognitionStatus:
        """ Get: RecognitionStatus(self: RecognizerContextRecognitionWithAlternatesEventArgs) -> RecognitionStatus """
        ...

    @property
    def Result(self) -> RecognitionResult:
        """ Get: Result(self: RecognizerContextRecognitionWithAlternatesEventArgs) -> RecognitionResult """
        ...


    def __new__(cls, result:RecognitionResult, customData:object, recognitionStatus:RecognitionStatus) -> Self:
        """ __new__(cls: type, result: RecognitionResult, customData: object, recognitionStatus: RecognitionStatus) """
        ...


class RecognizerContextRecognitionWithAlternatesEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ RecognizerContextRecognitionWithAlternatesEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:RecognizerContextRecognitionWithAlternatesEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: RecognizerContextRecognitionWithAlternatesEventHandler, sender: object, e: RecognizerContextRecognitionWithAlternatesEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: RecognizerContextRecognitionWithAlternatesEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:RecognizerContextRecognitionWithAlternatesEventArgs): # -> 
        """ Invoke(self: RecognizerContextRecognitionWithAlternatesEventHandler, sender: object, e: RecognizerContextRecognitionWithAlternatesEventArgs) """
        ...


class RecognizerGuide: # skipped bases: <type 'object'>, <type 'object'>
    """ RecognizerGuide(rows: int, columns: int, midline: int, writingBox: Rectangle, drawnBox: Rectangle) """
    @property
    def Columns(self) -> int:
        """
        Get: Columns(self: RecognizerGuide) -> int
        Set: Columns(self: RecognizerGuide) = value
        """
        ...

    @property
    def DrawnBox(self) -> Rectangle:
        """
        Get: DrawnBox(self: RecognizerGuide) -> Rectangle
        Set: DrawnBox(self: RecognizerGuide) = value
        """
        ...

    @property
    def Midline(self) -> int:
        """
        Get: Midline(self: RecognizerGuide) -> int
        Set: Midline(self: RecognizerGuide) = value
        """
        ...

    @property
    def Rows(self) -> int:
        """
        Get: Rows(self: RecognizerGuide) -> int
        Set: Rows(self: RecognizerGuide) = value
        """
        ...

    @property
    def WritingBox(self) -> Rectangle:
        """
        Get: WritingBox(self: RecognizerGuide) -> Rectangle
        Set: WritingBox(self: RecognizerGuide) = value
        """
        ...



class Recognizers(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ Recognizers() """
    def GetDefaultRecognizer(self, lcid:int = ...) -> Recognizer:
        """
        GetDefaultRecognizer(self: Recognizers) -> Recognizer
        GetDefaultRecognizer(self: Recognizers, lcid: int) -> Recognizer
        """
        ...

    def GetEnumerator(self): # -> RecognizersEnumerator
        """ GetEnumerator(self: Recognizers) -> RecognizersEnumerator """
        ...

    def RecognizersEnumerator(self, *args): #cannot find CLR method
        """ RecognizersEnumerator(r: Recognizers) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class Renderer: # skipped bases: <type 'object'>, <type 'object'>
    """ Renderer() """
    def Draw(self, *__args): # -> 
        """ Draw(self: Renderer, g: Graphics, strokes: Strokes)Draw(self: Renderer, hdc: IntPtr, strokes: Strokes)Draw(self: Renderer, g: Graphics, stroke: Stroke)Draw(self: Renderer, g: Graphics, stroke: Stroke, da: DrawingAttributes)Draw(self: Renderer, hdc: IntPtr, stroke: Stroke)Draw(self: Renderer, hdc: IntPtr, stroke: Stroke, da: DrawingAttributes)Draw(self: Renderer, destinationBitmap: Bitmap, strokes: Strokes)Draw(self: Renderer, destinationBitmap: Bitmap, stroke: Stroke)Draw(self: Renderer, destinationBitmap: Bitmap, stroke: Stroke, da: DrawingAttributes) """
        ...

    def GetObjectTransform(self, objectTransform:Matrix) -> Matrix:
        """ GetObjectTransform(self: Renderer, objectTransform: Matrix) -> Matrix """
        ...

    def GetViewTransform(self, viewTransform:Matrix) -> Matrix:
        """ GetViewTransform(self: Renderer, viewTransform: Matrix) -> Matrix """
        ...

    def InkSpaceToPixel(self, *__args) -> Point:
        """
        InkSpaceToPixel(self: Renderer, g: Graphics, pt: Point) -> Point
        InkSpaceToPixel(self: Renderer, hdc: IntPtr, pt: Point) -> Point
        InkSpaceToPixel(self: Renderer, g: Graphics, pts: Array[Point]) -> Array[Point]
        InkSpaceToPixel(self: Renderer, hdc: IntPtr, pts: Array[Point]) -> Array[Point]
        """
        ...

    def Measure(self, *__args:Strokes) -> Rectangle:
        """
        Measure(self: Renderer, strokes: Strokes) -> Rectangle
        Measure(self: Renderer, stroke: Stroke) -> Rectangle
        Measure(self: Renderer, stroke: Stroke, da: DrawingAttributes) -> Rectangle
        """
        ...

    def Move(self, offsetX:Single, offsetY:Single): # -> 
        """ Move(self: Renderer, offsetX: Single, offsetY: Single) """
        ...

    def PixelToInkSpace(self, *__args) -> Point:
        """
        PixelToInkSpace(self: Renderer, g: Graphics, pt: Point) -> Point
        PixelToInkSpace(self: Renderer, hdc: IntPtr, pt: Point) -> Point
        PixelToInkSpace(self: Renderer, g: Graphics, pts: Array[Point]) -> Array[Point]
        PixelToInkSpace(self: Renderer, hdc: IntPtr, pts: Array[Point]) -> Array[Point]
        """
        ...

    def Rotate(self, degrees:Single, point:Point = ...): # -> 
        """ Rotate(self: Renderer, degrees: Single, point: Point)Rotate(self: Renderer, degrees: Single) """
        ...

    def Scale(self, scaleX:Single, scaleY:Single, applyOnPenWidth:bool = ...): # -> 
        """ Scale(self: Renderer, scaleX: Single, scaleY: Single, applyOnPenWidth: bool)Scale(self: Renderer, scaleX: Single, scaleY: Single) """
        ...

    def SetObjectTransform(self, objectTransform:Matrix): # -> 
        """ SetObjectTransform(self: Renderer, objectTransform: Matrix) """
        ...

    def SetViewTransform(self, viewTransform:Matrix): # -> 
        """ SetViewTransform(self: Renderer, viewTransform: Matrix) """
        ...


class SelectionHitResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SelectionHitResult, values: East (5), None (0), North (7), Northeast (3), Northwest (1), Selection (9), South (8), Southeast (2), Southwest (4), West (6) """
    East: SelectionHitResult = ...
    North: SelectionHitResult = ...
    Northeast: SelectionHitResult = ...
    Northwest: SelectionHitResult = ...
    Selection: SelectionHitResult = ...
    South: SelectionHitResult = ...
    Southeast: SelectionHitResult = ...
    Southwest: SelectionHitResult = ...
    value__ = ...
    West: SelectionHitResult = ...


class Stroke: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BezierCusps(self) -> Array:
        """ Get: BezierCusps(self: Stroke) -> Array[int] """
        ...

    @property
    def BezierPoints(self) -> Array:
        """ Get: BezierPoints(self: Stroke) -> Array[Point] """
        ...

    @property
    def Deleted(self) -> bool:
        """ Get: Deleted(self: Stroke) -> bool """
        ...

    @property
    def DrawingAttributes(self) -> DrawingAttributes:
        """
        Get: DrawingAttributes(self: Stroke) -> DrawingAttributes
        Set: DrawingAttributes(self: Stroke) = value
        """
        ...

    @property
    def ExtendedProperties(self) -> ExtendedProperties:
        """ Get: ExtendedProperties(self: Stroke) -> ExtendedProperties """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: Stroke) -> int """
        ...

    @property
    def Ink(self) -> Ink:
        """ Get: Ink(self: Stroke) -> Ink """
        ...

    @property
    def PacketCount(self) -> int:
        """ Get: PacketCount(self: Stroke) -> int """
        ...

    @property
    def PacketDescription(self) -> Array:
        """ Get: PacketDescription(self: Stroke) -> Array[Guid] """
        ...

    @property
    def PacketSize(self) -> int:
        """ Get: PacketSize(self: Stroke) -> int """
        ...

    @property
    def PolylineCusps(self) -> Array:
        """ Get: PolylineCusps(self: Stroke) -> Array[int] """
        ...

    @property
    def SelfIntersections(self) -> Array:
        """ Get: SelfIntersections(self: Stroke) -> Array[Single] """
        ...


    def Clip(self, r:Rectangle): # -> 
        """ Clip(self: Stroke, r: Rectangle) """
        ...

    def FindIntersections(self, strokes:Strokes) -> Array:
        """ FindIntersections(self: Stroke, strokes: Strokes) -> Array[Single] """
        ...

    def GetBoundingBox(self, mode:BoundingBoxMode = ...) -> Rectangle:
        """
        GetBoundingBox(self: Stroke, mode: BoundingBoxMode) -> Rectangle
        GetBoundingBox(self: Stroke) -> Rectangle
        """
        ...

    def GetFlattenedBezierPoints(self, fittingError:int = ...) -> Array:
        """
        GetFlattenedBezierPoints(self: Stroke, fittingError: int) -> Array[Point]
        GetFlattenedBezierPoints(self: Stroke) -> Array[Point]
        """
        ...

    def GetPacketData(self, index:int = ..., count:int = ...) -> Array:
        """
        GetPacketData(self: Stroke, index: int, count: int) -> Array[int]
        GetPacketData(self: Stroke, index: int) -> Array[int]
        GetPacketData(self: Stroke) -> Array[int]
        """
        ...

    def GetPacketDescriptionPropertyMetrics(self, id:Guid) -> TabletPropertyMetrics:
        """ GetPacketDescriptionPropertyMetrics(self: Stroke, id: Guid) -> TabletPropertyMetrics """
        ...

    def GetPacketValuesByProperty(self, id:Guid, index:int = ..., count:int = ...) -> Array:
        """
        GetPacketValuesByProperty(self: Stroke, id: Guid, index: int, count: int) -> Array[int]
        GetPacketValuesByProperty(self: Stroke, id: Guid, index: int) -> Array[int]
        GetPacketValuesByProperty(self: Stroke, id: Guid) -> Array[int]
        """
        ...

    def GetPoint(self, index:int) -> Point:
        """ GetPoint(self: Stroke, index: int) -> Point """
        ...

    def GetPoints(self, index:int = ..., count:int = ...) -> Array:
        """
        GetPoints(self: Stroke, index: int, count: int) -> Array[Point]
        GetPoints(self: Stroke) -> Array[Point]
        """
        ...

    def GetRectangleIntersections(self, intersectRectangle:Rectangle) -> Array:
        """ GetRectangleIntersections(self: Stroke, intersectRectangle: Rectangle) -> Array[StrokeIntersection] """
        ...

    def HitTest(self, pt:Point, radius:Single) -> bool:
        """ HitTest(self: Stroke, pt: Point, radius: Single) -> bool """
        ...

    def Move(self, offsetX:Single, offsetY:Single): # -> 
        """ Move(self: Stroke, offsetX: Single, offsetY: Single) """
        ...

    def NearestPoint(self, pt, distance=None) -> Tuple_[Single, Single]:
        """
        NearestPoint(self: Stroke, pt: Point) -> (Single, Single)
        NearestPoint(self: Stroke, pt: Point) -> Single
        """
        ...

    def Rotate(self, degrees:Single, point:Point): # -> 
        """ Rotate(self: Stroke, degrees: Single, point: Point) """
        ...

    def Scale(self, scaleX:Single, scaleY:Single): # -> 
        """ Scale(self: Stroke, scaleX: Single, scaleY: Single) """
        ...

    def ScaleToRectangle(self, scaleRectangle:Rectangle): # -> 
        """ ScaleToRectangle(self: Stroke, scaleRectangle: Rectangle) """
        ...

    def SetPacketValuesByProperty(self, id:Guid, *__args:Array) -> int:
        """
        SetPacketValuesByProperty(self: Stroke, id: Guid, index: int, count: int, packetValues: Array[int]) -> int
        SetPacketValuesByProperty(self: Stroke, id: Guid, index: int, packetValues: Array[int]) -> int
        SetPacketValuesByProperty(self: Stroke, id: Guid, packetValues: Array[int]) -> int
        """
        ...

    def SetPoint(self, index:int, point:Point) -> int:
        """ SetPoint(self: Stroke, index: int, point: Point) -> int """
        ...

    def SetPoints(self, *__args:Array) -> int:
        """
        SetPoints(self: Stroke, index: int, points: Array[Point]) -> int
        SetPoints(self: Stroke, points: Array[Point]) -> int
        """
        ...

    def Shear(self, shearX:Single, shearY:Single): # -> 
        """ Shear(self: Stroke, shearX: Single, shearY: Single) """
        ...

    def Split(self, findex:Single) -> Stroke:
        """ Split(self: Stroke, findex: Single) -> Stroke """
        ...

    def Transform(self, inkTransform:Matrix, applyOnPenWidth:bool = ...): # -> 
        """ Transform(self: Stroke, inkTransform: Matrix, applyOnPenWidth: bool)Transform(self: Stroke, inkTransform: Matrix) """
        ...


class StrokeIntersection: # skipped bases: <type 'object'>, <type 'object'>
    """ StrokeIntersection(beginIndex: Single, endIndex: Single) """
    @property
    def BeginIndex(self) -> Single:
        """
        Get: BeginIndex(self: StrokeIntersection) -> Single
        Set: BeginIndex(self: StrokeIntersection) = value
        """
        ...

    @property
    def EndIndex(self) -> Single:
        """
        Get: EndIndex(self: StrokeIntersection) -> Single
        Set: EndIndex(self: StrokeIntersection) = value
        """
        ...



class Strokes(IDisposable, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Ink(self) -> Ink:
        """ Get: Ink(self: Strokes) -> Ink """
        ...

    @property
    def IsFixedSize(self) -> bool:
        """ Get: IsFixedSize(self: Strokes) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: Strokes) -> bool """
        ...

    @property
    def RecognitionResult(self) -> RecognitionResult:
        """ Get: RecognitionResult(self: Strokes) -> RecognitionResult """
        ...


    def Add(self, *__args:Stroke) -> int:
        """
        Add(self: Strokes, stroke: Stroke) -> int
        Add(self: Strokes, strokes: Strokes)
        """
        ...

    def Clear(self): # -> 
        """ Clear(self: Strokes) """
        ...

    def Clip(self, r:Rectangle): # -> 
        """ Clip(self: Strokes, r: Rectangle) """
        ...

    def Contains(self, s:Stroke) -> bool:
        """ Contains(self: Strokes, s: Stroke) -> bool """
        ...

    def GetBoundingBox(self, mode:BoundingBoxMode = ...) -> Rectangle:
        """
        GetBoundingBox(self: Strokes, mode: BoundingBoxMode) -> Rectangle
        GetBoundingBox(self: Strokes) -> Rectangle
        """
        ...

    def GetEnumerator(self): # -> StrokesEnumerator
        """ GetEnumerator(self: Strokes) -> StrokesEnumerator """
        ...

    def IndexOf(self, s:Stroke) -> int:
        """ IndexOf(self: Strokes, s: Stroke) -> int """
        ...

    def ModifyDrawingAttributes(self, da:DrawingAttributes): # -> 
        """ ModifyDrawingAttributes(self: Strokes, da: DrawingAttributes) """
        ...

    def Move(self, offsetX:Single, offsetY:Single): # -> 
        """ Move(self: Strokes, offsetX: Single, offsetY: Single) """
        ...

    def Remove(self, *__args:Stroke): # -> 
        """ Remove(self: Strokes, stroke: Stroke)Remove(self: Strokes, strokes: Strokes) """
        ...

    def RemoveAt(self, i:int): # -> 
        """ RemoveAt(self: Strokes, i: int) """
        ...

    def RemoveRecognitionResult(self): # -> 
        """ RemoveRecognitionResult(self: Strokes) """
        ...

    def Rotate(self, degrees:Single, point:Point): # -> 
        """ Rotate(self: Strokes, degrees: Single, point: Point) """
        ...

    def Scale(self, scaleX:Single, scaleY:Single): # -> 
        """ Scale(self: Strokes, scaleX: Single, scaleY: Single) """
        ...

    def ScaleToRectangle(self, scaleRectangle:Rectangle): # -> 
        """ ScaleToRectangle(self: Strokes, scaleRectangle: Rectangle) """
        ...

    def Shear(self, shearX:Single, shearY:Single): # -> 
        """ Shear(self: Strokes, shearX: Single, shearY: Single) """
        ...

    def StrokesEnumerator(self, *args): #cannot find CLR method
        """ StrokesEnumerator(s: Strokes) """
        ...

    def ToString(self) -> str:
        """ ToString(self: Strokes) -> str """
        ...

    def Transform(self, inkTransform:Matrix, applyOnPenWidth:bool = ...): # -> 
        """ Transform(self: Strokes, inkTransform: Matrix, applyOnPenWidth: bool)Transform(self: Strokes, inkTransform: Matrix) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    StrokesAdded = ...
    StrokesRemoved = ...


class StrokesEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ StrokesEventArgs(ids: Array[int]) """
    @property
    def StrokeIds(self) -> Array:
        """ Get: StrokeIds(self: StrokesEventArgs) -> Array[int] """
        ...


    def __new__(cls, ids:Array) -> Self:
        """ __new__(cls: type, ids: Array[int]) """
        ...


class StrokesEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ StrokesEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:StrokesEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: StrokesEventHandler, sender: object, e: StrokesEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: StrokesEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:StrokesEventArgs): # -> 
        """ Invoke(self: StrokesEventHandler, sender: object, e: StrokesEventArgs) """
        ...


class SystemGesture(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SystemGesture, values: DoubleTap (17), Drag (19), Flick (31), HoldEnter (21), HoldLeave (22), HoverEnter (23), HoverLeave (24), RightDrag (20), RightTap (18), Tap (16) """
    DoubleTap: SystemGesture = ...
    Drag: SystemGesture = ...
    Flick: SystemGesture = ...
    HoldEnter: SystemGesture = ...
    HoldLeave: SystemGesture = ...
    HoverEnter: SystemGesture = ...
    HoverLeave: SystemGesture = ...
    RightDrag: SystemGesture = ...
    RightTap: SystemGesture = ...
    Tap: SystemGesture = ...
    value__ = ...


class Tablet: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DeviceKind(self) -> TabletDeviceKind:
        """ Get: DeviceKind(self: Tablet) -> TabletDeviceKind """
        ...

    @property
    def HardwareCapabilities(self) -> TabletHardwareCapabilities:
        """ Get: HardwareCapabilities(self: Tablet) -> TabletHardwareCapabilities """
        ...

    @property
    def IsMultiTouch(self) -> bool:
        """ Get: IsMultiTouch(self: Tablet) -> bool """
        ...

    @property
    def MaximumCursors(self) -> int:
        """ Get: MaximumCursors(self: Tablet) -> int """
        ...

    @property
    def MaximumInputRectangle(self) -> Rectangle:
        """ Get: MaximumInputRectangle(self: Tablet) -> Rectangle """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Tablet) -> str """
        ...

    @property
    def PlugAndPlayId(self) -> str:
        """ Get: PlugAndPlayId(self: Tablet) -> str """
        ...


    def GetPropertyMetrics(self, id:Guid) -> TabletPropertyMetrics:
        """ GetPropertyMetrics(self: Tablet, id: Guid) -> TabletPropertyMetrics """
        ...

    def IsPacketPropertySupported(self, id:Guid) -> bool:
        """ IsPacketPropertySupported(self: Tablet, id: Guid) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: Tablet) -> str """
        ...


class TabletDeviceKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TabletDeviceKind, values: Mouse (0), Pen (1), Touch (2) """
    Mouse: TabletDeviceKind = ...
    Pen: TabletDeviceKind = ...
    Touch: TabletDeviceKind = ...
    value__ = ...


class TabletHardwareCapabilities(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TabletHardwareCapabilities, values: CursorMustTouch (2), CursorsHavePhysicalIds (8), HardProximity (4), Integrated (1) """
    CursorMustTouch: TabletHardwareCapabilities = ...
    CursorsHavePhysicalIds: TabletHardwareCapabilities = ...
    HardProximity: TabletHardwareCapabilities = ...
    Integrated: TabletHardwareCapabilities = ...
    value__ = ...


class TabletPropertyDescription: # skipped bases: <type 'object'>, <type 'object'>
    """ TabletPropertyDescription(packetPropertyId: Guid, tabletPropertyMetrics: TabletPropertyMetrics) """
    @property
    def PacketPropertyId(self) -> Guid:
        """ Get: PacketPropertyId(self: TabletPropertyDescription) -> Guid """
        ...

    @property
    def TabletPropertyMetrics(self) -> TabletPropertyMetrics:
        """ Get: TabletPropertyMetrics(self: TabletPropertyDescription) -> TabletPropertyMetrics """
        ...



class TabletPropertyDescriptionCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    TabletPropertyDescriptionCollection()
    TabletPropertyDescriptionCollection(inkToDeviceScaleX: Single, inkToDeviceScaleY: Single)
    """
    @property
    def InkToDeviceScaleX(self) -> Single:
        """ Get: InkToDeviceScaleX(self: TabletPropertyDescriptionCollection) -> Single """
        ...

    @property
    def InkToDeviceScaleY(self) -> Single:
        """ Get: InkToDeviceScaleY(self: TabletPropertyDescriptionCollection) -> Single """
        ...


    def Add(self, value:TabletPropertyDescription) -> int:
        """ Add(self: TabletPropertyDescriptionCollection, value: TabletPropertyDescription) -> int """
        ...

    def Remove(self, value:TabletPropertyDescription): # -> 
        """ Remove(self: TabletPropertyDescriptionCollection, value: TabletPropertyDescription) """
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


class TabletPropertyMetrics: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Maximum = ...
    Minimum = ...
    Resolution = ...
    Units = ...


class TabletPropertyMetricUnit(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TabletPropertyMetricUnit, values: Centimeters (2), Default (0), Degrees (3), Grams (7), Inches (1), Pounds (6), Radians (4), Seconds (5) """
    Centimeters: TabletPropertyMetricUnit = ...
    Default: TabletPropertyMetricUnit = ...
    Degrees: TabletPropertyMetricUnit = ...
    Grams: TabletPropertyMetricUnit = ...
    Inches: TabletPropertyMetricUnit = ...
    Pounds: TabletPropertyMetricUnit = ...
    Radians: TabletPropertyMetricUnit = ...
    Seconds: TabletPropertyMetricUnit = ...
    value__ = ...


class Tablets(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ Tablets() """
    @property
    def DefaultTablet(self) -> Tablet:
        """ Get: DefaultTablet(self: Tablets) -> Tablet """
        ...


    def GetEnumerator(self): # -> TabletsEnumerator
        """ GetEnumerator(self: Tablets) -> TabletsEnumerator """
        ...

    def IsPacketPropertySupported(self, g:Guid) -> bool:
        """ IsPacketPropertySupported(self: Tablets, g: Guid) -> bool """
        ...

    def TabletsEnumerator(self, *args): #cannot find CLR method
        """ TabletsEnumerator(t: Tablets) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class UnicodeRange: # skipped bases: <type 'object'>, <type 'object'>
    """ UnicodeRange(startingCharacter: Char, length: int) """
    @property
    def Length(self) -> int:
        """
        Get: Length(self: UnicodeRange) -> int
        Set: Length(self: UnicodeRange) = value
        """
        ...

    @property
    def StartingCharacter(self) -> Char:
        """
        Get: StartingCharacter(self: UnicodeRange) -> Char
        Set: StartingCharacter(self: UnicodeRange) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: UnicodeRange, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: UnicodeRange) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class WordList: # skipped bases: <type 'object'>, <type 'object'>
    """ WordList() """
    def Add(self, *__args:str): # -> 
        """ Add(self: WordList, s: str)Add(self: WordList, words: Array[str]) """
        ...

    def Merge(self, wl:WordList): # -> 
        """ Merge(self: WordList, wl: WordList) """
        ...

    def Remove(self, s:str): # -> 
        """ Remove(self: WordList, s: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...


# variables with complex values

