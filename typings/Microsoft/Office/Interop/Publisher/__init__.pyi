# encoding: utf-8
# module Microsoft.Office.Interop.Publisher calls itself Publisher
# from Microsoft.Office.Interop.Publisher, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualStudio.CommandBars import CommandBars

from System import Enum, MulticastDelegate, Single

from System.Collections import IEnumerable

"""The following names are not found in the module: (Assistant, BoundEvent, 
    COMAddIns, FileSearch, IAssistance, MsoAlignCmd, MsoArrowheadLength, 
    MsoArrowheadStyle, MsoArrowheadWidth, MsoAutoShapeType, 
    MsoAutomationSecurity, MsoBevelType, MsoBlackWhiteMode, 
    MsoCalloutAngleType, MsoCalloutDropType, MsoCalloutType, MsoConnectorType, 
    MsoDebugOptions, MsoDistributeCmd, MsoEditingType, MsoEncoding, 
    MsoEnvelope, MsoExtrusionColorType, MsoFillType, MsoFilterComparison, 
    MsoFilterConjunction, MsoFlipCmd, MsoGradientColorType, MsoGradientStyle, 
    MsoHyperlinkType, MsoLanguageID, MsoLineCapStyle, MsoLineDashStyle, 
    MsoLineFillType, MsoLineJoinStyle, MsoLineStyle, MsoPatternType, 
    MsoPictureColorType, MsoPresetExtrusionDirection, MsoPresetGradientType, 
    MsoPresetLightingDirection, MsoPresetLightingSoftness, MsoPresetMaterial, 
    MsoPresetTextEffect, MsoPresetTextEffectShape, MsoPresetTexture, 
    MsoPresetThreeDFormat, MsoReflectionType, MsoScaleFrom, MsoSegmentType, 
    MsoShadowType, MsoSoftEdgeType, MsoTextEffectAlignment, 
    MsoTextureAlignment, MsoTextureType, MsoTriState, MsoZOrderCmd, 
    OfficeDataSourceObject, WebComponentFormat, _IMsoDispObj, __ComObject, 
    field#)
"""

# no functions
# classes

class Adjustments(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Adjustments) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Adjustments) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Adjustments) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class AdvancedPrintOptions: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AllowBleeds(self) -> bool:
        """
        Get: AllowBleeds(self: AdvancedPrintOptions) -> bool
        Set: AllowBleeds(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: AdvancedPrintOptions) -> Application """
        ...

    @property
    def BackSideInsertFaceUp(self) -> bool:
        """
        Get: BackSideInsertFaceUp(self: AdvancedPrintOptions) -> bool
        Set: BackSideInsertFaceUp(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def GraphicsResolution(self) -> PbPrintGraphics:
        """
        Get: GraphicsResolution(self: AdvancedPrintOptions) -> PbPrintGraphics
        Set: GraphicsResolution(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def HorizontalFlip(self) -> bool:
        """
        Get: HorizontalFlip(self: AdvancedPrintOptions) -> bool
        Set: HorizontalFlip(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def InksToPrint(self) -> PbInksToPrint:
        """
        Get: InksToPrint(self: AdvancedPrintOptions) -> PbInksToPrint
        Set: InksToPrint(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def IsPostscriptPrinter(self) -> bool:
        """ Get: IsPostscriptPrinter(self: AdvancedPrintOptions) -> bool """
        ...

    @property
    def ManualFeedAlign(self) -> PbPlacementType:
        """
        Get: ManualFeedAlign(self: AdvancedPrintOptions) -> PbPlacementType
        Set: ManualFeedAlign(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def ManualFeedDirection(self) -> PbOrientationType:
        """
        Get: ManualFeedDirection(self: AdvancedPrintOptions) -> PbOrientationType
        Set: ManualFeedDirection(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def NegativeImage(self) -> bool:
        """
        Get: NegativeImage(self: AdvancedPrintOptions) -> bool
        Set: NegativeImage(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def PageRotated(self) -> bool:
        """
        Get: PageRotated(self: AdvancedPrintOptions) -> bool
        Set: PageRotated(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: AdvancedPrintOptions) -> object """
        ...

    @property
    def PrintablePlates(self) -> PrintablePlates:
        """ Get: PrintablePlates(self: AdvancedPrintOptions) -> PrintablePlates """
        ...

    @property
    def PrintableRect(self) -> PrintableRect:
        """ Get: PrintableRect(self: AdvancedPrintOptions) -> PrintableRect """
        ...

    @property
    def PrintBlankPlates(self) -> bool:
        """
        Get: PrintBlankPlates(self: AdvancedPrintOptions) -> bool
        Set: PrintBlankPlates(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def PrintBleedMarks(self) -> bool:
        """
        Get: PrintBleedMarks(self: AdvancedPrintOptions) -> bool
        Set: PrintBleedMarks(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def PrintCMYKByDefault(self) -> bool:
        """
        Get: PrintCMYKByDefault(self: AdvancedPrintOptions) -> bool
        Set: PrintCMYKByDefault(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def PrintColorBars(self) -> bool:
        """
        Get: PrintColorBars(self: AdvancedPrintOptions) -> bool
        Set: PrintColorBars(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def PrintCropMarks(self) -> bool:
        """
        Get: PrintCropMarks(self: AdvancedPrintOptions) -> bool
        Set: PrintCropMarks(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def PrintDensityBars(self) -> bool:
        """
        Get: PrintDensityBars(self: AdvancedPrintOptions) -> bool
        Set: PrintDensityBars(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def PrintJobInformation(self) -> bool:
        """
        Get: PrintJobInformation(self: AdvancedPrintOptions) -> bool
        Set: PrintJobInformation(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def PrintMode(self) -> PbPrintMode:
        """
        Get: PrintMode(self: AdvancedPrintOptions) -> PbPrintMode
        Set: PrintMode(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def PrintRegistrationMarks(self) -> bool:
        """
        Get: PrintRegistrationMarks(self: AdvancedPrintOptions) -> bool
        Set: PrintRegistrationMarks(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def Resolution(self) -> str:
        """
        Get: Resolution(self: AdvancedPrintOptions) -> str
        Set: Resolution(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def UseCustomHalftone(self) -> bool:
        """
        Get: UseCustomHalftone(self: AdvancedPrintOptions) -> bool
        Set: UseCustomHalftone(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def UseOnlyPublicationFonts(self) -> bool:
        """
        Get: UseOnlyPublicationFonts(self: AdvancedPrintOptions) -> bool
        Set: UseOnlyPublicationFonts(self: AdvancedPrintOptions) = value
        """
        ...

    @property
    def VerticalFlip(self) -> bool:
        """
        Get: VerticalFlip(self: AdvancedPrintOptions) -> bool
        Set: VerticalFlip(self: AdvancedPrintOptions) = value
        """
        ...



class ApplicationEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_AfterPrint(self): # -> 
        """ add_AfterPrint(self: ApplicationEvents_Event, : ApplicationEvents_AfterPrintEventHandler) """
        ...

    def add_BeforePrint(self): # -> 
        """ add_BeforePrint(self: ApplicationEvents_Event, : ApplicationEvents_BeforePrintEventHandler) """
        ...

    def add_DocumentBeforeClose(self): # -> 
        """ add_DocumentBeforeClose(self: ApplicationEvents_Event, : ApplicationEvents_DocumentBeforeCloseEventHandler) """
        ...

    def add_DocumentOpen(self): # -> 
        """ add_DocumentOpen(self: ApplicationEvents_Event, : ApplicationEvents_DocumentOpenEventHandler) """
        ...

    def add_HideCatalogUI(self): # -> 
        """ add_HideCatalogUI(self: ApplicationEvents_Event, : ApplicationEvents_HideCatalogUIEventHandler) """
        ...

    def add_MailMergeAfterMerge(self): # -> 
        """ add_MailMergeAfterMerge(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeAfterMergeEventHandler) """
        ...

    def add_MailMergeAfterRecordMerge(self): # -> 
        """ add_MailMergeAfterRecordMerge(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeAfterRecordMergeEventHandler) """
        ...

    def add_MailMergeBeforeMerge(self): # -> 
        """ add_MailMergeBeforeMerge(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeBeforeMergeEventHandler) """
        ...

    def add_MailMergeBeforeRecordMerge(self): # -> 
        """ add_MailMergeBeforeRecordMerge(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeBeforeRecordMergeEventHandler) """
        ...

    def add_MailMergeDataSourceLoad(self): # -> 
        """ add_MailMergeDataSourceLoad(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeDataSourceLoadEventHandler) """
        ...

    def add_MailMergeDataSourceValidate(self): # -> 
        """ add_MailMergeDataSourceValidate(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeDataSourceValidateEventHandler) """
        ...

    def add_MailMergeGenerateBarcode(self): # -> 
        """ add_MailMergeGenerateBarcode(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeGenerateBarcodeEventHandler) """
        ...

    def add_MailMergeInsertBarcode(self): # -> 
        """ add_MailMergeInsertBarcode(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeInsertBarcodeEventHandler) """
        ...

    def add_MailMergeRecipientListClose(self): # -> 
        """ add_MailMergeRecipientListClose(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeRecipientListCloseEventHandler) """
        ...

    def add_MailMergeWizardFollowUpCustom(self): # -> 
        """ add_MailMergeWizardFollowUpCustom(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeWizardFollowUpCustomEventHandler) """
        ...

    def add_MailMergeWizardSendToCustom(self): # -> 
        """ add_MailMergeWizardSendToCustom(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeWizardSendToCustomEventHandler) """
        ...

    def add_MailMergeWizardStateChange(self): # -> 
        """ add_MailMergeWizardStateChange(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeWizardStateChangeEventHandler) """
        ...

    def add_NewDocument(self): # -> 
        """ add_NewDocument(self: ApplicationEvents_Event, : ApplicationEvents_NewDocumentEventHandler) """
        ...

    def add_Quit(self): # -> 
        """ add_Quit(self: ApplicationEvents_Event, : ApplicationEvents_QuitEventHandler) """
        ...

    def add_ShowCatalogUI(self): # -> 
        """ add_ShowCatalogUI(self: ApplicationEvents_Event, : ApplicationEvents_ShowCatalogUIEventHandler) """
        ...

    def add_WindowActivate(self): # -> 
        """ add_WindowActivate(self: ApplicationEvents_Event, : ApplicationEvents_WindowActivateEventHandler) """
        ...

    def add_WindowDeactivate(self): # -> 
        """ add_WindowDeactivate(self: ApplicationEvents_Event, : ApplicationEvents_WindowDeactivateEventHandler) """
        ...

    def add_WindowPageChange(self): # -> 
        """ add_WindowPageChange(self: ApplicationEvents_Event, : ApplicationEvents_WindowPageChangeEventHandler) """
        ...

    def remove_AfterPrint(self): # -> 
        """ remove_AfterPrint(self: ApplicationEvents_Event, : ApplicationEvents_AfterPrintEventHandler) """
        ...

    def remove_BeforePrint(self): # -> 
        """ remove_BeforePrint(self: ApplicationEvents_Event, : ApplicationEvents_BeforePrintEventHandler) """
        ...

    def remove_DocumentBeforeClose(self): # -> 
        """ remove_DocumentBeforeClose(self: ApplicationEvents_Event, : ApplicationEvents_DocumentBeforeCloseEventHandler) """
        ...

    def remove_DocumentOpen(self): # -> 
        """ remove_DocumentOpen(self: ApplicationEvents_Event, : ApplicationEvents_DocumentOpenEventHandler) """
        ...

    def remove_HideCatalogUI(self): # -> 
        """ remove_HideCatalogUI(self: ApplicationEvents_Event, : ApplicationEvents_HideCatalogUIEventHandler) """
        ...

    def remove_MailMergeAfterMerge(self): # -> 
        """ remove_MailMergeAfterMerge(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeAfterMergeEventHandler) """
        ...

    def remove_MailMergeAfterRecordMerge(self): # -> 
        """ remove_MailMergeAfterRecordMerge(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeAfterRecordMergeEventHandler) """
        ...

    def remove_MailMergeBeforeMerge(self): # -> 
        """ remove_MailMergeBeforeMerge(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeBeforeMergeEventHandler) """
        ...

    def remove_MailMergeBeforeRecordMerge(self): # -> 
        """ remove_MailMergeBeforeRecordMerge(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeBeforeRecordMergeEventHandler) """
        ...

    def remove_MailMergeDataSourceLoad(self): # -> 
        """ remove_MailMergeDataSourceLoad(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeDataSourceLoadEventHandler) """
        ...

    def remove_MailMergeDataSourceValidate(self): # -> 
        """ remove_MailMergeDataSourceValidate(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeDataSourceValidateEventHandler) """
        ...

    def remove_MailMergeGenerateBarcode(self): # -> 
        """ remove_MailMergeGenerateBarcode(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeGenerateBarcodeEventHandler) """
        ...

    def remove_MailMergeInsertBarcode(self): # -> 
        """ remove_MailMergeInsertBarcode(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeInsertBarcodeEventHandler) """
        ...

    def remove_MailMergeRecipientListClose(self): # -> 
        """ remove_MailMergeRecipientListClose(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeRecipientListCloseEventHandler) """
        ...

    def remove_MailMergeWizardFollowUpCustom(self): # -> 
        """ remove_MailMergeWizardFollowUpCustom(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeWizardFollowUpCustomEventHandler) """
        ...

    def remove_MailMergeWizardSendToCustom(self): # -> 
        """ remove_MailMergeWizardSendToCustom(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeWizardSendToCustomEventHandler) """
        ...

    def remove_MailMergeWizardStateChange(self): # -> 
        """ remove_MailMergeWizardStateChange(self: ApplicationEvents_Event, : ApplicationEvents_MailMergeWizardStateChangeEventHandler) """
        ...

    def remove_NewDocument(self): # -> 
        """ remove_NewDocument(self: ApplicationEvents_Event, : ApplicationEvents_NewDocumentEventHandler) """
        ...

    def remove_Quit(self): # -> 
        """ remove_Quit(self: ApplicationEvents_Event, : ApplicationEvents_QuitEventHandler) """
        ...

    def remove_ShowCatalogUI(self): # -> 
        """ remove_ShowCatalogUI(self: ApplicationEvents_Event, : ApplicationEvents_ShowCatalogUIEventHandler) """
        ...

    def remove_WindowActivate(self): # -> 
        """ remove_WindowActivate(self: ApplicationEvents_Event, : ApplicationEvents_WindowActivateEventHandler) """
        ...

    def remove_WindowDeactivate(self): # -> 
        """ remove_WindowDeactivate(self: ApplicationEvents_Event, : ApplicationEvents_WindowDeactivateEventHandler) """
        ...

    def remove_WindowPageChange(self): # -> 
        """ remove_WindowPageChange(self: ApplicationEvents_Event, : ApplicationEvents_WindowPageChangeEventHandler) """
        ...

    AfterPrint = ...
    BeforePrint = ...
    DocumentBeforeClose = ...
    DocumentOpen = ...
    HideCatalogUI = ...
    MailMergeAfterMerge = ...
    MailMergeAfterRecordMerge = ...
    MailMergeBeforeMerge = ...
    MailMergeBeforeRecordMerge = ...
    MailMergeDataSourceLoad = ...
    MailMergeDataSourceValidate = ...
    MailMergeGenerateBarcode = ...
    MailMergeInsertBarcode = ...
    MailMergeRecipientListClose = ...
    MailMergeWizardFollowUpCustom = ...
    MailMergeWizardSendToCustom = ...
    MailMergeWizardStateChange = ...
    NewDocument = ...
    Quit = ...
    ShowCatalogUI = ...
    WindowActivate = ...
    WindowDeactivate = ...
    WindowPageChange = ...


class _Application: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActiveDocument(self) -> Document:
        """ Get: ActiveDocument(self: _Application) -> Document """
        ...

    @property
    def ActiveWindow(self) -> Window:
        """ Get: ActiveWindow(self: _Application) -> Window """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: _Application) -> Application """
        ...

    @property
    def Assistance(self): # -> IAssistance
        """ Get: Assistance(self: _Application) -> IAssistance """
        ...

    @property
    def Assistant(self): # -> Assistant
        """ Get: Assistant(self: _Application) -> Assistant """
        ...

    @property
    def AutomationSecurity(self): # -> MsoAutomationSecurity
        """
        Get: AutomationSecurity(self: _Application) -> MsoAutomationSecurity
        Set: AutomationSecurity(self: _Application) = value
        """
        ...

    @property
    def Build(self) -> int:
        """ Get: Build(self: _Application) -> int """
        ...

    @property
    def CaptionStyles(self) -> CaptionStyles:
        """ Get: CaptionStyles(self: _Application) -> CaptionStyles """
        ...

    @property
    def ColorSchemes(self) -> ColorSchemes:
        """ Get: ColorSchemes(self: _Application) -> ColorSchemes """
        ...

    @property
    def COMAddIns(self): # -> COMAddIns
        """ Get: COMAddIns(self: _Application) -> COMAddIns """
        ...

    @property
    def CommandBars(self) -> CommandBars:
        """ Get: CommandBars(self: _Application) -> CommandBars """
        ...

    @property
    def Documents(self) -> Documents:
        """ Get: Documents(self: _Application) -> Documents """
        ...

    @property
    def FileSearch(self): # -> FileSearch
        """ Get: FileSearch(self: _Application) -> FileSearch """
        ...

    @property
    def InsertBarcodeVisible(self) -> bool:
        """
        Get: InsertBarcodeVisible(self: _Application) -> bool
        Set: InsertBarcodeVisible(self: _Application) = value
        """
        ...

    @property
    def InstalledPrinters(self) -> InstalledPrinters:
        """ Get: InstalledPrinters(self: _Application) -> InstalledPrinters """
        ...

    @property
    def Language(self) -> int:
        """ Get: Language(self: _Application) -> int """
        ...

    @property
    def MsoDebugOptions(self): # -> MsoDebugOptions
        """ Get: MsoDebugOptions(self: _Application) -> MsoDebugOptions """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: _Application) -> str """
        ...

    @property
    def OfficeDataSourceObject(self): # -> OfficeDataSourceObject
        """ Get: OfficeDataSourceObject(self: _Application) -> OfficeDataSourceObject """
        ...

    @property
    def Options(self) -> Options:
        """ Get: Options(self: _Application) -> Options """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: _Application) -> object """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: _Application) -> str """
        ...

    @property
    def PathSeparator(self) -> str:
        """ Get: PathSeparator(self: _Application) -> str """
        ...

    @property
    def PrintPreview(self) -> bool:
        """
        Get: PrintPreview(self: _Application) -> bool
        Set: PrintPreview(self: _Application) = value
        """
        ...

    @property
    def ProductCode(self) -> str:
        """ Get: ProductCode(self: _Application) -> str """
        ...

    @property
    def ScreenUpdating(self) -> bool:
        """
        Get: ScreenUpdating(self: _Application) -> bool
        Set: ScreenUpdating(self: _Application) = value
        """
        ...

    @property
    def Selection(self) -> Selection:
        """ Get: Selection(self: _Application) -> Selection """
        ...

    @property
    def ShowFollowUpCustom(self) -> str:
        """
        Get: ShowFollowUpCustom(self: _Application) -> str
        Set: ShowFollowUpCustom(self: _Application) = value
        """
        ...

    @property
    def SnapToGuides(self) -> bool:
        """
        Get: SnapToGuides(self: _Application) -> bool
        Set: SnapToGuides(self: _Application) = value
        """
        ...

    @property
    def SnapToObjects(self) -> bool:
        """
        Get: SnapToObjects(self: _Application) -> bool
        Set: SnapToObjects(self: _Application) = value
        """
        ...

    @property
    def TemplateFolderPath(self) -> str:
        """ Get: TemplateFolderPath(self: _Application) -> str """
        ...

    @property
    def ValidateAddressVisible(self) -> bool:
        """
        Get: ValidateAddressVisible(self: _Application) -> bool
        Set: ValidateAddressVisible(self: _Application) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: _Application) -> str """
        ...

    @property
    def WebOptions(self) -> WebOptions:
        """ Get: WebOptions(self: _Application) -> WebOptions """
        ...

    @property
    def WizardCatalogVisible(self) -> bool:
        """
        Get: WizardCatalogVisible(self: _Application) -> bool
        Set: WizardCatalogVisible(self: _Application) = value
        """
        ...


    def CentimetersToPoints(self, Value:Single) -> Single:
        """ CentimetersToPoints(self: _Application, Value: Single) -> Single """
        ...

    def ChangeFileOpenDirectory(self, Dir:str): # -> 
        """ ChangeFileOpenDirectory(self: _Application, Dir: str) """
        ...

    def EmusToPoints(self, Value:Single) -> Single:
        """ EmusToPoints(self: _Application, Value: Single) -> Single """
        ...

    def Help(self, HelpType:PbHelpType): # -> 
        """ Help(self: _Application, HelpType: PbHelpType) """
        ...

    def InchesToPoints(self, Value:Single) -> Single:
        """ InchesToPoints(self: _Application, Value: Single) -> Single """
        ...

    def IsValidObject(self, Object:object) -> bool:
        """ IsValidObject(self: _Application, Object: object) -> bool """
        ...

    def LaunchWebService(self): # -> 
        """ LaunchWebService(self: _Application) """
        ...

    def LinesToPoints(self, Value:Single) -> Single:
        """ LinesToPoints(self: _Application, Value: Single) -> Single """
        ...

    def MillimetersToPoints(self, Value:Single) -> Single:
        """ MillimetersToPoints(self: _Application, Value: Single) -> Single """
        ...

    def NewDocument(self, Wizard:PbWizard, Design:int) -> Document:
        """ NewDocument(self: _Application, Wizard: PbWizard, Design: int) -> Document """
        ...

    def Open(self, Filename:str, ReadOnly:bool, AddToRecentFiles:bool, SaveChanges:PbSaveOptions) -> Document:
        """ Open(self: _Application, Filename: str, ReadOnly: bool, AddToRecentFiles: bool, SaveChanges: PbSaveOptions) -> Document """
        ...

    def PicasToPoints(self, Value:Single) -> Single:
        """ PicasToPoints(self: _Application, Value: Single) -> Single """
        ...

    def PixelsToPoints(self, Value:Single) -> Single:
        """ PixelsToPoints(self: _Application, Value: Single) -> Single """
        ...

    def PointsToCentimeters(self, Value:Single) -> Single:
        """ PointsToCentimeters(self: _Application, Value: Single) -> Single """
        ...

    def PointsToEmus(self, Value:Single) -> Single:
        """ PointsToEmus(self: _Application, Value: Single) -> Single """
        ...

    def PointsToInches(self, Value:Single) -> Single:
        """ PointsToInches(self: _Application, Value: Single) -> Single """
        ...

    def PointsToLines(self, Value:Single) -> Single:
        """ PointsToLines(self: _Application, Value: Single) -> Single """
        ...

    def PointsToMillimeters(self, Value:Single) -> Single:
        """ PointsToMillimeters(self: _Application, Value: Single) -> Single """
        ...

    def PointsToPicas(self, Value:Single) -> Single:
        """ PointsToPicas(self: _Application, Value: Single) -> Single """
        ...

    def PointsToPixels(self, Value:Single) -> Single:
        """ PointsToPixels(self: _Application, Value: Single) -> Single """
        ...

    def PointsToTwips(self, Value:Single) -> Single:
        """ PointsToTwips(self: _Application, Value: Single) -> Single """
        ...

    def Quit(self): # -> 
        """ Quit(self: _Application) """
        ...

    def ShowWizardCatalog(self, Wizard:PbWizard): # -> 
        """ ShowWizardCatalog(self: _Application, Wizard: PbWizard) """
        ...

    def TwipsToPoints(self, Value:Single) -> Single:
        """ TwipsToPoints(self: _Application, Value: Single) -> Single """
        ...


class Application(_Application, ApplicationEvents_Event): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ApplicationClass(Application, __ComObject): # skipped bases: <type '_Application'>, <type 'ApplicationEvents_Event'>, <type 'object'>
    """ ApplicationClass() """
    @property
    def ActiveDocument(self) -> Document:
        """ Get: ActiveDocument(self: ApplicationClass) -> Document """
        ...

    @property
    def ActiveWindow(self) -> Window:
        """ Get: ActiveWindow(self: ApplicationClass) -> Window """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: ApplicationClass) -> Application """
        ...

    @property
    def Assistance(self): # -> IAssistance
        """ Get: Assistance(self: ApplicationClass) -> IAssistance """
        ...

    @property
    def Assistant(self): # -> Assistant
        """ Get: Assistant(self: ApplicationClass) -> Assistant """
        ...

    @property
    def AutomationSecurity(self): # -> MsoAutomationSecurity
        """
        Get: AutomationSecurity(self: ApplicationClass) -> MsoAutomationSecurity
        Set: AutomationSecurity(self: ApplicationClass) = value
        """
        ...

    @property
    def Build(self) -> int:
        """ Get: Build(self: ApplicationClass) -> int """
        ...

    @property
    def CaptionStyles(self) -> CaptionStyles:
        """ Get: CaptionStyles(self: ApplicationClass) -> CaptionStyles """
        ...

    @property
    def ColorSchemes(self) -> ColorSchemes:
        """ Get: ColorSchemes(self: ApplicationClass) -> ColorSchemes """
        ...

    @property
    def COMAddIns(self): # -> COMAddIns
        """ Get: COMAddIns(self: ApplicationClass) -> COMAddIns """
        ...

    @property
    def CommandBars(self) -> CommandBars:
        """ Get: CommandBars(self: ApplicationClass) -> CommandBars """
        ...

    @property
    def Documents(self) -> Documents:
        """ Get: Documents(self: ApplicationClass) -> Documents """
        ...

    @property
    def FileSearch(self): # -> FileSearch
        """ Get: FileSearch(self: ApplicationClass) -> FileSearch """
        ...

    @property
    def InsertBarcodeVisible(self) -> bool:
        """
        Get: InsertBarcodeVisible(self: ApplicationClass) -> bool
        Set: InsertBarcodeVisible(self: ApplicationClass) = value
        """
        ...

    @property
    def InstalledPrinters(self) -> InstalledPrinters:
        """ Get: InstalledPrinters(self: ApplicationClass) -> InstalledPrinters """
        ...

    @property
    def Language(self) -> int:
        """ Get: Language(self: ApplicationClass) -> int """
        ...

    @property
    def MsoDebugOptions(self): # -> MsoDebugOptions
        """ Get: MsoDebugOptions(self: ApplicationClass) -> MsoDebugOptions """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ApplicationClass) -> str """
        ...

    @property
    def OfficeDataSourceObject(self): # -> OfficeDataSourceObject
        """ Get: OfficeDataSourceObject(self: ApplicationClass) -> OfficeDataSourceObject """
        ...

    @property
    def Options(self) -> Options:
        """ Get: Options(self: ApplicationClass) -> Options """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ApplicationClass) -> object """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: ApplicationClass) -> str """
        ...

    @property
    def PathSeparator(self) -> str:
        """ Get: PathSeparator(self: ApplicationClass) -> str """
        ...

    @property
    def PrintPreview(self) -> bool:
        """
        Get: PrintPreview(self: ApplicationClass) -> bool
        Set: PrintPreview(self: ApplicationClass) = value
        """
        ...

    @property
    def ProductCode(self) -> str:
        """ Get: ProductCode(self: ApplicationClass) -> str """
        ...

    @property
    def ScreenUpdating(self) -> bool:
        """
        Get: ScreenUpdating(self: ApplicationClass) -> bool
        Set: ScreenUpdating(self: ApplicationClass) = value
        """
        ...

    @property
    def Selection(self) -> Selection:
        """ Get: Selection(self: ApplicationClass) -> Selection """
        ...

    @property
    def ShowFollowUpCustom(self) -> str:
        """
        Get: ShowFollowUpCustom(self: ApplicationClass) -> str
        Set: ShowFollowUpCustom(self: ApplicationClass) = value
        """
        ...

    @property
    def SnapToGuides(self) -> bool:
        """
        Get: SnapToGuides(self: ApplicationClass) -> bool
        Set: SnapToGuides(self: ApplicationClass) = value
        """
        ...

    @property
    def SnapToObjects(self) -> bool:
        """
        Get: SnapToObjects(self: ApplicationClass) -> bool
        Set: SnapToObjects(self: ApplicationClass) = value
        """
        ...

    @property
    def TemplateFolderPath(self) -> str:
        """ Get: TemplateFolderPath(self: ApplicationClass) -> str """
        ...

    @property
    def ValidateAddressVisible(self) -> bool:
        """
        Get: ValidateAddressVisible(self: ApplicationClass) -> bool
        Set: ValidateAddressVisible(self: ApplicationClass) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: ApplicationClass) -> str """
        ...

    @property
    def WebOptions(self) -> WebOptions:
        """ Get: WebOptions(self: ApplicationClass) -> WebOptions """
        ...

    @property
    def WizardCatalogVisible(self) -> bool:
        """
        Get: WizardCatalogVisible(self: ApplicationClass) -> bool
        Set: WizardCatalogVisible(self: ApplicationClass) = value
        """
        ...


    def add_AfterPrint(self): # -> 
        """ add_AfterPrint(self: ApplicationClass, : ApplicationEvents_AfterPrintEventHandler) """
        ...

    def add_BeforePrint(self): # -> 
        """ add_BeforePrint(self: ApplicationClass, : ApplicationEvents_BeforePrintEventHandler) """
        ...

    def add_DocumentBeforeClose(self): # -> 
        """ add_DocumentBeforeClose(self: ApplicationClass, : ApplicationEvents_DocumentBeforeCloseEventHandler) """
        ...

    def add_DocumentOpen(self): # -> 
        """ add_DocumentOpen(self: ApplicationClass, : ApplicationEvents_DocumentOpenEventHandler) """
        ...

    def add_HideCatalogUI(self): # -> 
        """ add_HideCatalogUI(self: ApplicationClass, : ApplicationEvents_HideCatalogUIEventHandler) """
        ...

    def add_MailMergeAfterMerge(self): # -> 
        """ add_MailMergeAfterMerge(self: ApplicationClass, : ApplicationEvents_MailMergeAfterMergeEventHandler) """
        ...

    def add_MailMergeAfterRecordMerge(self): # -> 
        """ add_MailMergeAfterRecordMerge(self: ApplicationClass, : ApplicationEvents_MailMergeAfterRecordMergeEventHandler) """
        ...

    def add_MailMergeBeforeMerge(self): # -> 
        """ add_MailMergeBeforeMerge(self: ApplicationClass, : ApplicationEvents_MailMergeBeforeMergeEventHandler) """
        ...

    def add_MailMergeBeforeRecordMerge(self): # -> 
        """ add_MailMergeBeforeRecordMerge(self: ApplicationClass, : ApplicationEvents_MailMergeBeforeRecordMergeEventHandler) """
        ...

    def add_MailMergeDataSourceLoad(self): # -> 
        """ add_MailMergeDataSourceLoad(self: ApplicationClass, : ApplicationEvents_MailMergeDataSourceLoadEventHandler) """
        ...

    def add_MailMergeDataSourceValidate(self): # -> 
        """ add_MailMergeDataSourceValidate(self: ApplicationClass, : ApplicationEvents_MailMergeDataSourceValidateEventHandler) """
        ...

    def add_MailMergeGenerateBarcode(self): # -> 
        """ add_MailMergeGenerateBarcode(self: ApplicationClass, : ApplicationEvents_MailMergeGenerateBarcodeEventHandler) """
        ...

    def add_MailMergeInsertBarcode(self): # -> 
        """ add_MailMergeInsertBarcode(self: ApplicationClass, : ApplicationEvents_MailMergeInsertBarcodeEventHandler) """
        ...

    def add_MailMergeRecipientListClose(self): # -> 
        """ add_MailMergeRecipientListClose(self: ApplicationClass, : ApplicationEvents_MailMergeRecipientListCloseEventHandler) """
        ...

    def add_MailMergeWizardFollowUpCustom(self): # -> 
        """ add_MailMergeWizardFollowUpCustom(self: ApplicationClass, : ApplicationEvents_MailMergeWizardFollowUpCustomEventHandler) """
        ...

    def add_MailMergeWizardSendToCustom(self): # -> 
        """ add_MailMergeWizardSendToCustom(self: ApplicationClass, : ApplicationEvents_MailMergeWizardSendToCustomEventHandler) """
        ...

    def add_MailMergeWizardStateChange(self): # -> 
        """ add_MailMergeWizardStateChange(self: ApplicationClass, : ApplicationEvents_MailMergeWizardStateChangeEventHandler) """
        ...

    def add_NewDocument(self): # -> 
        """ add_NewDocument(self: ApplicationClass, : ApplicationEvents_NewDocumentEventHandler) """
        ...

    def add_Quit(self): # -> 
        """ add_Quit(self: ApplicationClass, : ApplicationEvents_QuitEventHandler) """
        ...

    def add_ShowCatalogUI(self): # -> 
        """ add_ShowCatalogUI(self: ApplicationClass, : ApplicationEvents_ShowCatalogUIEventHandler) """
        ...

    def add_WindowActivate(self): # -> 
        """ add_WindowActivate(self: ApplicationClass, : ApplicationEvents_WindowActivateEventHandler) """
        ...

    def add_WindowDeactivate(self): # -> 
        """ add_WindowDeactivate(self: ApplicationClass, : ApplicationEvents_WindowDeactivateEventHandler) """
        ...

    def add_WindowPageChange(self): # -> 
        """ add_WindowPageChange(self: ApplicationClass, : ApplicationEvents_WindowPageChangeEventHandler) """
        ...

    def CentimetersToPoints(self, Value:Single) -> Single:
        """ CentimetersToPoints(self: ApplicationClass, Value: Single) -> Single """
        ...

    def ChangeFileOpenDirectory(self, Dir:str): # -> 
        """ ChangeFileOpenDirectory(self: ApplicationClass, Dir: str) """
        ...

    def EmusToPoints(self, Value:Single) -> Single:
        """ EmusToPoints(self: ApplicationClass, Value: Single) -> Single """
        ...

    def Help(self, HelpType:PbHelpType): # -> 
        """ Help(self: ApplicationClass, HelpType: PbHelpType) """
        ...

    def InchesToPoints(self, Value:Single) -> Single:
        """ InchesToPoints(self: ApplicationClass, Value: Single) -> Single """
        ...

    def IsValidObject(self, Object:object) -> bool:
        """ IsValidObject(self: ApplicationClass, Object: object) -> bool """
        ...

    def LaunchWebService(self): # -> 
        """ LaunchWebService(self: ApplicationClass) """
        ...

    def LinesToPoints(self, Value:Single) -> Single:
        """ LinesToPoints(self: ApplicationClass, Value: Single) -> Single """
        ...

    def MillimetersToPoints(self, Value:Single) -> Single:
        """ MillimetersToPoints(self: ApplicationClass, Value: Single) -> Single """
        ...

    def NewDocument(self, Wizard:PbWizard, Design:int) -> Document:
        """ NewDocument(self: ApplicationClass, Wizard: PbWizard, Design: int) -> Document """
        ...

    def Open(self, Filename:str, ReadOnly:bool, AddToRecentFiles:bool, SaveChanges:PbSaveOptions) -> Document:
        """ Open(self: ApplicationClass, Filename: str, ReadOnly: bool, AddToRecentFiles: bool, SaveChanges: PbSaveOptions) -> Document """
        ...

    def PicasToPoints(self, Value:Single) -> Single:
        """ PicasToPoints(self: ApplicationClass, Value: Single) -> Single """
        ...

    def PixelsToPoints(self, Value:Single) -> Single:
        """ PixelsToPoints(self: ApplicationClass, Value: Single) -> Single """
        ...

    def PointsToCentimeters(self, Value:Single) -> Single:
        """ PointsToCentimeters(self: ApplicationClass, Value: Single) -> Single """
        ...

    def PointsToEmus(self, Value:Single) -> Single:
        """ PointsToEmus(self: ApplicationClass, Value: Single) -> Single """
        ...

    def PointsToInches(self, Value:Single) -> Single:
        """ PointsToInches(self: ApplicationClass, Value: Single) -> Single """
        ...

    def PointsToLines(self, Value:Single) -> Single:
        """ PointsToLines(self: ApplicationClass, Value: Single) -> Single """
        ...

    def PointsToMillimeters(self, Value:Single) -> Single:
        """ PointsToMillimeters(self: ApplicationClass, Value: Single) -> Single """
        ...

    def PointsToPicas(self, Value:Single) -> Single:
        """ PointsToPicas(self: ApplicationClass, Value: Single) -> Single """
        ...

    def PointsToPixels(self, Value:Single) -> Single:
        """ PointsToPixels(self: ApplicationClass, Value: Single) -> Single """
        ...

    def PointsToTwips(self, Value:Single) -> Single:
        """ PointsToTwips(self: ApplicationClass, Value: Single) -> Single """
        ...

    def Quit(self): # -> 
        """ Quit(self: ApplicationClass) """
        ...

    def remove_AfterPrint(self): # -> 
        """ remove_AfterPrint(self: ApplicationClass, : ApplicationEvents_AfterPrintEventHandler) """
        ...

    def remove_BeforePrint(self): # -> 
        """ remove_BeforePrint(self: ApplicationClass, : ApplicationEvents_BeforePrintEventHandler) """
        ...

    def remove_DocumentBeforeClose(self): # -> 
        """ remove_DocumentBeforeClose(self: ApplicationClass, : ApplicationEvents_DocumentBeforeCloseEventHandler) """
        ...

    def remove_DocumentOpen(self): # -> 
        """ remove_DocumentOpen(self: ApplicationClass, : ApplicationEvents_DocumentOpenEventHandler) """
        ...

    def remove_HideCatalogUI(self): # -> 
        """ remove_HideCatalogUI(self: ApplicationClass, : ApplicationEvents_HideCatalogUIEventHandler) """
        ...

    def remove_MailMergeAfterMerge(self): # -> 
        """ remove_MailMergeAfterMerge(self: ApplicationClass, : ApplicationEvents_MailMergeAfterMergeEventHandler) """
        ...

    def remove_MailMergeAfterRecordMerge(self): # -> 
        """ remove_MailMergeAfterRecordMerge(self: ApplicationClass, : ApplicationEvents_MailMergeAfterRecordMergeEventHandler) """
        ...

    def remove_MailMergeBeforeMerge(self): # -> 
        """ remove_MailMergeBeforeMerge(self: ApplicationClass, : ApplicationEvents_MailMergeBeforeMergeEventHandler) """
        ...

    def remove_MailMergeBeforeRecordMerge(self): # -> 
        """ remove_MailMergeBeforeRecordMerge(self: ApplicationClass, : ApplicationEvents_MailMergeBeforeRecordMergeEventHandler) """
        ...

    def remove_MailMergeDataSourceLoad(self): # -> 
        """ remove_MailMergeDataSourceLoad(self: ApplicationClass, : ApplicationEvents_MailMergeDataSourceLoadEventHandler) """
        ...

    def remove_MailMergeDataSourceValidate(self): # -> 
        """ remove_MailMergeDataSourceValidate(self: ApplicationClass, : ApplicationEvents_MailMergeDataSourceValidateEventHandler) """
        ...

    def remove_MailMergeGenerateBarcode(self): # -> 
        """ remove_MailMergeGenerateBarcode(self: ApplicationClass, : ApplicationEvents_MailMergeGenerateBarcodeEventHandler) """
        ...

    def remove_MailMergeInsertBarcode(self): # -> 
        """ remove_MailMergeInsertBarcode(self: ApplicationClass, : ApplicationEvents_MailMergeInsertBarcodeEventHandler) """
        ...

    def remove_MailMergeRecipientListClose(self): # -> 
        """ remove_MailMergeRecipientListClose(self: ApplicationClass, : ApplicationEvents_MailMergeRecipientListCloseEventHandler) """
        ...

    def remove_MailMergeWizardFollowUpCustom(self): # -> 
        """ remove_MailMergeWizardFollowUpCustom(self: ApplicationClass, : ApplicationEvents_MailMergeWizardFollowUpCustomEventHandler) """
        ...

    def remove_MailMergeWizardSendToCustom(self): # -> 
        """ remove_MailMergeWizardSendToCustom(self: ApplicationClass, : ApplicationEvents_MailMergeWizardSendToCustomEventHandler) """
        ...

    def remove_MailMergeWizardStateChange(self): # -> 
        """ remove_MailMergeWizardStateChange(self: ApplicationClass, : ApplicationEvents_MailMergeWizardStateChangeEventHandler) """
        ...

    def remove_NewDocument(self): # -> 
        """ remove_NewDocument(self: ApplicationClass, : ApplicationEvents_NewDocumentEventHandler) """
        ...

    def remove_Quit(self): # -> 
        """ remove_Quit(self: ApplicationClass, : ApplicationEvents_QuitEventHandler) """
        ...

    def remove_ShowCatalogUI(self): # -> 
        """ remove_ShowCatalogUI(self: ApplicationClass, : ApplicationEvents_ShowCatalogUIEventHandler) """
        ...

    def remove_WindowActivate(self): # -> 
        """ remove_WindowActivate(self: ApplicationClass, : ApplicationEvents_WindowActivateEventHandler) """
        ...

    def remove_WindowDeactivate(self): # -> 
        """ remove_WindowDeactivate(self: ApplicationClass, : ApplicationEvents_WindowDeactivateEventHandler) """
        ...

    def remove_WindowPageChange(self): # -> 
        """ remove_WindowPageChange(self: ApplicationClass, : ApplicationEvents_WindowPageChangeEventHandler) """
        ...

    def ShowWizardCatalog(self, Wizard:PbWizard): # -> 
        """ ShowWizardCatalog(self: ApplicationClass, Wizard: PbWizard) """
        ...

    def TwipsToPoints(self, Value:Single) -> Single:
        """ TwipsToPoints(self: ApplicationClass, Value: Single) -> Single """
        ...

    AfterPrint = ...
    ApplicationEvents_Event_NewDocument = ...
    ApplicationEvents_Event_Quit = ...
    BeforePrint = ...
    DocumentBeforeClose = ...
    DocumentOpen = ...
    HideCatalogUI = ...
    MailMergeAfterMerge = ...
    MailMergeAfterRecordMerge = ...
    MailMergeBeforeMerge = ...
    MailMergeBeforeRecordMerge = ...
    MailMergeDataSourceLoad = ...
    MailMergeDataSourceValidate = ...
    MailMergeGenerateBarcode = ...
    MailMergeInsertBarcode = ...
    MailMergeRecipientListClose = ...
    MailMergeWizardFollowUpCustom = ...
    MailMergeWizardSendToCustom = ...
    MailMergeWizardStateChange = ...
    ShowCatalogUI = ...
    WindowActivate = ...
    WindowDeactivate = ...
    WindowPageChange = ...


class ApplicationEvents: # skipped bases: <type 'object'>
    """ no doc """
    def AfterPrint(self, Doc:Document): # -> 
        """ AfterPrint(self: ApplicationEvents, Doc: Document) """
        ...

    def BeforePrint(self, Doc, Cancel) -> bool:
        """ BeforePrint(self: ApplicationEvents, Doc: Document) -> bool """
        ...

    def DocumentBeforeClose(self, Doc, Cancel) -> bool:
        """ DocumentBeforeClose(self: ApplicationEvents, Doc: Document) -> bool """
        ...

    def DocumentOpen(self, Doc:Document): # -> 
        """ DocumentOpen(self: ApplicationEvents, Doc: Document) """
        ...

    def HideCatalogUI(self): # -> 
        """ HideCatalogUI(self: ApplicationEvents) """
        ...

    def MailMergeAfterMerge(self, Doc:Document): # -> 
        """ MailMergeAfterMerge(self: ApplicationEvents, Doc: Document) """
        ...

    def MailMergeAfterRecordMerge(self, Doc:Document): # -> 
        """ MailMergeAfterRecordMerge(self: ApplicationEvents, Doc: Document) """
        ...

    def MailMergeBeforeMerge(self, Doc, StartRecord, EndRecord, Cancel) -> bool:
        """ MailMergeBeforeMerge(self: ApplicationEvents, Doc: Document, StartRecord: int, EndRecord: int) -> bool """
        ...

    def MailMergeBeforeRecordMerge(self, Doc, Cancel) -> bool:
        """ MailMergeBeforeRecordMerge(self: ApplicationEvents, Doc: Document) -> bool """
        ...

    def MailMergeDataSourceLoad(self, Doc:Document): # -> 
        """ MailMergeDataSourceLoad(self: ApplicationEvents, Doc: Document) """
        ...

    def MailMergeDataSourceValidate(self, Doc, Handled) -> bool:
        """ MailMergeDataSourceValidate(self: ApplicationEvents, Doc: Document) -> bool """
        ...

    def MailMergeGenerateBarcode(self, Doc, bstrString) -> str:
        """ MailMergeGenerateBarcode(self: ApplicationEvents, Doc: Document) -> str """
        ...

    def MailMergeInsertBarcode(self, Doc, OkToInsert) -> bool:
        """ MailMergeInsertBarcode(self: ApplicationEvents, Doc: Document) -> bool """
        ...

    def MailMergeRecipientListClose(self, Doc:Document): # -> 
        """ MailMergeRecipientListClose(self: ApplicationEvents, Doc: Document) """
        ...

    def MailMergeWizardFollowUpCustom(self, Doc:Document): # -> 
        """ MailMergeWizardFollowUpCustom(self: ApplicationEvents, Doc: Document) """
        ...

    def MailMergeWizardSendToCustom(self, Doc:Document): # -> 
        """ MailMergeWizardSendToCustom(self: ApplicationEvents, Doc: Document) """
        ...

    def MailMergeWizardStateChange(self, Doc:Document, FromState:int): # -> 
        """ MailMergeWizardStateChange(self: ApplicationEvents, Doc: Document, FromState: int) """
        ...

    def NewDocument(self, Doc:Document): # -> 
        """ NewDocument(self: ApplicationEvents, Doc: Document) """
        ...

    def Quit(self): # -> 
        """ Quit(self: ApplicationEvents) """
        ...

    def ShowCatalogUI(self): # -> 
        """ ShowCatalogUI(self: ApplicationEvents) """
        ...

    def WindowActivate(self, Wn:Window): # -> 
        """ WindowActivate(self: ApplicationEvents, Wn: Window) """
        ...

    def WindowDeactivate(self, Wn:Window): # -> 
        """ WindowDeactivate(self: ApplicationEvents, Wn: Window) """
        ...

    def WindowPageChange(self, Vw:View): # -> 
        """ WindowPageChange(self: ApplicationEvents, Vw: View) """
        ...


class ApplicationEvents_AfterPrintEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_AfterPrintEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc:Document): # -> 
        """ Invoke(self: ApplicationEvents_AfterPrintEventHandler, Doc: Document) """
        ...


class ApplicationEvents_BeforePrintEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_BeforePrintEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc, Cancel) -> bool:
        """ Invoke(self: ApplicationEvents_BeforePrintEventHandler, Doc: Document) -> bool """
        ...


class ApplicationEvents_DocumentBeforeCloseEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_DocumentBeforeCloseEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc, Cancel) -> bool:
        """ Invoke(self: ApplicationEvents_DocumentBeforeCloseEventHandler, Doc: Document) -> bool """
        ...


class ApplicationEvents_DocumentOpenEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_DocumentOpenEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc:Document): # -> 
        """ Invoke(self: ApplicationEvents_DocumentOpenEventHandler, Doc: Document) """
        ...


class ApplicationEvents_HideCatalogUIEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_HideCatalogUIEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: ApplicationEvents_HideCatalogUIEventHandler) """
        ...


class ApplicationEvents_MailMergeAfterMergeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_MailMergeAfterMergeEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc:Document): # -> 
        """ Invoke(self: ApplicationEvents_MailMergeAfterMergeEventHandler, Doc: Document) """
        ...


class ApplicationEvents_MailMergeAfterRecordMergeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_MailMergeAfterRecordMergeEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc:Document): # -> 
        """ Invoke(self: ApplicationEvents_MailMergeAfterRecordMergeEventHandler, Doc: Document) """
        ...


class ApplicationEvents_MailMergeBeforeMergeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_MailMergeBeforeMergeEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc, StartRecord, EndRecord, Cancel) -> bool:
        """ Invoke(self: ApplicationEvents_MailMergeBeforeMergeEventHandler, Doc: Document, StartRecord: int, EndRecord: int) -> bool """
        ...


class ApplicationEvents_MailMergeBeforeRecordMergeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_MailMergeBeforeRecordMergeEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc, Cancel) -> bool:
        """ Invoke(self: ApplicationEvents_MailMergeBeforeRecordMergeEventHandler, Doc: Document) -> bool """
        ...


class ApplicationEvents_MailMergeDataSourceLoadEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_MailMergeDataSourceLoadEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc:Document): # -> 
        """ Invoke(self: ApplicationEvents_MailMergeDataSourceLoadEventHandler, Doc: Document) """
        ...


class ApplicationEvents_MailMergeDataSourceValidateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_MailMergeDataSourceValidateEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc, Handled) -> bool:
        """ Invoke(self: ApplicationEvents_MailMergeDataSourceValidateEventHandler, Doc: Document) -> bool """
        ...


class ApplicationEvents_MailMergeGenerateBarcodeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_MailMergeGenerateBarcodeEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc, bstrString) -> str:
        """ Invoke(self: ApplicationEvents_MailMergeGenerateBarcodeEventHandler, Doc: Document) -> str """
        ...


class ApplicationEvents_MailMergeInsertBarcodeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_MailMergeInsertBarcodeEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc, OkToInsert) -> bool:
        """ Invoke(self: ApplicationEvents_MailMergeInsertBarcodeEventHandler, Doc: Document) -> bool """
        ...


class ApplicationEvents_MailMergeRecipientListCloseEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_MailMergeRecipientListCloseEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc:Document): # -> 
        """ Invoke(self: ApplicationEvents_MailMergeRecipientListCloseEventHandler, Doc: Document) """
        ...


class ApplicationEvents_MailMergeWizardFollowUpCustomEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_MailMergeWizardFollowUpCustomEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc:Document): # -> 
        """ Invoke(self: ApplicationEvents_MailMergeWizardFollowUpCustomEventHandler, Doc: Document) """
        ...


class ApplicationEvents_MailMergeWizardSendToCustomEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_MailMergeWizardSendToCustomEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc:Document): # -> 
        """ Invoke(self: ApplicationEvents_MailMergeWizardSendToCustomEventHandler, Doc: Document) """
        ...


class ApplicationEvents_MailMergeWizardStateChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_MailMergeWizardStateChangeEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc:Document, FromState:int): # -> 
        """ Invoke(self: ApplicationEvents_MailMergeWizardStateChangeEventHandler, Doc: Document, FromState: int) """
        ...


class ApplicationEvents_NewDocumentEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_NewDocumentEventHandler(: object, : UIntPtr) """
    def Invoke(self, Doc:Document): # -> 
        """ Invoke(self: ApplicationEvents_NewDocumentEventHandler, Doc: Document) """
        ...


class ApplicationEvents_QuitEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_QuitEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: ApplicationEvents_QuitEventHandler) """
        ...


class ApplicationEvents_ShowCatalogUIEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_ShowCatalogUIEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: ApplicationEvents_ShowCatalogUIEventHandler) """
        ...


class ApplicationEvents_SinkHelper(ApplicationEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_AfterPrintDelegate = ...
    m_BeforePrintDelegate = ...
    m_DocumentBeforeCloseDelegate = ...
    m_DocumentOpenDelegate = ...
    m_dwCookie = ...
    m_HideCatalogUIDelegate = ...
    m_MailMergeAfterMergeDelegate = ...
    m_MailMergeAfterRecordMergeDelegate = ...
    m_MailMergeBeforeMergeDelegate = ...
    m_MailMergeBeforeRecordMergeDelegate = ...
    m_MailMergeDataSourceLoadDelegate = ...
    m_MailMergeDataSourceValidateDelegate = ...
    m_MailMergeGenerateBarcodeDelegate = ...
    m_MailMergeInsertBarcodeDelegate = ...
    m_MailMergeRecipientListCloseDelegate = ...
    m_MailMergeWizardFollowUpCustomDelegate = ...
    m_MailMergeWizardSendToCustomDelegate = ...
    m_MailMergeWizardStateChangeDelegate = ...
    m_NewDocumentDelegate = ...
    m_QuitDelegate = ...
    m_ShowCatalogUIDelegate = ...
    m_WindowActivateDelegate = ...
    m_WindowDeactivateDelegate = ...
    m_WindowPageChangeDelegate = ...


class ApplicationEvents_WindowActivateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_WindowActivateEventHandler(: object, : UIntPtr) """
    def Invoke(self, Wn:Window): # -> 
        """ Invoke(self: ApplicationEvents_WindowActivateEventHandler, Wn: Window) """
        ...


class ApplicationEvents_WindowDeactivateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_WindowDeactivateEventHandler(: object, : UIntPtr) """
    def Invoke(self, Wn:Window): # -> 
        """ Invoke(self: ApplicationEvents_WindowDeactivateEventHandler, Wn: Window) """
        ...


class ApplicationEvents_WindowPageChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ApplicationEvents_WindowPageChangeEventHandler(: object, : UIntPtr) """
    def Invoke(self, Vw:View): # -> 
        """ Invoke(self: ApplicationEvents_WindowPageChangeEventHandler, Vw: View) """
        ...


class Attachment: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: Attachment) -> str """
        ...


    def Delete(self): # -> 
        """ Delete(self: Attachment) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Attachments(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Attachments) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Attachments) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Attachments) -> object """
        ...


    def Add(self, Filename:str) -> Attachment:
        """ Add(self: Attachments, Filename: str) -> Attachment """
        ...

    def ClearAll(self): # -> 
        """ ClearAll(self: Attachments) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class BorderArt: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: BorderArt) -> Application """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: BorderArt) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: BorderArt) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class BorderArtFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: BorderArtFormat) -> Application """
        ...

    @property
    def Color(self) -> ColorFormat:
        """
        Get: Color(self: BorderArtFormat) -> ColorFormat
        Set: Color(self: BorderArtFormat) = value
        """
        ...

    @property
    def Exists(self) -> bool:
        """ Get: Exists(self: BorderArtFormat) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: BorderArtFormat) -> str
        Set: Name(self: BorderArtFormat) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: BorderArtFormat) -> object """
        ...

    @property
    def StretchPictures(self) -> bool:
        """
        Get: StretchPictures(self: BorderArtFormat) -> bool
        Set: StretchPictures(self: BorderArtFormat) = value
        """
        ...

    @property
    def Weight(self) -> object:
        """
        Get: Weight(self: BorderArtFormat) -> object
        Set: Weight(self: BorderArtFormat) = value
        """
        ...


    def Delete(self): # -> 
        """ Delete(self: BorderArtFormat) """
        ...

    def RevertToDefaultWeight(self): # -> 
        """ RevertToDefaultWeight(self: BorderArtFormat) """
        ...

    def RevertToOriginalColor(self): # -> 
        """ RevertToOriginalColor(self: BorderArtFormat) """
        ...

    def Set(self, BorderArtName:object): # -> 
        """ Set(self: BorderArtFormat, BorderArtName: object) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class BorderArts(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: BorderArts) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: BorderArts) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: BorderArts) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class BuildingBlock: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Category(self) -> str:
        """
        Get: Category(self: BuildingBlock) -> str
        Set: Category(self: BuildingBlock) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: BuildingBlock) -> str
        Set: Description(self: BuildingBlock) = value
        """
        ...

    @property
    def Gallery(self) -> PbBuildingBlockGallery:
        """
        Get: Gallery(self: BuildingBlock) -> PbBuildingBlockGallery
        Set: Gallery(self: BuildingBlock) = value
        """
        ...

    @property
    def Keywords(self) -> str:
        """
        Get: Keywords(self: BuildingBlock) -> str
        Set: Keywords(self: BuildingBlock) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: BuildingBlock) -> str
        Set: Name(self: BuildingBlock) = value
        """
        ...

    @property
    def ShowInGallery(self) -> bool:
        """
        Get: ShowInGallery(self: BuildingBlock) -> bool
        Set: ShowInGallery(self: BuildingBlock) = value
        """
        ...

    @property
    def Type(self) -> PbBuildingBlockType:
        """ Get: Type(self: BuildingBlock) -> PbBuildingBlockType """
        ...


    def Delete(self): # -> 
        """ Delete(self: BuildingBlock) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class BuildingBlocks(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: BuildingBlocks) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: BuildingBlocks) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: BuildingBlocks) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class CalloutFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Accent(self): # -> MsoTriState
        """
        Get: Accent(self: CalloutFormat) -> MsoTriState
        Set: Accent(self: CalloutFormat) = value
        """
        ...

    @property
    def Angle(self): # -> MsoCalloutAngleType
        """
        Get: Angle(self: CalloutFormat) -> MsoCalloutAngleType
        Set: Angle(self: CalloutFormat) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: CalloutFormat) -> Application """
        ...

    @property
    def AutoAttach(self): # -> MsoTriState
        """
        Get: AutoAttach(self: CalloutFormat) -> MsoTriState
        Set: AutoAttach(self: CalloutFormat) = value
        """
        ...

    @property
    def AutoLength(self): # -> MsoTriState
        """ Get: AutoLength(self: CalloutFormat) -> MsoTriState """
        ...

    @property
    def Border(self): # -> MsoTriState
        """
        Get: Border(self: CalloutFormat) -> MsoTriState
        Set: Border(self: CalloutFormat) = value
        """
        ...

    @property
    def Drop(self) -> object:
        """ Get: Drop(self: CalloutFormat) -> object """
        ...

    @property
    def DropType(self): # -> MsoCalloutDropType
        """ Get: DropType(self: CalloutFormat) -> MsoCalloutDropType """
        ...

    @property
    def Gap(self) -> object:
        """
        Get: Gap(self: CalloutFormat) -> object
        Set: Gap(self: CalloutFormat) = value
        """
        ...

    @property
    def Length(self) -> object:
        """ Get: Length(self: CalloutFormat) -> object """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: CalloutFormat) -> object """
        ...

    @property
    def Type(self): # -> MsoCalloutType
        """
        Get: Type(self: CalloutFormat) -> MsoCalloutType
        Set: Type(self: CalloutFormat) = value
        """
        ...


    def AutomaticLength(self): # -> 
        """ AutomaticLength(self: CalloutFormat) """
        ...

    def CustomDrop(self, Drop:object): # -> 
        """ CustomDrop(self: CalloutFormat, Drop: object) """
        ...

    def CustomLength(self, Length:object): # -> 
        """ CustomLength(self: CalloutFormat, Length: object) """
        ...

    def PresetDrop(self, DropType): # ->  # Not found arg types: {'DropType': 'MsoCalloutDropType'}
        """ PresetDrop(self: CalloutFormat, DropType: MsoCalloutDropType) """
        ...


class CaptionStyle: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: CaptionStyle) -> Application """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: CaptionStyle) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: CaptionStyle) -> object """
        ...



class CaptionStyles(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: CaptionStyles) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: CaptionStyles) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: CaptionStyles) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class CatalogMergeShapes(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: CatalogMergeShapes) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: CatalogMergeShapes) -> int """
        ...

    @property
    def HorizontalRepeat(self) -> int:
        """ Get: HorizontalRepeat(self: CatalogMergeShapes) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: CatalogMergeShapes) -> object """
        ...

    @property
    def VerticalRepeat(self) -> int:
        """ Get: VerticalRepeat(self: CatalogMergeShapes) -> int """
        ...


    def Range(self, Index:object) -> ShapeRange:
        """ Range(self: CatalogMergeShapes, Index: object) -> ShapeRange """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Cell: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Cell) -> Application """
        ...

    @property
    def BorderBottom(self) -> CellBorder:
        """ Get: BorderBottom(self: Cell) -> CellBorder """
        ...

    @property
    def BorderDiagonal(self) -> CellBorder:
        """ Get: BorderDiagonal(self: Cell) -> CellBorder """
        ...

    @property
    def BorderLeft(self) -> CellBorder:
        """ Get: BorderLeft(self: Cell) -> CellBorder """
        ...

    @property
    def BorderRight(self) -> CellBorder:
        """ Get: BorderRight(self: Cell) -> CellBorder """
        ...

    @property
    def BorderTop(self) -> CellBorder:
        """ Get: BorderTop(self: Cell) -> CellBorder """
        ...

    @property
    def CellTextOrientation(self) -> PbTextOrientation:
        """
        Get: CellTextOrientation(self: Cell) -> PbTextOrientation
        Set: CellTextOrientation(self: Cell) = value
        """
        ...

    @property
    def Column(self) -> int:
        """ Get: Column(self: Cell) -> int """
        ...

    @property
    def Diagonal(self) -> PbCellDiagonalType:
        """
        Get: Diagonal(self: Cell) -> PbCellDiagonalType
        Set: Diagonal(self: Cell) = value
        """
        ...

    @property
    def Fill(self) -> FillFormat:
        """ Get: Fill(self: Cell) -> FillFormat """
        ...

    @property
    def HasText(self) -> bool:
        """ Get: HasText(self: Cell) -> bool """
        ...

    @property
    def Height(self) -> int:
        """ Get: Height(self: Cell) -> int """
        ...

    @property
    def MarginBottom(self) -> object:
        """
        Get: MarginBottom(self: Cell) -> object
        Set: MarginBottom(self: Cell) = value
        """
        ...

    @property
    def MarginLeft(self) -> object:
        """
        Get: MarginLeft(self: Cell) -> object
        Set: MarginLeft(self: Cell) = value
        """
        ...

    @property
    def MarginRight(self) -> object:
        """
        Get: MarginRight(self: Cell) -> object
        Set: MarginRight(self: Cell) = value
        """
        ...

    @property
    def MarginTop(self) -> object:
        """
        Get: MarginTop(self: Cell) -> object
        Set: MarginTop(self: Cell) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Cell) -> object """
        ...

    @property
    def Row(self) -> int:
        """ Get: Row(self: Cell) -> int """
        ...

    @property
    def Selected(self) -> bool:
        """ Get: Selected(self: Cell) -> bool """
        ...

    @property
    def TextRange(self) -> TextRange:
        """ Get: TextRange(self: Cell) -> TextRange """
        ...

    @property
    def VerticalTextAlignment(self) -> PbVerticalTextAlignmentType:
        """
        Get: VerticalTextAlignment(self: Cell) -> PbVerticalTextAlignmentType
        Set: VerticalTextAlignment(self: Cell) = value
        """
        ...

    @property
    def Width(self) -> int:
        """ Get: Width(self: Cell) -> int """
        ...


    def Merge(self, MergeTo:Cell): # -> 
        """ Merge(self: Cell, MergeTo: Cell) """
        ...

    def Select(self): # -> 
        """ Select(self: Cell) """
        ...

    def Split(self) -> CellRange:
        """ Split(self: Cell) -> CellRange """
        ...


class CellBorder: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: CellBorder) -> Application """
        ...

    @property
    def Color(self) -> ColorFormat:
        """ Get: Color(self: CellBorder) -> ColorFormat """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: CellBorder) -> object """
        ...

    @property
    def Weight(self) -> object:
        """
        Get: Weight(self: CellBorder) -> object
        Set: Weight(self: CellBorder) = value
        """
        ...



class CellRange(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: CellRange) -> Application """
        ...

    @property
    def Column(self) -> int:
        """ Get: Column(self: CellRange) -> int """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: CellRange) -> int """
        ...

    @property
    def Height(self) -> int:
        """ Get: Height(self: CellRange) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: CellRange) -> object """
        ...

    @property
    def Row(self) -> int:
        """ Get: Row(self: CellRange) -> int """
        ...

    @property
    def Width(self) -> int:
        """ Get: Width(self: CellRange) -> int """
        ...


    def Merge(self): # -> 
        """ Merge(self: CellRange) """
        ...

    def Select(self): # -> 
        """ Select(self: CellRange) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ColorCMYK: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ColorCMYK) -> Application """
        ...

    @property
    def Black(self) -> int:
        """
        Get: Black(self: ColorCMYK) -> int
        Set: Black(self: ColorCMYK) = value
        """
        ...

    @property
    def Cyan(self) -> int:
        """
        Get: Cyan(self: ColorCMYK) -> int
        Set: Cyan(self: ColorCMYK) = value
        """
        ...

    @property
    def Magenta(self) -> int:
        """
        Get: Magenta(self: ColorCMYK) -> int
        Set: Magenta(self: ColorCMYK) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ColorCMYK) -> object """
        ...

    @property
    def Yellow(self) -> int:
        """
        Get: Yellow(self: ColorCMYK) -> int
        Set: Yellow(self: ColorCMYK) = value
        """
        ...


    def SetCMYK(self, Cyan:int, Magenta:int, Yellow:int, Black:int): # -> 
        """ SetCMYK(self: ColorCMYK, Cyan: int, Magenta: int, Yellow: int, Black: int) """
        ...


class ColorFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ColorFormat) -> Application """
        ...

    @property
    def BaseCMYK(self) -> ColorCMYK:
        """ Get: BaseCMYK(self: ColorFormat) -> ColorCMYK """
        ...

    @property
    def BaseRGB(self) -> int:
        """
        Get: BaseRGB(self: ColorFormat) -> int
        Set: BaseRGB(self: ColorFormat) = value
        """
        ...

    @property
    def CMYK(self) -> ColorCMYK:
        """ Get: CMYK(self: ColorFormat) -> ColorCMYK """
        ...

    @property
    def Ink(self) -> int:
        """
        Get: Ink(self: ColorFormat) -> int
        Set: Ink(self: ColorFormat) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ColorFormat) -> object """
        ...

    @property
    def RGB(self) -> int:
        """
        Get: RGB(self: ColorFormat) -> int
        Set: RGB(self: ColorFormat) = value
        """
        ...

    @property
    def SchemeColor(self) -> PbSchemeColorIndex:
        """
        Get: SchemeColor(self: ColorFormat) -> PbSchemeColorIndex
        Set: SchemeColor(self: ColorFormat) = value
        """
        ...

    @property
    def TintAndShade(self) -> Single:
        """
        Get: TintAndShade(self: ColorFormat) -> Single
        Set: TintAndShade(self: ColorFormat) = value
        """
        ...

    @property
    def Transparency(self) -> Single:
        """
        Get: Transparency(self: ColorFormat) -> Single
        Set: Transparency(self: ColorFormat) = value
        """
        ...

    @property
    def Type(self) -> PbColorType:
        """ Get: Type(self: ColorFormat) -> PbColorType """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ColorScheme: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ColorScheme) -> Application """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ColorScheme) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ColorScheme) -> object """
        ...



class ColorSchemes(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ColorSchemes) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ColorSchemes) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ColorSchemes) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ColorsInUse(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ColorsInUse) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ColorsInUse) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ColorsInUse) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Column: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Column) -> Application """
        ...

    @property
    def Cells(self) -> CellRange:
        """ Get: Cells(self: Column) -> CellRange """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Column) -> object """
        ...

    @property
    def Width(self) -> object:
        """
        Get: Width(self: Column) -> object
        Set: Width(self: Column) = value
        """
        ...


    def Delete(self): # -> 
        """ Delete(self: Column) """
        ...


class Columns(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Columns) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Columns) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Columns) -> object """
        ...


    def Add(self, BeforeColumn:int) -> Column:
        """ Add(self: Columns, BeforeColumn: int) -> Column """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ConnectorFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ConnectorFormat) -> Application """
        ...

    @property
    def BeginConnected(self): # -> MsoTriState
        """ Get: BeginConnected(self: ConnectorFormat) -> MsoTriState """
        ...

    @property
    def BeginConnectedShape(self) -> Shape:
        """ Get: BeginConnectedShape(self: ConnectorFormat) -> Shape """
        ...

    @property
    def BeginConnectionSite(self) -> int:
        """ Get: BeginConnectionSite(self: ConnectorFormat) -> int """
        ...

    @property
    def EndConnected(self): # -> MsoTriState
        """ Get: EndConnected(self: ConnectorFormat) -> MsoTriState """
        ...

    @property
    def EndConnectedShape(self) -> Shape:
        """ Get: EndConnectedShape(self: ConnectorFormat) -> Shape """
        ...

    @property
    def EndConnectionSite(self) -> int:
        """ Get: EndConnectionSite(self: ConnectorFormat) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ConnectorFormat) -> object """
        ...

    @property
    def Type(self): # -> MsoConnectorType
        """
        Get: Type(self: ConnectorFormat) -> MsoConnectorType
        Set: Type(self: ConnectorFormat) = value
        """
        ...


    def BeginConnect(self, ConnectedShape:Shape, ConnectionSite:int): # -> 
        """ BeginConnect(self: ConnectorFormat, ConnectedShape: Shape, ConnectionSite: int) """
        ...

    def BeginDisconnect(self): # -> 
        """ BeginDisconnect(self: ConnectorFormat) """
        ...

    def EndConnect(self, ConnectedShape:Shape, ConnectionSite:int): # -> 
        """ EndConnect(self: ConnectorFormat, ConnectedShape: Shape, ConnectionSite: int) """
        ...

    def EndDisconnect(self): # -> 
        """ EndDisconnect(self: ConnectorFormat) """
        ...


class DocumentEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_BeforeClose(self): # -> 
        """ add_BeforeClose(self: DocumentEvents_Event, : DocumentEvents_BeforeCloseEventHandler) """
        ...

    def add_Open(self): # -> 
        """ add_Open(self: DocumentEvents_Event, : DocumentEvents_OpenEventHandler) """
        ...

    def add_Redo(self): # -> 
        """ add_Redo(self: DocumentEvents_Event, : DocumentEvents_RedoEventHandler) """
        ...

    def add_ShapesAdded(self): # -> 
        """ add_ShapesAdded(self: DocumentEvents_Event, : DocumentEvents_ShapesAddedEventHandler) """
        ...

    def add_ShapesRemoved(self): # -> 
        """ add_ShapesRemoved(self: DocumentEvents_Event, : DocumentEvents_ShapesRemovedEventHandler) """
        ...

    def add_Undo(self): # -> 
        """ add_Undo(self: DocumentEvents_Event, : DocumentEvents_UndoEventHandler) """
        ...

    def add_WizardAfterChange(self): # -> 
        """ add_WizardAfterChange(self: DocumentEvents_Event, : DocumentEvents_WizardAfterChangeEventHandler) """
        ...

    def remove_BeforeClose(self): # -> 
        """ remove_BeforeClose(self: DocumentEvents_Event, : DocumentEvents_BeforeCloseEventHandler) """
        ...

    def remove_Open(self): # -> 
        """ remove_Open(self: DocumentEvents_Event, : DocumentEvents_OpenEventHandler) """
        ...

    def remove_Redo(self): # -> 
        """ remove_Redo(self: DocumentEvents_Event, : DocumentEvents_RedoEventHandler) """
        ...

    def remove_ShapesAdded(self): # -> 
        """ remove_ShapesAdded(self: DocumentEvents_Event, : DocumentEvents_ShapesAddedEventHandler) """
        ...

    def remove_ShapesRemoved(self): # -> 
        """ remove_ShapesRemoved(self: DocumentEvents_Event, : DocumentEvents_ShapesRemovedEventHandler) """
        ...

    def remove_Undo(self): # -> 
        """ remove_Undo(self: DocumentEvents_Event, : DocumentEvents_UndoEventHandler) """
        ...

    def remove_WizardAfterChange(self): # -> 
        """ remove_WizardAfterChange(self: DocumentEvents_Event, : DocumentEvents_WizardAfterChangeEventHandler) """
        ...

    BeforeClose = ...
    Open = ...
    Redo = ...
    ShapesAdded = ...
    ShapesRemoved = ...
    Undo = ...
    WizardAfterChange = ...


class _Document: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActivePrinter(self) -> str:
        """
        Get: ActivePrinter(self: _Document) -> str
        Set: ActivePrinter(self: _Document) = value
        """
        ...

    @property
    def ActiveView(self) -> View:
        """ Get: ActiveView(self: _Document) -> View """
        ...

    @property
    def ActiveWindow(self) -> Window:
        """ Get: ActiveWindow(self: _Document) -> Window """
        ...

    @property
    def AdvancedPrintOptions(self) -> AdvancedPrintOptions:
        """ Get: AdvancedPrintOptions(self: _Document) -> AdvancedPrintOptions """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: _Document) -> Application """
        ...

    @property
    def AvailableBuildingBlocks(self) -> BuildingBlocks:
        """ Get: AvailableBuildingBlocks(self: _Document) -> BuildingBlocks """
        ...

    @property
    def BorderArts(self) -> BorderArts:
        """ Get: BorderArts(self: _Document) -> BorderArts """
        ...

    @property
    def ColorMode(self) -> PbColorMode:
        """ Get: ColorMode(self: _Document) -> PbColorMode """
        ...

    @property
    def ColorScheme(self) -> ColorScheme:
        """
        Get: ColorScheme(self: _Document) -> ColorScheme
        Set: ColorScheme(self: _Document) = value
        """
        ...

    @property
    def ColorsInUse(self) -> ColorsInUse:
        """ Get: ColorsInUse(self: _Document) -> ColorsInUse """
        ...

    @property
    def DefaultTabStop(self) -> object:
        """
        Get: DefaultTabStop(self: _Document) -> object
        Set: DefaultTabStop(self: _Document) = value
        """
        ...

    @property
    def DocumentDirection(self) -> PbDirectionType:
        """
        Get: DocumentDirection(self: _Document) -> PbDirectionType
        Set: DocumentDirection(self: _Document) = value
        """
        ...

    @property
    def EnvelopeVisible(self) -> bool:
        """
        Get: EnvelopeVisible(self: _Document) -> bool
        Set: EnvelopeVisible(self: _Document) = value
        """
        ...

    @property
    def Find(self) -> FindReplace:
        """ Get: Find(self: _Document) -> FindReplace """
        ...

    @property
    def FullName(self) -> str:
        """ Get: FullName(self: _Document) -> str """
        ...

    @property
    def IsDataSourceConnected(self) -> bool:
        """ Get: IsDataSourceConnected(self: _Document) -> bool """
        ...

    @property
    def IsWizard(self) -> bool:
        """ Get: IsWizard(self: _Document) -> bool """
        ...

    @property
    def LayoutGuides(self) -> LayoutGuides:
        """ Get: LayoutGuides(self: _Document) -> LayoutGuides """
        ...

    @property
    def MailEnvelope(self): # -> MsoEnvelope
        """ Get: MailEnvelope(self: _Document) -> MsoEnvelope """
        ...

    @property
    def MailMerge(self) -> MailMerge:
        """ Get: MailMerge(self: _Document) -> MailMerge """
        ...

    @property
    def MasterPages(self) -> MasterPages:
        """ Get: MasterPages(self: _Document) -> MasterPages """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: _Document) -> str """
        ...

    @property
    def Pages(self) -> Pages:
        """ Get: Pages(self: _Document) -> Pages """
        ...

    @property
    def PageSetup(self) -> PageSetup:
        """ Get: PageSetup(self: _Document) -> PageSetup """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: _Document) -> object """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: _Document) -> str """
        ...

    @property
    def PersonalInformationSet(self) -> PbPersonalInfoSet:
        """
        Get: PersonalInformationSet(self: _Document) -> PbPersonalInfoSet
        Set: PersonalInformationSet(self: _Document) = value
        """
        ...

    @property
    def Plates(self) -> Plates:
        """ Get: Plates(self: _Document) -> Plates """
        ...

    @property
    def PrintPageBackgrounds(self) -> bool:
        """
        Get: PrintPageBackgrounds(self: _Document) -> bool
        Set: PrintPageBackgrounds(self: _Document) = value
        """
        ...

    @property
    def PrintStyle(self) -> PbPrintStyle:
        """ Get: PrintStyle(self: _Document) -> PbPrintStyle """
        ...

    @property
    def PublicationType(self) -> PbPublicationType:
        """ Get: PublicationType(self: _Document) -> PbPublicationType """
        ...

    @property
    def ReadOnly(self) -> bool:
        """ Get: ReadOnly(self: _Document) -> bool """
        ...

    @property
    def RedoActionsAvailable(self) -> int:
        """ Get: RedoActionsAvailable(self: _Document) -> int """
        ...

    @property
    def RemovePersonalInformation(self) -> bool:
        """
        Get: RemovePersonalInformation(self: _Document) -> bool
        Set: RemovePersonalInformation(self: _Document) = value
        """
        ...

    @property
    def Saved(self) -> bool:
        """ Get: Saved(self: _Document) -> bool """
        ...

    @property
    def SaveFormat(self) -> PbFileFormat:
        """ Get: SaveFormat(self: _Document) -> PbFileFormat """
        ...

    @property
    def ScratchArea(self) -> ScratchArea:
        """ Get: ScratchArea(self: _Document) -> ScratchArea """
        ...

    @property
    def Sections(self) -> Sections:
        """ Get: Sections(self: _Document) -> Sections """
        ...

    @property
    def Selection(self) -> Selection:
        """ Get: Selection(self: _Document) -> Selection """
        ...

    @property
    def Stories(self) -> Stories:
        """ Get: Stories(self: _Document) -> Stories """
        ...

    @property
    def SurplusShapes(self) -> ShapeRange:
        """ Get: SurplusShapes(self: _Document) -> ShapeRange """
        ...

    @property
    def Tags(self) -> Tags:
        """ Get: Tags(self: _Document) -> Tags """
        ...

    @property
    def TextStyles(self) -> TextStyles:
        """ Get: TextStyles(self: _Document) -> TextStyles """
        ...

    @property
    def UndoActionsAvailable(self) -> int:
        """ Get: UndoActionsAvailable(self: _Document) -> int """
        ...

    @property
    def ViewBoundaries(self) -> bool:
        """
        Get: ViewBoundaries(self: _Document) -> bool
        Set: ViewBoundaries(self: _Document) = value
        """
        ...

    @property
    def ViewBoundariesAndGuides(self) -> bool:
        """
        Get: ViewBoundariesAndGuides(self: _Document) -> bool
        Set: ViewBoundariesAndGuides(self: _Document) = value
        """
        ...

    @property
    def ViewGuides(self) -> bool:
        """
        Get: ViewGuides(self: _Document) -> bool
        Set: ViewGuides(self: _Document) = value
        """
        ...

    @property
    def ViewHorizontalBaseLineGuides(self) -> bool:
        """
        Get: ViewHorizontalBaseLineGuides(self: _Document) -> bool
        Set: ViewHorizontalBaseLineGuides(self: _Document) = value
        """
        ...

    @property
    def ViewTwoPageSpread(self) -> bool:
        """
        Get: ViewTwoPageSpread(self: _Document) -> bool
        Set: ViewTwoPageSpread(self: _Document) = value
        """
        ...

    @property
    def ViewVerticalBaseLineGuides(self) -> bool:
        """
        Get: ViewVerticalBaseLineGuides(self: _Document) -> bool
        Set: ViewVerticalBaseLineGuides(self: _Document) = value
        """
        ...

    @property
    def WebNavigationBarSets(self) -> WebNavigationBarSets:
        """ Get: WebNavigationBarSets(self: _Document) -> WebNavigationBarSets """
        ...

    @property
    def Wizard(self) -> Wizard:
        """ Get: Wizard(self: _Document) -> Wizard """
        ...


    def BeginCustomUndoAction(self, ActionName:str): # -> 
        """ BeginCustomUndoAction(self: _Document, ActionName: str) """
        ...

    def ChangeDocument(self, Wizard:PbWizard, Design:int): # -> 
        """ ChangeDocument(self: _Document, Wizard: PbWizard, Design: int) """
        ...

    def Close(self): # -> 
        """ Close(self: _Document) """
        ...

    def ConvertPublicationType(self, Value:PbPublicationType): # -> 
        """ ConvertPublicationType(self: _Document, Value: PbPublicationType) """
        ...

    def CreatePlateCollection(self, Mode:PbColorMode) -> Plates:
        """ CreatePlateCollection(self: _Document, Mode: PbColorMode) -> Plates """
        ...

    def EndCustomUndoAction(self): # -> 
        """ EndCustomUndoAction(self: _Document) """
        ...

    def EnterColorMode(self, Mode:PbColorMode, Plates:object, DeleteExcessInks:bool): # -> 
        """ EnterColorMode(self: _Document, Mode: PbColorMode, Plates: object, DeleteExcessInks: bool) """
        ...

    def EnterColorMode10(self, Mode:PbColorMode, Plates:object): # -> 
        """ EnterColorMode10(self: _Document, Mode: PbColorMode, Plates: object) """
        ...

    def ExportAsFixedFormat(self, Format:PbFixedFormatType, Filename:str, Intent:PbFixedFormatIntent, IncludeDocumentProperties:bool, ColorDownsampleTarget:int, ColorDownsampleThreshold:int, OneBitDownsampleTarget:int, OneBitDownsampleThreshold:int, From:int, To:int, Copies:int, Collate:bool, PrintStyle:PbPrintStyle, DocStructureTags:bool, BitmapMissingFonts:bool, UseISO19005_1:bool, ExternalExporter:object): # -> 
        """ ExportAsFixedFormat(self: _Document, Format: PbFixedFormatType, Filename: str, Intent: PbFixedFormatIntent, IncludeDocumentProperties: bool, ColorDownsampleTarget: int, ColorDownsampleThreshold: int, OneBitDownsampleTarget: int, OneBitDownsampleThreshold: int, From: int, To: int, Copies: int, Collate: bool, PrintStyle: PbPrintStyle, DocStructureTags: bool, BitmapMissingFonts: bool, UseISO19005_1: bool, ExternalExporter: object) """
        ...

    def FindShapeByWizardTag(self, WizardTag:PbWizardTag, Instance:int) -> ShapeRange:
        """ FindShapeByWizardTag(self: _Document, WizardTag: PbWizardTag, Instance: int) -> ShapeRange """
        ...

    def FindShapesByTag(self, TagName:str) -> ShapeRange:
        """ FindShapesByTag(self: _Document, TagName: str) -> ShapeRange """
        ...

    def PrintOut(self, From:int, To:int, PrintToFile:str, Copies:int, Collate:bool): # -> 
        """ PrintOut(self: _Document, From: int, To: int, PrintToFile: str, Copies: int, Collate: bool) """
        ...

    def PrintOutEx(self, From:int, To:int, PrintToFile:str, Copies:int, Collate:bool, PrintStyle:PbPrintStyle): # -> 
        """ PrintOutEx(self: _Document, From: int, To: int, PrintToFile: str, Copies: int, Collate: bool, PrintStyle: PbPrintStyle) """
        ...

    def Redo(self, Count:int): # -> 
        """ Redo(self: _Document, Count: int) """
        ...

    def Save(self): # -> 
        """ Save(self: _Document) """
        ...

    def SaveAs(self, Filename:object, Format:PbFileFormat, AddToRecentFiles:bool): # -> 
        """ SaveAs(self: _Document, Filename: object, Format: PbFileFormat, AddToRecentFiles: bool) """
        ...

    def SelectID(self, oh:int): # -> 
        """ SelectID(self: _Document, oh: int) """
        ...

    def SetBusinessInformation(self, Name:str): # -> 
        """ SetBusinessInformation(self: _Document, Name: str) """
        ...

    def Undo(self, Count:int): # -> 
        """ Undo(self: _Document, Count: int) """
        ...

    def UndoClear(self): # -> 
        """ UndoClear(self: _Document) """
        ...

    def UpdateOLEObjects(self): # -> 
        """ UpdateOLEObjects(self: _Document) """
        ...

    def WebPagePreview(self): # -> 
        """ WebPagePreview(self: _Document) """
        ...


class Document(_Document, DocumentEvents_Event): # skipped bases: <type 'object'>
    """ no doc """
    pass

class DocumentClass(__ComObject, Document): # skipped bases: <type 'DocumentEvents_Event'>, <type '_Document'>, <type 'object'>
    """ DocumentClass() """
    @property
    def ActivePrinter(self) -> str:
        """
        Get: ActivePrinter(self: DocumentClass) -> str
        Set: ActivePrinter(self: DocumentClass) = value
        """
        ...

    @property
    def ActiveView(self) -> View:
        """ Get: ActiveView(self: DocumentClass) -> View """
        ...

    @property
    def ActiveWindow(self) -> Window:
        """ Get: ActiveWindow(self: DocumentClass) -> Window """
        ...

    @property
    def AdvancedPrintOptions(self) -> AdvancedPrintOptions:
        """ Get: AdvancedPrintOptions(self: DocumentClass) -> AdvancedPrintOptions """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: DocumentClass) -> Application """
        ...

    @property
    def AvailableBuildingBlocks(self) -> BuildingBlocks:
        """ Get: AvailableBuildingBlocks(self: DocumentClass) -> BuildingBlocks """
        ...

    @property
    def BorderArts(self) -> BorderArts:
        """ Get: BorderArts(self: DocumentClass) -> BorderArts """
        ...

    @property
    def ColorMode(self) -> PbColorMode:
        """ Get: ColorMode(self: DocumentClass) -> PbColorMode """
        ...

    @property
    def ColorScheme(self) -> ColorScheme:
        """
        Get: ColorScheme(self: DocumentClass) -> ColorScheme
        Set: ColorScheme(self: DocumentClass) = value
        """
        ...

    @property
    def ColorsInUse(self) -> ColorsInUse:
        """ Get: ColorsInUse(self: DocumentClass) -> ColorsInUse """
        ...

    @property
    def DefaultTabStop(self) -> object:
        """
        Get: DefaultTabStop(self: DocumentClass) -> object
        Set: DefaultTabStop(self: DocumentClass) = value
        """
        ...

    @property
    def DocumentDirection(self) -> PbDirectionType:
        """
        Get: DocumentDirection(self: DocumentClass) -> PbDirectionType
        Set: DocumentDirection(self: DocumentClass) = value
        """
        ...

    @property
    def EnvelopeVisible(self) -> bool:
        """
        Get: EnvelopeVisible(self: DocumentClass) -> bool
        Set: EnvelopeVisible(self: DocumentClass) = value
        """
        ...

    @property
    def Find(self) -> FindReplace:
        """ Get: Find(self: DocumentClass) -> FindReplace """
        ...

    @property
    def FullName(self) -> str:
        """ Get: FullName(self: DocumentClass) -> str """
        ...

    @property
    def IsDataSourceConnected(self) -> bool:
        """ Get: IsDataSourceConnected(self: DocumentClass) -> bool """
        ...

    @property
    def IsWizard(self) -> bool:
        """ Get: IsWizard(self: DocumentClass) -> bool """
        ...

    @property
    def LayoutGuides(self) -> LayoutGuides:
        """ Get: LayoutGuides(self: DocumentClass) -> LayoutGuides """
        ...

    @property
    def MailEnvelope(self): # -> MsoEnvelope
        """ Get: MailEnvelope(self: DocumentClass) -> MsoEnvelope """
        ...

    @property
    def MailMerge(self) -> MailMerge:
        """ Get: MailMerge(self: DocumentClass) -> MailMerge """
        ...

    @property
    def MasterPages(self) -> MasterPages:
        """ Get: MasterPages(self: DocumentClass) -> MasterPages """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DocumentClass) -> str """
        ...

    @property
    def Pages(self) -> Pages:
        """ Get: Pages(self: DocumentClass) -> Pages """
        ...

    @property
    def PageSetup(self) -> PageSetup:
        """ Get: PageSetup(self: DocumentClass) -> PageSetup """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: DocumentClass) -> object """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: DocumentClass) -> str """
        ...

    @property
    def PersonalInformationSet(self) -> PbPersonalInfoSet:
        """
        Get: PersonalInformationSet(self: DocumentClass) -> PbPersonalInfoSet
        Set: PersonalInformationSet(self: DocumentClass) = value
        """
        ...

    @property
    def Plates(self) -> Plates:
        """ Get: Plates(self: DocumentClass) -> Plates """
        ...

    @property
    def PrintPageBackgrounds(self) -> bool:
        """
        Get: PrintPageBackgrounds(self: DocumentClass) -> bool
        Set: PrintPageBackgrounds(self: DocumentClass) = value
        """
        ...

    @property
    def PrintStyle(self) -> PbPrintStyle:
        """ Get: PrintStyle(self: DocumentClass) -> PbPrintStyle """
        ...

    @property
    def PublicationType(self) -> PbPublicationType:
        """ Get: PublicationType(self: DocumentClass) -> PbPublicationType """
        ...

    @property
    def ReadOnly(self) -> bool:
        """ Get: ReadOnly(self: DocumentClass) -> bool """
        ...

    @property
    def RedoActionsAvailable(self) -> int:
        """ Get: RedoActionsAvailable(self: DocumentClass) -> int """
        ...

    @property
    def RemovePersonalInformation(self) -> bool:
        """
        Get: RemovePersonalInformation(self: DocumentClass) -> bool
        Set: RemovePersonalInformation(self: DocumentClass) = value
        """
        ...

    @property
    def Saved(self) -> bool:
        """ Get: Saved(self: DocumentClass) -> bool """
        ...

    @property
    def SaveFormat(self) -> PbFileFormat:
        """ Get: SaveFormat(self: DocumentClass) -> PbFileFormat """
        ...

    @property
    def ScratchArea(self) -> ScratchArea:
        """ Get: ScratchArea(self: DocumentClass) -> ScratchArea """
        ...

    @property
    def Sections(self) -> Sections:
        """ Get: Sections(self: DocumentClass) -> Sections """
        ...

    @property
    def Selection(self) -> Selection:
        """ Get: Selection(self: DocumentClass) -> Selection """
        ...

    @property
    def Stories(self) -> Stories:
        """ Get: Stories(self: DocumentClass) -> Stories """
        ...

    @property
    def SurplusShapes(self) -> ShapeRange:
        """ Get: SurplusShapes(self: DocumentClass) -> ShapeRange """
        ...

    @property
    def Tags(self) -> Tags:
        """ Get: Tags(self: DocumentClass) -> Tags """
        ...

    @property
    def TextStyles(self) -> TextStyles:
        """ Get: TextStyles(self: DocumentClass) -> TextStyles """
        ...

    @property
    def UndoActionsAvailable(self) -> int:
        """ Get: UndoActionsAvailable(self: DocumentClass) -> int """
        ...

    @property
    def ViewBoundaries(self) -> bool:
        """
        Get: ViewBoundaries(self: DocumentClass) -> bool
        Set: ViewBoundaries(self: DocumentClass) = value
        """
        ...

    @property
    def ViewBoundariesAndGuides(self) -> bool:
        """
        Get: ViewBoundariesAndGuides(self: DocumentClass) -> bool
        Set: ViewBoundariesAndGuides(self: DocumentClass) = value
        """
        ...

    @property
    def ViewGuides(self) -> bool:
        """
        Get: ViewGuides(self: DocumentClass) -> bool
        Set: ViewGuides(self: DocumentClass) = value
        """
        ...

    @property
    def ViewHorizontalBaseLineGuides(self) -> bool:
        """
        Get: ViewHorizontalBaseLineGuides(self: DocumentClass) -> bool
        Set: ViewHorizontalBaseLineGuides(self: DocumentClass) = value
        """
        ...

    @property
    def ViewTwoPageSpread(self) -> bool:
        """
        Get: ViewTwoPageSpread(self: DocumentClass) -> bool
        Set: ViewTwoPageSpread(self: DocumentClass) = value
        """
        ...

    @property
    def ViewVerticalBaseLineGuides(self) -> bool:
        """
        Get: ViewVerticalBaseLineGuides(self: DocumentClass) -> bool
        Set: ViewVerticalBaseLineGuides(self: DocumentClass) = value
        """
        ...

    @property
    def WebNavigationBarSets(self) -> WebNavigationBarSets:
        """ Get: WebNavigationBarSets(self: DocumentClass) -> WebNavigationBarSets """
        ...

    @property
    def Wizard(self) -> Wizard:
        """ Get: Wizard(self: DocumentClass) -> Wizard """
        ...


    def add_BeforeClose(self): # -> 
        """ add_BeforeClose(self: DocumentClass, : DocumentEvents_BeforeCloseEventHandler) """
        ...

    def add_Open(self): # -> 
        """ add_Open(self: DocumentClass, : DocumentEvents_OpenEventHandler) """
        ...

    def add_Redo(self): # -> 
        """ add_Redo(self: DocumentClass, : DocumentEvents_RedoEventHandler) """
        ...

    def add_ShapesAdded(self): # -> 
        """ add_ShapesAdded(self: DocumentClass, : DocumentEvents_ShapesAddedEventHandler) """
        ...

    def add_ShapesRemoved(self): # -> 
        """ add_ShapesRemoved(self: DocumentClass, : DocumentEvents_ShapesRemovedEventHandler) """
        ...

    def add_Undo(self): # -> 
        """ add_Undo(self: DocumentClass, : DocumentEvents_UndoEventHandler) """
        ...

    def add_WizardAfterChange(self): # -> 
        """ add_WizardAfterChange(self: DocumentClass, : DocumentEvents_WizardAfterChangeEventHandler) """
        ...

    def BeginCustomUndoAction(self, ActionName:str): # -> 
        """ BeginCustomUndoAction(self: DocumentClass, ActionName: str) """
        ...

    def ChangeDocument(self, Wizard:PbWizard, Design:int): # -> 
        """ ChangeDocument(self: DocumentClass, Wizard: PbWizard, Design: int) """
        ...

    def Close(self): # -> 
        """ Close(self: DocumentClass) """
        ...

    def ConvertPublicationType(self, Value:PbPublicationType): # -> 
        """ ConvertPublicationType(self: DocumentClass, Value: PbPublicationType) """
        ...

    def CreatePlateCollection(self, Mode:PbColorMode) -> Plates:
        """ CreatePlateCollection(self: DocumentClass, Mode: PbColorMode) -> Plates """
        ...

    def EndCustomUndoAction(self): # -> 
        """ EndCustomUndoAction(self: DocumentClass) """
        ...

    def EnterColorMode(self, Mode:PbColorMode, Plates:object, DeleteExcessInks:bool): # -> 
        """ EnterColorMode(self: DocumentClass, Mode: PbColorMode, Plates: object, DeleteExcessInks: bool) """
        ...

    def EnterColorMode10(self, Mode:PbColorMode, Plates:object): # -> 
        """ EnterColorMode10(self: DocumentClass, Mode: PbColorMode, Plates: object) """
        ...

    def ExportAsFixedFormat(self, Format:PbFixedFormatType, Filename:str, Intent:PbFixedFormatIntent, IncludeDocumentProperties:bool, ColorDownsampleTarget:int, ColorDownsampleThreshold:int, OneBitDownsampleTarget:int, OneBitDownsampleThreshold:int, From:int, To:int, Copies:int, Collate:bool, PrintStyle:PbPrintStyle, DocStructureTags:bool, BitmapMissingFonts:bool, UseISO19005_1:bool, ExternalExporter:object): # -> 
        """ ExportAsFixedFormat(self: DocumentClass, Format: PbFixedFormatType, Filename: str, Intent: PbFixedFormatIntent, IncludeDocumentProperties: bool, ColorDownsampleTarget: int, ColorDownsampleThreshold: int, OneBitDownsampleTarget: int, OneBitDownsampleThreshold: int, From: int, To: int, Copies: int, Collate: bool, PrintStyle: PbPrintStyle, DocStructureTags: bool, BitmapMissingFonts: bool, UseISO19005_1: bool, ExternalExporter: object) """
        ...

    def FindShapeByWizardTag(self, WizardTag:PbWizardTag, Instance:int) -> ShapeRange:
        """ FindShapeByWizardTag(self: DocumentClass, WizardTag: PbWizardTag, Instance: int) -> ShapeRange """
        ...

    def FindShapesByTag(self, TagName:str) -> ShapeRange:
        """ FindShapesByTag(self: DocumentClass, TagName: str) -> ShapeRange """
        ...

    def PrintOut(self, From:int, To:int, PrintToFile:str, Copies:int, Collate:bool): # -> 
        """ PrintOut(self: DocumentClass, From: int, To: int, PrintToFile: str, Copies: int, Collate: bool) """
        ...

    def PrintOutEx(self, From:int, To:int, PrintToFile:str, Copies:int, Collate:bool, PrintStyle:PbPrintStyle): # -> 
        """ PrintOutEx(self: DocumentClass, From: int, To: int, PrintToFile: str, Copies: int, Collate: bool, PrintStyle: PbPrintStyle) """
        ...

    def Redo(self, Count:int): # -> 
        """ Redo(self: DocumentClass, Count: int) """
        ...

    def remove_BeforeClose(self): # -> 
        """ remove_BeforeClose(self: DocumentClass, : DocumentEvents_BeforeCloseEventHandler) """
        ...

    def remove_Open(self): # -> 
        """ remove_Open(self: DocumentClass, : DocumentEvents_OpenEventHandler) """
        ...

    def remove_Redo(self): # -> 
        """ remove_Redo(self: DocumentClass, : DocumentEvents_RedoEventHandler) """
        ...

    def remove_ShapesAdded(self): # -> 
        """ remove_ShapesAdded(self: DocumentClass, : DocumentEvents_ShapesAddedEventHandler) """
        ...

    def remove_ShapesRemoved(self): # -> 
        """ remove_ShapesRemoved(self: DocumentClass, : DocumentEvents_ShapesRemovedEventHandler) """
        ...

    def remove_Undo(self): # -> 
        """ remove_Undo(self: DocumentClass, : DocumentEvents_UndoEventHandler) """
        ...

    def remove_WizardAfterChange(self): # -> 
        """ remove_WizardAfterChange(self: DocumentClass, : DocumentEvents_WizardAfterChangeEventHandler) """
        ...

    def Save(self): # -> 
        """ Save(self: DocumentClass) """
        ...

    def SaveAs(self, Filename:object, Format:PbFileFormat, AddToRecentFiles:bool): # -> 
        """ SaveAs(self: DocumentClass, Filename: object, Format: PbFileFormat, AddToRecentFiles: bool) """
        ...

    def SelectID(self, oh:int): # -> 
        """ SelectID(self: DocumentClass, oh: int) """
        ...

    def SetBusinessInformation(self, Name:str): # -> 
        """ SetBusinessInformation(self: DocumentClass, Name: str) """
        ...

    def Undo(self, Count:int): # -> 
        """ Undo(self: DocumentClass, Count: int) """
        ...

    def UndoClear(self): # -> 
        """ UndoClear(self: DocumentClass) """
        ...

    def UpdateOLEObjects(self): # -> 
        """ UpdateOLEObjects(self: DocumentClass) """
        ...

    def WebPagePreview(self): # -> 
        """ WebPagePreview(self: DocumentClass) """
        ...

    BeforeClose = ...
    DocumentEvents_Event_Redo = ...
    DocumentEvents_Event_Undo = ...
    Open = ...
    ShapesAdded = ...
    ShapesRemoved = ...
    WizardAfterChange = ...


class DocumentEvents: # skipped bases: <type 'object'>
    """ no doc """
    def BeforeClose(self, Cancel) -> bool:
        """ BeforeClose(self: DocumentEvents) -> bool """
        ...

    def Open(self): # -> 
        """ Open(self: DocumentEvents) """
        ...

    def Redo(self): # -> 
        """ Redo(self: DocumentEvents) """
        ...

    def ShapesAdded(self): # -> 
        """ ShapesAdded(self: DocumentEvents) """
        ...

    def ShapesRemoved(self): # -> 
        """ ShapesRemoved(self: DocumentEvents) """
        ...

    def Undo(self): # -> 
        """ Undo(self: DocumentEvents) """
        ...

    def WizardAfterChange(self): # -> 
        """ WizardAfterChange(self: DocumentEvents) """
        ...


class DocumentEvents_BeforeCloseEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DocumentEvents_BeforeCloseEventHandler(: object, : UIntPtr) """
    def Invoke(self, Cancel) -> bool:
        """ Invoke(self: DocumentEvents_BeforeCloseEventHandler) -> bool """
        ...


class DocumentEvents_OpenEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DocumentEvents_OpenEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: DocumentEvents_OpenEventHandler) """
        ...


class DocumentEvents_RedoEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DocumentEvents_RedoEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: DocumentEvents_RedoEventHandler) """
        ...


class DocumentEvents_ShapesAddedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DocumentEvents_ShapesAddedEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: DocumentEvents_ShapesAddedEventHandler) """
        ...


class DocumentEvents_ShapesRemovedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DocumentEvents_ShapesRemovedEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: DocumentEvents_ShapesRemovedEventHandler) """
        ...


class DocumentEvents_SinkHelper(DocumentEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_BeforeCloseDelegate = ...
    m_dwCookie = ...
    m_OpenDelegate = ...
    m_RedoDelegate = ...
    m_ShapesAddedDelegate = ...
    m_ShapesRemovedDelegate = ...
    m_UndoDelegate = ...
    m_WizardAfterChangeDelegate = ...


class DocumentEvents_UndoEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DocumentEvents_UndoEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: DocumentEvents_UndoEventHandler) """
        ...


class DocumentEvents_WizardAfterChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DocumentEvents_WizardAfterChangeEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: DocumentEvents_WizardAfterChangeEventHandler) """
        ...


class Documents(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Documents) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Documents) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Documents) -> object """
        ...


    def Add(self, PbWizard:PbWizard, desid:int) -> Document:
        """ Add(self: Documents, PbWizard: PbWizard, desid: int) -> Document """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DropCap: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: DropCap) -> Application """
        ...

    @property
    def FontBold(self): # -> MsoTriState
        """
        Get: FontBold(self: DropCap) -> MsoTriState
        Set: FontBold(self: DropCap) = value
        """
        ...

    @property
    def FontColor(self) -> ColorFormat:
        """ Get: FontColor(self: DropCap) -> ColorFormat """
        ...

    @property
    def FontItalic(self): # -> MsoTriState
        """
        Get: FontItalic(self: DropCap) -> MsoTriState
        Set: FontItalic(self: DropCap) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: DropCap) -> str
        Set: FontName(self: DropCap) = value
        """
        ...

    @property
    def LinesUp(self) -> int:
        """
        Get: LinesUp(self: DropCap) -> int
        Set: LinesUp(self: DropCap) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: DropCap) -> object """
        ...

    @property
    def Size(self) -> int:
        """
        Get: Size(self: DropCap) -> int
        Set: Size(self: DropCap) = value
        """
        ...

    @property
    def Span(self) -> int:
        """
        Get: Span(self: DropCap) -> int
        Set: Span(self: DropCap) = value
        """
        ...


    def ApplyCustomDropCap(self, LinesUp:int, Size:int, Span:int, FontName:str, Bold:bool, Italic:bool): # -> 
        """ ApplyCustomDropCap(self: DropCap, LinesUp: int, Size: int, Span: int, FontName: str, Bold: bool, Italic: bool) """
        ...

    def Clear(self): # -> 
        """ Clear(self: DropCap) """
        ...


class EmailMergeEnvelope: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: EmailMergeEnvelope) -> Application """
        ...

    @property
    def Attachemts(self) -> Attachments:
        """ Get: Attachemts(self: EmailMergeEnvelope) -> Attachments """
        ...

    @property
    def Bcc(self) -> str:
        """
        Get: Bcc(self: EmailMergeEnvelope) -> str
        Set: Bcc(self: EmailMergeEnvelope) = value
        """
        ...

    @property
    def Cc(self) -> MailMergeDataField:
        """
        Get: Cc(self: EmailMergeEnvelope) -> MailMergeDataField
        Set: Cc(self: EmailMergeEnvelope) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: EmailMergeEnvelope) -> object """
        ...

    @property
    def Priority(self) -> pbEmailMergePriority:
        """
        Get: Priority(self: EmailMergeEnvelope) -> pbEmailMergePriority
        Set: Priority(self: EmailMergeEnvelope) = value
        """
        ...

    @property
    def Subject(self) -> str:
        """
        Get: Subject(self: EmailMergeEnvelope) -> str
        Set: Subject(self: EmailMergeEnvelope) = value
        """
        ...

    @property
    def To(self) -> MailMergeDataField:
        """
        Get: To(self: EmailMergeEnvelope) -> MailMergeDataField
        Set: To(self: EmailMergeEnvelope) = value
        """
        ...



class Field: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Field) -> Application """
        ...

    @property
    def Code(self) -> str:
        """ Get: Code(self: Field) -> str """
        ...

    @property
    def Next(self) -> Field:
        """ Get: Next(self: Field) -> Field """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Field) -> object """
        ...

    @property
    def PhoneticGuide(self) -> PhoneticGuide:
        """ Get: PhoneticGuide(self: Field) -> PhoneticGuide """
        ...

    @property
    def Result(self) -> str:
        """ Get: Result(self: Field) -> str """
        ...

    @property
    def TextRange(self) -> TextRange:
        """ Get: TextRange(self: Field) -> TextRange """
        ...

    @property
    def Type(self) -> PbFieldType:
        """ Get: Type(self: Field) -> PbFieldType """
        ...


    def Unlink(self): # -> 
        """ Unlink(self: Field) """
        ...


class Fields(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Fields) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Fields) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Fields) -> object """
        ...


    def AddHorizontalInVertical(self, Range:TextRange, Text:str) -> Field:
        """ AddHorizontalInVertical(self: Fields, Range: TextRange, Text: str) -> Field """
        ...

    def AddPhoneticGuide(self, Range:TextRange, Text:str, Alignment:PbPhoneticGuideAlignmentType, Raise:object, FontName:str, FontSize:object) -> Field:
        """ AddPhoneticGuide(self: Fields, Range: TextRange, Text: str, Alignment: PbPhoneticGuideAlignmentType, Raise: object, FontName: str, FontSize: object) -> Field """
        ...

    def Unlink(self): # -> 
        """ Unlink(self: Fields) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class FillFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: FillFormat) -> Application """
        ...

    @property
    def BackColor(self) -> ColorFormat:
        """
        Get: BackColor(self: FillFormat) -> ColorFormat
        Set: BackColor(self: FillFormat) = value
        """
        ...

    @property
    def ForeColor(self) -> ColorFormat:
        """
        Get: ForeColor(self: FillFormat) -> ColorFormat
        Set: ForeColor(self: FillFormat) = value
        """
        ...

    @property
    def GradientAngle(self) -> Single:
        """
        Get: GradientAngle(self: FillFormat) -> Single
        Set: GradientAngle(self: FillFormat) = value
        """
        ...

    @property
    def GradientColorType(self): # -> MsoGradientColorType
        """ Get: GradientColorType(self: FillFormat) -> MsoGradientColorType """
        ...

    @property
    def GradientDegree(self) -> Single:
        """ Get: GradientDegree(self: FillFormat) -> Single """
        ...

    @property
    def GradientStyle(self): # -> MsoGradientStyle
        """ Get: GradientStyle(self: FillFormat) -> MsoGradientStyle """
        ...

    @property
    def GradientVariant(self) -> int:
        """ Get: GradientVariant(self: FillFormat) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: FillFormat) -> object """
        ...

    @property
    def Pattern(self): # -> MsoPatternType
        """ Get: Pattern(self: FillFormat) -> MsoPatternType """
        ...

    @property
    def PresetGradientType(self): # -> MsoPresetGradientType
        """ Get: PresetGradientType(self: FillFormat) -> MsoPresetGradientType """
        ...

    @property
    def PresetTexture(self): # -> MsoPresetTexture
        """ Get: PresetTexture(self: FillFormat) -> MsoPresetTexture """
        ...

    @property
    def RotateWithObject(self): # -> MsoTriState
        """
        Get: RotateWithObject(self: FillFormat) -> MsoTriState
        Set: RotateWithObject(self: FillFormat) = value
        """
        ...

    @property
    def TextureAlignment(self): # -> MsoTextureAlignment
        """
        Get: TextureAlignment(self: FillFormat) -> MsoTextureAlignment
        Set: TextureAlignment(self: FillFormat) = value
        """
        ...

    @property
    def TextureHorizontalScale(self) -> Single:
        """
        Get: TextureHorizontalScale(self: FillFormat) -> Single
        Set: TextureHorizontalScale(self: FillFormat) = value
        """
        ...

    @property
    def TextureName(self) -> str:
        """ Get: TextureName(self: FillFormat) -> str """
        ...

    @property
    def TextureOffsetX(self) -> Single:
        """
        Get: TextureOffsetX(self: FillFormat) -> Single
        Set: TextureOffsetX(self: FillFormat) = value
        """
        ...

    @property
    def TextureOffsetY(self) -> Single:
        """
        Get: TextureOffsetY(self: FillFormat) -> Single
        Set: TextureOffsetY(self: FillFormat) = value
        """
        ...

    @property
    def TextureType(self): # -> MsoTextureType
        """ Get: TextureType(self: FillFormat) -> MsoTextureType """
        ...

    @property
    def TextureVerticalScale(self) -> Single:
        """
        Get: TextureVerticalScale(self: FillFormat) -> Single
        Set: TextureVerticalScale(self: FillFormat) = value
        """
        ...

    @property
    def Transparency(self) -> Single:
        """
        Get: Transparency(self: FillFormat) -> Single
        Set: Transparency(self: FillFormat) = value
        """
        ...

    @property
    def Type(self): # -> MsoFillType
        """ Get: Type(self: FillFormat) -> MsoFillType """
        ...

    @property
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: FillFormat) -> MsoTriState
        Set: Visible(self: FillFormat) = value
        """
        ...


    def OneColorGradient(self, Style, Variant:int, Degree:Single): # ->  # Not found arg types: {'Style': 'MsoGradientStyle'}
        """ OneColorGradient(self: FillFormat, Style: MsoGradientStyle, Variant: int, Degree: Single) """
        ...

    def Patterned(self, Pattern): # ->  # Not found arg types: {'Pattern': 'MsoPatternType'}
        """ Patterned(self: FillFormat, Pattern: MsoPatternType) """
        ...

    def PresetGradient(self, Style, Variant:int, PresetGradientType): # ->  # Not found arg types: {'Style': 'MsoGradientStyle', 'PresetGradientType': 'MsoPresetGradientType'}
        """ PresetGradient(self: FillFormat, Style: MsoGradientStyle, Variant: int, PresetGradientType: MsoPresetGradientType) """
        ...

    def PresetTextured(self, PresetTexture): # ->  # Not found arg types: {'PresetTexture': 'MsoPresetTexture'}
        """ PresetTextured(self: FillFormat, PresetTexture: MsoPresetTexture) """
        ...

    def Solid(self): # -> 
        """ Solid(self: FillFormat) """
        ...

    def TwoColorGradient(self, Style, Variant:int): # ->  # Not found arg types: {'Style': 'MsoGradientStyle'}
        """ TwoColorGradient(self: FillFormat, Style: MsoGradientStyle, Variant: int) """
        ...

    def UserPicture(self, PictureFile:str): # -> 
        """ UserPicture(self: FillFormat, PictureFile: str) """
        ...

    def UserTextured(self, TextureFile:str): # -> 
        """ UserTextured(self: FillFormat, TextureFile: str) """
        ...


class FindReplace: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: FindReplace) -> Application """
        ...

    @property
    def FindText(self) -> str:
        """
        Get: FindText(self: FindReplace) -> str
        Set: FindText(self: FindReplace) = value
        """
        ...

    @property
    def Forward(self) -> bool:
        """
        Get: Forward(self: FindReplace) -> bool
        Set: Forward(self: FindReplace) = value
        """
        ...

    @property
    def FoundTextRange(self) -> TextRange:
        """ Get: FoundTextRange(self: FindReplace) -> TextRange """
        ...

    @property
    def MatchAlefHamza(self) -> bool:
        """
        Get: MatchAlefHamza(self: FindReplace) -> bool
        Set: MatchAlefHamza(self: FindReplace) = value
        """
        ...

    @property
    def MatchCase(self) -> bool:
        """
        Get: MatchCase(self: FindReplace) -> bool
        Set: MatchCase(self: FindReplace) = value
        """
        ...

    @property
    def MatchDiacritics(self) -> bool:
        """
        Get: MatchDiacritics(self: FindReplace) -> bool
        Set: MatchDiacritics(self: FindReplace) = value
        """
        ...

    @property
    def MatchKashida(self) -> bool:
        """
        Get: MatchKashida(self: FindReplace) -> bool
        Set: MatchKashida(self: FindReplace) = value
        """
        ...

    @property
    def MatchWholeWord(self) -> bool:
        """
        Get: MatchWholeWord(self: FindReplace) -> bool
        Set: MatchWholeWord(self: FindReplace) = value
        """
        ...

    @property
    def MatchWidth(self) -> bool:
        """
        Get: MatchWidth(self: FindReplace) -> bool
        Set: MatchWidth(self: FindReplace) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: FindReplace) -> object """
        ...

    @property
    def ReplaceScope(self) -> PbReplaceScope:
        """
        Get: ReplaceScope(self: FindReplace) -> PbReplaceScope
        Set: ReplaceScope(self: FindReplace) = value
        """
        ...

    @property
    def ReplaceWithText(self) -> str:
        """
        Get: ReplaceWithText(self: FindReplace) -> str
        Set: ReplaceWithText(self: FindReplace) = value
        """
        ...


    def Clear(self): # -> 
        """ Clear(self: FindReplace) """
        ...

    def Execute(self) -> bool:
        """ Execute(self: FindReplace) -> bool """
        ...


class Font: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AllCaps(self): # -> MsoTriState
        """
        Get: AllCaps(self: Font) -> MsoTriState
        Set: AllCaps(self: Font) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: Font) -> Application """
        ...

    @property
    def AttachedToText(self) -> bool:
        """ Get: AttachedToText(self: Font) -> bool """
        ...

    @property
    def AutomaticPairKerningThreshold(self) -> object:
        """
        Get: AutomaticPairKerningThreshold(self: Font) -> object
        Set: AutomaticPairKerningThreshold(self: Font) = value
        """
        ...

    @property
    def Bold(self): # -> MsoTriState
        """
        Get: Bold(self: Font) -> MsoTriState
        Set: Bold(self: Font) = value
        """
        ...

    @property
    def BoldBi(self): # -> MsoTriState
        """
        Get: BoldBi(self: Font) -> MsoTriState
        Set: BoldBi(self: Font) = value
        """
        ...

    @property
    def Color(self) -> ColorFormat:
        """ Get: Color(self: Font) -> ColorFormat """
        ...

    @property
    def ContextualAlternates(self): # -> MsoTriState
        """
        Get: ContextualAlternates(self: Font) -> MsoTriState
        Set: ContextualAlternates(self: Font) = value
        """
        ...

    @property
    def DiacriticColor(self) -> ColorFormat:
        """ Get: DiacriticColor(self: Font) -> ColorFormat """
        ...

    @property
    def Emboss(self): # -> MsoTriState
        """
        Get: Emboss(self: Font) -> MsoTriState
        Set: Emboss(self: Font) = value
        """
        ...

    @property
    def Engrave(self): # -> MsoTriState
        """
        Get: Engrave(self: Font) -> MsoTriState
        Set: Engrave(self: Font) = value
        """
        ...

    @property
    def ExpandUsingKashida(self): # -> MsoTriState
        """
        Get: ExpandUsingKashida(self: Font) -> MsoTriState
        Set: ExpandUsingKashida(self: Font) = value
        """
        ...

    @property
    def Fill(self) -> FillFormat:
        """ Get: Fill(self: Font) -> FillFormat """
        ...

    @property
    def Glow(self) -> GlowFormat:
        """ Get: Glow(self: Font) -> GlowFormat """
        ...

    @property
    def Italic(self): # -> MsoTriState
        """
        Get: Italic(self: Font) -> MsoTriState
        Set: Italic(self: Font) = value
        """
        ...

    @property
    def ItalicBi(self): # -> MsoTriState
        """
        Get: ItalicBi(self: Font) -> MsoTriState
        Set: ItalicBi(self: Font) = value
        """
        ...

    @property
    def Kerning(self) -> object:
        """
        Get: Kerning(self: Font) -> object
        Set: Kerning(self: Font) = value
        """
        ...

    @property
    def Ligature(self) -> PbLigaturePresetType:
        """
        Get: Ligature(self: Font) -> PbLigaturePresetType
        Set: Ligature(self: Font) = value
        """
        ...

    @property
    def Line(self) -> LineFormat:
        """ Get: Line(self: Font) -> LineFormat """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Font) -> str
        Set: Name(self: Font) = value
        """
        ...

    @property
    def NumberStyle(self) -> PbNumberStylesType:
        """
        Get: NumberStyle(self: Font) -> PbNumberStylesType
        Set: NumberStyle(self: Font) = value
        """
        ...

    @property
    def Outline(self): # -> MsoTriState
        """
        Get: Outline(self: Font) -> MsoTriState
        Set: Outline(self: Font) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Font) -> object """
        ...

    @property
    def Position(self) -> object:
        """
        Get: Position(self: Font) -> object
        Set: Position(self: Font) = value
        """
        ...

    @property
    def Reflection(self) -> ReflectionFormat:
        """ Get: Reflection(self: Font) -> ReflectionFormat """
        ...

    @property
    def Scaling(self) -> object:
        """
        Get: Scaling(self: Font) -> object
        Set: Scaling(self: Font) = value
        """
        ...

    @property
    def Shadow(self): # -> MsoTriState
        """
        Get: Shadow(self: Font) -> MsoTriState
        Set: Shadow(self: Font) = value
        """
        ...

    @property
    def Size(self) -> object:
        """
        Get: Size(self: Font) -> object
        Set: Size(self: Font) = value
        """
        ...

    @property
    def SizeBi(self) -> object:
        """
        Get: SizeBi(self: Font) -> object
        Set: SizeBi(self: Font) = value
        """
        ...

    @property
    def SmallCaps(self): # -> MsoTriState
        """
        Get: SmallCaps(self: Font) -> MsoTriState
        Set: SmallCaps(self: Font) = value
        """
        ...

    @property
    def StrikeThrough(self): # -> MsoTriState
        """
        Get: StrikeThrough(self: Font) -> MsoTriState
        Set: StrikeThrough(self: Font) = value
        """
        ...

    @property
    def StylisticAlternates(self) -> object:
        """
        Get: StylisticAlternates(self: Font) -> object
        Set: StylisticAlternates(self: Font) = value
        """
        ...

    @property
    def StylisticSets(self) -> object:
        """
        Get: StylisticSets(self: Font) -> object
        Set: StylisticSets(self: Font) = value
        """
        ...

    @property
    def SubScript(self): # -> MsoTriState
        """
        Get: SubScript(self: Font) -> MsoTriState
        Set: SubScript(self: Font) = value
        """
        ...

    @property
    def SuperScript(self): # -> MsoTriState
        """
        Get: SuperScript(self: Font) -> MsoTriState
        Set: SuperScript(self: Font) = value
        """
        ...

    @property
    def Swash(self): # -> MsoTriState
        """
        Get: Swash(self: Font) -> MsoTriState
        Set: Swash(self: Font) = value
        """
        ...

    @property
    def TextShadow(self) -> ShadowFormat:
        """ Get: TextShadow(self: Font) -> ShadowFormat """
        ...

    @property
    def ThreeD(self) -> ThreeDFormat:
        """ Get: ThreeD(self: Font) -> ThreeDFormat """
        ...

    @property
    def Tracking(self) -> object:
        """
        Get: Tracking(self: Font) -> object
        Set: Tracking(self: Font) = value
        """
        ...

    @property
    def TrackingPreset(self) -> PbTrackingPresetType:
        """
        Get: TrackingPreset(self: Font) -> PbTrackingPresetType
        Set: TrackingPreset(self: Font) = value
        """
        ...

    @property
    def Underline(self) -> PbUnderlineType:
        """
        Get: Underline(self: Font) -> PbUnderlineType
        Set: Underline(self: Font) = value
        """
        ...

    @property
    def UseDiacriticColor(self): # -> MsoTriState
        """
        Get: UseDiacriticColor(self: Font) -> MsoTriState
        Set: UseDiacriticColor(self: Font) = value
        """
        ...


    def Duplicate(self) -> Font:
        """ Duplicate(self: Font) -> Font """
        ...

    def GetScriptName(self, Script:PbFontScriptType) -> str:
        """ GetScriptName(self: Font, Script: PbFontScriptType) -> str """
        ...

    def Grow(self): # -> 
        """ Grow(self: Font) """
        ...

    def Reset(self): # -> 
        """ Reset(self: Font) """
        ...

    def SetScriptName(self, Script:PbFontScriptType, FontName:str): # -> 
        """ SetScriptName(self: Font, Script: PbFontScriptType, FontName: str) """
        ...

    def Shrink(self): # -> 
        """ Shrink(self: Font) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class FreeformBuilder: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: FreeformBuilder) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: FreeformBuilder) -> object """
        ...


    def AddNodes(self, SegmentType, EditingType, X1:object, Y1:object, X2:object, Y2:object, X3:object, Y3:object): # ->  # Not found arg types: {'EditingType': 'MsoEditingType', 'SegmentType': 'MsoSegmentType'}
        """ AddNodes(self: FreeformBuilder, SegmentType: MsoSegmentType, EditingType: MsoEditingType, X1: object, Y1: object, X2: object, Y2: object, X3: object, Y3: object) """
        ...

    def ConvertToShape(self) -> Shape:
        """ ConvertToShape(self: FreeformBuilder) -> Shape """
        ...


class GlowFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Color(self) -> ColorFormat:
        """ Get: Color(self: GlowFormat) -> ColorFormat """
        ...

    @property
    def Radius(self) -> Single:
        """
        Get: Radius(self: GlowFormat) -> Single
        Set: Radius(self: GlowFormat) = value
        """
        ...

    @property
    def Transparency(self) -> Single:
        """
        Get: Transparency(self: GlowFormat) -> Single
        Set: Transparency(self: GlowFormat) = value
        """
        ...

    @property
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: GlowFormat) -> MsoTriState
        Set: Visible(self: GlowFormat) = value
        """
        ...



class GroupShapes(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: GroupShapes) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: GroupShapes) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: GroupShapes) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class HeaderFooter: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: HeaderFooter) -> Application """
        ...

    @property
    def IsHeader(self) -> bool:
        """ Get: IsHeader(self: HeaderFooter) -> bool """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: HeaderFooter) -> object """
        ...

    @property
    def TextRange(self) -> TextRange:
        """ Get: TextRange(self: HeaderFooter) -> TextRange """
        ...


    def Delete(self): # -> 
        """ Delete(self: HeaderFooter) """
        ...


class Hyperlink: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Address(self) -> str:
        """
        Get: Address(self: Hyperlink) -> str
        Set: Address(self: Hyperlink) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: Hyperlink) -> Application """
        ...

    @property
    def EmailSubject(self) -> str:
        """
        Get: EmailSubject(self: Hyperlink) -> str
        Set: EmailSubject(self: Hyperlink) = value
        """
        ...

    @property
    def PageID(self) -> int:
        """
        Get: PageID(self: Hyperlink) -> int
        Set: PageID(self: Hyperlink) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Hyperlink) -> object """
        ...

    @property
    def Range(self) -> TextRange:
        """ Get: Range(self: Hyperlink) -> TextRange """
        ...

    @property
    def Shape(self) -> Shape:
        """ Get: Shape(self: Hyperlink) -> Shape """
        ...

    @property
    def TargetType(self) -> PbHlinkTargetType:
        """ Get: TargetType(self: Hyperlink) -> PbHlinkTargetType """
        ...

    @property
    def TextToDisplay(self) -> str:
        """
        Get: TextToDisplay(self: Hyperlink) -> str
        Set: TextToDisplay(self: Hyperlink) = value
        """
        ...

    @property
    def Type(self): # -> MsoHyperlinkType
        """ Get: Type(self: Hyperlink) -> MsoHyperlinkType """
        ...


    def Delete(self): # -> 
        """ Delete(self: Hyperlink) """
        ...

    def Move(self, NewIndex:int): # -> 
        """ Move(self: Hyperlink, NewIndex: int) """
        ...

    def SetPageRelative(self, RelativePage:PbHlinkTargetType): # -> 
        """ SetPageRelative(self: Hyperlink, RelativePage: PbHlinkTargetType) """
        ...


class Hyperlinks(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Hyperlinks) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Hyperlinks) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Hyperlinks) -> object """
        ...


    def Add(self, Text:TextRange, Address:str, RelativePage:PbHlinkTargetType, PageID:int, TextToDisplay:str) -> Hyperlink:
        """ Add(self: Hyperlinks, Text: TextRange, Address: str, RelativePage: PbHlinkTargetType, PageID: int, TextToDisplay: str) -> Hyperlink """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IApplicationEvents: # skipped bases: <type 'object'>
    """ no doc """
    def AfterPrint(self, Doc:Document): # -> 
        """ AfterPrint(self: IApplicationEvents, Doc: Document) """
        ...

    def BeforePrint(self, Doc, Cancel) -> bool:
        """ BeforePrint(self: IApplicationEvents, Doc: Document) -> bool """
        ...

    def DocumentBeforeClose(self, Doc, Cancel) -> bool:
        """ DocumentBeforeClose(self: IApplicationEvents, Doc: Document) -> bool """
        ...

    def DocumentOpen(self, Doc:Document): # -> 
        """ DocumentOpen(self: IApplicationEvents, Doc: Document) """
        ...

    def HideCatalogUI(self): # -> 
        """ HideCatalogUI(self: IApplicationEvents) """
        ...

    def MailMergeAfterMerge(self, Doc:Document): # -> 
        """ MailMergeAfterMerge(self: IApplicationEvents, Doc: Document) """
        ...

    def MailMergeAfterRecordMerge(self, Doc:Document): # -> 
        """ MailMergeAfterRecordMerge(self: IApplicationEvents, Doc: Document) """
        ...

    def MailMergeBeforeMerge(self, Doc, StartRecord, EndRecord, Cancel) -> bool:
        """ MailMergeBeforeMerge(self: IApplicationEvents, Doc: Document, StartRecord: int, EndRecord: int) -> bool """
        ...

    def MailMergeBeforeRecordMerge(self, Doc, Cancel) -> bool:
        """ MailMergeBeforeRecordMerge(self: IApplicationEvents, Doc: Document) -> bool """
        ...

    def MailMergeDataSourceLoad(self, Doc:Document): # -> 
        """ MailMergeDataSourceLoad(self: IApplicationEvents, Doc: Document) """
        ...

    def MailMergeDataSourceValidate(self, Doc, Handled) -> bool:
        """ MailMergeDataSourceValidate(self: IApplicationEvents, Doc: Document) -> bool """
        ...

    def MailMergeGenerateBarcode(self, Doc, bstrString) -> str:
        """ MailMergeGenerateBarcode(self: IApplicationEvents, Doc: Document) -> str """
        ...

    def MailMergeInsertBarcode(self, Doc, OkToInsert) -> bool:
        """ MailMergeInsertBarcode(self: IApplicationEvents, Doc: Document) -> bool """
        ...

    def MailMergeRecipientListClose(self, Doc:Document): # -> 
        """ MailMergeRecipientListClose(self: IApplicationEvents, Doc: Document) """
        ...

    def MailMergeWizardFollowUpCustom(self, Doc:Document): # -> 
        """ MailMergeWizardFollowUpCustom(self: IApplicationEvents, Doc: Document) """
        ...

    def MailMergeWizardSendToCustom(self, Doc:Document): # -> 
        """ MailMergeWizardSendToCustom(self: IApplicationEvents, Doc: Document) """
        ...

    def MailMergeWizardStateChange(self, Doc:Document, FromState:int): # -> 
        """ MailMergeWizardStateChange(self: IApplicationEvents, Doc: Document, FromState: int) """
        ...

    def NewDocument(self, Doc:Document): # -> 
        """ NewDocument(self: IApplicationEvents, Doc: Document) """
        ...

    def Quit(self): # -> 
        """ Quit(self: IApplicationEvents) """
        ...

    def ShowCatalogUI(self): # -> 
        """ ShowCatalogUI(self: IApplicationEvents) """
        ...

    def WindowActivate(self, Wn:Window): # -> 
        """ WindowActivate(self: IApplicationEvents, Wn: Window) """
        ...

    def WindowDeactivate(self, Wn:Window): # -> 
        """ WindowDeactivate(self: IApplicationEvents, Wn: Window) """
        ...

    def WindowPageChange(self, Vw:View): # -> 
        """ WindowPageChange(self: IApplicationEvents, Vw: View) """
        ...


class ICagNotifySink: # skipped bases: <type 'object'>
    """ no doc """
    def InsertClip(self, pClipMoniker:object, pItemMoniker:object) -> int:
        """ InsertClip(self: ICagNotifySink, pClipMoniker: object, pItemMoniker: object) -> int """
        ...

    def WindowIsClosing(self) -> int:
        """ WindowIsClosing(self: ICagNotifySink) -> int """
        ...


class IDocumentEvents: # skipped bases: <type 'object'>
    """ no doc """
    def BeforeClose(self, Cancel) -> bool:
        """ BeforeClose(self: IDocumentEvents) -> bool """
        ...

    def Open(self): # -> 
        """ Open(self: IDocumentEvents) """
        ...

    def Redo(self): # -> 
        """ Redo(self: IDocumentEvents) """
        ...

    def ShapesAdded(self): # -> 
        """ ShapesAdded(self: IDocumentEvents) """
        ...

    def ShapesRemoved(self): # -> 
        """ ShapesRemoved(self: IDocumentEvents) """
        ...

    def Undo(self): # -> 
        """ Undo(self: IDocumentEvents) """
        ...

    def WizardAfterChange(self): # -> 
        """ WizardAfterChange(self: IDocumentEvents) """
        ...


class InlineShapes(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: InlineShapes) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: InlineShapes) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: InlineShapes) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class InstalledPrinters(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: InstalledPrinters) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: InstalledPrinters) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: InstalledPrinters) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Label: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Label) -> Application """
        ...

    @property
    def Height(self) -> object:
        """ Get: Height(self: Label) -> object """
        ...

    @property
    def HorizontalGap(self) -> object:
        """
        Get: HorizontalGap(self: Label) -> object
        Set: HorizontalGap(self: Label) = value
        """
        ...

    @property
    def LeftMargin(self) -> object:
        """
        Get: LeftMargin(self: Label) -> object
        Set: LeftMargin(self: Label) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Label) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Label) -> object """
        ...

    @property
    def TopMargin(self) -> object:
        """
        Get: TopMargin(self: Label) -> object
        Set: TopMargin(self: Label) = value
        """
        ...

    @property
    def VerticalGap(self) -> object:
        """
        Get: VerticalGap(self: Label) -> object
        Set: VerticalGap(self: Label) = value
        """
        ...

    @property
    def Width(self) -> object:
        """ Get: Width(self: Label) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Labels(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Labels) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Labels) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Labels) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class LayoutGuides: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: LayoutGuides) -> Application """
        ...

    @property
    def ColumnGutterWidth(self) -> Single:
        """
        Get: ColumnGutterWidth(self: LayoutGuides) -> Single
        Set: ColumnGutterWidth(self: LayoutGuides) = value
        """
        ...

    @property
    def Columns(self) -> int:
        """
        Get: Columns(self: LayoutGuides) -> int
        Set: Columns(self: LayoutGuides) = value
        """
        ...

    @property
    def GutterCenterlines(self) -> bool:
        """
        Get: GutterCenterlines(self: LayoutGuides) -> bool
        Set: GutterCenterlines(self: LayoutGuides) = value
        """
        ...

    @property
    def HorizontalBaseLineOffset(self) -> Single:
        """
        Get: HorizontalBaseLineOffset(self: LayoutGuides) -> Single
        Set: HorizontalBaseLineOffset(self: LayoutGuides) = value
        """
        ...

    @property
    def HorizontalBaseLineSpacing(self) -> Single:
        """
        Get: HorizontalBaseLineSpacing(self: LayoutGuides) -> Single
        Set: HorizontalBaseLineSpacing(self: LayoutGuides) = value
        """
        ...

    @property
    def MarginBottom(self) -> object:
        """
        Get: MarginBottom(self: LayoutGuides) -> object
        Set: MarginBottom(self: LayoutGuides) = value
        """
        ...

    @property
    def MarginLeft(self) -> object:
        """
        Get: MarginLeft(self: LayoutGuides) -> object
        Set: MarginLeft(self: LayoutGuides) = value
        """
        ...

    @property
    def MarginRight(self) -> object:
        """
        Get: MarginRight(self: LayoutGuides) -> object
        Set: MarginRight(self: LayoutGuides) = value
        """
        ...

    @property
    def MarginTop(self) -> object:
        """
        Get: MarginTop(self: LayoutGuides) -> object
        Set: MarginTop(self: LayoutGuides) = value
        """
        ...

    @property
    def MirrorGuides(self) -> bool:
        """
        Get: MirrorGuides(self: LayoutGuides) -> bool
        Set: MirrorGuides(self: LayoutGuides) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: LayoutGuides) -> object """
        ...

    @property
    def RowGutterWidth(self) -> Single:
        """
        Get: RowGutterWidth(self: LayoutGuides) -> Single
        Set: RowGutterWidth(self: LayoutGuides) = value
        """
        ...

    @property
    def Rows(self) -> int:
        """
        Get: Rows(self: LayoutGuides) -> int
        Set: Rows(self: LayoutGuides) = value
        """
        ...

    @property
    def VerticalBaseLineOffset(self) -> Single:
        """
        Get: VerticalBaseLineOffset(self: LayoutGuides) -> Single
        Set: VerticalBaseLineOffset(self: LayoutGuides) = value
        """
        ...

    @property
    def VerticalBaseLineSpacing(self) -> Single:
        """
        Get: VerticalBaseLineSpacing(self: LayoutGuides) -> Single
        Set: VerticalBaseLineSpacing(self: LayoutGuides) = value
        """
        ...



class LineFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: LineFormat) -> Application """
        ...

    @property
    def BackColor(self) -> ColorFormat:
        """
        Get: BackColor(self: LineFormat) -> ColorFormat
        Set: BackColor(self: LineFormat) = value
        """
        ...

    @property
    def BeginArrowheadLength(self): # -> MsoArrowheadLength
        """
        Get: BeginArrowheadLength(self: LineFormat) -> MsoArrowheadLength
        Set: BeginArrowheadLength(self: LineFormat) = value
        """
        ...

    @property
    def BeginArrowheadStyle(self): # -> MsoArrowheadStyle
        """
        Get: BeginArrowheadStyle(self: LineFormat) -> MsoArrowheadStyle
        Set: BeginArrowheadStyle(self: LineFormat) = value
        """
        ...

    @property
    def BeginArrowheadWidth(self): # -> MsoArrowheadWidth
        """
        Get: BeginArrowheadWidth(self: LineFormat) -> MsoArrowheadWidth
        Set: BeginArrowheadWidth(self: LineFormat) = value
        """
        ...

    @property
    def CapStyle(self): # -> MsoLineCapStyle
        """
        Get: CapStyle(self: LineFormat) -> MsoLineCapStyle
        Set: CapStyle(self: LineFormat) = value
        """
        ...

    @property
    def DashStyle(self): # -> MsoLineDashStyle
        """
        Get: DashStyle(self: LineFormat) -> MsoLineDashStyle
        Set: DashStyle(self: LineFormat) = value
        """
        ...

    @property
    def EndArrowheadLength(self): # -> MsoArrowheadLength
        """
        Get: EndArrowheadLength(self: LineFormat) -> MsoArrowheadLength
        Set: EndArrowheadLength(self: LineFormat) = value
        """
        ...

    @property
    def EndArrowheadStyle(self): # -> MsoArrowheadStyle
        """
        Get: EndArrowheadStyle(self: LineFormat) -> MsoArrowheadStyle
        Set: EndArrowheadStyle(self: LineFormat) = value
        """
        ...

    @property
    def EndArrowheadWidth(self): # -> MsoArrowheadWidth
        """
        Get: EndArrowheadWidth(self: LineFormat) -> MsoArrowheadWidth
        Set: EndArrowheadWidth(self: LineFormat) = value
        """
        ...

    @property
    def ForeColor(self) -> ColorFormat:
        """
        Get: ForeColor(self: LineFormat) -> ColorFormat
        Set: ForeColor(self: LineFormat) = value
        """
        ...

    @property
    def GradientAngle(self) -> Single:
        """
        Get: GradientAngle(self: LineFormat) -> Single
        Set: GradientAngle(self: LineFormat) = value
        """
        ...

    @property
    def GradientColorType(self): # -> MsoGradientColorType
        """ Get: GradientColorType(self: LineFormat) -> MsoGradientColorType """
        ...

    @property
    def GradientStyle(self): # -> MsoGradientStyle
        """ Get: GradientStyle(self: LineFormat) -> MsoGradientStyle """
        ...

    @property
    def GradientVariant(self) -> int:
        """ Get: GradientVariant(self: LineFormat) -> int """
        ...

    @property
    def InsetPen(self): # -> MsoTriState
        """
        Get: InsetPen(self: LineFormat) -> MsoTriState
        Set: InsetPen(self: LineFormat) = value
        """
        ...

    @property
    def JoinStyle(self): # -> MsoLineJoinStyle
        """
        Get: JoinStyle(self: LineFormat) -> MsoLineJoinStyle
        Set: JoinStyle(self: LineFormat) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: LineFormat) -> object """
        ...

    @property
    def Pattern(self): # -> MsoPatternType
        """
        Get: Pattern(self: LineFormat) -> MsoPatternType
        Set: Pattern(self: LineFormat) = value
        """
        ...

    @property
    def PresetGradientType(self): # -> MsoPresetGradientType
        """ Get: PresetGradientType(self: LineFormat) -> MsoPresetGradientType """
        ...

    @property
    def Style(self): # -> MsoLineStyle
        """
        Get: Style(self: LineFormat) -> MsoLineStyle
        Set: Style(self: LineFormat) = value
        """
        ...

    @property
    def Transparency(self) -> Single:
        """
        Get: Transparency(self: LineFormat) -> Single
        Set: Transparency(self: LineFormat) = value
        """
        ...

    @property
    def Type(self): # -> MsoLineFillType
        """ Get: Type(self: LineFormat) -> MsoLineFillType """
        ...

    @property
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: LineFormat) -> MsoTriState
        Set: Visible(self: LineFormat) = value
        """
        ...

    @property
    def Weight(self) -> object:
        """
        Get: Weight(self: LineFormat) -> object
        Set: Weight(self: LineFormat) = value
        """
        ...


    def PresetGradient(self, Style, Variant:int, PresetGradientType): # ->  # Not found arg types: {'Style': 'MsoGradientStyle', 'PresetGradientType': 'MsoPresetGradientType'}
        """ PresetGradient(self: LineFormat, Style: MsoGradientStyle, Variant: int, PresetGradientType: MsoPresetGradientType) """
        ...


class LinkFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: LinkFormat) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: LinkFormat) -> object """
        ...

    @property
    def SourceFullName(self) -> str:
        """ Get: SourceFullName(self: LinkFormat) -> str """
        ...


    def Update(self): # -> 
        """ Update(self: LinkFormat) """
        ...


class MailMerge: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: MailMerge) -> Application """
        ...

    @property
    def DataSource(self) -> MailMergeDataSource:
        """ Get: DataSource(self: MailMerge) -> MailMergeDataSource """
        ...

    @property
    def Destination(self) -> int:
        """ Get: Destination(self: MailMerge) -> int """
        ...

    @property
    def DocumentUpdating(self) -> bool:
        """
        Get: DocumentUpdating(self: MailMerge) -> bool
        Set: DocumentUpdating(self: MailMerge) = value
        """
        ...

    @property
    def EmailMergeEnvelope(self) -> EmailMergeEnvelope:
        """ Get: EmailMergeEnvelope(self: MailMerge) -> EmailMergeEnvelope """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: MailMerge) -> object """
        ...

    @property
    def ShowSendToCustom(self) -> str:
        """
        Get: ShowSendToCustom(self: MailMerge) -> str
        Set: ShowSendToCustom(self: MailMerge) = value
        """
        ...

    @property
    def SuppressBlankLines(self) -> bool:
        """
        Get: SuppressBlankLines(self: MailMerge) -> bool
        Set: SuppressBlankLines(self: MailMerge) = value
        """
        ...

    @property
    def Type(self) -> PbMergeType:
        """
        Get: Type(self: MailMerge) -> PbMergeType
        Set: Type(self: MailMerge) = value
        """
        ...

    @property
    def ViewMailMergeFieldCodes(self) -> bool:
        """
        Get: ViewMailMergeFieldCodes(self: MailMerge) -> bool
        Set: ViewMailMergeFieldCodes(self: MailMerge) = value
        """
        ...

    @property
    def WizardState(self) -> int:
        """
        Get: WizardState(self: MailMerge) -> int
        Set: WizardState(self: MailMerge) = value
        """
        ...


    def CreateShortcut(self, Filename:str): # -> 
        """ CreateShortcut(self: MailMerge, Filename: str) """
        ...

    def Execute(self, Pause:bool, Destination:PbMailMergeDestination, Filename:str) -> Document:
        """ Execute(self: MailMerge, Pause: bool, Destination: PbMailMergeDestination, Filename: str) -> Document """
        ...

    def Execute10(self, Pause:bool): # -> 
        """ Execute10(self: MailMerge, Pause: bool) """
        ...

    def ExportRecipientList(self, Filename:str, FileType:PbRecipientListFileType, IncludedOnly:bool): # -> 
        """ ExportRecipientList(self: MailMerge, Filename: str, FileType: PbRecipientListFileType, IncludedOnly: bool) """
        ...

    def OpenDataSource(self, bstrDataSource:str, bstrConnect:str, bstrTable:str, fOpenExclusive:int, fNeverPrompt:int): # -> 
        """ OpenDataSource(self: MailMerge, bstrDataSource: str, bstrConnect: str, bstrTable: str, fOpenExclusive: int, fNeverPrompt: int) """
        ...

    def ShowWizard(self, ShowDocumentStep:bool, ShowTemplateStep:bool, ShowDataStep:bool, ShowWriteStep:bool, ShowPreviewStep:bool, ShowMergeStep:bool): # -> 
        """ ShowWizard(self: MailMerge, ShowDocumentStep: bool, ShowTemplateStep: bool, ShowDataStep: bool, ShowWriteStep: bool, ShowPreviewStep: bool, ShowMergeStep: bool) """
        ...

    def ShowWizardEx(self, ShowDocumentStep:bool, ShowTemplateStep:bool, ShowDataStep:bool, ShowWriteStep:bool, ShowPreviewStep:bool, ShowMergeStep:bool, MergeType:PbMergeType, iStep:int): # -> 
        """ ShowWizardEx(self: MailMerge, ShowDocumentStep: bool, ShowTemplateStep: bool, ShowDataStep: bool, ShowWriteStep: bool, ShowPreviewStep: bool, ShowMergeStep: bool, MergeType: PbMergeType, iStep: int) """
        ...


class MailMergeDataField(_IMsoDispObj): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def FieldType(self) -> PbMailMergeDataFieldType:
        """
        Get: FieldType(self: MailMergeDataField) -> PbMailMergeDataFieldType
        Set: FieldType(self: MailMergeDataField) = value
        """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: MailMergeDataField) -> int """
        ...

    @property
    def IsMapped(self) -> bool:
        """ Get: IsMapped(self: MailMergeDataField) -> bool """
        ...

    @property
    def MappedTo(self) -> str:
        """ Get: MappedTo(self: MailMergeDataField) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MailMergeDataField) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: MailMergeDataField) -> object """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: MailMergeDataField) -> str """
        ...


    def AddToRecipientFields(self): # -> 
        """ AddToRecipientFields(self: MailMergeDataField) """
        ...

    def Insert(self, Range:TextRange) -> Shape:
        """ Insert(self: MailMergeDataField, Range: TextRange) -> Shape """
        ...

    def MapToRecipientField(self, bstrValue:str): # -> 
        """ MapToRecipientField(self: MailMergeDataField, bstrValue: str) """
        ...

    def UnMapRecipientField(self): # -> 
        """ UnMapRecipientField(self: MailMergeDataField) """
        ...


class MailMergeDataFields(IEnumerable, _IMsoDispObj): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: MailMergeDataFields) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: MailMergeDataFields) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class MailMergeDataSource: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActiveRecord(self) -> int:
        """
        Get: ActiveRecord(self: MailMergeDataSource) -> int
        Set: ActiveRecord(self: MailMergeDataSource) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: MailMergeDataSource) -> Application """
        ...

    @property
    def ConnectString(self) -> str:
        """ Get: ConnectString(self: MailMergeDataSource) -> str """
        ...

    @property
    def DataFields(self) -> MailMergeDataFields:
        """ Get: DataFields(self: MailMergeDataSource) -> MailMergeDataFields """
        ...

    @property
    def DataSources(self) -> MailMergeDataSources:
        """ Get: DataSources(self: MailMergeDataSource) -> MailMergeDataSources """
        ...

    @property
    def EverValidated(self) -> bool:
        """
        Get: EverValidated(self: MailMergeDataSource) -> bool
        Set: EverValidated(self: MailMergeDataSource) = value
        """
        ...

    @property
    def Filters(self) -> MailMergeFilters:
        """ Get: Filters(self: MailMergeDataSource) -> MailMergeFilters """
        ...

    @property
    def FirstRecord(self) -> int:
        """
        Get: FirstRecord(self: MailMergeDataSource) -> int
        Set: FirstRecord(self: MailMergeDataSource) = value
        """
        ...

    @property
    def Included(self) -> bool:
        """
        Get: Included(self: MailMergeDataSource) -> bool
        Set: Included(self: MailMergeDataSource) = value
        """
        ...

    @property
    def InvalidAddress(self) -> bool:
        """
        Get: InvalidAddress(self: MailMergeDataSource) -> bool
        Set: InvalidAddress(self: MailMergeDataSource) = value
        """
        ...

    @property
    def InvalidComments(self) -> str:
        """
        Get: InvalidComments(self: MailMergeDataSource) -> str
        Set: InvalidComments(self: MailMergeDataSource) = value
        """
        ...

    @property
    def IsMaster(self) -> bool:
        """ Get: IsMaster(self: MailMergeDataSource) -> bool """
        ...

    @property
    def LastRecord(self) -> int:
        """
        Get: LastRecord(self: MailMergeDataSource) -> int
        Set: LastRecord(self: MailMergeDataSource) = value
        """
        ...

    @property
    def MappedDataFields(self) -> MailMergeMappedDataFields:
        """ Get: MappedDataFields(self: MailMergeDataSource) -> MailMergeMappedDataFields """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MailMergeDataSource) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: MailMergeDataSource) -> object """
        ...

    @property
    def RecordCount(self) -> int:
        """ Get: RecordCount(self: MailMergeDataSource) -> int """
        ...

    @property
    def TableName(self) -> str:
        """ Get: TableName(self: MailMergeDataSource) -> str """
        ...

    @property
    def Type(self) -> int:
        """ Get: Type(self: MailMergeDataSource) -> int """
        ...

    @property
    def ValidatedClean(self) -> bool:
        """
        Get: ValidatedClean(self: MailMergeDataSource) -> bool
        Set: ValidatedClean(self: MailMergeDataSource) = value
        """
        ...


    def ApplyFilter(self): # -> 
        """ ApplyFilter(self: MailMergeDataSource) """
        ...

    def Close(self): # -> 
        """ Close(self: MailMergeDataSource) """
        ...

    def EditRecord(self, lRec:int, varField:object, Value:object): # -> 
        """ EditRecord(self: MailMergeDataSource, lRec: int, varField: object, Value: object) """
        ...

    def FindRecord(self, FindText:str, Field:str) -> bool:
        """ FindRecord(self: MailMergeDataSource, FindText: str, Field: str) -> bool """
        ...

    def OpenRecipientsDialog(self): # -> 
        """ OpenRecipientsDialog(self: MailMergeDataSource) """
        ...

    def SetAllErrorFlags(self, Invalid:bool, InvalidComment:str): # -> 
        """ SetAllErrorFlags(self: MailMergeDataSource, Invalid: bool, InvalidComment: str) """
        ...

    def SetAllIncludedFlags(self, Included:bool): # -> 
        """ SetAllIncludedFlags(self: MailMergeDataSource, Included: bool) """
        ...

    def SetSortOrder(self, SortField1:str, SortAscending1:bool, SortField2:str, SortAscending2:bool, SortField3:str, SortAscending3:bool): # -> 
        """ SetSortOrder(self: MailMergeDataSource, SortField1: str, SortAscending1: bool, SortField2: str, SortAscending2: bool, SortField3: str, SortAscending3: bool) """
        ...


class MailMergeDataSources(_IMsoDispObj): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: MailMergeDataSources) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: MailMergeDataSources) -> object """
        ...


    def Item(self, varIndex:object) -> MailMergeDataSource:
        """ Item(self: MailMergeDataSources, varIndex: object) -> MailMergeDataSource """
        ...


class MailMergeFilterCriterion(_IMsoDispObj): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Column(self) -> str:
        """
        Get: Column(self: MailMergeFilterCriterion) -> str
        Set: Column(self: MailMergeFilterCriterion) = value
        """
        ...

    @property
    def CompareTo(self) -> str:
        """
        Get: CompareTo(self: MailMergeFilterCriterion) -> str
        Set: CompareTo(self: MailMergeFilterCriterion) = value
        """
        ...

    @property
    def Comparison(self): # -> MsoFilterComparison
        """
        Get: Comparison(self: MailMergeFilterCriterion) -> MsoFilterComparison
        Set: Comparison(self: MailMergeFilterCriterion) = value
        """
        ...

    @property
    def Conjunction(self): # -> MsoFilterConjunction
        """
        Get: Conjunction(self: MailMergeFilterCriterion) -> MsoFilterConjunction
        Set: Conjunction(self: MailMergeFilterCriterion) = value
        """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: MailMergeFilterCriterion) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: MailMergeFilterCriterion) -> object """
        ...



class MailMergeFilters(IEnumerable, _IMsoDispObj): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: MailMergeFilters) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: MailMergeFilters) -> object """
        ...


    def Add(self, Column:str, Comparison, Conjunction, bstrCompareTo:str, DeferUpdate:bool): # ->  # Not found arg types: {'Comparison': 'MsoFilterComparison', 'Conjunction': 'MsoFilterConjunction'}
        """ Add(self: MailMergeFilters, Column: str, Comparison: MsoFilterComparison, Conjunction: MsoFilterConjunction, bstrCompareTo: str, DeferUpdate: bool) """
        ...

    def Delete(self, Index:int, DeferUpdate:bool): # -> 
        """ Delete(self: MailMergeFilters, Index: int, DeferUpdate: bool) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class MailMergeMappedDataField: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: MailMergeMappedDataField) -> Application """
        ...

    @property
    def DataFieldName(self) -> str:
        """ Get: DataFieldName(self: MailMergeMappedDataField) -> str """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: MailMergeMappedDataField) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MailMergeMappedDataField) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: MailMergeMappedDataField) -> object """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: MailMergeMappedDataField) -> str """
        ...



class MailMergeMappedDataFields(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: MailMergeMappedDataFields) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: MailMergeMappedDataFields) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: MailMergeMappedDataFields) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class MasterPages(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: MasterPages) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: MasterPages) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: MasterPages) -> object """
        ...


    def Add(self, IsTwoPageMaster:bool, Abbreviation:str, Description:str) -> Page:
        """ Add(self: MasterPages, IsTwoPageMaster: bool, Abbreviation: str, Description: str) -> Page """
        ...

    def FindByPageID(self, PageID:int) -> Page:
        """ FindByPageID(self: MasterPages, PageID: int) -> Page """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ModalBrowser: # skipped bases: <type 'object'>
    """ no doc """
    def MoveTo(self, lx:int, ly:int): # -> 
        """ MoveTo(self: ModalBrowser, lx: int, ly: int) """
        ...

    def ResizeTo(self, lWidth:int, lHeight:int): # -> 
        """ ResizeTo(self: ModalBrowser, lWidth: int, lHeight: int) """
        ...

    def TaskCompleted(self): # -> 
        """ TaskCompleted(self: ModalBrowser) """
        ...


class ObjectVerbs(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ObjectVerbs) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ObjectVerbs) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ObjectVerbs) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class OLEFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: OLEFormat) -> Application """
        ...

    @property
    def Object(self) -> object:
        """ Get: Object(self: OLEFormat) -> object """
        ...

    @property
    def ObjectVerbs(self) -> ObjectVerbs:
        """ Get: ObjectVerbs(self: OLEFormat) -> ObjectVerbs """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: OLEFormat) -> object """
        ...

    @property
    def ProgId(self) -> str:
        """ Get: ProgId(self: OLEFormat) -> str """
        ...


    def Activate(self): # -> 
        """ Activate(self: OLEFormat) """
        ...

    def DoVerb(self, iVerb:int): # -> 
        """ DoVerb(self: OLEFormat, iVerb: int) """
        ...


class Options: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AddHebDoubleQuote(self) -> bool:
        """
        Get: AddHebDoubleQuote(self: Options) -> bool
        Set: AddHebDoubleQuote(self: Options) = value
        """
        ...

    @property
    def AllowBackgroundSave(self) -> bool:
        """
        Get: AllowBackgroundSave(self: Options) -> bool
        Set: AllowBackgroundSave(self: Options) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: Options) -> Application """
        ...

    @property
    def AutoFormatWord(self) -> bool:
        """
        Get: AutoFormatWord(self: Options) -> bool
        Set: AutoFormatWord(self: Options) = value
        """
        ...

    @property
    def AutoHyphenate(self) -> bool:
        """
        Get: AutoHyphenate(self: Options) -> bool
        Set: AutoHyphenate(self: Options) = value
        """
        ...

    @property
    def AutoKeyboardSwitching(self) -> bool:
        """
        Get: AutoKeyboardSwitching(self: Options) -> bool
        Set: AutoKeyboardSwitching(self: Options) = value
        """
        ...

    @property
    def AutoSelectWord(self) -> bool:
        """
        Get: AutoSelectWord(self: Options) -> bool
        Set: AutoSelectWord(self: Options) = value
        """
        ...

    @property
    def DefaultPubDirection(self) -> PbDirectionType:
        """
        Get: DefaultPubDirection(self: Options) -> PbDirectionType
        Set: DefaultPubDirection(self: Options) = value
        """
        ...

    @property
    def DefaultTextFlowDirection(self) -> PbDirectionType:
        """
        Get: DefaultTextFlowDirection(self: Options) -> PbDirectionType
        Set: DefaultTextFlowDirection(self: Options) = value
        """
        ...

    @property
    def DisplayPrintTroubleshooter(self) -> bool:
        """
        Get: DisplayPrintTroubleshooter(self: Options) -> bool
        Set: DisplayPrintTroubleshooter(self: Options) = value
        """
        ...

    @property
    def DisplayStatusBar(self) -> bool:
        """
        Get: DisplayStatusBar(self: Options) -> bool
        Set: DisplayStatusBar(self: Options) = value
        """
        ...

    @property
    def DragAndDropText(self) -> bool:
        """
        Get: DragAndDropText(self: Options) -> bool
        Set: DragAndDropText(self: Options) = value
        """
        ...

    @property
    def EnvelopePrintOrientation(self) -> PbOrientationType:
        """
        Get: EnvelopePrintOrientation(self: Options) -> PbOrientationType
        Set: EnvelopePrintOrientation(self: Options) = value
        """
        ...

    @property
    def EnvelopePrintPlacement(self) -> PbPlacementType:
        """
        Get: EnvelopePrintPlacement(self: Options) -> PbPlacementType
        Set: EnvelopePrintPlacement(self: Options) = value
        """
        ...

    @property
    def HyphenationZone(self) -> object:
        """
        Get: HyphenationZone(self: Options) -> object
        Set: HyphenationZone(self: Options) = value
        """
        ...

    @property
    def MeasurementUnit(self) -> PbUnitType:
        """
        Get: MeasurementUnit(self: Options) -> PbUnitType
        Set: MeasurementUnit(self: Options) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Options) -> object """
        ...

    @property
    def PathForPictures(self) -> str:
        """
        Get: PathForPictures(self: Options) -> str
        Set: PathForPictures(self: Options) = value
        """
        ...

    @property
    def PathForPublications(self) -> str:
        """
        Get: PathForPublications(self: Options) -> str
        Set: PathForPublications(self: Options) = value
        """
        ...

    @property
    def PrintLineByLine(self) -> bool:
        """
        Get: PrintLineByLine(self: Options) -> bool
        Set: PrintLineByLine(self: Options) = value
        """
        ...

    @property
    def SaveAutoRecoverInfo(self) -> bool:
        """
        Get: SaveAutoRecoverInfo(self: Options) -> bool
        Set: SaveAutoRecoverInfo(self: Options) = value
        """
        ...

    @property
    def SaveAutoRecoverInfoInterval(self) -> int:
        """
        Get: SaveAutoRecoverInfoInterval(self: Options) -> int
        Set: SaveAutoRecoverInfoInterval(self: Options) = value
        """
        ...

    @property
    def SequenceCheck(self) -> bool:
        """
        Get: SequenceCheck(self: Options) -> bool
        Set: SequenceCheck(self: Options) = value
        """
        ...

    @property
    def ShowBasicColors(self) -> bool:
        """
        Get: ShowBasicColors(self: Options) -> bool
        Set: ShowBasicColors(self: Options) = value
        """
        ...

    @property
    def ShowScreenTipsOnObjects(self) -> bool:
        """
        Get: ShowScreenTipsOnObjects(self: Options) -> bool
        Set: ShowScreenTipsOnObjects(self: Options) = value
        """
        ...

    @property
    def ShowTipPages(self) -> bool:
        """
        Get: ShowTipPages(self: Options) -> bool
        Set: ShowTipPages(self: Options) = value
        """
        ...

    @property
    def TypeNReplace(self) -> bool:
        """
        Get: TypeNReplace(self: Options) -> bool
        Set: TypeNReplace(self: Options) = value
        """
        ...

    @property
    def UpdatePersonalInfoOnSave(self) -> bool:
        """
        Get: UpdatePersonalInfoOnSave(self: Options) -> bool
        Set: UpdatePersonalInfoOnSave(self: Options) = value
        """
        ...

    @property
    def UseCatalogAtStartup(self) -> bool:
        """
        Get: UseCatalogAtStartup(self: Options) -> bool
        Set: UseCatalogAtStartup(self: Options) = value
        """
        ...

    @property
    def UseEnvelopePaperSizes(self) -> bool:
        """
        Get: UseEnvelopePaperSizes(self: Options) -> bool
        Set: UseEnvelopePaperSizes(self: Options) = value
        """
        ...

    @property
    def UseEnvelopePrintOptions(self) -> bool:
        """
        Get: UseEnvelopePrintOptions(self: Options) -> bool
        Set: UseEnvelopePrintOptions(self: Options) = value
        """
        ...

    @property
    def UseHelpfulMousePointers(self) -> bool:
        """
        Get: UseHelpfulMousePointers(self: Options) -> bool
        Set: UseHelpfulMousePointers(self: Options) = value
        """
        ...

    @property
    def UseWizardForBlankPublication(self) -> bool:
        """
        Get: UseWizardForBlankPublication(self: Options) -> bool
        Set: UseWizardForBlankPublication(self: Options) = value
        """
        ...


    def ResetTips(self): # -> 
        """ ResetTips(self: Options) """
        ...

    def ResetWizardSynchronizing(self): # -> 
        """ ResetWizardSynchronizing(self: Options) """
        ...


class Page: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Page) -> Application """
        ...

    @property
    def Background(self) -> PageBackground:
        """ Get: Background(self: Page) -> PageBackground """
        ...

    @property
    def Footer(self) -> HeaderFooter:
        """ Get: Footer(self: Page) -> HeaderFooter """
        ...

    @property
    def Header(self) -> HeaderFooter:
        """ Get: Header(self: Page) -> HeaderFooter """
        ...

    @property
    def Height(self) -> int:
        """ Get: Height(self: Page) -> int """
        ...

    @property
    def IgnoreMaster(self) -> bool:
        """
        Get: IgnoreMaster(self: Page) -> bool
        Set: IgnoreMaster(self: Page) = value
        """
        ...

    @property
    def IsLeading(self) -> bool:
        """ Get: IsLeading(self: Page) -> bool """
        ...

    @property
    def IsTrailing(self) -> bool:
        """ Get: IsTrailing(self: Page) -> bool """
        ...

    @property
    def IsTwoPageMaster(self) -> bool:
        """
        Get: IsTwoPageMaster(self: Page) -> bool
        Set: IsTwoPageMaster(self: Page) = value
        """
        ...

    @property
    def IsWizardPage(self) -> bool:
        """ Get: IsWizardPage(self: Page) -> bool """
        ...

    @property
    def LayoutGuides(self) -> LayoutGuides:
        """ Get: LayoutGuides(self: Page) -> LayoutGuides """
        ...

    @property
    def Master(self) -> Page:
        """
        Get: Master(self: Page) -> Page
        Set: Master(self: Page) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Page) -> str
        Set: Name(self: Page) = value
        """
        ...

    @property
    def PageID(self) -> int:
        """ Get: PageID(self: Page) -> int """
        ...

    @property
    def PageIndex(self) -> int:
        """ Get: PageIndex(self: Page) -> int """
        ...

    @property
    def PageNumber(self) -> str:
        """
        Get: PageNumber(self: Page) -> str
        Set: PageNumber(self: Page) = value
        """
        ...

    @property
    def PageType(self) -> PbPageType:
        """ Get: PageType(self: Page) -> PbPageType """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Page) -> object """
        ...

    @property
    def ReaderSpread(self) -> ReaderSpread:
        """ Get: ReaderSpread(self: Page) -> ReaderSpread """
        ...

    @property
    def RulerGuides(self) -> RulerGuides:
        """ Get: RulerGuides(self: Page) -> RulerGuides """
        ...

    @property
    def Shapes(self) -> Shapes:
        """ Get: Shapes(self: Page) -> Shapes """
        ...

    @property
    def Tags(self) -> Tags:
        """ Get: Tags(self: Page) -> Tags """
        ...

    @property
    def WebPageOptions(self) -> WebPageOptions:
        """ Get: WebPageOptions(self: Page) -> WebPageOptions """
        ...

    @property
    def Width(self) -> int:
        """ Get: Width(self: Page) -> int """
        ...

    @property
    def Wizard(self) -> Wizard:
        """ Get: Wizard(self: Page) -> Wizard """
        ...

    @property
    def XOffsetWithinReaderSpread(self) -> Single:
        """ Get: XOffsetWithinReaderSpread(self: Page) -> Single """
        ...

    @property
    def YOffsetWithinReaderSpread(self) -> Single:
        """ Get: YOffsetWithinReaderSpread(self: Page) -> Single """
        ...


    def Delete(self): # -> 
        """ Delete(self: Page) """
        ...

    def Duplicate(self, NewAbbreviation:str, NewName:str) -> Page:
        """ Duplicate(self: Page, NewAbbreviation: str, NewName: str) -> Page """
        ...

    def ExportEmailHTML(self, Filename:str): # -> 
        """ ExportEmailHTML(self: Page, Filename: str) """
        ...

    def Move(self, Page:int, After:bool): # -> 
        """ Move(self: Page, Page: int, After: bool) """
        ...

    def SaveAsPicture(self, Filename:str, pbResolution:PbPictureResolution): # -> 
        """ SaveAsPicture(self: Page, Filename: str, pbResolution: PbPictureResolution) """
        ...

    def SaveAsPicture10(self, Filename:str): # -> 
        """ SaveAsPicture10(self: Page, Filename: str) """
        ...


class PageBackground: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PageBackground) -> Application """
        ...

    @property
    def Exists(self) -> bool:
        """ Get: Exists(self: PageBackground) -> bool """
        ...

    @property
    def Fill(self) -> FillFormat:
        """ Get: Fill(self: PageBackground) -> FillFormat """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PageBackground) -> object """
        ...


    def Create(self): # -> 
        """ Create(self: PageBackground) """
        ...

    def Delete(self): # -> 
        """ Delete(self: PageBackground) """
        ...


class Pages(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Pages) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Pages) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Pages) -> object """
        ...


    def Add(self, Count:int, After:int, DuplicateObjectsOnPage:int, AddHyperlinkToWebNavBar:bool) -> Page:
        """ Add(self: Pages, Count: int, After: int, DuplicateObjectsOnPage: int, AddHyperlinkToWebNavBar: bool) -> Page """
        ...

    def Add10(self, Count:int, After:int, DuplicateObjectsOnPage:int) -> Page:
        """ Add10(self: Pages, Count: int, After: int, DuplicateObjectsOnPage: int) -> Page """
        ...

    def AddWizardPage(self, After:int, PageType:PbWizardPageType, AddHyperlinkToWebNavBar:bool): # -> 
        """ AddWizardPage(self: Pages, After: int, PageType: PbWizardPageType, AddHyperlinkToWebNavBar: bool) """
        ...

    def AddWizardPage10(self, After:int, PageType:PbWizardPageType): # -> 
        """ AddWizardPage10(self: Pages, After: int, PageType: PbWizardPageType) """
        ...

    def FindByPageID(self, PageID:int) -> Page:
        """ FindByPageID(self: Pages, PageID: int) -> Page """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class PageSetup: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PageSetup) -> Application """
        ...

    @property
    def AvailableLabels(self) -> Labels:
        """ Get: AvailableLabels(self: PageSetup) -> Labels """
        ...

    @property
    def AvailablePageSizes(self) -> PageSizes:
        """ Get: AvailablePageSizes(self: PageSetup) -> PageSizes """
        ...

    @property
    def HorizontalGap(self) -> object:
        """
        Get: HorizontalGap(self: PageSetup) -> object
        Set: HorizontalGap(self: PageSetup) = value
        """
        ...

    @property
    def Label(self) -> Label:
        """
        Get: Label(self: PageSetup) -> Label
        Set: Label(self: PageSetup) = value
        """
        ...

    @property
    def LeftMargin(self) -> object:
        """
        Get: LeftMargin(self: PageSetup) -> object
        Set: LeftMargin(self: PageSetup) = value
        """
        ...

    @property
    def MultiplePagesPerSheet(self) -> bool:
        """
        Get: MultiplePagesPerSheet(self: PageSetup) -> bool
        Set: MultiplePagesPerSheet(self: PageSetup) = value
        """
        ...

    @property
    def Orientation(self) -> PbOrientationType:
        """
        Get: Orientation(self: PageSetup) -> PbOrientationType
        Set: Orientation(self: PageSetup) = value
        """
        ...

    @property
    def PageHeight(self) -> object:
        """
        Get: PageHeight(self: PageSetup) -> object
        Set: PageHeight(self: PageSetup) = value
        """
        ...

    @property
    def PageSize(self) -> PageSize:
        """
        Get: PageSize(self: PageSetup) -> PageSize
        Set: PageSize(self: PageSetup) = value
        """
        ...

    @property
    def PageWidth(self) -> object:
        """
        Get: PageWidth(self: PageSetup) -> object
        Set: PageWidth(self: PageSetup) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PageSetup) -> object """
        ...

    @property
    def PublicationLayout(self) -> PbPublicationLayout:
        """
        Get: PublicationLayout(self: PageSetup) -> PbPublicationLayout
        Set: PublicationLayout(self: PageSetup) = value
        """
        ...

    @property
    def TopMargin(self) -> object:
        """
        Get: TopMargin(self: PageSetup) -> object
        Set: TopMargin(self: PageSetup) = value
        """
        ...

    @property
    def VerticalGap(self) -> object:
        """
        Get: VerticalGap(self: PageSetup) -> object
        Set: VerticalGap(self: PageSetup) = value
        """
        ...



class PageSize: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PageSize) -> Application """
        ...

    @property
    def HasBackgroundImage(self) -> bool:
        """ Get: HasBackgroundImage(self: PageSize) -> bool """
        ...

    @property
    def HorizontalGap(self) -> object:
        """ Get: HorizontalGap(self: PageSize) -> object """
        ...

    @property
    def LeftMargin(self) -> object:
        """ Get: LeftMargin(self: PageSize) -> object """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PageSize) -> str """
        ...

    @property
    def PageHeight(self) -> object:
        """
        Get: PageHeight(self: PageSize) -> object
        Set: PageHeight(self: PageSize) = value
        """
        ...

    @property
    def PageWidth(self) -> object:
        """
        Get: PageWidth(self: PageSize) -> object
        Set: PageWidth(self: PageSize) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PageSize) -> object """
        ...

    @property
    def TopMargin(self) -> object:
        """ Get: TopMargin(self: PageSize) -> object """
        ...

    @property
    def VerticalGap(self) -> object:
        """ Get: VerticalGap(self: PageSize) -> object """
        ...



class PageSizes(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PageSizes) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: PageSizes) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PageSizes) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ParagraphFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Alignment(self) -> PbParagraphAlignmentType:
        """
        Get: Alignment(self: ParagraphFormat) -> PbParagraphAlignmentType
        Set: Alignment(self: ParagraphFormat) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: ParagraphFormat) -> Application """
        ...

    @property
    def AttachedToText(self) -> bool:
        """ Get: AttachedToText(self: ParagraphFormat) -> bool """
        ...

    @property
    def CharBasedFirstLineIndent(self) -> int:
        """
        Get: CharBasedFirstLineIndent(self: ParagraphFormat) -> int
        Set: CharBasedFirstLineIndent(self: ParagraphFormat) = value
        """
        ...

    @property
    def FirstLineIndent(self) -> object:
        """
        Get: FirstLineIndent(self: ParagraphFormat) -> object
        Set: FirstLineIndent(self: ParagraphFormat) = value
        """
        ...

    @property
    def KashidaPercentage(self) -> int:
        """
        Get: KashidaPercentage(self: ParagraphFormat) -> int
        Set: KashidaPercentage(self: ParagraphFormat) = value
        """
        ...

    @property
    def KeepLinesTogether(self): # -> MsoTriState
        """
        Get: KeepLinesTogether(self: ParagraphFormat) -> MsoTriState
        Set: KeepLinesTogether(self: ParagraphFormat) = value
        """
        ...

    @property
    def KeepWithNext(self): # -> MsoTriState
        """
        Get: KeepWithNext(self: ParagraphFormat) -> MsoTriState
        Set: KeepWithNext(self: ParagraphFormat) = value
        """
        ...

    @property
    def LeftIndent(self) -> object:
        """
        Get: LeftIndent(self: ParagraphFormat) -> object
        Set: LeftIndent(self: ParagraphFormat) = value
        """
        ...

    @property
    def LineSpacing(self) -> object:
        """
        Get: LineSpacing(self: ParagraphFormat) -> object
        Set: LineSpacing(self: ParagraphFormat) = value
        """
        ...

    @property
    def LineSpacingRule(self) -> PbLineSpacingRule:
        """
        Get: LineSpacingRule(self: ParagraphFormat) -> PbLineSpacingRule
        Set: LineSpacingRule(self: ParagraphFormat) = value
        """
        ...

    @property
    def ListBulletFontName(self) -> str:
        """
        Get: ListBulletFontName(self: ParagraphFormat) -> str
        Set: ListBulletFontName(self: ParagraphFormat) = value
        """
        ...

    @property
    def ListBulletFontSize(self) -> Single:
        """
        Get: ListBulletFontSize(self: ParagraphFormat) -> Single
        Set: ListBulletFontSize(self: ParagraphFormat) = value
        """
        ...

    @property
    def ListBulletText(self) -> str:
        """ Get: ListBulletText(self: ParagraphFormat) -> str """
        ...

    @property
    def ListIndent(self) -> Single:
        """
        Get: ListIndent(self: ParagraphFormat) -> Single
        Set: ListIndent(self: ParagraphFormat) = value
        """
        ...

    @property
    def ListNumberSeparator(self) -> PbListSeparator:
        """
        Get: ListNumberSeparator(self: ParagraphFormat) -> PbListSeparator
        Set: ListNumberSeparator(self: ParagraphFormat) = value
        """
        ...

    @property
    def ListNumberStart(self) -> int:
        """
        Get: ListNumberStart(self: ParagraphFormat) -> int
        Set: ListNumberStart(self: ParagraphFormat) = value
        """
        ...

    @property
    def ListType(self) -> PbListType:
        """ Get: ListType(self: ParagraphFormat) -> PbListType """
        ...

    @property
    def LockToBaseLine(self): # -> MsoTriState
        """
        Get: LockToBaseLine(self: ParagraphFormat) -> MsoTriState
        Set: LockToBaseLine(self: ParagraphFormat) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ParagraphFormat) -> object """
        ...

    @property
    def RightIndent(self) -> object:
        """
        Get: RightIndent(self: ParagraphFormat) -> object
        Set: RightIndent(self: ParagraphFormat) = value
        """
        ...

    @property
    def SpaceAfter(self) -> object:
        """
        Get: SpaceAfter(self: ParagraphFormat) -> object
        Set: SpaceAfter(self: ParagraphFormat) = value
        """
        ...

    @property
    def SpaceBefore(self) -> object:
        """
        Get: SpaceBefore(self: ParagraphFormat) -> object
        Set: SpaceBefore(self: ParagraphFormat) = value
        """
        ...

    @property
    def StartInNextTextBox(self): # -> MsoTriState
        """
        Get: StartInNextTextBox(self: ParagraphFormat) -> MsoTriState
        Set: StartInNextTextBox(self: ParagraphFormat) = value
        """
        ...

    @property
    def Tabs(self) -> TabStops:
        """ Get: Tabs(self: ParagraphFormat) -> TabStops """
        ...

    @property
    def TextDirection(self) -> PbTextDirection:
        """
        Get: TextDirection(self: ParagraphFormat) -> PbTextDirection
        Set: TextDirection(self: ParagraphFormat) = value
        """
        ...

    @property
    def TextStyle(self) -> object:
        """
        Get: TextStyle(self: ParagraphFormat) -> object
        Set: TextStyle(self: ParagraphFormat) = value
        """
        ...

    @property
    def UseCharBasedFirstLineIndent(self): # -> MsoTriState
        """
        Get: UseCharBasedFirstLineIndent(self: ParagraphFormat) -> MsoTriState
        Set: UseCharBasedFirstLineIndent(self: ParagraphFormat) = value
        """
        ...

    @property
    def WidowControl(self): # -> MsoTriState
        """
        Get: WidowControl(self: ParagraphFormat) -> MsoTriState
        Set: WidowControl(self: ParagraphFormat) = value
        """
        ...


    def Duplicate(self) -> ParagraphFormat:
        """ Duplicate(self: ParagraphFormat) -> ParagraphFormat """
        ...

    def Reset(self): # -> 
        """ Reset(self: ParagraphFormat) """
        ...

    def SetLineSpacing(self, Rule:PbLineSpacingRule, Spacing:object): # -> 
        """ SetLineSpacing(self: ParagraphFormat, Rule: PbLineSpacingRule, Spacing: object) """
        ...

    def SetListType(self, Value:PbListType, BulletText:str): # -> 
        """ SetListType(self: ParagraphFormat, Value: PbListType, BulletText: str) """
        ...


class PbBuildingBlockGallery(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbBuildingBlockGallery, values: pbBBGalAccents (1), pbBBGalAdvertisements (0), pbBBGalBusinessInfo (3), pbBBGalCalendars (2), pbBBGalNone (-1), pbBBGalPageParts (4) """
    pbBBGalAccents: PbBuildingBlockGallery = ...
    pbBBGalAdvertisements: PbBuildingBlockGallery = ...
    pbBBGalBusinessInfo: PbBuildingBlockGallery = ...
    pbBBGalCalendars: PbBuildingBlockGallery = ...
    pbBBGalNone: PbBuildingBlockGallery = ...
    pbBBGalPageParts: PbBuildingBlockGallery = ...
    value__ = ...


class PbBuildingBlockType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbBuildingBlockType, values: pbBBBuiltIn (1), pbBBDownloaded (2), pbBBNone (0), pbBBUser (3), pbBBWorkGroup (4) """
    pbBBBuiltIn: PbBuildingBlockType = ...
    pbBBDownloaded: PbBuildingBlockType = ...
    pbBBNone: PbBuildingBlockType = ...
    pbBBUser: PbBuildingBlockType = ...
    pbBBWorkGroup: PbBuildingBlockType = ...
    value__ = ...


class PbCalendarType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbCalendarType, values: pbCalendarTypeArabicHijri (1), pbCalendarTypeArabicUmalqura (13), pbCalendarTypeChineseNational (3), pbCalendarTypeHebrewLunar (2), pbCalendarTypeJapaneseEmperor (4), pbCalendarTypeKoreanDanki (6), pbCalendarTypeSakaEra (7), pbCalendarTypeThaiBuddhist (5), pbCalendarTypeTranslitEnglish (8), pbCalendarTypeTranslitFrench (9), pbCalendarTypeWestern (0) """
    pbCalendarTypeArabicHijri: PbCalendarType = ...
    pbCalendarTypeArabicUmalqura: PbCalendarType = ...
    pbCalendarTypeChineseNational: PbCalendarType = ...
    pbCalendarTypeHebrewLunar: PbCalendarType = ...
    pbCalendarTypeJapaneseEmperor: PbCalendarType = ...
    pbCalendarTypeKoreanDanki: PbCalendarType = ...
    pbCalendarTypeSakaEra: PbCalendarType = ...
    pbCalendarTypeThaiBuddhist: PbCalendarType = ...
    pbCalendarTypeTranslitEnglish: PbCalendarType = ...
    pbCalendarTypeTranslitFrench: PbCalendarType = ...
    pbCalendarTypeWestern: PbCalendarType = ...
    value__ = ...


class pbCanvasArrangementType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum pbCanvasArrangementType, values: pbCanvasArrangementTypeColsCanvas (1), pbCanvasArrangementTypeOneCanvas (0), pbCanvasArrangementTypeRowsCanvas (2) """
    pbCanvasArrangementTypeColsCanvas: pbCanvasArrangementType = ...
    pbCanvasArrangementTypeOneCanvas: pbCanvasArrangementType = ...
    pbCanvasArrangementTypeRowsCanvas: pbCanvasArrangementType = ...
    value__ = ...


class pbCatalogMergeFieldType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum pbCatalogMergeFieldType, values: pbCatalogMergeFieldTypePicture (1), pbCatalogMergeFieldTypeText (0) """
    pbCatalogMergeFieldTypePicture: pbCatalogMergeFieldType = ...
    pbCatalogMergeFieldTypeText: pbCatalogMergeFieldType = ...
    value__ = ...


class PbCellDiagonalType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbCellDiagonalType, values: pbTableCellDiagonalDown (2), pbTableCellDiagonalMixed (-2), pbTableCellDiagonalNone (0), pbTableCellDiagonalUp (1) """
    pbTableCellDiagonalDown: PbCellDiagonalType = ...
    pbTableCellDiagonalMixed: PbCellDiagonalType = ...
    pbTableCellDiagonalNone: PbCellDiagonalType = ...
    pbTableCellDiagonalUp: PbCellDiagonalType = ...
    value__ = ...


class PbCollapseDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbCollapseDirection, values: pbCollapseEnd (2), pbCollapseStart (1) """
    pbCollapseEnd: PbCollapseDirection = ...
    pbCollapseStart: PbCollapseDirection = ...
    value__ = ...


class PbColorMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbColorMode, values: pbColorModeBW (3), pbColorModeDesktop (0), pbColorModeProcess (1), pbColorModeSpot (2), pbColorModeSpotAndProcess (4) """
    pbColorModeBW: PbColorMode = ...
    pbColorModeDesktop: PbColorMode = ...
    pbColorModeProcess: PbColorMode = ...
    pbColorModeSpot: PbColorMode = ...
    pbColorModeSpotAndProcess: PbColorMode = ...
    value__ = ...


class PbColorModel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbColorModel, values: pbColorModelCMYK (2), pbColorModelGreyScale (3), pbColorModelRGB (1), pbColorModelUnknown (4) """
    pbColorModelCMYK: PbColorModel = ...
    pbColorModelGreyScale: PbColorModel = ...
    pbColorModelRGB: PbColorModel = ...
    pbColorModelUnknown: PbColorModel = ...
    value__ = ...


class PbColorScheme(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbColorScheme, values: pbColorSchemeAlpine (-1), pbColorSchemeAqua (-2), pbColorSchemeBerry (-3), pbColorSchemeBlackGray (-4), pbColorSchemeBlackWhite (-58), pbColorSchemeBrown (-5), pbColorSchemeBurgundy (-6), pbColorSchemeCavern (-7), pbColorSchemeCelebration (-1004), pbColorSchemeCherry (-1002), pbColorSchemeCitrus (-8), pbColorSchemeClay (-9), pbColorSchemeCranberry (-10), pbColorSchemeCrocus (-11), pbColorSchemeCustom (1), pbColorSchemeDarkBlue (-61), pbColorSchemeDesert (-12), pbColorSchemeField (-13), pbColorSchemeFirstUserDefined (2000), pbColorSchemeFjord (-14), pbColorSchemeFloral (-15), pbColorSchemeGarnet (-16), pbColorSchemeGlacier (-17), pbColorSchemeGreen (-59), pbColorSchemeHeather (-18), pbColorSchemeIris (-19), pbColorSchemeIsland (-20), pbColorSchemeIvy (-21), pbColorSchemeLagoon (-22), pbColorSchemeLilac (-23), pbColorSchemeMahogany (-24), pbColorSchemeMarine (-25), pbColorSchemeMaroon (-26), pbColorSchemeMeadow (-27), pbColorSchemeMist (-28), pbColorSchemeMistletoe (-29), pbColorSchemeMonarch (-41), pbColorSchemeMoss (-30), pbColorSchemeMountain (-31), pbColorSchemeMulberry (-32), pbColorSchemeNavy (-33), pbColorSchemeNutmeg (-34), pbColorSchemeOcean (-1000), pbColorSchemeOlive (-35), pbColorSchemeOrange (-1003), pbColorSchemeOrchid (-36), pbColorSchemeParrot (-37), pbColorSchemePeach (-1005), pbColorSchemePebbles (-38), pbColorSchemePrairie (-39), pbColorSchemePurple (-1001), pbColorSchemeRainForest (-40), pbColorSchemeRed (-60), pbColorSchemeRedwood (-42), pbColorSchemeReef (-43), pbColorSchemeSagebrush (-44), pbColorSchemeSapphire (-45), pbColorSchemeShamrock (-46), pbColorSchemeSienna (-47), pbColorSchemeSpice (-48), pbColorSchemeSunrise (-49), pbColorSchemeSunset (-50), pbColorSchemeTeal (-51), pbColorSchemeTidepool (-52), pbColorSchemeTropics (-53), pbColorSchemeTrout (-54), pbColorSchemeVineyard (-55), pbColorSchemeWaterfall (-56), pbColorSchemeWildflower (-57) """
    pbColorSchemeAlpine: PbColorScheme = ...
    pbColorSchemeAqua: PbColorScheme = ...
    pbColorSchemeBerry: PbColorScheme = ...
    pbColorSchemeBlackGray: PbColorScheme = ...
    pbColorSchemeBlackWhite: PbColorScheme = ...
    pbColorSchemeBrown: PbColorScheme = ...
    pbColorSchemeBurgundy: PbColorScheme = ...
    pbColorSchemeCavern: PbColorScheme = ...
    pbColorSchemeCelebration: PbColorScheme = ...
    pbColorSchemeCherry: PbColorScheme = ...
    pbColorSchemeCitrus: PbColorScheme = ...
    pbColorSchemeClay: PbColorScheme = ...
    pbColorSchemeCranberry: PbColorScheme = ...
    pbColorSchemeCrocus: PbColorScheme = ...
    pbColorSchemeCustom: PbColorScheme = ...
    pbColorSchemeDarkBlue: PbColorScheme = ...
    pbColorSchemeDesert: PbColorScheme = ...
    pbColorSchemeField: PbColorScheme = ...
    pbColorSchemeFirstUserDefined: PbColorScheme = ...
    pbColorSchemeFjord: PbColorScheme = ...
    pbColorSchemeFloral: PbColorScheme = ...
    pbColorSchemeGarnet: PbColorScheme = ...
    pbColorSchemeGlacier: PbColorScheme = ...
    pbColorSchemeGreen: PbColorScheme = ...
    pbColorSchemeHeather: PbColorScheme = ...
    pbColorSchemeIris: PbColorScheme = ...
    pbColorSchemeIsland: PbColorScheme = ...
    pbColorSchemeIvy: PbColorScheme = ...
    pbColorSchemeLagoon: PbColorScheme = ...
    pbColorSchemeLilac: PbColorScheme = ...
    pbColorSchemeMahogany: PbColorScheme = ...
    pbColorSchemeMarine: PbColorScheme = ...
    pbColorSchemeMaroon: PbColorScheme = ...
    pbColorSchemeMeadow: PbColorScheme = ...
    pbColorSchemeMist: PbColorScheme = ...
    pbColorSchemeMistletoe: PbColorScheme = ...
    pbColorSchemeMonarch: PbColorScheme = ...
    pbColorSchemeMoss: PbColorScheme = ...
    pbColorSchemeMountain: PbColorScheme = ...
    pbColorSchemeMulberry: PbColorScheme = ...
    pbColorSchemeNavy: PbColorScheme = ...
    pbColorSchemeNutmeg: PbColorScheme = ...
    pbColorSchemeOcean: PbColorScheme = ...
    pbColorSchemeOlive: PbColorScheme = ...
    pbColorSchemeOrange: PbColorScheme = ...
    pbColorSchemeOrchid: PbColorScheme = ...
    pbColorSchemeParrot: PbColorScheme = ...
    pbColorSchemePeach: PbColorScheme = ...
    pbColorSchemePebbles: PbColorScheme = ...
    pbColorSchemePrairie: PbColorScheme = ...
    pbColorSchemePurple: PbColorScheme = ...
    pbColorSchemeRainForest: PbColorScheme = ...
    pbColorSchemeRed: PbColorScheme = ...
    pbColorSchemeRedwood: PbColorScheme = ...
    pbColorSchemeReef: PbColorScheme = ...
    pbColorSchemeSagebrush: PbColorScheme = ...
    pbColorSchemeSapphire: PbColorScheme = ...
    pbColorSchemeShamrock: PbColorScheme = ...
    pbColorSchemeSienna: PbColorScheme = ...
    pbColorSchemeSpice: PbColorScheme = ...
    pbColorSchemeSunrise: PbColorScheme = ...
    pbColorSchemeSunset: PbColorScheme = ...
    pbColorSchemeTeal: PbColorScheme = ...
    pbColorSchemeTidepool: PbColorScheme = ...
    pbColorSchemeTropics: PbColorScheme = ...
    pbColorSchemeTrout: PbColorScheme = ...
    pbColorSchemeVineyard: PbColorScheme = ...
    pbColorSchemeWaterfall: PbColorScheme = ...
    pbColorSchemeWildflower: PbColorScheme = ...
    value__ = ...


class PbColorType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbColorType, values: pbColorTypeCMS (4), pbColorTypeCMYK (3), pbColorTypeInk (5), pbColorTypeMixed (-2), pbColorTypeRGB (1), pbColorTypeScheme (2) """
    pbColorTypeCMS: PbColorType = ...
    pbColorTypeCMYK: PbColorType = ...
    pbColorTypeInk: PbColorType = ...
    pbColorTypeMixed: PbColorType = ...
    pbColorTypeRGB: PbColorType = ...
    pbColorTypeScheme: PbColorType = ...
    value__ = ...


class PbCommandButtonType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbCommandButtonType, values: pbCommandButtonReset (2), pbCommandButtonSubmit (1) """
    pbCommandButtonReset: PbCommandButtonType = ...
    pbCommandButtonSubmit: PbCommandButtonType = ...
    value__ = ...


class PbDateTimeFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbDateTimeFormat, values: pbDateEnglish (8), pbDateISO (4), pbDateLong (2), pbDateLongDay (1), pbDateMon_Yr (10), pbDateMonthYr (9), pbDateShort (0), pbDateShortAbb (7), pbDateShortAlt (3), pbDateShortMon (5), pbDateShortSlash (6), pbDateTimeEastAsia1 (17), pbDateTimeEastAsia2 (18), pbDateTimeEastAsia3 (19), pbDateTimeEastAsia4 (20), pbDateTimeEastAsia5 (21), pbTime24 (15), pbTimeDatePM (11), pbTimeDateSecPM (12), pbTimePM (13), pbTimeSec24 (16), pbTimeSecPM (14) """
    pbDateEnglish: PbDateTimeFormat = ...
    pbDateISO: PbDateTimeFormat = ...
    pbDateLong: PbDateTimeFormat = ...
    pbDateLongDay: PbDateTimeFormat = ...
    pbDateMonthYr: PbDateTimeFormat = ...
    pbDateMon_Yr: PbDateTimeFormat = ...
    pbDateShort: PbDateTimeFormat = ...
    pbDateShortAbb: PbDateTimeFormat = ...
    pbDateShortAlt: PbDateTimeFormat = ...
    pbDateShortMon: PbDateTimeFormat = ...
    pbDateShortSlash: PbDateTimeFormat = ...
    pbDateTimeEastAsia1: PbDateTimeFormat = ...
    pbDateTimeEastAsia2: PbDateTimeFormat = ...
    pbDateTimeEastAsia3: PbDateTimeFormat = ...
    pbDateTimeEastAsia4: PbDateTimeFormat = ...
    pbDateTimeEastAsia5: PbDateTimeFormat = ...
    pbTime24: PbDateTimeFormat = ...
    pbTimeDatePM: PbDateTimeFormat = ...
    pbTimeDateSecPM: PbDateTimeFormat = ...
    pbTimePM: PbDateTimeFormat = ...
    pbTimeSec24: PbDateTimeFormat = ...
    pbTimeSecPM: PbDateTimeFormat = ...
    value__ = ...


class PbDirectionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbDirectionType, values: pbDirectionLeftToRight (1), pbDirectionRightToLeft (2) """
    pbDirectionLeftToRight: PbDirectionType = ...
    pbDirectionRightToLeft: PbDirectionType = ...
    value__ = ...


class PbDriverType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbDriverType, values: pbDriverTypeNonPostScript (1), pbDriverTypePostScript1 (2), pbDriverTypePostScript2 (3), pbDriverTypePostScript3 (4), pbDriverTypeXPS (5) """
    pbDriverTypeNonPostScript: PbDriverType = ...
    pbDriverTypePostScript1: PbDriverType = ...
    pbDriverTypePostScript2: PbDriverType = ...
    pbDriverTypePostScript3: PbDriverType = ...
    pbDriverTypeXPS: PbDriverType = ...
    value__ = ...


class pbEmailMergePriority(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum pbEmailMergePriority, values: pbPriorityHigh (1), pbPriorityLow (2), pbPriorityNone (0) """
    pbPriorityHigh: pbEmailMergePriority = ...
    pbPriorityLow: pbEmailMergePriority = ...
    pbPriorityNone: pbEmailMergePriority = ...
    value__ = ...


class PbFieldType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbFieldType, values: pbFieldDateTime (4), pbFieldHyperlinkAbsolutePage (11), pbFieldHyperlinkEmail (12), pbFieldHyperlinkFile (13), pbFieldHyperlinkRelativePage (10), pbFieldHyperlinkURL (9), pbFieldIHIV (6), pbFieldMailMerge (5), pbFieldNone (0), pbFieldPageNumber (1), pbFieldPageNumberNext (2), pbFieldPageNumberPrev (3), pbFieldPersonalizedHyperlinkURL (14), pbFieldPhoneticGuide (7), pbFieldWizardSampleText (8) """
    pbFieldDateTime: PbFieldType = ...
    pbFieldHyperlinkAbsolutePage: PbFieldType = ...
    pbFieldHyperlinkEmail: PbFieldType = ...
    pbFieldHyperlinkFile: PbFieldType = ...
    pbFieldHyperlinkRelativePage: PbFieldType = ...
    pbFieldHyperlinkURL: PbFieldType = ...
    pbFieldIHIV: PbFieldType = ...
    pbFieldMailMerge: PbFieldType = ...
    pbFieldNone: PbFieldType = ...
    pbFieldPageNumber: PbFieldType = ...
    pbFieldPageNumberNext: PbFieldType = ...
    pbFieldPageNumberPrev: PbFieldType = ...
    pbFieldPersonalizedHyperlinkURL: PbFieldType = ...
    pbFieldPhoneticGuide: PbFieldType = ...
    pbFieldWizardSampleText: PbFieldType = ...
    value__ = ...


class PbFileFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbFileFormat, values: pbFileHTMLFiltered (7), pbFilePlainText (8), pbFilePublication (1), pbFilePublicationHTML (4), pbFilePublisher2000 (3), pbFilePublisher98 (2), pbFileRTF (6), pbFileUnicodeText (9), pbFileWebArchive (5) """
    pbFileHTMLFiltered: PbFileFormat = ...
    pbFilePlainText: PbFileFormat = ...
    pbFilePublication: PbFileFormat = ...
    pbFilePublicationHTML: PbFileFormat = ...
    pbFilePublisher2000: PbFileFormat = ...
    pbFilePublisher98: PbFileFormat = ...
    pbFileRTF: PbFileFormat = ...
    pbFileUnicodeText: PbFileFormat = ...
    pbFileWebArchive: PbFileFormat = ...
    value__ = ...


class PbFilterComparison(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbFilterComparison, values: pbComparisonEqual (0), pbComparisonGreaterThan (3), pbComparisonGreaterThanEqual (5), pbComparisonIsBlank (6), pbComparisonIsNotBlank (7), pbComparisonLessThan (2), pbComparisonLessThanEqual (4), pbComparisonNotEqual (1) """
    pbComparisonEqual: PbFilterComparison = ...
    pbComparisonGreaterThan: PbFilterComparison = ...
    pbComparisonGreaterThanEqual: PbFilterComparison = ...
    pbComparisonIsBlank: PbFilterComparison = ...
    pbComparisonIsNotBlank: PbFilterComparison = ...
    pbComparisonLessThan: PbFilterComparison = ...
    pbComparisonLessThanEqual: PbFilterComparison = ...
    pbComparisonNotEqual: PbFilterComparison = ...
    value__ = ...


class PbFilterConjunction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbFilterConjunction, values: pbConjunctionAnd (0), pbConjunctionOr (1) """
    pbConjunctionAnd: PbFilterConjunction = ...
    pbConjunctionOr: PbFilterConjunction = ...
    value__ = ...


class PbFixedFormatIntent(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbFixedFormatIntent, values: pbIntentCommercial (4), pbIntentMinimum (1), pbIntentPrinting (3), pbIntentStandard (2) """
    pbIntentCommercial: PbFixedFormatIntent = ...
    pbIntentMinimum: PbFixedFormatIntent = ...
    pbIntentPrinting: PbFixedFormatIntent = ...
    pbIntentStandard: PbFixedFormatIntent = ...
    value__ = ...


class PbFixedFormatType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbFixedFormatType, values: pbFixedFormatTypePDF (2), pbFixedFormatTypeXPS (1) """
    pbFixedFormatTypePDF: PbFixedFormatType = ...
    pbFixedFormatTypeXPS: PbFixedFormatType = ...
    value__ = ...


class PbFontLicenseLimitations(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbFontLicenseLimitations, values: pbFontEmbeddable (1), pbFontNotEmbeddable (3), pbFontPrintPreviewEmbeddable (2) """
    pbFontEmbeddable: PbFontLicenseLimitations = ...
    pbFontNotEmbeddable: PbFontLicenseLimitations = ...
    pbFontPrintPreviewEmbeddable: PbFontLicenseLimitations = ...
    value__ = ...


class PbFontScriptType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbFontScriptType, values: pbFontScriptArabic (7), pbFontScriptArmenian (5), pbFontScriptAsciiLatin (1), pbFontScriptAsciiSym (43), pbFontScriptBengali (9), pbFontScriptBopomofo (23), pbFontScriptBraille (41), pbFontScriptCanadianAbor (36), pbFontScriptCherokee (35), pbFontScriptCurrency (42), pbFontScriptCyrillic (4), pbFontScriptDefault (0), pbFontScriptDevanagari (8), pbFontScriptEthiopic (34), pbFontScriptEUDC (26), pbFontScriptGeorgian (20), pbFontScriptGreek (3), pbFontScriptGujarati (11), pbFontScriptGurmukhi (10), pbFontScriptHalfWidthKana (25), pbFontScriptHan (24), pbFontScriptHangul (21), pbFontScriptHanSurrogate (28), pbFontScriptHebrew (6), pbFontScriptKana (22), pbFontScriptKannada (15), pbFontScriptKhmer (39), pbFontScriptLao (18), pbFontScriptLatin (2), pbFontScriptMalayalam (16), pbFontScriptMixed (-2), pbFontScriptMongolian (40), pbFontScriptMyanmar (32), pbFontScriptNonHanSurrogate (29), pbFontScriptOgham (37), pbFontScriptOriya (12), pbFontScriptRunic (38), pbFontScriptSinhala (33), pbFontScriptSyriac (30), pbFontScriptTamil (13), pbFontScriptTelugu (14), pbFontScriptThaana (31), pbFontScriptThai (17), pbFontScriptTibetan (19), pbFontScriptYi (27) """
    pbFontScriptArabic: PbFontScriptType = ...
    pbFontScriptArmenian: PbFontScriptType = ...
    pbFontScriptAsciiLatin: PbFontScriptType = ...
    pbFontScriptAsciiSym: PbFontScriptType = ...
    pbFontScriptBengali: PbFontScriptType = ...
    pbFontScriptBopomofo: PbFontScriptType = ...
    pbFontScriptBraille: PbFontScriptType = ...
    pbFontScriptCanadianAbor: PbFontScriptType = ...
    pbFontScriptCherokee: PbFontScriptType = ...
    pbFontScriptCurrency: PbFontScriptType = ...
    pbFontScriptCyrillic: PbFontScriptType = ...
    pbFontScriptDefault: PbFontScriptType = ...
    pbFontScriptDevanagari: PbFontScriptType = ...
    pbFontScriptEthiopic: PbFontScriptType = ...
    pbFontScriptEUDC: PbFontScriptType = ...
    pbFontScriptGeorgian: PbFontScriptType = ...
    pbFontScriptGreek: PbFontScriptType = ...
    pbFontScriptGujarati: PbFontScriptType = ...
    pbFontScriptGurmukhi: PbFontScriptType = ...
    pbFontScriptHalfWidthKana: PbFontScriptType = ...
    pbFontScriptHan: PbFontScriptType = ...
    pbFontScriptHangul: PbFontScriptType = ...
    pbFontScriptHanSurrogate: PbFontScriptType = ...
    pbFontScriptHebrew: PbFontScriptType = ...
    pbFontScriptKana: PbFontScriptType = ...
    pbFontScriptKannada: PbFontScriptType = ...
    pbFontScriptKhmer: PbFontScriptType = ...
    pbFontScriptLao: PbFontScriptType = ...
    pbFontScriptLatin: PbFontScriptType = ...
    pbFontScriptMalayalam: PbFontScriptType = ...
    pbFontScriptMixed: PbFontScriptType = ...
    pbFontScriptMongolian: PbFontScriptType = ...
    pbFontScriptMyanmar: PbFontScriptType = ...
    pbFontScriptNonHanSurrogate: PbFontScriptType = ...
    pbFontScriptOgham: PbFontScriptType = ...
    pbFontScriptOriya: PbFontScriptType = ...
    pbFontScriptRunic: PbFontScriptType = ...
    pbFontScriptSinhala: PbFontScriptType = ...
    pbFontScriptSyriac: PbFontScriptType = ...
    pbFontScriptTamil: PbFontScriptType = ...
    pbFontScriptTelugu: PbFontScriptType = ...
    pbFontScriptThaana: PbFontScriptType = ...
    pbFontScriptThai: PbFontScriptType = ...
    pbFontScriptTibetan: PbFontScriptType = ...
    pbFontScriptYi: PbFontScriptType = ...
    value__ = ...


class PbFontSource(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbFontSource, values: pbFontDocument (2), pbFontMissing (3), pbFontSystem (1) """
    pbFontDocument: PbFontSource = ...
    pbFontMissing: PbFontSource = ...
    pbFontSystem: PbFontSource = ...
    value__ = ...


class PbFontType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbFontType, values: pbFontPrinter (2), pbFontRaster (3), pbFontTrueType (1), pbFontUnknown (4) """
    pbFontPrinter: PbFontType = ...
    pbFontRaster: PbFontType = ...
    pbFontTrueType: PbFontType = ...
    pbFontUnknown: PbFontType = ...
    value__ = ...


class PbHelpType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbHelpType, values: pbHelp (1), pbHelpActiveWindow (2), pbHelpPSSHelp (3) """
    pbHelp: PbHelpType = ...
    pbHelpActiveWindow: PbHelpType = ...
    pbHelpPSSHelp: PbHelpType = ...
    value__ = ...


class PbHlinkTargetType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbHlinkTargetType, values: pbHlinkTargetTypeEmail (2), pbHlinkTargetTypeFirstPage (3), pbHlinkTargetTypeLastPage (4), pbHlinkTargetTypeNextPage (5), pbHlinkTargetTypeNone (0), pbHlinkTargetTypePageID (7), pbHlinkTargetTypePersonalized (8), pbHlinkTargetTypePreviousPage (6), pbHlinkTargetTypeURL (1) """
    pbHlinkTargetTypeEmail: PbHlinkTargetType = ...
    pbHlinkTargetTypeFirstPage: PbHlinkTargetType = ...
    pbHlinkTargetTypeLastPage: PbHlinkTargetType = ...
    pbHlinkTargetTypeNextPage: PbHlinkTargetType = ...
    pbHlinkTargetTypeNone: PbHlinkTargetType = ...
    pbHlinkTargetTypePageID: PbHlinkTargetType = ...
    pbHlinkTargetTypePersonalized: PbHlinkTargetType = ...
    pbHlinkTargetTypePreviousPage: PbHlinkTargetType = ...
    pbHlinkTargetTypeURL: PbHlinkTargetType = ...
    value__ = ...


class PbHorizontalPictureLocking(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbHorizontalPictureLocking, values: pbHorizontalLockingLeft (1), pbHorizontalLockingNone (0), pbHorizontalLockingRight (2), pbHorizontalLockingStretch (3) """
    pbHorizontalLockingLeft: PbHorizontalPictureLocking = ...
    pbHorizontalLockingNone: PbHorizontalPictureLocking = ...
    pbHorizontalLockingRight: PbHorizontalPictureLocking = ...
    pbHorizontalLockingStretch: PbHorizontalPictureLocking = ...
    value__ = ...


class PbImageFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbImageFormat, values: pbImageFormatCMYKJPEG (10), pbImageFormatDIB (7), pbImageFormatEMF (2), pbImageFormatGIF (8), pbImageFormatJPEG (5), pbImageFormatPICT (4), pbImageFormatPNG (6), pbImageFormatTIFF (9), pbImageFormatUNKNOWN (1), pbImageFormatWMF (3) """
    pbImageFormatCMYKJPEG: PbImageFormat = ...
    pbImageFormatDIB: PbImageFormat = ...
    pbImageFormatEMF: PbImageFormat = ...
    pbImageFormatGIF: PbImageFormat = ...
    pbImageFormatJPEG: PbImageFormat = ...
    pbImageFormatPICT: PbImageFormat = ...
    pbImageFormatPNG: PbImageFormat = ...
    pbImageFormatTIFF: PbImageFormat = ...
    pbImageFormatUNKNOWN: PbImageFormat = ...
    pbImageFormatWMF: PbImageFormat = ...
    value__ = ...


class PbInkName(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbInkName, values: pbInkNameBlack (4), pbInkNameCyan (1), pbInkNameMagenta (2), pbInkNameSpot1 (257), pbInkNameSpot10 (266), pbInkNameSpot11 (267), pbInkNameSpot12 (268), pbInkNameSpot2 (258), pbInkNameSpot3 (259), pbInkNameSpot4 (260), pbInkNameSpot5 (261), pbInkNameSpot6 (262), pbInkNameSpot7 (263), pbInkNameSpot8 (264), pbInkNameSpot9 (265), pbInkNameYellow (3) """
    pbInkNameBlack: PbInkName = ...
    pbInkNameCyan: PbInkName = ...
    pbInkNameMagenta: PbInkName = ...
    pbInkNameSpot1: PbInkName = ...
    pbInkNameSpot10: PbInkName = ...
    pbInkNameSpot11: PbInkName = ...
    pbInkNameSpot12: PbInkName = ...
    pbInkNameSpot2: PbInkName = ...
    pbInkNameSpot3: PbInkName = ...
    pbInkNameSpot4: PbInkName = ...
    pbInkNameSpot5: PbInkName = ...
    pbInkNameSpot6: PbInkName = ...
    pbInkNameSpot7: PbInkName = ...
    pbInkNameSpot8: PbInkName = ...
    pbInkNameSpot9: PbInkName = ...
    pbInkNameYellow: PbInkName = ...
    value__ = ...


class PbInksToPrint(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbInksToPrint, values: pbInksToPrintAll (1), pbInksToPrintConvertSpotToProcess (3), pbInksToPrintUsed (2) """
    pbInksToPrintAll: PbInksToPrint = ...
    pbInksToPrintConvertSpotToProcess: PbInksToPrint = ...
    pbInksToPrintUsed: PbInksToPrint = ...
    value__ = ...


class PbInlineAlignment(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbInlineAlignment, values: pbInlineAlignmentCharacter (0), pbInlineAlignmentLeft (1), pbInlineAlignmentMixed (-2), pbInlineAlignmentRight (2) """
    pbInlineAlignmentCharacter: PbInlineAlignment = ...
    pbInlineAlignmentLeft: PbInlineAlignment = ...
    pbInlineAlignmentMixed: PbInlineAlignment = ...
    pbInlineAlignmentRight: PbInlineAlignment = ...
    value__ = ...


class PbLigaturePresetType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbLigaturePresetType, values: pbLigatureAll (3), pbLigatureMixed (-1), pbLigatureNone (4), pbLigatureStandard (0), pbLigatureStandardHistorical (2), pbLigatureStandardOptional (1) """
    pbLigatureAll: PbLigaturePresetType = ...
    pbLigatureMixed: PbLigaturePresetType = ...
    pbLigatureNone: PbLigaturePresetType = ...
    pbLigatureStandard: PbLigaturePresetType = ...
    pbLigatureStandardHistorical: PbLigaturePresetType = ...
    pbLigatureStandardOptional: PbLigaturePresetType = ...
    value__ = ...


class PbLineSpacingRule(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbLineSpacingRule, values: pbLineSpacing1pt5 (1), pbLineSpacingDouble (2), pbLineSpacingExactly (4), pbLineSpacingMixed (-9999999), pbLineSpacingMultiple (5), pbLineSpacingSingle (0) """
    pbLineSpacing1pt5: PbLineSpacingRule = ...
    pbLineSpacingDouble: PbLineSpacingRule = ...
    pbLineSpacingExactly: PbLineSpacingRule = ...
    pbLineSpacingMixed: PbLineSpacingRule = ...
    pbLineSpacingMultiple: PbLineSpacingRule = ...
    pbLineSpacingSingle: PbLineSpacingRule = ...
    value__ = ...


class PbLinkedFileStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbLinkedFileStatus, values: pbLinkedFileMissing (2), pbLinkedFileModified (3), pbLinkedFileOK (1) """
    pbLinkedFileMissing: PbLinkedFileStatus = ...
    pbLinkedFileModified: PbLinkedFileStatus = ...
    pbLinkedFileOK: PbLinkedFileStatus = ...
    value__ = ...


class PbListSeparator(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbListSeparator, values: pbListSeparatorColon (327680), pbListSeparatorDoubleHyphen (458752), pbListSeparatorDoubleParen (65536), pbListSeparatorDoubleSquare (393216), pbListSeparatorParenthesis (0), pbListSeparatorPeriod (131072), pbListSeparatorPlain (196608), pbListSeparatorSquare (262144), pbListSeparatorWideComma (524288) """
    pbListSeparatorColon: PbListSeparator = ...
    pbListSeparatorDoubleHyphen: PbListSeparator = ...
    pbListSeparatorDoubleParen: PbListSeparator = ...
    pbListSeparatorDoubleSquare: PbListSeparator = ...
    pbListSeparatorParenthesis: PbListSeparator = ...
    pbListSeparatorPeriod: PbListSeparator = ...
    pbListSeparatorPlain: PbListSeparator = ...
    pbListSeparatorSquare: PbListSeparator = ...
    pbListSeparatorWideComma: PbListSeparator = ...
    value__ = ...


class PbListType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbListType, values: pbListTypeAiueo (12), pbListTypeArabic (0), pbListTypeArabic1 (46), pbListTypeArabic2 (48), pbListTypeArabicLeadingZero (22), pbListTypeBullet (23), pbListTypeCardinalText (6), pbListTypeChnDbNum2 (38), pbListTypeChnDbNum3 (39), pbListTypeChosung (25), pbListTypeCirclenum (18), pbListTypeDAiueo (20), pbListTypeDbChar (14), pbListTypeDbNum1 (10), pbListTypeDbNum2 (11), pbListTypeDbNum3 (16), pbListTypeDbNum4 (17), pbListTypeDIroha (21), pbListTypeGanada (24), pbListTypeHebrew1 (45), pbListTypeHebrew2 (47), pbListTypeHindi1 (49), pbListTypeHindi2 (50), pbListTypeHindi3 (51), pbListTypeHindi4 (52), pbListTypeIroha (13), pbListTypeKorDbNum1 (41), pbListTypeKorDbNum2 (42), pbListTypeKorDbNum3 (43), pbListTypeKorDbNum4 (44), pbListTypeLowerCaseLetter (4), pbListTypeLowerCaseRoman (2), pbListTypeLowerCaseRussian (58), pbListTypeNone (255), pbListTypeOrdinal (5), pbListTypeOrdinalText (7), pbListTypeThai1 (53), pbListTypeThai2 (54), pbListTypeThai3 (55), pbListTypeTpeDbNum2 (34), pbListTypeTpeDbNum3 (35), pbListTypeUpperCaseLetter (3), pbListTypeUpperCaseRoman (1), pbListTypeUpperCaseRussian (59), pbListTypeVietnamese1 (56), pbListTypeZodiac1 (30), pbListTypeZodiac2 (31) """
    pbListTypeAiueo: PbListType = ...
    pbListTypeArabic: PbListType = ...
    pbListTypeArabic1: PbListType = ...
    pbListTypeArabic2: PbListType = ...
    pbListTypeArabicLeadingZero: PbListType = ...
    pbListTypeBullet: PbListType = ...
    pbListTypeCardinalText: PbListType = ...
    pbListTypeChnDbNum2: PbListType = ...
    pbListTypeChnDbNum3: PbListType = ...
    pbListTypeChosung: PbListType = ...
    pbListTypeCirclenum: PbListType = ...
    pbListTypeDAiueo: PbListType = ...
    pbListTypeDbChar: PbListType = ...
    pbListTypeDbNum1: PbListType = ...
    pbListTypeDbNum2: PbListType = ...
    pbListTypeDbNum3: PbListType = ...
    pbListTypeDbNum4: PbListType = ...
    pbListTypeDIroha: PbListType = ...
    pbListTypeGanada: PbListType = ...
    pbListTypeHebrew1: PbListType = ...
    pbListTypeHebrew2: PbListType = ...
    pbListTypeHindi1: PbListType = ...
    pbListTypeHindi2: PbListType = ...
    pbListTypeHindi3: PbListType = ...
    pbListTypeHindi4: PbListType = ...
    pbListTypeIroha: PbListType = ...
    pbListTypeKorDbNum1: PbListType = ...
    pbListTypeKorDbNum2: PbListType = ...
    pbListTypeKorDbNum3: PbListType = ...
    pbListTypeKorDbNum4: PbListType = ...
    pbListTypeLowerCaseLetter: PbListType = ...
    pbListTypeLowerCaseRoman: PbListType = ...
    pbListTypeLowerCaseRussian: PbListType = ...
    pbListTypeNone: PbListType = ...
    pbListTypeOrdinal: PbListType = ...
    pbListTypeOrdinalText: PbListType = ...
    pbListTypeThai1: PbListType = ...
    pbListTypeThai2: PbListType = ...
    pbListTypeThai3: PbListType = ...
    pbListTypeTpeDbNum2: PbListType = ...
    pbListTypeTpeDbNum3: PbListType = ...
    pbListTypeUpperCaseLetter: PbListType = ...
    pbListTypeUpperCaseRoman: PbListType = ...
    pbListTypeUpperCaseRussian: PbListType = ...
    pbListTypeVietnamese1: PbListType = ...
    pbListTypeZodiac1: PbListType = ...
    pbListTypeZodiac2: PbListType = ...
    value__ = ...


class PbMailMergeDataFieldType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbMailMergeDataFieldType, values: pbMailMergeDataFieldPicture (1), pbMailMergeDataFieldString (0) """
    pbMailMergeDataFieldPicture: PbMailMergeDataFieldType = ...
    pbMailMergeDataFieldString: PbMailMergeDataFieldType = ...
    value__ = ...


class PbMailMergeDataSource(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbMailMergeDataSource, values: pbMergeInfoFromODSO (5), pbMergeInfoSubODSO (6) """
    pbMergeInfoFromODSO: PbMailMergeDataSource = ...
    pbMergeInfoSubODSO: PbMailMergeDataSource = ...
    value__ = ...


class PbMailMergeDestination(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbMailMergeDestination, values: pbMergeToExistingPublication (3), pbMergeToNewPublication (2), pbSendEmail (4), pbSendToPrinter (1) """
    pbMergeToExistingPublication: PbMailMergeDestination = ...
    pbMergeToNewPublication: PbMailMergeDestination = ...
    pbSendEmail: PbMailMergeDestination = ...
    pbSendToPrinter: PbMailMergeDestination = ...
    value__ = ...


class PbMappedDataFields(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbMappedDataFields, values: pbAddress1 (10), pbAddress2 (11), pbAddress3 (29), pbBusinessFax (17), pbBusinessPhone (16), pbCity (12), pbCompany (9), pbCountryRegion (15), pbCourtesyTitle (2), pbDepartment (30), pbEmailAddress (20), pbFirstName (3), pbHomeFax (19), pbHomePhone (18), pbJobTitle (8), pbLastName (5), pbMiddleName (4), pbNickname (7), pbPostalCode (14), pbRubyFirstName (27), pbRubyLastName (28), pbSpouseCourtesyTitle (22), pbSpouseFirstName (23), pbSpouseLastName (25), pbSpouseMiddleName (24), pbSpouseNickname (26), pbState (13), pbSuffix (6), pbUniqueIdentifier (1), pbWebPageURL (21) """
    pbAddress1: PbMappedDataFields = ...
    pbAddress2: PbMappedDataFields = ...
    pbAddress3: PbMappedDataFields = ...
    pbBusinessFax: PbMappedDataFields = ...
    pbBusinessPhone: PbMappedDataFields = ...
    pbCity: PbMappedDataFields = ...
    pbCompany: PbMappedDataFields = ...
    pbCountryRegion: PbMappedDataFields = ...
    pbCourtesyTitle: PbMappedDataFields = ...
    pbDepartment: PbMappedDataFields = ...
    pbEmailAddress: PbMappedDataFields = ...
    pbFirstName: PbMappedDataFields = ...
    pbHomeFax: PbMappedDataFields = ...
    pbHomePhone: PbMappedDataFields = ...
    pbJobTitle: PbMappedDataFields = ...
    pbLastName: PbMappedDataFields = ...
    pbMiddleName: PbMappedDataFields = ...
    pbNickname: PbMappedDataFields = ...
    pbPostalCode: PbMappedDataFields = ...
    pbRubyFirstName: PbMappedDataFields = ...
    pbRubyLastName: PbMappedDataFields = ...
    pbSpouseCourtesyTitle: PbMappedDataFields = ...
    pbSpouseFirstName: PbMappedDataFields = ...
    pbSpouseLastName: PbMappedDataFields = ...
    pbSpouseMiddleName: PbMappedDataFields = ...
    pbSpouseNickname: PbMappedDataFields = ...
    pbState: PbMappedDataFields = ...
    pbSuffix: PbMappedDataFields = ...
    pbUniqueIdentifier: PbMappedDataFields = ...
    pbWebPageURL: PbMappedDataFields = ...
    value__ = ...


class PbMasterPageType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbMasterPageType, values: pbMasterPageLeftPage (1), pbMasterPageRightPage (2) """
    pbMasterPageLeftPage: PbMasterPageType = ...
    pbMasterPageRightPage: PbMasterPageType = ...
    value__ = ...


class PbMergeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbMergeType, values: pbCatalogMerge (3), pbEmailMerge (4), pbMailMerge (2), pbMergeDefault (0) """
    pbCatalogMerge: PbMergeType = ...
    pbEmailMerge: PbMergeType = ...
    pbMailMerge: PbMergeType = ...
    pbMergeDefault: PbMergeType = ...
    value__ = ...


class PbNavBarOrientation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbNavBarOrientation, values: pbNavBarOrientHorizontal (1), pbNavBarOrientVertical (2) """
    pbNavBarOrientHorizontal: PbNavBarOrientation = ...
    pbNavBarOrientVertical: PbNavBarOrientation = ...
    value__ = ...


class PbNumberStylesType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbNumberStylesType, values: pbNumberStyleDefault (0), pbNumberStyleMixed (-1), pbNumberStyleProportionalLining (1), pbNumberStyleProportionalOldstyle (3), pbNumberStyleTabularLining (2), pbNumberStyleTabularOldstyle (4) """
    pbNumberStyleDefault: PbNumberStylesType = ...
    pbNumberStyleMixed: PbNumberStylesType = ...
    pbNumberStyleProportionalLining: PbNumberStylesType = ...
    pbNumberStyleProportionalOldstyle: PbNumberStylesType = ...
    pbNumberStyleTabularLining: PbNumberStylesType = ...
    pbNumberStyleTabularOldstyle: PbNumberStylesType = ...
    value__ = ...


class PbOrientationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbOrientationType, values: pbOrientationLandscape (2), pbOrientationPortrait (1) """
    pbOrientationLandscape: PbOrientationType = ...
    pbOrientationPortrait: PbOrientationType = ...
    value__ = ...


class PbOriginalFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbOriginalFormat, values: pbOriginalPublicationFormat (1), pbPublisherFile (2) """
    pbOriginalPublicationFormat: PbOriginalFormat = ...
    pbPublisherFile: PbOriginalFormat = ...
    value__ = ...


class PbPageNumberFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbPageNumberFormat, values: pbPageNumberFormatAiueo (12), pbPageNumberFormatArabic (0), pbPageNumberFormatArabic1 (46), pbPageNumberFormatArabic2 (48), pbPageNumberFormatArabicLZ (22), pbPageNumberFormatCardtext (6), pbPageNumberFormatChnDbNum2 (38), pbPageNumberFormatChnDbNum3 (39), pbPageNumberFormatChosung (25), pbPageNumberFormatCirclenum (18), pbPageNumberFormatDAiueo (20), pbPageNumberFormatDbChar (14), pbPageNumberFormatDbNum1 (10), pbPageNumberFormatDbNum2 (11), pbPageNumberFormatDbNum3 (16), pbPageNumberFormatDIroha (21), pbPageNumberFormatGanada (24), pbPageNumberFormatHebrew1 (45), pbPageNumberFormatHebrew2 (47), pbPageNumberFormatHindi1 (49), pbPageNumberFormatHindi2 (50), pbPageNumberFormatHindi3 (51), pbPageNumberFormatHindi4 (52), pbPageNumberFormatIroha (13), pbPageNumberFormatKorDbNum1 (41), pbPageNumberFormatKorDbNum2 (42), pbPageNumberFormatKorDbNum3 (43), pbPageNumberFormatKorDbNum4 (44), pbPageNumberFormatLCLetter (4), pbPageNumberFormatLCRoman (2), pbPageNumberFormatLCRus (58), pbPageNumberFormatOrdinal (5), pbPageNumberFormatOrdtext (7), pbPageNumberFormatThai1 (53), pbPageNumberFormatThai2 (54), pbPageNumberFormatThai3 (55), pbPageNumberFormatTpeDbNum2 (34), pbPageNumberFormatTpeDbNum3 (35), pbPageNumberFormatUCLetter (3), pbPageNumberFormatUCRoman (1), pbPageNumberFormatUCRus (59), pbPageNumberFormatViet1 (56), pbPageNumberFormatZodiac1 (30), pbPageNumberFormatZodiac2 (31) """
    pbPageNumberFormatAiueo: PbPageNumberFormat = ...
    pbPageNumberFormatArabic: PbPageNumberFormat = ...
    pbPageNumberFormatArabic1: PbPageNumberFormat = ...
    pbPageNumberFormatArabic2: PbPageNumberFormat = ...
    pbPageNumberFormatArabicLZ: PbPageNumberFormat = ...
    pbPageNumberFormatCardtext: PbPageNumberFormat = ...
    pbPageNumberFormatChnDbNum2: PbPageNumberFormat = ...
    pbPageNumberFormatChnDbNum3: PbPageNumberFormat = ...
    pbPageNumberFormatChosung: PbPageNumberFormat = ...
    pbPageNumberFormatCirclenum: PbPageNumberFormat = ...
    pbPageNumberFormatDAiueo: PbPageNumberFormat = ...
    pbPageNumberFormatDbChar: PbPageNumberFormat = ...
    pbPageNumberFormatDbNum1: PbPageNumberFormat = ...
    pbPageNumberFormatDbNum2: PbPageNumberFormat = ...
    pbPageNumberFormatDbNum3: PbPageNumberFormat = ...
    pbPageNumberFormatDIroha: PbPageNumberFormat = ...
    pbPageNumberFormatGanada: PbPageNumberFormat = ...
    pbPageNumberFormatHebrew1: PbPageNumberFormat = ...
    pbPageNumberFormatHebrew2: PbPageNumberFormat = ...
    pbPageNumberFormatHindi1: PbPageNumberFormat = ...
    pbPageNumberFormatHindi2: PbPageNumberFormat = ...
    pbPageNumberFormatHindi3: PbPageNumberFormat = ...
    pbPageNumberFormatHindi4: PbPageNumberFormat = ...
    pbPageNumberFormatIroha: PbPageNumberFormat = ...
    pbPageNumberFormatKorDbNum1: PbPageNumberFormat = ...
    pbPageNumberFormatKorDbNum2: PbPageNumberFormat = ...
    pbPageNumberFormatKorDbNum3: PbPageNumberFormat = ...
    pbPageNumberFormatKorDbNum4: PbPageNumberFormat = ...
    pbPageNumberFormatLCLetter: PbPageNumberFormat = ...
    pbPageNumberFormatLCRoman: PbPageNumberFormat = ...
    pbPageNumberFormatLCRus: PbPageNumberFormat = ...
    pbPageNumberFormatOrdinal: PbPageNumberFormat = ...
    pbPageNumberFormatOrdtext: PbPageNumberFormat = ...
    pbPageNumberFormatThai1: PbPageNumberFormat = ...
    pbPageNumberFormatThai2: PbPageNumberFormat = ...
    pbPageNumberFormatThai3: PbPageNumberFormat = ...
    pbPageNumberFormatTpeDbNum2: PbPageNumberFormat = ...
    pbPageNumberFormatTpeDbNum3: PbPageNumberFormat = ...
    pbPageNumberFormatUCLetter: PbPageNumberFormat = ...
    pbPageNumberFormatUCRoman: PbPageNumberFormat = ...
    pbPageNumberFormatUCRus: PbPageNumberFormat = ...
    pbPageNumberFormatViet1: PbPageNumberFormat = ...
    pbPageNumberFormatZodiac1: PbPageNumberFormat = ...
    pbPageNumberFormatZodiac2: PbPageNumberFormat = ...
    value__ = ...


class PbPageNumberType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbPageNumberType, values: pbPageNumberCurrent (1), pbPageNumberNextInStory (2), pbPageNumberPreviousInStory (3) """
    pbPageNumberCurrent: PbPageNumberType = ...
    pbPageNumberNextInStory: PbPageNumberType = ...
    pbPageNumberPreviousInStory: PbPageNumberType = ...
    value__ = ...


class PbPageType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbPageType, values: pbPageLeftPage (1), pbPageMasterPage (4), pbPageRightPage (2), pbPageScratchPage (3) """
    pbPageLeftPage: PbPageType = ...
    pbPageMasterPage: PbPageType = ...
    pbPageRightPage: PbPageType = ...
    pbPageScratchPage: PbPageType = ...
    value__ = ...


class PbParagraphAlignmentType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbParagraphAlignmentType, values: pbParagraphAlignmentCenter (1), pbParagraphAlignmentDistribute (4), pbParagraphAlignmentDistributeAll (9), pbParagraphAlignmentDistributeCenterLast (10), pbParagraphAlignmentDistributeEastAsia (5), pbParagraphAlignmentInterCluster (8), pbParagraphAlignmentInterIdeograph (7), pbParagraphAlignmentInterWord (3), pbParagraphAlignmentJustified (6), pbParagraphAlignmentKashida (11), pbParagraphAlignmentLeft (0), pbParagraphAlignmentMixed (-9999999), pbParagraphAlignmentRight (2) """
    pbParagraphAlignmentCenter: PbParagraphAlignmentType = ...
    pbParagraphAlignmentDistribute: PbParagraphAlignmentType = ...
    pbParagraphAlignmentDistributeAll: PbParagraphAlignmentType = ...
    pbParagraphAlignmentDistributeCenterLast: PbParagraphAlignmentType = ...
    pbParagraphAlignmentDistributeEastAsia: PbParagraphAlignmentType = ...
    pbParagraphAlignmentInterCluster: PbParagraphAlignmentType = ...
    pbParagraphAlignmentInterIdeograph: PbParagraphAlignmentType = ...
    pbParagraphAlignmentInterWord: PbParagraphAlignmentType = ...
    pbParagraphAlignmentJustified: PbParagraphAlignmentType = ...
    pbParagraphAlignmentKashida: PbParagraphAlignmentType = ...
    pbParagraphAlignmentLeft: PbParagraphAlignmentType = ...
    pbParagraphAlignmentMixed: PbParagraphAlignmentType = ...
    pbParagraphAlignmentRight: PbParagraphAlignmentType = ...
    value__ = ...


class PbPersonalInfoSet(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbPersonalInfoSet, values: pbPersonalInfoHome (4), pbPersonalInfoOtherOrganization (3), pbPersonalInfoPrimaryBusiness (1), pbPersonalInfoSecondaryBusiness (2) """
    pbPersonalInfoHome: PbPersonalInfoSet = ...
    pbPersonalInfoOtherOrganization: PbPersonalInfoSet = ...
    pbPersonalInfoPrimaryBusiness: PbPersonalInfoSet = ...
    pbPersonalInfoSecondaryBusiness: PbPersonalInfoSet = ...
    value__ = ...


class PbPhoneticGuideAlignmentType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbPhoneticGuideAlignmentType, values: pbPhoneticGuideAlignmentCenter (3), pbPhoneticGuideAlignmentDefault (0), pbPhoneticGuideAlignmentLeft (4), pbPhoneticGuideAlignmentOneTwoOne (2), pbPhoneticGuideAlignmentRight (5), pbPhoneticGuideAlignmentZeroOneZero (1) """
    pbPhoneticGuideAlignmentCenter: PbPhoneticGuideAlignmentType = ...
    pbPhoneticGuideAlignmentDefault: PbPhoneticGuideAlignmentType = ...
    pbPhoneticGuideAlignmentLeft: PbPhoneticGuideAlignmentType = ...
    pbPhoneticGuideAlignmentOneTwoOne: PbPhoneticGuideAlignmentType = ...
    pbPhoneticGuideAlignmentRight: PbPhoneticGuideAlignmentType = ...
    pbPhoneticGuideAlignmentZeroOneZero: PbPhoneticGuideAlignmentType = ...
    value__ = ...


class PbPictureInsertAs(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbPictureInsertAs, values: pbPictureInsertAsEmbedded (1), pbPictureInsertAsLinked (2), pbPictureInsertAsOriginalState (3) """
    pbPictureInsertAsEmbedded: PbPictureInsertAs = ...
    pbPictureInsertAsLinked: PbPictureInsertAs = ...
    pbPictureInsertAsOriginalState: PbPictureInsertAs = ...
    value__ = ...


class pbPictureInsertFit(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum pbPictureInsertFit, values: pbFill (1), pbFit (0) """
    pbFill: pbPictureInsertFit = ...
    pbFit: pbPictureInsertFit = ...
    value__ = ...


class PbPictureResolution(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbPictureResolution, values: pbPictureResolutionCommercialPrint_300dpi (3), pbPictureResolutionDefault (0), pbPictureResolutionDesktopPrint_150dpi (2), pbPictureResolutionWeb_96dpi (1) """
    pbPictureResolutionCommercialPrint_300dpi: PbPictureResolution = ...
    pbPictureResolutionDefault: PbPictureResolution = ...
    pbPictureResolutionDesktopPrint_150dpi: PbPictureResolution = ...
    pbPictureResolutionWeb_96dpi: PbPictureResolution = ...
    value__ = ...


class PbPlacementType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbPlacementType, values: pbPlacementCenter (3), pbPlacementLeft (1), pbPlacementRight (2) """
    pbPlacementCenter: PbPlacementType = ...
    pbPlacementLeft: PbPlacementType = ...
    pbPlacementRight: PbPlacementType = ...
    value__ = ...


class pbPresetWordArt(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum pbPresetWordArt, values: pbPresetWordArt1 (0), pbPresetWordArt10 (9), pbPresetWordArt11 (10), pbPresetWordArt12 (11), pbPresetWordArt13 (12), pbPresetWordArt14 (13), pbPresetWordArt15 (14), pbPresetWordArt16 (15), pbPresetWordArt17 (16), pbPresetWordArt18 (17), pbPresetWordArt19 (18), pbPresetWordArt2 (1), pbPresetWordArt20 (19), pbPresetWordArt21 (20), pbPresetWordArt22 (21), pbPresetWordArt23 (22), pbPresetWordArt24 (23), pbPresetWordArt25 (24), pbPresetWordArt26 (25), pbPresetWordArt27 (26), pbPresetWordArt28 (27), pbPresetWordArt29 (28), pbPresetWordArt3 (2), pbPresetWordArt30 (29), pbPresetWordArt31 (30), pbPresetWordArt32 (31), pbPresetWordArt33 (32), pbPresetWordArt34 (33), pbPresetWordArt35 (34), pbPresetWordArt36 (35), pbPresetWordArt37 (36), pbPresetWordArt38 (37), pbPresetWordArt39 (38), pbPresetWordArt4 (3), pbPresetWordArt40 (39), pbPresetWordArt41 (40), pbPresetWordArt42 (41), pbPresetWordArt43 (42), pbPresetWordArt44 (43), pbPresetWordArt45 (44), pbPresetWordArt46 (45), pbPresetWordArt47 (46), pbPresetWordArt48 (47), pbPresetWordArt49 (48), pbPresetWordArt5 (4), pbPresetWordArt50 (49), pbPresetWordArt51 (50), pbPresetWordArt52 (51), pbPresetWordArt53 (52), pbPresetWordArt54 (53), pbPresetWordArt55 (54), pbPresetWordArt56 (55), pbPresetWordArt57 (56), pbPresetWordArt58 (57), pbPresetWordArt59 (58), pbPresetWordArt6 (5), pbPresetWordArt60 (59), pbPresetWordArt7 (6), pbPresetWordArt8 (7), pbPresetWordArt9 (8), pbPresetWordArtMixed (-2) """
    pbPresetWordArt1: pbPresetWordArt = ...
    pbPresetWordArt10: pbPresetWordArt = ...
    pbPresetWordArt11: pbPresetWordArt = ...
    pbPresetWordArt12: pbPresetWordArt = ...
    pbPresetWordArt13: pbPresetWordArt = ...
    pbPresetWordArt14: pbPresetWordArt = ...
    pbPresetWordArt15: pbPresetWordArt = ...
    pbPresetWordArt16: pbPresetWordArt = ...
    pbPresetWordArt17: pbPresetWordArt = ...
    pbPresetWordArt18: pbPresetWordArt = ...
    pbPresetWordArt19: pbPresetWordArt = ...
    pbPresetWordArt2: pbPresetWordArt = ...
    pbPresetWordArt20: pbPresetWordArt = ...
    pbPresetWordArt21: pbPresetWordArt = ...
    pbPresetWordArt22: pbPresetWordArt = ...
    pbPresetWordArt23: pbPresetWordArt = ...
    pbPresetWordArt24: pbPresetWordArt = ...
    pbPresetWordArt25: pbPresetWordArt = ...
    pbPresetWordArt26: pbPresetWordArt = ...
    pbPresetWordArt27: pbPresetWordArt = ...
    pbPresetWordArt28: pbPresetWordArt = ...
    pbPresetWordArt29: pbPresetWordArt = ...
    pbPresetWordArt3: pbPresetWordArt = ...
    pbPresetWordArt30: pbPresetWordArt = ...
    pbPresetWordArt31: pbPresetWordArt = ...
    pbPresetWordArt32: pbPresetWordArt = ...
    pbPresetWordArt33: pbPresetWordArt = ...
    pbPresetWordArt34: pbPresetWordArt = ...
    pbPresetWordArt35: pbPresetWordArt = ...
    pbPresetWordArt36: pbPresetWordArt = ...
    pbPresetWordArt37: pbPresetWordArt = ...
    pbPresetWordArt38: pbPresetWordArt = ...
    pbPresetWordArt39: pbPresetWordArt = ...
    pbPresetWordArt4: pbPresetWordArt = ...
    pbPresetWordArt40: pbPresetWordArt = ...
    pbPresetWordArt41: pbPresetWordArt = ...
    pbPresetWordArt42: pbPresetWordArt = ...
    pbPresetWordArt43: pbPresetWordArt = ...
    pbPresetWordArt44: pbPresetWordArt = ...
    pbPresetWordArt45: pbPresetWordArt = ...
    pbPresetWordArt46: pbPresetWordArt = ...
    pbPresetWordArt47: pbPresetWordArt = ...
    pbPresetWordArt48: pbPresetWordArt = ...
    pbPresetWordArt49: pbPresetWordArt = ...
    pbPresetWordArt5: pbPresetWordArt = ...
    pbPresetWordArt50: pbPresetWordArt = ...
    pbPresetWordArt51: pbPresetWordArt = ...
    pbPresetWordArt52: pbPresetWordArt = ...
    pbPresetWordArt53: pbPresetWordArt = ...
    pbPresetWordArt54: pbPresetWordArt = ...
    pbPresetWordArt55: pbPresetWordArt = ...
    pbPresetWordArt56: pbPresetWordArt = ...
    pbPresetWordArt57: pbPresetWordArt = ...
    pbPresetWordArt58: pbPresetWordArt = ...
    pbPresetWordArt59: pbPresetWordArt = ...
    pbPresetWordArt6: pbPresetWordArt = ...
    pbPresetWordArt60: pbPresetWordArt = ...
    pbPresetWordArt7: pbPresetWordArt = ...
    pbPresetWordArt8: pbPresetWordArt = ...
    pbPresetWordArt9: pbPresetWordArt = ...
    pbPresetWordArtMixed: pbPresetWordArt = ...
    value__ = ...


class PbPrintGraphics(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbPrintGraphics, values: pbPrintHighResolution (1), pbPrintLowResolution (2), pbPrintNoGraphics (3) """
    pbPrintHighResolution: PbPrintGraphics = ...
    pbPrintLowResolution: PbPrintGraphics = ...
    pbPrintNoGraphics: PbPrintGraphics = ...
    value__ = ...


class PbPrintMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbPrintMode, values: pbPrintModeCompositeCMYK (3), pbPrintModeCompositeGrayscale (4), pbPrintModeCompositeRGB (1), pbPrintModeSeparations (2) """
    pbPrintModeCompositeCMYK: PbPrintMode = ...
    pbPrintModeCompositeGrayscale: PbPrintMode = ...
    pbPrintModeCompositeRGB: PbPrintMode = ...
    pbPrintModeSeparations: PbPrintMode = ...
    value__ = ...


class PbPrintStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbPrintStyle, values: pbPrintStyleBookletSideFold (5), pbPrintStyleBookletTopFold (6), pbPrintStyleDefault (0), pbPrintStyleEnvelope (11), pbPrintStyleHalfFoldSide (7), pbPrintStyleHalfFoldTop (8), pbPrintStyleMultipleCopiesPerSheet (3), pbPrintStyleMultiplePagesPerSheet (4), pbPrintStyleOnePagePerSheet (1), pbPrintStyleQuarterFoldSide (10), pbPrintStyleQuarterFoldTop (9), pbPrintStyleTiled (2) """
    pbPrintStyleBookletSideFold: PbPrintStyle = ...
    pbPrintStyleBookletTopFold: PbPrintStyle = ...
    pbPrintStyleDefault: PbPrintStyle = ...
    pbPrintStyleEnvelope: PbPrintStyle = ...
    pbPrintStyleHalfFoldSide: PbPrintStyle = ...
    pbPrintStyleHalfFoldTop: PbPrintStyle = ...
    pbPrintStyleMultipleCopiesPerSheet: PbPrintStyle = ...
    pbPrintStyleMultiplePagesPerSheet: PbPrintStyle = ...
    pbPrintStyleOnePagePerSheet: PbPrintStyle = ...
    pbPrintStyleQuarterFoldSide: PbPrintStyle = ...
    pbPrintStyleQuarterFoldTop: PbPrintStyle = ...
    pbPrintStyleTiled: PbPrintStyle = ...
    value__ = ...


class PbPublicationLayout(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbPublicationLayout, values: pbLayout4x6BaePan (10), pbLayout4x6BanPan (12), pbLayout4x6Pan (11), pbLayoutAdvertisement (36), pbLayoutAwardCertificate (37), pbLayoutBanner (38), pbLayoutBannerCustom (27), pbLayoutBannerLarge (26), pbLayoutBannerMedium (25), pbLayoutBannerSmall (24), pbLayoutBook (2), pbLayoutBrochure (39), pbLayoutBusinessCard (40), pbLayoutBusinessCardEurope (18), pbLayoutBusinessCardFE (19), pbLayoutBusinessCardLocal (20), pbLayoutBusinessCardUS (17), pbLayoutBusinessForm (41), pbLayoutCalendar (42), pbLayoutCatalog (43), pbLayoutCrownPan (13), pbLayoutCustom (23), pbLayoutEmail (44), pbLayoutEnvelope (33), pbLayoutFlyer (45), pbLayoutFoldCard (3), pbLayoutFullPage (1), pbLayoutGiftCertificate (46), pbLayoutGreetingCard (47), pbLayoutGreetingCardL (4), pbLayoutGreetingCardT (5), pbLayoutIndexCard (16), pbLayoutInvitationCard (49), pbLayoutJang4x6Pan (15), pbLayoutKookBaePan (6), pbLayoutKookBanPan (9), pbLayoutKookPan (7), pbLayoutLabel (32), pbLayoutLetterhead (50), pbLayoutMenu (51), pbLayoutNewsletter (52), pbLayoutPaperFoldingProject (53), pbLayoutPostcard (54), pbLayoutPostcardA4 (30), pbLayoutPostcardHalfLetter (29), pbLayoutPostcardJapan (31), pbLayoutPostcardUS (28), pbLayoutPosterLarge (22), pbLayoutPosterSmall (21), pbLayoutProgram (55), pbLayoutQuickPublication (60), pbLayoutResume (56), pbLayoutShinKookPan (8), pbLayoutShinSeoPan (14), pbLayoutSign (57), pbLayoutWebPageLarge (35), pbLayoutWebPageSmall (34), pbLayoutWebSite (59), pbLayoutWithComplimentsCard (58), pbLayoutWordImport (48) """
    pbLayout4x6BaePan: PbPublicationLayout = ...
    pbLayout4x6BanPan: PbPublicationLayout = ...
    pbLayout4x6Pan: PbPublicationLayout = ...
    pbLayoutAdvertisement: PbPublicationLayout = ...
    pbLayoutAwardCertificate: PbPublicationLayout = ...
    pbLayoutBanner: PbPublicationLayout = ...
    pbLayoutBannerCustom: PbPublicationLayout = ...
    pbLayoutBannerLarge: PbPublicationLayout = ...
    pbLayoutBannerMedium: PbPublicationLayout = ...
    pbLayoutBannerSmall: PbPublicationLayout = ...
    pbLayoutBook: PbPublicationLayout = ...
    pbLayoutBrochure: PbPublicationLayout = ...
    pbLayoutBusinessCard: PbPublicationLayout = ...
    pbLayoutBusinessCardEurope: PbPublicationLayout = ...
    pbLayoutBusinessCardFE: PbPublicationLayout = ...
    pbLayoutBusinessCardLocal: PbPublicationLayout = ...
    pbLayoutBusinessCardUS: PbPublicationLayout = ...
    pbLayoutBusinessForm: PbPublicationLayout = ...
    pbLayoutCalendar: PbPublicationLayout = ...
    pbLayoutCatalog: PbPublicationLayout = ...
    pbLayoutCrownPan: PbPublicationLayout = ...
    pbLayoutCustom: PbPublicationLayout = ...
    pbLayoutEmail: PbPublicationLayout = ...
    pbLayoutEnvelope: PbPublicationLayout = ...
    pbLayoutFlyer: PbPublicationLayout = ...
    pbLayoutFoldCard: PbPublicationLayout = ...
    pbLayoutFullPage: PbPublicationLayout = ...
    pbLayoutGiftCertificate: PbPublicationLayout = ...
    pbLayoutGreetingCard: PbPublicationLayout = ...
    pbLayoutGreetingCardL: PbPublicationLayout = ...
    pbLayoutGreetingCardT: PbPublicationLayout = ...
    pbLayoutIndexCard: PbPublicationLayout = ...
    pbLayoutInvitationCard: PbPublicationLayout = ...
    pbLayoutJang4x6Pan: PbPublicationLayout = ...
    pbLayoutKookBaePan: PbPublicationLayout = ...
    pbLayoutKookBanPan: PbPublicationLayout = ...
    pbLayoutKookPan: PbPublicationLayout = ...
    pbLayoutLabel: PbPublicationLayout = ...
    pbLayoutLetterhead: PbPublicationLayout = ...
    pbLayoutMenu: PbPublicationLayout = ...
    pbLayoutNewsletter: PbPublicationLayout = ...
    pbLayoutPaperFoldingProject: PbPublicationLayout = ...
    pbLayoutPostcard: PbPublicationLayout = ...
    pbLayoutPostcardA4: PbPublicationLayout = ...
    pbLayoutPostcardHalfLetter: PbPublicationLayout = ...
    pbLayoutPostcardJapan: PbPublicationLayout = ...
    pbLayoutPostcardUS: PbPublicationLayout = ...
    pbLayoutPosterLarge: PbPublicationLayout = ...
    pbLayoutPosterSmall: PbPublicationLayout = ...
    pbLayoutProgram: PbPublicationLayout = ...
    pbLayoutQuickPublication: PbPublicationLayout = ...
    pbLayoutResume: PbPublicationLayout = ...
    pbLayoutShinKookPan: PbPublicationLayout = ...
    pbLayoutShinSeoPan: PbPublicationLayout = ...
    pbLayoutSign: PbPublicationLayout = ...
    pbLayoutWebPageLarge: PbPublicationLayout = ...
    pbLayoutWebPageSmall: PbPublicationLayout = ...
    pbLayoutWebSite: PbPublicationLayout = ...
    pbLayoutWithComplimentsCard: PbPublicationLayout = ...
    pbLayoutWordImport: PbPublicationLayout = ...
    value__ = ...


class PbPublicationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbPublicationType, values: pbTypePrint (1), pbTypeWeb (2) """
    pbTypePrint: PbPublicationType = ...
    pbTypeWeb: PbPublicationType = ...
    value__ = ...


class PbRecipientListFileType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbRecipientListFileType, values: pbAsCsvFile (1), pbAsMdbFile (0) """
    pbAsCsvFile: PbRecipientListFileType = ...
    pbAsMdbFile: PbRecipientListFileType = ...
    value__ = ...


class PbReplaceScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbReplaceScope, values: pbReplaceScopeAll (2), pbReplaceScopeNone (0), pbReplaceScopeOne (1) """
    pbReplaceScopeAll: PbReplaceScope = ...
    pbReplaceScopeNone: PbReplaceScope = ...
    pbReplaceScopeOne: PbReplaceScope = ...
    value__ = ...


class PbReplaceTint(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbReplaceTint, values: pbReplaceTintKeepTints (1), pbReplaceTintMaintainLuminosity (2), pbReplaceTintUseDefault (0) """
    pbReplaceTintKeepTints: PbReplaceTint = ...
    pbReplaceTintMaintainLuminosity: PbReplaceTint = ...
    pbReplaceTintUseDefault: PbReplaceTint = ...
    value__ = ...


class PbRulerGuideType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbRulerGuideType, values: pbRulerGuideTypeHorizontal (2), pbRulerGuideTypeVertical (1) """
    pbRulerGuideTypeHorizontal: PbRulerGuideType = ...
    pbRulerGuideTypeVertical: PbRulerGuideType = ...
    value__ = ...


class PbSaveOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbSaveOptions, values: pbDoNotSaveChanges (3), pbPromptToSaveChanges (1), pbSaveChanges (2) """
    pbDoNotSaveChanges: PbSaveOptions = ...
    pbPromptToSaveChanges: PbSaveOptions = ...
    pbSaveChanges: PbSaveOptions = ...
    value__ = ...


class PbSchemeColorIndex(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbSchemeColorIndex, values: pbSchemeColorAccent1 (2), pbSchemeColorAccent2 (3), pbSchemeColorAccent3 (4), pbSchemeColorAccent4 (5), pbSchemeColorAccent5 (8), pbSchemeColorFollowedHyperlink (7), pbSchemeColorHyperlink (6), pbSchemeColorMain (1), pbSchemeColorNone (0) """
    pbSchemeColorAccent1: PbSchemeColorIndex = ...
    pbSchemeColorAccent2: PbSchemeColorIndex = ...
    pbSchemeColorAccent3: PbSchemeColorIndex = ...
    pbSchemeColorAccent4: PbSchemeColorIndex = ...
    pbSchemeColorAccent5: PbSchemeColorIndex = ...
    pbSchemeColorFollowedHyperlink: PbSchemeColorIndex = ...
    pbSchemeColorHyperlink: PbSchemeColorIndex = ...
    pbSchemeColorMain: PbSchemeColorIndex = ...
    pbSchemeColorNone: PbSchemeColorIndex = ...
    value__ = ...


class PbSelectionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbSelectionType, values: pbSelectionNone (0), pbSelectionShape (1), pbSelectionShapeSubSelection (4), pbSelectionTableCells (3), pbSelectionText (2) """
    pbSelectionNone: PbSelectionType = ...
    pbSelectionShape: PbSelectionType = ...
    pbSelectionShapeSubSelection: PbSelectionType = ...
    pbSelectionTableCells: PbSelectionType = ...
    pbSelectionText: PbSelectionType = ...
    value__ = ...


class PbShapeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbShapeType, values: pbAutoShape (1), pbBarCodePictureHolder (113), pbCallout (2), pbCatalogMergeArea (111), pbChart (3), pbComment (4), pbEmbeddedOLEObject (7), pbFormControl (8), pbFreeform (5), pbGroup (6), pbGroupWizard (108), pbLine (9), pbLinkedOLEObject (10), pbLinkedPicture (11), pbMedia (16), pbOLEControlObject (12), pbPicture (13), pbPlaceholder (14), pbShapeTypeMixed (-2), pbTable (18), pbTextEffect (15), pbTextFrame (17), pbWebCheckBox (100), pbWebCommandButton (101), pbWebHotSpot (110), pbWebHTMLFragment (107), pbWebListBox (102), pbWebMultiLineTextBox (103), pbWebNavigationBar (112), pbWebOptionButton (104), pbWebSingleLineTextBox (105), pbWebWebComponent (106) """
    pbAutoShape: PbShapeType = ...
    pbBarCodePictureHolder: PbShapeType = ...
    pbCallout: PbShapeType = ...
    pbCatalogMergeArea: PbShapeType = ...
    pbChart: PbShapeType = ...
    pbComment: PbShapeType = ...
    pbEmbeddedOLEObject: PbShapeType = ...
    pbFormControl: PbShapeType = ...
    pbFreeform: PbShapeType = ...
    pbGroup: PbShapeType = ...
    pbGroupWizard: PbShapeType = ...
    pbLine: PbShapeType = ...
    pbLinkedOLEObject: PbShapeType = ...
    pbLinkedPicture: PbShapeType = ...
    pbMedia: PbShapeType = ...
    pbOLEControlObject: PbShapeType = ...
    pbPicture: PbShapeType = ...
    pbPlaceholder: PbShapeType = ...
    pbShapeTypeMixed: PbShapeType = ...
    pbTable: PbShapeType = ...
    pbTextEffect: PbShapeType = ...
    pbTextFrame: PbShapeType = ...
    pbWebCheckBox: PbShapeType = ...
    pbWebCommandButton: PbShapeType = ...
    pbWebHotSpot: PbShapeType = ...
    pbWebHTMLFragment: PbShapeType = ...
    pbWebListBox: PbShapeType = ...
    pbWebMultiLineTextBox: PbShapeType = ...
    pbWebNavigationBar: PbShapeType = ...
    pbWebOptionButton: PbShapeType = ...
    pbWebSingleLineTextBox: PbShapeType = ...
    pbWebWebComponent: PbShapeType = ...
    value__ = ...


class PbShowDialog(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbShowDialog, values: pbDefaultBehavior (1), PbShowDialog (2), pbSuppressDialog (3) """
    pbDefaultBehavior: PbShowDialog = ...
    PbShowDialog: PbShowDialog = ...
    pbSuppressDialog: PbShowDialog = ...
    value__ = ...


class PbSpotColor(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbSpotColor, values: pbInkNone (0) """
    pbInkNone: PbSpotColor = ...
    value__ = ...


class PbStoryType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbStoryType, values: pbStoryContinuedFrom (2), pbStoryContinuedOn (3), pbStoryTable (0), pbStoryTextFrame (1) """
    pbStoryContinuedFrom: PbStoryType = ...
    pbStoryContinuedOn: PbStoryType = ...
    pbStoryTable: PbStoryType = ...
    pbStoryTextFrame: PbStoryType = ...
    value__ = ...


class PbSubmitDataFormatType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbSubmitDataFormatType, values: pbSubmitDataFormatCSV (3), pbSubmitDataFormatHTML (1), pbSubmitDataFormatRichText (2), pbSubmitDataFormatTab (4) """
    pbSubmitDataFormatCSV: PbSubmitDataFormatType = ...
    pbSubmitDataFormatHTML: PbSubmitDataFormatType = ...
    pbSubmitDataFormatRichText: PbSubmitDataFormatType = ...
    pbSubmitDataFormatTab: PbSubmitDataFormatType = ...
    value__ = ...


class PbSubmitDataRetrievalMethodType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbSubmitDataRetrievalMethodType, values: pbSubmitDataRetrievalEmail (2), pbSubmitDataRetrievalProgram (3), pbSubmitDataRetrievalSaveOnServer (1) """
    pbSubmitDataRetrievalEmail: PbSubmitDataRetrievalMethodType = ...
    pbSubmitDataRetrievalProgram: PbSubmitDataRetrievalMethodType = ...
    pbSubmitDataRetrievalSaveOnServer: PbSubmitDataRetrievalMethodType = ...
    value__ = ...


class PbTabAlignmentType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbTabAlignmentType, values: pbTabAlignmentCenter (1), pbTabAlignmentDecimal (3), pbTabAlignmentLeading (0), pbTabAlignmentTrailing (2) """
    pbTabAlignmentCenter: PbTabAlignmentType = ...
    pbTabAlignmentDecimal: PbTabAlignmentType = ...
    pbTabAlignmentLeading: PbTabAlignmentType = ...
    pbTabAlignmentTrailing: PbTabAlignmentType = ...
    value__ = ...


class PbTabLeaderType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbTabLeaderType, values: pbTabLeaderBullet (5), pbTabLeaderDashes (2), pbTabLeaderDot (1), pbTabLeaderLine (3), pbTabLeaderNone (0) """
    pbTabLeaderBullet: PbTabLeaderType = ...
    pbTabLeaderDashes: PbTabLeaderType = ...
    pbTabLeaderDot: PbTabLeaderType = ...
    pbTabLeaderLine: PbTabLeaderType = ...
    pbTabLeaderNone: PbTabLeaderType = ...
    value__ = ...


class PbTableAutoFormatType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbTableAutoFormatType, values: pbTableAutoFormatCheckbookRegister (0), pbTableAutoFormatCheckerboard (20), pbTableAutoFormatDefault (-3), pbTableAutoFormatList1 (1), pbTableAutoFormatList2 (2), pbTableAutoFormatList3 (3), pbTableAutoFormatList4 (4), pbTableAutoFormatList5 (5), pbTableAutoFormatList6 (6), pbTableAutoFormatList7 (7), pbTableAutoFormatListWithTitle1 (8), pbTableAutoFormatListWithTitle2 (9), pbTableAutoFormatListWithTitle3 (10), pbTableAutoFormatMixed (-1), pbTableAutoFormatNone (-2), pbTableAutoFormatNumbers1 (11), pbTableAutoFormatNumbers2 (12), pbTableAutoFormatNumbers3 (13), pbTableAutoFormatNumbers4 (14), pbTableAutoFormatNumbers5 (15), pbTableAutoFormatNumbers6 (16), pbTableAutoFormatTableOfContents1 (17), pbTableAutoFormatTableOfContents2 (18), pbTableAutoFormatTableOfContents3 (19) """
    pbTableAutoFormatCheckbookRegister: PbTableAutoFormatType = ...
    pbTableAutoFormatCheckerboard: PbTableAutoFormatType = ...
    pbTableAutoFormatDefault: PbTableAutoFormatType = ...
    pbTableAutoFormatList1: PbTableAutoFormatType = ...
    pbTableAutoFormatList2: PbTableAutoFormatType = ...
    pbTableAutoFormatList3: PbTableAutoFormatType = ...
    pbTableAutoFormatList4: PbTableAutoFormatType = ...
    pbTableAutoFormatList5: PbTableAutoFormatType = ...
    pbTableAutoFormatList6: PbTableAutoFormatType = ...
    pbTableAutoFormatList7: PbTableAutoFormatType = ...
    pbTableAutoFormatListWithTitle1: PbTableAutoFormatType = ...
    pbTableAutoFormatListWithTitle2: PbTableAutoFormatType = ...
    pbTableAutoFormatListWithTitle3: PbTableAutoFormatType = ...
    pbTableAutoFormatMixed: PbTableAutoFormatType = ...
    pbTableAutoFormatNone: PbTableAutoFormatType = ...
    pbTableAutoFormatNumbers1: PbTableAutoFormatType = ...
    pbTableAutoFormatNumbers2: PbTableAutoFormatType = ...
    pbTableAutoFormatNumbers3: PbTableAutoFormatType = ...
    pbTableAutoFormatNumbers4: PbTableAutoFormatType = ...
    pbTableAutoFormatNumbers5: PbTableAutoFormatType = ...
    pbTableAutoFormatNumbers6: PbTableAutoFormatType = ...
    pbTableAutoFormatTableOfContents1: PbTableAutoFormatType = ...
    pbTableAutoFormatTableOfContents2: PbTableAutoFormatType = ...
    pbTableAutoFormatTableOfContents3: PbTableAutoFormatType = ...
    value__ = ...


class PbTableDirectionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbTableDirectionType, values: pbTableDirectionLeftToRight (1), pbTableDirectionRightToLeft (2) """
    pbTableDirectionLeftToRight: PbTableDirectionType = ...
    pbTableDirectionRightToLeft: PbTableDirectionType = ...
    value__ = ...


class PbTextAutoFitType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbTextAutoFitType, values: pbTextAutoFitBestFit (2), pbTextAutoFitGrowToFit (3), pbTextAutoFitNone (0), pbTextAutoFitShrinkOnOverflow (1) """
    pbTextAutoFitBestFit: PbTextAutoFitType = ...
    pbTextAutoFitGrowToFit: PbTextAutoFitType = ...
    pbTextAutoFitNone: PbTextAutoFitType = ...
    pbTextAutoFitShrinkOnOverflow: PbTextAutoFitType = ...
    value__ = ...


class PbTextDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbTextDirection, values: pbTextDirectionLeftToRight (1), pbTextDirectionMixed (-9999999), pbTextDirectionRightToLeft (2) """
    pbTextDirectionLeftToRight: PbTextDirection = ...
    pbTextDirectionMixed: PbTextDirection = ...
    pbTextDirectionRightToLeft: PbTextDirection = ...
    value__ = ...


class PbTextOrientation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbTextOrientation, values: pbTextOrientationHorizontal (1), pbTextOrientationMixed (-2), pbTextOrientationRightToLeft (256), pbTextOrientationVerticalEastAsia (2) """
    pbTextOrientationHorizontal: PbTextOrientation = ...
    pbTextOrientationMixed: PbTextOrientation = ...
    pbTextOrientationRightToLeft: PbTextOrientation = ...
    pbTextOrientationVerticalEastAsia: PbTextOrientation = ...
    value__ = ...


class PbTextUnit(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbTextUnit, values: pbTextUnitCell (12), pbTextUnitCharacter (1), pbTextUnitCharFormat (13), pbTextUnitCodePoint (17), pbTextUnitColumn (9), pbTextUnitLine (5), pbTextUnitObject (16), pbTextUnitParaFormat (14), pbTextUnitParagraph (4), pbTextUnitRow (10), pbTextUnitScreen (7), pbTextUnitSection (8), pbTextUnitSentence (3), pbTextUnitStory (6), pbTextUnitTable (15), pbTextUnitWindow (11), pbTextUnitWord (2) """
    pbTextUnitCell: PbTextUnit = ...
    pbTextUnitCharacter: PbTextUnit = ...
    pbTextUnitCharFormat: PbTextUnit = ...
    pbTextUnitCodePoint: PbTextUnit = ...
    pbTextUnitColumn: PbTextUnit = ...
    pbTextUnitLine: PbTextUnit = ...
    pbTextUnitObject: PbTextUnit = ...
    pbTextUnitParaFormat: PbTextUnit = ...
    pbTextUnitParagraph: PbTextUnit = ...
    pbTextUnitRow: PbTextUnit = ...
    pbTextUnitScreen: PbTextUnit = ...
    pbTextUnitSection: PbTextUnit = ...
    pbTextUnitSentence: PbTextUnit = ...
    pbTextUnitStory: PbTextUnit = ...
    pbTextUnitTable: PbTextUnit = ...
    pbTextUnitWindow: PbTextUnit = ...
    pbTextUnitWord: PbTextUnit = ...
    value__ = ...


class PbTrackingPresetType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbTrackingPresetType, values: pbTrackingCustom (-1), pbTrackingLoose (1), pbTrackingMixed (-2), pbTrackingNormal (2), pbTrackingTight (3), pbTrackingVeryLoose (0), pbTrackingVeryTight (4) """
    pbTrackingCustom: PbTrackingPresetType = ...
    pbTrackingLoose: PbTrackingPresetType = ...
    pbTrackingMixed: PbTrackingPresetType = ...
    pbTrackingNormal: PbTrackingPresetType = ...
    pbTrackingTight: PbTrackingPresetType = ...
    pbTrackingVeryLoose: PbTrackingPresetType = ...
    pbTrackingVeryTight: PbTrackingPresetType = ...
    value__ = ...


class PbUnderlineType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbUnderlineType, values: pbUnderlineDash (6), pbUnderlineDashHeavy (12), pbUnderlineDashLong (15), pbUnderlineDashLongHeavy (16), pbUnderlineDotDash (7), pbUnderlineDotDashHeavy (13), pbUnderlineDotDotDash (8), pbUnderlineDotDotDashHeavy (14), pbUnderlineDotHeavy (11), pbUnderlineDotted (4), pbUnderlineDouble (3), pbUnderlineMixed (-1), pbUnderlineNone (0), pbUnderlineSingle (1), pbUnderlineThick (5), pbUnderlineWavy (9), pbUnderlineWavyDouble (17), pbUnderlineWavyHeavy (10), pbUnderlineWordsOnly (2) """
    pbUnderlineDash: PbUnderlineType = ...
    pbUnderlineDashHeavy: PbUnderlineType = ...
    pbUnderlineDashLong: PbUnderlineType = ...
    pbUnderlineDashLongHeavy: PbUnderlineType = ...
    pbUnderlineDotDash: PbUnderlineType = ...
    pbUnderlineDotDashHeavy: PbUnderlineType = ...
    pbUnderlineDotDotDash: PbUnderlineType = ...
    pbUnderlineDotDotDashHeavy: PbUnderlineType = ...
    pbUnderlineDotHeavy: PbUnderlineType = ...
    pbUnderlineDotted: PbUnderlineType = ...
    pbUnderlineDouble: PbUnderlineType = ...
    pbUnderlineMixed: PbUnderlineType = ...
    pbUnderlineNone: PbUnderlineType = ...
    pbUnderlineSingle: PbUnderlineType = ...
    pbUnderlineThick: PbUnderlineType = ...
    pbUnderlineWavy: PbUnderlineType = ...
    pbUnderlineWavyDouble: PbUnderlineType = ...
    pbUnderlineWavyHeavy: PbUnderlineType = ...
    pbUnderlineWordsOnly: PbUnderlineType = ...
    value__ = ...


class PbUnitType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbUnitType, values: pbUnitCM (1), pbUnitEmu (4), pbUnitFeet (6), pbUnitHa (9), pbUnitInch (0), pbUnitKyu (8), pbUnitMeter (7), pbUnitPica (2), pbUnitPixel (10), pbUnitPoint (3), pbUnitTwip (5) """
    pbUnitCM: PbUnitType = ...
    pbUnitEmu: PbUnitType = ...
    pbUnitFeet: PbUnitType = ...
    pbUnitHa: PbUnitType = ...
    pbUnitInch: PbUnitType = ...
    pbUnitKyu: PbUnitType = ...
    pbUnitMeter: PbUnitType = ...
    pbUnitPica: PbUnitType = ...
    pbUnitPixel: PbUnitType = ...
    pbUnitPoint: PbUnitType = ...
    pbUnitTwip: PbUnitType = ...
    value__ = ...


class PbVerticalPictureLocking(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbVerticalPictureLocking, values: pbVerticalLockingBottom (2), pbVerticalLockingNone (0), pbVerticalLockingStretch (3), pbVerticalLockingTop (1) """
    pbVerticalLockingBottom: PbVerticalPictureLocking = ...
    pbVerticalLockingNone: PbVerticalPictureLocking = ...
    pbVerticalLockingStretch: PbVerticalPictureLocking = ...
    pbVerticalLockingTop: PbVerticalPictureLocking = ...
    value__ = ...


class PbVerticalTextAlignmentType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbVerticalTextAlignmentType, values: pbVerticalTextAlignmentBottom (2), pbVerticalTextAlignmentCenter (1), pbVerticalTextAlignmentTop (0) """
    pbVerticalTextAlignmentBottom: PbVerticalTextAlignmentType = ...
    pbVerticalTextAlignmentCenter: PbVerticalTextAlignmentType = ...
    pbVerticalTextAlignmentTop: PbVerticalTextAlignmentType = ...
    value__ = ...


class PbWebControlType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbWebControlType, values: pbWebControlCheckBox (100), pbWebControlCommandButton (101), pbWebControlHotSpot (110), pbWebControlHTMLFragment (107), pbWebControlListBox (102), pbWebControlMultiLineTextBox (103), pbWebControlOptionButton (104), pbWebControlSingleLineTextBox (105), pbWebControlWebComponent (106) """
    pbWebControlCheckBox: PbWebControlType = ...
    pbWebControlCommandButton: PbWebControlType = ...
    pbWebControlHotSpot: PbWebControlType = ...
    pbWebControlHTMLFragment: PbWebControlType = ...
    pbWebControlListBox: PbWebControlType = ...
    pbWebControlMultiLineTextBox: PbWebControlType = ...
    pbWebControlOptionButton: PbWebControlType = ...
    pbWebControlSingleLineTextBox: PbWebControlType = ...
    pbWebControlWebComponent: PbWebControlType = ...
    value__ = ...


class PbWindowState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbWindowState, values: pbWindowStateMaximize (0), pbWindowStateMinimize (1), pbWindowStateNormal (2) """
    pbWindowStateMaximize: PbWindowState = ...
    pbWindowStateMinimize: PbWindowState = ...
    pbWindowStateNormal: PbWindowState = ...
    value__ = ...


class PbWizard(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbWizard, values: pbWizardAdvertisements (12), pbWizardAirplanes (23), pbWizardBanners (21), pbWizardBrochures (8), pbWizardBusinessCards (3), pbWizardBusinessForms (20), pbWizardCalendars (13), pbWizardCatalogs (161), pbWizardCertificates (62), pbWizardEmailActivityEvent (302), pbWizardEmailAutomatic (305), pbWizardEmailFeaturedProduct (304), pbWizardEmailLetter (300), pbWizardEmailNewsletter (39), pbWizardEmailProductList (303), pbWizardEmailSpeakerEvent (301), pbWizardEnvelopes (7), pbWizardFlyers (16), pbWizardGiftCertificates (63), pbWizardGreetingCard (40), pbWizardInvitation (41), pbWizardJapaneseAdvertisements (165), pbWizardJapaneseAirplanes (164), pbWizardJapaneseBanners (121), pbWizardJapaneseBrochures (92), pbWizardJapaneseBusinessCards (91), pbWizardJapaneseBusinessForms (123), pbWizardJapaneseCalendars (82), pbWizardJapaneseCatalogs (177), pbWizardJapaneseCertificates (119), pbWizardJapaneseEnvelopes (93), pbWizardJapaneseFlyers (94), pbWizardJapaneseGiftCertificates (122), pbWizardJapaneseGreetingCards (80), pbWizardJapaneseInvitations (81), pbWizardJapaneseLabels (118), pbWizardJapaneseLetterheads (95), pbWizardJapaneseMenus (116), pbWizardJapaneseNewsletters (117), pbWizardJapaneseOrigami (163), pbWizardJapanesePostcards (78), pbWizardJapanesePrograms (115), pbWizardJapaneseSigns (149), pbWizardJapaneseWebSites (120), pbWizardLabels (19), pbWizardLetterheads (6), pbWizardMenus (59), pbWizardNewsletters (9), pbWizardNone (0), pbWizardOrigami (22), pbWizardPostcards (10), pbWizardPrograms (76), pbWizardQuickPublications (179), pbWizardResumes (18), pbWizardSigns (17), pbWizardWebSiteBlank (203), pbWizardWebSiteHomePage (5), pbWizardWebSiteProductSales (201), pbWizardWebSiteServices (202), pbWizardWebSiteThreePage (200), pbWizardWithComplimentsCards (73), pbWizardWordDocument (189) """
    pbWizardAdvertisements: PbWizard = ...
    pbWizardAirplanes: PbWizard = ...
    pbWizardBanners: PbWizard = ...
    pbWizardBrochures: PbWizard = ...
    pbWizardBusinessCards: PbWizard = ...
    pbWizardBusinessForms: PbWizard = ...
    pbWizardCalendars: PbWizard = ...
    pbWizardCatalogs: PbWizard = ...
    pbWizardCertificates: PbWizard = ...
    pbWizardEmailActivityEvent: PbWizard = ...
    pbWizardEmailAutomatic: PbWizard = ...
    pbWizardEmailFeaturedProduct: PbWizard = ...
    pbWizardEmailLetter: PbWizard = ...
    pbWizardEmailNewsletter: PbWizard = ...
    pbWizardEmailProductList: PbWizard = ...
    pbWizardEmailSpeakerEvent: PbWizard = ...
    pbWizardEnvelopes: PbWizard = ...
    pbWizardFlyers: PbWizard = ...
    pbWizardGiftCertificates: PbWizard = ...
    pbWizardGreetingCard: PbWizard = ...
    pbWizardInvitation: PbWizard = ...
    pbWizardJapaneseAdvertisements: PbWizard = ...
    pbWizardJapaneseAirplanes: PbWizard = ...
    pbWizardJapaneseBanners: PbWizard = ...
    pbWizardJapaneseBrochures: PbWizard = ...
    pbWizardJapaneseBusinessCards: PbWizard = ...
    pbWizardJapaneseBusinessForms: PbWizard = ...
    pbWizardJapaneseCalendars: PbWizard = ...
    pbWizardJapaneseCatalogs: PbWizard = ...
    pbWizardJapaneseCertificates: PbWizard = ...
    pbWizardJapaneseEnvelopes: PbWizard = ...
    pbWizardJapaneseFlyers: PbWizard = ...
    pbWizardJapaneseGiftCertificates: PbWizard = ...
    pbWizardJapaneseGreetingCards: PbWizard = ...
    pbWizardJapaneseInvitations: PbWizard = ...
    pbWizardJapaneseLabels: PbWizard = ...
    pbWizardJapaneseLetterheads: PbWizard = ...
    pbWizardJapaneseMenus: PbWizard = ...
    pbWizardJapaneseNewsletters: PbWizard = ...
    pbWizardJapaneseOrigami: PbWizard = ...
    pbWizardJapanesePostcards: PbWizard = ...
    pbWizardJapanesePrograms: PbWizard = ...
    pbWizardJapaneseSigns: PbWizard = ...
    pbWizardJapaneseWebSites: PbWizard = ...
    pbWizardLabels: PbWizard = ...
    pbWizardLetterheads: PbWizard = ...
    pbWizardMenus: PbWizard = ...
    pbWizardNewsletters: PbWizard = ...
    pbWizardNone: PbWizard = ...
    pbWizardOrigami: PbWizard = ...
    pbWizardPostcards: PbWizard = ...
    pbWizardPrograms: PbWizard = ...
    pbWizardQuickPublications: PbWizard = ...
    pbWizardResumes: PbWizard = ...
    pbWizardSigns: PbWizard = ...
    pbWizardWebSiteBlank: PbWizard = ...
    pbWizardWebSiteHomePage: PbWizard = ...
    pbWizardWebSiteProductSales: PbWizard = ...
    pbWizardWebSiteServices: PbWizard = ...
    pbWizardWebSiteThreePage: PbWizard = ...
    pbWizardWithComplimentsCards: PbWizard = ...
    pbWizardWordDocument: PbWizard = ...
    value__ = ...


class PbWizard10(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbWizard10, values: pbWizardGreetingCards (14), pbWizardInvitations (15), pbWizardWebSites (11) """
    pbWizardGreetingCards: PbWizard10 = ...
    pbWizardInvitations: PbWizard10 = ...
    pbWizardWebSites: PbWizard10 = ...
    value__ = ...


class PbWizardGroup(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbWizardGroup, values: pbWizardGroupAccentBox (151), pbWizardGroupAccessoryBar (154), pbWizardGroupAdvertisements (68), pbWizardGroupAttentionGetter (61), pbWizardGroupBarbells (52), pbWizardGroupBorders (155), pbWizardGroupBoxes (50), pbWizardGroupCalendars (77), pbWizardGroupCheckerboards (53), pbWizardGroupCoupon (60), pbWizardGroupDots (49), pbWizardGroupEastAsiaZipCode (181), pbWizardGroupJapaneseAccentBox (168), pbWizardGroupJapaneseAccessoryBar (171), pbWizardGroupJapaneseAttentionGetters (97), pbWizardGroupJapaneseBorders (172), pbWizardGroupJapaneseCalendar (83), pbWizardGroupJapaneseCoupons (99), pbWizardGroupJapaneseLinearAccent (170), pbWizardGroupJapaneseMarquees (167), pbWizardGroupJapaneseMastheads (141), pbWizardGroupJapanesePullQuotes (144), pbWizardGroupJapaneseReplyForms (137), pbWizardGroupJapaneseSidebars (143), pbWizardGroupJapaneseTableOfContents (142), pbWizardGroupJapaneseWebButtonEmail (182), pbWizardGroupJapaneseWebButtonHome (183), pbWizardGroupJapaneseWebButtonLink (184), pbWizardGroupJapaneseWebMastheads (138), pbWizardGroupJapaneseWebNavigationBars (148), pbWizardGroupJapaneseWebPullQuotes (139), pbWizardGroupJapaneseWebSidebars (140), pbWizardGroupLinearAccent (153), pbWizardGroupLogo (4), pbWizardGroupMarquee (150), pbWizardGroupMastheads (105), pbWizardGroupPhoneTearoff (66), pbWizardGroupPictureCaptions (109), pbWizardGroupPullQuotes (108), pbWizardGroupPunctuation (152), pbWizardGroupReplyForms (79), pbWizardGroupSidebars (107), pbWizardGroupTableOfContents (106), pbWizardGroupWebButtonsEmail (133), pbWizardGroupWebButtonsHome (134), pbWizardGroupWebButtonsLink (136), pbWizardGroupWebCalendars (35), pbWizardGroupWebMastheads (102), pbWizardGroupWebNavigationBars (75), pbWizardGroupWebSidebars (104), pbWizardGroupWellPullQuotes (103) """
    pbWizardGroupAccentBox: PbWizardGroup = ...
    pbWizardGroupAccessoryBar: PbWizardGroup = ...
    pbWizardGroupAdvertisements: PbWizardGroup = ...
    pbWizardGroupAttentionGetter: PbWizardGroup = ...
    pbWizardGroupBarbells: PbWizardGroup = ...
    pbWizardGroupBorders: PbWizardGroup = ...
    pbWizardGroupBoxes: PbWizardGroup = ...
    pbWizardGroupCalendars: PbWizardGroup = ...
    pbWizardGroupCheckerboards: PbWizardGroup = ...
    pbWizardGroupCoupon: PbWizardGroup = ...
    pbWizardGroupDots: PbWizardGroup = ...
    pbWizardGroupEastAsiaZipCode: PbWizardGroup = ...
    pbWizardGroupJapaneseAccentBox: PbWizardGroup = ...
    pbWizardGroupJapaneseAccessoryBar: PbWizardGroup = ...
    pbWizardGroupJapaneseAttentionGetters: PbWizardGroup = ...
    pbWizardGroupJapaneseBorders: PbWizardGroup = ...
    pbWizardGroupJapaneseCalendar: PbWizardGroup = ...
    pbWizardGroupJapaneseCoupons: PbWizardGroup = ...
    pbWizardGroupJapaneseLinearAccent: PbWizardGroup = ...
    pbWizardGroupJapaneseMarquees: PbWizardGroup = ...
    pbWizardGroupJapaneseMastheads: PbWizardGroup = ...
    pbWizardGroupJapanesePullQuotes: PbWizardGroup = ...
    pbWizardGroupJapaneseReplyForms: PbWizardGroup = ...
    pbWizardGroupJapaneseSidebars: PbWizardGroup = ...
    pbWizardGroupJapaneseTableOfContents: PbWizardGroup = ...
    pbWizardGroupJapaneseWebButtonEmail: PbWizardGroup = ...
    pbWizardGroupJapaneseWebButtonHome: PbWizardGroup = ...
    pbWizardGroupJapaneseWebButtonLink: PbWizardGroup = ...
    pbWizardGroupJapaneseWebMastheads: PbWizardGroup = ...
    pbWizardGroupJapaneseWebNavigationBars: PbWizardGroup = ...
    pbWizardGroupJapaneseWebPullQuotes: PbWizardGroup = ...
    pbWizardGroupJapaneseWebSidebars: PbWizardGroup = ...
    pbWizardGroupLinearAccent: PbWizardGroup = ...
    pbWizardGroupLogo: PbWizardGroup = ...
    pbWizardGroupMarquee: PbWizardGroup = ...
    pbWizardGroupMastheads: PbWizardGroup = ...
    pbWizardGroupPhoneTearoff: PbWizardGroup = ...
    pbWizardGroupPictureCaptions: PbWizardGroup = ...
    pbWizardGroupPullQuotes: PbWizardGroup = ...
    pbWizardGroupPunctuation: PbWizardGroup = ...
    pbWizardGroupReplyForms: PbWizardGroup = ...
    pbWizardGroupSidebars: PbWizardGroup = ...
    pbWizardGroupTableOfContents: PbWizardGroup = ...
    pbWizardGroupWebButtonsEmail: PbWizardGroup = ...
    pbWizardGroupWebButtonsHome: PbWizardGroup = ...
    pbWizardGroupWebButtonsLink: PbWizardGroup = ...
    pbWizardGroupWebCalendars: PbWizardGroup = ...
    pbWizardGroupWebMastheads: PbWizardGroup = ...
    pbWizardGroupWebNavigationBars: PbWizardGroup = ...
    pbWizardGroupWebSidebars: PbWizardGroup = ...
    pbWizardGroupWellPullQuotes: PbWizardGroup = ...
    value__ = ...


class PbWizardNavBarAlignment(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbWizardNavBarAlignment, values: pbnbAlignCenter (2), pbnbAlignLeft (1), pbnbAlignRight (3) """
    pbnbAlignCenter: PbWizardNavBarAlignment = ...
    pbnbAlignLeft: PbWizardNavBarAlignment = ...
    pbnbAlignRight: PbWizardNavBarAlignment = ...
    value__ = ...


class PbWizardNavBarButtonStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbWizardNavBarButtonStyle, values: pbnbButtonStyleLarge (2), pbnbButtonStyleSmall (1), pbnbButtonStyleText (3) """
    pbnbButtonStyleLarge: PbWizardNavBarButtonStyle = ...
    pbnbButtonStyleSmall: PbWizardNavBarButtonStyle = ...
    pbnbButtonStyleText: PbWizardNavBarButtonStyle = ...
    value__ = ...


class PbWizardNavBarDesign(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbWizardNavBarDesign, values: pbnbDesignAmbient (2), pbnbDesignBaseline (26), pbnbDesignBracket (11), pbnbDesignBulletStaff (20), pbnbDesignCapsule (3), pbnbDesignCornice (15), pbnbDesignCounter (13), pbnbDesignDimension (8), pbnbDesignDottedArrow (9), pbnbDesignEdge (17), pbnbDesignEnclosedArrow (12), pbnbDesignEndCap (14), pbnbDesignHollowArrow (10), pbnbDesignKeyPunch (22), pbnbDesignOffset (7), pbnbDesignOutline (5), pbnbDesignRadius (6), pbnbDesignRectangle (1), pbnbDesignRoundBullet (23), pbnbDesignSquareBullet (24), pbnbDesignStaff (16), pbnbDesignTopBar (21), pbnbDesignTopDrawer (4), pbnbDesignTopLine (18), pbnbDesignUnderscore (19), pbnbDesignWatermark (25) """
    pbnbDesignAmbient: PbWizardNavBarDesign = ...
    pbnbDesignBaseline: PbWizardNavBarDesign = ...
    pbnbDesignBracket: PbWizardNavBarDesign = ...
    pbnbDesignBulletStaff: PbWizardNavBarDesign = ...
    pbnbDesignCapsule: PbWizardNavBarDesign = ...
    pbnbDesignCornice: PbWizardNavBarDesign = ...
    pbnbDesignCounter: PbWizardNavBarDesign = ...
    pbnbDesignDimension: PbWizardNavBarDesign = ...
    pbnbDesignDottedArrow: PbWizardNavBarDesign = ...
    pbnbDesignEdge: PbWizardNavBarDesign = ...
    pbnbDesignEnclosedArrow: PbWizardNavBarDesign = ...
    pbnbDesignEndCap: PbWizardNavBarDesign = ...
    pbnbDesignHollowArrow: PbWizardNavBarDesign = ...
    pbnbDesignKeyPunch: PbWizardNavBarDesign = ...
    pbnbDesignOffset: PbWizardNavBarDesign = ...
    pbnbDesignOutline: PbWizardNavBarDesign = ...
    pbnbDesignRadius: PbWizardNavBarDesign = ...
    pbnbDesignRectangle: PbWizardNavBarDesign = ...
    pbnbDesignRoundBullet: PbWizardNavBarDesign = ...
    pbnbDesignSquareBullet: PbWizardNavBarDesign = ...
    pbnbDesignStaff: PbWizardNavBarDesign = ...
    pbnbDesignTopBar: PbWizardNavBarDesign = ...
    pbnbDesignTopDrawer: PbWizardNavBarDesign = ...
    pbnbDesignTopLine: PbWizardNavBarDesign = ...
    pbnbDesignUnderscore: PbWizardNavBarDesign = ...
    pbnbDesignWatermark: PbWizardNavBarDesign = ...
    value__ = ...


class PbWizardPageType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbWizardPageType, values: pbWizardPageTypeCatalogBlank (35), pbWizardPageTypeCatalogCalendar (22), pbWizardPageTypeCatalogEightItemsOneColumn (33), pbWizardPageTypeCatalogEightItemsTwoColumns (34), pbWizardPageTypeCatalogFeaturedItem (24), pbWizardPageTypeCatalogForm (36), pbWizardPageTypeCatalogFourItemsAlignedPictures (30), pbWizardPageTypeCatalogFourItemsOffsetPictures (31), pbWizardPageTypeCatalogFourItemsSquaredPictures (32), pbWizardPageTypeCatalogOneColumnText (18), pbWizardPageTypeCatalogOneColumnTextPicture (19), pbWizardPageTypeCatalogTableOfContents (23), pbWizardPageTypeCatalogThreeItemsAlignedPictures (27), pbWizardPageTypeCatalogThreeItemsOffsetPictures (28), pbWizardPageTypeCatalogThreeItemsStackedPictures (29), pbWizardPageTypeCatalogTwoColumnsText (20), pbWizardPageTypeCatalogTwoColumnsTextPicture (21), pbWizardPageTypeCatalogTwoItemsAlignedPictures (25), pbWizardPageTypeCatalogTwoItemsOffsetPictures (26), pbWizardPageTypeNewsletter3Stories (1), pbWizardPageTypeNewsletterCalendar (2), pbWizardPageTypeNewsletterOrderForm (15), pbWizardPageTypeNewsletterResponseForm (16), pbWizardPageTypeNewsletterSignupForm (17), pbWizardPageTypeNone (-1), pbWizardPageTypeWebAboutUs (501), pbWizardPageTypeWebArticle (512), pbWizardPageTypeWebBlank (524), pbWizardPageTypeWebCalendarPage (504), pbWizardPageTypeWebCalendarWithLinks (800), pbWizardPageTypeWebContactUs (505), pbWizardPageTypeWebEmployee (507), pbWizardPageTypeWebEmployeeList (506), pbWizardPageTypeWebEmployeesWithLinks (802), pbWizardPageTypeWebFAQ (508), pbWizardPageTypeWebHome (509), pbWizardPageTypeWebInformational (502), pbWizardPageTypeWebJobs (510), pbWizardPageTypeWebLegal (511), pbWizardPageTypeWebLinks (518), pbWizardPageTypeWebList (503), pbWizardPageTypeWebOrderForm (525), pbWizardPageTypeWebPhoto (513), pbWizardPageTypeWebPhotoGallery (514), pbWizardPageTypeWebPhotosWithLinks (805), pbWizardPageTypeWebProduct (515), pbWizardPageTypeWebProductList (516), pbWizardPageTypeWebProductsWithLinks (801), pbWizardPageTypeWebProjectList (517), pbWizardPageTypeWebProjectsWithLinks (804), pbWizardPageTypeWebResponseForm (526), pbWizardPageTypeWebSeminar (519), pbWizardPageTypeWebService (521), pbWizardPageTypeWebServiceList (520), pbWizardPageTypeWebServicesWithLinks (803), pbWizardPageTypeWebSignupForm (527), pbWizardPageTypeWebSpecial (522) """
    pbWizardPageTypeCatalogBlank: PbWizardPageType = ...
    pbWizardPageTypeCatalogCalendar: PbWizardPageType = ...
    pbWizardPageTypeCatalogEightItemsOneColumn: PbWizardPageType = ...
    pbWizardPageTypeCatalogEightItemsTwoColumns: PbWizardPageType = ...
    pbWizardPageTypeCatalogFeaturedItem: PbWizardPageType = ...
    pbWizardPageTypeCatalogForm: PbWizardPageType = ...
    pbWizardPageTypeCatalogFourItemsAlignedPictures: PbWizardPageType = ...
    pbWizardPageTypeCatalogFourItemsOffsetPictures: PbWizardPageType = ...
    pbWizardPageTypeCatalogFourItemsSquaredPictures: PbWizardPageType = ...
    pbWizardPageTypeCatalogOneColumnText: PbWizardPageType = ...
    pbWizardPageTypeCatalogOneColumnTextPicture: PbWizardPageType = ...
    pbWizardPageTypeCatalogTableOfContents: PbWizardPageType = ...
    pbWizardPageTypeCatalogThreeItemsAlignedPictures: PbWizardPageType = ...
    pbWizardPageTypeCatalogThreeItemsOffsetPictures: PbWizardPageType = ...
    pbWizardPageTypeCatalogThreeItemsStackedPictures: PbWizardPageType = ...
    pbWizardPageTypeCatalogTwoColumnsText: PbWizardPageType = ...
    pbWizardPageTypeCatalogTwoColumnsTextPicture: PbWizardPageType = ...
    pbWizardPageTypeCatalogTwoItemsAlignedPictures: PbWizardPageType = ...
    pbWizardPageTypeCatalogTwoItemsOffsetPictures: PbWizardPageType = ...
    pbWizardPageTypeNewsletter3Stories: PbWizardPageType = ...
    pbWizardPageTypeNewsletterCalendar: PbWizardPageType = ...
    pbWizardPageTypeNewsletterOrderForm: PbWizardPageType = ...
    pbWizardPageTypeNewsletterResponseForm: PbWizardPageType = ...
    pbWizardPageTypeNewsletterSignupForm: PbWizardPageType = ...
    pbWizardPageTypeNone: PbWizardPageType = ...
    pbWizardPageTypeWebAboutUs: PbWizardPageType = ...
    pbWizardPageTypeWebArticle: PbWizardPageType = ...
    pbWizardPageTypeWebBlank: PbWizardPageType = ...
    pbWizardPageTypeWebCalendarPage: PbWizardPageType = ...
    pbWizardPageTypeWebCalendarWithLinks: PbWizardPageType = ...
    pbWizardPageTypeWebContactUs: PbWizardPageType = ...
    pbWizardPageTypeWebEmployee: PbWizardPageType = ...
    pbWizardPageTypeWebEmployeeList: PbWizardPageType = ...
    pbWizardPageTypeWebEmployeesWithLinks: PbWizardPageType = ...
    pbWizardPageTypeWebFAQ: PbWizardPageType = ...
    pbWizardPageTypeWebHome: PbWizardPageType = ...
    pbWizardPageTypeWebInformational: PbWizardPageType = ...
    pbWizardPageTypeWebJobs: PbWizardPageType = ...
    pbWizardPageTypeWebLegal: PbWizardPageType = ...
    pbWizardPageTypeWebLinks: PbWizardPageType = ...
    pbWizardPageTypeWebList: PbWizardPageType = ...
    pbWizardPageTypeWebOrderForm: PbWizardPageType = ...
    pbWizardPageTypeWebPhoto: PbWizardPageType = ...
    pbWizardPageTypeWebPhotoGallery: PbWizardPageType = ...
    pbWizardPageTypeWebPhotosWithLinks: PbWizardPageType = ...
    pbWizardPageTypeWebProduct: PbWizardPageType = ...
    pbWizardPageTypeWebProductList: PbWizardPageType = ...
    pbWizardPageTypeWebProductsWithLinks: PbWizardPageType = ...
    pbWizardPageTypeWebProjectList: PbWizardPageType = ...
    pbWizardPageTypeWebProjectsWithLinks: PbWizardPageType = ...
    pbWizardPageTypeWebResponseForm: PbWizardPageType = ...
    pbWizardPageTypeWebSeminar: PbWizardPageType = ...
    pbWizardPageTypeWebService: PbWizardPageType = ...
    pbWizardPageTypeWebServiceList: PbWizardPageType = ...
    pbWizardPageTypeWebServicesWithLinks: PbWizardPageType = ...
    pbWizardPageTypeWebSignupForm: PbWizardPageType = ...
    pbWizardPageTypeWebSpecial: PbWizardPageType = ...
    value__ = ...


class PbWizardPageType10(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbWizardPageType10, values: pbWizardPageTypeWebCalendar (9), pbWizardPageTypeWebEvent (13), pbWizardPageTypeWebPriceList (8), pbWizardPageTypeWebRelatedLinks (7), pbWizardPageTypeWebSpecialOffer (12), pbWizardPageTypeWebStory (6) """
    pbWizardPageTypeWebCalendar: PbWizardPageType10 = ...
    pbWizardPageTypeWebEvent: PbWizardPageType10 = ...
    pbWizardPageTypeWebPriceList: PbWizardPageType10 = ...
    pbWizardPageTypeWebRelatedLinks: PbWizardPageType10 = ...
    pbWizardPageTypeWebSpecialOffer: PbWizardPageType10 = ...
    pbWizardPageTypeWebStory: PbWizardPageType10 = ...
    value__ = ...


class PbWizardTag(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbWizardTag, values: pbWizardTagAddress (10), pbWizardTagAddressGroup (117), pbWizardTagBriefDescriptionCaption (1361), pbWizardTagBriefDescriptionGraphic (1359), pbWizardTagBriefDescriptionSummary (1353), pbWizardTagBriefDescriptionSummaryPrimary (1365), pbWizardTagBriefDescriptionTitle (1364), pbWizardTagBusinessDescription (685), pbWizardTagCustomerMailingAddress (560), pbWizardTagDate (1835), pbWizardTagEAPostalCodeBox (2151), pbWizardTagEAPostalCodeGroup (2150), pbWizardTagEAPostalCodeLine (2152), pbWizardTagFloatingGraphicCaption (1362), pbWizardTagHourTimeDateInformation (684), pbWizardTagJobTitle (115), pbWizardTagLinkedStoryPrimary (1354), pbWizardTagLinkedStorySecondary (1355), pbWizardTagLinkedStoryTertiary (1356), pbWizardTagList (1837), pbWizardTagLocation (488), pbWizardTagLogoGroup (5), pbWizardTagMainFloatingGraphic (1357), pbWizardTagMainGraphic (1833), pbWizardTagMainTitle (1832), pbWizardTagMapPicture (489), pbWizardTagMasthead (1831), pbWizardTagNewsletterTitle (1344), pbWizardTagOrganizationName (7), pbWizardTagOrganizationNameGroup (118), pbWizardTagPageNumber (1346), pbWizardTagPersonalName (8), pbWizardTagPersonalNameGroup (116), pbWizardTagPhoneFaxEmail (113), pbWizardTagPhoneFaxEmailGroup (120), pbWizardTagPhoneNumber (114), pbWizardTagPhotePlaceholderText (1135), pbWizardTagPhotoPlaceholderFrame (1134), pbWizardTagPictureCaption (2155), pbWizardTagPictureCaptionPicture (2153), pbWizardTagPictureCaptionText (2154), pbWizardTagPublicationDate (1341), pbWizardTagQuickPubContent (2143), pbWizardTagQuickPubHeading (2140), pbWizardTagQuickPubMessage (2141), pbWizardTagQuickPubPicture (2142), pbWizardTagReturnAddressLines (793), pbWizardTagStampBox (887), pbWizardTagStampBoxOutline (794), pbWizardTagStory (1349), pbWizardTagStoryCaptionPrimary (1351), pbWizardTagStoryCaptionSecondary (1373), pbWizardTagStoryGraphicPrimary (1350), pbWizardTagStoryGraphicSecondary (1360), pbWizardTagStoryTitle (1348), pbWizardTagTableOfContents (1343), pbWizardTagTableOfContentsTitle (1342), pbWizardTagTagLine (112), pbWizardTagTagLineGroup (119), pbWizardTagTime (1836) """
    pbWizardTagAddress: PbWizardTag = ...
    pbWizardTagAddressGroup: PbWizardTag = ...
    pbWizardTagBriefDescriptionCaption: PbWizardTag = ...
    pbWizardTagBriefDescriptionGraphic: PbWizardTag = ...
    pbWizardTagBriefDescriptionSummary: PbWizardTag = ...
    pbWizardTagBriefDescriptionSummaryPrimary: PbWizardTag = ...
    pbWizardTagBriefDescriptionTitle: PbWizardTag = ...
    pbWizardTagBusinessDescription: PbWizardTag = ...
    pbWizardTagCustomerMailingAddress: PbWizardTag = ...
    pbWizardTagDate: PbWizardTag = ...
    pbWizardTagEAPostalCodeBox: PbWizardTag = ...
    pbWizardTagEAPostalCodeGroup: PbWizardTag = ...
    pbWizardTagEAPostalCodeLine: PbWizardTag = ...
    pbWizardTagFloatingGraphicCaption: PbWizardTag = ...
    pbWizardTagHourTimeDateInformation: PbWizardTag = ...
    pbWizardTagJobTitle: PbWizardTag = ...
    pbWizardTagLinkedStoryPrimary: PbWizardTag = ...
    pbWizardTagLinkedStorySecondary: PbWizardTag = ...
    pbWizardTagLinkedStoryTertiary: PbWizardTag = ...
    pbWizardTagList: PbWizardTag = ...
    pbWizardTagLocation: PbWizardTag = ...
    pbWizardTagLogoGroup: PbWizardTag = ...
    pbWizardTagMainFloatingGraphic: PbWizardTag = ...
    pbWizardTagMainGraphic: PbWizardTag = ...
    pbWizardTagMainTitle: PbWizardTag = ...
    pbWizardTagMapPicture: PbWizardTag = ...
    pbWizardTagMasthead: PbWizardTag = ...
    pbWizardTagNewsletterTitle: PbWizardTag = ...
    pbWizardTagOrganizationName: PbWizardTag = ...
    pbWizardTagOrganizationNameGroup: PbWizardTag = ...
    pbWizardTagPageNumber: PbWizardTag = ...
    pbWizardTagPersonalName: PbWizardTag = ...
    pbWizardTagPersonalNameGroup: PbWizardTag = ...
    pbWizardTagPhoneFaxEmail: PbWizardTag = ...
    pbWizardTagPhoneFaxEmailGroup: PbWizardTag = ...
    pbWizardTagPhoneNumber: PbWizardTag = ...
    pbWizardTagPhotePlaceholderText: PbWizardTag = ...
    pbWizardTagPhotoPlaceholderFrame: PbWizardTag = ...
    pbWizardTagPictureCaption: PbWizardTag = ...
    pbWizardTagPictureCaptionPicture: PbWizardTag = ...
    pbWizardTagPictureCaptionText: PbWizardTag = ...
    pbWizardTagPublicationDate: PbWizardTag = ...
    pbWizardTagQuickPubContent: PbWizardTag = ...
    pbWizardTagQuickPubHeading: PbWizardTag = ...
    pbWizardTagQuickPubMessage: PbWizardTag = ...
    pbWizardTagQuickPubPicture: PbWizardTag = ...
    pbWizardTagReturnAddressLines: PbWizardTag = ...
    pbWizardTagStampBox: PbWizardTag = ...
    pbWizardTagStampBoxOutline: PbWizardTag = ...
    pbWizardTagStory: PbWizardTag = ...
    pbWizardTagStoryCaptionPrimary: PbWizardTag = ...
    pbWizardTagStoryCaptionSecondary: PbWizardTag = ...
    pbWizardTagStoryGraphicPrimary: PbWizardTag = ...
    pbWizardTagStoryGraphicSecondary: PbWizardTag = ...
    pbWizardTagStoryTitle: PbWizardTag = ...
    pbWizardTagTableOfContents: PbWizardTag = ...
    pbWizardTagTableOfContentsTitle: PbWizardTag = ...
    pbWizardTagTagLine: PbWizardTag = ...
    pbWizardTagTagLineGroup: PbWizardTag = ...
    pbWizardTagTime: PbWizardTag = ...
    value__ = ...


class PbWrapSideType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbWrapSideType, values: pbWrapSideBoth (0), pbWrapSideLarger (3), pbWrapSideLeft (1), pbWrapSideMixed (-1), pbWrapSideNeither (4), pbWrapSideRight (2) """
    pbWrapSideBoth: PbWrapSideType = ...
    pbWrapSideLarger: PbWrapSideType = ...
    pbWrapSideLeft: PbWrapSideType = ...
    pbWrapSideMixed: PbWrapSideType = ...
    pbWrapSideNeither: PbWrapSideType = ...
    pbWrapSideRight: PbWrapSideType = ...
    value__ = ...


class PbWrapType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbWrapType, values: pbWrapTypeMixed (-1), pbWrapTypeNone (0), pbWrapTypeSquare (1), pbWrapTypeThrough (3), pbWrapTypeTight (2), pbWrapTypeTopAndBottom (4) """
    pbWrapTypeMixed: PbWrapType = ...
    pbWrapTypeNone: PbWrapType = ...
    pbWrapTypeSquare: PbWrapType = ...
    pbWrapTypeThrough: PbWrapType = ...
    pbWrapTypeTight: PbWrapType = ...
    pbWrapTypeTopAndBottom: PbWrapType = ...
    value__ = ...


class PbZoom(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PbZoom, values: pbZoomFitSelection (-3), pbZoomPageWidth (-1), pbZoomWholePage (-2) """
    pbZoomFitSelection: PbZoom = ...
    pbZoomPageWidth: PbZoom = ...
    pbZoomWholePage: PbZoom = ...
    value__ = ...


class PhoneticGuide: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Alignment(self) -> PbPhoneticGuideAlignmentType:
        """ Get: Alignment(self: PhoneticGuide) -> PbPhoneticGuideAlignmentType """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: PhoneticGuide) -> Application """
        ...

    @property
    def BaseText(self) -> str:
        """ Get: BaseText(self: PhoneticGuide) -> str """
        ...

    @property
    def FontName(self) -> str:
        """ Get: FontName(self: PhoneticGuide) -> str """
        ...

    @property
    def FontSize(self) -> object:
        """ Get: FontSize(self: PhoneticGuide) -> object """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PhoneticGuide) -> object """
        ...

    @property
    def Raise(self) -> object:
        """ Get: Raise(self: PhoneticGuide) -> object """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: PhoneticGuide) -> str """
        ...


    def Clear(self): # -> 
        """ Clear(self: PhoneticGuide) """
        ...


class PictureFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PictureFormat) -> Application """
        ...

    @property
    def Brightness(self) -> Single:
        """
        Get: Brightness(self: PictureFormat) -> Single
        Set: Brightness(self: PictureFormat) = value
        """
        ...

    @property
    def ColorModel(self) -> PbColorModel:
        """ Get: ColorModel(self: PictureFormat) -> PbColorModel """
        ...

    @property
    def ColorsInPalette(self) -> int:
        """ Get: ColorsInPalette(self: PictureFormat) -> int """
        ...

    @property
    def ColorType(self): # -> MsoPictureColorType
        """
        Get: ColorType(self: PictureFormat) -> MsoPictureColorType
        Set: ColorType(self: PictureFormat) = value
        """
        ...

    @property
    def Contrast(self) -> Single:
        """
        Get: Contrast(self: PictureFormat) -> Single
        Set: Contrast(self: PictureFormat) = value
        """
        ...

    @property
    def CropBottom(self) -> object:
        """
        Get: CropBottom(self: PictureFormat) -> object
        Set: CropBottom(self: PictureFormat) = value
        """
        ...

    @property
    def CropLeft(self) -> object:
        """
        Get: CropLeft(self: PictureFormat) -> object
        Set: CropLeft(self: PictureFormat) = value
        """
        ...

    @property
    def CropRight(self) -> object:
        """
        Get: CropRight(self: PictureFormat) -> object
        Set: CropRight(self: PictureFormat) = value
        """
        ...

    @property
    def CropTop(self) -> object:
        """
        Get: CropTop(self: PictureFormat) -> object
        Set: CropTop(self: PictureFormat) = value
        """
        ...

    @property
    def EffectiveResolution(self) -> int:
        """ Get: EffectiveResolution(self: PictureFormat) -> int """
        ...

    @property
    def Filename(self) -> str:
        """ Get: Filename(self: PictureFormat) -> str """
        ...

    @property
    def FileSize(self) -> int:
        """ Get: FileSize(self: PictureFormat) -> int """
        ...

    @property
    def HasAlphaChannel(self): # -> MsoTriState
        """ Get: HasAlphaChannel(self: PictureFormat) -> MsoTriState """
        ...

    @property
    def HasTransparencyColor(self) -> bool:
        """ Get: HasTransparencyColor(self: PictureFormat) -> bool """
        ...

    @property
    def Height(self) -> object:
        """ Get: Height(self: PictureFormat) -> object """
        ...

    @property
    def HorizontalPictureLocking(self) -> PbHorizontalPictureLocking:
        """
        Get: HorizontalPictureLocking(self: PictureFormat) -> PbHorizontalPictureLocking
        Set: HorizontalPictureLocking(self: PictureFormat) = value
        """
        ...

    @property
    def HorizontalScale(self) -> int:
        """ Get: HorizontalScale(self: PictureFormat) -> int """
        ...

    @property
    def ImageFormat(self) -> PbImageFormat:
        """ Get: ImageFormat(self: PictureFormat) -> PbImageFormat """
        ...

    @property
    def IsEmpty(self): # -> MsoTriState
        """ Get: IsEmpty(self: PictureFormat) -> MsoTriState """
        ...

    @property
    def IsGreyScale(self): # -> MsoTriState
        """ Get: IsGreyScale(self: PictureFormat) -> MsoTriState """
        ...

    @property
    def IsLinked(self): # -> MsoTriState
        """ Get: IsLinked(self: PictureFormat) -> MsoTriState """
        ...

    @property
    def IsRecolored(self): # -> MsoTriState
        """ Get: IsRecolored(self: PictureFormat) -> MsoTriState """
        ...

    @property
    def IsTrueColor(self): # -> MsoTriState
        """ Get: IsTrueColor(self: PictureFormat) -> MsoTriState """
        ...

    @property
    def LeaveBlackAsBlack(self): # -> MsoTriState
        """ Get: LeaveBlackAsBlack(self: PictureFormat) -> MsoTriState """
        ...

    @property
    def LinkedFileStatus(self) -> PbLinkedFileStatus:
        """ Get: LinkedFileStatus(self: PictureFormat) -> PbLinkedFileStatus """
        ...

    @property
    def OriginalColorsInPalette(self) -> int:
        """ Get: OriginalColorsInPalette(self: PictureFormat) -> int """
        ...

    @property
    def OriginalFileSize(self) -> int:
        """ Get: OriginalFileSize(self: PictureFormat) -> int """
        ...

    @property
    def OriginalHasAlphaChannel(self): # -> MsoTriState
        """ Get: OriginalHasAlphaChannel(self: PictureFormat) -> MsoTriState """
        ...

    @property
    def OriginalHeight(self) -> object:
        """ Get: OriginalHeight(self: PictureFormat) -> object """
        ...

    @property
    def OriginalIsTrueColor(self): # -> MsoTriState
        """ Get: OriginalIsTrueColor(self: PictureFormat) -> MsoTriState """
        ...

    @property
    def OriginalResolution(self) -> int:
        """ Get: OriginalResolution(self: PictureFormat) -> int """
        ...

    @property
    def OriginalWidth(self) -> object:
        """ Get: OriginalWidth(self: PictureFormat) -> object """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PictureFormat) -> object """
        ...

    @property
    def RecoloredPictureColor(self) -> ColorFormat:
        """ Get: RecoloredPictureColor(self: PictureFormat) -> ColorFormat """
        ...

    @property
    def TransparencyColor(self) -> int:
        """
        Get: TransparencyColor(self: PictureFormat) -> int
        Set: TransparencyColor(self: PictureFormat) = value
        """
        ...

    @property
    def TransparentBackground(self): # -> MsoTriState
        """
        Get: TransparentBackground(self: PictureFormat) -> MsoTriState
        Set: TransparentBackground(self: PictureFormat) = value
        """
        ...

    @property
    def VerticalPictureLocking(self) -> PbVerticalPictureLocking:
        """
        Get: VerticalPictureLocking(self: PictureFormat) -> PbVerticalPictureLocking
        Set: VerticalPictureLocking(self: PictureFormat) = value
        """
        ...

    @property
    def VerticalScale(self) -> int:
        """ Get: VerticalScale(self: PictureFormat) -> int """
        ...

    @property
    def Width(self) -> object:
        """ Get: Width(self: PictureFormat) -> object """
        ...


    def ClearCrop(self): # -> 
        """ ClearCrop(self: PictureFormat) """
        ...

    def FillFrame(self): # -> 
        """ FillFrame(self: PictureFormat) """
        ...

    def FitFrame(self): # -> 
        """ FitFrame(self: PictureFormat) """
        ...

    def IncrementBrightness(self, Increment:Single): # -> 
        """ IncrementBrightness(self: PictureFormat, Increment: Single) """
        ...

    def IncrementContrast(self, Increment:Single): # -> 
        """ IncrementContrast(self: PictureFormat, Increment: Single) """
        ...

    def Recolor(self, Color:ColorFormat, LeaveBlackPartsBlack): # ->  # Not found arg types: {'LeaveBlackPartsBlack': 'MsoTriState'}
        """ Recolor(self: PictureFormat, Color: ColorFormat, LeaveBlackPartsBlack: MsoTriState) """
        ...

    def Remove(self): # -> 
        """ Remove(self: PictureFormat) """
        ...

    def Replace(self, Pathname:str, InsertAs:PbPictureInsertAs): # -> 
        """ Replace(self: PictureFormat, Pathname: str, InsertAs: PbPictureInsertAs) """
        ...

    def ReplaceEx(self, Pathname:str, InsertAs:PbPictureInsertAs, Fit:pbPictureInsertFit): # -> 
        """ ReplaceEx(self: PictureFormat, Pathname: str, InsertAs: PbPictureInsertAs, Fit: pbPictureInsertFit) """
        ...

    def RestoreOriginalColors(self): # -> 
        """ RestoreOriginalColors(self: PictureFormat) """
        ...


class Plate: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Angle(self) -> int:
        """
        Get: Angle(self: Plate) -> int
        Set: Angle(self: Plate) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: Plate) -> Application """
        ...

    @property
    def Color(self) -> ColorFormat:
        """ Get: Color(self: Plate) -> ColorFormat """
        ...

    @property
    def Frequency(self) -> int:
        """
        Get: Frequency(self: Plate) -> int
        Set: Frequency(self: Plate) = value
        """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: Plate) -> int """
        ...

    @property
    def InkName(self) -> PbInkName:
        """ Get: InkName(self: Plate) -> PbInkName """
        ...

    @property
    def InUse(self) -> bool:
        """ Get: InUse(self: Plate) -> bool """
        ...

    @property
    def Luminance(self) -> int:
        """
        Get: Luminance(self: Plate) -> int
        Set: Luminance(self: Plate) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Plate) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Plate) -> object """
        ...


    def ConvertToProcess(self): # -> 
        """ ConvertToProcess(self: Plate) """
        ...

    def Delete(self, PlateReplaceWith:object, ReplaceTint:PbReplaceTint): # -> 
        """ Delete(self: Plate, PlateReplaceWith: object, ReplaceTint: PbReplaceTint) """
        ...

    def Delete10(self): # -> 
        """ Delete10(self: Plate) """
        ...


class Plates(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Plates) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Plates) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Plates) -> object """
        ...


    def Add(self, PlateColor:ColorFormat): # -> 
        """ Add(self: Plates, PlateColor: ColorFormat) """
        ...

    def FindPlateByInkName(self, InkName:PbInkName) -> Plate:
        """ FindPlateByInkName(self: Plates, InkName: PbInkName) -> Plate """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class PrintablePlate: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Angle(self) -> int:
        """
        Get: Angle(self: PrintablePlate) -> int
        Set: Angle(self: PrintablePlate) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: PrintablePlate) -> Application """
        ...

    @property
    def Frequency(self) -> int:
        """
        Get: Frequency(self: PrintablePlate) -> int
        Set: Frequency(self: PrintablePlate) = value
        """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: PrintablePlate) -> int """
        ...

    @property
    def InkName(self) -> PbInkName:
        """ Get: InkName(self: PrintablePlate) -> PbInkName """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PrintablePlate) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PrintablePlate) -> object """
        ...

    @property
    def PrintPlate(self) -> bool:
        """
        Get: PrintPlate(self: PrintablePlate) -> bool
        Set: PrintPlate(self: PrintablePlate) = value
        """
        ...



class PrintablePlates(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PrintablePlates) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: PrintablePlates) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PrintablePlates) -> object """
        ...


    def FindPlateByInkName(self, InkName:PbInkName) -> PrintablePlate:
        """ FindPlateByInkName(self: PrintablePlates, InkName: PbInkName) -> PrintablePlate """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class PrintableRect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PrintableRect) -> Application """
        ...

    @property
    def Height(self) -> Single:
        """ Get: Height(self: PrintableRect) -> Single """
        ...

    @property
    def Left(self) -> Single:
        """ Get: Left(self: PrintableRect) -> Single """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PrintableRect) -> object """
        ...

    @property
    def Top(self) -> Single:
        """ Get: Top(self: PrintableRect) -> Single """
        ...

    @property
    def Width(self) -> Single:
        """ Get: Width(self: PrintableRect) -> Single """
        ...



class Printer: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Printer) -> Application """
        ...

    @property
    def DriverType(self) -> PbDriverType:
        """ Get: DriverType(self: Printer) -> PbDriverType """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: Printer) -> int """
        ...

    @property
    def IsActivePrinter(self) -> bool:
        """
        Get: IsActivePrinter(self: Printer) -> bool
        Set: IsActivePrinter(self: Printer) = value
        """
        ...

    @property
    def IsColor(self) -> bool:
        """ Get: IsColor(self: Printer) -> bool """
        ...

    @property
    def IsDuplex(self) -> bool:
        """ Get: IsDuplex(self: Printer) -> bool """
        ...

    @property
    def PaperHeight(self) -> int:
        """
        Get: PaperHeight(self: Printer) -> int
        Set: PaperHeight(self: Printer) = value
        """
        ...

    @property
    def PaperOrientation(self) -> PbOrientationType:
        """
        Get: PaperOrientation(self: Printer) -> PbOrientationType
        Set: PaperOrientation(self: Printer) = value
        """
        ...

    @property
    def PaperSize(self) -> str:
        """ Get: PaperSize(self: Printer) -> str """
        ...

    @property
    def PaperSource(self) -> str:
        """ Get: PaperSource(self: Printer) -> str """
        ...

    @property
    def PaperWidth(self) -> int:
        """
        Get: PaperWidth(self: Printer) -> int
        Set: PaperWidth(self: Printer) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Printer) -> object """
        ...

    @property
    def PrintableRect(self) -> PrintableRect:
        """ Get: PrintableRect(self: Printer) -> PrintableRect """
        ...

    @property
    def PrinterName(self) -> str:
        """ Get: PrinterName(self: Printer) -> str """
        ...

    @property
    def PrintMode(self) -> PbPrintMode:
        """
        Get: PrintMode(self: Printer) -> PbPrintMode
        Set: PrintMode(self: Printer) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ReaderSpread: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ReaderSpread) -> Application """
        ...

    @property
    def Height(self) -> Single:
        """ Get: Height(self: ReaderSpread) -> Single """
        ...

    @property
    def Left(self) -> Single:
        """ Get: Left(self: ReaderSpread) -> Single """
        ...

    @property
    def PageCount(self) -> int:
        """ Get: PageCount(self: ReaderSpread) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ReaderSpread) -> object """
        ...

    @property
    def Top(self) -> Single:
        """ Get: Top(self: ReaderSpread) -> Single """
        ...

    @property
    def Width(self) -> Single:
        """ Get: Width(self: ReaderSpread) -> Single """
        ...



class ReflectionFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Blur(self) -> Single:
        """
        Get: Blur(self: ReflectionFormat) -> Single
        Set: Blur(self: ReflectionFormat) = value
        """
        ...

    @property
    def Offset(self) -> Single:
        """
        Get: Offset(self: ReflectionFormat) -> Single
        Set: Offset(self: ReflectionFormat) = value
        """
        ...

    @property
    def Size(self) -> Single:
        """
        Get: Size(self: ReflectionFormat) -> Single
        Set: Size(self: ReflectionFormat) = value
        """
        ...

    @property
    def Transparency(self) -> Single:
        """
        Get: Transparency(self: ReflectionFormat) -> Single
        Set: Transparency(self: ReflectionFormat) = value
        """
        ...

    @property
    def Type(self): # -> MsoReflectionType
        """
        Get: Type(self: ReflectionFormat) -> MsoReflectionType
        Set: Type(self: ReflectionFormat) = value
        """
        ...

    @property
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: ReflectionFormat) -> MsoTriState
        Set: Visible(self: ReflectionFormat) = value
        """
        ...



class Row: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Row) -> Application """
        ...

    @property
    def Cells(self) -> CellRange:
        """ Get: Cells(self: Row) -> CellRange """
        ...

    @property
    def Height(self) -> object:
        """
        Get: Height(self: Row) -> object
        Set: Height(self: Row) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Row) -> object """
        ...


    def Delete(self): # -> 
        """ Delete(self: Row) """
        ...


class Rows(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Rows) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Rows) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Rows) -> object """
        ...


    def Add(self, BeforeRow:int) -> Row:
        """ Add(self: Rows, BeforeRow: int) -> Row """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class RulerGuide: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: RulerGuide) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: RulerGuide) -> object """
        ...

    @property
    def Position(self) -> object:
        """
        Get: Position(self: RulerGuide) -> object
        Set: Position(self: RulerGuide) = value
        """
        ...

    @property
    def Type(self) -> PbRulerGuideType:
        """
        Get: Type(self: RulerGuide) -> PbRulerGuideType
        Set: Type(self: RulerGuide) = value
        """
        ...


    def Delete(self): # -> 
        """ Delete(self: RulerGuide) """
        ...


class RulerGuides(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: RulerGuides) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: RulerGuides) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: RulerGuides) -> object """
        ...


    def Add(self, Position:object, Type:PbRulerGuideType): # -> 
        """ Add(self: RulerGuides, Position: object, Type: PbRulerGuideType) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ScratchArea: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ScratchArea) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ScratchArea) -> object """
        ...

    @property
    def Shapes(self) -> Shapes:
        """ Get: Shapes(self: ScratchArea) -> Shapes """
        ...



class Section: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Section) -> Application """
        ...

    @property
    def ContinueNumbersFromPreviousSection(self) -> bool:
        """
        Get: ContinueNumbersFromPreviousSection(self: Section) -> bool
        Set: ContinueNumbersFromPreviousSection(self: Section) = value
        """
        ...

    @property
    def PageNumberFormat(self) -> PbPageNumberFormat:
        """
        Get: PageNumberFormat(self: Section) -> PbPageNumberFormat
        Set: PageNumberFormat(self: Section) = value
        """
        ...

    @property
    def PageNumberStart(self) -> int:
        """
        Get: PageNumberStart(self: Section) -> int
        Set: PageNumberStart(self: Section) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Section) -> object """
        ...

    @property
    def ShowHeaderFooterOnFirstPage(self) -> bool:
        """
        Get: ShowHeaderFooterOnFirstPage(self: Section) -> bool
        Set: ShowHeaderFooterOnFirstPage(self: Section) = value
        """
        ...

    @property
    def StartPageIndex(self) -> int:
        """ Get: StartPageIndex(self: Section) -> int """
        ...


    def Delete(self): # -> 
        """ Delete(self: Section) """
        ...


class Sections(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Sections) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Sections) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Sections) -> object """
        ...


    def Add(self, StartPageIndex:int) -> Section:
        """ Add(self: Sections, StartPageIndex: int) -> Section """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Selection: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Selection) -> Application """
        ...

    @property
    def ChildShapeRange(self) -> ShapeRange:
        """ Get: ChildShapeRange(self: Selection) -> ShapeRange """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Selection) -> object """
        ...

    @property
    def ShapeRange(self) -> ShapeRange:
        """ Get: ShapeRange(self: Selection) -> ShapeRange """
        ...

    @property
    def TableCellRange(self) -> CellRange:
        """ Get: TableCellRange(self: Selection) -> CellRange """
        ...

    @property
    def TextRange(self) -> TextRange:
        """ Get: TextRange(self: Selection) -> TextRange """
        ...

    @property
    def Type(self) -> PbSelectionType:
        """ Get: Type(self: Selection) -> PbSelectionType """
        ...


    def Unselect(self): # -> 
        """ Unselect(self: Selection) """
        ...


class ShadowFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ShadowFormat) -> Application """
        ...

    @property
    def Blur(self) -> Single:
        """
        Get: Blur(self: ShadowFormat) -> Single
        Set: Blur(self: ShadowFormat) = value
        """
        ...

    @property
    def ForeColor(self) -> ColorFormat:
        """
        Get: ForeColor(self: ShadowFormat) -> ColorFormat
        Set: ForeColor(self: ShadowFormat) = value
        """
        ...

    @property
    def Obscured(self): # -> MsoTriState
        """
        Get: Obscured(self: ShadowFormat) -> MsoTriState
        Set: Obscured(self: ShadowFormat) = value
        """
        ...

    @property
    def OffsetX(self) -> object:
        """
        Get: OffsetX(self: ShadowFormat) -> object
        Set: OffsetX(self: ShadowFormat) = value
        """
        ...

    @property
    def OffsetY(self) -> object:
        """
        Get: OffsetY(self: ShadowFormat) -> object
        Set: OffsetY(self: ShadowFormat) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ShadowFormat) -> object """
        ...

    @property
    def RotateWithShape(self): # -> MsoTriState
        """
        Get: RotateWithShape(self: ShadowFormat) -> MsoTriState
        Set: RotateWithShape(self: ShadowFormat) = value
        """
        ...

    @property
    def Size(self) -> Single:
        """
        Get: Size(self: ShadowFormat) -> Single
        Set: Size(self: ShadowFormat) = value
        """
        ...

    @property
    def Transparency(self) -> Single:
        """
        Get: Transparency(self: ShadowFormat) -> Single
        Set: Transparency(self: ShadowFormat) = value
        """
        ...

    @property
    def Type(self): # -> MsoShadowType
        """
        Get: Type(self: ShadowFormat) -> MsoShadowType
        Set: Type(self: ShadowFormat) = value
        """
        ...

    @property
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: ShadowFormat) -> MsoTriState
        Set: Visible(self: ShadowFormat) = value
        """
        ...


    def IncrementOffsetX(self, Increment:object): # -> 
        """ IncrementOffsetX(self: ShadowFormat, Increment: object) """
        ...

    def IncrementOffsetY(self, Increment:object): # -> 
        """ IncrementOffsetY(self: ShadowFormat, Increment: object) """
        ...


class Shape: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Adjustments(self) -> Adjustments:
        """ Get: Adjustments(self: Shape) -> Adjustments """
        ...

    @property
    def AlternativeText(self) -> str:
        """
        Get: AlternativeText(self: Shape) -> str
        Set: AlternativeText(self: Shape) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: Shape) -> Application """
        ...

    @property
    def AutoShapeType(self): # -> MsoAutoShapeType
        """
        Get: AutoShapeType(self: Shape) -> MsoAutoShapeType
        Set: AutoShapeType(self: Shape) = value
        """
        ...

    @property
    def BlackWhiteMode(self): # -> MsoBlackWhiteMode
        """
        Get: BlackWhiteMode(self: Shape) -> MsoBlackWhiteMode
        Set: BlackWhiteMode(self: Shape) = value
        """
        ...

    @property
    def BorderArt(self) -> BorderArtFormat:
        """ Get: BorderArt(self: Shape) -> BorderArtFormat """
        ...

    @property
    def Callout(self) -> CalloutFormat:
        """ Get: Callout(self: Shape) -> CalloutFormat """
        ...

    @property
    def CatalogMergeItems(self) -> CatalogMergeShapes:
        """ Get: CatalogMergeItems(self: Shape) -> CatalogMergeShapes """
        ...

    @property
    def ConnectionSiteCount(self) -> int:
        """ Get: ConnectionSiteCount(self: Shape) -> int """
        ...

    @property
    def Connector(self): # -> MsoTriState
        """ Get: Connector(self: Shape) -> MsoTriState """
        ...

    @property
    def ConnectorFormat(self) -> ConnectorFormat:
        """ Get: ConnectorFormat(self: Shape) -> ConnectorFormat """
        ...

    @property
    def Fill(self) -> FillFormat:
        """ Get: Fill(self: Shape) -> FillFormat """
        ...

    @property
    def Glow(self) -> GlowFormat:
        """ Get: Glow(self: Shape) -> GlowFormat """
        ...

    @property
    def GroupItems(self) -> GroupShapes:
        """ Get: GroupItems(self: Shape) -> GroupShapes """
        ...

    @property
    def HasTable(self): # -> MsoTriState
        """ Get: HasTable(self: Shape) -> MsoTriState """
        ...

    @property
    def HasTextFrame(self): # -> MsoTriState
        """ Get: HasTextFrame(self: Shape) -> MsoTriState """
        ...

    @property
    def Height(self) -> object:
        """
        Get: Height(self: Shape) -> object
        Set: Height(self: Shape) = value
        """
        ...

    @property
    def HorizontalFlip(self): # -> MsoTriState
        """ Get: HorizontalFlip(self: Shape) -> MsoTriState """
        ...

    @property
    def Hyperlink(self) -> Hyperlink:
        """ Get: Hyperlink(self: Shape) -> Hyperlink """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: Shape) -> int """
        ...

    @property
    def InlineAlignment(self) -> PbInlineAlignment:
        """
        Get: InlineAlignment(self: Shape) -> PbInlineAlignment
        Set: InlineAlignment(self: Shape) = value
        """
        ...

    @property
    def InlineTextRange(self) -> TextRange:
        """ Get: InlineTextRange(self: Shape) -> TextRange """
        ...

    @property
    def IsExcess(self): # -> MsoTriState
        """ Get: IsExcess(self: Shape) -> MsoTriState """
        ...

    @property
    def IsGroupMember(self) -> bool:
        """ Get: IsGroupMember(self: Shape) -> bool """
        ...

    @property
    def IsInline(self): # -> MsoTriState
        """ Get: IsInline(self: Shape) -> MsoTriState """
        ...

    @property
    def Left(self) -> object:
        """
        Get: Left(self: Shape) -> object
        Set: Left(self: Shape) = value
        """
        ...

    @property
    def Line(self) -> LineFormat:
        """ Get: Line(self: Shape) -> LineFormat """
        ...

    @property
    def LinkFormat(self) -> LinkFormat:
        """ Get: LinkFormat(self: Shape) -> LinkFormat """
        ...

    @property
    def LockAspectRatio(self): # -> MsoTriState
        """
        Get: LockAspectRatio(self: Shape) -> MsoTriState
        Set: LockAspectRatio(self: Shape) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Shape) -> str
        Set: Name(self: Shape) = value
        """
        ...

    @property
    def Nodes(self) -> ShapeNodes:
        """ Get: Nodes(self: Shape) -> ShapeNodes """
        ...

    @property
    def OLEFormat(self) -> OLEFormat:
        """ Get: OLEFormat(self: Shape) -> OLEFormat """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Shape) -> object """
        ...

    @property
    def ParentGroupShape(self) -> Shape:
        """ Get: ParentGroupShape(self: Shape) -> Shape """
        ...

    @property
    def PictureFormat(self) -> PictureFormat:
        """ Get: PictureFormat(self: Shape) -> PictureFormat """
        ...

    @property
    def Reflection(self) -> ReflectionFormat:
        """ Get: Reflection(self: Shape) -> ReflectionFormat """
        ...

    @property
    def Rotation(self) -> Single:
        """
        Get: Rotation(self: Shape) -> Single
        Set: Rotation(self: Shape) = value
        """
        ...

    @property
    def Shadow(self) -> ShadowFormat:
        """ Get: Shadow(self: Shape) -> ShadowFormat """
        ...

    @property
    def SoftEdge(self) -> SoftEdgeFormat:
        """ Get: SoftEdge(self: Shape) -> SoftEdgeFormat """
        ...

    @property
    def Table(self) -> Table:
        """ Get: Table(self: Shape) -> Table """
        ...

    @property
    def Tags(self) -> Tags:
        """ Get: Tags(self: Shape) -> Tags """
        ...

    @property
    def TextEffect(self) -> TextEffectFormat:
        """ Get: TextEffect(self: Shape) -> TextEffectFormat """
        ...

    @property
    def TextFrame(self) -> TextFrame:
        """ Get: TextFrame(self: Shape) -> TextFrame """
        ...

    @property
    def TextWrap(self) -> WrapFormat:
        """ Get: TextWrap(self: Shape) -> WrapFormat """
        ...

    @property
    def ThreeD(self) -> ThreeDFormat:
        """ Get: ThreeD(self: Shape) -> ThreeDFormat """
        ...

    @property
    def Top(self) -> object:
        """
        Get: Top(self: Shape) -> object
        Set: Top(self: Shape) = value
        """
        ...

    @property
    def Type(self) -> PbShapeType:
        """ Get: Type(self: Shape) -> PbShapeType """
        ...

    @property
    def VerticalFlip(self): # -> MsoTriState
        """ Get: VerticalFlip(self: Shape) -> MsoTriState """
        ...

    @property
    def Vertices(self) -> object:
        """ Get: Vertices(self: Shape) -> object """
        ...

    @property
    def WebCheckBox(self) -> WebCheckBox:
        """ Get: WebCheckBox(self: Shape) -> WebCheckBox """
        ...

    @property
    def WebCommandButton(self) -> WebCommandButton:
        """ Get: WebCommandButton(self: Shape) -> WebCommandButton """
        ...

    @property
    def WebComponentFormat(self): # -> WebComponentFormat
        """ Get: WebComponentFormat(self: Shape) -> WebComponentFormat """
        ...

    @property
    def WebListBox(self) -> WebListBox:
        """ Get: WebListBox(self: Shape) -> WebListBox """
        ...

    @property
    def WebNavigationBarSetName(self) -> str:
        """ Get: WebNavigationBarSetName(self: Shape) -> str """
        ...

    @property
    def WebOptionButton(self) -> WebOptionButton:
        """ Get: WebOptionButton(self: Shape) -> WebOptionButton """
        ...

    @property
    def WebTextBox(self) -> WebTextBox:
        """ Get: WebTextBox(self: Shape) -> WebTextBox """
        ...

    @property
    def Width(self) -> object:
        """
        Get: Width(self: Shape) -> object
        Set: Width(self: Shape) = value
        """
        ...

    @property
    def Wizard(self) -> Wizard:
        """ Get: Wizard(self: Shape) -> Wizard """
        ...

    @property
    def WizardTag(self) -> PbWizardTag:
        """
        Get: WizardTag(self: Shape) -> PbWizardTag
        Set: WizardTag(self: Shape) = value
        """
        ...

    @property
    def WizardTagInstance(self) -> int:
        """
        Get: WizardTagInstance(self: Shape) -> int
        Set: WizardTagInstance(self: Shape) = value
        """
        ...

    @property
    def ZOrderPosition(self) -> int:
        """ Get: ZOrderPosition(self: Shape) -> int """
        ...


    def AddToCatalogMergeArea(self): # -> 
        """ AddToCatalogMergeArea(self: Shape) """
        ...

    def Apply(self): # -> 
        """ Apply(self: Shape) """
        ...

    def Copy(self): # -> 
        """ Copy(self: Shape) """
        ...

    def Cut(self): # -> 
        """ Cut(self: Shape) """
        ...

    def Delete(self): # -> 
        """ Delete(self: Shape) """
        ...

    def Duplicate(self) -> Shape:
        """ Duplicate(self: Shape) -> Shape """
        ...

    def Flip(self, FlipCmd): # ->  # Not found arg types: {'FlipCmd': 'MsoFlipCmd'}
        """ Flip(self: Shape, FlipCmd: MsoFlipCmd) """
        ...

    def GetHeight(self, Unit:PbUnitType) -> Single:
        """ GetHeight(self: Shape, Unit: PbUnitType) -> Single """
        ...

    def GetLeft(self, Unit:PbUnitType) -> Single:
        """ GetLeft(self: Shape, Unit: PbUnitType) -> Single """
        ...

    def GetTop(self, Unit:PbUnitType) -> Single:
        """ GetTop(self: Shape, Unit: PbUnitType) -> Single """
        ...

    def GetWidth(self, Unit:PbUnitType) -> Single:
        """ GetWidth(self: Shape, Unit: PbUnitType) -> Single """
        ...

    def IncrementLeft(self, Increment:object): # -> 
        """ IncrementLeft(self: Shape, Increment: object) """
        ...

    def IncrementRotation(self, Increment:Single): # -> 
        """ IncrementRotation(self: Shape, Increment: Single) """
        ...

    def IncrementTop(self, Increment:object): # -> 
        """ IncrementTop(self: Shape, Increment: object) """
        ...

    def MoveIntoTextFlow(self, Range:TextRange): # -> 
        """ MoveIntoTextFlow(self: Shape, Range: TextRange) """
        ...

    def MoveOutOfTextFlow(self): # -> 
        """ MoveOutOfTextFlow(self: Shape) """
        ...

    def MoveToPage(self, Page:int, Left:object, Top:object): # -> 
        """ MoveToPage(self: Shape, Page: int, Left: object, Top: object) """
        ...

    def PickUp(self): # -> 
        """ PickUp(self: Shape) """
        ...

    def RemoveCatalogMergeArea(self): # -> 
        """ RemoveCatalogMergeArea(self: Shape) """
        ...

    def RemoveFromCatalogMergeArea(self): # -> 
        """ RemoveFromCatalogMergeArea(self: Shape) """
        ...

    def RerouteConnections(self): # -> 
        """ RerouteConnections(self: Shape) """
        ...

    def SaveAsBuildingBlock(self, Name:str) -> BuildingBlock:
        """ SaveAsBuildingBlock(self: Shape, Name: str) -> BuildingBlock """
        ...

    def SaveAsPicture(self, Filename:str, pbResolution:PbPictureResolution): # -> 
        """ SaveAsPicture(self: Shape, Filename: str, pbResolution: PbPictureResolution) """
        ...

    def ScaleHeight(self, Factor:Single, RelativeToOriginalSize, fScale): # ->  # Not found arg types: {'RelativeToOriginalSize': 'MsoTriState', 'fScale': 'MsoScaleFrom'}
        """ ScaleHeight(self: Shape, Factor: Single, RelativeToOriginalSize: MsoTriState, fScale: MsoScaleFrom) """
        ...

    def ScaleWidth(self, Factor:Single, RelativeToOriginalSize, fScale): # ->  # Not found arg types: {'RelativeToOriginalSize': 'MsoTriState', 'fScale': 'MsoScaleFrom'}
        """ ScaleWidth(self: Shape, Factor: Single, RelativeToOriginalSize: MsoTriState, fScale: MsoScaleFrom) """
        ...

    def Select(self, Replace:object): # -> 
        """ Select(self: Shape, Replace: object) """
        ...

    def SetCaption(self, Style:CaptionStyle) -> Shape:
        """ SetCaption(self: Shape, Style: CaptionStyle) -> Shape """
        ...

    def SetShapesDefaultProperties(self): # -> 
        """ SetShapesDefaultProperties(self: Shape) """
        ...

    def Ungroup(self) -> ShapeRange:
        """ Ungroup(self: Shape) -> ShapeRange """
        ...

    def ZOrder(self, ZOrderCmd): # ->  # Not found arg types: {'ZOrderCmd': 'MsoZOrderCmd'}
        """ ZOrder(self: Shape, ZOrderCmd: MsoZOrderCmd) """
        ...


class ShapeNode: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ShapeNode) -> Application """
        ...

    @property
    def EditingType(self): # -> MsoEditingType
        """ Get: EditingType(self: ShapeNode) -> MsoEditingType """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ShapeNode) -> object """
        ...

    @property
    def Points(self) -> object:
        """ Get: Points(self: ShapeNode) -> object """
        ...

    @property
    def SegmentType(self): # -> MsoSegmentType
        """ Get: SegmentType(self: ShapeNode) -> MsoSegmentType """
        ...



class ShapeNodes(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ShapeNodes) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ShapeNodes) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ShapeNodes) -> object """
        ...


    def Delete(self, Index:int): # -> 
        """ Delete(self: ShapeNodes, Index: int) """
        ...

    def Insert(self, Index:int, SegmentType, EditingType, X1:object, Y1:object, X2:object, Y2:object, X3:object, Y3:object): # ->  # Not found arg types: {'EditingType': 'MsoEditingType', 'SegmentType': 'MsoSegmentType'}
        """ Insert(self: ShapeNodes, Index: int, SegmentType: MsoSegmentType, EditingType: MsoEditingType, X1: object, Y1: object, X2: object, Y2: object, X3: object, Y3: object) """
        ...

    def SetEditingType(self, Index:int, EditingType): # ->  # Not found arg types: {'EditingType': 'MsoEditingType'}
        """ SetEditingType(self: ShapeNodes, Index: int, EditingType: MsoEditingType) """
        ...

    def SetPosition(self, Index:int, X1:object, Y1:object): # -> 
        """ SetPosition(self: ShapeNodes, Index: int, X1: object, Y1: object) """
        ...

    def SetSegmentType(self, Index:int, SegmentType): # ->  # Not found arg types: {'SegmentType': 'MsoSegmentType'}
        """ SetSegmentType(self: ShapeNodes, Index: int, SegmentType: MsoSegmentType) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ShapeRange(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Adjustments(self) -> Adjustments:
        """ Get: Adjustments(self: ShapeRange) -> Adjustments """
        ...

    @property
    def AlternativeText(self) -> str:
        """
        Get: AlternativeText(self: ShapeRange) -> str
        Set: AlternativeText(self: ShapeRange) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: ShapeRange) -> Application """
        ...

    @property
    def AutoShapeType(self): # -> MsoAutoShapeType
        """
        Get: AutoShapeType(self: ShapeRange) -> MsoAutoShapeType
        Set: AutoShapeType(self: ShapeRange) = value
        """
        ...

    @property
    def BlackWhiteMode(self): # -> MsoBlackWhiteMode
        """
        Get: BlackWhiteMode(self: ShapeRange) -> MsoBlackWhiteMode
        Set: BlackWhiteMode(self: ShapeRange) = value
        """
        ...

    @property
    def Callout(self) -> CalloutFormat:
        """ Get: Callout(self: ShapeRange) -> CalloutFormat """
        ...

    @property
    def ConnectionSiteCount(self) -> int:
        """ Get: ConnectionSiteCount(self: ShapeRange) -> int """
        ...

    @property
    def Connector(self): # -> MsoTriState
        """ Get: Connector(self: ShapeRange) -> MsoTriState """
        ...

    @property
    def ConnectorFormat(self) -> ConnectorFormat:
        """ Get: ConnectorFormat(self: ShapeRange) -> ConnectorFormat """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ShapeRange) -> int """
        ...

    @property
    def Fill(self) -> FillFormat:
        """ Get: Fill(self: ShapeRange) -> FillFormat """
        ...

    @property
    def Glow(self) -> GlowFormat:
        """ Get: Glow(self: ShapeRange) -> GlowFormat """
        ...

    @property
    def GroupItems(self) -> GroupShapes:
        """ Get: GroupItems(self: ShapeRange) -> GroupShapes """
        ...

    @property
    def HasTable(self): # -> MsoTriState
        """ Get: HasTable(self: ShapeRange) -> MsoTriState """
        ...

    @property
    def HasTextFrame(self): # -> MsoTriState
        """ Get: HasTextFrame(self: ShapeRange) -> MsoTriState """
        ...

    @property
    def Height(self) -> object:
        """ Get: Height(self: ShapeRange) -> object """
        ...

    @property
    def HorizontalFlip(self): # -> MsoTriState
        """ Get: HorizontalFlip(self: ShapeRange) -> MsoTriState """
        ...

    @property
    def Hyperlink(self) -> Hyperlink:
        """ Get: Hyperlink(self: ShapeRange) -> Hyperlink """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: ShapeRange) -> int """
        ...

    @property
    def InlineAlignment(self) -> PbInlineAlignment:
        """
        Get: InlineAlignment(self: ShapeRange) -> PbInlineAlignment
        Set: InlineAlignment(self: ShapeRange) = value
        """
        ...

    @property
    def InlineTextRange(self) -> TextRange:
        """ Get: InlineTextRange(self: ShapeRange) -> TextRange """
        ...

    @property
    def IsInline(self): # -> MsoTriState
        """ Get: IsInline(self: ShapeRange) -> MsoTriState """
        ...

    @property
    def Left(self) -> object:
        """ Get: Left(self: ShapeRange) -> object """
        ...

    @property
    def Line(self) -> LineFormat:
        """ Get: Line(self: ShapeRange) -> LineFormat """
        ...

    @property
    def LinkFormat(self) -> LinkFormat:
        """ Get: LinkFormat(self: ShapeRange) -> LinkFormat """
        ...

    @property
    def LockAspectRatio(self): # -> MsoTriState
        """
        Get: LockAspectRatio(self: ShapeRange) -> MsoTriState
        Set: LockAspectRatio(self: ShapeRange) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ShapeRange) -> str
        Set: Name(self: ShapeRange) = value
        """
        ...

    @property
    def Nodes(self) -> ShapeNodes:
        """ Get: Nodes(self: ShapeRange) -> ShapeNodes """
        ...

    @property
    def OLEFormat(self) -> OLEFormat:
        """ Get: OLEFormat(self: ShapeRange) -> OLEFormat """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ShapeRange) -> object """
        ...

    @property
    def PictureFormat(self) -> PictureFormat:
        """ Get: PictureFormat(self: ShapeRange) -> PictureFormat """
        ...

    @property
    def Reflection(self) -> ReflectionFormat:
        """ Get: Reflection(self: ShapeRange) -> ReflectionFormat """
        ...

    @property
    def Rotation(self) -> Single:
        """
        Get: Rotation(self: ShapeRange) -> Single
        Set: Rotation(self: ShapeRange) = value
        """
        ...

    @property
    def Shadow(self) -> ShadowFormat:
        """ Get: Shadow(self: ShapeRange) -> ShadowFormat """
        ...

    @property
    def SoftEdge(self) -> SoftEdgeFormat:
        """ Get: SoftEdge(self: ShapeRange) -> SoftEdgeFormat """
        ...

    @property
    def Table(self) -> Table:
        """ Get: Table(self: ShapeRange) -> Table """
        ...

    @property
    def Tags(self) -> Tags:
        """ Get: Tags(self: ShapeRange) -> Tags """
        ...

    @property
    def TextEffect(self) -> TextEffectFormat:
        """ Get: TextEffect(self: ShapeRange) -> TextEffectFormat """
        ...

    @property
    def TextFrame(self) -> TextFrame:
        """ Get: TextFrame(self: ShapeRange) -> TextFrame """
        ...

    @property
    def TextWrap(self) -> WrapFormat:
        """ Get: TextWrap(self: ShapeRange) -> WrapFormat """
        ...

    @property
    def ThreeD(self) -> ThreeDFormat:
        """ Get: ThreeD(self: ShapeRange) -> ThreeDFormat """
        ...

    @property
    def Top(self) -> object:
        """ Get: Top(self: ShapeRange) -> object """
        ...

    @property
    def Type(self) -> PbShapeType:
        """ Get: Type(self: ShapeRange) -> PbShapeType """
        ...

    @property
    def VerticalFlip(self): # -> MsoTriState
        """ Get: VerticalFlip(self: ShapeRange) -> MsoTriState """
        ...

    @property
    def Vertices(self) -> object:
        """ Get: Vertices(self: ShapeRange) -> object """
        ...

    @property
    def Width(self) -> object:
        """ Get: Width(self: ShapeRange) -> object """
        ...

    @property
    def Wizard(self) -> Wizard:
        """ Get: Wizard(self: ShapeRange) -> Wizard """
        ...

    @property
    def WizardTag(self) -> PbWizardTag:
        """
        Get: WizardTag(self: ShapeRange) -> PbWizardTag
        Set: WizardTag(self: ShapeRange) = value
        """
        ...

    @property
    def WizardTagInstance(self) -> int:
        """
        Get: WizardTagInstance(self: ShapeRange) -> int
        Set: WizardTagInstance(self: ShapeRange) = value
        """
        ...

    @property
    def ZOrderPosition(self) -> int:
        """ Get: ZOrderPosition(self: ShapeRange) -> int """
        ...


    def AddToCatalogMergeArea(self): # -> 
        """ AddToCatalogMergeArea(self: ShapeRange) """
        ...

    def Align(self, AlignCmd, RelativeTo): # ->  # Not found arg types: {'RelativeTo': 'MsoTriState', 'AlignCmd': 'MsoAlignCmd'}
        """ Align(self: ShapeRange, AlignCmd: MsoAlignCmd, RelativeTo: MsoTriState) """
        ...

    def Apply(self): # -> 
        """ Apply(self: ShapeRange) """
        ...

    def Copy(self): # -> 
        """ Copy(self: ShapeRange) """
        ...

    def Cut(self): # -> 
        """ Cut(self: ShapeRange) """
        ...

    def Delete(self): # -> 
        """ Delete(self: ShapeRange) """
        ...

    def Distribute(self, DistributeCmd, RelativeTo): # ->  # Not found arg types: {'DistributeCmd': 'MsoDistributeCmd', 'RelativeTo': 'MsoTriState'}
        """ Distribute(self: ShapeRange, DistributeCmd: MsoDistributeCmd, RelativeTo: MsoTriState) """
        ...

    def Duplicate(self) -> ShapeRange:
        """ Duplicate(self: ShapeRange) -> ShapeRange """
        ...

    def Flip(self, FlipCmd): # ->  # Not found arg types: {'FlipCmd': 'MsoFlipCmd'}
        """ Flip(self: ShapeRange, FlipCmd: MsoFlipCmd) """
        ...

    def GetHeight(self, Unit:PbUnitType) -> Single:
        """ GetHeight(self: ShapeRange, Unit: PbUnitType) -> Single """
        ...

    def GetLeft(self, Unit:PbUnitType) -> Single:
        """ GetLeft(self: ShapeRange, Unit: PbUnitType) -> Single """
        ...

    def GetTop(self, Unit:PbUnitType) -> Single:
        """ GetTop(self: ShapeRange, Unit: PbUnitType) -> Single """
        ...

    def GetWidth(self, Unit:PbUnitType) -> Single:
        """ GetWidth(self: ShapeRange, Unit: PbUnitType) -> Single """
        ...

    def Group(self) -> Shape:
        """ Group(self: ShapeRange) -> Shape """
        ...

    def IncrementLeft(self, Increment:object): # -> 
        """ IncrementLeft(self: ShapeRange, Increment: object) """
        ...

    def IncrementRotation(self, Increment:Single): # -> 
        """ IncrementRotation(self: ShapeRange, Increment: Single) """
        ...

    def IncrementTop(self, Increment:object): # -> 
        """ IncrementTop(self: ShapeRange, Increment: object) """
        ...

    def MoveIntoTextFlow(self, Range:TextRange): # -> 
        """ MoveIntoTextFlow(self: ShapeRange, Range: TextRange) """
        ...

    def MoveOutOfTextFlow(self): # -> 
        """ MoveOutOfTextFlow(self: ShapeRange) """
        ...

    def PickUp(self): # -> 
        """ PickUp(self: ShapeRange) """
        ...

    def Regroup(self) -> Shape:
        """ Regroup(self: ShapeRange) -> Shape """
        ...

    def RemoveFromCatalogMergeArea(self): # -> 
        """ RemoveFromCatalogMergeArea(self: ShapeRange) """
        ...

    def RerouteConnections(self): # -> 
        """ RerouteConnections(self: ShapeRange) """
        ...

    def SaveAsBuildingBlock(self, Name:str) -> BuildingBlock:
        """ SaveAsBuildingBlock(self: ShapeRange, Name: str) -> BuildingBlock """
        ...

    def SaveAsPicture(self, Filename:str, pbResolution:PbPictureResolution): # -> 
        """ SaveAsPicture(self: ShapeRange, Filename: str, pbResolution: PbPictureResolution) """
        ...

    def ScaleHeight(self, Factor:Single, RelativeToOriginalSize, fScale): # ->  # Not found arg types: {'RelativeToOriginalSize': 'MsoTriState', 'fScale': 'MsoScaleFrom'}
        """ ScaleHeight(self: ShapeRange, Factor: Single, RelativeToOriginalSize: MsoTriState, fScale: MsoScaleFrom) """
        ...

    def ScaleWidth(self, Factor:Single, RelativeToOriginalSize, fScale): # ->  # Not found arg types: {'RelativeToOriginalSize': 'MsoTriState', 'fScale': 'MsoScaleFrom'}
        """ ScaleWidth(self: ShapeRange, Factor: Single, RelativeToOriginalSize: MsoTriState, fScale: MsoScaleFrom) """
        ...

    def Select(self, Replace:object): # -> 
        """ Select(self: ShapeRange, Replace: object) """
        ...

    def SetShapesDefaultProperties(self): # -> 
        """ SetShapesDefaultProperties(self: ShapeRange) """
        ...

    def Ungroup(self) -> ShapeRange:
        """ Ungroup(self: ShapeRange) -> ShapeRange """
        ...

    def ZOrder(self, ZOrderCmd): # ->  # Not found arg types: {'ZOrderCmd': 'MsoZOrderCmd'}
        """ ZOrder(self: ShapeRange, ZOrderCmd: MsoZOrderCmd) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Shapes(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Shapes) -> Application """
        ...

    @property
    def CanvasArrangementType(self) -> pbCanvasArrangementType:
        """
        Get: CanvasArrangementType(self: Shapes) -> pbCanvasArrangementType
        Set: CanvasArrangementType(self: Shapes) = value
        """
        ...

    @property
    def CanvasesCount(self) -> int:
        """ Get: CanvasesCount(self: Shapes) -> int """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Shapes) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Shapes) -> object """
        ...


    def AddBuildingBlock(self, BBlockIn:BuildingBlock, Left:object, Top:object) -> Shape:
        """ AddBuildingBlock(self: Shapes, BBlockIn: BuildingBlock, Left: object, Top: object) -> Shape """
        ...

    def AddCallout(self, Type, Left:object, Top:object, Width:object, Height:object) -> Shape: # Not found arg types: {'Type': 'MsoCalloutType'}
        """ AddCallout(self: Shapes, Type: MsoCalloutType, Left: object, Top: object, Width: object, Height: object) -> Shape """
        ...

    def AddCatalogMergeArea(self) -> Shape:
        """ AddCatalogMergeArea(self: Shapes) -> Shape """
        ...

    def AddCatalogMergeFieldToCanvas(self, CanvasId:int, CatalogMergeFieldType:pbCatalogMergeFieldType, DbCol:int): # -> 
        """ AddCatalogMergeFieldToCanvas(self: Shapes, CanvasId: int, CatalogMergeFieldType: pbCatalogMergeFieldType, DbCol: int) """
        ...

    def AddConnector(self, Type, BeginX:object, BeginY:object, EndX:object, EndY:object) -> Shape: # Not found arg types: {'Type': 'MsoConnectorType'}
        """ AddConnector(self: Shapes, Type: MsoConnectorType, BeginX: object, BeginY: object, EndX: object, EndY: object) -> Shape """
        ...

    def AddCurve(self, SafeArrayOfPoints:object) -> Shape:
        """ AddCurve(self: Shapes, SafeArrayOfPoints: object) -> Shape """
        ...

    def AddEmptyPictureFrame(self, Left:object, Top:object, Width:object, Height:object) -> Shape:
        """ AddEmptyPictureFrame(self: Shapes, Left: object, Top: object, Width: object, Height: object) -> Shape """
        ...

    def AddGroupWizard(self, Wizard:PbWizardGroup, Left:object, Top:object, Width:object, Height:object, Design:int) -> Shape:
        """ AddGroupWizard(self: Shapes, Wizard: PbWizardGroup, Left: object, Top: object, Width: object, Height: object, Design: int) -> Shape """
        ...

    def AddLabel(self, Orientation:PbTextOrientation, Left:object, Top:object, Width:object, Height:object) -> Shape:
        """ AddLabel(self: Shapes, Orientation: PbTextOrientation, Left: object, Top: object, Width: object, Height: object) -> Shape """
        ...

    def AddLine(self, BeginX:object, BeginY:object, EndX:object, EndY:object) -> Shape:
        """ AddLine(self: Shapes, BeginX: object, BeginY: object, EndX: object, EndY: object) -> Shape """
        ...

    def AddOLEObject(self, Left:object, Top:object, Width:object, Height:object, ClassName:str, Filename:str, Link) -> Shape: # Not found arg types: {'Link': 'MsoTriState'}
        """ AddOLEObject(self: Shapes, Left: object, Top: object, Width: object, Height: object, ClassName: str, Filename: str, Link: MsoTriState) -> Shape """
        ...

    def AddPicture(self, Filename:str, LinkToFile, SaveWithDocument, Left:object, Top:object, Width:object, Height:object) -> Shape: # Not found arg types: {'LinkToFile': 'MsoTriState', 'SaveWithDocument': 'MsoTriState'}
        """ AddPicture(self: Shapes, Filename: str, LinkToFile: MsoTriState, SaveWithDocument: MsoTriState, Left: object, Top: object, Width: object, Height: object) -> Shape """
        ...

    def AddPolyline(self, SafeArrayOfPoints:object) -> Shape:
        """ AddPolyline(self: Shapes, SafeArrayOfPoints: object) -> Shape """
        ...

    def AddShape(self, Type, Left:object, Top:object, Width:object, Height:object) -> Shape: # Not found arg types: {'Type': 'MsoAutoShapeType'}
        """ AddShape(self: Shapes, Type: MsoAutoShapeType, Left: object, Top: object, Width: object, Height: object) -> Shape """
        ...

    def AddTable(self, NumRows:int, NumColumns:int, Left:object, Top:object, Width:object, Height:object, FixedSize:bool, Direction:PbTableDirectionType) -> Shape:
        """ AddTable(self: Shapes, NumRows: int, NumColumns: int, Left: object, Top: object, Width: object, Height: object, FixedSize: bool, Direction: PbTableDirectionType) -> Shape """
        ...

    def AddTextbox(self, Orientation:PbTextOrientation, Left:object, Top:object, Width:object, Height:object) -> Shape:
        """ AddTextbox(self: Shapes, Orientation: PbTextOrientation, Left: object, Top: object, Width: object, Height: object) -> Shape """
        ...

    def AddTextEffect(self, PresetTextEffect, Text:str, FontName:str, FontSize:object, FontBold, FontItalic, Left:object, Top:object) -> Shape: # Not found arg types: {'FontItalic': 'MsoTriState', 'FontBold': 'MsoTriState', 'PresetTextEffect': 'MsoPresetTextEffect'}
        """ AddTextEffect(self: Shapes, PresetTextEffect: MsoPresetTextEffect, Text: str, FontName: str, FontSize: object, FontBold: MsoTriState, FontItalic: MsoTriState, Left: object, Top: object) -> Shape """
        ...

    def AddWebControl(self, Type:PbWebControlType, Left:object, Top:object, Width:object, Height:object, LaunchPropertiesWindow:bool) -> Shape:
        """ AddWebControl(self: Shapes, Type: PbWebControlType, Left: object, Top: object, Width: object, Height: object, LaunchPropertiesWindow: bool) -> Shape """
        ...

    def AddWebNavigationBar(self, Name:str, Left:object, Top:object, Width:object) -> Shape:
        """ AddWebNavigationBar(self: Shapes, Name: str, Left: object, Top: object, Width: object) -> Shape """
        ...

    def AddWordArt(self, PresetWordArt:pbPresetWordArt, Text:str, FontName:str, FontSize:object, FontBold, FontItalic, Left:object, Top:object) -> Shape: # Not found arg types: {'FontItalic': 'MsoTriState', 'FontBold': 'MsoTriState'}
        """ AddWordArt(self: Shapes, PresetWordArt: pbPresetWordArt, Text: str, FontName: str, FontSize: object, FontBold: MsoTriState, FontItalic: MsoTriState, Left: object, Top: object) -> Shape """
        ...

    def BuildFreeform(self, EditingType, X1:object, Y1:object) -> FreeformBuilder: # Not found arg types: {'EditingType': 'MsoEditingType'}
        """ BuildFreeform(self: Shapes, EditingType: MsoEditingType, X1: object, Y1: object) -> FreeformBuilder """
        ...

    def FindShapeByWizardTag(self, WizardTag:PbWizardTag, Instance:int) -> ShapeRange:
        """ FindShapeByWizardTag(self: Shapes, WizardTag: PbWizardTag, Instance: int) -> ShapeRange """
        ...

    def Paste(self) -> ShapeRange:
        """ Paste(self: Shapes) -> ShapeRange """
        ...

    def Range(self, Index:object) -> ShapeRange:
        """ Range(self: Shapes, Index: object) -> ShapeRange """
        ...

    def SelectAll(self): # -> 
        """ SelectAll(self: Shapes) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class SoftEdgeFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Radius(self) -> Single:
        """
        Get: Radius(self: SoftEdgeFormat) -> Single
        Set: Radius(self: SoftEdgeFormat) = value
        """
        ...

    @property
    def Type(self): # -> MsoSoftEdgeType
        """
        Get: Type(self: SoftEdgeFormat) -> MsoSoftEdgeType
        Set: Type(self: SoftEdgeFormat) = value
        """
        ...

    @property
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: SoftEdgeFormat) -> MsoTriState
        Set: Visible(self: SoftEdgeFormat) = value
        """
        ...



class Stories(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Stories) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Stories) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Stories) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Story: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Story) -> Application """
        ...

    @property
    def HasTable(self): # -> MsoTriState
        """ Get: HasTable(self: Story) -> MsoTriState """
        ...

    @property
    def HasTextFrame(self): # -> MsoTriState
        """ Get: HasTextFrame(self: Story) -> MsoTriState """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Story) -> object """
        ...

    @property
    def Table(self) -> Table:
        """ Get: Table(self: Story) -> Table """
        ...

    @property
    def TextFrame(self) -> TextFrame:
        """ Get: TextFrame(self: Story) -> TextFrame """
        ...

    @property
    def TextRange(self) -> TextRange:
        """ Get: TextRange(self: Story) -> TextRange """
        ...

    @property
    def Type(self) -> PbStoryType:
        """ Get: Type(self: Story) -> PbStoryType """
        ...



class Table: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Table) -> Application """
        ...

    @property
    def Columns(self) -> Columns:
        """ Get: Columns(self: Table) -> Columns """
        ...

    @property
    def GrowToFitText(self) -> bool:
        """
        Get: GrowToFitText(self: Table) -> bool
        Set: GrowToFitText(self: Table) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Table) -> object """
        ...

    @property
    def Rows(self) -> Rows:
        """ Get: Rows(self: Table) -> Rows """
        ...

    @property
    def TableDirection(self) -> PbTableDirectionType:
        """
        Get: TableDirection(self: Table) -> PbTableDirectionType
        Set: TableDirection(self: Table) = value
        """
        ...


    def ApplyAutoFormat(self, AutoFormat:PbTableAutoFormatType, TextFormatting:bool, TextAlignment:bool, Fill:bool, Borders:bool): # -> 
        """ ApplyAutoFormat(self: Table, AutoFormat: PbTableAutoFormatType, TextFormatting: bool, TextAlignment: bool, Fill: bool, Borders: bool) """
        ...


class TabStop: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Alignment(self) -> PbTabAlignmentType:
        """
        Get: Alignment(self: TabStop) -> PbTabAlignmentType
        Set: Alignment(self: TabStop) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: TabStop) -> Application """
        ...

    @property
    def Leader(self) -> PbTabLeaderType:
        """
        Get: Leader(self: TabStop) -> PbTabLeaderType
        Set: Leader(self: TabStop) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TabStop) -> object """
        ...

    @property
    def Position(self) -> object:
        """
        Get: Position(self: TabStop) -> object
        Set: Position(self: TabStop) = value
        """
        ...


    def Clear(self): # -> 
        """ Clear(self: TabStop) """
        ...


class TabStops(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: TabStops) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: TabStops) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TabStops) -> object """
        ...


    def Add(self, Position:object, Alignment:PbTabAlignmentType, Leader:PbTabLeaderType): # -> 
        """ Add(self: TabStops, Position: object, Alignment: PbTabAlignmentType, Leader: PbTabLeaderType) """
        ...

    def ClearAll(self): # -> 
        """ ClearAll(self: TabStops) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Tag: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Tag) -> Application """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Tag) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Tag) -> object """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: Tag) -> object
        Set: Value(self: Tag) = value
        """
        ...


    def Delete(self): # -> 
        """ Delete(self: Tag) """
        ...


class Tags(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Tags) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Tags) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Tags) -> object """
        ...


    def Add(self, Name:str, Value:object) -> Tag:
        """ Add(self: Tags, Name: str, Value: object) -> Tag """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class TextEffectFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Alignment(self): # -> MsoTextEffectAlignment
        """
        Get: Alignment(self: TextEffectFormat) -> MsoTextEffectAlignment
        Set: Alignment(self: TextEffectFormat) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: TextEffectFormat) -> Application """
        ...

    @property
    def FontBold(self): # -> MsoTriState
        """
        Get: FontBold(self: TextEffectFormat) -> MsoTriState
        Set: FontBold(self: TextEffectFormat) = value
        """
        ...

    @property
    def FontItalic(self): # -> MsoTriState
        """
        Get: FontItalic(self: TextEffectFormat) -> MsoTriState
        Set: FontItalic(self: TextEffectFormat) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: TextEffectFormat) -> str
        Set: FontName(self: TextEffectFormat) = value
        """
        ...

    @property
    def FontSize(self) -> object:
        """
        Get: FontSize(self: TextEffectFormat) -> object
        Set: FontSize(self: TextEffectFormat) = value
        """
        ...

    @property
    def KernedPairs(self): # -> MsoTriState
        """
        Get: KernedPairs(self: TextEffectFormat) -> MsoTriState
        Set: KernedPairs(self: TextEffectFormat) = value
        """
        ...

    @property
    def NormalizedHeight(self): # -> MsoTriState
        """
        Get: NormalizedHeight(self: TextEffectFormat) -> MsoTriState
        Set: NormalizedHeight(self: TextEffectFormat) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TextEffectFormat) -> object """
        ...

    @property
    def PresetShape(self): # -> MsoPresetTextEffectShape
        """
        Get: PresetShape(self: TextEffectFormat) -> MsoPresetTextEffectShape
        Set: PresetShape(self: TextEffectFormat) = value
        """
        ...

    @property
    def PresetTextEffect(self): # -> MsoPresetTextEffect
        """
        Get: PresetTextEffect(self: TextEffectFormat) -> MsoPresetTextEffect
        Set: PresetTextEffect(self: TextEffectFormat) = value
        """
        ...

    @property
    def PresetWordArt(self) -> pbPresetWordArt:
        """
        Get: PresetWordArt(self: TextEffectFormat) -> pbPresetWordArt
        Set: PresetWordArt(self: TextEffectFormat) = value
        """
        ...

    @property
    def RotatedChars(self): # -> MsoTriState
        """
        Get: RotatedChars(self: TextEffectFormat) -> MsoTriState
        Set: RotatedChars(self: TextEffectFormat) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: TextEffectFormat) -> str
        Set: Text(self: TextEffectFormat) = value
        """
        ...

    @property
    def Tracking(self) -> object:
        """
        Get: Tracking(self: TextEffectFormat) -> object
        Set: Tracking(self: TextEffectFormat) = value
        """
        ...


    def ToggleVerticalText(self): # -> 
        """ ToggleVerticalText(self: TextEffectFormat) """
        ...


class TextFrame: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: TextFrame) -> Application """
        ...

    @property
    def AutoFitText(self) -> PbTextAutoFitType:
        """
        Get: AutoFitText(self: TextFrame) -> PbTextAutoFitType
        Set: AutoFitText(self: TextFrame) = value
        """
        ...

    @property
    def Columns(self) -> int:
        """
        Get: Columns(self: TextFrame) -> int
        Set: Columns(self: TextFrame) = value
        """
        ...

    @property
    def ColumnSpacing(self) -> object:
        """
        Get: ColumnSpacing(self: TextFrame) -> object
        Set: ColumnSpacing(self: TextFrame) = value
        """
        ...

    @property
    def HasNextLink(self): # -> MsoTriState
        """ Get: HasNextLink(self: TextFrame) -> MsoTriState """
        ...

    @property
    def HasPreviousLink(self): # -> MsoTriState
        """ Get: HasPreviousLink(self: TextFrame) -> MsoTriState """
        ...

    @property
    def HasText(self): # -> MsoTriState
        """ Get: HasText(self: TextFrame) -> MsoTriState """
        ...

    @property
    def IncludeContinuedFromPage(self): # -> MsoTriState
        """
        Get: IncludeContinuedFromPage(self: TextFrame) -> MsoTriState
        Set: IncludeContinuedFromPage(self: TextFrame) = value
        """
        ...

    @property
    def IncludeContinuedOnPage(self): # -> MsoTriState
        """
        Get: IncludeContinuedOnPage(self: TextFrame) -> MsoTriState
        Set: IncludeContinuedOnPage(self: TextFrame) = value
        """
        ...

    @property
    def MarginBottom(self) -> object:
        """
        Get: MarginBottom(self: TextFrame) -> object
        Set: MarginBottom(self: TextFrame) = value
        """
        ...

    @property
    def MarginLeft(self) -> object:
        """
        Get: MarginLeft(self: TextFrame) -> object
        Set: MarginLeft(self: TextFrame) = value
        """
        ...

    @property
    def MarginRight(self) -> object:
        """
        Get: MarginRight(self: TextFrame) -> object
        Set: MarginRight(self: TextFrame) = value
        """
        ...

    @property
    def MarginTop(self) -> object:
        """
        Get: MarginTop(self: TextFrame) -> object
        Set: MarginTop(self: TextFrame) = value
        """
        ...

    @property
    def NextLinkedTextFrame(self) -> TextFrame:
        """
        Get: NextLinkedTextFrame(self: TextFrame) -> TextFrame
        Set: NextLinkedTextFrame(self: TextFrame) = value
        """
        ...

    @property
    def Orientation(self) -> PbTextOrientation:
        """
        Get: Orientation(self: TextFrame) -> PbTextOrientation
        Set: Orientation(self: TextFrame) = value
        """
        ...

    @property
    def Overflowing(self): # -> MsoTriState
        """ Get: Overflowing(self: TextFrame) -> MsoTriState """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TextFrame) -> object """
        ...

    @property
    def PreviousLinkedTextFrame(self) -> TextFrame:
        """ Get: PreviousLinkedTextFrame(self: TextFrame) -> TextFrame """
        ...

    @property
    def Story(self) -> Story:
        """ Get: Story(self: TextFrame) -> Story """
        ...

    @property
    def TextRange(self) -> TextRange:
        """ Get: TextRange(self: TextFrame) -> TextRange """
        ...

    @property
    def VerticalTextAlignment(self) -> PbVerticalTextAlignmentType:
        """
        Get: VerticalTextAlignment(self: TextFrame) -> PbVerticalTextAlignmentType
        Set: VerticalTextAlignment(self: TextFrame) = value
        """
        ...


    def BreakForwardLink(self): # -> 
        """ BreakForwardLink(self: TextFrame) """
        ...

    def ValidLinkTarget(self, LinkTarget:Shape) -> bool:
        """ ValidLinkTarget(self: TextFrame, LinkTarget: Shape) -> bool """
        ...


class TextRange: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: TextRange) -> Application """
        ...

    @property
    def BoundHeight(self) -> Single:
        """ Get: BoundHeight(self: TextRange) -> Single """
        ...

    @property
    def BoundLeft(self) -> Single:
        """ Get: BoundLeft(self: TextRange) -> Single """
        ...

    @property
    def BoundTop(self) -> Single:
        """ Get: BoundTop(self: TextRange) -> Single """
        ...

    @property
    def BoundWidth(self) -> Single:
        """ Get: BoundWidth(self: TextRange) -> Single """
        ...

    @property
    def ContainingObject(self) -> object:
        """ Get: ContainingObject(self: TextRange) -> object """
        ...

    @property
    def DropCap(self) -> DropCap:
        """ Get: DropCap(self: TextRange) -> DropCap """
        ...

    @property
    def Duplicate(self) -> TextRange:
        """ Get: Duplicate(self: TextRange) -> TextRange """
        ...

    @property
    def End(self) -> int:
        """
        Get: End(self: TextRange) -> int
        Set: End(self: TextRange) = value
        """
        ...

    @property
    def Fields(self) -> Fields:
        """ Get: Fields(self: TextRange) -> Fields """
        ...

    @property
    def Find(self) -> FindReplace:
        """ Get: Find(self: TextRange) -> FindReplace """
        ...

    @property
    def Font(self) -> Font:
        """
        Get: Font(self: TextRange) -> Font
        Set: Font(self: TextRange) = value
        """
        ...

    @property
    def Hyperlinks(self) -> Hyperlinks:
        """ Get: Hyperlinks(self: TextRange) -> Hyperlinks """
        ...

    @property
    def InlineShapes(self) -> InlineShapes:
        """ Get: InlineShapes(self: TextRange) -> InlineShapes """
        ...

    @property
    def LanguageID(self): # -> MsoLanguageID
        """
        Get: LanguageID(self: TextRange) -> MsoLanguageID
        Set: LanguageID(self: TextRange) = value
        """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: TextRange) -> int """
        ...

    @property
    def LinesCount(self) -> int:
        """ Get: LinesCount(self: TextRange) -> int """
        ...

    @property
    def MajorityFont(self) -> Font:
        """ Get: MajorityFont(self: TextRange) -> Font """
        ...

    @property
    def MajorityParagraphFormat(self) -> ParagraphFormat:
        """ Get: MajorityParagraphFormat(self: TextRange) -> ParagraphFormat """
        ...

    @property
    def ParagraphFormat(self) -> ParagraphFormat:
        """
        Get: ParagraphFormat(self: TextRange) -> ParagraphFormat
        Set: ParagraphFormat(self: TextRange) = value
        """
        ...

    @property
    def ParagraphsCount(self) -> int:
        """ Get: ParagraphsCount(self: TextRange) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TextRange) -> object """
        ...

    @property
    def Script(self) -> PbFontScriptType:
        """ Get: Script(self: TextRange) -> PbFontScriptType """
        ...

    @property
    def Start(self) -> int:
        """
        Get: Start(self: TextRange) -> int
        Set: Start(self: TextRange) = value
        """
        ...

    @property
    def Story(self) -> Story:
        """ Get: Story(self: TextRange) -> Story """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: TextRange) -> str
        Set: Text(self: TextRange) = value
        """
        ...

    @property
    def WordsCount(self) -> int:
        """ Get: WordsCount(self: TextRange) -> int """
        ...


    def Characters(self, Start:int, Length:int) -> TextRange:
        """ Characters(self: TextRange, Start: int, Length: int) -> TextRange """
        ...

    def Collapse(self, Direction:PbCollapseDirection): # -> 
        """ Collapse(self: TextRange, Direction: PbCollapseDirection) """
        ...

    def Copy(self): # -> 
        """ Copy(self: TextRange) """
        ...

    def Cut(self): # -> 
        """ Cut(self: TextRange) """
        ...

    def Delete(self): # -> 
        """ Delete(self: TextRange) """
        ...

    def Expand(self, Unit:PbTextUnit) -> int:
        """ Expand(self: TextRange, Unit: PbTextUnit) -> int """
        ...

    def InsertAfter(self, NewText:str) -> TextRange:
        """ InsertAfter(self: TextRange, NewText: str) -> TextRange """
        ...

    def InsertBarcode(self) -> TextRange:
        """ InsertBarcode(self: TextRange) -> TextRange """
        ...

    def InsertBefore(self, NewText:str) -> TextRange:
        """ InsertBefore(self: TextRange, NewText: str) -> TextRange """
        ...

    def InsertDateTime(self, Format:PbDateTimeFormat, InsertAsField:bool, InsertAsFullWidth:bool, Language, Calendar:PbCalendarType) -> TextRange: # Not found arg types: {'Language': 'MsoLanguageID'}
        """ InsertDateTime(self: TextRange, Format: PbDateTimeFormat, InsertAsField: bool, InsertAsFullWidth: bool, Language: MsoLanguageID, Calendar: PbCalendarType) -> TextRange """
        ...

    def InsertMailMergeField(self, varIndex:object) -> TextRange:
        """ InsertMailMergeField(self: TextRange, varIndex: object) -> TextRange """
        ...

    def InsertPageNumber(self, Type:PbPageNumberType) -> TextRange:
        """ InsertPageNumber(self: TextRange, Type: PbPageNumberType) -> TextRange """
        ...

    def InsertSymbol(self, FontName:str, CharIndex:int) -> TextRange:
        """ InsertSymbol(self: TextRange, FontName: str, CharIndex: int) -> TextRange """
        ...

    def Lines(self, Start:int, Length:int) -> TextRange:
        """ Lines(self: TextRange, Start: int, Length: int) -> TextRange """
        ...

    def Move(self, Unit:PbTextUnit, Size:int) -> int:
        """ Move(self: TextRange, Unit: PbTextUnit, Size: int) -> int """
        ...

    def MoveEnd(self, Unit:PbTextUnit, Size:int) -> int:
        """ MoveEnd(self: TextRange, Unit: PbTextUnit, Size: int) -> int """
        ...

    def MoveStart(self, Unit:PbTextUnit, Size:int) -> int:
        """ MoveStart(self: TextRange, Unit: PbTextUnit, Size: int) -> int """
        ...

    def Paragraphs(self, Start:int, Length:int) -> TextRange:
        """ Paragraphs(self: TextRange, Start: int, Length: int) -> TextRange """
        ...

    def Paste(self) -> TextRange:
        """ Paste(self: TextRange) -> TextRange """
        ...

    def Select(self): # -> 
        """ Select(self: TextRange) """
        ...

    def Words(self, Start:int, Length:int) -> TextRange:
        """ Words(self: TextRange, Start: int, Length: int) -> TextRange """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class TextStyle: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: TextStyle) -> Application """
        ...

    @property
    def BaseStyle(self) -> str:
        """
        Get: BaseStyle(self: TextStyle) -> str
        Set: BaseStyle(self: TextStyle) = value
        """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: TextStyle) -> str """
        ...

    @property
    def Font(self) -> Font:
        """
        Get: Font(self: TextStyle) -> Font
        Set: Font(self: TextStyle) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: TextStyle) -> str """
        ...

    @property
    def NextParagraphStyle(self) -> str:
        """
        Get: NextParagraphStyle(self: TextStyle) -> str
        Set: NextParagraphStyle(self: TextStyle) = value
        """
        ...

    @property
    def ParagraphFormat(self) -> ParagraphFormat:
        """
        Get: ParagraphFormat(self: TextStyle) -> ParagraphFormat
        Set: ParagraphFormat(self: TextStyle) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TextStyle) -> object """
        ...


    def Delete(self): # -> 
        """ Delete(self: TextStyle) """
        ...


class TextStyles(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: TextStyles) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: TextStyles) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TextStyles) -> object """
        ...


    def Add(self, StyleName:str, BasedOn:str, Font:Font, ParagraphFormat:ParagraphFormat) -> TextStyle:
        """ Add(self: TextStyles, StyleName: str, BasedOn: str, Font: Font, ParagraphFormat: ParagraphFormat) -> TextStyle """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ThreeDFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ThreeDFormat) -> Application """
        ...

    @property
    def BevelBottomDepth(self) -> Single:
        """
        Get: BevelBottomDepth(self: ThreeDFormat) -> Single
        Set: BevelBottomDepth(self: ThreeDFormat) = value
        """
        ...

    @property
    def BevelBottomInset(self) -> Single:
        """
        Get: BevelBottomInset(self: ThreeDFormat) -> Single
        Set: BevelBottomInset(self: ThreeDFormat) = value
        """
        ...

    @property
    def BevelBottomType(self): # -> MsoBevelType
        """
        Get: BevelBottomType(self: ThreeDFormat) -> MsoBevelType
        Set: BevelBottomType(self: ThreeDFormat) = value
        """
        ...

    @property
    def BevelTopDepth(self) -> Single:
        """
        Get: BevelTopDepth(self: ThreeDFormat) -> Single
        Set: BevelTopDepth(self: ThreeDFormat) = value
        """
        ...

    @property
    def BevelTopInset(self) -> Single:
        """
        Get: BevelTopInset(self: ThreeDFormat) -> Single
        Set: BevelTopInset(self: ThreeDFormat) = value
        """
        ...

    @property
    def BevelTopType(self): # -> MsoBevelType
        """
        Get: BevelTopType(self: ThreeDFormat) -> MsoBevelType
        Set: BevelTopType(self: ThreeDFormat) = value
        """
        ...

    @property
    def ContourColor(self) -> ColorFormat:
        """ Get: ContourColor(self: ThreeDFormat) -> ColorFormat """
        ...

    @property
    def ContourWidth(self) -> Single:
        """
        Get: ContourWidth(self: ThreeDFormat) -> Single
        Set: ContourWidth(self: ThreeDFormat) = value
        """
        ...

    @property
    def Depth(self) -> object:
        """
        Get: Depth(self: ThreeDFormat) -> object
        Set: Depth(self: ThreeDFormat) = value
        """
        ...

    @property
    def ExtrusionColor(self) -> ColorFormat:
        """ Get: ExtrusionColor(self: ThreeDFormat) -> ColorFormat """
        ...

    @property
    def ExtrusionColorType(self): # -> MsoExtrusionColorType
        """
        Get: ExtrusionColorType(self: ThreeDFormat) -> MsoExtrusionColorType
        Set: ExtrusionColorType(self: ThreeDFormat) = value
        """
        ...

    @property
    def FieldOfView(self) -> Single:
        """
        Get: FieldOfView(self: ThreeDFormat) -> Single
        Set: FieldOfView(self: ThreeDFormat) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ThreeDFormat) -> object """
        ...

    @property
    def Perspective(self): # -> MsoTriState
        """
        Get: Perspective(self: ThreeDFormat) -> MsoTriState
        Set: Perspective(self: ThreeDFormat) = value
        """
        ...

    @property
    def PresetExtrusionDirection(self): # -> MsoPresetExtrusionDirection
        """ Get: PresetExtrusionDirection(self: ThreeDFormat) -> MsoPresetExtrusionDirection """
        ...

    @property
    def PresetLightingDirection(self): # -> MsoPresetLightingDirection
        """
        Get: PresetLightingDirection(self: ThreeDFormat) -> MsoPresetLightingDirection
        Set: PresetLightingDirection(self: ThreeDFormat) = value
        """
        ...

    @property
    def PresetLightingSoftness(self): # -> MsoPresetLightingSoftness
        """
        Get: PresetLightingSoftness(self: ThreeDFormat) -> MsoPresetLightingSoftness
        Set: PresetLightingSoftness(self: ThreeDFormat) = value
        """
        ...

    @property
    def PresetMaterial(self): # -> MsoPresetMaterial
        """
        Get: PresetMaterial(self: ThreeDFormat) -> MsoPresetMaterial
        Set: PresetMaterial(self: ThreeDFormat) = value
        """
        ...

    @property
    def PresetThreeDFormat(self): # -> MsoPresetThreeDFormat
        """ Get: PresetThreeDFormat(self: ThreeDFormat) -> MsoPresetThreeDFormat """
        ...

    @property
    def RotationX(self) -> Single:
        """
        Get: RotationX(self: ThreeDFormat) -> Single
        Set: RotationX(self: ThreeDFormat) = value
        """
        ...

    @property
    def RotationY(self) -> Single:
        """
        Get: RotationY(self: ThreeDFormat) -> Single
        Set: RotationY(self: ThreeDFormat) = value
        """
        ...

    @property
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: ThreeDFormat) -> MsoTriState
        Set: Visible(self: ThreeDFormat) = value
        """
        ...


    def IncrementRotationX(self, Increment:Single): # -> 
        """ IncrementRotationX(self: ThreeDFormat, Increment: Single) """
        ...

    def IncrementRotationY(self, Increment:Single): # -> 
        """ IncrementRotationY(self: ThreeDFormat, Increment: Single) """
        ...

    def ResetRotation(self): # -> 
        """ ResetRotation(self: ThreeDFormat) """
        ...

    def SetExtrusionDirection(self, PresetExtrusionDirection): # ->  # Not found arg types: {'PresetExtrusionDirection': 'MsoPresetExtrusionDirection'}
        """ SetExtrusionDirection(self: ThreeDFormat, PresetExtrusionDirection: MsoPresetExtrusionDirection) """
        ...

    def SetThreeDFormat(self, PresetThreeDFormat): # ->  # Not found arg types: {'PresetThreeDFormat': 'MsoPresetThreeDFormat'}
        """ SetThreeDFormat(self: ThreeDFormat, PresetThreeDFormat: MsoPresetThreeDFormat) """
        ...


class View: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActivePage(self) -> Page:
        """
        Get: ActivePage(self: View) -> Page
        Set: ActivePage(self: View) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: View) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: View) -> object """
        ...

    @property
    def Zoom(self) -> PbZoom:
        """
        Get: Zoom(self: View) -> PbZoom
        Set: Zoom(self: View) = value
        """
        ...


    def ScrollShapeIntoView(self, Shape:Shape): # -> 
        """ ScrollShapeIntoView(self: View, Shape: Shape) """
        ...

    def ZoomIn(self): # -> 
        """ ZoomIn(self: View) """
        ...

    def ZoomOut(self): # -> 
        """ ZoomOut(self: View) """
        ...


class WebCheckBox: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: WebCheckBox) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WebCheckBox) -> object """
        ...

    @property
    def ReturnDataLabel(self) -> str:
        """
        Get: ReturnDataLabel(self: WebCheckBox) -> str
        Set: ReturnDataLabel(self: WebCheckBox) = value
        """
        ...

    @property
    def Selected(self): # -> MsoTriState
        """
        Get: Selected(self: WebCheckBox) -> MsoTriState
        Set: Selected(self: WebCheckBox) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: WebCheckBox) -> str
        Set: Value(self: WebCheckBox) = value
        """
        ...



class WebCommandButton: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActionURL(self) -> str:
        """
        Get: ActionURL(self: WebCommandButton) -> str
        Set: ActionURL(self: WebCommandButton) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: WebCommandButton) -> Application """
        ...

    @property
    def ButtonText(self) -> str:
        """
        Get: ButtonText(self: WebCommandButton) -> str
        Set: ButtonText(self: WebCommandButton) = value
        """
        ...

    @property
    def ButtonType(self) -> PbCommandButtonType:
        """
        Get: ButtonType(self: WebCommandButton) -> PbCommandButtonType
        Set: ButtonType(self: WebCommandButton) = value
        """
        ...

    @property
    def DataFileFormat(self) -> PbSubmitDataFormatType:
        """
        Get: DataFileFormat(self: WebCommandButton) -> PbSubmitDataFormatType
        Set: DataFileFormat(self: WebCommandButton) = value
        """
        ...

    @property
    def DataFileName(self) -> str:
        """
        Get: DataFileName(self: WebCommandButton) -> str
        Set: DataFileName(self: WebCommandButton) = value
        """
        ...

    @property
    def DataRetrievalMethod(self) -> PbSubmitDataRetrievalMethodType:
        """
        Get: DataRetrievalMethod(self: WebCommandButton) -> PbSubmitDataRetrievalMethodType
        Set: DataRetrievalMethod(self: WebCommandButton) = value
        """
        ...

    @property
    def EmailAddress(self) -> str:
        """
        Get: EmailAddress(self: WebCommandButton) -> str
        Set: EmailAddress(self: WebCommandButton) = value
        """
        ...

    @property
    def EmailSubject(self) -> str:
        """
        Get: EmailSubject(self: WebCommandButton) -> str
        Set: EmailSubject(self: WebCommandButton) = value
        """
        ...

    @property
    def HiddenFields(self) -> WebHiddenFields:
        """ Get: HiddenFields(self: WebCommandButton) -> WebHiddenFields """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WebCommandButton) -> object """
        ...

    @property
    def PostFormData(self): # -> MsoTriState
        """
        Get: PostFormData(self: WebCommandButton) -> MsoTriState
        Set: PostFormData(self: WebCommandButton) = value
        """
        ...



class WebHiddenFields(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: WebHiddenFields) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: WebHiddenFields) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WebHiddenFields) -> object """
        ...


    def Add(self, Name:str, Value:str) -> int:
        """ Add(self: WebHiddenFields, Name: str, Value: str) -> int """
        ...

    def Delete(self, Index:int): # -> 
        """ Delete(self: WebHiddenFields, Index: int) """
        ...

    def Name(self, Index:int) -> str:
        """ Name(self: WebHiddenFields, Index: int) -> str """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class WebListBox: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: WebListBox) -> Application """
        ...

    @property
    def ListBoxItems(self) -> WebListBoxItems:
        """ Get: ListBoxItems(self: WebListBox) -> WebListBoxItems """
        ...

    @property
    def MultiSelect(self): # -> MsoTriState
        """
        Get: MultiSelect(self: WebListBox) -> MsoTriState
        Set: MultiSelect(self: WebListBox) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WebListBox) -> object """
        ...

    @property
    def ReturnDataLabel(self) -> str:
        """
        Get: ReturnDataLabel(self: WebListBox) -> str
        Set: ReturnDataLabel(self: WebListBox) = value
        """
        ...



class WebListBoxItems(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: WebListBoxItems) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: WebListBoxItems) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WebListBoxItems) -> object """
        ...


    def AddItem(self, Item:str, Index:int, SelectState:bool, ItemValue:str): # -> 
        """ AddItem(self: WebListBoxItems, Item: str, Index: int, SelectState: bool, ItemValue: str) """
        ...

    def Delete(self, Index:int): # -> 
        """ Delete(self: WebListBoxItems, Index: int) """
        ...

    def Selected(self, Index:int, SelectState:bool): # -> 
        """ Selected(self: WebListBoxItems, Index: int, SelectState: bool) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class WebNavigationBarHyperlinks(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: WebNavigationBarHyperlinks) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: WebNavigationBarHyperlinks) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WebNavigationBarHyperlinks) -> object """
        ...


    def Add(self, Address:str, RelativePage:PbHlinkTargetType, PageID:int, TextToDisplay:str, Index:int) -> Hyperlink:
        """ Add(self: WebNavigationBarHyperlinks, Address: str, RelativePage: PbHlinkTargetType, PageID: int, TextToDisplay: str, Index: int) -> Hyperlink """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class WebNavigationBarSet: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: WebNavigationBarSet) -> Application """
        ...

    @property
    def AutoUpdate(self) -> bool:
        """
        Get: AutoUpdate(self: WebNavigationBarSet) -> bool
        Set: AutoUpdate(self: WebNavigationBarSet) = value
        """
        ...

    @property
    def ButtonStyle(self) -> PbWizardNavBarButtonStyle:
        """
        Get: ButtonStyle(self: WebNavigationBarSet) -> PbWizardNavBarButtonStyle
        Set: ButtonStyle(self: WebNavigationBarSet) = value
        """
        ...

    @property
    def Design(self) -> PbWizardNavBarDesign:
        """
        Get: Design(self: WebNavigationBarSet) -> PbWizardNavBarDesign
        Set: Design(self: WebNavigationBarSet) = value
        """
        ...

    @property
    def HorizontalAlignment(self) -> PbWizardNavBarAlignment:
        """
        Get: HorizontalAlignment(self: WebNavigationBarSet) -> PbWizardNavBarAlignment
        Set: HorizontalAlignment(self: WebNavigationBarSet) = value
        """
        ...

    @property
    def HorizontalButtonCount(self) -> int:
        """
        Get: HorizontalButtonCount(self: WebNavigationBarSet) -> int
        Set: HorizontalButtonCount(self: WebNavigationBarSet) = value
        """
        ...

    @property
    def IsHorizontal(self) -> bool:
        """ Get: IsHorizontal(self: WebNavigationBarSet) -> bool """
        ...

    @property
    def Links(self) -> WebNavigationBarHyperlinks:
        """
        Get: Links(self: WebNavigationBarSet) -> WebNavigationBarHyperlinks
        Set: Links(self: WebNavigationBarSet) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: WebNavigationBarSet) -> str
        Set: Name(self: WebNavigationBarSet) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WebNavigationBarSet) -> object """
        ...

    @property
    def ShowSelected(self) -> bool:
        """
        Get: ShowSelected(self: WebNavigationBarSet) -> bool
        Set: ShowSelected(self: WebNavigationBarSet) = value
        """
        ...


    def AddToEveryPage(self, Left:object, Top:object, Width:object) -> ShapeRange:
        """ AddToEveryPage(self: WebNavigationBarSet, Left: object, Top: object, Width: object) -> ShapeRange """
        ...

    def ChangeOrientation(self, Orientation:PbNavBarOrientation): # -> 
        """ ChangeOrientation(self: WebNavigationBarSet, Orientation: PbNavBarOrientation) """
        ...

    def DeleteSetAndInstances(self): # -> 
        """ DeleteSetAndInstances(self: WebNavigationBarSet) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class WebNavigationBarSets(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: WebNavigationBarSets) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: WebNavigationBarSets) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WebNavigationBarSets) -> object """
        ...


    def AddSet(self, Name:str, Design:PbWizardNavBarDesign, AutoUpdate:bool) -> WebNavigationBarSet:
        """ AddSet(self: WebNavigationBarSets, Name: str, Design: PbWizardNavBarDesign, AutoUpdate: bool) -> WebNavigationBarSet """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class WebOptionButton: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: WebOptionButton) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WebOptionButton) -> object """
        ...

    @property
    def ReturnDataLabel(self) -> str:
        """
        Get: ReturnDataLabel(self: WebOptionButton) -> str
        Set: ReturnDataLabel(self: WebOptionButton) = value
        """
        ...

    @property
    def Selected(self): # -> MsoTriState
        """
        Get: Selected(self: WebOptionButton) -> MsoTriState
        Set: Selected(self: WebOptionButton) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: WebOptionButton) -> str
        Set: Value(self: WebOptionButton) = value
        """
        ...



class WebOptions: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AlwaysSaveInDefaultEncoding(self) -> bool:
        """
        Get: AlwaysSaveInDefaultEncoding(self: WebOptions) -> bool
        Set: AlwaysSaveInDefaultEncoding(self: WebOptions) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: WebOptions) -> Application """
        ...

    @property
    def EmailAsImg(self) -> bool:
        """
        Get: EmailAsImg(self: WebOptions) -> bool
        Set: EmailAsImg(self: WebOptions) = value
        """
        ...

    @property
    def EnableIncrementalUpload(self) -> bool:
        """
        Get: EnableIncrementalUpload(self: WebOptions) -> bool
        Set: EnableIncrementalUpload(self: WebOptions) = value
        """
        ...

    @property
    def Encoding(self): # -> MsoEncoding
        """
        Get: Encoding(self: WebOptions) -> MsoEncoding
        Set: Encoding(self: WebOptions) = value
        """
        ...

    @property
    def OrganizeInFolder(self) -> bool:
        """
        Get: OrganizeInFolder(self: WebOptions) -> bool
        Set: OrganizeInFolder(self: WebOptions) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WebOptions) -> object """
        ...

    @property
    def RelyOnVML(self) -> bool:
        """
        Get: RelyOnVML(self: WebOptions) -> bool
        Set: RelyOnVML(self: WebOptions) = value
        """
        ...

    @property
    def ShowOnlyWebFonts(self) -> bool:
        """
        Get: ShowOnlyWebFonts(self: WebOptions) -> bool
        Set: ShowOnlyWebFonts(self: WebOptions) = value
        """
        ...



class WebPageOptions: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: WebPageOptions) -> Application """
        ...

    @property
    def BackgroundSound(self) -> str:
        """
        Get: BackgroundSound(self: WebPageOptions) -> str
        Set: BackgroundSound(self: WebPageOptions) = value
        """
        ...

    @property
    def BackgroundSoundLoopCount(self) -> int:
        """ Get: BackgroundSoundLoopCount(self: WebPageOptions) -> int """
        ...

    @property
    def BackgroundSoundLoopForever(self) -> bool:
        """ Get: BackgroundSoundLoopForever(self: WebPageOptions) -> bool """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: WebPageOptions) -> str
        Set: Description(self: WebPageOptions) = value
        """
        ...

    @property
    def IncludePageOnNewWebNavigationBars(self) -> bool:
        """
        Get: IncludePageOnNewWebNavigationBars(self: WebPageOptions) -> bool
        Set: IncludePageOnNewWebNavigationBars(self: WebPageOptions) = value
        """
        ...

    @property
    def Keywords(self) -> str:
        """
        Get: Keywords(self: WebPageOptions) -> str
        Set: Keywords(self: WebPageOptions) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WebPageOptions) -> object """
        ...

    @property
    def PublishFileName(self) -> str:
        """
        Get: PublishFileName(self: WebPageOptions) -> str
        Set: PublishFileName(self: WebPageOptions) = value
        """
        ...


    def SetBackgroundSoundRepeat(self, RepeatForever:bool, RepeatTimes:int): # -> 
        """ SetBackgroundSoundRepeat(self: WebPageOptions, RepeatForever: bool, RepeatTimes: int) """
        ...


class WebTextBox: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: WebTextBox) -> Application """
        ...

    @property
    def DefaultText(self) -> str:
        """
        Get: DefaultText(self: WebTextBox) -> str
        Set: DefaultText(self: WebTextBox) = value
        """
        ...

    @property
    def EchoAsterisks(self): # -> MsoTriState
        """
        Get: EchoAsterisks(self: WebTextBox) -> MsoTriState
        Set: EchoAsterisks(self: WebTextBox) = value
        """
        ...

    @property
    def Limit(self) -> int:
        """
        Get: Limit(self: WebTextBox) -> int
        Set: Limit(self: WebTextBox) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WebTextBox) -> object """
        ...

    @property
    def RequiredControl(self): # -> MsoTriState
        """
        Get: RequiredControl(self: WebTextBox) -> MsoTriState
        Set: RequiredControl(self: WebTextBox) = value
        """
        ...

    @property
    def ReturnDataLabel(self) -> str:
        """
        Get: ReturnDataLabel(self: WebTextBox) -> str
        Set: ReturnDataLabel(self: WebTextBox) = value
        """
        ...



class Window: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Window) -> Application """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: Window) -> str
        Set: Caption(self: Window) = value
        """
        ...

    @property
    def Height(self) -> int:
        """
        Get: Height(self: Window) -> int
        Set: Height(self: Window) = value
        """
        ...

    @property
    def Hwnd(self) -> int:
        """ Get: Hwnd(self: Window) -> int """
        ...

    @property
    def Left(self) -> int:
        """
        Get: Left(self: Window) -> int
        Set: Left(self: Window) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Window) -> object """
        ...

    @property
    def Top(self) -> int:
        """
        Get: Top(self: Window) -> int
        Set: Top(self: Window) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: Window) -> bool
        Set: Visible(self: Window) = value
        """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: Window) -> int
        Set: Width(self: Window) = value
        """
        ...

    @property
    def WindowState(self) -> PbWindowState:
        """
        Get: WindowState(self: Window) -> PbWindowState
        Set: WindowState(self: Window) = value
        """
        ...


    def Activate(self): # -> 
        """ Activate(self: Window) """
        ...

    def Move(self, Left:int, Top:int): # -> 
        """ Move(self: Window, Left: int, Top: int) """
        ...

    def Resize(self, Width:int, Height:int): # -> 
        """ Resize(self: Window, Width: int, Height: int) """
        ...


class Wizard: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Wizard) -> Application """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: Wizard) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Wizard) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Wizard) -> object """
        ...

    @property
    def Properties(self) -> WizardProperties:
        """ Get: Properties(self: Wizard) -> WizardProperties """
        ...


    def SetId(self, ID:int): # -> 
        """ SetId(self: Wizard, ID: int) """
        ...


class WizardProperties(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: WizardProperties) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: WizardProperties) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WizardProperties) -> object """
        ...


    def FindPropertyById(self, ID:int) -> WizardProperty:
        """ FindPropertyById(self: WizardProperties, ID: int) -> WizardProperty """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class WizardProperty: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: WizardProperty) -> Application """
        ...

    @property
    def CurrentValueId(self) -> int:
        """
        Get: CurrentValueId(self: WizardProperty) -> int
        Set: CurrentValueId(self: WizardProperty) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """ Get: Enabled(self: WizardProperty) -> bool """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: WizardProperty) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: WizardProperty) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WizardProperty) -> object """
        ...

    @property
    def Values(self) -> WizardValues:
        """ Get: Values(self: WizardProperty) -> WizardValues """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class WizardValue: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: WizardValue) -> Application """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: WizardValue) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: WizardValue) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WizardValue) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class WizardValues(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: WizardValues) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: WizardValues) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WizardValues) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class WrapFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: WrapFormat) -> Application """
        ...

    @property
    def DistanceAuto(self): # -> MsoTriState
        """
        Get: DistanceAuto(self: WrapFormat) -> MsoTriState
        Set: DistanceAuto(self: WrapFormat) = value
        """
        ...

    @property
    def DistanceBottom(self) -> object:
        """
        Get: DistanceBottom(self: WrapFormat) -> object
        Set: DistanceBottom(self: WrapFormat) = value
        """
        ...

    @property
    def DistanceLeft(self) -> object:
        """
        Get: DistanceLeft(self: WrapFormat) -> object
        Set: DistanceLeft(self: WrapFormat) = value
        """
        ...

    @property
    def DistanceRight(self) -> object:
        """
        Get: DistanceRight(self: WrapFormat) -> object
        Set: DistanceRight(self: WrapFormat) = value
        """
        ...

    @property
    def DistanceTop(self) -> object:
        """
        Get: DistanceTop(self: WrapFormat) -> object
        Set: DistanceTop(self: WrapFormat) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: WrapFormat) -> object """
        ...

    @property
    def Side(self) -> PbWrapSideType:
        """
        Get: Side(self: WrapFormat) -> PbWrapSideType
        Set: Side(self: WrapFormat) = value
        """
        ...

    @property
    def Type(self) -> PbWrapType:
        """
        Get: Type(self: WrapFormat) -> PbWrapType
        Set: Type(self: WrapFormat) = value
        """
        ...



