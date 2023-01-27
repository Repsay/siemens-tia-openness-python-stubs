# encoding: utf-8
# module System.Drawing.Printing calls itself Printing
# from System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Enum, EventArgs, IAsyncResult, 
    ICloneable, Int16, IntPtr, MulticastDelegate, Single, SystemException, 
    Type)

from System.Collections import IDictionary

from System.Collections.Specialized import StringCollection

from System.ComponentModel import (CancelEventArgs, Component, 
    ExpandableObjectConverter, ITypeDescriptorContext)

from System.Drawing import Graphics, Image, Rectangle, RectangleF

from System.Drawing.Imaging import ImageFormat

from System.Globalization import CultureInfo

from System.Security import CodeAccessPermission, IPermission

from System.Security.Permissions import (CodeAccessSecurityAttribute, 
    IUnrestrictedPermission, PermissionState)

from typing import Self

from Windows.Foundation import Size

"""The following names are not found in the module: (BoundEvent, 
    PaperSizeCollection, PaperSourceCollection, PrinterResolutionCollection, 
    field#)
"""

# no functions
# classes

class Duplex(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Duplex, values: Default (-1), Horizontal (3), Simplex (1), Vertical (2) """
    Default: Duplex = ...
    Horizontal: Duplex = ...
    Simplex: Duplex = ...
    value__ = ...
    Vertical: Duplex = ...


class InvalidPrinterException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ InvalidPrinterException(settings: PrinterSettings) """
    SerializeObjectState = ...


class Margins(ICloneable): # skipped bases: <type 'object'>
    """
    Margins()
    Margins(left: int, right: int, top: int, bottom: int)
    """
    @property
    def Bottom(self) -> int:
        """
        Get: Bottom(self: Margins) -> int
        Set: Bottom(self: Margins) = value
        """
        ...

    @property
    def Left(self) -> int:
        """
        Get: Left(self: Margins) -> int
        Set: Left(self: Margins) = value
        """
        ...

    @property
    def Right(self) -> int:
        """
        Get: Right(self: Margins) -> int
        Set: Right(self: Margins) = value
        """
        ...

    @property
    def Top(self) -> int:
        """
        Get: Top(self: Margins) -> int
        Set: Top(self: Margins) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Margins, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Margins) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Margins) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MarginsConverter(ExpandableObjectConverter): # skipped bases: <type 'object'>
    """ MarginsConverter() """
    def CanConvertFrom(self, *__args) -> bool:
        """ CanConvertFrom(self: MarginsConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool """
        ...

    def CanConvertTo(self, *__args) -> bool:
        """ CanConvertTo(self: MarginsConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool """
        ...

    def ConvertFrom(self, *__args) -> object:
        """ ConvertFrom(self: MarginsConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object """
        ...

    def ConvertTo(self, *__args) -> object:
        """ ConvertTo(self: MarginsConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object """
        ...

    def CreateInstance(self, *__args) -> object:
        """ CreateInstance(self: MarginsConverter, context: ITypeDescriptorContext, propertyValues: IDictionary) -> object """
        ...

    def GetCreateInstanceSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetCreateInstanceSupported(self: MarginsConverter, context: ITypeDescriptorContext) -> bool """
        ...


class PageSettings(ICloneable): # skipped bases: <type 'object'>
    """
    PageSettings()
    PageSettings(printerSettings: PrinterSettings)
    """
    @property
    def Bounds(self) -> Rectangle:
        """ Get: Bounds(self: PageSettings) -> Rectangle """
        ...

    @property
    def Color(self) -> bool:
        """
        Get: Color(self: PageSettings) -> bool
        Set: Color(self: PageSettings) = value
        """
        ...

    @property
    def HardMarginX(self) -> Single:
        """ Get: HardMarginX(self: PageSettings) -> Single """
        ...

    @property
    def HardMarginY(self) -> Single:
        """ Get: HardMarginY(self: PageSettings) -> Single """
        ...

    @property
    def Landscape(self) -> bool:
        """
        Get: Landscape(self: PageSettings) -> bool
        Set: Landscape(self: PageSettings) = value
        """
        ...

    @property
    def Margins(self) -> Margins:
        """
        Get: Margins(self: PageSettings) -> Margins
        Set: Margins(self: PageSettings) = value
        """
        ...

    @property
    def PaperSize(self) -> PaperSize:
        """
        Get: PaperSize(self: PageSettings) -> PaperSize
        Set: PaperSize(self: PageSettings) = value
        """
        ...

    @property
    def PaperSource(self) -> PaperSource:
        """
        Get: PaperSource(self: PageSettings) -> PaperSource
        Set: PaperSource(self: PageSettings) = value
        """
        ...

    @property
    def PrintableArea(self) -> RectangleF:
        """ Get: PrintableArea(self: PageSettings) -> RectangleF """
        ...

    @property
    def PrinterResolution(self) -> PrinterResolution:
        """
        Get: PrinterResolution(self: PageSettings) -> PrinterResolution
        Set: PrinterResolution(self: PageSettings) = value
        """
        ...

    @property
    def PrinterSettings(self) -> PrinterSettings:
        """
        Get: PrinterSettings(self: PageSettings) -> PrinterSettings
        Set: PrinterSettings(self: PageSettings) = value
        """
        ...


    def CopyToHdevmode(self, hdevmode:IntPtr): # -> 
        """ CopyToHdevmode(self: PageSettings, hdevmode: IntPtr) """
        ...

    def SetHdevmode(self, hdevmode:IntPtr): # -> 
        """ SetHdevmode(self: PageSettings, hdevmode: IntPtr) """
        ...

    def ToString(self) -> str:
        """ ToString(self: PageSettings) -> str """
        ...


class PaperKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PaperKind, values: A2 (66), A3 (8), A3Extra (63), A3ExtraTransverse (68), A3Rotated (76), A3Transverse (67), A4 (9), A4Extra (53), A4Plus (60), A4Rotated (77), A4Small (10), A4Transverse (55), A5 (11), A5Extra (64), A5Rotated (78), A5Transverse (61), A6 (70), A6Rotated (83), APlus (57), B4 (12), B4Envelope (33), B4JisRotated (79), B5 (13), B5Envelope (34), B5Extra (65), B5JisRotated (80), B5Transverse (62), B6Envelope (35), B6Jis (88), B6JisRotated (89), BPlus (58), C3Envelope (29), C4Envelope (30), C5Envelope (28), C65Envelope (32), C6Envelope (31), CSheet (24), Custom (0), DLEnvelope (27), DSheet (25), ESheet (26), Executive (7), Folio (14), GermanLegalFanfold (41), GermanStandardFanfold (40), InviteEnvelope (47), IsoB4 (42), ItalyEnvelope (36), JapaneseDoublePostcard (69), JapaneseDoublePostcardRotated (82), JapaneseEnvelopeChouNumber3 (73), JapaneseEnvelopeChouNumber3Rotated (86), JapaneseEnvelopeChouNumber4 (74), JapaneseEnvelopeChouNumber4Rotated (87), JapaneseEnvelopeKakuNumber2 (71), JapaneseEnvelopeKakuNumber2Rotated (84), JapaneseEnvelopeKakuNumber3 (72), JapaneseEnvelopeKakuNumber3Rotated (85), JapaneseEnvelopeYouNumber4 (91), JapaneseEnvelopeYouNumber4Rotated (92), JapanesePostcard (43), JapanesePostcardRotated (81), Ledger (4), Legal (5), LegalExtra (51), Letter (1), LetterExtra (50), LetterExtraTransverse (56), LetterPlus (59), LetterRotated (75), LetterSmall (2), LetterTransverse (54), MonarchEnvelope (37), Note (18), Number10Envelope (20), Number11Envelope (21), Number12Envelope (22), Number14Envelope (23), Number9Envelope (19), PersonalEnvelope (38), Prc16K (93), Prc16KRotated (106), Prc32K (94), Prc32KBig (95), Prc32KBigRotated (108), Prc32KRotated (107), PrcEnvelopeNumber1 (96), PrcEnvelopeNumber10 (105), PrcEnvelopeNumber10Rotated (118), PrcEnvelopeNumber1Rotated (109), PrcEnvelopeNumber2 (97), PrcEnvelopeNumber2Rotated (110), PrcEnvelopeNumber3 (98), PrcEnvelopeNumber3Rotated (111), PrcEnvelopeNumber4 (99), PrcEnvelopeNumber4Rotated (112), PrcEnvelopeNumber5 (100), PrcEnvelopeNumber5Rotated (113), PrcEnvelopeNumber6 (101), PrcEnvelopeNumber6Rotated (114), PrcEnvelopeNumber7 (102), PrcEnvelopeNumber7Rotated (115), PrcEnvelopeNumber8 (103), PrcEnvelopeNumber8Rotated (116), PrcEnvelopeNumber9 (104), PrcEnvelopeNumber9Rotated (117), Quarto (15), Standard10x11 (45), Standard10x14 (16), Standard11x17 (17), Standard12x11 (90), Standard15x11 (46), Standard9x11 (44), Statement (6), Tabloid (3), TabloidExtra (52), USStandardFanfold (39) """
    A2: PaperKind = ...
    A3: PaperKind = ...
    A3Extra: PaperKind = ...
    A3ExtraTransverse: PaperKind = ...
    A3Rotated: PaperKind = ...
    A3Transverse: PaperKind = ...
    A4: PaperKind = ...
    A4Extra: PaperKind = ...
    A4Plus: PaperKind = ...
    A4Rotated: PaperKind = ...
    A4Small: PaperKind = ...
    A4Transverse: PaperKind = ...
    A5: PaperKind = ...
    A5Extra: PaperKind = ...
    A5Rotated: PaperKind = ...
    A5Transverse: PaperKind = ...
    A6: PaperKind = ...
    A6Rotated: PaperKind = ...
    APlus: PaperKind = ...
    B4: PaperKind = ...
    B4Envelope: PaperKind = ...
    B4JisRotated: PaperKind = ...
    B5: PaperKind = ...
    B5Envelope: PaperKind = ...
    B5Extra: PaperKind = ...
    B5JisRotated: PaperKind = ...
    B5Transverse: PaperKind = ...
    B6Envelope: PaperKind = ...
    B6Jis: PaperKind = ...
    B6JisRotated: PaperKind = ...
    BPlus: PaperKind = ...
    C3Envelope: PaperKind = ...
    C4Envelope: PaperKind = ...
    C5Envelope: PaperKind = ...
    C65Envelope: PaperKind = ...
    C6Envelope: PaperKind = ...
    CSheet: PaperKind = ...
    Custom: PaperKind = ...
    DLEnvelope: PaperKind = ...
    DSheet: PaperKind = ...
    ESheet: PaperKind = ...
    Executive: PaperKind = ...
    Folio: PaperKind = ...
    GermanLegalFanfold: PaperKind = ...
    GermanStandardFanfold: PaperKind = ...
    InviteEnvelope: PaperKind = ...
    IsoB4: PaperKind = ...
    ItalyEnvelope: PaperKind = ...
    JapaneseDoublePostcard: PaperKind = ...
    JapaneseDoublePostcardRotated: PaperKind = ...
    JapaneseEnvelopeChouNumber3: PaperKind = ...
    JapaneseEnvelopeChouNumber3Rotated: PaperKind = ...
    JapaneseEnvelopeChouNumber4: PaperKind = ...
    JapaneseEnvelopeChouNumber4Rotated: PaperKind = ...
    JapaneseEnvelopeKakuNumber2: PaperKind = ...
    JapaneseEnvelopeKakuNumber2Rotated: PaperKind = ...
    JapaneseEnvelopeKakuNumber3: PaperKind = ...
    JapaneseEnvelopeKakuNumber3Rotated: PaperKind = ...
    JapaneseEnvelopeYouNumber4: PaperKind = ...
    JapaneseEnvelopeYouNumber4Rotated: PaperKind = ...
    JapanesePostcard: PaperKind = ...
    JapanesePostcardRotated: PaperKind = ...
    Ledger: PaperKind = ...
    Legal: PaperKind = ...
    LegalExtra: PaperKind = ...
    Letter: PaperKind = ...
    LetterExtra: PaperKind = ...
    LetterExtraTransverse: PaperKind = ...
    LetterPlus: PaperKind = ...
    LetterRotated: PaperKind = ...
    LetterSmall: PaperKind = ...
    LetterTransverse: PaperKind = ...
    MonarchEnvelope: PaperKind = ...
    Note: PaperKind = ...
    Number10Envelope: PaperKind = ...
    Number11Envelope: PaperKind = ...
    Number12Envelope: PaperKind = ...
    Number14Envelope: PaperKind = ...
    Number9Envelope: PaperKind = ...
    PersonalEnvelope: PaperKind = ...
    Prc16K: PaperKind = ...
    Prc16KRotated: PaperKind = ...
    Prc32K: PaperKind = ...
    Prc32KBig: PaperKind = ...
    Prc32KBigRotated: PaperKind = ...
    Prc32KRotated: PaperKind = ...
    PrcEnvelopeNumber1: PaperKind = ...
    PrcEnvelopeNumber10: PaperKind = ...
    PrcEnvelopeNumber10Rotated: PaperKind = ...
    PrcEnvelopeNumber1Rotated: PaperKind = ...
    PrcEnvelopeNumber2: PaperKind = ...
    PrcEnvelopeNumber2Rotated: PaperKind = ...
    PrcEnvelopeNumber3: PaperKind = ...
    PrcEnvelopeNumber3Rotated: PaperKind = ...
    PrcEnvelopeNumber4: PaperKind = ...
    PrcEnvelopeNumber4Rotated: PaperKind = ...
    PrcEnvelopeNumber5: PaperKind = ...
    PrcEnvelopeNumber5Rotated: PaperKind = ...
    PrcEnvelopeNumber6: PaperKind = ...
    PrcEnvelopeNumber6Rotated: PaperKind = ...
    PrcEnvelopeNumber7: PaperKind = ...
    PrcEnvelopeNumber7Rotated: PaperKind = ...
    PrcEnvelopeNumber8: PaperKind = ...
    PrcEnvelopeNumber8Rotated: PaperKind = ...
    PrcEnvelopeNumber9: PaperKind = ...
    PrcEnvelopeNumber9Rotated: PaperKind = ...
    Quarto: PaperKind = ...
    Standard10x11: PaperKind = ...
    Standard10x14: PaperKind = ...
    Standard11x17: PaperKind = ...
    Standard12x11: PaperKind = ...
    Standard15x11: PaperKind = ...
    Standard9x11: PaperKind = ...
    Statement: PaperKind = ...
    Tabloid: PaperKind = ...
    TabloidExtra: PaperKind = ...
    USStandardFanfold: PaperKind = ...
    value__ = ...


class PaperSize: # skipped bases: <type 'object'>, <type 'object'>
    """
    PaperSize()
    PaperSize(name: str, width: int, height: int)
    """
    @property
    def Height(self) -> int:
        """
        Get: Height(self: PaperSize) -> int
        Set: Height(self: PaperSize) = value
        """
        ...

    @property
    def Kind(self) -> PaperKind:
        """ Get: Kind(self: PaperSize) -> PaperKind """
        ...

    @property
    def PaperName(self) -> str:
        """
        Get: PaperName(self: PaperSize) -> str
        Set: PaperName(self: PaperSize) = value
        """
        ...

    @property
    def RawKind(self) -> int:
        """
        Get: RawKind(self: PaperSize) -> int
        Set: RawKind(self: PaperSize) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: PaperSize) -> int
        Set: Width(self: PaperSize) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: PaperSize) -> str """
        ...


class PaperSource: # skipped bases: <type 'object'>, <type 'object'>
    """ PaperSource() """
    @property
    def Kind(self) -> PaperSourceKind:
        """ Get: Kind(self: PaperSource) -> PaperSourceKind """
        ...

    @property
    def RawKind(self) -> int:
        """
        Get: RawKind(self: PaperSource) -> int
        Set: RawKind(self: PaperSource) = value
        """
        ...

    @property
    def SourceName(self) -> str:
        """
        Get: SourceName(self: PaperSource) -> str
        Set: SourceName(self: PaperSource) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: PaperSource) -> str """
        ...


class PaperSourceKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PaperSourceKind, values: AutomaticFeed (7), Cassette (14), Custom (257), Envelope (5), FormSource (15), LargeCapacity (11), LargeFormat (10), Lower (2), Manual (4), ManualFeed (6), Middle (3), SmallFormat (9), TractorFeed (8), Upper (1) """
    AutomaticFeed: PaperSourceKind = ...
    Cassette: PaperSourceKind = ...
    Custom: PaperSourceKind = ...
    Envelope: PaperSourceKind = ...
    FormSource: PaperSourceKind = ...
    LargeCapacity: PaperSourceKind = ...
    LargeFormat: PaperSourceKind = ...
    Lower: PaperSourceKind = ...
    Manual: PaperSourceKind = ...
    ManualFeed: PaperSourceKind = ...
    Middle: PaperSourceKind = ...
    SmallFormat: PaperSourceKind = ...
    TractorFeed: PaperSourceKind = ...
    Upper: PaperSourceKind = ...
    value__ = ...


class PreviewPageInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ PreviewPageInfo(image: Image, physicalSize: Size) """
    @property
    def Image(self) -> Image:
        """ Get: Image(self: PreviewPageInfo) -> Image """
        ...

    @property
    def PhysicalSize(self) -> Size:
        """ Get: PhysicalSize(self: PreviewPageInfo) -> Size """
        ...



class PrintController: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsPreview(self) -> bool:
        """ Get: IsPreview(self: PrintController) -> bool """
        ...


    def OnEndPage(self, document:PrintDocument, e:PrintPageEventArgs): # -> 
        """ OnEndPage(self: PrintController, document: PrintDocument, e: PrintPageEventArgs) """
        ...

    def OnEndPrint(self, document:PrintDocument, e:PrintEventArgs): # -> 
        """ OnEndPrint(self: PrintController, document: PrintDocument, e: PrintEventArgs) """
        ...

    def OnStartPage(self, document:PrintDocument, e:PrintPageEventArgs) -> Graphics:
        """ OnStartPage(self: PrintController, document: PrintDocument, e: PrintPageEventArgs) -> Graphics """
        ...

    def OnStartPrint(self, document:PrintDocument, e:PrintEventArgs): # -> 
        """ OnStartPrint(self: PrintController, document: PrintDocument, e: PrintEventArgs) """
        ...


class PreviewPrintController(PrintController): # skipped bases: <type 'object'>
    """ PreviewPrintController() """
    @property
    def UseAntiAlias(self) -> bool:
        """
        Get: UseAntiAlias(self: PreviewPrintController) -> bool
        Set: UseAntiAlias(self: PreviewPrintController) = value
        """
        ...


    def GetPreviewPageInfo(self) -> Array:
        """ GetPreviewPageInfo(self: PreviewPrintController) -> Array[PreviewPageInfo] """
        ...


class PrintAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PrintAction, values: PrintToFile (0), PrintToPreview (1), PrintToPrinter (2) """
    PrintToFile: PrintAction = ...
    PrintToPreview: PrintAction = ...
    PrintToPrinter: PrintAction = ...
    value__ = ...


class PrintDocument(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ PrintDocument() """
    @property
    def DefaultPageSettings(self) -> PageSettings:
        """
        Get: DefaultPageSettings(self: PrintDocument) -> PageSettings
        Set: DefaultPageSettings(self: PrintDocument) = value
        """
        ...

    @property
    def DocumentName(self) -> str:
        """
        Get: DocumentName(self: PrintDocument) -> str
        Set: DocumentName(self: PrintDocument) = value
        """
        ...

    @property
    def OriginAtMargins(self) -> bool:
        """
        Get: OriginAtMargins(self: PrintDocument) -> bool
        Set: OriginAtMargins(self: PrintDocument) = value
        """
        ...

    @property
    def PrintController(self) -> PrintController:
        """
        Get: PrintController(self: PrintDocument) -> PrintController
        Set: PrintController(self: PrintDocument) = value
        """
        ...

    @property
    def PrinterSettings(self) -> PrinterSettings:
        """
        Get: PrinterSettings(self: PrintDocument) -> PrinterSettings
        Set: PrinterSettings(self: PrintDocument) = value
        """
        ...


    def OnBeginPrint(self, *args): #cannot find CLR method
        """ OnBeginPrint(self: PrintDocument, e: PrintEventArgs) """
        ...

    def OnEndPrint(self, *args): #cannot find CLR method
        """ OnEndPrint(self: PrintDocument, e: PrintEventArgs) """
        ...

    def OnPrintPage(self, *args): #cannot find CLR method
        """ OnPrintPage(self: PrintDocument, e: PrintPageEventArgs) """
        ...

    def OnQueryPageSettings(self, *args): #cannot find CLR method
        """ OnQueryPageSettings(self: PrintDocument, e: QueryPageSettingsEventArgs) """
        ...

    def Print(self): # -> 
        """ Print(self: PrintDocument) """
        ...

    BeginPrint = ...
    EndPrint = ...
    PrintPage = ...
    QueryPageSettings = ...


class PrinterResolution: # skipped bases: <type 'object'>, <type 'object'>
    """ PrinterResolution() """
    @property
    def Kind(self) -> PrinterResolutionKind:
        """
        Get: Kind(self: PrinterResolution) -> PrinterResolutionKind
        Set: Kind(self: PrinterResolution) = value
        """
        ...

    @property
    def X(self) -> int:
        """
        Get: X(self: PrinterResolution) -> int
        Set: X(self: PrinterResolution) = value
        """
        ...

    @property
    def Y(self) -> int:
        """
        Get: Y(self: PrinterResolution) -> int
        Set: Y(self: PrinterResolution) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: PrinterResolution) -> str """
        ...


class PrinterResolutionKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PrinterResolutionKind, values: Custom (0), Draft (-1), High (-4), Low (-2), Medium (-3) """
    Custom: PrinterResolutionKind = ...
    Draft: PrinterResolutionKind = ...
    High: PrinterResolutionKind = ...
    Low: PrinterResolutionKind = ...
    Medium: PrinterResolutionKind = ...
    value__ = ...


class PrinterSettings(ICloneable): # skipped bases: <type 'object'>
    """ PrinterSettings() """
    @property
    def CanDuplex(self) -> bool:
        """ Get: CanDuplex(self: PrinterSettings) -> bool """
        ...

    @property
    def Collate(self) -> bool:
        """
        Get: Collate(self: PrinterSettings) -> bool
        Set: Collate(self: PrinterSettings) = value
        """
        ...

    @property
    def Copies(self) -> Int16:
        """
        Get: Copies(self: PrinterSettings) -> Int16
        Set: Copies(self: PrinterSettings) = value
        """
        ...

    @property
    def DefaultPageSettings(self) -> PageSettings:
        """ Get: DefaultPageSettings(self: PrinterSettings) -> PageSettings """
        ...

    @property
    def Duplex(self) -> Duplex:
        """
        Get: Duplex(self: PrinterSettings) -> Duplex
        Set: Duplex(self: PrinterSettings) = value
        """
        ...

    @property
    def FromPage(self) -> int:
        """
        Get: FromPage(self: PrinterSettings) -> int
        Set: FromPage(self: PrinterSettings) = value
        """
        ...

    @property
    def InstalledPrinters(self) -> StringCollection:
        """ Get: InstalledPrinters() -> StringCollection """
        ...

    @property
    def IsDefaultPrinter(self) -> bool:
        """ Get: IsDefaultPrinter(self: PrinterSettings) -> bool """
        ...

    @property
    def IsPlotter(self) -> bool:
        """ Get: IsPlotter(self: PrinterSettings) -> bool """
        ...

    @property
    def IsValid(self) -> bool:
        """ Get: IsValid(self: PrinterSettings) -> bool """
        ...

    @property
    def LandscapeAngle(self) -> int:
        """ Get: LandscapeAngle(self: PrinterSettings) -> int """
        ...

    @property
    def MaximumCopies(self) -> int:
        """ Get: MaximumCopies(self: PrinterSettings) -> int """
        ...

    @property
    def MaximumPage(self) -> int:
        """
        Get: MaximumPage(self: PrinterSettings) -> int
        Set: MaximumPage(self: PrinterSettings) = value
        """
        ...

    @property
    def MinimumPage(self) -> int:
        """
        Get: MinimumPage(self: PrinterSettings) -> int
        Set: MinimumPage(self: PrinterSettings) = value
        """
        ...

    @property
    def PaperSizes(self): # -> PaperSizeCollection
        """ Get: PaperSizes(self: PrinterSettings) -> PaperSizeCollection """
        ...

    @property
    def PaperSources(self): # -> PaperSourceCollection
        """ Get: PaperSources(self: PrinterSettings) -> PaperSourceCollection """
        ...

    @property
    def PrinterName(self) -> str:
        """
        Get: PrinterName(self: PrinterSettings) -> str
        Set: PrinterName(self: PrinterSettings) = value
        """
        ...

    @property
    def PrinterResolutions(self): # -> PrinterResolutionCollection
        """ Get: PrinterResolutions(self: PrinterSettings) -> PrinterResolutionCollection """
        ...

    @property
    def PrintFileName(self) -> str:
        """
        Get: PrintFileName(self: PrinterSettings) -> str
        Set: PrintFileName(self: PrinterSettings) = value
        """
        ...

    @property
    def PrintRange(self) -> PrintRange:
        """
        Get: PrintRange(self: PrinterSettings) -> PrintRange
        Set: PrintRange(self: PrinterSettings) = value
        """
        ...

    @property
    def PrintToFile(self) -> bool:
        """
        Get: PrintToFile(self: PrinterSettings) -> bool
        Set: PrintToFile(self: PrinterSettings) = value
        """
        ...

    @property
    def SupportsColor(self) -> bool:
        """ Get: SupportsColor(self: PrinterSettings) -> bool """
        ...

    @property
    def ToPage(self) -> int:
        """
        Get: ToPage(self: PrinterSettings) -> int
        Set: ToPage(self: PrinterSettings) = value
        """
        ...


    def CreateMeasurementGraphics(self, *__args:bool) -> Graphics:
        """
        CreateMeasurementGraphics(self: PrinterSettings) -> Graphics
        CreateMeasurementGraphics(self: PrinterSettings, honorOriginAtMargins: bool) -> Graphics
        CreateMeasurementGraphics(self: PrinterSettings, pageSettings: PageSettings) -> Graphics
        CreateMeasurementGraphics(self: PrinterSettings, pageSettings: PageSettings, honorOriginAtMargins: bool) -> Graphics
        """
        ...

    def GetHdevmode(self, pageSettings:PageSettings = ...) -> IntPtr:
        """
        GetHdevmode(self: PrinterSettings) -> IntPtr
        GetHdevmode(self: PrinterSettings, pageSettings: PageSettings) -> IntPtr
        """
        ...

    def GetHdevnames(self) -> IntPtr:
        """ GetHdevnames(self: PrinterSettings) -> IntPtr """
        ...

    def IsDirectPrintingSupported(self, *__args:ImageFormat) -> bool:
        """
        IsDirectPrintingSupported(self: PrinterSettings, imageFormat: ImageFormat) -> bool
        IsDirectPrintingSupported(self: PrinterSettings, image: Image) -> bool
        """
        ...

    def PaperSizeCollection(self, *args): #cannot find CLR method
        """ PaperSizeCollection(array: Array[PaperSize]) """
        ...

    def PaperSourceCollection(self, *args): #cannot find CLR method
        """ PaperSourceCollection(array: Array[PaperSource]) """
        ...

    def PrinterResolutionCollection(self, *args): #cannot find CLR method
        """ PrinterResolutionCollection(array: Array[PrinterResolution]) """
        ...

    def SetHdevmode(self, hdevmode:IntPtr): # -> 
        """ SetHdevmode(self: PrinterSettings, hdevmode: IntPtr) """
        ...

    def SetHdevnames(self, hdevnames:IntPtr): # -> 
        """ SetHdevnames(self: PrinterSettings, hdevnames: IntPtr) """
        ...

    def StringCollection(self, *args): #cannot find CLR method
        """ StringCollection(array: Array[str]) """
        ...

    def ToString(self) -> str:
        """ ToString(self: PrinterSettings) -> str """
        ...



class PrinterUnit(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PrinterUnit, values: Display (0), HundredthsOfAMillimeter (2), TenthsOfAMillimeter (3), ThousandthsOfAnInch (1) """
    Display: PrinterUnit = ...
    HundredthsOfAMillimeter: PrinterUnit = ...
    TenthsOfAMillimeter: PrinterUnit = ...
    ThousandthsOfAnInch: PrinterUnit = ...
    value__ = ...


class PrinterUnitConvert: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Convert(value:float, fromUnit:PrinterUnit, toUnit:PrinterUnit) -> float:
        """
        Convert(value: float, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> float
        Convert(value: int, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> int
        Convert(value: Point, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> Point
        Convert(value: Size, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> Size
        Convert(value: Rectangle, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> Rectangle
        Convert(value: Margins, fromUnit: PrinterUnit, toUnit: PrinterUnit) -> Margins
        """
        ...


class PrintEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ PrintEventArgs() """
    @property
    def PrintAction(self) -> PrintAction:
        """ Get: PrintAction(self: PrintEventArgs) -> PrintAction """
        ...



class PrintEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PrintEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:PrintEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PrintEventHandler, sender: object, e: PrintEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PrintEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:PrintEventArgs): # -> 
        """ Invoke(self: PrintEventHandler, sender: object, e: PrintEventArgs) """
        ...


class PrintingPermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    PrintingPermission(state: PermissionState)
    PrintingPermission(printingLevel: PrintingPermissionLevel)
    """
    @property
    def Level(self) -> PrintingPermissionLevel:
        """
        Get: Level(self: PrintingPermission) -> PrintingPermissionLevel
        Set: Level(self: PrintingPermission) = value
        """
        ...


    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, printingLevel: PrintingPermissionLevel)
        """
        ...


class PrintingPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PrintingPermissionAttribute(action: SecurityAction) """
    @property
    def Level(self) -> PrintingPermissionLevel:
        """
        Get: Level(self: PrintingPermissionAttribute) -> PrintingPermissionLevel
        Set: Level(self: PrintingPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: PrintingPermissionAttribute) -> IPermission """
        ...


class PrintingPermissionLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PrintingPermissionLevel, values: AllPrinting (3), DefaultPrinting (2), NoPrinting (0), SafePrinting (1) """
    AllPrinting: PrintingPermissionLevel = ...
    DefaultPrinting: PrintingPermissionLevel = ...
    NoPrinting: PrintingPermissionLevel = ...
    SafePrinting: PrintingPermissionLevel = ...
    value__ = ...


class PrintPageEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ PrintPageEventArgs(graphics: Graphics, marginBounds: Rectangle, pageBounds: Rectangle, pageSettings: PageSettings) """
    @property
    def Cancel(self) -> bool:
        """
        Get: Cancel(self: PrintPageEventArgs) -> bool
        Set: Cancel(self: PrintPageEventArgs) = value
        """
        ...

    @property
    def Graphics(self) -> Graphics:
        """ Get: Graphics(self: PrintPageEventArgs) -> Graphics """
        ...

    @property
    def HasMorePages(self) -> bool:
        """
        Get: HasMorePages(self: PrintPageEventArgs) -> bool
        Set: HasMorePages(self: PrintPageEventArgs) = value
        """
        ...

    @property
    def MarginBounds(self) -> Rectangle:
        """ Get: MarginBounds(self: PrintPageEventArgs) -> Rectangle """
        ...

    @property
    def PageBounds(self) -> Rectangle:
        """ Get: PageBounds(self: PrintPageEventArgs) -> Rectangle """
        ...

    @property
    def PageSettings(self) -> PageSettings:
        """ Get: PageSettings(self: PrintPageEventArgs) -> PageSettings """
        ...


    def __new__(cls, graphics:Graphics, marginBounds:Rectangle, pageBounds:Rectangle, pageSettings:PageSettings) -> Self:
        """ __new__(cls: type, graphics: Graphics, marginBounds: Rectangle, pageBounds: Rectangle, pageSettings: PageSettings) """
        ...


class PrintPageEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PrintPageEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:PrintPageEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PrintPageEventHandler, sender: object, e: PrintPageEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PrintPageEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:PrintPageEventArgs): # -> 
        """ Invoke(self: PrintPageEventHandler, sender: object, e: PrintPageEventArgs) """
        ...


class PrintRange(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PrintRange, values: AllPages (0), CurrentPage (4194304), Selection (1), SomePages (2) """
    AllPages: PrintRange = ...
    CurrentPage: PrintRange = ...
    Selection: PrintRange = ...
    SomePages: PrintRange = ...
    value__ = ...


class QueryPageSettingsEventArgs(PrintEventArgs): # skipped bases: <type 'object'>
    """ QueryPageSettingsEventArgs(pageSettings: PageSettings) """
    @property
    def PageSettings(self) -> PageSettings:
        """
        Get: PageSettings(self: QueryPageSettingsEventArgs) -> PageSettings
        Set: PageSettings(self: QueryPageSettingsEventArgs) = value
        """
        ...


    def __new__(cls, pageSettings:PageSettings) -> Self:
        """ __new__(cls: type, pageSettings: PageSettings) """
        ...


class QueryPageSettingsEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ QueryPageSettingsEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:QueryPageSettingsEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: QueryPageSettingsEventHandler, sender: object, e: QueryPageSettingsEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: QueryPageSettingsEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:QueryPageSettingsEventArgs): # -> 
        """ Invoke(self: QueryPageSettingsEventHandler, sender: object, e: QueryPageSettingsEventArgs) """
        ...


class StandardPrintController(PrintController): # skipped bases: <type 'object'>
    """ StandardPrintController() """
    pass

