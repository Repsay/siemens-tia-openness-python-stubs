# encoding: utf-8
# module Microsoft.Office.Interop.PowerPoint calls itself PowerPoint
# from Microsoft.Office.Interop.PowerPoint, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Office.Interop.Graph import XlChartType

from Microsoft.Office.Interop.Publisher import (GlowFormat, ReflectionFormat, 
    SoftEdgeFormat)

from Microsoft.VisualStudio.CommandBars import CommandBars

from System import Array, DateTime, Enum, MulticastDelegate, Single, UInt32

from System.Collections import IEnumerable

from typing import Tuple as Tuple_

"""The following names are not found in the module: (AnswerWizard, Assistant, 
    BoundEvent, COMAddIns, Crop, CustomXMLPart, CustomXMLParts, 
    DocumentInspectors, DocumentLibraryVersions, FileSearch, GradientStops, 
    HTMLProject, IAssistance, IFind, LanguageSettings, MetaProperties, 
    MsoAlignCmd, MsoArrowheadLength, MsoArrowheadStyle, MsoArrowheadWidth, 
    MsoAutoShapeType, MsoAutoSize, MsoAutomationSecurity, 
    MsoBackgroundStyleIndex, MsoBevelType, MsoBlackWhiteMode, 
    MsoBroadcastState, MsoCalloutAngleType, MsoCalloutDropType, 
    MsoCalloutType, MsoChartElementType, MsoColorType, MsoConnectorType, 
    MsoDebugOptions, MsoDiagramNodeType, MsoDiagramType, MsoDistributeCmd, 
    MsoEditingType, MsoEncoding, MsoExtraInfoMethod, MsoExtrusionColorType, 
    MsoFarEastLineBreakLanguageID, MsoFeatureInstall, MsoFileValidationMode, 
    MsoFillType, MsoFlipCmd, MsoGradientColorType, MsoGradientStyle, 
    MsoHorizontalAnchor, MsoHyperlinkType, MsoLanguageID, MsoLightRigType, 
    MsoLineDashStyle, MsoLineStyle, MsoMergeCmd, MsoOrgChartLayoutType, 
    MsoOrientation, MsoPathFormat, MsoPatternType, MsoPictureColorType, 
    MsoPictureCompress, MsoPresetCamera, MsoPresetExtrusionDirection, 
    MsoPresetGradientType, MsoPresetLightingDirection, 
    MsoPresetLightingSoftness, MsoPresetMaterial, MsoPresetTextEffect, 
    MsoPresetTextEffectShape, MsoPresetTexture, MsoPresetThreeDFormat, 
    MsoRelativeNodePosition, MsoScaleFrom, MsoScreenSize, MsoSegmentType, 
    MsoShadowStyle, MsoShadowType, MsoShapeStyleIndex, MsoShapeType, 
    MsoSyncEventType, MsoTargetBrowser, MsoTextEffectAlignment, 
    MsoTextOrientation, MsoTextureAlignment, MsoTextureType, 
    MsoThemeColorIndex, MsoTriState, MsoVerticalAnchor, MsoWarpFormat, 
    MsoZOrderCmd, NewFile, OfficeTheme, Permission, PictureEffects, Ruler2, 
    Script, Scripts, ServerPolicy, SharedWorkspace, SignatureSet, SmartArt, 
    SmartArtColors, SmartArtLayout, SmartArtLayouts, SmartArtQuickStyles, 
    Sync, TextColumn2, TextRange2, ThemeColorScheme, VBE, VBProject, 
    WebPageFonts, WorkflowTasks, WorkflowTemplates, __ComObject, field#)
"""

# no functions
# classes

class ActionSetting: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Action(self) -> PpActionType:
        """
        Get: Action(self: ActionSetting) -> PpActionType
        Set: Action(self: ActionSetting) = value
        """
        ...

    @property
    def ActionVerb(self) -> str:
        """
        Get: ActionVerb(self: ActionSetting) -> str
        Set: ActionVerb(self: ActionSetting) = value
        """
        ...

    @property
    def AnimateAction(self): # -> MsoTriState
        """
        Get: AnimateAction(self: ActionSetting) -> MsoTriState
        Set: AnimateAction(self: ActionSetting) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: ActionSetting) -> Application """
        ...

    @property
    def Hyperlink(self) -> Hyperlink:
        """ Get: Hyperlink(self: ActionSetting) -> Hyperlink """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ActionSetting) -> object """
        ...

    @property
    def Run(self) -> str:
        """
        Get: Run(self: ActionSetting) -> str
        Set: Run(self: ActionSetting) = value
        """
        ...

    @property
    def ShowAndReturn(self): # -> MsoTriState
        """
        Get: ShowAndReturn(self: ActionSetting) -> MsoTriState
        Set: ShowAndReturn(self: ActionSetting) = value
        """
        ...

    @property
    def SlideShowName(self) -> str:
        """
        Get: SlideShowName(self: ActionSetting) -> str
        Set: SlideShowName(self: ActionSetting) = value
        """
        ...

    @property
    def SoundEffect(self) -> SoundEffect:
        """ Get: SoundEffect(self: ActionSetting) -> SoundEffect """
        ...



class Collection(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: Collection) -> int """
        ...


    def _Index(self, Index:int) -> object:
        """ _Index(self: Collection, Index: int) -> object """
        ...


class ActionSettings(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ActionSettings) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ActionSettings) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class AddIn: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: AddIn) -> Application """
        ...

    @property
    def AutoLoad(self): # -> MsoTriState
        """
        Get: AutoLoad(self: AddIn) -> MsoTriState
        Set: AutoLoad(self: AddIn) = value
        """
        ...

    @property
    def DisplayAlerts(self): # -> MsoTriState
        """
        Get: DisplayAlerts(self: AddIn) -> MsoTriState
        Set: DisplayAlerts(self: AddIn) = value
        """
        ...

    @property
    def FullName(self) -> str:
        """ Get: FullName(self: AddIn) -> str """
        ...

    @property
    def Loaded(self): # -> MsoTriState
        """
        Get: Loaded(self: AddIn) -> MsoTriState
        Set: Loaded(self: AddIn) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: AddIn) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: AddIn) -> object """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: AddIn) -> str """
        ...

    @property
    def Registered(self): # -> MsoTriState
        """
        Get: Registered(self: AddIn) -> MsoTriState
        Set: Registered(self: AddIn) = value
        """
        ...

    @property
    def RegisteredInHKLM(self): # -> MsoTriState
        """ Get: RegisteredInHKLM(self: AddIn) -> MsoTriState """
        ...



class AddIns(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: AddIns) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: AddIns) -> object """
        ...


    def Add(self, FileName:str) -> AddIn:
        """ Add(self: AddIns, FileName: str) -> AddIn """
        ...

    def Remove(self, Index:object) -> object:
        """ Remove(self: AddIns, Index: object) -> object """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Adjustments: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: Adjustments) -> object """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Adjustments) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Adjustments) -> int """
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


class AnimationBehavior: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Accumulate(self) -> MsoAnimAccumulate:
        """
        Get: Accumulate(self: AnimationBehavior) -> MsoAnimAccumulate
        Set: Accumulate(self: AnimationBehavior) = value
        """
        ...

    @property
    def Additive(self) -> MsoAnimAdditive:
        """
        Get: Additive(self: AnimationBehavior) -> MsoAnimAdditive
        Set: Additive(self: AnimationBehavior) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: AnimationBehavior) -> Application """
        ...

    @property
    def ColorEffect(self) -> ColorEffect:
        """ Get: ColorEffect(self: AnimationBehavior) -> ColorEffect """
        ...

    @property
    def CommandEffect(self) -> CommandEffect:
        """ Get: CommandEffect(self: AnimationBehavior) -> CommandEffect """
        ...

    @property
    def FilterEffect(self) -> FilterEffect:
        """ Get: FilterEffect(self: AnimationBehavior) -> FilterEffect """
        ...

    @property
    def MotionEffect(self) -> MotionEffect:
        """ Get: MotionEffect(self: AnimationBehavior) -> MotionEffect """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: AnimationBehavior) -> object """
        ...

    @property
    def PropertyEffect(self) -> PropertyEffect:
        """ Get: PropertyEffect(self: AnimationBehavior) -> PropertyEffect """
        ...

    @property
    def RotationEffect(self) -> RotationEffect:
        """ Get: RotationEffect(self: AnimationBehavior) -> RotationEffect """
        ...

    @property
    def ScaleEffect(self) -> ScaleEffect:
        """ Get: ScaleEffect(self: AnimationBehavior) -> ScaleEffect """
        ...

    @property
    def SetEffect(self) -> SetEffect:
        """ Get: SetEffect(self: AnimationBehavior) -> SetEffect """
        ...

    @property
    def Timing(self) -> Timing:
        """ Get: Timing(self: AnimationBehavior) -> Timing """
        ...

    @property
    def Type(self) -> MsoAnimType:
        """
        Get: Type(self: AnimationBehavior) -> MsoAnimType
        Set: Type(self: AnimationBehavior) = value
        """
        ...


    def Delete(self): # -> 
        """ Delete(self: AnimationBehavior) """
        ...


class AnimationBehaviors(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: AnimationBehaviors) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: AnimationBehaviors) -> object """
        ...


    def Add(self, Type:MsoAnimType, Index:int) -> AnimationBehavior:
        """ Add(self: AnimationBehaviors, Type: MsoAnimType, Index: int) -> AnimationBehavior """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class AnimationPoint: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: AnimationPoint) -> Application """
        ...

    @property
    def Formula(self) -> str:
        """
        Get: Formula(self: AnimationPoint) -> str
        Set: Formula(self: AnimationPoint) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: AnimationPoint) -> object """
        ...

    @property
    def Time(self) -> Single:
        """
        Get: Time(self: AnimationPoint) -> Single
        Set: Time(self: AnimationPoint) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: AnimationPoint) -> object
        Set: Value(self: AnimationPoint) = value
        """
        ...


    def Delete(self): # -> 
        """ Delete(self: AnimationPoint) """
        ...


class AnimationPoints(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: AnimationPoints) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: AnimationPoints) -> object """
        ...

    @property
    def Smooth(self): # -> MsoTriState
        """
        Get: Smooth(self: AnimationPoints) -> MsoTriState
        Set: Smooth(self: AnimationPoints) = value
        """
        ...


    def Add(self, Index:int) -> AnimationPoint:
        """ Add(self: AnimationPoints, Index: int) -> AnimationPoint """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class AnimationSettings: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AdvanceMode(self) -> PpAdvanceMode:
        """
        Get: AdvanceMode(self: AnimationSettings) -> PpAdvanceMode
        Set: AdvanceMode(self: AnimationSettings) = value
        """
        ...

    @property
    def AdvanceTime(self) -> Single:
        """
        Get: AdvanceTime(self: AnimationSettings) -> Single
        Set: AdvanceTime(self: AnimationSettings) = value
        """
        ...

    @property
    def AfterEffect(self) -> PpAfterEffect:
        """
        Get: AfterEffect(self: AnimationSettings) -> PpAfterEffect
        Set: AfterEffect(self: AnimationSettings) = value
        """
        ...

    @property
    def Animate(self): # -> MsoTriState
        """
        Get: Animate(self: AnimationSettings) -> MsoTriState
        Set: Animate(self: AnimationSettings) = value
        """
        ...

    @property
    def AnimateBackground(self): # -> MsoTriState
        """
        Get: AnimateBackground(self: AnimationSettings) -> MsoTriState
        Set: AnimateBackground(self: AnimationSettings) = value
        """
        ...

    @property
    def AnimateTextInReverse(self): # -> MsoTriState
        """
        Get: AnimateTextInReverse(self: AnimationSettings) -> MsoTriState
        Set: AnimateTextInReverse(self: AnimationSettings) = value
        """
        ...

    @property
    def AnimationOrder(self) -> int:
        """
        Get: AnimationOrder(self: AnimationSettings) -> int
        Set: AnimationOrder(self: AnimationSettings) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: AnimationSettings) -> Application """
        ...

    @property
    def ChartUnitEffect(self) -> PpChartUnitEffect:
        """
        Get: ChartUnitEffect(self: AnimationSettings) -> PpChartUnitEffect
        Set: ChartUnitEffect(self: AnimationSettings) = value
        """
        ...

    @property
    def DimColor(self) -> ColorFormat:
        """ Get: DimColor(self: AnimationSettings) -> ColorFormat """
        ...

    @property
    def EntryEffect(self) -> PpEntryEffect:
        """
        Get: EntryEffect(self: AnimationSettings) -> PpEntryEffect
        Set: EntryEffect(self: AnimationSettings) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: AnimationSettings) -> object """
        ...

    @property
    def PlaySettings(self) -> PlaySettings:
        """ Get: PlaySettings(self: AnimationSettings) -> PlaySettings """
        ...

    @property
    def SoundEffect(self) -> SoundEffect:
        """ Get: SoundEffect(self: AnimationSettings) -> SoundEffect """
        ...

    @property
    def TextLevelEffect(self) -> PpTextLevelEffect:
        """
        Get: TextLevelEffect(self: AnimationSettings) -> PpTextLevelEffect
        Set: TextLevelEffect(self: AnimationSettings) = value
        """
        ...

    @property
    def TextUnitEffect(self) -> PpTextUnitEffect:
        """
        Get: TextUnitEffect(self: AnimationSettings) -> PpTextUnitEffect
        Set: TextUnitEffect(self: AnimationSettings) = value
        """
        ...



class EApplication_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_AfterDragDropOnSlide(self): # -> 
        """ add_AfterDragDropOnSlide(self: EApplication_Event, : EApplication_AfterDragDropOnSlideEventHandler) """
        ...

    def add_AfterNewPresentation(self): # -> 
        """ add_AfterNewPresentation(self: EApplication_Event, : EApplication_AfterNewPresentationEventHandler) """
        ...

    def add_AfterPresentationOpen(self): # -> 
        """ add_AfterPresentationOpen(self: EApplication_Event, : EApplication_AfterPresentationOpenEventHandler) """
        ...

    def add_AfterShapeSizeChange(self): # -> 
        """ add_AfterShapeSizeChange(self: EApplication_Event, : EApplication_AfterShapeSizeChangeEventHandler) """
        ...

    def add_ColorSchemeChanged(self): # -> 
        """ add_ColorSchemeChanged(self: EApplication_Event, : EApplication_ColorSchemeChangedEventHandler) """
        ...

    def add_NewPresentation(self): # -> 
        """ add_NewPresentation(self: EApplication_Event, : EApplication_NewPresentationEventHandler) """
        ...

    def add_PresentationBeforeClose(self): # -> 
        """ add_PresentationBeforeClose(self: EApplication_Event, : EApplication_PresentationBeforeCloseEventHandler) """
        ...

    def add_PresentationBeforeSave(self): # -> 
        """ add_PresentationBeforeSave(self: EApplication_Event, : EApplication_PresentationBeforeSaveEventHandler) """
        ...

    def add_PresentationClose(self): # -> 
        """ add_PresentationClose(self: EApplication_Event, : EApplication_PresentationCloseEventHandler) """
        ...

    def add_PresentationCloseFinal(self): # -> 
        """ add_PresentationCloseFinal(self: EApplication_Event, : EApplication_PresentationCloseFinalEventHandler) """
        ...

    def add_PresentationNewSlide(self): # -> 
        """ add_PresentationNewSlide(self: EApplication_Event, : EApplication_PresentationNewSlideEventHandler) """
        ...

    def add_PresentationOpen(self): # -> 
        """ add_PresentationOpen(self: EApplication_Event, : EApplication_PresentationOpenEventHandler) """
        ...

    def add_PresentationPrint(self): # -> 
        """ add_PresentationPrint(self: EApplication_Event, : EApplication_PresentationPrintEventHandler) """
        ...

    def add_PresentationSave(self): # -> 
        """ add_PresentationSave(self: EApplication_Event, : EApplication_PresentationSaveEventHandler) """
        ...

    def add_PresentationSync(self): # -> 
        """ add_PresentationSync(self: EApplication_Event, : EApplication_PresentationSyncEventHandler) """
        ...

    def add_ProtectedViewWindowActivate(self): # -> 
        """ add_ProtectedViewWindowActivate(self: EApplication_Event, : EApplication_ProtectedViewWindowActivateEventHandler) """
        ...

    def add_ProtectedViewWindowBeforeClose(self): # -> 
        """ add_ProtectedViewWindowBeforeClose(self: EApplication_Event, : EApplication_ProtectedViewWindowBeforeCloseEventHandler) """
        ...

    def add_ProtectedViewWindowBeforeEdit(self): # -> 
        """ add_ProtectedViewWindowBeforeEdit(self: EApplication_Event, : EApplication_ProtectedViewWindowBeforeEditEventHandler) """
        ...

    def add_ProtectedViewWindowDeactivate(self): # -> 
        """ add_ProtectedViewWindowDeactivate(self: EApplication_Event, : EApplication_ProtectedViewWindowDeactivateEventHandler) """
        ...

    def add_ProtectedViewWindowOpen(self): # -> 
        """ add_ProtectedViewWindowOpen(self: EApplication_Event, : EApplication_ProtectedViewWindowOpenEventHandler) """
        ...

    def add_SlideSelectionChanged(self): # -> 
        """ add_SlideSelectionChanged(self: EApplication_Event, : EApplication_SlideSelectionChangedEventHandler) """
        ...

    def add_SlideShowBegin(self): # -> 
        """ add_SlideShowBegin(self: EApplication_Event, : EApplication_SlideShowBeginEventHandler) """
        ...

    def add_SlideShowEnd(self): # -> 
        """ add_SlideShowEnd(self: EApplication_Event, : EApplication_SlideShowEndEventHandler) """
        ...

    def add_SlideShowNextBuild(self): # -> 
        """ add_SlideShowNextBuild(self: EApplication_Event, : EApplication_SlideShowNextBuildEventHandler) """
        ...

    def add_SlideShowNextClick(self): # -> 
        """ add_SlideShowNextClick(self: EApplication_Event, : EApplication_SlideShowNextClickEventHandler) """
        ...

    def add_SlideShowNextSlide(self): # -> 
        """ add_SlideShowNextSlide(self: EApplication_Event, : EApplication_SlideShowNextSlideEventHandler) """
        ...

    def add_SlideShowOnNext(self): # -> 
        """ add_SlideShowOnNext(self: EApplication_Event, : EApplication_SlideShowOnNextEventHandler) """
        ...

    def add_SlideShowOnPrevious(self): # -> 
        """ add_SlideShowOnPrevious(self: EApplication_Event, : EApplication_SlideShowOnPreviousEventHandler) """
        ...

    def add_WindowActivate(self): # -> 
        """ add_WindowActivate(self: EApplication_Event, : EApplication_WindowActivateEventHandler) """
        ...

    def add_WindowBeforeDoubleClick(self): # -> 
        """ add_WindowBeforeDoubleClick(self: EApplication_Event, : EApplication_WindowBeforeDoubleClickEventHandler) """
        ...

    def add_WindowBeforeRightClick(self): # -> 
        """ add_WindowBeforeRightClick(self: EApplication_Event, : EApplication_WindowBeforeRightClickEventHandler) """
        ...

    def add_WindowDeactivate(self): # -> 
        """ add_WindowDeactivate(self: EApplication_Event, : EApplication_WindowDeactivateEventHandler) """
        ...

    def add_WindowSelectionChange(self): # -> 
        """ add_WindowSelectionChange(self: EApplication_Event, : EApplication_WindowSelectionChangeEventHandler) """
        ...

    def remove_AfterDragDropOnSlide(self): # -> 
        """ remove_AfterDragDropOnSlide(self: EApplication_Event, : EApplication_AfterDragDropOnSlideEventHandler) """
        ...

    def remove_AfterNewPresentation(self): # -> 
        """ remove_AfterNewPresentation(self: EApplication_Event, : EApplication_AfterNewPresentationEventHandler) """
        ...

    def remove_AfterPresentationOpen(self): # -> 
        """ remove_AfterPresentationOpen(self: EApplication_Event, : EApplication_AfterPresentationOpenEventHandler) """
        ...

    def remove_AfterShapeSizeChange(self): # -> 
        """ remove_AfterShapeSizeChange(self: EApplication_Event, : EApplication_AfterShapeSizeChangeEventHandler) """
        ...

    def remove_ColorSchemeChanged(self): # -> 
        """ remove_ColorSchemeChanged(self: EApplication_Event, : EApplication_ColorSchemeChangedEventHandler) """
        ...

    def remove_NewPresentation(self): # -> 
        """ remove_NewPresentation(self: EApplication_Event, : EApplication_NewPresentationEventHandler) """
        ...

    def remove_PresentationBeforeClose(self): # -> 
        """ remove_PresentationBeforeClose(self: EApplication_Event, : EApplication_PresentationBeforeCloseEventHandler) """
        ...

    def remove_PresentationBeforeSave(self): # -> 
        """ remove_PresentationBeforeSave(self: EApplication_Event, : EApplication_PresentationBeforeSaveEventHandler) """
        ...

    def remove_PresentationClose(self): # -> 
        """ remove_PresentationClose(self: EApplication_Event, : EApplication_PresentationCloseEventHandler) """
        ...

    def remove_PresentationCloseFinal(self): # -> 
        """ remove_PresentationCloseFinal(self: EApplication_Event, : EApplication_PresentationCloseFinalEventHandler) """
        ...

    def remove_PresentationNewSlide(self): # -> 
        """ remove_PresentationNewSlide(self: EApplication_Event, : EApplication_PresentationNewSlideEventHandler) """
        ...

    def remove_PresentationOpen(self): # -> 
        """ remove_PresentationOpen(self: EApplication_Event, : EApplication_PresentationOpenEventHandler) """
        ...

    def remove_PresentationPrint(self): # -> 
        """ remove_PresentationPrint(self: EApplication_Event, : EApplication_PresentationPrintEventHandler) """
        ...

    def remove_PresentationSave(self): # -> 
        """ remove_PresentationSave(self: EApplication_Event, : EApplication_PresentationSaveEventHandler) """
        ...

    def remove_PresentationSync(self): # -> 
        """ remove_PresentationSync(self: EApplication_Event, : EApplication_PresentationSyncEventHandler) """
        ...

    def remove_ProtectedViewWindowActivate(self): # -> 
        """ remove_ProtectedViewWindowActivate(self: EApplication_Event, : EApplication_ProtectedViewWindowActivateEventHandler) """
        ...

    def remove_ProtectedViewWindowBeforeClose(self): # -> 
        """ remove_ProtectedViewWindowBeforeClose(self: EApplication_Event, : EApplication_ProtectedViewWindowBeforeCloseEventHandler) """
        ...

    def remove_ProtectedViewWindowBeforeEdit(self): # -> 
        """ remove_ProtectedViewWindowBeforeEdit(self: EApplication_Event, : EApplication_ProtectedViewWindowBeforeEditEventHandler) """
        ...

    def remove_ProtectedViewWindowDeactivate(self): # -> 
        """ remove_ProtectedViewWindowDeactivate(self: EApplication_Event, : EApplication_ProtectedViewWindowDeactivateEventHandler) """
        ...

    def remove_ProtectedViewWindowOpen(self): # -> 
        """ remove_ProtectedViewWindowOpen(self: EApplication_Event, : EApplication_ProtectedViewWindowOpenEventHandler) """
        ...

    def remove_SlideSelectionChanged(self): # -> 
        """ remove_SlideSelectionChanged(self: EApplication_Event, : EApplication_SlideSelectionChangedEventHandler) """
        ...

    def remove_SlideShowBegin(self): # -> 
        """ remove_SlideShowBegin(self: EApplication_Event, : EApplication_SlideShowBeginEventHandler) """
        ...

    def remove_SlideShowEnd(self): # -> 
        """ remove_SlideShowEnd(self: EApplication_Event, : EApplication_SlideShowEndEventHandler) """
        ...

    def remove_SlideShowNextBuild(self): # -> 
        """ remove_SlideShowNextBuild(self: EApplication_Event, : EApplication_SlideShowNextBuildEventHandler) """
        ...

    def remove_SlideShowNextClick(self): # -> 
        """ remove_SlideShowNextClick(self: EApplication_Event, : EApplication_SlideShowNextClickEventHandler) """
        ...

    def remove_SlideShowNextSlide(self): # -> 
        """ remove_SlideShowNextSlide(self: EApplication_Event, : EApplication_SlideShowNextSlideEventHandler) """
        ...

    def remove_SlideShowOnNext(self): # -> 
        """ remove_SlideShowOnNext(self: EApplication_Event, : EApplication_SlideShowOnNextEventHandler) """
        ...

    def remove_SlideShowOnPrevious(self): # -> 
        """ remove_SlideShowOnPrevious(self: EApplication_Event, : EApplication_SlideShowOnPreviousEventHandler) """
        ...

    def remove_WindowActivate(self): # -> 
        """ remove_WindowActivate(self: EApplication_Event, : EApplication_WindowActivateEventHandler) """
        ...

    def remove_WindowBeforeDoubleClick(self): # -> 
        """ remove_WindowBeforeDoubleClick(self: EApplication_Event, : EApplication_WindowBeforeDoubleClickEventHandler) """
        ...

    def remove_WindowBeforeRightClick(self): # -> 
        """ remove_WindowBeforeRightClick(self: EApplication_Event, : EApplication_WindowBeforeRightClickEventHandler) """
        ...

    def remove_WindowDeactivate(self): # -> 
        """ remove_WindowDeactivate(self: EApplication_Event, : EApplication_WindowDeactivateEventHandler) """
        ...

    def remove_WindowSelectionChange(self): # -> 
        """ remove_WindowSelectionChange(self: EApplication_Event, : EApplication_WindowSelectionChangeEventHandler) """
        ...

    AfterDragDropOnSlide = ...
    AfterNewPresentation = ...
    AfterPresentationOpen = ...
    AfterShapeSizeChange = ...
    ColorSchemeChanged = ...
    NewPresentation = ...
    PresentationBeforeClose = ...
    PresentationBeforeSave = ...
    PresentationClose = ...
    PresentationCloseFinal = ...
    PresentationNewSlide = ...
    PresentationOpen = ...
    PresentationPrint = ...
    PresentationSave = ...
    PresentationSync = ...
    ProtectedViewWindowActivate = ...
    ProtectedViewWindowBeforeClose = ...
    ProtectedViewWindowBeforeEdit = ...
    ProtectedViewWindowDeactivate = ...
    ProtectedViewWindowOpen = ...
    SlideSelectionChanged = ...
    SlideShowBegin = ...
    SlideShowEnd = ...
    SlideShowNextBuild = ...
    SlideShowNextClick = ...
    SlideShowNextSlide = ...
    SlideShowOnNext = ...
    SlideShowOnPrevious = ...
    WindowActivate = ...
    WindowBeforeDoubleClick = ...
    WindowBeforeRightClick = ...
    WindowDeactivate = ...
    WindowSelectionChange = ...


class _Application: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Active(self): # -> MsoTriState
        """ Get: Active(self: _Application) -> MsoTriState """
        ...

    @property
    def ActiveEncryptionSession(self) -> int:
        """ Get: ActiveEncryptionSession(self: _Application) -> int """
        ...

    @property
    def ActivePresentation(self) -> Presentation:
        """ Get: ActivePresentation(self: _Application) -> Presentation """
        ...

    @property
    def ActivePrinter(self) -> str:
        """ Get: ActivePrinter(self: _Application) -> str """
        ...

    @property
    def ActiveProtectedViewWindow(self) -> ProtectedViewWindow:
        """ Get: ActiveProtectedViewWindow(self: _Application) -> ProtectedViewWindow """
        ...

    @property
    def ActiveWindow(self) -> DocumentWindow:
        """ Get: ActiveWindow(self: _Application) -> DocumentWindow """
        ...

    @property
    def AddIns(self) -> AddIns:
        """ Get: AddIns(self: _Application) -> AddIns """
        ...

    @property
    def AnswerWizard(self): # -> AnswerWizard
        """ Get: AnswerWizard(self: _Application) -> AnswerWizard """
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
    def AutoCorrect(self) -> AutoCorrect:
        """ Get: AutoCorrect(self: _Application) -> AutoCorrect """
        ...

    @property
    def AutomationSecurity(self): # -> MsoAutomationSecurity
        """
        Get: AutomationSecurity(self: _Application) -> MsoAutomationSecurity
        Set: AutomationSecurity(self: _Application) = value
        """
        ...

    @property
    def Build(self) -> str:
        """ Get: Build(self: _Application) -> str """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: _Application) -> str
        Set: Caption(self: _Application) = value
        """
        ...

    @property
    def ChartDataPointTrack(self) -> bool:
        """
        Get: ChartDataPointTrack(self: _Application) -> bool
        Set: ChartDataPointTrack(self: _Application) = value
        """
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
    def Creator(self) -> int:
        """ Get: Creator(self: _Application) -> int """
        ...

    @property
    def DefaultWebOptions(self) -> DefaultWebOptions:
        """ Get: DefaultWebOptions(self: _Application) -> DefaultWebOptions """
        ...

    @property
    def Dialogs(self) -> object:
        """ Get: Dialogs(self: _Application) -> object """
        ...

    @property
    def DisplayAlerts(self) -> PpAlertLevel:
        """
        Get: DisplayAlerts(self: _Application) -> PpAlertLevel
        Set: DisplayAlerts(self: _Application) = value
        """
        ...

    @property
    def DisplayDocumentInformationPanel(self) -> bool:
        """
        Get: DisplayDocumentInformationPanel(self: _Application) -> bool
        Set: DisplayDocumentInformationPanel(self: _Application) = value
        """
        ...

    @property
    def DisplayGridLines(self): # -> MsoTriState
        """
        Get: DisplayGridLines(self: _Application) -> MsoTriState
        Set: DisplayGridLines(self: _Application) = value
        """
        ...

    @property
    def DisplayGuides(self): # -> MsoTriState
        """
        Get: DisplayGuides(self: _Application) -> MsoTriState
        Set: DisplayGuides(self: _Application) = value
        """
        ...

    @property
    def FeatureInstall(self): # -> MsoFeatureInstall
        """
        Get: FeatureInstall(self: _Application) -> MsoFeatureInstall
        Set: FeatureInstall(self: _Application) = value
        """
        ...

    @property
    def FileConverters(self) -> FileConverters:
        """ Get: FileConverters(self: _Application) -> FileConverters """
        ...

    @property
    def FileFind(self): # -> IFind
        """ Get: FileFind(self: _Application) -> IFind """
        ...

    @property
    def FileSearch(self): # -> FileSearch
        """ Get: FileSearch(self: _Application) -> FileSearch """
        ...

    @property
    def FileValidation(self): # -> MsoFileValidationMode
        """
        Get: FileValidation(self: _Application) -> MsoFileValidationMode
        Set: FileValidation(self: _Application) = value
        """
        ...

    @property
    def Height(self) -> Single:
        """
        Get: Height(self: _Application) -> Single
        Set: Height(self: _Application) = value
        """
        ...

    @property
    def HWND(self) -> int:
        """ Get: HWND(self: _Application) -> int """
        ...

    @property
    def IsSandboxed(self) -> bool:
        """ Get: IsSandboxed(self: _Application) -> bool """
        ...

    @property
    def LanguageSettings(self): # -> LanguageSettings
        """ Get: LanguageSettings(self: _Application) -> LanguageSettings """
        ...

    @property
    def Left(self) -> Single:
        """
        Get: Left(self: _Application) -> Single
        Set: Left(self: _Application) = value
        """
        ...

    @property
    def Marker(self) -> object:
        """ Get: Marker(self: _Application) -> object """
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
    def NewPresentation(self): # -> NewFile
        """ Get: NewPresentation(self: _Application) -> NewFile """
        ...

    @property
    def OperatingSystem(self) -> str:
        """ Get: OperatingSystem(self: _Application) -> str """
        ...

    @property
    def Options(self) -> Options:
        """ Get: Options(self: _Application) -> Options """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: _Application) -> str """
        ...

    @property
    def Presentations(self) -> Presentations:
        """ Get: Presentations(self: _Application) -> Presentations """
        ...

    @property
    def ProductCode(self) -> str:
        """ Get: ProductCode(self: _Application) -> str """
        ...

    @property
    def ProtectedViewWindows(self) -> ProtectedViewWindows:
        """ Get: ProtectedViewWindows(self: _Application) -> ProtectedViewWindows """
        ...

    @property
    def ResampleMediaTasks(self) -> ResampleMediaTasks:
        """ Get: ResampleMediaTasks(self: _Application) -> ResampleMediaTasks """
        ...

    @property
    def ShowStartupDialog(self): # -> MsoTriState
        """
        Get: ShowStartupDialog(self: _Application) -> MsoTriState
        Set: ShowStartupDialog(self: _Application) = value
        """
        ...

    @property
    def ShowWindowsInTaskbar(self): # -> MsoTriState
        """
        Get: ShowWindowsInTaskbar(self: _Application) -> MsoTriState
        Set: ShowWindowsInTaskbar(self: _Application) = value
        """
        ...

    @property
    def SlideShowWindows(self) -> SlideShowWindows:
        """ Get: SlideShowWindows(self: _Application) -> SlideShowWindows """
        ...

    @property
    def SmartArtColors(self): # -> SmartArtColors
        """ Get: SmartArtColors(self: _Application) -> SmartArtColors """
        ...

    @property
    def SmartArtLayouts(self): # -> SmartArtLayouts
        """ Get: SmartArtLayouts(self: _Application) -> SmartArtLayouts """
        ...

    @property
    def SmartArtQuickStyles(self): # -> SmartArtQuickStyles
        """ Get: SmartArtQuickStyles(self: _Application) -> SmartArtQuickStyles """
        ...

    @property
    def Top(self) -> Single:
        """
        Get: Top(self: _Application) -> Single
        Set: Top(self: _Application) = value
        """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: _Application) -> VBE """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: _Application) -> str """
        ...

    @property
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: _Application) -> MsoTriState
        Set: Visible(self: _Application) = value
        """
        ...

    @property
    def Width(self) -> Single:
        """
        Get: Width(self: _Application) -> Single
        Set: Width(self: _Application) = value
        """
        ...

    @property
    def Windows(self) -> DocumentWindows:
        """ Get: Windows(self: _Application) -> DocumentWindows """
        ...

    @property
    def WindowState(self) -> PpWindowState:
        """
        Get: WindowState(self: _Application) -> PpWindowState
        Set: WindowState(self: _Application) = value
        """
        ...


    def Activate(self): # -> 
        """ Activate(self: _Application) """
        ...

    def GetOptionFlag(self, Option:int, Persist:bool) -> bool:
        """ GetOptionFlag(self: _Application, Option: int, Persist: bool) -> bool """
        ...

    def Help(self, HelpFile:str, ContextID:int): # -> 
        """ Help(self: _Application, HelpFile: str, ContextID: int) """
        ...

    def LaunchPublishSlidesDialog(self, SlideLibraryUrl:str): # -> 
        """ LaunchPublishSlidesDialog(self: _Application, SlideLibraryUrl: str) """
        ...

    def LaunchSendToPPTDialog(self, SlideUrls:object) -> object:
        """ LaunchSendToPPTDialog(self: _Application, SlideUrls: object) -> object """
        ...

    def LaunchSpelling(self, pWindow:DocumentWindow): # -> 
        """ LaunchSpelling(self: _Application, pWindow: DocumentWindow) """
        ...

    def OpenThemeFile(self, themeFileName:str) -> Theme:
        """ OpenThemeFile(self: _Application, themeFileName: str) -> Theme """
        ...

    def PPFileDialog(self, Type:PpFileDialogType) -> object:
        """ PPFileDialog(self: _Application, Type: PpFileDialogType) -> object """
        ...

    def Quit(self): # -> 
        """ Quit(self: _Application) """
        ...

    def Run(self, MacroName:str, safeArrayOfParams:Array) -> Tuple_[object, Array]:
        """ Run(self: _Application, MacroName: str, *safeArrayOfParams: Array[object]) -> (object, Array[object]) """
        ...

    def SetOptionFlag(self, Option:int, State:bool, Persist:bool): # -> 
        """ SetOptionFlag(self: _Application, Option: int, State: bool, Persist: bool) """
        ...

    def SetPerfMarker(self, Marker:int): # -> 
        """ SetPerfMarker(self: _Application, Marker: int) """
        ...

    def StartNewUndoEntry(self): # -> 
        """ StartNewUndoEntry(self: _Application) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Application(_Application, EApplication_Event): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ApplicationClass(Application, __ComObject): # skipped bases: <type '_Application'>, <type 'EApplication_Event'>, <type 'object'>
    """ ApplicationClass() """
    @property
    def Active(self): # -> MsoTriState
        """ Get: Active(self: ApplicationClass) -> MsoTriState """
        ...

    @property
    def ActiveEncryptionSession(self) -> int:
        """ Get: ActiveEncryptionSession(self: ApplicationClass) -> int """
        ...

    @property
    def ActivePresentation(self) -> Presentation:
        """ Get: ActivePresentation(self: ApplicationClass) -> Presentation """
        ...

    @property
    def ActivePrinter(self) -> str:
        """ Get: ActivePrinter(self: ApplicationClass) -> str """
        ...

    @property
    def ActiveProtectedViewWindow(self) -> ProtectedViewWindow:
        """ Get: ActiveProtectedViewWindow(self: ApplicationClass) -> ProtectedViewWindow """
        ...

    @property
    def ActiveWindow(self) -> DocumentWindow:
        """ Get: ActiveWindow(self: ApplicationClass) -> DocumentWindow """
        ...

    @property
    def AddIns(self) -> AddIns:
        """ Get: AddIns(self: ApplicationClass) -> AddIns """
        ...

    @property
    def AnswerWizard(self): # -> AnswerWizard
        """ Get: AnswerWizard(self: ApplicationClass) -> AnswerWizard """
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
    def AutoCorrect(self) -> AutoCorrect:
        """ Get: AutoCorrect(self: ApplicationClass) -> AutoCorrect """
        ...

    @property
    def AutomationSecurity(self): # -> MsoAutomationSecurity
        """
        Get: AutomationSecurity(self: ApplicationClass) -> MsoAutomationSecurity
        Set: AutomationSecurity(self: ApplicationClass) = value
        """
        ...

    @property
    def Build(self) -> str:
        """ Get: Build(self: ApplicationClass) -> str """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: ApplicationClass) -> str
        Set: Caption(self: ApplicationClass) = value
        """
        ...

    @property
    def ChartDataPointTrack(self) -> bool:
        """
        Get: ChartDataPointTrack(self: ApplicationClass) -> bool
        Set: ChartDataPointTrack(self: ApplicationClass) = value
        """
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
    def Creator(self) -> int:
        """ Get: Creator(self: ApplicationClass) -> int """
        ...

    @property
    def DefaultWebOptions(self) -> DefaultWebOptions:
        """ Get: DefaultWebOptions(self: ApplicationClass) -> DefaultWebOptions """
        ...

    @property
    def Dialogs(self) -> object:
        """ Get: Dialogs(self: ApplicationClass) -> object """
        ...

    @property
    def DisplayAlerts(self) -> PpAlertLevel:
        """
        Get: DisplayAlerts(self: ApplicationClass) -> PpAlertLevel
        Set: DisplayAlerts(self: ApplicationClass) = value
        """
        ...

    @property
    def DisplayDocumentInformationPanel(self) -> bool:
        """
        Get: DisplayDocumentInformationPanel(self: ApplicationClass) -> bool
        Set: DisplayDocumentInformationPanel(self: ApplicationClass) = value
        """
        ...

    @property
    def DisplayGridLines(self): # -> MsoTriState
        """
        Get: DisplayGridLines(self: ApplicationClass) -> MsoTriState
        Set: DisplayGridLines(self: ApplicationClass) = value
        """
        ...

    @property
    def DisplayGuides(self): # -> MsoTriState
        """
        Get: DisplayGuides(self: ApplicationClass) -> MsoTriState
        Set: DisplayGuides(self: ApplicationClass) = value
        """
        ...

    @property
    def FeatureInstall(self): # -> MsoFeatureInstall
        """
        Get: FeatureInstall(self: ApplicationClass) -> MsoFeatureInstall
        Set: FeatureInstall(self: ApplicationClass) = value
        """
        ...

    @property
    def FileConverters(self) -> FileConverters:
        """ Get: FileConverters(self: ApplicationClass) -> FileConverters """
        ...

    @property
    def FileFind(self): # -> IFind
        """ Get: FileFind(self: ApplicationClass) -> IFind """
        ...

    @property
    def FileSearch(self): # -> FileSearch
        """ Get: FileSearch(self: ApplicationClass) -> FileSearch """
        ...

    @property
    def FileValidation(self): # -> MsoFileValidationMode
        """
        Get: FileValidation(self: ApplicationClass) -> MsoFileValidationMode
        Set: FileValidation(self: ApplicationClass) = value
        """
        ...

    @property
    def Height(self) -> Single:
        """
        Get: Height(self: ApplicationClass) -> Single
        Set: Height(self: ApplicationClass) = value
        """
        ...

    @property
    def HWND(self) -> int:
        """ Get: HWND(self: ApplicationClass) -> int """
        ...

    @property
    def IsSandboxed(self) -> bool:
        """ Get: IsSandboxed(self: ApplicationClass) -> bool """
        ...

    @property
    def LanguageSettings(self): # -> LanguageSettings
        """ Get: LanguageSettings(self: ApplicationClass) -> LanguageSettings """
        ...

    @property
    def Left(self) -> Single:
        """
        Get: Left(self: ApplicationClass) -> Single
        Set: Left(self: ApplicationClass) = value
        """
        ...

    @property
    def Marker(self) -> object:
        """ Get: Marker(self: ApplicationClass) -> object """
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
    def NewPresentation(self): # -> NewFile
        """ Get: NewPresentation(self: ApplicationClass) -> NewFile """
        ...

    @property
    def OperatingSystem(self) -> str:
        """ Get: OperatingSystem(self: ApplicationClass) -> str """
        ...

    @property
    def Options(self) -> Options:
        """ Get: Options(self: ApplicationClass) -> Options """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: ApplicationClass) -> str """
        ...

    @property
    def Presentations(self) -> Presentations:
        """ Get: Presentations(self: ApplicationClass) -> Presentations """
        ...

    @property
    def ProductCode(self) -> str:
        """ Get: ProductCode(self: ApplicationClass) -> str """
        ...

    @property
    def ProtectedViewWindows(self) -> ProtectedViewWindows:
        """ Get: ProtectedViewWindows(self: ApplicationClass) -> ProtectedViewWindows """
        ...

    @property
    def ResampleMediaTasks(self) -> ResampleMediaTasks:
        """ Get: ResampleMediaTasks(self: ApplicationClass) -> ResampleMediaTasks """
        ...

    @property
    def ShowStartupDialog(self): # -> MsoTriState
        """
        Get: ShowStartupDialog(self: ApplicationClass) -> MsoTriState
        Set: ShowStartupDialog(self: ApplicationClass) = value
        """
        ...

    @property
    def ShowWindowsInTaskbar(self): # -> MsoTriState
        """
        Get: ShowWindowsInTaskbar(self: ApplicationClass) -> MsoTriState
        Set: ShowWindowsInTaskbar(self: ApplicationClass) = value
        """
        ...

    @property
    def SlideShowWindows(self) -> SlideShowWindows:
        """ Get: SlideShowWindows(self: ApplicationClass) -> SlideShowWindows """
        ...

    @property
    def SmartArtColors(self): # -> SmartArtColors
        """ Get: SmartArtColors(self: ApplicationClass) -> SmartArtColors """
        ...

    @property
    def SmartArtLayouts(self): # -> SmartArtLayouts
        """ Get: SmartArtLayouts(self: ApplicationClass) -> SmartArtLayouts """
        ...

    @property
    def SmartArtQuickStyles(self): # -> SmartArtQuickStyles
        """ Get: SmartArtQuickStyles(self: ApplicationClass) -> SmartArtQuickStyles """
        ...

    @property
    def Top(self) -> Single:
        """
        Get: Top(self: ApplicationClass) -> Single
        Set: Top(self: ApplicationClass) = value
        """
        ...

    @property
    def VBE(self): # -> VBE
        """ Get: VBE(self: ApplicationClass) -> VBE """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: ApplicationClass) -> str """
        ...

    @property
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: ApplicationClass) -> MsoTriState
        Set: Visible(self: ApplicationClass) = value
        """
        ...

    @property
    def Width(self) -> Single:
        """
        Get: Width(self: ApplicationClass) -> Single
        Set: Width(self: ApplicationClass) = value
        """
        ...

    @property
    def Windows(self) -> DocumentWindows:
        """ Get: Windows(self: ApplicationClass) -> DocumentWindows """
        ...

    @property
    def WindowState(self) -> PpWindowState:
        """
        Get: WindowState(self: ApplicationClass) -> PpWindowState
        Set: WindowState(self: ApplicationClass) = value
        """
        ...


    def Activate(self): # -> 
        """ Activate(self: ApplicationClass) """
        ...

    def add_AfterDragDropOnSlide(self): # -> 
        """ add_AfterDragDropOnSlide(self: ApplicationClass, : EApplication_AfterDragDropOnSlideEventHandler) """
        ...

    def add_AfterNewPresentation(self): # -> 
        """ add_AfterNewPresentation(self: ApplicationClass, : EApplication_AfterNewPresentationEventHandler) """
        ...

    def add_AfterPresentationOpen(self): # -> 
        """ add_AfterPresentationOpen(self: ApplicationClass, : EApplication_AfterPresentationOpenEventHandler) """
        ...

    def add_AfterShapeSizeChange(self): # -> 
        """ add_AfterShapeSizeChange(self: ApplicationClass, : EApplication_AfterShapeSizeChangeEventHandler) """
        ...

    def add_ColorSchemeChanged(self): # -> 
        """ add_ColorSchemeChanged(self: ApplicationClass, : EApplication_ColorSchemeChangedEventHandler) """
        ...

    def add_NewPresentation(self): # -> 
        """ add_NewPresentation(self: ApplicationClass, : EApplication_NewPresentationEventHandler) """
        ...

    def add_PresentationBeforeClose(self): # -> 
        """ add_PresentationBeforeClose(self: ApplicationClass, : EApplication_PresentationBeforeCloseEventHandler) """
        ...

    def add_PresentationBeforeSave(self): # -> 
        """ add_PresentationBeforeSave(self: ApplicationClass, : EApplication_PresentationBeforeSaveEventHandler) """
        ...

    def add_PresentationClose(self): # -> 
        """ add_PresentationClose(self: ApplicationClass, : EApplication_PresentationCloseEventHandler) """
        ...

    def add_PresentationCloseFinal(self): # -> 
        """ add_PresentationCloseFinal(self: ApplicationClass, : EApplication_PresentationCloseFinalEventHandler) """
        ...

    def add_PresentationNewSlide(self): # -> 
        """ add_PresentationNewSlide(self: ApplicationClass, : EApplication_PresentationNewSlideEventHandler) """
        ...

    def add_PresentationOpen(self): # -> 
        """ add_PresentationOpen(self: ApplicationClass, : EApplication_PresentationOpenEventHandler) """
        ...

    def add_PresentationPrint(self): # -> 
        """ add_PresentationPrint(self: ApplicationClass, : EApplication_PresentationPrintEventHandler) """
        ...

    def add_PresentationSave(self): # -> 
        """ add_PresentationSave(self: ApplicationClass, : EApplication_PresentationSaveEventHandler) """
        ...

    def add_PresentationSync(self): # -> 
        """ add_PresentationSync(self: ApplicationClass, : EApplication_PresentationSyncEventHandler) """
        ...

    def add_ProtectedViewWindowActivate(self): # -> 
        """ add_ProtectedViewWindowActivate(self: ApplicationClass, : EApplication_ProtectedViewWindowActivateEventHandler) """
        ...

    def add_ProtectedViewWindowBeforeClose(self): # -> 
        """ add_ProtectedViewWindowBeforeClose(self: ApplicationClass, : EApplication_ProtectedViewWindowBeforeCloseEventHandler) """
        ...

    def add_ProtectedViewWindowBeforeEdit(self): # -> 
        """ add_ProtectedViewWindowBeforeEdit(self: ApplicationClass, : EApplication_ProtectedViewWindowBeforeEditEventHandler) """
        ...

    def add_ProtectedViewWindowDeactivate(self): # -> 
        """ add_ProtectedViewWindowDeactivate(self: ApplicationClass, : EApplication_ProtectedViewWindowDeactivateEventHandler) """
        ...

    def add_ProtectedViewWindowOpen(self): # -> 
        """ add_ProtectedViewWindowOpen(self: ApplicationClass, : EApplication_ProtectedViewWindowOpenEventHandler) """
        ...

    def add_SlideSelectionChanged(self): # -> 
        """ add_SlideSelectionChanged(self: ApplicationClass, : EApplication_SlideSelectionChangedEventHandler) """
        ...

    def add_SlideShowBegin(self): # -> 
        """ add_SlideShowBegin(self: ApplicationClass, : EApplication_SlideShowBeginEventHandler) """
        ...

    def add_SlideShowEnd(self): # -> 
        """ add_SlideShowEnd(self: ApplicationClass, : EApplication_SlideShowEndEventHandler) """
        ...

    def add_SlideShowNextBuild(self): # -> 
        """ add_SlideShowNextBuild(self: ApplicationClass, : EApplication_SlideShowNextBuildEventHandler) """
        ...

    def add_SlideShowNextClick(self): # -> 
        """ add_SlideShowNextClick(self: ApplicationClass, : EApplication_SlideShowNextClickEventHandler) """
        ...

    def add_SlideShowNextSlide(self): # -> 
        """ add_SlideShowNextSlide(self: ApplicationClass, : EApplication_SlideShowNextSlideEventHandler) """
        ...

    def add_SlideShowOnNext(self): # -> 
        """ add_SlideShowOnNext(self: ApplicationClass, : EApplication_SlideShowOnNextEventHandler) """
        ...

    def add_SlideShowOnPrevious(self): # -> 
        """ add_SlideShowOnPrevious(self: ApplicationClass, : EApplication_SlideShowOnPreviousEventHandler) """
        ...

    def add_WindowActivate(self): # -> 
        """ add_WindowActivate(self: ApplicationClass, : EApplication_WindowActivateEventHandler) """
        ...

    def add_WindowBeforeDoubleClick(self): # -> 
        """ add_WindowBeforeDoubleClick(self: ApplicationClass, : EApplication_WindowBeforeDoubleClickEventHandler) """
        ...

    def add_WindowBeforeRightClick(self): # -> 
        """ add_WindowBeforeRightClick(self: ApplicationClass, : EApplication_WindowBeforeRightClickEventHandler) """
        ...

    def add_WindowDeactivate(self): # -> 
        """ add_WindowDeactivate(self: ApplicationClass, : EApplication_WindowDeactivateEventHandler) """
        ...

    def add_WindowSelectionChange(self): # -> 
        """ add_WindowSelectionChange(self: ApplicationClass, : EApplication_WindowSelectionChangeEventHandler) """
        ...

    def GetOptionFlag(self, Option:int, Persist:bool) -> bool:
        """ GetOptionFlag(self: ApplicationClass, Option: int, Persist: bool) -> bool """
        ...

    def Help(self, HelpFile:str, ContextID:int): # -> 
        """ Help(self: ApplicationClass, HelpFile: str, ContextID: int) """
        ...

    def LaunchPublishSlidesDialog(self, SlideLibraryUrl:str): # -> 
        """ LaunchPublishSlidesDialog(self: ApplicationClass, SlideLibraryUrl: str) """
        ...

    def LaunchSendToPPTDialog(self, SlideUrls:object) -> object:
        """ LaunchSendToPPTDialog(self: ApplicationClass, SlideUrls: object) -> object """
        ...

    def LaunchSpelling(self, pWindow:DocumentWindow): # -> 
        """ LaunchSpelling(self: ApplicationClass, pWindow: DocumentWindow) """
        ...

    def OpenThemeFile(self, themeFileName:str) -> Theme:
        """ OpenThemeFile(self: ApplicationClass, themeFileName: str) -> Theme """
        ...

    def PPFileDialog(self, Type:PpFileDialogType) -> object:
        """ PPFileDialog(self: ApplicationClass, Type: PpFileDialogType) -> object """
        ...

    def Quit(self): # -> 
        """ Quit(self: ApplicationClass) """
        ...

    def remove_AfterDragDropOnSlide(self): # -> 
        """ remove_AfterDragDropOnSlide(self: ApplicationClass, : EApplication_AfterDragDropOnSlideEventHandler) """
        ...

    def remove_AfterNewPresentation(self): # -> 
        """ remove_AfterNewPresentation(self: ApplicationClass, : EApplication_AfterNewPresentationEventHandler) """
        ...

    def remove_AfterPresentationOpen(self): # -> 
        """ remove_AfterPresentationOpen(self: ApplicationClass, : EApplication_AfterPresentationOpenEventHandler) """
        ...

    def remove_AfterShapeSizeChange(self): # -> 
        """ remove_AfterShapeSizeChange(self: ApplicationClass, : EApplication_AfterShapeSizeChangeEventHandler) """
        ...

    def remove_ColorSchemeChanged(self): # -> 
        """ remove_ColorSchemeChanged(self: ApplicationClass, : EApplication_ColorSchemeChangedEventHandler) """
        ...

    def remove_NewPresentation(self): # -> 
        """ remove_NewPresentation(self: ApplicationClass, : EApplication_NewPresentationEventHandler) """
        ...

    def remove_PresentationBeforeClose(self): # -> 
        """ remove_PresentationBeforeClose(self: ApplicationClass, : EApplication_PresentationBeforeCloseEventHandler) """
        ...

    def remove_PresentationBeforeSave(self): # -> 
        """ remove_PresentationBeforeSave(self: ApplicationClass, : EApplication_PresentationBeforeSaveEventHandler) """
        ...

    def remove_PresentationClose(self): # -> 
        """ remove_PresentationClose(self: ApplicationClass, : EApplication_PresentationCloseEventHandler) """
        ...

    def remove_PresentationCloseFinal(self): # -> 
        """ remove_PresentationCloseFinal(self: ApplicationClass, : EApplication_PresentationCloseFinalEventHandler) """
        ...

    def remove_PresentationNewSlide(self): # -> 
        """ remove_PresentationNewSlide(self: ApplicationClass, : EApplication_PresentationNewSlideEventHandler) """
        ...

    def remove_PresentationOpen(self): # -> 
        """ remove_PresentationOpen(self: ApplicationClass, : EApplication_PresentationOpenEventHandler) """
        ...

    def remove_PresentationPrint(self): # -> 
        """ remove_PresentationPrint(self: ApplicationClass, : EApplication_PresentationPrintEventHandler) """
        ...

    def remove_PresentationSave(self): # -> 
        """ remove_PresentationSave(self: ApplicationClass, : EApplication_PresentationSaveEventHandler) """
        ...

    def remove_PresentationSync(self): # -> 
        """ remove_PresentationSync(self: ApplicationClass, : EApplication_PresentationSyncEventHandler) """
        ...

    def remove_ProtectedViewWindowActivate(self): # -> 
        """ remove_ProtectedViewWindowActivate(self: ApplicationClass, : EApplication_ProtectedViewWindowActivateEventHandler) """
        ...

    def remove_ProtectedViewWindowBeforeClose(self): # -> 
        """ remove_ProtectedViewWindowBeforeClose(self: ApplicationClass, : EApplication_ProtectedViewWindowBeforeCloseEventHandler) """
        ...

    def remove_ProtectedViewWindowBeforeEdit(self): # -> 
        """ remove_ProtectedViewWindowBeforeEdit(self: ApplicationClass, : EApplication_ProtectedViewWindowBeforeEditEventHandler) """
        ...

    def remove_ProtectedViewWindowDeactivate(self): # -> 
        """ remove_ProtectedViewWindowDeactivate(self: ApplicationClass, : EApplication_ProtectedViewWindowDeactivateEventHandler) """
        ...

    def remove_ProtectedViewWindowOpen(self): # -> 
        """ remove_ProtectedViewWindowOpen(self: ApplicationClass, : EApplication_ProtectedViewWindowOpenEventHandler) """
        ...

    def remove_SlideSelectionChanged(self): # -> 
        """ remove_SlideSelectionChanged(self: ApplicationClass, : EApplication_SlideSelectionChangedEventHandler) """
        ...

    def remove_SlideShowBegin(self): # -> 
        """ remove_SlideShowBegin(self: ApplicationClass, : EApplication_SlideShowBeginEventHandler) """
        ...

    def remove_SlideShowEnd(self): # -> 
        """ remove_SlideShowEnd(self: ApplicationClass, : EApplication_SlideShowEndEventHandler) """
        ...

    def remove_SlideShowNextBuild(self): # -> 
        """ remove_SlideShowNextBuild(self: ApplicationClass, : EApplication_SlideShowNextBuildEventHandler) """
        ...

    def remove_SlideShowNextClick(self): # -> 
        """ remove_SlideShowNextClick(self: ApplicationClass, : EApplication_SlideShowNextClickEventHandler) """
        ...

    def remove_SlideShowNextSlide(self): # -> 
        """ remove_SlideShowNextSlide(self: ApplicationClass, : EApplication_SlideShowNextSlideEventHandler) """
        ...

    def remove_SlideShowOnNext(self): # -> 
        """ remove_SlideShowOnNext(self: ApplicationClass, : EApplication_SlideShowOnNextEventHandler) """
        ...

    def remove_SlideShowOnPrevious(self): # -> 
        """ remove_SlideShowOnPrevious(self: ApplicationClass, : EApplication_SlideShowOnPreviousEventHandler) """
        ...

    def remove_WindowActivate(self): # -> 
        """ remove_WindowActivate(self: ApplicationClass, : EApplication_WindowActivateEventHandler) """
        ...

    def remove_WindowBeforeDoubleClick(self): # -> 
        """ remove_WindowBeforeDoubleClick(self: ApplicationClass, : EApplication_WindowBeforeDoubleClickEventHandler) """
        ...

    def remove_WindowBeforeRightClick(self): # -> 
        """ remove_WindowBeforeRightClick(self: ApplicationClass, : EApplication_WindowBeforeRightClickEventHandler) """
        ...

    def remove_WindowDeactivate(self): # -> 
        """ remove_WindowDeactivate(self: ApplicationClass, : EApplication_WindowDeactivateEventHandler) """
        ...

    def remove_WindowSelectionChange(self): # -> 
        """ remove_WindowSelectionChange(self: ApplicationClass, : EApplication_WindowSelectionChangeEventHandler) """
        ...

    def Run(self, MacroName:str, safeArrayOfParams:Array) -> Tuple_[object, Array]:
        """ Run(self: ApplicationClass, MacroName: str, *safeArrayOfParams: Array[object]) -> (object, Array[object]) """
        ...

    def SetOptionFlag(self, Option:int, State:bool, Persist:bool): # -> 
        """ SetOptionFlag(self: ApplicationClass, Option: int, State: bool, Persist: bool) """
        ...

    def SetPerfMarker(self, Marker:int): # -> 
        """ SetPerfMarker(self: ApplicationClass, Marker: int) """
        ...

    def StartNewUndoEntry(self): # -> 
        """ StartNewUndoEntry(self: ApplicationClass) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    AfterDragDropOnSlide = ...
    AfterNewPresentation = ...
    AfterPresentationOpen = ...
    AfterShapeSizeChange = ...
    ColorSchemeChanged = ...
    EApplication_Event_NewPresentation = ...
    PresentationBeforeClose = ...
    PresentationBeforeSave = ...
    PresentationClose = ...
    PresentationCloseFinal = ...
    PresentationNewSlide = ...
    PresentationOpen = ...
    PresentationPrint = ...
    PresentationSave = ...
    PresentationSync = ...
    ProtectedViewWindowActivate = ...
    ProtectedViewWindowBeforeClose = ...
    ProtectedViewWindowBeforeEdit = ...
    ProtectedViewWindowDeactivate = ...
    ProtectedViewWindowOpen = ...
    SlideSelectionChanged = ...
    SlideShowBegin = ...
    SlideShowEnd = ...
    SlideShowNextBuild = ...
    SlideShowNextClick = ...
    SlideShowNextSlide = ...
    SlideShowOnNext = ...
    SlideShowOnPrevious = ...
    WindowActivate = ...
    WindowBeforeDoubleClick = ...
    WindowBeforeRightClick = ...
    WindowDeactivate = ...
    WindowSelectionChange = ...


class AutoCorrect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DisplayAutoCorrectOptions(self) -> bool:
        """
        Get: DisplayAutoCorrectOptions(self: AutoCorrect) -> bool
        Set: DisplayAutoCorrectOptions(self: AutoCorrect) = value
        """
        ...

    @property
    def DisplayAutoLayoutOptions(self) -> bool:
        """
        Get: DisplayAutoLayoutOptions(self: AutoCorrect) -> bool
        Set: DisplayAutoLayoutOptions(self: AutoCorrect) = value
        """
        ...



class Axes(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Axes) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Axes) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Axes) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Axes) -> object """
        ...


    def Item(self, Type:XlAxisType, AxisGroup:XlAxisGroup) -> Axis:
        """ Item(self: Axes, Type: XlAxisType, AxisGroup: XlAxisGroup) -> Axis """
        ...

    def _Default(self, Type:XlAxisType, AxisGroup:XlAxisGroup) -> Axis:
        """ _Default(self: Axes, Type: XlAxisType, AxisGroup: XlAxisGroup) -> Axis """
        ...


class Axis: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Axis) -> Application """
        ...

    @property
    def AxisBetweenCategories(self) -> bool:
        """
        Get: AxisBetweenCategories(self: Axis) -> bool
        Set: AxisBetweenCategories(self: Axis) = value
        """
        ...

    @property
    def AxisGroup(self) -> XlAxisGroup:
        """ Get: AxisGroup(self: Axis) -> XlAxisGroup """
        ...

    @property
    def AxisTitle(self) -> AxisTitle:
        """ Get: AxisTitle(self: Axis) -> AxisTitle """
        ...

    @property
    def BaseUnit(self) -> XlTimeUnit:
        """
        Get: BaseUnit(self: Axis) -> XlTimeUnit
        Set: BaseUnit(self: Axis) = value
        """
        ...

    @property
    def BaseUnitIsAuto(self) -> bool:
        """
        Get: BaseUnitIsAuto(self: Axis) -> bool
        Set: BaseUnitIsAuto(self: Axis) = value
        """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: Axis) -> ChartBorder """
        ...

    @property
    def CategoryNames(self) -> object:
        """
        Get: CategoryNames(self: Axis) -> object
        Set: CategoryNames(self: Axis) = value
        """
        ...

    @property
    def CategoryType(self) -> XlCategoryType:
        """
        Get: CategoryType(self: Axis) -> XlCategoryType
        Set: CategoryType(self: Axis) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Axis) -> int """
        ...

    @property
    def Crosses(self) -> XlAxisCrosses:
        """
        Get: Crosses(self: Axis) -> XlAxisCrosses
        Set: Crosses(self: Axis) = value
        """
        ...

    @property
    def CrossesAt(self) -> float:
        """
        Get: CrossesAt(self: Axis) -> float
        Set: CrossesAt(self: Axis) = value
        """
        ...

    @property
    def DisplayUnit(self) -> XlDisplayUnit:
        """
        Get: DisplayUnit(self: Axis) -> XlDisplayUnit
        Set: DisplayUnit(self: Axis) = value
        """
        ...

    @property
    def DisplayUnitCustom(self) -> float:
        """
        Get: DisplayUnitCustom(self: Axis) -> float
        Set: DisplayUnitCustom(self: Axis) = value
        """
        ...

    @property
    def DisplayUnitLabel(self) -> DisplayUnitLabel:
        """ Get: DisplayUnitLabel(self: Axis) -> DisplayUnitLabel """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: Axis) -> ChartFormat """
        ...

    @property
    def HasDisplayUnitLabel(self) -> bool:
        """
        Get: HasDisplayUnitLabel(self: Axis) -> bool
        Set: HasDisplayUnitLabel(self: Axis) = value
        """
        ...

    @property
    def HasMajorGridlines(self) -> bool:
        """
        Get: HasMajorGridlines(self: Axis) -> bool
        Set: HasMajorGridlines(self: Axis) = value
        """
        ...

    @property
    def HasMinorGridlines(self) -> bool:
        """
        Get: HasMinorGridlines(self: Axis) -> bool
        Set: HasMinorGridlines(self: Axis) = value
        """
        ...

    @property
    def HasTitle(self) -> bool:
        """
        Get: HasTitle(self: Axis) -> bool
        Set: HasTitle(self: Axis) = value
        """
        ...

    @property
    def Height(self) -> float:
        """ Get: Height(self: Axis) -> float """
        ...

    @property
    def Left(self) -> float:
        """ Get: Left(self: Axis) -> float """
        ...

    @property
    def LogBase(self) -> float:
        """
        Get: LogBase(self: Axis) -> float
        Set: LogBase(self: Axis) = value
        """
        ...

    @property
    def MajorGridlines(self) -> Gridlines:
        """ Get: MajorGridlines(self: Axis) -> Gridlines """
        ...

    @property
    def MajorTickMark(self) -> XlTickMark:
        """
        Get: MajorTickMark(self: Axis) -> XlTickMark
        Set: MajorTickMark(self: Axis) = value
        """
        ...

    @property
    def MajorUnit(self) -> float:
        """
        Get: MajorUnit(self: Axis) -> float
        Set: MajorUnit(self: Axis) = value
        """
        ...

    @property
    def MajorUnitIsAuto(self) -> bool:
        """
        Get: MajorUnitIsAuto(self: Axis) -> bool
        Set: MajorUnitIsAuto(self: Axis) = value
        """
        ...

    @property
    def MajorUnitScale(self) -> XlTimeUnit:
        """
        Get: MajorUnitScale(self: Axis) -> XlTimeUnit
        Set: MajorUnitScale(self: Axis) = value
        """
        ...

    @property
    def MaximumScale(self) -> float:
        """
        Get: MaximumScale(self: Axis) -> float
        Set: MaximumScale(self: Axis) = value
        """
        ...

    @property
    def MaximumScaleIsAuto(self) -> bool:
        """
        Get: MaximumScaleIsAuto(self: Axis) -> bool
        Set: MaximumScaleIsAuto(self: Axis) = value
        """
        ...

    @property
    def MinimumScale(self) -> float:
        """
        Get: MinimumScale(self: Axis) -> float
        Set: MinimumScale(self: Axis) = value
        """
        ...

    @property
    def MinimumScaleIsAuto(self) -> bool:
        """
        Get: MinimumScaleIsAuto(self: Axis) -> bool
        Set: MinimumScaleIsAuto(self: Axis) = value
        """
        ...

    @property
    def MinorGridlines(self) -> Gridlines:
        """ Get: MinorGridlines(self: Axis) -> Gridlines """
        ...

    @property
    def MinorTickMark(self) -> XlTickMark:
        """
        Get: MinorTickMark(self: Axis) -> XlTickMark
        Set: MinorTickMark(self: Axis) = value
        """
        ...

    @property
    def MinorUnit(self) -> float:
        """
        Get: MinorUnit(self: Axis) -> float
        Set: MinorUnit(self: Axis) = value
        """
        ...

    @property
    def MinorUnitIsAuto(self) -> bool:
        """
        Get: MinorUnitIsAuto(self: Axis) -> bool
        Set: MinorUnitIsAuto(self: Axis) = value
        """
        ...

    @property
    def MinorUnitScale(self) -> XlTimeUnit:
        """
        Get: MinorUnitScale(self: Axis) -> XlTimeUnit
        Set: MinorUnitScale(self: Axis) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Axis) -> object """
        ...

    @property
    def ReversePlotOrder(self) -> bool:
        """
        Get: ReversePlotOrder(self: Axis) -> bool
        Set: ReversePlotOrder(self: Axis) = value
        """
        ...

    @property
    def ScaleType(self) -> XlScaleType:
        """
        Get: ScaleType(self: Axis) -> XlScaleType
        Set: ScaleType(self: Axis) = value
        """
        ...

    @property
    def TickLabelPosition(self) -> XlTickLabelPosition:
        """
        Get: TickLabelPosition(self: Axis) -> XlTickLabelPosition
        Set: TickLabelPosition(self: Axis) = value
        """
        ...

    @property
    def TickLabels(self) -> TickLabels:
        """ Get: TickLabels(self: Axis) -> TickLabels """
        ...

    @property
    def TickLabelSpacing(self) -> int:
        """
        Get: TickLabelSpacing(self: Axis) -> int
        Set: TickLabelSpacing(self: Axis) = value
        """
        ...

    @property
    def TickLabelSpacingIsAuto(self) -> bool:
        """
        Get: TickLabelSpacingIsAuto(self: Axis) -> bool
        Set: TickLabelSpacingIsAuto(self: Axis) = value
        """
        ...

    @property
    def TickMarkSpacing(self) -> int:
        """
        Get: TickMarkSpacing(self: Axis) -> int
        Set: TickMarkSpacing(self: Axis) = value
        """
        ...

    @property
    def Top(self) -> float:
        """ Get: Top(self: Axis) -> float """
        ...

    @property
    def Type(self) -> XlAxisType:
        """
        Get: Type(self: Axis) -> XlAxisType
        Set: Type(self: Axis) = value
        """
        ...

    @property
    def Width(self) -> float:
        """ Get: Width(self: Axis) -> float """
        ...


    def Delete(self) -> object:
        """ Delete(self: Axis) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: Axis) -> object """
        ...


class AxisTitle: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: AxisTitle) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: AxisTitle) -> object
        Set: AutoScaleFont(self: AxisTitle) = value
        """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: AxisTitle) -> ChartBorder """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: AxisTitle) -> str
        Set: Caption(self: AxisTitle) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: AxisTitle) -> int """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: AxisTitle) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> ChartFont:
        """ Get: Font(self: AxisTitle) -> ChartFont """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: AxisTitle) -> ChartFormat """
        ...

    @property
    def Formula(self) -> str:
        """
        Get: Formula(self: AxisTitle) -> str
        Set: Formula(self: AxisTitle) = value
        """
        ...

    @property
    def FormulaLocal(self) -> str:
        """
        Get: FormulaLocal(self: AxisTitle) -> str
        Set: FormulaLocal(self: AxisTitle) = value
        """
        ...

    @property
    def FormulaR1C1(self) -> str:
        """
        Get: FormulaR1C1(self: AxisTitle) -> str
        Set: FormulaR1C1(self: AxisTitle) = value
        """
        ...

    @property
    def FormulaR1C1Local(self) -> str:
        """
        Get: FormulaR1C1Local(self: AxisTitle) -> str
        Set: FormulaR1C1Local(self: AxisTitle) = value
        """
        ...

    @property
    def Height(self) -> float:
        """ Get: Height(self: AxisTitle) -> float """
        ...

    @property
    def HorizontalAlignment(self) -> object:
        """
        Get: HorizontalAlignment(self: AxisTitle) -> object
        Set: HorizontalAlignment(self: AxisTitle) = value
        """
        ...

    @property
    def IncludeInLayout(self) -> bool:
        """
        Get: IncludeInLayout(self: AxisTitle) -> bool
        Set: IncludeInLayout(self: AxisTitle) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: AxisTitle) -> Interior """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: AxisTitle) -> float
        Set: Left(self: AxisTitle) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: AxisTitle) -> str """
        ...

    @property
    def Orientation(self) -> object:
        """
        Get: Orientation(self: AxisTitle) -> object
        Set: Orientation(self: AxisTitle) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: AxisTitle) -> object """
        ...

    @property
    def Position(self) -> XlChartElementPosition:
        """
        Get: Position(self: AxisTitle) -> XlChartElementPosition
        Set: Position(self: AxisTitle) = value
        """
        ...

    @property
    def ReadingOrder(self) -> int:
        """
        Get: ReadingOrder(self: AxisTitle) -> int
        Set: ReadingOrder(self: AxisTitle) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: AxisTitle) -> bool
        Set: Shadow(self: AxisTitle) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: AxisTitle) -> str
        Set: Text(self: AxisTitle) = value
        """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: AxisTitle) -> float
        Set: Top(self: AxisTitle) = value
        """
        ...

    @property
    def VerticalAlignment(self) -> object:
        """
        Get: VerticalAlignment(self: AxisTitle) -> object
        Set: VerticalAlignment(self: AxisTitle) = value
        """
        ...

    @property
    def Width(self) -> float:
        """ Get: Width(self: AxisTitle) -> float """
        ...


    def Delete(self) -> object:
        """ Delete(self: AxisTitle) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: AxisTitle) -> object """
        ...


class Borders(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Borders) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Borders) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Broadcast: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Broadcast) -> Application """
        ...

    @property
    def AttendeeUrl(self) -> str:
        """ Get: AttendeeUrl(self: Broadcast) -> str """
        ...

    @property
    def Capabilities(self) -> int:
        """ Get: Capabilities(self: Broadcast) -> int """
        ...

    @property
    def IsBroadcasting(self) -> bool:
        """ Get: IsBroadcasting(self: Broadcast) -> bool """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Broadcast) -> object """
        ...

    @property
    def PresenterServiceUrl(self) -> str:
        """ Get: PresenterServiceUrl(self: Broadcast) -> str """
        ...

    @property
    def SessionID(self) -> str:
        """ Get: SessionID(self: Broadcast) -> str """
        ...

    @property
    def State(self): # -> MsoBroadcastState
        """ Get: State(self: Broadcast) -> MsoBroadcastState """
        ...


    def AddMeetingNotes(self, notesUrl:str, notesWacUrl:str): # -> 
        """ AddMeetingNotes(self: Broadcast, notesUrl: str, notesWacUrl: str) """
        ...

    def End(self): # -> 
        """ End(self: Broadcast) """
        ...

    def Pause(self): # -> 
        """ Pause(self: Broadcast) """
        ...

    def Resume(self): # -> 
        """ Resume(self: Broadcast) """
        ...

    def Start(self, serverUrl:str): # -> 
        """ Start(self: Broadcast, serverUrl: str) """
        ...


class BulletFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: BulletFormat) -> Application """
        ...

    @property
    def Character(self) -> int:
        """
        Get: Character(self: BulletFormat) -> int
        Set: Character(self: BulletFormat) = value
        """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: BulletFormat) -> Font """
        ...

    @property
    def Number(self) -> int:
        """ Get: Number(self: BulletFormat) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: BulletFormat) -> object """
        ...

    @property
    def RelativeSize(self) -> Single:
        """
        Get: RelativeSize(self: BulletFormat) -> Single
        Set: RelativeSize(self: BulletFormat) = value
        """
        ...

    @property
    def StartValue(self) -> int:
        """
        Get: StartValue(self: BulletFormat) -> int
        Set: StartValue(self: BulletFormat) = value
        """
        ...

    @property
    def Style(self) -> PpNumberedBulletStyle:
        """
        Get: Style(self: BulletFormat) -> PpNumberedBulletStyle
        Set: Style(self: BulletFormat) = value
        """
        ...

    @property
    def Type(self) -> PpBulletType:
        """
        Get: Type(self: BulletFormat) -> PpBulletType
        Set: Type(self: BulletFormat) = value
        """
        ...

    @property
    def UseTextColor(self): # -> MsoTriState
        """
        Get: UseTextColor(self: BulletFormat) -> MsoTriState
        Set: UseTextColor(self: BulletFormat) = value
        """
        ...

    @property
    def UseTextFont(self): # -> MsoTriState
        """
        Get: UseTextFont(self: BulletFormat) -> MsoTriState
        Set: UseTextFont(self: BulletFormat) = value
        """
        ...

    @property
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: BulletFormat) -> MsoTriState
        Set: Visible(self: BulletFormat) = value
        """
        ...


    def Picture(self, Picture:str): # -> 
        """ Picture(self: BulletFormat, Picture: str) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
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
    def Application(self) -> object:
        """ Get: Application(self: CalloutFormat) -> object """
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
    def Creator(self) -> int:
        """ Get: Creator(self: CalloutFormat) -> int """
        ...

    @property
    def Drop(self) -> Single:
        """ Get: Drop(self: CalloutFormat) -> Single """
        ...

    @property
    def DropType(self): # -> MsoCalloutDropType
        """ Get: DropType(self: CalloutFormat) -> MsoCalloutDropType """
        ...

    @property
    def Gap(self) -> Single:
        """
        Get: Gap(self: CalloutFormat) -> Single
        Set: Gap(self: CalloutFormat) = value
        """
        ...

    @property
    def Length(self) -> Single:
        """ Get: Length(self: CalloutFormat) -> Single """
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

    def CustomDrop(self, Drop:Single): # -> 
        """ CustomDrop(self: CalloutFormat, Drop: Single) """
        ...

    def CustomLength(self, Length:Single): # -> 
        """ CustomLength(self: CalloutFormat, Length: Single) """
        ...

    def PresetDrop(self, DropType): # ->  # Not found arg types: {'DropType': 'MsoCalloutDropType'}
        """ PresetDrop(self: CalloutFormat, DropType: MsoCalloutDropType) """
        ...


class CanvasShapes(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: CanvasShapes) -> object """
        ...

    @property
    def Background(self) -> Shape:
        """ Get: Background(self: CanvasShapes) -> Shape """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: CanvasShapes) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: CanvasShapes) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: CanvasShapes) -> object """
        ...


    def AddCallout(self, Type, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape: # Not found arg types: {'Type': 'MsoCalloutType'}
        """ AddCallout(self: CanvasShapes, Type: MsoCalloutType, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddConnector(self, Type, BeginX:Single, BeginY:Single, EndX:Single, EndY:Single) -> Shape: # Not found arg types: {'Type': 'MsoConnectorType'}
        """ AddConnector(self: CanvasShapes, Type: MsoConnectorType, BeginX: Single, BeginY: Single, EndX: Single, EndY: Single) -> Shape """
        ...

    def AddCurve(self, SafeArrayOfPoints:object) -> Shape:
        """ AddCurve(self: CanvasShapes, SafeArrayOfPoints: object) -> Shape """
        ...

    def AddLabel(self, Orientation, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape: # Not found arg types: {'Orientation': 'MsoTextOrientation'}
        """ AddLabel(self: CanvasShapes, Orientation: MsoTextOrientation, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddLine(self, BeginX:Single, BeginY:Single, EndX:Single, EndY:Single) -> Shape:
        """ AddLine(self: CanvasShapes, BeginX: Single, BeginY: Single, EndX: Single, EndY: Single) -> Shape """
        ...

    def AddPicture(self, FileName:str, LinkToFile, SaveWithDocument, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape: # Not found arg types: {'LinkToFile': 'MsoTriState', 'SaveWithDocument': 'MsoTriState'}
        """ AddPicture(self: CanvasShapes, FileName: str, LinkToFile: MsoTriState, SaveWithDocument: MsoTriState, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddPolyline(self, SafeArrayOfPoints:object) -> Shape:
        """ AddPolyline(self: CanvasShapes, SafeArrayOfPoints: object) -> Shape """
        ...

    def AddShape(self, Type, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape: # Not found arg types: {'Type': 'MsoAutoShapeType'}
        """ AddShape(self: CanvasShapes, Type: MsoAutoShapeType, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddTextbox(self, Orientation, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape: # Not found arg types: {'Orientation': 'MsoTextOrientation'}
        """ AddTextbox(self: CanvasShapes, Orientation: MsoTextOrientation, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddTextEffect(self, PresetTextEffect, Text:str, FontName:str, FontSize:Single, FontBold, FontItalic, Left:Single, Top:Single) -> Shape: # Not found arg types: {'FontItalic': 'MsoTriState', 'FontBold': 'MsoTriState', 'PresetTextEffect': 'MsoPresetTextEffect'}
        """ AddTextEffect(self: CanvasShapes, PresetTextEffect: MsoPresetTextEffect, Text: str, FontName: str, FontSize: Single, FontBold: MsoTriState, FontItalic: MsoTriState, Left: Single, Top: Single) -> Shape """
        ...

    def BuildFreeform(self, EditingType, X1:Single, Y1:Single) -> FreeformBuilder: # Not found arg types: {'EditingType': 'MsoEditingType'}
        """ BuildFreeform(self: CanvasShapes, EditingType: MsoEditingType, X1: Single, Y1: Single) -> FreeformBuilder """
        ...

    def Range(self, Index:object) -> ShapeRange:
        """ Range(self: CanvasShapes, Index: object) -> ShapeRange """
        ...

    def SelectAll(self): # -> 
        """ SelectAll(self: CanvasShapes) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class CategoryCollection: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: CategoryCollection) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: CategoryCollection) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: CategoryCollection) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: CategoryCollection) -> object """
        ...


    def Item(self, Index:object) -> ChartCategory:
        """ Item(self: CategoryCollection, Index: object) -> ChartCategory """
        ...

    def _Default(self, Index:object) -> ChartCategory:
        """ _Default(self: CategoryCollection, Index: object) -> ChartCategory """
        ...


class Cell: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Cell) -> Application """
        ...

    @property
    def Borders(self) -> Borders:
        """ Get: Borders(self: Cell) -> Borders """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Cell) -> object """
        ...

    @property
    def Selected(self) -> bool:
        """ Get: Selected(self: Cell) -> bool """
        ...

    @property
    def Shape(self) -> Shape:
        """ Get: Shape(self: Cell) -> Shape """
        ...


    def Merge(self, MergeTo:Cell): # -> 
        """ Merge(self: Cell, MergeTo: Cell) """
        ...

    def Select(self): # -> 
        """ Select(self: Cell) """
        ...

    def Split(self, NumRows:int, NumColumns:int): # -> 
        """ Split(self: Cell, NumRows: int, NumColumns: int) """
        ...


class CellRange(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: CellRange) -> Application """
        ...

    @property
    def Borders(self) -> Borders:
        """ Get: Borders(self: CellRange) -> Borders """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: CellRange) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Chart: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AlternativeText(self) -> str:
        """
        Get: AlternativeText(self: Chart) -> str
        Set: AlternativeText(self: Chart) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: Chart) -> Application """
        ...

    @property
    def Area3DGroup(self) -> ChartGroup:
        """ Get: Area3DGroup(self: Chart) -> ChartGroup """
        ...

    @property
    def AutoScaling(self) -> bool:
        """
        Get: AutoScaling(self: Chart) -> bool
        Set: AutoScaling(self: Chart) = value
        """
        ...

    @property
    def BackWall(self) -> Walls:
        """ Get: BackWall(self: Chart) -> Walls """
        ...

    @property
    def Bar3DGroup(self) -> ChartGroup:
        """ Get: Bar3DGroup(self: Chart) -> ChartGroup """
        ...

    @property
    def BarShape(self) -> XlBarShape:
        """
        Get: BarShape(self: Chart) -> XlBarShape
        Set: BarShape(self: Chart) = value
        """
        ...

    @property
    def CategoryLabelLevel(self) -> XlCategoryLabelLevel:
        """
        Get: CategoryLabelLevel(self: Chart) -> XlCategoryLabelLevel
        Set: CategoryLabelLevel(self: Chart) = value
        """
        ...

    @property
    def ChartArea(self) -> ChartArea:
        """ Get: ChartArea(self: Chart) -> ChartArea """
        ...

    @property
    def ChartColor(self) -> object:
        """
        Get: ChartColor(self: Chart) -> object
        Set: ChartColor(self: Chart) = value
        """
        ...

    @property
    def ChartData(self) -> ChartData:
        """ Get: ChartData(self: Chart) -> ChartData """
        ...

    @property
    def ChartStyle(self) -> object:
        """
        Get: ChartStyle(self: Chart) -> object
        Set: ChartStyle(self: Chart) = value
        """
        ...

    @property
    def ChartTitle(self) -> ChartTitle:
        """ Get: ChartTitle(self: Chart) -> ChartTitle """
        ...

    @property
    def ChartType(self) -> XlChartType:
        """
        Get: ChartType(self: Chart) -> XlChartType
        Set: ChartType(self: Chart) = value
        """
        ...

    @property
    def Column3DGroup(self) -> ChartGroup:
        """ Get: Column3DGroup(self: Chart) -> ChartGroup """
        ...

    @property
    def Corners(self) -> Corners:
        """ Get: Corners(self: Chart) -> Corners """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Chart) -> int """
        ...

    @property
    def DataTable(self) -> DataTable:
        """ Get: DataTable(self: Chart) -> DataTable """
        ...

    @property
    def DepthPercent(self) -> int:
        """
        Get: DepthPercent(self: Chart) -> int
        Set: DepthPercent(self: Chart) = value
        """
        ...

    @property
    def DisplayBlanksAs(self) -> XlDisplayBlanksAs:
        """
        Get: DisplayBlanksAs(self: Chart) -> XlDisplayBlanksAs
        Set: DisplayBlanksAs(self: Chart) = value
        """
        ...

    @property
    def Elevation(self) -> int:
        """
        Get: Elevation(self: Chart) -> int
        Set: Elevation(self: Chart) = value
        """
        ...

    @property
    def Floor(self) -> Floor:
        """ Get: Floor(self: Chart) -> Floor """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: Chart) -> ChartFormat """
        ...

    @property
    def GapDepth(self) -> int:
        """
        Get: GapDepth(self: Chart) -> int
        Set: GapDepth(self: Chart) = value
        """
        ...

    @property
    def HasDataTable(self) -> bool:
        """
        Get: HasDataTable(self: Chart) -> bool
        Set: HasDataTable(self: Chart) = value
        """
        ...

    @property
    def HasHiddenContent(self) -> bool:
        """ Get: HasHiddenContent(self: Chart) -> bool """
        ...

    @property
    def HasLegend(self) -> bool:
        """
        Get: HasLegend(self: Chart) -> bool
        Set: HasLegend(self: Chart) = value
        """
        ...

    @property
    def HasPivotFields(self) -> bool:
        """
        Get: HasPivotFields(self: Chart) -> bool
        Set: HasPivotFields(self: Chart) = value
        """
        ...

    @property
    def HasTitle(self) -> bool:
        """
        Get: HasTitle(self: Chart) -> bool
        Set: HasTitle(self: Chart) = value
        """
        ...

    @property
    def HeightPercent(self) -> int:
        """
        Get: HeightPercent(self: Chart) -> int
        Set: HeightPercent(self: Chart) = value
        """
        ...

    @property
    def Legend(self) -> Legend:
        """ Get: Legend(self: Chart) -> Legend """
        ...

    @property
    def Line3DGroup(self) -> ChartGroup:
        """ Get: Line3DGroup(self: Chart) -> ChartGroup """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Chart) -> str
        Set: Name(self: Chart) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Chart) -> object """
        ...

    @property
    def Perspective(self) -> int:
        """
        Get: Perspective(self: Chart) -> int
        Set: Perspective(self: Chart) = value
        """
        ...

    @property
    def Pie3DGroup(self) -> ChartGroup:
        """ Get: Pie3DGroup(self: Chart) -> ChartGroup """
        ...

    @property
    def PlotArea(self) -> PlotArea:
        """ Get: PlotArea(self: Chart) -> PlotArea """
        ...

    @property
    def PlotBy(self) -> XlRowCol:
        """
        Get: PlotBy(self: Chart) -> XlRowCol
        Set: PlotBy(self: Chart) = value
        """
        ...

    @property
    def PlotVisibleOnly(self) -> bool:
        """
        Get: PlotVisibleOnly(self: Chart) -> bool
        Set: PlotVisibleOnly(self: Chart) = value
        """
        ...

    @property
    def RightAngleAxes(self) -> object:
        """
        Get: RightAngleAxes(self: Chart) -> object
        Set: RightAngleAxes(self: Chart) = value
        """
        ...

    @property
    def Rotation(self) -> object:
        """
        Get: Rotation(self: Chart) -> object
        Set: Rotation(self: Chart) = value
        """
        ...

    @property
    def SeriesNameLevel(self) -> XlSeriesNameLevel:
        """
        Get: SeriesNameLevel(self: Chart) -> XlSeriesNameLevel
        Set: SeriesNameLevel(self: Chart) = value
        """
        ...

    @property
    def Shapes(self) -> Shapes:
        """ Get: Shapes(self: Chart) -> Shapes """
        ...

    @property
    def ShowAllFieldButtons(self) -> bool:
        """
        Get: ShowAllFieldButtons(self: Chart) -> bool
        Set: ShowAllFieldButtons(self: Chart) = value
        """
        ...

    @property
    def ShowAxisFieldButtons(self) -> bool:
        """
        Get: ShowAxisFieldButtons(self: Chart) -> bool
        Set: ShowAxisFieldButtons(self: Chart) = value
        """
        ...

    @property
    def ShowDataLabelsOverMaximum(self) -> bool:
        """
        Get: ShowDataLabelsOverMaximum(self: Chart) -> bool
        Set: ShowDataLabelsOverMaximum(self: Chart) = value
        """
        ...

    @property
    def ShowLegendFieldButtons(self) -> bool:
        """
        Get: ShowLegendFieldButtons(self: Chart) -> bool
        Set: ShowLegendFieldButtons(self: Chart) = value
        """
        ...

    @property
    def ShowReportFilterFieldButtons(self) -> bool:
        """
        Get: ShowReportFilterFieldButtons(self: Chart) -> bool
        Set: ShowReportFilterFieldButtons(self: Chart) = value
        """
        ...

    @property
    def ShowValueFieldButtons(self) -> bool:
        """
        Get: ShowValueFieldButtons(self: Chart) -> bool
        Set: ShowValueFieldButtons(self: Chart) = value
        """
        ...

    @property
    def SideWall(self) -> Walls:
        """ Get: SideWall(self: Chart) -> Walls """
        ...

    @property
    def Subtype(self) -> int:
        """
        Get: Subtype(self: Chart) -> int
        Set: Subtype(self: Chart) = value
        """
        ...

    @property
    def SurfaceGroup(self) -> ChartGroup:
        """ Get: SurfaceGroup(self: Chart) -> ChartGroup """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: Chart) -> str
        Set: Title(self: Chart) = value
        """
        ...

    @property
    def Type(self) -> int:
        """
        Get: Type(self: Chart) -> int
        Set: Type(self: Chart) = value
        """
        ...

    @property
    def Walls(self) -> Walls:
        """ Get: Walls(self: Chart) -> Walls """
        ...


    def ApplyChartTemplate(self, FileName:str): # -> 
        """ ApplyChartTemplate(self: Chart, FileName: str) """
        ...

    def ApplyCustomType(self, ChartType:XlChartType, TypeName:object): # -> 
        """ ApplyCustomType(self: Chart, ChartType: XlChartType, TypeName: object) """
        ...

    def ApplyDataLabels(self, Type:XlDataLabelsType, LegendKey:object, AutoText:object, HasLeaderLines:object, ShowSeriesName:object, ShowCategoryName:object, ShowValue:object, ShowPercentage:object, ShowBubbleSize:object, Separator:object): # -> 
        """ ApplyDataLabels(self: Chart, Type: XlDataLabelsType, LegendKey: object, AutoText: object, HasLeaderLines: object, ShowSeriesName: object, ShowCategoryName: object, ShowValue: object, ShowPercentage: object, ShowBubbleSize: object, Separator: object) """
        ...

    def ApplyLayout(self, Layout:int, ChartType:object): # -> 
        """ ApplyLayout(self: Chart, Layout: int, ChartType: object) """
        ...

    def AreaGroups(self, Index:object) -> object:
        """ AreaGroups(self: Chart, Index: object) -> object """
        ...

    def AutoFormat(self, Gallery:int, Format:object): # -> 
        """ AutoFormat(self: Chart, Gallery: int, Format: object) """
        ...

    def Axes(self, Type:object, AxisGroup:XlAxisGroup) -> object:
        """ Axes(self: Chart, Type: object, AxisGroup: XlAxisGroup) -> object """
        ...

    def BarGroups(self, Index:object) -> object:
        """ BarGroups(self: Chart, Index: object) -> object """
        ...

    def ChartGroups(self, Index:object) -> object:
        """ ChartGroups(self: Chart, Index: object) -> object """
        ...

    def ChartWizard(self, Source:object, Gallery:object, Format:object, PlotBy:object, CategoryLabels:object, SeriesLabels:object, HasLegend:object, Title:object, CategoryTitle:object, ValueTitle:object, ExtraTitle:object): # -> 
        """ ChartWizard(self: Chart, Source: object, Gallery: object, Format: object, PlotBy: object, CategoryLabels: object, SeriesLabels: object, HasLegend: object, Title: object, CategoryTitle: object, ValueTitle: object, ExtraTitle: object) """
        ...

    def ClearToMatchColorStyle(self): # -> 
        """ ClearToMatchColorStyle(self: Chart) """
        ...

    def ClearToMatchStyle(self): # -> 
        """ ClearToMatchStyle(self: Chart) """
        ...

    def ColumnGroups(self, Index:object) -> object:
        """ ColumnGroups(self: Chart, Index: object) -> object """
        ...

    def Copy(self, Before:object, After:object): # -> 
        """ Copy(self: Chart, Before: object, After: object) """
        ...

    def CopyPicture(self, Appearance:XlPictureAppearance, Format:XlCopyPictureFormat, Size:XlPictureAppearance): # -> 
        """ CopyPicture(self: Chart, Appearance: XlPictureAppearance, Format: XlCopyPictureFormat, Size: XlPictureAppearance) """
        ...

    def Delete(self): # -> 
        """ Delete(self: Chart) """
        ...

    def DeleteHiddenContent(self): # -> 
        """ DeleteHiddenContent(self: Chart) """
        ...

    def DoughnutGroups(self, Index:object) -> object:
        """ DoughnutGroups(self: Chart, Index: object) -> object """
        ...

    def Export(self, FileName:str, FilterName:object, Interactive:object) -> bool:
        """ Export(self: Chart, FileName: str, FilterName: object, Interactive: object) -> bool """
        ...

    def FullSeriesCollection(self, Index:object) -> object:
        """ FullSeriesCollection(self: Chart, Index: object) -> object """
        ...

    def GetChartElement(self, X, Y, ElementID, Arg1, Arg2) -> Tuple_[int, int, int]:
        """ GetChartElement(self: Chart, X: int, Y: int) -> (int, int, int) """
        ...

    def LineGroups(self, Index:object) -> object:
        """ LineGroups(self: Chart, Index: object) -> object """
        ...

    def Paste(self, Type:object): # -> 
        """ Paste(self: Chart, Type: object) """
        ...

    def PieGroups(self, Index:object) -> object:
        """ PieGroups(self: Chart, Index: object) -> object """
        ...

    def RadarGroups(self, Index:object) -> object:
        """ RadarGroups(self: Chart, Index: object) -> object """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: Chart) """
        ...

    def SaveChartTemplate(self, FileName:str): # -> 
        """ SaveChartTemplate(self: Chart, FileName: str) """
        ...

    def Select(self, Replace:object): # -> 
        """ Select(self: Chart, Replace: object) """
        ...

    def SeriesCollection(self, Index:object) -> object:
        """ SeriesCollection(self: Chart, Index: object) -> object """
        ...

    def SetBackgroundPicture(self, FileName:str): # -> 
        """ SetBackgroundPicture(self: Chart, FileName: str) """
        ...

    def SetDefaultChart(self, Name:object): # -> 
        """ SetDefaultChart(self: Chart, Name: object) """
        ...

    def SetElement(self, Element): # ->  # Not found arg types: {'Element': 'MsoChartElementType'}
        """ SetElement(self: Chart, Element: MsoChartElementType) """
        ...

    def SetSourceData(self, Source:str, PlotBy:object): # -> 
        """ SetSourceData(self: Chart, Source: str, PlotBy: object) """
        ...

    def XYGroups(self, Index:object) -> object:
        """ XYGroups(self: Chart, Index: object) -> object """
        ...

    def _ApplyDataLabels(self, Type:XlDataLabelsType, LegendKey:object, AutoText:object, HasLeaderLines:object): # -> 
        """ _ApplyDataLabels(self: Chart, Type: XlDataLabelsType, LegendKey: object, AutoText: object, HasLeaderLines: object) """
        ...


class ChartArea: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ChartArea) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: ChartArea) -> object
        Set: AutoScaleFont(self: ChartArea) = value
        """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: ChartArea) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: ChartArea) -> int """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: ChartArea) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> ChartFont:
        """ Get: Font(self: ChartArea) -> ChartFont """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: ChartArea) -> ChartFormat """
        ...

    @property
    def Height(self) -> float:
        """
        Get: Height(self: ChartArea) -> float
        Set: Height(self: ChartArea) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: ChartArea) -> Interior """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: ChartArea) -> float
        Set: Left(self: ChartArea) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ChartArea) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ChartArea) -> object """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: ChartArea) -> bool
        Set: Shadow(self: ChartArea) = value
        """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: ChartArea) -> float
        Set: Top(self: ChartArea) = value
        """
        ...

    @property
    def Width(self) -> float:
        """
        Get: Width(self: ChartArea) -> float
        Set: Width(self: ChartArea) = value
        """
        ...


    def Clear(self) -> object:
        """ Clear(self: ChartArea) -> object """
        ...

    def ClearContents(self) -> object:
        """ ClearContents(self: ChartArea) -> object """
        ...

    def ClearFormats(self) -> object:
        """ ClearFormats(self: ChartArea) -> object """
        ...

    def Copy(self) -> object:
        """ Copy(self: ChartArea) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: ChartArea) -> object """
        ...


class ChartBorder: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ChartBorder) -> Application """
        ...

    @property
    def Color(self) -> object:
        """
        Get: Color(self: ChartBorder) -> object
        Set: Color(self: ChartBorder) = value
        """
        ...

    @property
    def ColorIndex(self) -> object:
        """
        Get: ColorIndex(self: ChartBorder) -> object
        Set: ColorIndex(self: ChartBorder) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: ChartBorder) -> int """
        ...

    @property
    def LineStyle(self) -> object:
        """
        Get: LineStyle(self: ChartBorder) -> object
        Set: LineStyle(self: ChartBorder) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ChartBorder) -> object """
        ...

    @property
    def Weight(self) -> object:
        """
        Get: Weight(self: ChartBorder) -> object
        Set: Weight(self: ChartBorder) = value
        """
        ...



class ChartCategory: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsFiltered(self) -> bool:
        """
        Get: IsFiltered(self: ChartCategory) -> bool
        Set: IsFiltered(self: ChartCategory) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ChartCategory) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ChartCategory) -> object """
        ...



class ChartCharacters: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ChartCharacters) -> Application """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: ChartCharacters) -> str
        Set: Caption(self: ChartCharacters) = value
        """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ChartCharacters) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: ChartCharacters) -> int """
        ...

    @property
    def Font(self) -> ChartFont:
        """ Get: Font(self: ChartCharacters) -> ChartFont """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ChartCharacters) -> object """
        ...

    @property
    def PhoneticCharacters(self) -> str:
        """
        Get: PhoneticCharacters(self: ChartCharacters) -> str
        Set: PhoneticCharacters(self: ChartCharacters) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: ChartCharacters) -> str
        Set: Text(self: ChartCharacters) = value
        """
        ...


    def Delete(self) -> object:
        """ Delete(self: ChartCharacters) -> object """
        ...

    def Insert(self, String:str) -> object:
        """ Insert(self: ChartCharacters, String: str) -> object """
        ...


class ChartColorFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ChartColorFormat) -> Application """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: ChartColorFormat) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ChartColorFormat) -> object """
        ...

    @property
    def RGB(self) -> int:
        """ Get: RGB(self: ChartColorFormat) -> int """
        ...

    @property
    def SchemeColor(self) -> int:
        """
        Get: SchemeColor(self: ChartColorFormat) -> int
        Set: SchemeColor(self: ChartColorFormat) = value
        """
        ...

    @property
    def Type(self) -> int:
        """ Get: Type(self: ChartColorFormat) -> int """
        ...

    @property
    def _Default(self) -> int:
        """ Get: _Default(self: ChartColorFormat) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ChartData: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsLinked(self) -> bool:
        """ Get: IsLinked(self: ChartData) -> bool """
        ...

    @property
    def Workbook(self) -> object:
        """ Get: Workbook(self: ChartData) -> object """
        ...


    def Activate(self): # -> 
        """ Activate(self: ChartData) """
        ...

    def ActivateChartDataWindow(self): # -> 
        """ ActivateChartDataWindow(self: ChartData) """
        ...

    def BreakLink(self): # -> 
        """ BreakLink(self: ChartData) """
        ...


class ChartFillFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ChartFillFormat) -> Application """
        ...

    @property
    def BackColor(self) -> ChartColorFormat:
        """ Get: BackColor(self: ChartFillFormat) -> ChartColorFormat """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: ChartFillFormat) -> int """
        ...

    @property
    def ForeColor(self) -> ChartColorFormat:
        """ Get: ForeColor(self: ChartFillFormat) -> ChartColorFormat """
        ...

    @property
    def GradientColorType(self): # -> MsoGradientColorType
        """ Get: GradientColorType(self: ChartFillFormat) -> MsoGradientColorType """
        ...

    @property
    def GradientDegree(self) -> Single:
        """ Get: GradientDegree(self: ChartFillFormat) -> Single """
        ...

    @property
    def GradientStyle(self): # -> MsoGradientStyle
        """ Get: GradientStyle(self: ChartFillFormat) -> MsoGradientStyle """
        ...

    @property
    def GradientVariant(self) -> int:
        """ Get: GradientVariant(self: ChartFillFormat) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ChartFillFormat) -> object """
        ...

    @property
    def Pattern(self): # -> MsoPatternType
        """ Get: Pattern(self: ChartFillFormat) -> MsoPatternType """
        ...

    @property
    def PresetGradientType(self): # -> MsoPresetGradientType
        """ Get: PresetGradientType(self: ChartFillFormat) -> MsoPresetGradientType """
        ...

    @property
    def PresetTexture(self): # -> MsoPresetTexture
        """ Get: PresetTexture(self: ChartFillFormat) -> MsoPresetTexture """
        ...

    @property
    def TextureName(self) -> str:
        """ Get: TextureName(self: ChartFillFormat) -> str """
        ...

    @property
    def TextureType(self): # -> MsoTextureType
        """ Get: TextureType(self: ChartFillFormat) -> MsoTextureType """
        ...

    @property
    def Type(self): # -> MsoFillType
        """ Get: Type(self: ChartFillFormat) -> MsoFillType """
        ...

    @property
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: ChartFillFormat) -> MsoTriState
        Set: Visible(self: ChartFillFormat) = value
        """
        ...


    def OneColorGradient(self, Style, Variant:int, Degree:Single): # ->  # Not found arg types: {'Style': 'MsoGradientStyle'}
        """ OneColorGradient(self: ChartFillFormat, Style: MsoGradientStyle, Variant: int, Degree: Single) """
        ...

    def Patterned(self, Pattern): # ->  # Not found arg types: {'Pattern': 'MsoPatternType'}
        """ Patterned(self: ChartFillFormat, Pattern: MsoPatternType) """
        ...

    def PresetGradient(self, Style, Variant:int, PresetGradientType): # ->  # Not found arg types: {'Style': 'MsoGradientStyle', 'PresetGradientType': 'MsoPresetGradientType'}
        """ PresetGradient(self: ChartFillFormat, Style: MsoGradientStyle, Variant: int, PresetGradientType: MsoPresetGradientType) """
        ...

    def PresetTextured(self, PresetTexture): # ->  # Not found arg types: {'PresetTexture': 'MsoPresetTexture'}
        """ PresetTextured(self: ChartFillFormat, PresetTexture: MsoPresetTexture) """
        ...

    def Solid(self): # -> 
        """ Solid(self: ChartFillFormat) """
        ...

    def TwoColorGradient(self, Style, Variant:int): # ->  # Not found arg types: {'Style': 'MsoGradientStyle'}
        """ TwoColorGradient(self: ChartFillFormat, Style: MsoGradientStyle, Variant: int) """
        ...

    def UserPicture(self, PictureFile:object, PictureFormat:object, PictureStackUnit:object, PicturePlacement:object): # -> 
        """ UserPicture(self: ChartFillFormat, PictureFile: object, PictureFormat: object, PictureStackUnit: object, PicturePlacement: object) """
        ...

    def UserTextured(self, TextureFile:str): # -> 
        """ UserTextured(self: ChartFillFormat, TextureFile: str) """
        ...


class ChartFont: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ChartFont) -> Application """
        ...

    @property
    def Background(self) -> object:
        """
        Get: Background(self: ChartFont) -> object
        Set: Background(self: ChartFont) = value
        """
        ...

    @property
    def Bold(self) -> object:
        """
        Get: Bold(self: ChartFont) -> object
        Set: Bold(self: ChartFont) = value
        """
        ...

    @property
    def Color(self) -> object:
        """
        Get: Color(self: ChartFont) -> object
        Set: Color(self: ChartFont) = value
        """
        ...

    @property
    def ColorIndex(self) -> object:
        """
        Get: ColorIndex(self: ChartFont) -> object
        Set: ColorIndex(self: ChartFont) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: ChartFont) -> int """
        ...

    @property
    def FontStyle(self) -> object:
        """
        Get: FontStyle(self: ChartFont) -> object
        Set: FontStyle(self: ChartFont) = value
        """
        ...

    @property
    def Italic(self) -> object:
        """
        Get: Italic(self: ChartFont) -> object
        Set: Italic(self: ChartFont) = value
        """
        ...

    @property
    def Name(self) -> object:
        """
        Get: Name(self: ChartFont) -> object
        Set: Name(self: ChartFont) = value
        """
        ...

    @property
    def OutlineFont(self) -> object:
        """
        Get: OutlineFont(self: ChartFont) -> object
        Set: OutlineFont(self: ChartFont) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ChartFont) -> object """
        ...

    @property
    def Shadow(self) -> object:
        """
        Get: Shadow(self: ChartFont) -> object
        Set: Shadow(self: ChartFont) = value
        """
        ...

    @property
    def Size(self) -> object:
        """
        Get: Size(self: ChartFont) -> object
        Set: Size(self: ChartFont) = value
        """
        ...

    @property
    def Strikethrough(self) -> object:
        """
        Get: Strikethrough(self: ChartFont) -> object
        Set: Strikethrough(self: ChartFont) = value
        """
        ...

    @property
    def Subscript(self) -> object:
        """
        Get: Subscript(self: ChartFont) -> object
        Set: Subscript(self: ChartFont) = value
        """
        ...

    @property
    def Superscript(self) -> object:
        """
        Get: Superscript(self: ChartFont) -> object
        Set: Superscript(self: ChartFont) = value
        """
        ...

    @property
    def Underline(self) -> object:
        """
        Get: Underline(self: ChartFont) -> object
        Set: Underline(self: ChartFont) = value
        """
        ...



class ChartFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Adjustments(self) -> Adjustments:
        """ Get: Adjustments(self: ChartFormat) -> Adjustments """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: ChartFormat) -> Application """
        ...

    @property
    def AutoShapeType(self): # -> MsoAutoShapeType
        """
        Get: AutoShapeType(self: ChartFormat) -> MsoAutoShapeType
        Set: AutoShapeType(self: ChartFormat) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: ChartFormat) -> int """
        ...

    @property
    def Fill(self) -> FillFormat:
        """ Get: Fill(self: ChartFormat) -> FillFormat """
        ...

    @property
    def Glow(self) -> GlowFormat:
        """ Get: Glow(self: ChartFormat) -> GlowFormat """
        ...

    @property
    def Line(self) -> LineFormat:
        """ Get: Line(self: ChartFormat) -> LineFormat """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ChartFormat) -> object """
        ...

    @property
    def PictureFormat(self) -> PictureFormat:
        """ Get: PictureFormat(self: ChartFormat) -> PictureFormat """
        ...

    @property
    def Shadow(self) -> ShadowFormat:
        """ Get: Shadow(self: ChartFormat) -> ShadowFormat """
        ...

    @property
    def SoftEdge(self) -> SoftEdgeFormat:
        """ Get: SoftEdge(self: ChartFormat) -> SoftEdgeFormat """
        ...

    @property
    def TextFrame2(self) -> TextFrame2:
        """ Get: TextFrame2(self: ChartFormat) -> TextFrame2 """
        ...

    @property
    def ThreeD(self) -> ThreeDFormat:
        """ Get: ThreeD(self: ChartFormat) -> ThreeDFormat """
        ...



class ChartGroup: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ChartGroup) -> Application """
        ...

    @property
    def AxisGroup(self) -> XlAxisGroup:
        """
        Get: AxisGroup(self: ChartGroup) -> XlAxisGroup
        Set: AxisGroup(self: ChartGroup) = value
        """
        ...

    @property
    def BubbleScale(self) -> int:
        """
        Get: BubbleScale(self: ChartGroup) -> int
        Set: BubbleScale(self: ChartGroup) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: ChartGroup) -> int """
        ...

    @property
    def DoughnutHoleSize(self) -> int:
        """
        Get: DoughnutHoleSize(self: ChartGroup) -> int
        Set: DoughnutHoleSize(self: ChartGroup) = value
        """
        ...

    @property
    def DownBars(self) -> DownBars:
        """ Get: DownBars(self: ChartGroup) -> DownBars """
        ...

    @property
    def DropLines(self) -> DropLines:
        """ Get: DropLines(self: ChartGroup) -> DropLines """
        ...

    @property
    def FirstSliceAngle(self) -> int:
        """
        Get: FirstSliceAngle(self: ChartGroup) -> int
        Set: FirstSliceAngle(self: ChartGroup) = value
        """
        ...

    @property
    def GapWidth(self) -> int:
        """
        Get: GapWidth(self: ChartGroup) -> int
        Set: GapWidth(self: ChartGroup) = value
        """
        ...

    @property
    def Has3DShading(self) -> bool:
        """
        Get: Has3DShading(self: ChartGroup) -> bool
        Set: Has3DShading(self: ChartGroup) = value
        """
        ...

    @property
    def HasDropLines(self) -> bool:
        """
        Get: HasDropLines(self: ChartGroup) -> bool
        Set: HasDropLines(self: ChartGroup) = value
        """
        ...

    @property
    def HasHiLoLines(self) -> bool:
        """
        Get: HasHiLoLines(self: ChartGroup) -> bool
        Set: HasHiLoLines(self: ChartGroup) = value
        """
        ...

    @property
    def HasRadarAxisLabels(self) -> bool:
        """
        Get: HasRadarAxisLabels(self: ChartGroup) -> bool
        Set: HasRadarAxisLabels(self: ChartGroup) = value
        """
        ...

    @property
    def HasSeriesLines(self) -> bool:
        """
        Get: HasSeriesLines(self: ChartGroup) -> bool
        Set: HasSeriesLines(self: ChartGroup) = value
        """
        ...

    @property
    def HasUpDownBars(self) -> bool:
        """
        Get: HasUpDownBars(self: ChartGroup) -> bool
        Set: HasUpDownBars(self: ChartGroup) = value
        """
        ...

    @property
    def HiLoLines(self) -> HiLoLines:
        """ Get: HiLoLines(self: ChartGroup) -> HiLoLines """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: ChartGroup) -> int """
        ...

    @property
    def Overlap(self) -> int:
        """
        Get: Overlap(self: ChartGroup) -> int
        Set: Overlap(self: ChartGroup) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ChartGroup) -> object """
        ...

    @property
    def RadarAxisLabels(self) -> TickLabels:
        """ Get: RadarAxisLabels(self: ChartGroup) -> TickLabels """
        ...

    @property
    def SecondPlotSize(self) -> int:
        """
        Get: SecondPlotSize(self: ChartGroup) -> int
        Set: SecondPlotSize(self: ChartGroup) = value
        """
        ...

    @property
    def SeriesLines(self) -> SeriesLines:
        """ Get: SeriesLines(self: ChartGroup) -> SeriesLines """
        ...

    @property
    def ShowNegativeBubbles(self) -> bool:
        """
        Get: ShowNegativeBubbles(self: ChartGroup) -> bool
        Set: ShowNegativeBubbles(self: ChartGroup) = value
        """
        ...

    @property
    def SizeRepresents(self) -> XlSizeRepresents:
        """
        Get: SizeRepresents(self: ChartGroup) -> XlSizeRepresents
        Set: SizeRepresents(self: ChartGroup) = value
        """
        ...

    @property
    def SplitType(self) -> XlChartSplitType:
        """
        Get: SplitType(self: ChartGroup) -> XlChartSplitType
        Set: SplitType(self: ChartGroup) = value
        """
        ...

    @property
    def SplitValue(self) -> object:
        """
        Get: SplitValue(self: ChartGroup) -> object
        Set: SplitValue(self: ChartGroup) = value
        """
        ...

    @property
    def Subtype(self) -> int:
        """
        Get: Subtype(self: ChartGroup) -> int
        Set: Subtype(self: ChartGroup) = value
        """
        ...

    @property
    def Type(self) -> int:
        """
        Get: Type(self: ChartGroup) -> int
        Set: Type(self: ChartGroup) = value
        """
        ...

    @property
    def UpBars(self) -> UpBars:
        """ Get: UpBars(self: ChartGroup) -> UpBars """
        ...

    @property
    def VaryByCategories(self) -> bool:
        """
        Get: VaryByCategories(self: ChartGroup) -> bool
        Set: VaryByCategories(self: ChartGroup) = value
        """
        ...


    def CategoryCollection(self, Index:object) -> object:
        """ CategoryCollection(self: ChartGroup, Index: object) -> object """
        ...

    def FullCategoryCollection(self, Index:object) -> object:
        """ FullCategoryCollection(self: ChartGroup, Index: object) -> object """
        ...

    def SeriesCollection(self, Index:object) -> object:
        """ SeriesCollection(self: ChartGroup, Index: object) -> object """
        ...


class ChartGroups(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ChartGroups) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ChartGroups) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: ChartGroups) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ChartGroups) -> object """
        ...


    def Item(self, Index:object) -> ChartGroup:
        """ Item(self: ChartGroups, Index: object) -> ChartGroup """
        ...


class ChartTitle: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ChartTitle) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: ChartTitle) -> object
        Set: AutoScaleFont(self: ChartTitle) = value
        """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: ChartTitle) -> ChartBorder """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: ChartTitle) -> str
        Set: Caption(self: ChartTitle) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: ChartTitle) -> int """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: ChartTitle) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> ChartFont:
        """ Get: Font(self: ChartTitle) -> ChartFont """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: ChartTitle) -> ChartFormat """
        ...

    @property
    def Formula(self) -> str:
        """
        Get: Formula(self: ChartTitle) -> str
        Set: Formula(self: ChartTitle) = value
        """
        ...

    @property
    def FormulaLocal(self) -> str:
        """
        Get: FormulaLocal(self: ChartTitle) -> str
        Set: FormulaLocal(self: ChartTitle) = value
        """
        ...

    @property
    def FormulaR1C1(self) -> str:
        """
        Get: FormulaR1C1(self: ChartTitle) -> str
        Set: FormulaR1C1(self: ChartTitle) = value
        """
        ...

    @property
    def FormulaR1C1Local(self) -> str:
        """
        Get: FormulaR1C1Local(self: ChartTitle) -> str
        Set: FormulaR1C1Local(self: ChartTitle) = value
        """
        ...

    @property
    def Height(self) -> float:
        """ Get: Height(self: ChartTitle) -> float """
        ...

    @property
    def HorizontalAlignment(self) -> object:
        """
        Get: HorizontalAlignment(self: ChartTitle) -> object
        Set: HorizontalAlignment(self: ChartTitle) = value
        """
        ...

    @property
    def IncludeInLayout(self) -> bool:
        """
        Get: IncludeInLayout(self: ChartTitle) -> bool
        Set: IncludeInLayout(self: ChartTitle) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: ChartTitle) -> Interior """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: ChartTitle) -> float
        Set: Left(self: ChartTitle) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ChartTitle) -> str """
        ...

    @property
    def Orientation(self) -> object:
        """
        Get: Orientation(self: ChartTitle) -> object
        Set: Orientation(self: ChartTitle) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ChartTitle) -> object """
        ...

    @property
    def Position(self) -> XlChartElementPosition:
        """
        Get: Position(self: ChartTitle) -> XlChartElementPosition
        Set: Position(self: ChartTitle) = value
        """
        ...

    @property
    def ReadingOrder(self) -> int:
        """
        Get: ReadingOrder(self: ChartTitle) -> int
        Set: ReadingOrder(self: ChartTitle) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: ChartTitle) -> bool
        Set: Shadow(self: ChartTitle) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: ChartTitle) -> str
        Set: Text(self: ChartTitle) = value
        """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: ChartTitle) -> float
        Set: Top(self: ChartTitle) = value
        """
        ...

    @property
    def VerticalAlignment(self) -> object:
        """
        Get: VerticalAlignment(self: ChartTitle) -> object
        Set: VerticalAlignment(self: ChartTitle) = value
        """
        ...

    @property
    def Width(self) -> float:
        """ Get: Width(self: ChartTitle) -> float """
        ...


    def Delete(self) -> object:
        """ Delete(self: ChartTitle) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: ChartTitle) -> object """
        ...


class Coauthoring: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Coauthoring) -> Application """
        ...

    @property
    def CoauthorCount(self) -> int:
        """ Get: CoauthorCount(self: Coauthoring) -> int """
        ...

    @property
    def FavorServerEditsDuringMerge(self) -> bool:
        """
        Get: FavorServerEditsDuringMerge(self: Coauthoring) -> bool
        Set: FavorServerEditsDuringMerge(self: Coauthoring) = value
        """
        ...

    @property
    def MergeMode(self) -> bool:
        """ Get: MergeMode(self: Coauthoring) -> bool """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Coauthoring) -> object """
        ...

    @property
    def PendingUpdates(self) -> bool:
        """ Get: PendingUpdates(self: Coauthoring) -> bool """
        ...


    def EndReview(self): # -> 
        """ EndReview(self: Coauthoring) """
        ...


class ColorEffect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ColorEffect) -> Application """
        ...

    @property
    def By(self) -> ColorFormat:
        """ Get: By(self: ColorEffect) -> ColorFormat """
        ...

    @property
    def From(self) -> ColorFormat:
        """ Get: From(self: ColorEffect) -> ColorFormat """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ColorEffect) -> object """
        ...

    @property
    def To(self) -> ColorFormat:
        """ Get: To(self: ColorEffect) -> ColorFormat """
        ...



class ColorFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: ColorFormat) -> object """
        ...

    @property
    def Brightness(self) -> Single:
        """
        Get: Brightness(self: ColorFormat) -> Single
        Set: Brightness(self: ColorFormat) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: ColorFormat) -> int """
        ...

    @property
    def ObjectThemeColor(self): # -> MsoThemeColorIndex
        """
        Get: ObjectThemeColor(self: ColorFormat) -> MsoThemeColorIndex
        Set: ObjectThemeColor(self: ColorFormat) = value
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
    def SchemeColor(self) -> PpColorSchemeIndex:
        """
        Get: SchemeColor(self: ColorFormat) -> PpColorSchemeIndex
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
    def Type(self): # -> MsoColorType
        """ Get: Type(self: ColorFormat) -> MsoColorType """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ColorScheme(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ColorScheme) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ColorScheme) -> object """
        ...


    def Delete(self): # -> 
        """ Delete(self: ColorScheme) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ColorSchemes(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ColorSchemes) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ColorSchemes) -> object """
        ...


    def Add(self, Scheme:ColorScheme) -> ColorScheme:
        """ Add(self: ColorSchemes, Scheme: ColorScheme) -> ColorScheme """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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
    def Width(self) -> Single:
        """
        Get: Width(self: Column) -> Single
        Set: Width(self: Column) = value
        """
        ...


    def Delete(self): # -> 
        """ Delete(self: Column) """
        ...

    def Select(self): # -> 
        """ Select(self: Column) """
        ...


class Columns(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Columns) -> Application """
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


class CommandEffect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: CommandEffect) -> Application """
        ...

    @property
    def bookmark(self) -> str:
        """
        Get: bookmark(self: CommandEffect) -> str
        Set: bookmark(self: CommandEffect) = value
        """
        ...

    @property
    def Command(self) -> str:
        """
        Get: Command(self: CommandEffect) -> str
        Set: Command(self: CommandEffect) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: CommandEffect) -> object """
        ...

    @property
    def Type(self) -> MsoAnimCommandType:
        """
        Get: Type(self: CommandEffect) -> MsoAnimCommandType
        Set: Type(self: CommandEffect) = value
        """
        ...



class Comment: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Comment) -> Application """
        ...

    @property
    def Author(self) -> str:
        """ Get: Author(self: Comment) -> str """
        ...

    @property
    def AuthorIndex(self) -> int:
        """ Get: AuthorIndex(self: Comment) -> int """
        ...

    @property
    def AuthorInitials(self) -> str:
        """ Get: AuthorInitials(self: Comment) -> str """
        ...

    @property
    def Collapsed(self) -> bool:
        """ Get: Collapsed(self: Comment) -> bool """
        ...

    @property
    def DateTime(self) -> DateTime:
        """ Get: DateTime(self: Comment) -> DateTime """
        ...

    @property
    def Left(self) -> Single:
        """ Get: Left(self: Comment) -> Single """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Comment) -> object """
        ...

    @property
    def ProviderID(self) -> str:
        """ Get: ProviderID(self: Comment) -> str """
        ...

    @property
    def Replies(self) -> Comments:
        """ Get: Replies(self: Comment) -> Comments """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: Comment) -> str """
        ...

    @property
    def TimeZoneBias(self) -> int:
        """ Get: TimeZoneBias(self: Comment) -> int """
        ...

    @property
    def Top(self) -> Single:
        """ Get: Top(self: Comment) -> Single """
        ...

    @property
    def UserID(self) -> str:
        """ Get: UserID(self: Comment) -> str """
        ...


    def Delete(self): # -> 
        """ Delete(self: Comment) """
        ...


class Comments(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Comments) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Comments) -> object """
        ...


    def Add(self, Left:Single, Top:Single, Author:str, AuthorInitials:str, Text:str) -> Comment:
        """ Add(self: Comments, Left: Single, Top: Single, Author: str, AuthorInitials: str, Text: str) -> Comment """
        ...

    def Add2(self, Left:Single, Top:Single, Author:str, AuthorInitials:str, Text:str, ProviderID:str, UserID:str) -> Comment:
        """ Add2(self: Comments, Left: Single, Top: Single, Author: str, AuthorInitials: str, Text: str, ProviderID: str, UserID: str) -> Comment """
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
    def Application(self) -> object:
        """ Get: Application(self: ConnectorFormat) -> object """
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
    def Creator(self) -> int:
        """ Get: Creator(self: ConnectorFormat) -> int """
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


class Corners: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Corners) -> Application """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Corners) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Corners) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Corners) -> object """
        ...


    def Select(self) -> object:
        """ Select(self: Corners) -> object """
        ...


class CustomerData(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: CustomerData) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: CustomerData) -> object """
        ...


    def Add(self): # -> CustomXMLPart
        """ Add(self: CustomerData) -> CustomXMLPart """
        ...

    def Delete(self, Id:str): # -> 
        """ Delete(self: CustomerData, Id: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class CustomLayout: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: CustomLayout) -> Application """
        ...

    @property
    def Background(self) -> ShapeRange:
        """ Get: Background(self: CustomLayout) -> ShapeRange """
        ...

    @property
    def CustomerData(self) -> CustomerData:
        """ Get: CustomerData(self: CustomLayout) -> CustomerData """
        ...

    @property
    def Design(self) -> Design:
        """ Get: Design(self: CustomLayout) -> Design """
        ...

    @property
    def DisplayMasterShapes(self): # -> MsoTriState
        """
        Get: DisplayMasterShapes(self: CustomLayout) -> MsoTriState
        Set: DisplayMasterShapes(self: CustomLayout) = value
        """
        ...

    @property
    def FollowMasterBackground(self): # -> MsoTriState
        """
        Get: FollowMasterBackground(self: CustomLayout) -> MsoTriState
        Set: FollowMasterBackground(self: CustomLayout) = value
        """
        ...

    @property
    def Guides(self) -> Guides:
        """ Get: Guides(self: CustomLayout) -> Guides """
        ...

    @property
    def HeadersFooters(self) -> HeadersFooters:
        """ Get: HeadersFooters(self: CustomLayout) -> HeadersFooters """
        ...

    @property
    def Height(self) -> Single:
        """ Get: Height(self: CustomLayout) -> Single """
        ...

    @property
    def Hyperlinks(self) -> Hyperlinks:
        """ Get: Hyperlinks(self: CustomLayout) -> Hyperlinks """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: CustomLayout) -> int """
        ...

    @property
    def MatchingName(self) -> str:
        """
        Get: MatchingName(self: CustomLayout) -> str
        Set: MatchingName(self: CustomLayout) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CustomLayout) -> str
        Set: Name(self: CustomLayout) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: CustomLayout) -> object """
        ...

    @property
    def Preserved(self): # -> MsoTriState
        """
        Get: Preserved(self: CustomLayout) -> MsoTriState
        Set: Preserved(self: CustomLayout) = value
        """
        ...

    @property
    def Shapes(self) -> Shapes:
        """ Get: Shapes(self: CustomLayout) -> Shapes """
        ...

    @property
    def SlideShowTransition(self) -> SlideShowTransition:
        """ Get: SlideShowTransition(self: CustomLayout) -> SlideShowTransition """
        ...

    @property
    def ThemeColorScheme(self): # -> ThemeColorScheme
        """ Get: ThemeColorScheme(self: CustomLayout) -> ThemeColorScheme """
        ...

    @property
    def TimeLine(self) -> TimeLine:
        """ Get: TimeLine(self: CustomLayout) -> TimeLine """
        ...

    @property
    def Width(self) -> Single:
        """ Get: Width(self: CustomLayout) -> Single """
        ...


    def Copy(self): # -> 
        """ Copy(self: CustomLayout) """
        ...

    def Cut(self): # -> 
        """ Cut(self: CustomLayout) """
        ...

    def Delete(self): # -> 
        """ Delete(self: CustomLayout) """
        ...

    def Duplicate(self) -> CustomLayout:
        """ Duplicate(self: CustomLayout) -> CustomLayout """
        ...

    def MoveTo(self, toPos:int): # -> 
        """ MoveTo(self: CustomLayout, toPos: int) """
        ...

    def Select(self): # -> 
        """ Select(self: CustomLayout) """
        ...


class CustomLayouts(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: CustomLayouts) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: CustomLayouts) -> object """
        ...


    def Add(self, Index:int) -> CustomLayout:
        """ Add(self: CustomLayouts, Index: int) -> CustomLayout """
        ...

    def Paste(self, Index:int) -> CustomLayout:
        """ Paste(self: CustomLayouts, Index: int) -> CustomLayout """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DataLabel: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: DataLabel) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: DataLabel) -> object
        Set: AutoScaleFont(self: DataLabel) = value
        """
        ...

    @property
    def AutoText(self) -> bool:
        """
        Get: AutoText(self: DataLabel) -> bool
        Set: AutoText(self: DataLabel) = value
        """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: DataLabel) -> ChartBorder """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: DataLabel) -> str
        Set: Caption(self: DataLabel) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: DataLabel) -> int """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: DataLabel) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> ChartFont:
        """ Get: Font(self: DataLabel) -> ChartFont """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: DataLabel) -> ChartFormat """
        ...

    @property
    def Formula(self) -> str:
        """
        Get: Formula(self: DataLabel) -> str
        Set: Formula(self: DataLabel) = value
        """
        ...

    @property
    def FormulaLocal(self) -> str:
        """
        Get: FormulaLocal(self: DataLabel) -> str
        Set: FormulaLocal(self: DataLabel) = value
        """
        ...

    @property
    def FormulaR1C1(self) -> str:
        """
        Get: FormulaR1C1(self: DataLabel) -> str
        Set: FormulaR1C1(self: DataLabel) = value
        """
        ...

    @property
    def FormulaR1C1Local(self) -> str:
        """
        Get: FormulaR1C1Local(self: DataLabel) -> str
        Set: FormulaR1C1Local(self: DataLabel) = value
        """
        ...

    @property
    def Height(self) -> float:
        """
        Get: Height(self: DataLabel) -> float
        Set: Height(self: DataLabel) = value
        """
        ...

    @property
    def HorizontalAlignment(self) -> object:
        """
        Get: HorizontalAlignment(self: DataLabel) -> object
        Set: HorizontalAlignment(self: DataLabel) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: DataLabel) -> Interior """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: DataLabel) -> float
        Set: Left(self: DataLabel) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DataLabel) -> str """
        ...

    @property
    def NumberFormat(self) -> str:
        """
        Get: NumberFormat(self: DataLabel) -> str
        Set: NumberFormat(self: DataLabel) = value
        """
        ...

    @property
    def NumberFormatLinked(self) -> bool:
        """
        Get: NumberFormatLinked(self: DataLabel) -> bool
        Set: NumberFormatLinked(self: DataLabel) = value
        """
        ...

    @property
    def NumberFormatLocal(self) -> object:
        """
        Get: NumberFormatLocal(self: DataLabel) -> object
        Set: NumberFormatLocal(self: DataLabel) = value
        """
        ...

    @property
    def Orientation(self) -> object:
        """
        Get: Orientation(self: DataLabel) -> object
        Set: Orientation(self: DataLabel) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: DataLabel) -> object """
        ...

    @property
    def Position(self) -> XlDataLabelPosition:
        """
        Get: Position(self: DataLabel) -> XlDataLabelPosition
        Set: Position(self: DataLabel) = value
        """
        ...

    @property
    def ReadingOrder(self) -> int:
        """
        Get: ReadingOrder(self: DataLabel) -> int
        Set: ReadingOrder(self: DataLabel) = value
        """
        ...

    @property
    def Separator(self) -> object:
        """
        Get: Separator(self: DataLabel) -> object
        Set: Separator(self: DataLabel) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: DataLabel) -> bool
        Set: Shadow(self: DataLabel) = value
        """
        ...

    @property
    def ShowBubbleSize(self) -> bool:
        """
        Get: ShowBubbleSize(self: DataLabel) -> bool
        Set: ShowBubbleSize(self: DataLabel) = value
        """
        ...

    @property
    def ShowCategoryName(self) -> bool:
        """
        Get: ShowCategoryName(self: DataLabel) -> bool
        Set: ShowCategoryName(self: DataLabel) = value
        """
        ...

    @property
    def ShowLegendKey(self) -> bool:
        """
        Get: ShowLegendKey(self: DataLabel) -> bool
        Set: ShowLegendKey(self: DataLabel) = value
        """
        ...

    @property
    def ShowPercentage(self) -> bool:
        """
        Get: ShowPercentage(self: DataLabel) -> bool
        Set: ShowPercentage(self: DataLabel) = value
        """
        ...

    @property
    def ShowRange(self) -> bool:
        """
        Get: ShowRange(self: DataLabel) -> bool
        Set: ShowRange(self: DataLabel) = value
        """
        ...

    @property
    def ShowSeriesName(self) -> bool:
        """
        Get: ShowSeriesName(self: DataLabel) -> bool
        Set: ShowSeriesName(self: DataLabel) = value
        """
        ...

    @property
    def ShowValue(self) -> bool:
        """
        Get: ShowValue(self: DataLabel) -> bool
        Set: ShowValue(self: DataLabel) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: DataLabel) -> str
        Set: Text(self: DataLabel) = value
        """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: DataLabel) -> float
        Set: Top(self: DataLabel) = value
        """
        ...

    @property
    def Type(self) -> object:
        """
        Get: Type(self: DataLabel) -> object
        Set: Type(self: DataLabel) = value
        """
        ...

    @property
    def VerticalAlignment(self) -> object:
        """
        Get: VerticalAlignment(self: DataLabel) -> object
        Set: VerticalAlignment(self: DataLabel) = value
        """
        ...

    @property
    def Width(self) -> float:
        """
        Get: Width(self: DataLabel) -> float
        Set: Width(self: DataLabel) = value
        """
        ...

    @property
    def _Height(self) -> float:
        """ Get: _Height(self: DataLabel) -> float """
        ...

    @property
    def _Width(self) -> float:
        """ Get: _Width(self: DataLabel) -> float """
        ...


    def Delete(self) -> object:
        """ Delete(self: DataLabel) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: DataLabel) -> object """
        ...


class DataLabels(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: DataLabels) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: DataLabels) -> object
        Set: AutoScaleFont(self: DataLabels) = value
        """
        ...

    @property
    def AutoText(self) -> bool:
        """
        Get: AutoText(self: DataLabels) -> bool
        Set: AutoText(self: DataLabels) = value
        """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: DataLabels) -> ChartBorder """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: DataLabels) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: DataLabels) -> int """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: DataLabels) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> ChartFont:
        """ Get: Font(self: DataLabels) -> ChartFont """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: DataLabels) -> ChartFormat """
        ...

    @property
    def HorizontalAlignment(self) -> object:
        """
        Get: HorizontalAlignment(self: DataLabels) -> object
        Set: HorizontalAlignment(self: DataLabels) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: DataLabels) -> Interior """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DataLabels) -> str """
        ...

    @property
    def NumberFormat(self) -> str:
        """
        Get: NumberFormat(self: DataLabels) -> str
        Set: NumberFormat(self: DataLabels) = value
        """
        ...

    @property
    def NumberFormatLinked(self) -> bool:
        """
        Get: NumberFormatLinked(self: DataLabels) -> bool
        Set: NumberFormatLinked(self: DataLabels) = value
        """
        ...

    @property
    def NumberFormatLocal(self) -> object:
        """
        Get: NumberFormatLocal(self: DataLabels) -> object
        Set: NumberFormatLocal(self: DataLabels) = value
        """
        ...

    @property
    def Orientation(self) -> object:
        """
        Get: Orientation(self: DataLabels) -> object
        Set: Orientation(self: DataLabels) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: DataLabels) -> object """
        ...

    @property
    def Position(self) -> XlDataLabelPosition:
        """
        Get: Position(self: DataLabels) -> XlDataLabelPosition
        Set: Position(self: DataLabels) = value
        """
        ...

    @property
    def ReadingOrder(self) -> int:
        """
        Get: ReadingOrder(self: DataLabels) -> int
        Set: ReadingOrder(self: DataLabels) = value
        """
        ...

    @property
    def Separator(self) -> object:
        """
        Get: Separator(self: DataLabels) -> object
        Set: Separator(self: DataLabels) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: DataLabels) -> bool
        Set: Shadow(self: DataLabels) = value
        """
        ...

    @property
    def ShowBubbleSize(self) -> bool:
        """
        Get: ShowBubbleSize(self: DataLabels) -> bool
        Set: ShowBubbleSize(self: DataLabels) = value
        """
        ...

    @property
    def ShowCategoryName(self) -> bool:
        """
        Get: ShowCategoryName(self: DataLabels) -> bool
        Set: ShowCategoryName(self: DataLabels) = value
        """
        ...

    @property
    def ShowLegendKey(self) -> bool:
        """
        Get: ShowLegendKey(self: DataLabels) -> bool
        Set: ShowLegendKey(self: DataLabels) = value
        """
        ...

    @property
    def ShowPercentage(self) -> bool:
        """
        Get: ShowPercentage(self: DataLabels) -> bool
        Set: ShowPercentage(self: DataLabels) = value
        """
        ...

    @property
    def ShowRange(self) -> bool:
        """
        Get: ShowRange(self: DataLabels) -> bool
        Set: ShowRange(self: DataLabels) = value
        """
        ...

    @property
    def ShowSeriesName(self) -> bool:
        """
        Get: ShowSeriesName(self: DataLabels) -> bool
        Set: ShowSeriesName(self: DataLabels) = value
        """
        ...

    @property
    def ShowValue(self) -> bool:
        """
        Get: ShowValue(self: DataLabels) -> bool
        Set: ShowValue(self: DataLabels) = value
        """
        ...

    @property
    def Type(self) -> object:
        """
        Get: Type(self: DataLabels) -> object
        Set: Type(self: DataLabels) = value
        """
        ...

    @property
    def VerticalAlignment(self) -> object:
        """
        Get: VerticalAlignment(self: DataLabels) -> object
        Set: VerticalAlignment(self: DataLabels) = value
        """
        ...


    def Delete(self) -> object:
        """ Delete(self: DataLabels) -> object """
        ...

    def Item(self, Index:object) -> DataLabel:
        """ Item(self: DataLabels, Index: object) -> DataLabel """
        ...

    def Propagate(self, Index:object): # -> 
        """ Propagate(self: DataLabels, Index: object) """
        ...

    def Select(self) -> object:
        """ Select(self: DataLabels) -> object """
        ...

    def _Default(self, Index:object) -> DataLabel:
        """ _Default(self: DataLabels, Index: object) -> DataLabel """
        ...


class DataTable: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: DataTable) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: DataTable) -> object
        Set: AutoScaleFont(self: DataTable) = value
        """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: DataTable) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: DataTable) -> int """
        ...

    @property
    def Font(self) -> ChartFont:
        """ Get: Font(self: DataTable) -> ChartFont """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: DataTable) -> ChartFormat """
        ...

    @property
    def HasBorderHorizontal(self) -> bool:
        """
        Get: HasBorderHorizontal(self: DataTable) -> bool
        Set: HasBorderHorizontal(self: DataTable) = value
        """
        ...

    @property
    def HasBorderOutline(self) -> bool:
        """
        Get: HasBorderOutline(self: DataTable) -> bool
        Set: HasBorderOutline(self: DataTable) = value
        """
        ...

    @property
    def HasBorderVertical(self) -> bool:
        """
        Get: HasBorderVertical(self: DataTable) -> bool
        Set: HasBorderVertical(self: DataTable) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: DataTable) -> object """
        ...

    @property
    def ShowLegendKey(self) -> bool:
        """
        Get: ShowLegendKey(self: DataTable) -> bool
        Set: ShowLegendKey(self: DataTable) = value
        """
        ...


    def Delete(self): # -> 
        """ Delete(self: DataTable) """
        ...

    def Select(self): # -> 
        """ Select(self: DataTable) """
        ...


class DefaultWebOptions: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AllowPNG(self): # -> MsoTriState
        """
        Get: AllowPNG(self: DefaultWebOptions) -> MsoTriState
        Set: AllowPNG(self: DefaultWebOptions) = value
        """
        ...

    @property
    def AlwaysSaveInDefaultEncoding(self): # -> MsoTriState
        """
        Get: AlwaysSaveInDefaultEncoding(self: DefaultWebOptions) -> MsoTriState
        Set: AlwaysSaveInDefaultEncoding(self: DefaultWebOptions) = value
        """
        ...

    @property
    def CheckIfOfficeIsHTMLEditor(self): # -> MsoTriState
        """
        Get: CheckIfOfficeIsHTMLEditor(self: DefaultWebOptions) -> MsoTriState
        Set: CheckIfOfficeIsHTMLEditor(self: DefaultWebOptions) = value
        """
        ...

    @property
    def Encoding(self): # -> MsoEncoding
        """
        Get: Encoding(self: DefaultWebOptions) -> MsoEncoding
        Set: Encoding(self: DefaultWebOptions) = value
        """
        ...

    @property
    def FolderSuffix(self) -> str:
        """ Get: FolderSuffix(self: DefaultWebOptions) -> str """
        ...

    @property
    def Fonts(self): # -> WebPageFonts
        """ Get: Fonts(self: DefaultWebOptions) -> WebPageFonts """
        ...

    @property
    def FrameColors(self) -> PpFrameColors:
        """
        Get: FrameColors(self: DefaultWebOptions) -> PpFrameColors
        Set: FrameColors(self: DefaultWebOptions) = value
        """
        ...

    @property
    def HTMLVersion(self) -> PpHTMLVersion:
        """
        Get: HTMLVersion(self: DefaultWebOptions) -> PpHTMLVersion
        Set: HTMLVersion(self: DefaultWebOptions) = value
        """
        ...

    @property
    def IncludeNavigation(self): # -> MsoTriState
        """
        Get: IncludeNavigation(self: DefaultWebOptions) -> MsoTriState
        Set: IncludeNavigation(self: DefaultWebOptions) = value
        """
        ...

    @property
    def OrganizeInFolder(self): # -> MsoTriState
        """
        Get: OrganizeInFolder(self: DefaultWebOptions) -> MsoTriState
        Set: OrganizeInFolder(self: DefaultWebOptions) = value
        """
        ...

    @property
    def RelyOnVML(self): # -> MsoTriState
        """
        Get: RelyOnVML(self: DefaultWebOptions) -> MsoTriState
        Set: RelyOnVML(self: DefaultWebOptions) = value
        """
        ...

    @property
    def ResizeGraphics(self): # -> MsoTriState
        """
        Get: ResizeGraphics(self: DefaultWebOptions) -> MsoTriState
        Set: ResizeGraphics(self: DefaultWebOptions) = value
        """
        ...

    @property
    def SaveNewWebPagesAsWebArchives(self): # -> MsoTriState
        """
        Get: SaveNewWebPagesAsWebArchives(self: DefaultWebOptions) -> MsoTriState
        Set: SaveNewWebPagesAsWebArchives(self: DefaultWebOptions) = value
        """
        ...

    @property
    def ScreenSize(self): # -> MsoScreenSize
        """
        Get: ScreenSize(self: DefaultWebOptions) -> MsoScreenSize
        Set: ScreenSize(self: DefaultWebOptions) = value
        """
        ...

    @property
    def ShowSlideAnimation(self): # -> MsoTriState
        """
        Get: ShowSlideAnimation(self: DefaultWebOptions) -> MsoTriState
        Set: ShowSlideAnimation(self: DefaultWebOptions) = value
        """
        ...

    @property
    def TargetBrowser(self): # -> MsoTargetBrowser
        """
        Get: TargetBrowser(self: DefaultWebOptions) -> MsoTargetBrowser
        Set: TargetBrowser(self: DefaultWebOptions) = value
        """
        ...

    @property
    def UpdateLinksOnSave(self): # -> MsoTriState
        """
        Get: UpdateLinksOnSave(self: DefaultWebOptions) -> MsoTriState
        Set: UpdateLinksOnSave(self: DefaultWebOptions) = value
        """
        ...

    @property
    def UseLongFileNames(self): # -> MsoTriState
        """
        Get: UseLongFileNames(self: DefaultWebOptions) -> MsoTriState
        Set: UseLongFileNames(self: DefaultWebOptions) = value
        """
        ...



class Design: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Design) -> Application """
        ...

    @property
    def HasTitleMaster(self): # -> MsoTriState
        """ Get: HasTitleMaster(self: Design) -> MsoTriState """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: Design) -> int """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Design) -> str
        Set: Name(self: Design) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Design) -> object """
        ...

    @property
    def Preserved(self): # -> MsoTriState
        """
        Get: Preserved(self: Design) -> MsoTriState
        Set: Preserved(self: Design) = value
        """
        ...

    @property
    def SlideMaster(self) -> Master:
        """ Get: SlideMaster(self: Design) -> Master """
        ...

    @property
    def TitleMaster(self) -> Master:
        """ Get: TitleMaster(self: Design) -> Master """
        ...


    def AddTitleMaster(self) -> Master:
        """ AddTitleMaster(self: Design) -> Master """
        ...

    def Delete(self): # -> 
        """ Delete(self: Design) """
        ...

    def MoveTo(self, toPos:int): # -> 
        """ MoveTo(self: Design, toPos: int) """
        ...


class Designs(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Designs) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Designs) -> object """
        ...


    def Add(self, designName:str, Index:int) -> Design:
        """ Add(self: Designs, designName: str, Index: int) -> Design """
        ...

    def Clone(self, pOriginal:Design, Index:int) -> Design:
        """ Clone(self: Designs, pOriginal: Design, Index: int) -> Design """
        ...

    def Load(self, TemplateName:str, Index:int) -> Design:
        """ Load(self: Designs, TemplateName: str, Index: int) -> Design """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Diagram: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: Diagram) -> object """
        ...

    @property
    def AutoFormat(self): # -> MsoTriState
        """
        Get: AutoFormat(self: Diagram) -> MsoTriState
        Set: AutoFormat(self: Diagram) = value
        """
        ...

    @property
    def AutoLayout(self): # -> MsoTriState
        """
        Get: AutoLayout(self: Diagram) -> MsoTriState
        Set: AutoLayout(self: Diagram) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Diagram) -> int """
        ...

    @property
    def Nodes(self) -> DiagramNodes:
        """ Get: Nodes(self: Diagram) -> DiagramNodes """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Diagram) -> object """
        ...

    @property
    def Reverse(self): # -> MsoTriState
        """
        Get: Reverse(self: Diagram) -> MsoTriState
        Set: Reverse(self: Diagram) = value
        """
        ...

    @property
    def Type(self): # -> MsoDiagramType
        """ Get: Type(self: Diagram) -> MsoDiagramType """
        ...


    def Convert(self, Type): # ->  # Not found arg types: {'Type': 'MsoDiagramType'}
        """ Convert(self: Diagram, Type: MsoDiagramType) """
        ...

    def FitText(self): # -> 
        """ FitText(self: Diagram) """
        ...


class DiagramNode: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: DiagramNode) -> object """
        ...

    @property
    def Children(self) -> DiagramNodeChildren:
        """ Get: Children(self: DiagramNode) -> DiagramNodeChildren """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: DiagramNode) -> int """
        ...

    @property
    def Diagram(self) -> Diagram:
        """ Get: Diagram(self: DiagramNode) -> Diagram """
        ...

    @property
    def Layout(self): # -> MsoOrgChartLayoutType
        """
        Get: Layout(self: DiagramNode) -> MsoOrgChartLayoutType
        Set: Layout(self: DiagramNode) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: DiagramNode) -> object """
        ...

    @property
    def Root(self) -> DiagramNode:
        """ Get: Root(self: DiagramNode) -> DiagramNode """
        ...

    @property
    def Shape(self) -> Shape:
        """ Get: Shape(self: DiagramNode) -> Shape """
        ...

    @property
    def TextShape(self) -> Shape:
        """ Get: TextShape(self: DiagramNode) -> Shape """
        ...


    def AddNode(self, Pos, NodeType) -> DiagramNode: # Not found arg types: {'Pos': 'MsoRelativeNodePosition', 'NodeType': 'MsoDiagramNodeType'}
        """ AddNode(self: DiagramNode, Pos: MsoRelativeNodePosition, NodeType: MsoDiagramNodeType) -> DiagramNode """
        ...

    def CloneNode(self, CopyChildren:bool, TargetNode:DiagramNode, Pos) -> DiagramNode: # Not found arg types: {'Pos': 'MsoRelativeNodePosition'}
        """ CloneNode(self: DiagramNode, CopyChildren: bool, TargetNode: DiagramNode, Pos: MsoRelativeNodePosition) -> DiagramNode """
        ...

    def Delete(self): # -> 
        """ Delete(self: DiagramNode) """
        ...

    def MoveNode(self, TargetNode:DiagramNode, Pos): # ->  # Not found arg types: {'Pos': 'MsoRelativeNodePosition'}
        """ MoveNode(self: DiagramNode, TargetNode: DiagramNode, Pos: MsoRelativeNodePosition) """
        ...

    def NextNode(self) -> DiagramNode:
        """ NextNode(self: DiagramNode) -> DiagramNode """
        ...

    def PrevNode(self) -> DiagramNode:
        """ PrevNode(self: DiagramNode) -> DiagramNode """
        ...

    def ReplaceNode(self, TargetNode:DiagramNode): # -> 
        """ ReplaceNode(self: DiagramNode, TargetNode: DiagramNode) """
        ...

    def SwapNode(self, TargetNode:DiagramNode, SwapChildren:bool): # -> 
        """ SwapNode(self: DiagramNode, TargetNode: DiagramNode, SwapChildren: bool) """
        ...

    def TransferChildren(self, ReceivingNode:DiagramNode): # -> 
        """ TransferChildren(self: DiagramNode, ReceivingNode: DiagramNode) """
        ...


class DiagramNodeChildren(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: DiagramNodeChildren) -> object """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: DiagramNodeChildren) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: DiagramNodeChildren) -> int """
        ...

    @property
    def FirstChild(self) -> DiagramNode:
        """ Get: FirstChild(self: DiagramNodeChildren) -> DiagramNode """
        ...

    @property
    def LastChild(self) -> DiagramNode:
        """ Get: LastChild(self: DiagramNodeChildren) -> DiagramNode """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: DiagramNodeChildren) -> object """
        ...


    def AddNode(self, Index:object, NodeType) -> DiagramNode: # Not found arg types: {'NodeType': 'MsoDiagramNodeType'}
        """ AddNode(self: DiagramNodeChildren, Index: object, NodeType: MsoDiagramNodeType) -> DiagramNode """
        ...

    def SelectAll(self): # -> 
        """ SelectAll(self: DiagramNodeChildren) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DiagramNodes(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: DiagramNodes) -> object """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: DiagramNodes) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: DiagramNodes) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: DiagramNodes) -> object """
        ...


    def SelectAll(self): # -> 
        """ SelectAll(self: DiagramNodes) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DisplayUnitLabel: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: DisplayUnitLabel) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: DisplayUnitLabel) -> object
        Set: AutoScaleFont(self: DisplayUnitLabel) = value
        """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: DisplayUnitLabel) -> ChartBorder """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: DisplayUnitLabel) -> str
        Set: Caption(self: DisplayUnitLabel) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: DisplayUnitLabel) -> int """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: DisplayUnitLabel) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> ChartFont:
        """ Get: Font(self: DisplayUnitLabel) -> ChartFont """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: DisplayUnitLabel) -> ChartFormat """
        ...

    @property
    def Formula(self) -> str:
        """
        Get: Formula(self: DisplayUnitLabel) -> str
        Set: Formula(self: DisplayUnitLabel) = value
        """
        ...

    @property
    def FormulaLocal(self) -> str:
        """
        Get: FormulaLocal(self: DisplayUnitLabel) -> str
        Set: FormulaLocal(self: DisplayUnitLabel) = value
        """
        ...

    @property
    def FormulaR1C1(self) -> str:
        """
        Get: FormulaR1C1(self: DisplayUnitLabel) -> str
        Set: FormulaR1C1(self: DisplayUnitLabel) = value
        """
        ...

    @property
    def FormulaR1C1Local(self) -> str:
        """
        Get: FormulaR1C1Local(self: DisplayUnitLabel) -> str
        Set: FormulaR1C1Local(self: DisplayUnitLabel) = value
        """
        ...

    @property
    def Height(self) -> float:
        """ Get: Height(self: DisplayUnitLabel) -> float """
        ...

    @property
    def HorizontalAlignment(self) -> object:
        """
        Get: HorizontalAlignment(self: DisplayUnitLabel) -> object
        Set: HorizontalAlignment(self: DisplayUnitLabel) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: DisplayUnitLabel) -> Interior """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: DisplayUnitLabel) -> float
        Set: Left(self: DisplayUnitLabel) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DisplayUnitLabel) -> str """
        ...

    @property
    def Orientation(self) -> object:
        """
        Get: Orientation(self: DisplayUnitLabel) -> object
        Set: Orientation(self: DisplayUnitLabel) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: DisplayUnitLabel) -> object """
        ...

    @property
    def Position(self) -> XlChartElementPosition:
        """
        Get: Position(self: DisplayUnitLabel) -> XlChartElementPosition
        Set: Position(self: DisplayUnitLabel) = value
        """
        ...

    @property
    def ReadingOrder(self) -> int:
        """
        Get: ReadingOrder(self: DisplayUnitLabel) -> int
        Set: ReadingOrder(self: DisplayUnitLabel) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: DisplayUnitLabel) -> bool
        Set: Shadow(self: DisplayUnitLabel) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: DisplayUnitLabel) -> str
        Set: Text(self: DisplayUnitLabel) = value
        """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: DisplayUnitLabel) -> float
        Set: Top(self: DisplayUnitLabel) = value
        """
        ...

    @property
    def VerticalAlignment(self) -> object:
        """
        Get: VerticalAlignment(self: DisplayUnitLabel) -> object
        Set: VerticalAlignment(self: DisplayUnitLabel) = value
        """
        ...

    @property
    def Width(self) -> float:
        """ Get: Width(self: DisplayUnitLabel) -> float """
        ...


    def Delete(self) -> object:
        """ Delete(self: DisplayUnitLabel) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: DisplayUnitLabel) -> object """
        ...


class DocumentWindow: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Active(self): # -> MsoTriState
        """ Get: Active(self: DocumentWindow) -> MsoTriState """
        ...

    @property
    def ActivePane(self) -> Pane:
        """ Get: ActivePane(self: DocumentWindow) -> Pane """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: DocumentWindow) -> Application """
        ...

    @property
    def BlackAndWhite(self): # -> MsoTriState
        """
        Get: BlackAndWhite(self: DocumentWindow) -> MsoTriState
        Set: BlackAndWhite(self: DocumentWindow) = value
        """
        ...

    @property
    def Caption(self) -> str:
        """ Get: Caption(self: DocumentWindow) -> str """
        ...

    @property
    def Height(self) -> Single:
        """
        Get: Height(self: DocumentWindow) -> Single
        Set: Height(self: DocumentWindow) = value
        """
        ...

    @property
    def HWND(self) -> int:
        """ Get: HWND(self: DocumentWindow) -> int """
        ...

    @property
    def Left(self) -> Single:
        """
        Get: Left(self: DocumentWindow) -> Single
        Set: Left(self: DocumentWindow) = value
        """
        ...

    @property
    def Panes(self) -> Panes:
        """ Get: Panes(self: DocumentWindow) -> Panes """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: DocumentWindow) -> object """
        ...

    @property
    def Presentation(self) -> Presentation:
        """ Get: Presentation(self: DocumentWindow) -> Presentation """
        ...

    @property
    def Selection(self) -> Selection:
        """ Get: Selection(self: DocumentWindow) -> Selection """
        ...

    @property
    def SplitHorizontal(self) -> int:
        """
        Get: SplitHorizontal(self: DocumentWindow) -> int
        Set: SplitHorizontal(self: DocumentWindow) = value
        """
        ...

    @property
    def SplitVertical(self) -> int:
        """
        Get: SplitVertical(self: DocumentWindow) -> int
        Set: SplitVertical(self: DocumentWindow) = value
        """
        ...

    @property
    def Top(self) -> Single:
        """
        Get: Top(self: DocumentWindow) -> Single
        Set: Top(self: DocumentWindow) = value
        """
        ...

    @property
    def View(self) -> View:
        """ Get: View(self: DocumentWindow) -> View """
        ...

    @property
    def ViewType(self) -> PpViewType:
        """
        Get: ViewType(self: DocumentWindow) -> PpViewType
        Set: ViewType(self: DocumentWindow) = value
        """
        ...

    @property
    def Width(self) -> Single:
        """
        Get: Width(self: DocumentWindow) -> Single
        Set: Width(self: DocumentWindow) = value
        """
        ...

    @property
    def WindowState(self) -> PpWindowState:
        """
        Get: WindowState(self: DocumentWindow) -> PpWindowState
        Set: WindowState(self: DocumentWindow) = value
        """
        ...


    def Activate(self): # -> 
        """ Activate(self: DocumentWindow) """
        ...

    def Close(self): # -> 
        """ Close(self: DocumentWindow) """
        ...

    def ExpandSection(self, sectionIndex:int, Expand:bool): # -> 
        """ ExpandSection(self: DocumentWindow, sectionIndex: int, Expand: bool) """
        ...

    def FitToPage(self): # -> 
        """ FitToPage(self: DocumentWindow) """
        ...

    def IsSectionExpanded(self, sectionIndex:int) -> bool:
        """ IsSectionExpanded(self: DocumentWindow, sectionIndex: int) -> bool """
        ...

    def LargeScroll(self, Down:int, Up:int, ToRight:int, ToLeft:int): # -> 
        """ LargeScroll(self: DocumentWindow, Down: int, Up: int, ToRight: int, ToLeft: int) """
        ...

    def NewWindow(self) -> DocumentWindow:
        """ NewWindow(self: DocumentWindow) -> DocumentWindow """
        ...

    def PointsToScreenPixelsX(self, Points:Single) -> int:
        """ PointsToScreenPixelsX(self: DocumentWindow, Points: Single) -> int """
        ...

    def PointsToScreenPixelsY(self, Points:Single) -> int:
        """ PointsToScreenPixelsY(self: DocumentWindow, Points: Single) -> int """
        ...

    def RangeFromPoint(self, X:int, Y:int) -> object:
        """ RangeFromPoint(self: DocumentWindow, X: int, Y: int) -> object """
        ...

    def ScrollIntoView(self, Left:Single, Top:Single, Width:Single, Height:Single, Start): # ->  # Not found arg types: {'Start': 'MsoTriState'}
        """ ScrollIntoView(self: DocumentWindow, Left: Single, Top: Single, Width: Single, Height: Single, Start: MsoTriState) """
        ...

    def SmallScroll(self, Down:int, Up:int, ToRight:int, ToLeft:int): # -> 
        """ SmallScroll(self: DocumentWindow, Down: int, Up: int, ToRight: int, ToLeft: int) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DocumentWindows(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: DocumentWindows) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: DocumentWindows) -> object """
        ...


    def Arrange(self, arrangeStyle:PpArrangeStyle): # -> 
        """ Arrange(self: DocumentWindows, arrangeStyle: PpArrangeStyle) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DownBars: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: DownBars) -> Application """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: DownBars) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: DownBars) -> int """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: DownBars) -> ChartFillFormat """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: DownBars) -> ChartFormat """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: DownBars) -> Interior """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DownBars) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: DownBars) -> object """
        ...


    def Delete(self) -> object:
        """ Delete(self: DownBars) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: DownBars) -> object """
        ...


class DropLines: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: DropLines) -> Application """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: DropLines) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: DropLines) -> int """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: DropLines) -> ChartFormat """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DropLines) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: DropLines) -> object """
        ...


    def Delete(self) -> object:
        """ Delete(self: DropLines) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: DropLines) -> object """
        ...


class EApplication: # skipped bases: <type 'object'>
    """ no doc """
    def AfterDragDropOnSlide(self, Sld:Slide, X:Single, Y:Single): # -> 
        """ AfterDragDropOnSlide(self: EApplication, Sld: Slide, X: Single, Y: Single) """
        ...

    def AfterNewPresentation(self, Pres:Presentation): # -> 
        """ AfterNewPresentation(self: EApplication, Pres: Presentation) """
        ...

    def AfterPresentationOpen(self, Pres:Presentation): # -> 
        """ AfterPresentationOpen(self: EApplication, Pres: Presentation) """
        ...

    def AfterShapeSizeChange(self, shp:Shape): # -> 
        """ AfterShapeSizeChange(self: EApplication, shp: Shape) """
        ...

    def ColorSchemeChanged(self, SldRange:SlideRange): # -> 
        """ ColorSchemeChanged(self: EApplication, SldRange: SlideRange) """
        ...

    def NewPresentation(self, Pres:Presentation): # -> 
        """ NewPresentation(self: EApplication, Pres: Presentation) """
        ...

    def PresentationBeforeClose(self, Pres, Cancel) -> bool:
        """ PresentationBeforeClose(self: EApplication, Pres: Presentation) -> bool """
        ...

    def PresentationBeforeSave(self, Pres, Cancel) -> bool:
        """ PresentationBeforeSave(self: EApplication, Pres: Presentation) -> bool """
        ...

    def PresentationClose(self, Pres:Presentation): # -> 
        """ PresentationClose(self: EApplication, Pres: Presentation) """
        ...

    def PresentationCloseFinal(self, Pres:Presentation): # -> 
        """ PresentationCloseFinal(self: EApplication, Pres: Presentation) """
        ...

    def PresentationNewSlide(self, Sld:Slide): # -> 
        """ PresentationNewSlide(self: EApplication, Sld: Slide) """
        ...

    def PresentationOpen(self, Pres:Presentation): # -> 
        """ PresentationOpen(self: EApplication, Pres: Presentation) """
        ...

    def PresentationPrint(self, Pres:Presentation): # -> 
        """ PresentationPrint(self: EApplication, Pres: Presentation) """
        ...

    def PresentationSave(self, Pres:Presentation): # -> 
        """ PresentationSave(self: EApplication, Pres: Presentation) """
        ...

    def PresentationSync(self, Pres:Presentation, SyncEventType): # ->  # Not found arg types: {'SyncEventType': 'MsoSyncEventType'}
        """ PresentationSync(self: EApplication, Pres: Presentation, SyncEventType: MsoSyncEventType) """
        ...

    def ProtectedViewWindowActivate(self, ProtViewWindow:ProtectedViewWindow): # -> 
        """ ProtectedViewWindowActivate(self: EApplication, ProtViewWindow: ProtectedViewWindow) """
        ...

    def ProtectedViewWindowBeforeClose(self, ProtViewWindow, ProtectedViewCloseReason, Cancel) -> bool:
        """ ProtectedViewWindowBeforeClose(self: EApplication, ProtViewWindow: ProtectedViewWindow, ProtectedViewCloseReason: PpProtectedViewCloseReason) -> bool """
        ...

    def ProtectedViewWindowBeforeEdit(self, ProtViewWindow, Cancel) -> bool:
        """ ProtectedViewWindowBeforeEdit(self: EApplication, ProtViewWindow: ProtectedViewWindow) -> bool """
        ...

    def ProtectedViewWindowDeactivate(self, ProtViewWindow:ProtectedViewWindow): # -> 
        """ ProtectedViewWindowDeactivate(self: EApplication, ProtViewWindow: ProtectedViewWindow) """
        ...

    def ProtectedViewWindowOpen(self, ProtViewWindow:ProtectedViewWindow): # -> 
        """ ProtectedViewWindowOpen(self: EApplication, ProtViewWindow: ProtectedViewWindow) """
        ...

    def SlideSelectionChanged(self, SldRange:SlideRange): # -> 
        """ SlideSelectionChanged(self: EApplication, SldRange: SlideRange) """
        ...

    def SlideShowBegin(self, Wn:SlideShowWindow): # -> 
        """ SlideShowBegin(self: EApplication, Wn: SlideShowWindow) """
        ...

    def SlideShowEnd(self, Pres:Presentation): # -> 
        """ SlideShowEnd(self: EApplication, Pres: Presentation) """
        ...

    def SlideShowNextBuild(self, Wn:SlideShowWindow): # -> 
        """ SlideShowNextBuild(self: EApplication, Wn: SlideShowWindow) """
        ...

    def SlideShowNextClick(self, Wn:SlideShowWindow, nEffect:Effect): # -> 
        """ SlideShowNextClick(self: EApplication, Wn: SlideShowWindow, nEffect: Effect) """
        ...

    def SlideShowNextSlide(self, Wn:SlideShowWindow): # -> 
        """ SlideShowNextSlide(self: EApplication, Wn: SlideShowWindow) """
        ...

    def SlideShowOnNext(self, Wn:SlideShowWindow): # -> 
        """ SlideShowOnNext(self: EApplication, Wn: SlideShowWindow) """
        ...

    def SlideShowOnPrevious(self, Wn:SlideShowWindow): # -> 
        """ SlideShowOnPrevious(self: EApplication, Wn: SlideShowWindow) """
        ...

    def WindowActivate(self, Pres:Presentation, Wn:DocumentWindow): # -> 
        """ WindowActivate(self: EApplication, Pres: Presentation, Wn: DocumentWindow) """
        ...

    def WindowBeforeDoubleClick(self, Sel, Cancel) -> bool:
        """ WindowBeforeDoubleClick(self: EApplication, Sel: Selection) -> bool """
        ...

    def WindowBeforeRightClick(self, Sel, Cancel) -> bool:
        """ WindowBeforeRightClick(self: EApplication, Sel: Selection) -> bool """
        ...

    def WindowDeactivate(self, Pres:Presentation, Wn:DocumentWindow): # -> 
        """ WindowDeactivate(self: EApplication, Pres: Presentation, Wn: DocumentWindow) """
        ...

    def WindowSelectionChange(self, Sel:Selection): # -> 
        """ WindowSelectionChange(self: EApplication, Sel: Selection) """
        ...


class EApplication_AfterDragDropOnSlideEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_AfterDragDropOnSlideEventHandler(: object, : UIntPtr) """
    def Invoke(self, Sld:Slide, X:Single, Y:Single): # -> 
        """ Invoke(self: EApplication_AfterDragDropOnSlideEventHandler, Sld: Slide, X: Single, Y: Single) """
        ...


class EApplication_AfterNewPresentationEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_AfterNewPresentationEventHandler(: object, : UIntPtr) """
    def Invoke(self, Pres:Presentation): # -> 
        """ Invoke(self: EApplication_AfterNewPresentationEventHandler, Pres: Presentation) """
        ...


class EApplication_AfterPresentationOpenEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_AfterPresentationOpenEventHandler(: object, : UIntPtr) """
    def Invoke(self, Pres:Presentation): # -> 
        """ Invoke(self: EApplication_AfterPresentationOpenEventHandler, Pres: Presentation) """
        ...


class EApplication_AfterShapeSizeChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_AfterShapeSizeChangeEventHandler(: object, : UIntPtr) """
    def Invoke(self, shp:Shape): # -> 
        """ Invoke(self: EApplication_AfterShapeSizeChangeEventHandler, shp: Shape) """
        ...


class EApplication_ColorSchemeChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_ColorSchemeChangedEventHandler(: object, : UIntPtr) """
    def Invoke(self, SldRange:SlideRange): # -> 
        """ Invoke(self: EApplication_ColorSchemeChangedEventHandler, SldRange: SlideRange) """
        ...


class EApplication_NewPresentationEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_NewPresentationEventHandler(: object, : UIntPtr) """
    def Invoke(self, Pres:Presentation): # -> 
        """ Invoke(self: EApplication_NewPresentationEventHandler, Pres: Presentation) """
        ...


class EApplication_PresentationBeforeCloseEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_PresentationBeforeCloseEventHandler(: object, : UIntPtr) """
    def Invoke(self, Pres, Cancel) -> bool:
        """ Invoke(self: EApplication_PresentationBeforeCloseEventHandler, Pres: Presentation) -> bool """
        ...


class EApplication_PresentationBeforeSaveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_PresentationBeforeSaveEventHandler(: object, : UIntPtr) """
    def Invoke(self, Pres, Cancel) -> bool:
        """ Invoke(self: EApplication_PresentationBeforeSaveEventHandler, Pres: Presentation) -> bool """
        ...


class EApplication_PresentationCloseEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_PresentationCloseEventHandler(: object, : UIntPtr) """
    def Invoke(self, Pres:Presentation): # -> 
        """ Invoke(self: EApplication_PresentationCloseEventHandler, Pres: Presentation) """
        ...


class EApplication_PresentationCloseFinalEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_PresentationCloseFinalEventHandler(: object, : UIntPtr) """
    def Invoke(self, Pres:Presentation): # -> 
        """ Invoke(self: EApplication_PresentationCloseFinalEventHandler, Pres: Presentation) """
        ...


class EApplication_PresentationNewSlideEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_PresentationNewSlideEventHandler(: object, : UIntPtr) """
    def Invoke(self, Sld:Slide): # -> 
        """ Invoke(self: EApplication_PresentationNewSlideEventHandler, Sld: Slide) """
        ...


class EApplication_PresentationOpenEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_PresentationOpenEventHandler(: object, : UIntPtr) """
    def Invoke(self, Pres:Presentation): # -> 
        """ Invoke(self: EApplication_PresentationOpenEventHandler, Pres: Presentation) """
        ...


class EApplication_PresentationPrintEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_PresentationPrintEventHandler(: object, : UIntPtr) """
    def Invoke(self, Pres:Presentation): # -> 
        """ Invoke(self: EApplication_PresentationPrintEventHandler, Pres: Presentation) """
        ...


class EApplication_PresentationSaveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_PresentationSaveEventHandler(: object, : UIntPtr) """
    def Invoke(self, Pres:Presentation): # -> 
        """ Invoke(self: EApplication_PresentationSaveEventHandler, Pres: Presentation) """
        ...


class EApplication_PresentationSyncEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_PresentationSyncEventHandler(: object, : UIntPtr) """
    def Invoke(self, Pres:Presentation, SyncEventType): # ->  # Not found arg types: {'SyncEventType': 'MsoSyncEventType'}
        """ Invoke(self: EApplication_PresentationSyncEventHandler, Pres: Presentation, SyncEventType: MsoSyncEventType) """
        ...


class EApplication_ProtectedViewWindowActivateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_ProtectedViewWindowActivateEventHandler(: object, : UIntPtr) """
    def Invoke(self, ProtViewWindow:ProtectedViewWindow): # -> 
        """ Invoke(self: EApplication_ProtectedViewWindowActivateEventHandler, ProtViewWindow: ProtectedViewWindow) """
        ...


class EApplication_ProtectedViewWindowBeforeCloseEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_ProtectedViewWindowBeforeCloseEventHandler(: object, : UIntPtr) """
    def Invoke(self, ProtViewWindow, ProtectedViewCloseReason, Cancel) -> bool:
        """ Invoke(self: EApplication_ProtectedViewWindowBeforeCloseEventHandler, ProtViewWindow: ProtectedViewWindow, ProtectedViewCloseReason: PpProtectedViewCloseReason) -> bool """
        ...


class EApplication_ProtectedViewWindowBeforeEditEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_ProtectedViewWindowBeforeEditEventHandler(: object, : UIntPtr) """
    def Invoke(self, ProtViewWindow, Cancel) -> bool:
        """ Invoke(self: EApplication_ProtectedViewWindowBeforeEditEventHandler, ProtViewWindow: ProtectedViewWindow) -> bool """
        ...


class EApplication_ProtectedViewWindowDeactivateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_ProtectedViewWindowDeactivateEventHandler(: object, : UIntPtr) """
    def Invoke(self, ProtViewWindow:ProtectedViewWindow): # -> 
        """ Invoke(self: EApplication_ProtectedViewWindowDeactivateEventHandler, ProtViewWindow: ProtectedViewWindow) """
        ...


class EApplication_ProtectedViewWindowOpenEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_ProtectedViewWindowOpenEventHandler(: object, : UIntPtr) """
    def Invoke(self, ProtViewWindow:ProtectedViewWindow): # -> 
        """ Invoke(self: EApplication_ProtectedViewWindowOpenEventHandler, ProtViewWindow: ProtectedViewWindow) """
        ...


class EApplication_SinkHelper(EApplication): # skipped bases: <type 'object'>
    """ no doc """
    m_AfterDragDropOnSlideDelegate = ...
    m_AfterNewPresentationDelegate = ...
    m_AfterPresentationOpenDelegate = ...
    m_AfterShapeSizeChangeDelegate = ...
    m_ColorSchemeChangedDelegate = ...
    m_dwCookie = ...
    m_NewPresentationDelegate = ...
    m_PresentationBeforeCloseDelegate = ...
    m_PresentationBeforeSaveDelegate = ...
    m_PresentationCloseDelegate = ...
    m_PresentationCloseFinalDelegate = ...
    m_PresentationNewSlideDelegate = ...
    m_PresentationOpenDelegate = ...
    m_PresentationPrintDelegate = ...
    m_PresentationSaveDelegate = ...
    m_PresentationSyncDelegate = ...
    m_ProtectedViewWindowActivateDelegate = ...
    m_ProtectedViewWindowBeforeCloseDelegate = ...
    m_ProtectedViewWindowBeforeEditDelegate = ...
    m_ProtectedViewWindowDeactivateDelegate = ...
    m_ProtectedViewWindowOpenDelegate = ...
    m_SlideSelectionChangedDelegate = ...
    m_SlideShowBeginDelegate = ...
    m_SlideShowEndDelegate = ...
    m_SlideShowNextBuildDelegate = ...
    m_SlideShowNextClickDelegate = ...
    m_SlideShowNextSlideDelegate = ...
    m_SlideShowOnNextDelegate = ...
    m_SlideShowOnPreviousDelegate = ...
    m_WindowActivateDelegate = ...
    m_WindowBeforeDoubleClickDelegate = ...
    m_WindowBeforeRightClickDelegate = ...
    m_WindowDeactivateDelegate = ...
    m_WindowSelectionChangeDelegate = ...


class EApplication_SlideSelectionChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_SlideSelectionChangedEventHandler(: object, : UIntPtr) """
    def Invoke(self, SldRange:SlideRange): # -> 
        """ Invoke(self: EApplication_SlideSelectionChangedEventHandler, SldRange: SlideRange) """
        ...


class EApplication_SlideShowBeginEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_SlideShowBeginEventHandler(: object, : UIntPtr) """
    def Invoke(self, Wn:SlideShowWindow): # -> 
        """ Invoke(self: EApplication_SlideShowBeginEventHandler, Wn: SlideShowWindow) """
        ...


class EApplication_SlideShowEndEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_SlideShowEndEventHandler(: object, : UIntPtr) """
    def Invoke(self, Pres:Presentation): # -> 
        """ Invoke(self: EApplication_SlideShowEndEventHandler, Pres: Presentation) """
        ...


class EApplication_SlideShowNextBuildEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_SlideShowNextBuildEventHandler(: object, : UIntPtr) """
    def Invoke(self, Wn:SlideShowWindow): # -> 
        """ Invoke(self: EApplication_SlideShowNextBuildEventHandler, Wn: SlideShowWindow) """
        ...


class EApplication_SlideShowNextClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_SlideShowNextClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Wn:SlideShowWindow, nEffect:Effect): # -> 
        """ Invoke(self: EApplication_SlideShowNextClickEventHandler, Wn: SlideShowWindow, nEffect: Effect) """
        ...


class EApplication_SlideShowNextSlideEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_SlideShowNextSlideEventHandler(: object, : UIntPtr) """
    def Invoke(self, Wn:SlideShowWindow): # -> 
        """ Invoke(self: EApplication_SlideShowNextSlideEventHandler, Wn: SlideShowWindow) """
        ...


class EApplication_SlideShowOnNextEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_SlideShowOnNextEventHandler(: object, : UIntPtr) """
    def Invoke(self, Wn:SlideShowWindow): # -> 
        """ Invoke(self: EApplication_SlideShowOnNextEventHandler, Wn: SlideShowWindow) """
        ...


class EApplication_SlideShowOnPreviousEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_SlideShowOnPreviousEventHandler(: object, : UIntPtr) """
    def Invoke(self, Wn:SlideShowWindow): # -> 
        """ Invoke(self: EApplication_SlideShowOnPreviousEventHandler, Wn: SlideShowWindow) """
        ...


class EApplication_WindowActivateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_WindowActivateEventHandler(: object, : UIntPtr) """
    def Invoke(self, Pres:Presentation, Wn:DocumentWindow): # -> 
        """ Invoke(self: EApplication_WindowActivateEventHandler, Pres: Presentation, Wn: DocumentWindow) """
        ...


class EApplication_WindowBeforeDoubleClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_WindowBeforeDoubleClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Sel, Cancel) -> bool:
        """ Invoke(self: EApplication_WindowBeforeDoubleClickEventHandler, Sel: Selection) -> bool """
        ...


class EApplication_WindowBeforeRightClickEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_WindowBeforeRightClickEventHandler(: object, : UIntPtr) """
    def Invoke(self, Sel, Cancel) -> bool:
        """ Invoke(self: EApplication_WindowBeforeRightClickEventHandler, Sel: Selection) -> bool """
        ...


class EApplication_WindowDeactivateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_WindowDeactivateEventHandler(: object, : UIntPtr) """
    def Invoke(self, Pres:Presentation, Wn:DocumentWindow): # -> 
        """ Invoke(self: EApplication_WindowDeactivateEventHandler, Pres: Presentation, Wn: DocumentWindow) """
        ...


class EApplication_WindowSelectionChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EApplication_WindowSelectionChangeEventHandler(: object, : UIntPtr) """
    def Invoke(self, Sel:Selection): # -> 
        """ Invoke(self: EApplication_WindowSelectionChangeEventHandler, Sel: Selection) """
        ...


class Effect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Effect) -> Application """
        ...

    @property
    def Behaviors(self) -> AnimationBehaviors:
        """ Get: Behaviors(self: Effect) -> AnimationBehaviors """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: Effect) -> str """
        ...

    @property
    def EffectInformation(self) -> EffectInformation:
        """ Get: EffectInformation(self: Effect) -> EffectInformation """
        ...

    @property
    def EffectParameters(self) -> EffectParameters:
        """ Get: EffectParameters(self: Effect) -> EffectParameters """
        ...

    @property
    def EffectType(self) -> MsoAnimEffect:
        """
        Get: EffectType(self: Effect) -> MsoAnimEffect
        Set: EffectType(self: Effect) = value
        """
        ...

    @property
    def Exit(self): # -> MsoTriState
        """
        Get: Exit(self: Effect) -> MsoTriState
        Set: Exit(self: Effect) = value
        """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: Effect) -> int """
        ...

    @property
    def Paragraph(self) -> int:
        """
        Get: Paragraph(self: Effect) -> int
        Set: Paragraph(self: Effect) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Effect) -> object """
        ...

    @property
    def Shape(self) -> Shape:
        """
        Get: Shape(self: Effect) -> Shape
        Set: Shape(self: Effect) = value
        """
        ...

    @property
    def TextRangeLength(self) -> int:
        """ Get: TextRangeLength(self: Effect) -> int """
        ...

    @property
    def TextRangeStart(self) -> int:
        """ Get: TextRangeStart(self: Effect) -> int """
        ...

    @property
    def Timing(self) -> Timing:
        """ Get: Timing(self: Effect) -> Timing """
        ...


    def Delete(self): # -> 
        """ Delete(self: Effect) """
        ...

    def MoveAfter(self, Effect:Effect): # -> 
        """ MoveAfter(self: Effect, Effect: Effect) """
        ...

    def MoveBefore(self, Effect:Effect): # -> 
        """ MoveBefore(self: Effect, Effect: Effect) """
        ...

    def MoveTo(self, toPos:int): # -> 
        """ MoveTo(self: Effect, toPos: int) """
        ...


class EffectInformation: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AfterEffect(self) -> MsoAnimAfterEffect:
        """ Get: AfterEffect(self: EffectInformation) -> MsoAnimAfterEffect """
        ...

    @property
    def AnimateBackground(self): # -> MsoTriState
        """ Get: AnimateBackground(self: EffectInformation) -> MsoTriState """
        ...

    @property
    def AnimateTextInReverse(self): # -> MsoTriState
        """ Get: AnimateTextInReverse(self: EffectInformation) -> MsoTriState """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: EffectInformation) -> Application """
        ...

    @property
    def BuildByLevelEffect(self) -> MsoAnimateByLevel:
        """ Get: BuildByLevelEffect(self: EffectInformation) -> MsoAnimateByLevel """
        ...

    @property
    def Dim(self) -> ColorFormat:
        """ Get: Dim(self: EffectInformation) -> ColorFormat """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: EffectInformation) -> object """
        ...

    @property
    def PlaySettings(self) -> PlaySettings:
        """ Get: PlaySettings(self: EffectInformation) -> PlaySettings """
        ...

    @property
    def SoundEffect(self) -> SoundEffect:
        """ Get: SoundEffect(self: EffectInformation) -> SoundEffect """
        ...

    @property
    def TextUnitEffect(self) -> MsoAnimTextUnitEffect:
        """ Get: TextUnitEffect(self: EffectInformation) -> MsoAnimTextUnitEffect """
        ...



class EffectParameters: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Amount(self) -> Single:
        """
        Get: Amount(self: EffectParameters) -> Single
        Set: Amount(self: EffectParameters) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: EffectParameters) -> Application """
        ...

    @property
    def Color2(self) -> ColorFormat:
        """ Get: Color2(self: EffectParameters) -> ColorFormat """
        ...

    @property
    def Direction(self) -> MsoAnimDirection:
        """
        Get: Direction(self: EffectParameters) -> MsoAnimDirection
        Set: Direction(self: EffectParameters) = value
        """
        ...

    @property
    def FontName(self) -> str:
        """
        Get: FontName(self: EffectParameters) -> str
        Set: FontName(self: EffectParameters) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: EffectParameters) -> object """
        ...

    @property
    def Relative(self): # -> MsoTriState
        """
        Get: Relative(self: EffectParameters) -> MsoTriState
        Set: Relative(self: EffectParameters) = value
        """
        ...

    @property
    def Size(self) -> Single:
        """
        Get: Size(self: EffectParameters) -> Single
        Set: Size(self: EffectParameters) = value
        """
        ...



class ErrorBars: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ErrorBars) -> Application """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: ErrorBars) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: ErrorBars) -> int """
        ...

    @property
    def EndStyle(self) -> XlEndStyleCap:
        """
        Get: EndStyle(self: ErrorBars) -> XlEndStyleCap
        Set: EndStyle(self: ErrorBars) = value
        """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: ErrorBars) -> ChartFormat """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ErrorBars) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ErrorBars) -> object """
        ...


    def ClearFormats(self) -> object:
        """ ClearFormats(self: ErrorBars) -> object """
        ...

    def Delete(self) -> object:
        """ Delete(self: ErrorBars) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: ErrorBars) -> object """
        ...


class ExtraColors(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ExtraColors) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ExtraColors) -> object """
        ...


    def Add(self, Type:int): # -> 
        """ Add(self: ExtraColors, Type: int) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ExtraColors) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class FileConverter: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: FileConverter) -> Application """
        ...

    @property
    def CanOpen(self) -> bool:
        """ Get: CanOpen(self: FileConverter) -> bool """
        ...

    @property
    def CanSave(self) -> bool:
        """ Get: CanSave(self: FileConverter) -> bool """
        ...

    @property
    def ClassName(self) -> str:
        """ Get: ClassName(self: FileConverter) -> str """
        ...

    @property
    def Creator(self) -> FileConverters:
        """ Get: Creator(self: FileConverter) -> FileConverters """
        ...

    @property
    def Extensions(self) -> str:
        """ Get: Extensions(self: FileConverter) -> str """
        ...

    @property
    def FormatName(self) -> str:
        """ Get: FormatName(self: FileConverter) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: FileConverter) -> str """
        ...

    @property
    def OpenFormat(self) -> int:
        """ Get: OpenFormat(self: FileConverter) -> int """
        ...

    @property
    def Parent(self) -> FileConverters:
        """ Get: Parent(self: FileConverter) -> FileConverters """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: FileConverter) -> str """
        ...

    @property
    def SaveFormat(self) -> int:
        """ Get: SaveFormat(self: FileConverter) -> int """
        ...



class FileConverters(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class FillFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: FillFormat) -> object """
        ...

    @property
    def BackColor(self) -> ColorFormat:
        """
        Get: BackColor(self: FillFormat) -> ColorFormat
        Set: BackColor(self: FillFormat) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: FillFormat) -> int """
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
    def GradientStops(self): # -> GradientStops
        """ Get: GradientStops(self: FillFormat) -> GradientStops """
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
    def PictureEffects(self): # -> PictureEffects
        """ Get: PictureEffects(self: FillFormat) -> PictureEffects """
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
    def TextureTile(self): # -> MsoTriState
        """
        Get: TextureTile(self: FillFormat) -> MsoTriState
        Set: TextureTile(self: FillFormat) = value
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


    def Background(self): # -> 
        """ Background(self: FillFormat) """
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


class FilterEffect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: FilterEffect) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: FilterEffect) -> object """
        ...

    @property
    def Reveal(self): # -> MsoTriState
        """
        Get: Reveal(self: FilterEffect) -> MsoTriState
        Set: Reveal(self: FilterEffect) = value
        """
        ...

    @property
    def Subtype(self) -> MsoAnimFilterEffectSubtype:
        """
        Get: Subtype(self: FilterEffect) -> MsoAnimFilterEffectSubtype
        Set: Subtype(self: FilterEffect) = value
        """
        ...

    @property
    def Type(self) -> MsoAnimFilterEffectType:
        """
        Get: Type(self: FilterEffect) -> MsoAnimFilterEffectType
        Set: Type(self: FilterEffect) = value
        """
        ...



class Floor: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Floor) -> Application """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: Floor) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Floor) -> int """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: Floor) -> ChartFillFormat """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: Floor) -> ChartFormat """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: Floor) -> Interior """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Floor) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Floor) -> object """
        ...

    @property
    def PictureType(self) -> object:
        """
        Get: PictureType(self: Floor) -> object
        Set: PictureType(self: Floor) = value
        """
        ...

    @property
    def Thickness(self) -> int:
        """
        Get: Thickness(self: Floor) -> int
        Set: Thickness(self: Floor) = value
        """
        ...


    def ClearFormats(self) -> object:
        """ ClearFormats(self: Floor) -> object """
        ...

    def Paste(self): # -> 
        """ Paste(self: Floor) """
        ...

    def Select(self) -> object:
        """ Select(self: Floor) -> object """
        ...


class Font: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Font) -> Application """
        ...

    @property
    def AutoRotateNumbers(self): # -> MsoTriState
        """
        Get: AutoRotateNumbers(self: Font) -> MsoTriState
        Set: AutoRotateNumbers(self: Font) = value
        """
        ...

    @property
    def BaselineOffset(self) -> Single:
        """
        Get: BaselineOffset(self: Font) -> Single
        Set: BaselineOffset(self: Font) = value
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
    def Color(self) -> ColorFormat:
        """ Get: Color(self: Font) -> ColorFormat """
        ...

    @property
    def Embeddable(self): # -> MsoTriState
        """ Get: Embeddable(self: Font) -> MsoTriState """
        ...

    @property
    def Embedded(self): # -> MsoTriState
        """ Get: Embedded(self: Font) -> MsoTriState """
        ...

    @property
    def Emboss(self): # -> MsoTriState
        """
        Get: Emboss(self: Font) -> MsoTriState
        Set: Emboss(self: Font) = value
        """
        ...

    @property
    def Italic(self): # -> MsoTriState
        """
        Get: Italic(self: Font) -> MsoTriState
        Set: Italic(self: Font) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Font) -> str
        Set: Name(self: Font) = value
        """
        ...

    @property
    def NameAscii(self) -> str:
        """
        Get: NameAscii(self: Font) -> str
        Set: NameAscii(self: Font) = value
        """
        ...

    @property
    def NameComplexScript(self) -> str:
        """
        Get: NameComplexScript(self: Font) -> str
        Set: NameComplexScript(self: Font) = value
        """
        ...

    @property
    def NameFarEast(self) -> str:
        """
        Get: NameFarEast(self: Font) -> str
        Set: NameFarEast(self: Font) = value
        """
        ...

    @property
    def NameOther(self) -> str:
        """
        Get: NameOther(self: Font) -> str
        Set: NameOther(self: Font) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Font) -> object """
        ...

    @property
    def Shadow(self): # -> MsoTriState
        """
        Get: Shadow(self: Font) -> MsoTriState
        Set: Shadow(self: Font) = value
        """
        ...

    @property
    def Size(self) -> Single:
        """
        Get: Size(self: Font) -> Single
        Set: Size(self: Font) = value
        """
        ...

    @property
    def Subscript(self): # -> MsoTriState
        """
        Get: Subscript(self: Font) -> MsoTriState
        Set: Subscript(self: Font) = value
        """
        ...

    @property
    def Superscript(self): # -> MsoTriState
        """
        Get: Superscript(self: Font) -> MsoTriState
        Set: Superscript(self: Font) = value
        """
        ...

    @property
    def Underline(self): # -> MsoTriState
        """
        Get: Underline(self: Font) -> MsoTriState
        Set: Underline(self: Font) = value
        """
        ...



class Fonts(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Fonts) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Fonts) -> object """
        ...


    def Replace(self, Original:str, Replacement:str): # -> 
        """ Replace(self: Fonts, Original: str, Replacement: str) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class FreeformBuilder: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: FreeformBuilder) -> object """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: FreeformBuilder) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: FreeformBuilder) -> object """
        ...


    def AddNodes(self, SegmentType, EditingType, X1:Single, Y1:Single, X2:Single, Y2:Single, X3:Single, Y3:Single): # ->  # Not found arg types: {'EditingType': 'MsoEditingType', 'SegmentType': 'MsoSegmentType'}
        """ AddNodes(self: FreeformBuilder, SegmentType: MsoSegmentType, EditingType: MsoEditingType, X1: Single, Y1: Single, X2: Single, Y2: Single, X3: Single, Y3: Single) """
        ...

    def ConvertToShape(self) -> Shape:
        """ ConvertToShape(self: FreeformBuilder) -> Shape """
        ...


class FullSeriesCollection(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: FullSeriesCollection) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: FullSeriesCollection) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: FullSeriesCollection) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: FullSeriesCollection) -> object """
        ...


    def Item(self, Index:object) -> Series:
        """ Item(self: FullSeriesCollection, Index: object) -> Series """
        ...

    def _Default(self, Index:object) -> Series:
        """ _Default(self: FullSeriesCollection, Index: object) -> Series """
        ...


class _Global: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActivePresentation(self) -> Presentation:
        """ Get: ActivePresentation(self: _Global) -> Presentation """
        ...

    @property
    def ActiveProtectedViewWindow(self) -> ProtectedViewWindow:
        """ Get: ActiveProtectedViewWindow(self: _Global) -> ProtectedViewWindow """
        ...

    @property
    def ActiveWindow(self) -> DocumentWindow:
        """ Get: ActiveWindow(self: _Global) -> DocumentWindow """
        ...

    @property
    def AddIns(self) -> AddIns:
        """ Get: AddIns(self: _Global) -> AddIns """
        ...

    @property
    def AnswerWizard(self): # -> AnswerWizard
        """ Get: AnswerWizard(self: _Global) -> AnswerWizard """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: _Global) -> Application """
        ...

    @property
    def Assistant(self): # -> Assistant
        """ Get: Assistant(self: _Global) -> Assistant """
        ...

    @property
    def CommandBars(self) -> CommandBars:
        """ Get: CommandBars(self: _Global) -> CommandBars """
        ...

    @property
    def Dialogs(self) -> object:
        """ Get: Dialogs(self: _Global) -> object """
        ...

    @property
    def FileConverters(self) -> FileConverters:
        """ Get: FileConverters(self: _Global) -> FileConverters """
        ...

    @property
    def IsSandboxed(self) -> bool:
        """ Get: IsSandboxed(self: _Global) -> bool """
        ...

    @property
    def Presentations(self) -> Presentations:
        """ Get: Presentations(self: _Global) -> Presentations """
        ...

    @property
    def ProtectedViewWindows(self) -> ProtectedViewWindows:
        """ Get: ProtectedViewWindows(self: _Global) -> ProtectedViewWindows """
        ...

    @property
    def SlideShowWindows(self) -> SlideShowWindows:
        """ Get: SlideShowWindows(self: _Global) -> SlideShowWindows """
        ...

    @property
    def Windows(self) -> DocumentWindows:
        """ Get: Windows(self: _Global) -> DocumentWindows """
        ...



class Global(_Global): # skipped bases: <type 'object'>
    """ no doc """
    pass

class GlobalClass(__ComObject, Global): # skipped bases: <type '_Global'>, <type 'object'>
    """ GlobalClass() """
    @property
    def ActivePresentation(self) -> Presentation:
        """ Get: ActivePresentation(self: GlobalClass) -> Presentation """
        ...

    @property
    def ActiveProtectedViewWindow(self) -> ProtectedViewWindow:
        """ Get: ActiveProtectedViewWindow(self: GlobalClass) -> ProtectedViewWindow """
        ...

    @property
    def ActiveWindow(self) -> DocumentWindow:
        """ Get: ActiveWindow(self: GlobalClass) -> DocumentWindow """
        ...

    @property
    def AddIns(self) -> AddIns:
        """ Get: AddIns(self: GlobalClass) -> AddIns """
        ...

    @property
    def AnswerWizard(self): # -> AnswerWizard
        """ Get: AnswerWizard(self: GlobalClass) -> AnswerWizard """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: GlobalClass) -> Application """
        ...

    @property
    def Assistant(self): # -> Assistant
        """ Get: Assistant(self: GlobalClass) -> Assistant """
        ...

    @property
    def CommandBars(self) -> CommandBars:
        """ Get: CommandBars(self: GlobalClass) -> CommandBars """
        ...

    @property
    def Dialogs(self) -> object:
        """ Get: Dialogs(self: GlobalClass) -> object """
        ...

    @property
    def FileConverters(self) -> FileConverters:
        """ Get: FileConverters(self: GlobalClass) -> FileConverters """
        ...

    @property
    def IsSandboxed(self) -> bool:
        """ Get: IsSandboxed(self: GlobalClass) -> bool """
        ...

    @property
    def Presentations(self) -> Presentations:
        """ Get: Presentations(self: GlobalClass) -> Presentations """
        ...

    @property
    def ProtectedViewWindows(self) -> ProtectedViewWindows:
        """ Get: ProtectedViewWindows(self: GlobalClass) -> ProtectedViewWindows """
        ...

    @property
    def SlideShowWindows(self) -> SlideShowWindows:
        """ Get: SlideShowWindows(self: GlobalClass) -> SlideShowWindows """
        ...

    @property
    def Windows(self) -> DocumentWindows:
        """ Get: Windows(self: GlobalClass) -> DocumentWindows """
        ...



class Gridlines: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Gridlines) -> Application """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: Gridlines) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Gridlines) -> int """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: Gridlines) -> ChartFormat """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Gridlines) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Gridlines) -> object """
        ...


    def Delete(self) -> object:
        """ Delete(self: Gridlines) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: Gridlines) -> object """
        ...


class GroupShapes(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: GroupShapes) -> object """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: GroupShapes) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: GroupShapes) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: GroupShapes) -> object """
        ...


    def Range(self, Index:object) -> ShapeRange:
        """ Range(self: GroupShapes, Index: object) -> ShapeRange """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Guide: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Guide) -> Application """
        ...

    @property
    def Color(self) -> ColorFormat:
        """ Get: Color(self: Guide) -> ColorFormat """
        ...

    @property
    def Orientation(self) -> PpGuideOrientation:
        """ Get: Orientation(self: Guide) -> PpGuideOrientation """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Guide) -> object """
        ...

    @property
    def Position(self) -> Single:
        """
        Get: Position(self: Guide) -> Single
        Set: Position(self: Guide) = value
        """
        ...


    def Delete(self): # -> 
        """ Delete(self: Guide) """
        ...


class Guides(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Guides) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Guides) -> object """
        ...


    def Add(self, Orientation:PpGuideOrientation, Position:Single) -> Guide:
        """ Add(self: Guides, Orientation: PpGuideOrientation, Position: Single) -> Guide """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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
    def Format(self) -> PpDateTimeFormat:
        """
        Get: Format(self: HeaderFooter) -> PpDateTimeFormat
        Set: Format(self: HeaderFooter) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: HeaderFooter) -> object """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: HeaderFooter) -> str
        Set: Text(self: HeaderFooter) = value
        """
        ...

    @property
    def UseFormat(self): # -> MsoTriState
        """
        Get: UseFormat(self: HeaderFooter) -> MsoTriState
        Set: UseFormat(self: HeaderFooter) = value
        """
        ...

    @property
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: HeaderFooter) -> MsoTriState
        Set: Visible(self: HeaderFooter) = value
        """
        ...



class HeadersFooters: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: HeadersFooters) -> Application """
        ...

    @property
    def DateAndTime(self) -> HeaderFooter:
        """ Get: DateAndTime(self: HeadersFooters) -> HeaderFooter """
        ...

    @property
    def DisplayOnTitleSlide(self): # -> MsoTriState
        """
        Get: DisplayOnTitleSlide(self: HeadersFooters) -> MsoTriState
        Set: DisplayOnTitleSlide(self: HeadersFooters) = value
        """
        ...

    @property
    def Footer(self) -> HeaderFooter:
        """ Get: Footer(self: HeadersFooters) -> HeaderFooter """
        ...

    @property
    def Header(self) -> HeaderFooter:
        """ Get: Header(self: HeadersFooters) -> HeaderFooter """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: HeadersFooters) -> object """
        ...

    @property
    def SlideNumber(self) -> HeaderFooter:
        """ Get: SlideNumber(self: HeadersFooters) -> HeaderFooter """
        ...


    def Clear(self): # -> 
        """ Clear(self: HeadersFooters) """
        ...


class HiLoLines: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: HiLoLines) -> Application """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: HiLoLines) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: HiLoLines) -> int """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: HiLoLines) -> ChartFormat """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: HiLoLines) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: HiLoLines) -> object """
        ...


    def Delete(self) -> object:
        """ Delete(self: HiLoLines) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: HiLoLines) -> object """
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
    def Parent(self) -> object:
        """ Get: Parent(self: Hyperlink) -> object """
        ...

    @property
    def ScreenTip(self) -> str:
        """
        Get: ScreenTip(self: Hyperlink) -> str
        Set: ScreenTip(self: Hyperlink) = value
        """
        ...

    @property
    def ShowAndReturn(self): # -> MsoTriState
        """
        Get: ShowAndReturn(self: Hyperlink) -> MsoTriState
        Set: ShowAndReturn(self: Hyperlink) = value
        """
        ...

    @property
    def SubAddress(self) -> str:
        """
        Get: SubAddress(self: Hyperlink) -> str
        Set: SubAddress(self: Hyperlink) = value
        """
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


    def AddToFavorites(self): # -> 
        """ AddToFavorites(self: Hyperlink) """
        ...

    def CreateNewDocument(self, FileName:str, EditNow, Overwrite): # ->  # Not found arg types: {'Overwrite': 'MsoTriState', 'EditNow': 'MsoTriState'}
        """ CreateNewDocument(self: Hyperlink, FileName: str, EditNow: MsoTriState, Overwrite: MsoTriState) """
        ...

    def Delete(self): # -> 
        """ Delete(self: Hyperlink) """
        ...

    def Follow(self): # -> 
        """ Follow(self: Hyperlink) """
        ...


class Hyperlinks(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Hyperlinks) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Hyperlinks) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Interior: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Interior) -> Application """
        ...

    @property
    def Color(self) -> object:
        """
        Get: Color(self: Interior) -> object
        Set: Color(self: Interior) = value
        """
        ...

    @property
    def ColorIndex(self) -> object:
        """
        Get: ColorIndex(self: Interior) -> object
        Set: ColorIndex(self: Interior) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Interior) -> int """
        ...

    @property
    def InvertIfNegative(self) -> object:
        """
        Get: InvertIfNegative(self: Interior) -> object
        Set: InvertIfNegative(self: Interior) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Interior) -> object """
        ...

    @property
    def Pattern(self) -> object:
        """
        Get: Pattern(self: Interior) -> object
        Set: Pattern(self: Interior) = value
        """
        ...

    @property
    def PatternColor(self) -> object:
        """
        Get: PatternColor(self: Interior) -> object
        Set: PatternColor(self: Interior) = value
        """
        ...

    @property
    def PatternColorIndex(self) -> object:
        """
        Get: PatternColorIndex(self: Interior) -> object
        Set: PatternColorIndex(self: Interior) = value
        """
        ...



class LeaderLines: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: LeaderLines) -> Application """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: LeaderLines) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: LeaderLines) -> int """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: LeaderLines) -> ChartFormat """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: LeaderLines) -> object """
        ...


    def Delete(self): # -> 
        """ Delete(self: LeaderLines) """
        ...

    def Select(self): # -> 
        """ Select(self: LeaderLines) """
        ...


class Legend: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Legend) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: Legend) -> object
        Set: AutoScaleFont(self: Legend) = value
        """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: Legend) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Legend) -> int """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: Legend) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> ChartFont:
        """ Get: Font(self: Legend) -> ChartFont """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: Legend) -> ChartFormat """
        ...

    @property
    def Height(self) -> float:
        """
        Get: Height(self: Legend) -> float
        Set: Height(self: Legend) = value
        """
        ...

    @property
    def IncludeInLayout(self) -> bool:
        """
        Get: IncludeInLayout(self: Legend) -> bool
        Set: IncludeInLayout(self: Legend) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: Legend) -> Interior """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: Legend) -> float
        Set: Left(self: Legend) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Legend) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Legend) -> object """
        ...

    @property
    def Position(self) -> XlLegendPosition:
        """
        Get: Position(self: Legend) -> XlLegendPosition
        Set: Position(self: Legend) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: Legend) -> bool
        Set: Shadow(self: Legend) = value
        """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: Legend) -> float
        Set: Top(self: Legend) = value
        """
        ...

    @property
    def Width(self) -> float:
        """
        Get: Width(self: Legend) -> float
        Set: Width(self: Legend) = value
        """
        ...


    def Clear(self) -> object:
        """ Clear(self: Legend) -> object """
        ...

    def Delete(self) -> object:
        """ Delete(self: Legend) -> object """
        ...

    def LegendEntries(self, Index:object) -> object:
        """ LegendEntries(self: Legend, Index: object) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: Legend) -> object """
        ...


class LegendEntries(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: LegendEntries) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: LegendEntries) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: LegendEntries) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: LegendEntries) -> object """
        ...


    def Item(self, Index:object) -> LegendEntry:
        """ Item(self: LegendEntries, Index: object) -> LegendEntry """
        ...

    def _Default(self, Index:object) -> LegendEntry:
        """ _Default(self: LegendEntries, Index: object) -> LegendEntry """
        ...


class LegendEntry: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: LegendEntry) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: LegendEntry) -> object
        Set: AutoScaleFont(self: LegendEntry) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: LegendEntry) -> int """
        ...

    @property
    def Font(self) -> ChartFont:
        """ Get: Font(self: LegendEntry) -> ChartFont """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: LegendEntry) -> ChartFormat """
        ...

    @property
    def Height(self) -> float:
        """ Get: Height(self: LegendEntry) -> float """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: LegendEntry) -> int """
        ...

    @property
    def Left(self) -> float:
        """ Get: Left(self: LegendEntry) -> float """
        ...

    @property
    def LegendKey(self) -> LegendKey:
        """ Get: LegendKey(self: LegendEntry) -> LegendKey """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: LegendEntry) -> object """
        ...

    @property
    def Top(self) -> float:
        """ Get: Top(self: LegendEntry) -> float """
        ...

    @property
    def Width(self) -> float:
        """ Get: Width(self: LegendEntry) -> float """
        ...


    def Delete(self) -> object:
        """ Delete(self: LegendEntry) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: LegendEntry) -> object """
        ...


class LegendKey: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: LegendKey) -> Application """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: LegendKey) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: LegendKey) -> int """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: LegendKey) -> ChartFillFormat """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: LegendKey) -> ChartFormat """
        ...

    @property
    def Height(self) -> float:
        """ Get: Height(self: LegendKey) -> float """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: LegendKey) -> Interior """
        ...

    @property
    def InvertIfNegative(self) -> bool:
        """
        Get: InvertIfNegative(self: LegendKey) -> bool
        Set: InvertIfNegative(self: LegendKey) = value
        """
        ...

    @property
    def Left(self) -> float:
        """ Get: Left(self: LegendKey) -> float """
        ...

    @property
    def MarkerBackgroundColor(self) -> int:
        """
        Get: MarkerBackgroundColor(self: LegendKey) -> int
        Set: MarkerBackgroundColor(self: LegendKey) = value
        """
        ...

    @property
    def MarkerBackgroundColorIndex(self) -> XlColorIndex:
        """
        Get: MarkerBackgroundColorIndex(self: LegendKey) -> XlColorIndex
        Set: MarkerBackgroundColorIndex(self: LegendKey) = value
        """
        ...

    @property
    def MarkerForegroundColor(self) -> int:
        """
        Get: MarkerForegroundColor(self: LegendKey) -> int
        Set: MarkerForegroundColor(self: LegendKey) = value
        """
        ...

    @property
    def MarkerForegroundColorIndex(self) -> XlColorIndex:
        """
        Get: MarkerForegroundColorIndex(self: LegendKey) -> XlColorIndex
        Set: MarkerForegroundColorIndex(self: LegendKey) = value
        """
        ...

    @property
    def MarkerSize(self) -> int:
        """
        Get: MarkerSize(self: LegendKey) -> int
        Set: MarkerSize(self: LegendKey) = value
        """
        ...

    @property
    def MarkerStyle(self) -> XlMarkerStyle:
        """
        Get: MarkerStyle(self: LegendKey) -> XlMarkerStyle
        Set: MarkerStyle(self: LegendKey) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: LegendKey) -> object """
        ...

    @property
    def PictureType(self) -> int:
        """
        Get: PictureType(self: LegendKey) -> int
        Set: PictureType(self: LegendKey) = value
        """
        ...

    @property
    def PictureUnit(self) -> int:
        """
        Get: PictureUnit(self: LegendKey) -> int
        Set: PictureUnit(self: LegendKey) = value
        """
        ...

    @property
    def PictureUnit2(self) -> float:
        """
        Get: PictureUnit2(self: LegendKey) -> float
        Set: PictureUnit2(self: LegendKey) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: LegendKey) -> bool
        Set: Shadow(self: LegendKey) = value
        """
        ...

    @property
    def Smooth(self) -> bool:
        """
        Get: Smooth(self: LegendKey) -> bool
        Set: Smooth(self: LegendKey) = value
        """
        ...

    @property
    def Top(self) -> float:
        """ Get: Top(self: LegendKey) -> float """
        ...

    @property
    def Width(self) -> float:
        """ Get: Width(self: LegendKey) -> float """
        ...


    def ClearFormats(self) -> object:
        """ ClearFormats(self: LegendKey) -> object """
        ...

    def Delete(self) -> object:
        """ Delete(self: LegendKey) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: LegendKey) -> object """
        ...


class LineFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: LineFormat) -> object """
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
    def Creator(self) -> int:
        """ Get: Creator(self: LineFormat) -> int """
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
    def InsetPen(self): # -> MsoTriState
        """
        Get: InsetPen(self: LineFormat) -> MsoTriState
        Set: InsetPen(self: LineFormat) = value
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
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: LineFormat) -> MsoTriState
        Set: Visible(self: LineFormat) = value
        """
        ...

    @property
    def Weight(self) -> Single:
        """
        Get: Weight(self: LineFormat) -> Single
        Set: Weight(self: LineFormat) = value
        """
        ...



class LinkFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: LinkFormat) -> Application """
        ...

    @property
    def AutoUpdate(self) -> PpUpdateOption:
        """
        Get: AutoUpdate(self: LinkFormat) -> PpUpdateOption
        Set: AutoUpdate(self: LinkFormat) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: LinkFormat) -> object """
        ...

    @property
    def SourceFullName(self) -> str:
        """
        Get: SourceFullName(self: LinkFormat) -> str
        Set: SourceFullName(self: LinkFormat) = value
        """
        ...


    def BreakLink(self): # -> 
        """ BreakLink(self: LinkFormat) """
        ...

    def Update(self): # -> 
        """ Update(self: LinkFormat) """
        ...


class MasterEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    pass

class _Master: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: _Master) -> Application """
        ...

    @property
    def Background(self) -> ShapeRange:
        """ Get: Background(self: _Master) -> ShapeRange """
        ...

    @property
    def BackgroundStyle(self): # -> MsoBackgroundStyleIndex
        """
        Get: BackgroundStyle(self: _Master) -> MsoBackgroundStyleIndex
        Set: BackgroundStyle(self: _Master) = value
        """
        ...

    @property
    def ColorScheme(self) -> ColorScheme:
        """
        Get: ColorScheme(self: _Master) -> ColorScheme
        Set: ColorScheme(self: _Master) = value
        """
        ...

    @property
    def CustomerData(self) -> CustomerData:
        """ Get: CustomerData(self: _Master) -> CustomerData """
        ...

    @property
    def CustomLayouts(self) -> CustomLayouts:
        """ Get: CustomLayouts(self: _Master) -> CustomLayouts """
        ...

    @property
    def Design(self) -> Design:
        """ Get: Design(self: _Master) -> Design """
        ...

    @property
    def Guides(self) -> Guides:
        """ Get: Guides(self: _Master) -> Guides """
        ...

    @property
    def HeadersFooters(self) -> HeadersFooters:
        """ Get: HeadersFooters(self: _Master) -> HeadersFooters """
        ...

    @property
    def Height(self) -> Single:
        """ Get: Height(self: _Master) -> Single """
        ...

    @property
    def Hyperlinks(self) -> Hyperlinks:
        """ Get: Hyperlinks(self: _Master) -> Hyperlinks """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: _Master) -> str
        Set: Name(self: _Master) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: _Master) -> object """
        ...

    @property
    def Scripts(self): # -> Scripts
        """ Get: Scripts(self: _Master) -> Scripts """
        ...

    @property
    def Shapes(self) -> Shapes:
        """ Get: Shapes(self: _Master) -> Shapes """
        ...

    @property
    def SlideShowTransition(self) -> SlideShowTransition:
        """ Get: SlideShowTransition(self: _Master) -> SlideShowTransition """
        ...

    @property
    def TextStyles(self) -> TextStyles:
        """ Get: TextStyles(self: _Master) -> TextStyles """
        ...

    @property
    def Theme(self): # -> OfficeTheme
        """ Get: Theme(self: _Master) -> OfficeTheme """
        ...

    @property
    def TimeLine(self) -> TimeLine:
        """ Get: TimeLine(self: _Master) -> TimeLine """
        ...

    @property
    def Width(self) -> Single:
        """ Get: Width(self: _Master) -> Single """
        ...


    def ApplyTheme(self, themeName:str): # -> 
        """ ApplyTheme(self: _Master, themeName: str) """
        ...

    def Delete(self): # -> 
        """ Delete(self: _Master) """
        ...


class Master(_Master, MasterEvents_Event): # skipped bases: <type 'object'>
    """ no doc """
    pass

class MasterClass(Master, __ComObject): # skipped bases: <type '_Master'>, <type 'MasterEvents_Event'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: MasterClass) -> Application """
        ...

    @property
    def Background(self) -> ShapeRange:
        """ Get: Background(self: MasterClass) -> ShapeRange """
        ...

    @property
    def BackgroundStyle(self): # -> MsoBackgroundStyleIndex
        """
        Get: BackgroundStyle(self: MasterClass) -> MsoBackgroundStyleIndex
        Set: BackgroundStyle(self: MasterClass) = value
        """
        ...

    @property
    def ColorScheme(self) -> ColorScheme:
        """
        Get: ColorScheme(self: MasterClass) -> ColorScheme
        Set: ColorScheme(self: MasterClass) = value
        """
        ...

    @property
    def CustomerData(self) -> CustomerData:
        """ Get: CustomerData(self: MasterClass) -> CustomerData """
        ...

    @property
    def CustomLayouts(self) -> CustomLayouts:
        """ Get: CustomLayouts(self: MasterClass) -> CustomLayouts """
        ...

    @property
    def Design(self) -> Design:
        """ Get: Design(self: MasterClass) -> Design """
        ...

    @property
    def Guides(self) -> Guides:
        """ Get: Guides(self: MasterClass) -> Guides """
        ...

    @property
    def HeadersFooters(self) -> HeadersFooters:
        """ Get: HeadersFooters(self: MasterClass) -> HeadersFooters """
        ...

    @property
    def Height(self) -> Single:
        """ Get: Height(self: MasterClass) -> Single """
        ...

    @property
    def Hyperlinks(self) -> Hyperlinks:
        """ Get: Hyperlinks(self: MasterClass) -> Hyperlinks """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: MasterClass) -> str
        Set: Name(self: MasterClass) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: MasterClass) -> object """
        ...

    @property
    def Scripts(self): # -> Scripts
        """ Get: Scripts(self: MasterClass) -> Scripts """
        ...

    @property
    def Shapes(self) -> Shapes:
        """ Get: Shapes(self: MasterClass) -> Shapes """
        ...

    @property
    def SlideShowTransition(self) -> SlideShowTransition:
        """ Get: SlideShowTransition(self: MasterClass) -> SlideShowTransition """
        ...

    @property
    def TextStyles(self) -> TextStyles:
        """ Get: TextStyles(self: MasterClass) -> TextStyles """
        ...

    @property
    def Theme(self): # -> OfficeTheme
        """ Get: Theme(self: MasterClass) -> OfficeTheme """
        ...

    @property
    def TimeLine(self) -> TimeLine:
        """ Get: TimeLine(self: MasterClass) -> TimeLine """
        ...

    @property
    def Width(self) -> Single:
        """ Get: Width(self: MasterClass) -> Single """
        ...


    def ApplyTheme(self, themeName:str): # -> 
        """ ApplyTheme(self: MasterClass, themeName: str) """
        ...

    def Delete(self): # -> 
        """ Delete(self: MasterClass) """
        ...


class MasterEvents: # skipped bases: <type 'object'>
    """ no doc """
    pass

class MasterEvents_SinkHelper(MasterEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_dwCookie = ...


class MediaBookmark: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Index(self) -> int:
        """ Get: Index(self: MediaBookmark) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MediaBookmark) -> str """
        ...

    @property
    def Position(self) -> int:
        """ Get: Position(self: MediaBookmark) -> int """
        ...


    def Delete(self): # -> 
        """ Delete(self: MediaBookmark) """
        ...


class MediaBookmarks(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Add(self, Position:int, Name:str) -> MediaBookmark:
        """ Add(self: MediaBookmarks, Position: int, Name: str) -> MediaBookmark """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class MediaFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: MediaFormat) -> Application """
        ...

    @property
    def AudioCompressionType(self) -> str:
        """ Get: AudioCompressionType(self: MediaFormat) -> str """
        ...

    @property
    def AudioSamplingRate(self) -> int:
        """ Get: AudioSamplingRate(self: MediaFormat) -> int """
        ...

    @property
    def EndPoint(self) -> int:
        """
        Get: EndPoint(self: MediaFormat) -> int
        Set: EndPoint(self: MediaFormat) = value
        """
        ...

    @property
    def FadeInDuration(self) -> int:
        """
        Get: FadeInDuration(self: MediaFormat) -> int
        Set: FadeInDuration(self: MediaFormat) = value
        """
        ...

    @property
    def FadeOutDuration(self) -> int:
        """
        Get: FadeOutDuration(self: MediaFormat) -> int
        Set: FadeOutDuration(self: MediaFormat) = value
        """
        ...

    @property
    def IsEmbedded(self) -> bool:
        """ Get: IsEmbedded(self: MediaFormat) -> bool """
        ...

    @property
    def IsLinked(self) -> bool:
        """ Get: IsLinked(self: MediaFormat) -> bool """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: MediaFormat) -> int """
        ...

    @property
    def MediaBookmarks(self) -> MediaBookmarks:
        """ Get: MediaBookmarks(self: MediaFormat) -> MediaBookmarks """
        ...

    @property
    def Muted(self) -> bool:
        """
        Get: Muted(self: MediaFormat) -> bool
        Set: Muted(self: MediaFormat) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: MediaFormat) -> object """
        ...

    @property
    def ResamplingStatus(self) -> PpMediaTaskStatus:
        """ Get: ResamplingStatus(self: MediaFormat) -> PpMediaTaskStatus """
        ...

    @property
    def SampleHeight(self) -> int:
        """ Get: SampleHeight(self: MediaFormat) -> int """
        ...

    @property
    def SampleWidth(self) -> int:
        """ Get: SampleWidth(self: MediaFormat) -> int """
        ...

    @property
    def StartPoint(self) -> int:
        """
        Get: StartPoint(self: MediaFormat) -> int
        Set: StartPoint(self: MediaFormat) = value
        """
        ...

    @property
    def VideoCompressionType(self) -> str:
        """ Get: VideoCompressionType(self: MediaFormat) -> str """
        ...

    @property
    def VideoFrameRate(self) -> int:
        """ Get: VideoFrameRate(self: MediaFormat) -> int """
        ...

    @property
    def Volume(self) -> Single:
        """
        Get: Volume(self: MediaFormat) -> Single
        Set: Volume(self: MediaFormat) = value
        """
        ...


    def Resample(self, Trim:bool, SampleHeight:int, SampleWidth:int, VideoFrameRate:int, AudioSamplingRate:int, VideoBitRate:int): # -> 
        """ Resample(self: MediaFormat, Trim: bool, SampleHeight: int, SampleWidth: int, VideoFrameRate: int, AudioSamplingRate: int, VideoBitRate: int) """
        ...

    def ResampleFromProfile(self, profile:PpResampleMediaProfile): # -> 
        """ ResampleFromProfile(self: MediaFormat, profile: PpResampleMediaProfile) """
        ...

    def SetDisplayPicture(self, Position:int): # -> 
        """ SetDisplayPicture(self: MediaFormat, Position: int) """
        ...

    def SetDisplayPictureFromFile(self, FilePath:str): # -> 
        """ SetDisplayPictureFromFile(self: MediaFormat, FilePath: str) """
        ...


class MotionEffect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: MotionEffect) -> Application """
        ...

    @property
    def ByX(self) -> Single:
        """
        Get: ByX(self: MotionEffect) -> Single
        Set: ByX(self: MotionEffect) = value
        """
        ...

    @property
    def ByY(self) -> Single:
        """
        Get: ByY(self: MotionEffect) -> Single
        Set: ByY(self: MotionEffect) = value
        """
        ...

    @property
    def FromX(self) -> Single:
        """
        Get: FromX(self: MotionEffect) -> Single
        Set: FromX(self: MotionEffect) = value
        """
        ...

    @property
    def FromY(self) -> Single:
        """
        Get: FromY(self: MotionEffect) -> Single
        Set: FromY(self: MotionEffect) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: MotionEffect) -> object """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: MotionEffect) -> str
        Set: Path(self: MotionEffect) = value
        """
        ...

    @property
    def ToX(self) -> Single:
        """
        Get: ToX(self: MotionEffect) -> Single
        Set: ToX(self: MotionEffect) = value
        """
        ...

    @property
    def ToY(self) -> Single:
        """
        Get: ToY(self: MotionEffect) -> Single
        Set: ToY(self: MotionEffect) = value
        """
        ...



class MouseDownHandler: # skipped bases: <type 'object'>
    """ no doc """
    def OnMouseDown(self, activeWin:object): # -> 
        """ OnMouseDown(self: MouseDownHandler, activeWin: object) """
        ...


class MouseTracker: # skipped bases: <type 'object'>
    """ no doc """
    def EndTrack(self, X:Single, Y:Single): # -> 
        """ EndTrack(self: MouseTracker, X: Single, Y: Single) """
        ...

    def OnTrack(self, X:Single, Y:Single): # -> 
        """ OnTrack(self: MouseTracker, X: Single, Y: Single) """
        ...


class MsoAnimAccumulate(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoAnimAccumulate, values: msoAnimAccumulateAlways (2), msoAnimAccumulateNone (1) """
    msoAnimAccumulateAlways: MsoAnimAccumulate = ...
    msoAnimAccumulateNone: MsoAnimAccumulate = ...
    value__ = ...


class MsoAnimAdditive(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoAnimAdditive, values: msoAnimAdditiveAddBase (1), msoAnimAdditiveAddSum (2) """
    msoAnimAdditiveAddBase: MsoAnimAdditive = ...
    msoAnimAdditiveAddSum: MsoAnimAdditive = ...
    value__ = ...


class MsoAnimAfterEffect(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoAnimAfterEffect, values: msoAnimAfterEffectDim (1), msoAnimAfterEffectHide (2), msoAnimAfterEffectHideOnNextClick (3), msoAnimAfterEffectMixed (-1), msoAnimAfterEffectNone (0) """
    msoAnimAfterEffectDim: MsoAnimAfterEffect = ...
    msoAnimAfterEffectHide: MsoAnimAfterEffect = ...
    msoAnimAfterEffectHideOnNextClick: MsoAnimAfterEffect = ...
    msoAnimAfterEffectMixed: MsoAnimAfterEffect = ...
    msoAnimAfterEffectNone: MsoAnimAfterEffect = ...
    value__ = ...


class MsoAnimateByLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoAnimateByLevel, values: msoAnimateChartAllAtOnce (7), msoAnimateChartByCategory (8), msoAnimateChartByCategoryElements (9), msoAnimateChartBySeries (10), msoAnimateChartBySeriesElements (11), msoAnimateDiagramAllAtOnce (12), msoAnimateDiagramBreadthByLevel (16), msoAnimateDiagramBreadthByNode (15), msoAnimateDiagramClockwise (17), msoAnimateDiagramClockwiseIn (18), msoAnimateDiagramClockwiseOut (19), msoAnimateDiagramCounterClockwise (20), msoAnimateDiagramCounterClockwiseIn (21), msoAnimateDiagramCounterClockwiseOut (22), msoAnimateDiagramDepthByBranch (14), msoAnimateDiagramDepthByNode (13), msoAnimateDiagramDown (26), msoAnimateDiagramInByRing (23), msoAnimateDiagramOutByRing (24), msoAnimateDiagramUp (25), msoAnimateLevelMixed (-1), msoAnimateLevelNone (0), msoAnimateTextByAllLevels (1), msoAnimateTextByFifthLevel (6), msoAnimateTextByFirstLevel (2), msoAnimateTextByFourthLevel (5), msoAnimateTextBySecondLevel (3), msoAnimateTextByThirdLevel (4) """
    msoAnimateChartAllAtOnce: MsoAnimateByLevel = ...
    msoAnimateChartByCategory: MsoAnimateByLevel = ...
    msoAnimateChartByCategoryElements: MsoAnimateByLevel = ...
    msoAnimateChartBySeries: MsoAnimateByLevel = ...
    msoAnimateChartBySeriesElements: MsoAnimateByLevel = ...
    msoAnimateDiagramAllAtOnce: MsoAnimateByLevel = ...
    msoAnimateDiagramBreadthByLevel: MsoAnimateByLevel = ...
    msoAnimateDiagramBreadthByNode: MsoAnimateByLevel = ...
    msoAnimateDiagramClockwise: MsoAnimateByLevel = ...
    msoAnimateDiagramClockwiseIn: MsoAnimateByLevel = ...
    msoAnimateDiagramClockwiseOut: MsoAnimateByLevel = ...
    msoAnimateDiagramCounterClockwise: MsoAnimateByLevel = ...
    msoAnimateDiagramCounterClockwiseIn: MsoAnimateByLevel = ...
    msoAnimateDiagramCounterClockwiseOut: MsoAnimateByLevel = ...
    msoAnimateDiagramDepthByBranch: MsoAnimateByLevel = ...
    msoAnimateDiagramDepthByNode: MsoAnimateByLevel = ...
    msoAnimateDiagramDown: MsoAnimateByLevel = ...
    msoAnimateDiagramInByRing: MsoAnimateByLevel = ...
    msoAnimateDiagramOutByRing: MsoAnimateByLevel = ...
    msoAnimateDiagramUp: MsoAnimateByLevel = ...
    msoAnimateLevelMixed: MsoAnimateByLevel = ...
    msoAnimateLevelNone: MsoAnimateByLevel = ...
    msoAnimateTextByAllLevels: MsoAnimateByLevel = ...
    msoAnimateTextByFifthLevel: MsoAnimateByLevel = ...
    msoAnimateTextByFirstLevel: MsoAnimateByLevel = ...
    msoAnimateTextByFourthLevel: MsoAnimateByLevel = ...
    msoAnimateTextBySecondLevel: MsoAnimateByLevel = ...
    msoAnimateTextByThirdLevel: MsoAnimateByLevel = ...
    value__ = ...


class MsoAnimCommandType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoAnimCommandType, values: msoAnimCommandTypeCall (1), msoAnimCommandTypeEvent (0), msoAnimCommandTypeVerb (2) """
    msoAnimCommandTypeCall: MsoAnimCommandType = ...
    msoAnimCommandTypeEvent: MsoAnimCommandType = ...
    msoAnimCommandTypeVerb: MsoAnimCommandType = ...
    value__ = ...


class MsoAnimDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoAnimDirection, values: msoAnimDirectionAcross (18), msoAnimDirectionBottom (11), msoAnimDirectionBottomLeft (15), msoAnimDirectionBottomRight (14), msoAnimDirectionCenter (28), msoAnimDirectionClockwise (21), msoAnimDirectionCounterclockwise (22), msoAnimDirectionCycleClockwise (43), msoAnimDirectionCycleCounterclockwise (44), msoAnimDirectionDown (3), msoAnimDirectionDownLeft (9), msoAnimDirectionDownRight (8), msoAnimDirectionFontAllCaps (40), msoAnimDirectionFontBold (35), msoAnimDirectionFontItalic (36), msoAnimDirectionFontShadow (39), msoAnimDirectionFontStrikethrough (38), msoAnimDirectionFontUnderline (37), msoAnimDirectionGradual (42), msoAnimDirectionHorizontal (16), msoAnimDirectionHorizontalIn (23), msoAnimDirectionHorizontalOut (24), msoAnimDirectionIn (19), msoAnimDirectionInBottom (31), msoAnimDirectionInCenter (30), msoAnimDirectionInSlightly (29), msoAnimDirectionInstant (41), msoAnimDirectionLeft (4), msoAnimDirectionNone (0), msoAnimDirectionOrdinalMask (5), msoAnimDirectionOut (20), msoAnimDirectionOutBottom (34), msoAnimDirectionOutCenter (33), msoAnimDirectionOutSlightly (32), msoAnimDirectionRight (2), msoAnimDirectionSlightly (27), msoAnimDirectionTop (10), msoAnimDirectionTopLeft (12), msoAnimDirectionTopRight (13), msoAnimDirectionUp (1), msoAnimDirectionUpLeft (6), msoAnimDirectionUpRight (7), msoAnimDirectionVertical (17), msoAnimDirectionVerticalIn (25), msoAnimDirectionVerticalOut (26) """
    msoAnimDirectionAcross: MsoAnimDirection = ...
    msoAnimDirectionBottom: MsoAnimDirection = ...
    msoAnimDirectionBottomLeft: MsoAnimDirection = ...
    msoAnimDirectionBottomRight: MsoAnimDirection = ...
    msoAnimDirectionCenter: MsoAnimDirection = ...
    msoAnimDirectionClockwise: MsoAnimDirection = ...
    msoAnimDirectionCounterclockwise: MsoAnimDirection = ...
    msoAnimDirectionCycleClockwise: MsoAnimDirection = ...
    msoAnimDirectionCycleCounterclockwise: MsoAnimDirection = ...
    msoAnimDirectionDown: MsoAnimDirection = ...
    msoAnimDirectionDownLeft: MsoAnimDirection = ...
    msoAnimDirectionDownRight: MsoAnimDirection = ...
    msoAnimDirectionFontAllCaps: MsoAnimDirection = ...
    msoAnimDirectionFontBold: MsoAnimDirection = ...
    msoAnimDirectionFontItalic: MsoAnimDirection = ...
    msoAnimDirectionFontShadow: MsoAnimDirection = ...
    msoAnimDirectionFontStrikethrough: MsoAnimDirection = ...
    msoAnimDirectionFontUnderline: MsoAnimDirection = ...
    msoAnimDirectionGradual: MsoAnimDirection = ...
    msoAnimDirectionHorizontal: MsoAnimDirection = ...
    msoAnimDirectionHorizontalIn: MsoAnimDirection = ...
    msoAnimDirectionHorizontalOut: MsoAnimDirection = ...
    msoAnimDirectionIn: MsoAnimDirection = ...
    msoAnimDirectionInBottom: MsoAnimDirection = ...
    msoAnimDirectionInCenter: MsoAnimDirection = ...
    msoAnimDirectionInSlightly: MsoAnimDirection = ...
    msoAnimDirectionInstant: MsoAnimDirection = ...
    msoAnimDirectionLeft: MsoAnimDirection = ...
    msoAnimDirectionNone: MsoAnimDirection = ...
    msoAnimDirectionOrdinalMask: MsoAnimDirection = ...
    msoAnimDirectionOut: MsoAnimDirection = ...
    msoAnimDirectionOutBottom: MsoAnimDirection = ...
    msoAnimDirectionOutCenter: MsoAnimDirection = ...
    msoAnimDirectionOutSlightly: MsoAnimDirection = ...
    msoAnimDirectionRight: MsoAnimDirection = ...
    msoAnimDirectionSlightly: MsoAnimDirection = ...
    msoAnimDirectionTop: MsoAnimDirection = ...
    msoAnimDirectionTopLeft: MsoAnimDirection = ...
    msoAnimDirectionTopRight: MsoAnimDirection = ...
    msoAnimDirectionUp: MsoAnimDirection = ...
    msoAnimDirectionUpLeft: MsoAnimDirection = ...
    msoAnimDirectionUpRight: MsoAnimDirection = ...
    msoAnimDirectionVertical: MsoAnimDirection = ...
    msoAnimDirectionVerticalIn: MsoAnimDirection = ...
    msoAnimDirectionVerticalOut: MsoAnimDirection = ...
    value__ = ...


class MsoAnimEffect(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoAnimEffect, values: msoAnimEffectAppear (1), msoAnimEffectArcUp (47), msoAnimEffectAscend (39), msoAnimEffectBlast (64), msoAnimEffectBlinds (3), msoAnimEffectBoldFlash (63), msoAnimEffectBoldReveal (65), msoAnimEffectBoomerang (25), msoAnimEffectBounce (26), msoAnimEffectBox (4), msoAnimEffectBrushOnColor (66), msoAnimEffectBrushOnUnderline (67), msoAnimEffectCenterRevolve (40), msoAnimEffectChangeFillColor (54), msoAnimEffectChangeFont (55), msoAnimEffectChangeFontColor (56), msoAnimEffectChangeFontSize (57), msoAnimEffectChangeFontStyle (58), msoAnimEffectChangeLineColor (60), msoAnimEffectCheckerboard (5), msoAnimEffectCircle (6), msoAnimEffectColorBlend (68), msoAnimEffectColorReveal (27), msoAnimEffectColorWave (69), msoAnimEffectComplementaryColor (70), msoAnimEffectComplementaryColor2 (71), msoAnimEffectContrastingColor (72), msoAnimEffectCrawl (7), msoAnimEffectCredits (28), msoAnimEffectCustom (0), msoAnimEffectDarken (73), msoAnimEffectDesaturate (74), msoAnimEffectDescend (42), msoAnimEffectDiamond (8), msoAnimEffectDissolve (9), msoAnimEffectEaseIn (29), msoAnimEffectExpand (50), msoAnimEffectFade (10), msoAnimEffectFadedSwivel (41), msoAnimEffectFadedZoom (48), msoAnimEffectFlashBulb (75), msoAnimEffectFlashOnce (11), msoAnimEffectFlicker (76), msoAnimEffectFlip (51), msoAnimEffectFloat (30), msoAnimEffectFly (2), msoAnimEffectFold (53), msoAnimEffectGlide (49), msoAnimEffectGrowAndTurn (31), msoAnimEffectGrowShrink (59), msoAnimEffectGrowWithColor (77), msoAnimEffectLighten (78), msoAnimEffectLightSpeed (32), msoAnimEffectMediaPause (84), msoAnimEffectMediaPlay (83), msoAnimEffectMediaPlayFromBookmark (150), msoAnimEffectMediaStop (85), msoAnimEffectPath4PointStar (101), msoAnimEffectPath5PointStar (90), msoAnimEffectPath6PointStar (96), msoAnimEffectPath8PointStar (102), msoAnimEffectPathArcDown (122), msoAnimEffectPathArcLeft (136), msoAnimEffectPathArcRight (143), msoAnimEffectPathArcUp (129), msoAnimEffectPathBean (116), msoAnimEffectPathBounceLeft (126), msoAnimEffectPathBounceRight (139), msoAnimEffectPathBuzzsaw (110), msoAnimEffectPathCircle (86), msoAnimEffectPathCrescentMoon (91), msoAnimEffectPathCurvedSquare (105), msoAnimEffectPathCurvedX (106), msoAnimEffectPathCurvyLeft (133), msoAnimEffectPathCurvyRight (146), msoAnimEffectPathCurvyStar (108), msoAnimEffectPathDecayingWave (145), msoAnimEffectPathDiagonalDownRight (134), msoAnimEffectPathDiagonalUpRight (141), msoAnimEffectPathDiamond (88), msoAnimEffectPathDown (127), msoAnimEffectPathEqualTriangle (98), msoAnimEffectPathFigure8Four (113), msoAnimEffectPathFootball (97), msoAnimEffectPathFunnel (137), msoAnimEffectPathHeart (94), msoAnimEffectPathHeartbeat (130), msoAnimEffectPathHexagon (89), msoAnimEffectPathHorizontalFigure8 (111), msoAnimEffectPathInvertedSquare (119), msoAnimEffectPathInvertedTriangle (118), msoAnimEffectPathLeft (120), msoAnimEffectPathLoopdeLoop (109), msoAnimEffectPathNeutron (114), msoAnimEffectPathOctagon (95), msoAnimEffectPathParallelogram (99), msoAnimEffectPathPeanut (112), msoAnimEffectPathPentagon (100), msoAnimEffectPathPlus (117), msoAnimEffectPathPointyStar (104), msoAnimEffectPathRight (149), msoAnimEffectPathRightTriangle (87), msoAnimEffectPathSCurve1 (144), msoAnimEffectPathSCurve2 (124), msoAnimEffectPathSineWave (125), msoAnimEffectPathSpiralLeft (140), msoAnimEffectPathSpiralRight (131), msoAnimEffectPathSpring (138), msoAnimEffectPathSquare (92), msoAnimEffectPathStairsDown (147), msoAnimEffectPathSwoosh (115), msoAnimEffectPathTeardrop (103), msoAnimEffectPathTrapezoid (93), msoAnimEffectPathTurnDown (135), msoAnimEffectPathTurnRight (121), msoAnimEffectPathTurnUp (128), msoAnimEffectPathTurnUpRight (142), msoAnimEffectPathUp (148), msoAnimEffectPathVerticalFigure8 (107), msoAnimEffectPathWave (132), msoAnimEffectPathZigzag (123), msoAnimEffectPeek (12), msoAnimEffectPinwheel (33), msoAnimEffectPlus (13), msoAnimEffectRandomBars (14), msoAnimEffectRandomEffects (24), msoAnimEffectRiseUp (34), msoAnimEffectShimmer (52), msoAnimEffectSling (43), msoAnimEffectSpin (61), msoAnimEffectSpinner (44), msoAnimEffectSpiral (15), msoAnimEffectSplit (16), msoAnimEffectStretch (17), msoAnimEffectStretchy (45), msoAnimEffectStrips (18), msoAnimEffectStyleEmphasis (79), msoAnimEffectSwish (35), msoAnimEffectSwivel (19), msoAnimEffectTeeter (80), msoAnimEffectThinLine (36), msoAnimEffectTransparency (62), msoAnimEffectUnfold (37), msoAnimEffectVerticalGrow (81), msoAnimEffectWave (82), msoAnimEffectWedge (20), msoAnimEffectWheel (21), msoAnimEffectWhip (38), msoAnimEffectWipe (22), msoAnimEffectZip (46), msoAnimEffectZoom (23) """
    msoAnimEffectAppear: MsoAnimEffect = ...
    msoAnimEffectArcUp: MsoAnimEffect = ...
    msoAnimEffectAscend: MsoAnimEffect = ...
    msoAnimEffectBlast: MsoAnimEffect = ...
    msoAnimEffectBlinds: MsoAnimEffect = ...
    msoAnimEffectBoldFlash: MsoAnimEffect = ...
    msoAnimEffectBoldReveal: MsoAnimEffect = ...
    msoAnimEffectBoomerang: MsoAnimEffect = ...
    msoAnimEffectBounce: MsoAnimEffect = ...
    msoAnimEffectBox: MsoAnimEffect = ...
    msoAnimEffectBrushOnColor: MsoAnimEffect = ...
    msoAnimEffectBrushOnUnderline: MsoAnimEffect = ...
    msoAnimEffectCenterRevolve: MsoAnimEffect = ...
    msoAnimEffectChangeFillColor: MsoAnimEffect = ...
    msoAnimEffectChangeFont: MsoAnimEffect = ...
    msoAnimEffectChangeFontColor: MsoAnimEffect = ...
    msoAnimEffectChangeFontSize: MsoAnimEffect = ...
    msoAnimEffectChangeFontStyle: MsoAnimEffect = ...
    msoAnimEffectChangeLineColor: MsoAnimEffect = ...
    msoAnimEffectCheckerboard: MsoAnimEffect = ...
    msoAnimEffectCircle: MsoAnimEffect = ...
    msoAnimEffectColorBlend: MsoAnimEffect = ...
    msoAnimEffectColorReveal: MsoAnimEffect = ...
    msoAnimEffectColorWave: MsoAnimEffect = ...
    msoAnimEffectComplementaryColor: MsoAnimEffect = ...
    msoAnimEffectComplementaryColor2: MsoAnimEffect = ...
    msoAnimEffectContrastingColor: MsoAnimEffect = ...
    msoAnimEffectCrawl: MsoAnimEffect = ...
    msoAnimEffectCredits: MsoAnimEffect = ...
    msoAnimEffectCustom: MsoAnimEffect = ...
    msoAnimEffectDarken: MsoAnimEffect = ...
    msoAnimEffectDesaturate: MsoAnimEffect = ...
    msoAnimEffectDescend: MsoAnimEffect = ...
    msoAnimEffectDiamond: MsoAnimEffect = ...
    msoAnimEffectDissolve: MsoAnimEffect = ...
    msoAnimEffectEaseIn: MsoAnimEffect = ...
    msoAnimEffectExpand: MsoAnimEffect = ...
    msoAnimEffectFade: MsoAnimEffect = ...
    msoAnimEffectFadedSwivel: MsoAnimEffect = ...
    msoAnimEffectFadedZoom: MsoAnimEffect = ...
    msoAnimEffectFlashBulb: MsoAnimEffect = ...
    msoAnimEffectFlashOnce: MsoAnimEffect = ...
    msoAnimEffectFlicker: MsoAnimEffect = ...
    msoAnimEffectFlip: MsoAnimEffect = ...
    msoAnimEffectFloat: MsoAnimEffect = ...
    msoAnimEffectFly: MsoAnimEffect = ...
    msoAnimEffectFold: MsoAnimEffect = ...
    msoAnimEffectGlide: MsoAnimEffect = ...
    msoAnimEffectGrowAndTurn: MsoAnimEffect = ...
    msoAnimEffectGrowShrink: MsoAnimEffect = ...
    msoAnimEffectGrowWithColor: MsoAnimEffect = ...
    msoAnimEffectLighten: MsoAnimEffect = ...
    msoAnimEffectLightSpeed: MsoAnimEffect = ...
    msoAnimEffectMediaPause: MsoAnimEffect = ...
    msoAnimEffectMediaPlay: MsoAnimEffect = ...
    msoAnimEffectMediaPlayFromBookmark: MsoAnimEffect = ...
    msoAnimEffectMediaStop: MsoAnimEffect = ...
    msoAnimEffectPath4PointStar: MsoAnimEffect = ...
    msoAnimEffectPath5PointStar: MsoAnimEffect = ...
    msoAnimEffectPath6PointStar: MsoAnimEffect = ...
    msoAnimEffectPath8PointStar: MsoAnimEffect = ...
    msoAnimEffectPathArcDown: MsoAnimEffect = ...
    msoAnimEffectPathArcLeft: MsoAnimEffect = ...
    msoAnimEffectPathArcRight: MsoAnimEffect = ...
    msoAnimEffectPathArcUp: MsoAnimEffect = ...
    msoAnimEffectPathBean: MsoAnimEffect = ...
    msoAnimEffectPathBounceLeft: MsoAnimEffect = ...
    msoAnimEffectPathBounceRight: MsoAnimEffect = ...
    msoAnimEffectPathBuzzsaw: MsoAnimEffect = ...
    msoAnimEffectPathCircle: MsoAnimEffect = ...
    msoAnimEffectPathCrescentMoon: MsoAnimEffect = ...
    msoAnimEffectPathCurvedSquare: MsoAnimEffect = ...
    msoAnimEffectPathCurvedX: MsoAnimEffect = ...
    msoAnimEffectPathCurvyLeft: MsoAnimEffect = ...
    msoAnimEffectPathCurvyRight: MsoAnimEffect = ...
    msoAnimEffectPathCurvyStar: MsoAnimEffect = ...
    msoAnimEffectPathDecayingWave: MsoAnimEffect = ...
    msoAnimEffectPathDiagonalDownRight: MsoAnimEffect = ...
    msoAnimEffectPathDiagonalUpRight: MsoAnimEffect = ...
    msoAnimEffectPathDiamond: MsoAnimEffect = ...
    msoAnimEffectPathDown: MsoAnimEffect = ...
    msoAnimEffectPathEqualTriangle: MsoAnimEffect = ...
    msoAnimEffectPathFigure8Four: MsoAnimEffect = ...
    msoAnimEffectPathFootball: MsoAnimEffect = ...
    msoAnimEffectPathFunnel: MsoAnimEffect = ...
    msoAnimEffectPathHeart: MsoAnimEffect = ...
    msoAnimEffectPathHeartbeat: MsoAnimEffect = ...
    msoAnimEffectPathHexagon: MsoAnimEffect = ...
    msoAnimEffectPathHorizontalFigure8: MsoAnimEffect = ...
    msoAnimEffectPathInvertedSquare: MsoAnimEffect = ...
    msoAnimEffectPathInvertedTriangle: MsoAnimEffect = ...
    msoAnimEffectPathLeft: MsoAnimEffect = ...
    msoAnimEffectPathLoopdeLoop: MsoAnimEffect = ...
    msoAnimEffectPathNeutron: MsoAnimEffect = ...
    msoAnimEffectPathOctagon: MsoAnimEffect = ...
    msoAnimEffectPathParallelogram: MsoAnimEffect = ...
    msoAnimEffectPathPeanut: MsoAnimEffect = ...
    msoAnimEffectPathPentagon: MsoAnimEffect = ...
    msoAnimEffectPathPlus: MsoAnimEffect = ...
    msoAnimEffectPathPointyStar: MsoAnimEffect = ...
    msoAnimEffectPathRight: MsoAnimEffect = ...
    msoAnimEffectPathRightTriangle: MsoAnimEffect = ...
    msoAnimEffectPathSCurve1: MsoAnimEffect = ...
    msoAnimEffectPathSCurve2: MsoAnimEffect = ...
    msoAnimEffectPathSineWave: MsoAnimEffect = ...
    msoAnimEffectPathSpiralLeft: MsoAnimEffect = ...
    msoAnimEffectPathSpiralRight: MsoAnimEffect = ...
    msoAnimEffectPathSpring: MsoAnimEffect = ...
    msoAnimEffectPathSquare: MsoAnimEffect = ...
    msoAnimEffectPathStairsDown: MsoAnimEffect = ...
    msoAnimEffectPathSwoosh: MsoAnimEffect = ...
    msoAnimEffectPathTeardrop: MsoAnimEffect = ...
    msoAnimEffectPathTrapezoid: MsoAnimEffect = ...
    msoAnimEffectPathTurnDown: MsoAnimEffect = ...
    msoAnimEffectPathTurnRight: MsoAnimEffect = ...
    msoAnimEffectPathTurnUp: MsoAnimEffect = ...
    msoAnimEffectPathTurnUpRight: MsoAnimEffect = ...
    msoAnimEffectPathUp: MsoAnimEffect = ...
    msoAnimEffectPathVerticalFigure8: MsoAnimEffect = ...
    msoAnimEffectPathWave: MsoAnimEffect = ...
    msoAnimEffectPathZigzag: MsoAnimEffect = ...
    msoAnimEffectPeek: MsoAnimEffect = ...
    msoAnimEffectPinwheel: MsoAnimEffect = ...
    msoAnimEffectPlus: MsoAnimEffect = ...
    msoAnimEffectRandomBars: MsoAnimEffect = ...
    msoAnimEffectRandomEffects: MsoAnimEffect = ...
    msoAnimEffectRiseUp: MsoAnimEffect = ...
    msoAnimEffectShimmer: MsoAnimEffect = ...
    msoAnimEffectSling: MsoAnimEffect = ...
    msoAnimEffectSpin: MsoAnimEffect = ...
    msoAnimEffectSpinner: MsoAnimEffect = ...
    msoAnimEffectSpiral: MsoAnimEffect = ...
    msoAnimEffectSplit: MsoAnimEffect = ...
    msoAnimEffectStretch: MsoAnimEffect = ...
    msoAnimEffectStretchy: MsoAnimEffect = ...
    msoAnimEffectStrips: MsoAnimEffect = ...
    msoAnimEffectStyleEmphasis: MsoAnimEffect = ...
    msoAnimEffectSwish: MsoAnimEffect = ...
    msoAnimEffectSwivel: MsoAnimEffect = ...
    msoAnimEffectTeeter: MsoAnimEffect = ...
    msoAnimEffectThinLine: MsoAnimEffect = ...
    msoAnimEffectTransparency: MsoAnimEffect = ...
    msoAnimEffectUnfold: MsoAnimEffect = ...
    msoAnimEffectVerticalGrow: MsoAnimEffect = ...
    msoAnimEffectWave: MsoAnimEffect = ...
    msoAnimEffectWedge: MsoAnimEffect = ...
    msoAnimEffectWheel: MsoAnimEffect = ...
    msoAnimEffectWhip: MsoAnimEffect = ...
    msoAnimEffectWipe: MsoAnimEffect = ...
    msoAnimEffectZip: MsoAnimEffect = ...
    msoAnimEffectZoom: MsoAnimEffect = ...
    value__ = ...


class MsoAnimEffectAfter(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoAnimEffectAfter, values: msoAnimEffectAfterFreeze (1), msoAnimEffectAfterHold (3), msoAnimEffectAfterRemove (2), msoAnimEffectAfterTransition (4) """
    msoAnimEffectAfterFreeze: MsoAnimEffectAfter = ...
    msoAnimEffectAfterHold: MsoAnimEffectAfter = ...
    msoAnimEffectAfterRemove: MsoAnimEffectAfter = ...
    msoAnimEffectAfterTransition: MsoAnimEffectAfter = ...
    value__ = ...


class MsoAnimEffectRestart(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoAnimEffectRestart, values: msoAnimEffectRestartAlways (1), msoAnimEffectRestartNever (3), msoAnimEffectRestartWhenOff (2) """
    msoAnimEffectRestartAlways: MsoAnimEffectRestart = ...
    msoAnimEffectRestartNever: MsoAnimEffectRestart = ...
    msoAnimEffectRestartWhenOff: MsoAnimEffectRestart = ...
    value__ = ...


class MsoAnimFilterEffectSubtype(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoAnimFilterEffectSubtype, values: msoAnimFilterEffectSubtypeAcross (9), msoAnimFilterEffectSubtypeDown (25), msoAnimFilterEffectSubtypeDownLeft (14), msoAnimFilterEffectSubtypeDownRight (16), msoAnimFilterEffectSubtypeFromBottom (13), msoAnimFilterEffectSubtypeFromLeft (10), msoAnimFilterEffectSubtypeFromRight (11), msoAnimFilterEffectSubtypeFromTop (12), msoAnimFilterEffectSubtypeHorizontal (5), msoAnimFilterEffectSubtypeIn (7), msoAnimFilterEffectSubtypeInHorizontal (3), msoAnimFilterEffectSubtypeInVertical (1), msoAnimFilterEffectSubtypeLeft (23), msoAnimFilterEffectSubtypeNone (0), msoAnimFilterEffectSubtypeOut (8), msoAnimFilterEffectSubtypeOutHorizontal (4), msoAnimFilterEffectSubtypeOutVertical (2), msoAnimFilterEffectSubtypeRight (24), msoAnimFilterEffectSubtypeSpokes1 (18), msoAnimFilterEffectSubtypeSpokes2 (19), msoAnimFilterEffectSubtypeSpokes3 (20), msoAnimFilterEffectSubtypeSpokes4 (21), msoAnimFilterEffectSubtypeSpokes8 (22), msoAnimFilterEffectSubtypeUp (26), msoAnimFilterEffectSubtypeUpLeft (15), msoAnimFilterEffectSubtypeUpRight (17), msoAnimFilterEffectSubtypeVertical (6) """
    msoAnimFilterEffectSubtypeAcross: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeDown: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeDownLeft: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeDownRight: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeFromBottom: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeFromLeft: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeFromRight: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeFromTop: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeHorizontal: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeIn: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeInHorizontal: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeInVertical: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeLeft: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeNone: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeOut: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeOutHorizontal: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeOutVertical: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeRight: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeSpokes1: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeSpokes2: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeSpokes3: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeSpokes4: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeSpokes8: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeUp: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeUpLeft: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeUpRight: MsoAnimFilterEffectSubtype = ...
    msoAnimFilterEffectSubtypeVertical: MsoAnimFilterEffectSubtype = ...
    value__ = ...


class MsoAnimFilterEffectType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoAnimFilterEffectType, values: msoAnimFilterEffectTypeBarn (1), msoAnimFilterEffectTypeBlinds (2), msoAnimFilterEffectTypeBox (3), msoAnimFilterEffectTypeCheckerboard (4), msoAnimFilterEffectTypeCircle (5), msoAnimFilterEffectTypeDiamond (6), msoAnimFilterEffectTypeDissolve (7), msoAnimFilterEffectTypeFade (8), msoAnimFilterEffectTypeImage (9), msoAnimFilterEffectTypeNone (0), msoAnimFilterEffectTypePixelate (10), msoAnimFilterEffectTypePlus (11), msoAnimFilterEffectTypeRandomBar (12), msoAnimFilterEffectTypeSlide (13), msoAnimFilterEffectTypeStretch (14), msoAnimFilterEffectTypeStrips (15), msoAnimFilterEffectTypeWedge (16), msoAnimFilterEffectTypeWheel (17), msoAnimFilterEffectTypeWipe (18) """
    msoAnimFilterEffectTypeBarn: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypeBlinds: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypeBox: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypeCheckerboard: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypeCircle: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypeDiamond: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypeDissolve: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypeFade: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypeImage: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypeNone: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypePixelate: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypePlus: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypeRandomBar: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypeSlide: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypeStretch: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypeStrips: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypeWedge: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypeWheel: MsoAnimFilterEffectType = ...
    msoAnimFilterEffectTypeWipe: MsoAnimFilterEffectType = ...
    value__ = ...


class MsoAnimProperty(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoAnimProperty, values: msoAnimColor (7), msoAnimHeight (4), msoAnimNone (0), msoAnimOpacity (5), msoAnimRotation (6), msoAnimShapeFillBackColor (1007), msoAnimShapeFillColor (1005), msoAnimShapeFillOn (1004), msoAnimShapeFillOpacity (1006), msoAnimShapeLineColor (1009), msoAnimShapeLineOn (1008), msoAnimShapePictureBrightness (1001), msoAnimShapePictureContrast (1000), msoAnimShapePictureGamma (1002), msoAnimShapePictureGrayscale (1003), msoAnimShapeShadowColor (1012), msoAnimShapeShadowOffsetX (1014), msoAnimShapeShadowOffsetY (1015), msoAnimShapeShadowOn (1010), msoAnimShapeShadowOpacity (1013), msoAnimShapeShadowType (1011), msoAnimTextBulletCharacter (111), msoAnimTextBulletColor (114), msoAnimTextBulletFontName (112), msoAnimTextBulletNumber (113), msoAnimTextBulletRelativeSize (115), msoAnimTextBulletStyle (116), msoAnimTextBulletType (117), msoAnimTextFontBold (100), msoAnimTextFontColor (101), msoAnimTextFontEmboss (102), msoAnimTextFontItalic (103), msoAnimTextFontName (104), msoAnimTextFontShadow (105), msoAnimTextFontSize (106), msoAnimTextFontStrikeThrough (110), msoAnimTextFontSubscript (107), msoAnimTextFontSuperscript (108), msoAnimTextFontUnderline (109), msoAnimVisibility (8), msoAnimWidth (3), msoAnimX (1), msoAnimY (2) """
    msoAnimColor: MsoAnimProperty = ...
    msoAnimHeight: MsoAnimProperty = ...
    msoAnimNone: MsoAnimProperty = ...
    msoAnimOpacity: MsoAnimProperty = ...
    msoAnimRotation: MsoAnimProperty = ...
    msoAnimShapeFillBackColor: MsoAnimProperty = ...
    msoAnimShapeFillColor: MsoAnimProperty = ...
    msoAnimShapeFillOn: MsoAnimProperty = ...
    msoAnimShapeFillOpacity: MsoAnimProperty = ...
    msoAnimShapeLineColor: MsoAnimProperty = ...
    msoAnimShapeLineOn: MsoAnimProperty = ...
    msoAnimShapePictureBrightness: MsoAnimProperty = ...
    msoAnimShapePictureContrast: MsoAnimProperty = ...
    msoAnimShapePictureGamma: MsoAnimProperty = ...
    msoAnimShapePictureGrayscale: MsoAnimProperty = ...
    msoAnimShapeShadowColor: MsoAnimProperty = ...
    msoAnimShapeShadowOffsetX: MsoAnimProperty = ...
    msoAnimShapeShadowOffsetY: MsoAnimProperty = ...
    msoAnimShapeShadowOn: MsoAnimProperty = ...
    msoAnimShapeShadowOpacity: MsoAnimProperty = ...
    msoAnimShapeShadowType: MsoAnimProperty = ...
    msoAnimTextBulletCharacter: MsoAnimProperty = ...
    msoAnimTextBulletColor: MsoAnimProperty = ...
    msoAnimTextBulletFontName: MsoAnimProperty = ...
    msoAnimTextBulletNumber: MsoAnimProperty = ...
    msoAnimTextBulletRelativeSize: MsoAnimProperty = ...
    msoAnimTextBulletStyle: MsoAnimProperty = ...
    msoAnimTextBulletType: MsoAnimProperty = ...
    msoAnimTextFontBold: MsoAnimProperty = ...
    msoAnimTextFontColor: MsoAnimProperty = ...
    msoAnimTextFontEmboss: MsoAnimProperty = ...
    msoAnimTextFontItalic: MsoAnimProperty = ...
    msoAnimTextFontName: MsoAnimProperty = ...
    msoAnimTextFontShadow: MsoAnimProperty = ...
    msoAnimTextFontSize: MsoAnimProperty = ...
    msoAnimTextFontStrikeThrough: MsoAnimProperty = ...
    msoAnimTextFontSubscript: MsoAnimProperty = ...
    msoAnimTextFontSuperscript: MsoAnimProperty = ...
    msoAnimTextFontUnderline: MsoAnimProperty = ...
    msoAnimVisibility: MsoAnimProperty = ...
    msoAnimWidth: MsoAnimProperty = ...
    msoAnimX: MsoAnimProperty = ...
    msoAnimY: MsoAnimProperty = ...
    value__ = ...


class MsoAnimTextUnitEffect(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoAnimTextUnitEffect, values: msoAnimTextUnitEffectByCharacter (1), msoAnimTextUnitEffectByParagraph (0), msoAnimTextUnitEffectByWord (2), msoAnimTextUnitEffectMixed (-1) """
    msoAnimTextUnitEffectByCharacter: MsoAnimTextUnitEffect = ...
    msoAnimTextUnitEffectByParagraph: MsoAnimTextUnitEffect = ...
    msoAnimTextUnitEffectByWord: MsoAnimTextUnitEffect = ...
    msoAnimTextUnitEffectMixed: MsoAnimTextUnitEffect = ...
    value__ = ...


class MsoAnimTriggerType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoAnimTriggerType, values: msoAnimTriggerAfterPrevious (3), msoAnimTriggerMixed (-1), msoAnimTriggerNone (0), msoAnimTriggerOnMediaBookmark (5), msoAnimTriggerOnPageClick (1), msoAnimTriggerOnShapeClick (4), msoAnimTriggerWithPrevious (2) """
    msoAnimTriggerAfterPrevious: MsoAnimTriggerType = ...
    msoAnimTriggerMixed: MsoAnimTriggerType = ...
    msoAnimTriggerNone: MsoAnimTriggerType = ...
    msoAnimTriggerOnMediaBookmark: MsoAnimTriggerType = ...
    msoAnimTriggerOnPageClick: MsoAnimTriggerType = ...
    msoAnimTriggerOnShapeClick: MsoAnimTriggerType = ...
    msoAnimTriggerWithPrevious: MsoAnimTriggerType = ...
    value__ = ...


class MsoAnimType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoAnimType, values: msoAnimTypeColor (2), msoAnimTypeCommand (6), msoAnimTypeFilter (7), msoAnimTypeMixed (-2), msoAnimTypeMotion (1), msoAnimTypeNone (0), msoAnimTypeProperty (5), msoAnimTypeRotation (4), msoAnimTypeScale (3), msoAnimTypeSet (8) """
    msoAnimTypeColor: MsoAnimType = ...
    msoAnimTypeCommand: MsoAnimType = ...
    msoAnimTypeFilter: MsoAnimType = ...
    msoAnimTypeMixed: MsoAnimType = ...
    msoAnimTypeMotion: MsoAnimType = ...
    msoAnimTypeNone: MsoAnimType = ...
    msoAnimTypeProperty: MsoAnimType = ...
    msoAnimTypeRotation: MsoAnimType = ...
    msoAnimTypeScale: MsoAnimType = ...
    msoAnimTypeSet: MsoAnimType = ...
    value__ = ...


class MsoClickState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsoClickState, values: msoClickStateAfterAllAnimations (-2), msoClickStateBeforeAutomaticAnimations (-1) """
    msoClickStateAfterAllAnimations: MsoClickState = ...
    msoClickStateBeforeAutomaticAnimations: MsoClickState = ...
    value__ = ...


class NamedSlideShow: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: NamedSlideShow) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: NamedSlideShow) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: NamedSlideShow) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: NamedSlideShow) -> object """
        ...

    @property
    def SlideIDs(self) -> object:
        """ Get: SlideIDs(self: NamedSlideShow) -> object """
        ...


    def Delete(self): # -> 
        """ Delete(self: NamedSlideShow) """
        ...


class NamedSlideShows(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: NamedSlideShows) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: NamedSlideShows) -> object """
        ...


    def Add(self, Name:str, safeArrayOfSlideIDs:object) -> NamedSlideShow:
        """ Add(self: NamedSlideShows, Name: str, safeArrayOfSlideIDs: object) -> NamedSlideShow """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ObjectVerbs(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ObjectVerbs) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ObjectVerbs) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class OCXExtender: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AltHTML(self) -> str:
        """
        Get: AltHTML(self: OCXExtender) -> str
        Set: AltHTML(self: OCXExtender) = value
        """
        ...

    @property
    def Height(self) -> Single:
        """
        Get: Height(self: OCXExtender) -> Single
        Set: Height(self: OCXExtender) = value
        """
        ...

    @property
    def Left(self) -> Single:
        """
        Get: Left(self: OCXExtender) -> Single
        Set: Left(self: OCXExtender) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: OCXExtender) -> str
        Set: Name(self: OCXExtender) = value
        """
        ...

    @property
    def Top(self) -> Single:
        """
        Get: Top(self: OCXExtender) -> Single
        Set: Top(self: OCXExtender) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: OCXExtender) -> bool
        Set: Visible(self: OCXExtender) = value
        """
        ...

    @property
    def Width(self) -> Single:
        """
        Get: Width(self: OCXExtender) -> Single
        Set: Width(self: OCXExtender) = value
        """
        ...

    @property
    def ZOrderPosition(self) -> int:
        """ Get: ZOrderPosition(self: OCXExtender) -> int """
        ...



class OCXExtenderEvents: # skipped bases: <type 'object'>
    """ no doc """
    def GotFocus(self): # -> 
        """ GotFocus(self: OCXExtenderEvents) """
        ...

    def LostFocus(self): # -> 
        """ LostFocus(self: OCXExtenderEvents) """
        ...


class OCXExtenderEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_GotFocus(self): # -> 
        """ add_GotFocus(self: OCXExtenderEvents_Event, : OCXExtenderEvents_GotFocusEventHandler) """
        ...

    def add_LostFocus(self): # -> 
        """ add_LostFocus(self: OCXExtenderEvents_Event, : OCXExtenderEvents_LostFocusEventHandler) """
        ...

    def remove_GotFocus(self): # -> 
        """ remove_GotFocus(self: OCXExtenderEvents_Event, : OCXExtenderEvents_GotFocusEventHandler) """
        ...

    def remove_LostFocus(self): # -> 
        """ remove_LostFocus(self: OCXExtenderEvents_Event, : OCXExtenderEvents_LostFocusEventHandler) """
        ...

    GotFocus = ...
    LostFocus = ...


class OCXExtenderEvents_GotFocusEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OCXExtenderEvents_GotFocusEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: OCXExtenderEvents_GotFocusEventHandler) """
        ...


class OCXExtenderEvents_LostFocusEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OCXExtenderEvents_LostFocusEventHandler(: object, : UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: OCXExtenderEvents_LostFocusEventHandler) """
        ...


class OCXExtenderEvents_SinkHelper(OCXExtenderEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_dwCookie = ...
    m_GotFocusDelegate = ...
    m_LostFocusDelegate = ...


class OLEControl(OCXExtenderEvents_Event, OCXExtender): # skipped bases: <type 'object'>
    """ no doc """
    pass

class OLEControlClass(OLEControl, __ComObject): # skipped bases: <type 'OCXExtenderEvents_Event'>, <type 'OCXExtender'>, <type 'object'>
    """ OLEControlClass() """
    @property
    def AltHTML(self) -> str:
        """
        Get: AltHTML(self: OLEControlClass) -> str
        Set: AltHTML(self: OLEControlClass) = value
        """
        ...

    @property
    def Height(self) -> Single:
        """
        Get: Height(self: OLEControlClass) -> Single
        Set: Height(self: OLEControlClass) = value
        """
        ...

    @property
    def Left(self) -> Single:
        """
        Get: Left(self: OLEControlClass) -> Single
        Set: Left(self: OLEControlClass) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: OLEControlClass) -> str
        Set: Name(self: OLEControlClass) = value
        """
        ...

    @property
    def Top(self) -> Single:
        """
        Get: Top(self: OLEControlClass) -> Single
        Set: Top(self: OLEControlClass) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: OLEControlClass) -> bool
        Set: Visible(self: OLEControlClass) = value
        """
        ...

    @property
    def Width(self) -> Single:
        """
        Get: Width(self: OLEControlClass) -> Single
        Set: Width(self: OLEControlClass) = value
        """
        ...

    @property
    def ZOrderPosition(self) -> int:
        """ Get: ZOrderPosition(self: OLEControlClass) -> int """
        ...


    def add_GotFocus(self): # -> 
        """ add_GotFocus(self: OLEControlClass, : OCXExtenderEvents_GotFocusEventHandler) """
        ...

    def add_LostFocus(self): # -> 
        """ add_LostFocus(self: OLEControlClass, : OCXExtenderEvents_LostFocusEventHandler) """
        ...

    def remove_GotFocus(self): # -> 
        """ remove_GotFocus(self: OLEControlClass, : OCXExtenderEvents_GotFocusEventHandler) """
        ...

    def remove_LostFocus(self): # -> 
        """ remove_LostFocus(self: OLEControlClass, : OCXExtenderEvents_LostFocusEventHandler) """
        ...

    GotFocus = ...
    LostFocus = ...


class OLEFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: OLEFormat) -> Application """
        ...

    @property
    def FollowColors(self) -> PpFollowColors:
        """
        Get: FollowColors(self: OLEFormat) -> PpFollowColors
        Set: FollowColors(self: OLEFormat) = value
        """
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
    def ProgID(self) -> str:
        """ Get: ProgID(self: OLEFormat) -> str """
        ...


    def Activate(self): # -> 
        """ Activate(self: OLEFormat) """
        ...

    def DoVerb(self, Index:int): # -> 
        """ DoVerb(self: OLEFormat, Index: int) """
        ...


class Options: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DisplayPasteOptions(self): # -> MsoTriState
        """
        Get: DisplayPasteOptions(self: Options) -> MsoTriState
        Set: DisplayPasteOptions(self: Options) = value
        """
        ...

    @property
    def DoNotPromptForConvert(self): # -> MsoTriState
        """
        Get: DoNotPromptForConvert(self: Options) -> MsoTriState
        Set: DoNotPromptForConvert(self: Options) = value
        """
        ...

    @property
    def ShowCoauthoringMergeChanges(self) -> bool:
        """
        Get: ShowCoauthoringMergeChanges(self: Options) -> bool
        Set: ShowCoauthoringMergeChanges(self: Options) = value
        """
        ...



class PageSetup: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PageSetup) -> Application """
        ...

    @property
    def FirstSlideNumber(self) -> int:
        """
        Get: FirstSlideNumber(self: PageSetup) -> int
        Set: FirstSlideNumber(self: PageSetup) = value
        """
        ...

    @property
    def NotesOrientation(self): # -> MsoOrientation
        """
        Get: NotesOrientation(self: PageSetup) -> MsoOrientation
        Set: NotesOrientation(self: PageSetup) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PageSetup) -> object """
        ...

    @property
    def SlideHeight(self) -> Single:
        """
        Get: SlideHeight(self: PageSetup) -> Single
        Set: SlideHeight(self: PageSetup) = value
        """
        ...

    @property
    def SlideOrientation(self): # -> MsoOrientation
        """
        Get: SlideOrientation(self: PageSetup) -> MsoOrientation
        Set: SlideOrientation(self: PageSetup) = value
        """
        ...

    @property
    def SlideSize(self) -> PpSlideSizeType:
        """
        Get: SlideSize(self: PageSetup) -> PpSlideSizeType
        Set: SlideSize(self: PageSetup) = value
        """
        ...

    @property
    def SlideWidth(self) -> Single:
        """
        Get: SlideWidth(self: PageSetup) -> Single
        Set: SlideWidth(self: PageSetup) = value
        """
        ...



class Pane: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Active(self): # -> MsoTriState
        """ Get: Active(self: Pane) -> MsoTriState """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: Pane) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Pane) -> object """
        ...

    @property
    def ViewType(self) -> PpViewType:
        """ Get: ViewType(self: Pane) -> PpViewType """
        ...


    def Activate(self): # -> 
        """ Activate(self: Pane) """
        ...


class Panes(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Panes) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Panes) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ParagraphFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Alignment(self) -> PpParagraphAlignment:
        """
        Get: Alignment(self: ParagraphFormat) -> PpParagraphAlignment
        Set: Alignment(self: ParagraphFormat) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: ParagraphFormat) -> Application """
        ...

    @property
    def BaseLineAlignment(self) -> PpBaselineAlignment:
        """
        Get: BaseLineAlignment(self: ParagraphFormat) -> PpBaselineAlignment
        Set: BaseLineAlignment(self: ParagraphFormat) = value
        """
        ...

    @property
    def Bullet(self) -> BulletFormat:
        """ Get: Bullet(self: ParagraphFormat) -> BulletFormat """
        ...

    @property
    def FarEastLineBreakControl(self): # -> MsoTriState
        """
        Get: FarEastLineBreakControl(self: ParagraphFormat) -> MsoTriState
        Set: FarEastLineBreakControl(self: ParagraphFormat) = value
        """
        ...

    @property
    def HangingPunctuation(self): # -> MsoTriState
        """
        Get: HangingPunctuation(self: ParagraphFormat) -> MsoTriState
        Set: HangingPunctuation(self: ParagraphFormat) = value
        """
        ...

    @property
    def LineRuleAfter(self): # -> MsoTriState
        """
        Get: LineRuleAfter(self: ParagraphFormat) -> MsoTriState
        Set: LineRuleAfter(self: ParagraphFormat) = value
        """
        ...

    @property
    def LineRuleBefore(self): # -> MsoTriState
        """
        Get: LineRuleBefore(self: ParagraphFormat) -> MsoTriState
        Set: LineRuleBefore(self: ParagraphFormat) = value
        """
        ...

    @property
    def LineRuleWithin(self): # -> MsoTriState
        """
        Get: LineRuleWithin(self: ParagraphFormat) -> MsoTriState
        Set: LineRuleWithin(self: ParagraphFormat) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ParagraphFormat) -> object """
        ...

    @property
    def SpaceAfter(self) -> Single:
        """
        Get: SpaceAfter(self: ParagraphFormat) -> Single
        Set: SpaceAfter(self: ParagraphFormat) = value
        """
        ...

    @property
    def SpaceBefore(self) -> Single:
        """
        Get: SpaceBefore(self: ParagraphFormat) -> Single
        Set: SpaceBefore(self: ParagraphFormat) = value
        """
        ...

    @property
    def SpaceWithin(self) -> Single:
        """
        Get: SpaceWithin(self: ParagraphFormat) -> Single
        Set: SpaceWithin(self: ParagraphFormat) = value
        """
        ...

    @property
    def TextDirection(self) -> PpDirection:
        """
        Get: TextDirection(self: ParagraphFormat) -> PpDirection
        Set: TextDirection(self: ParagraphFormat) = value
        """
        ...

    @property
    def WordWrap(self): # -> MsoTriState
        """
        Get: WordWrap(self: ParagraphFormat) -> MsoTriState
        Set: WordWrap(self: ParagraphFormat) = value
        """
        ...



class PictureFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: PictureFormat) -> object """
        ...

    @property
    def Brightness(self) -> Single:
        """
        Get: Brightness(self: PictureFormat) -> Single
        Set: Brightness(self: PictureFormat) = value
        """
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
    def Creator(self) -> int:
        """ Get: Creator(self: PictureFormat) -> int """
        ...

    @property
    def Crop(self): # -> Crop
        """ Get: Crop(self: PictureFormat) -> Crop """
        ...

    @property
    def CropBottom(self) -> Single:
        """
        Get: CropBottom(self: PictureFormat) -> Single
        Set: CropBottom(self: PictureFormat) = value
        """
        ...

    @property
    def CropLeft(self) -> Single:
        """
        Get: CropLeft(self: PictureFormat) -> Single
        Set: CropLeft(self: PictureFormat) = value
        """
        ...

    @property
    def CropRight(self) -> Single:
        """
        Get: CropRight(self: PictureFormat) -> Single
        Set: CropRight(self: PictureFormat) = value
        """
        ...

    @property
    def CropTop(self) -> Single:
        """
        Get: CropTop(self: PictureFormat) -> Single
        Set: CropTop(self: PictureFormat) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PictureFormat) -> object """
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


    def IncrementBrightness(self, Increment:Single): # -> 
        """ IncrementBrightness(self: PictureFormat, Increment: Single) """
        ...

    def IncrementContrast(self, Increment:Single): # -> 
        """ IncrementContrast(self: PictureFormat, Increment: Single) """
        ...


class PlaceholderFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PlaceholderFormat) -> Application """
        ...

    @property
    def ContainedType(self): # -> MsoShapeType
        """ Get: ContainedType(self: PlaceholderFormat) -> MsoShapeType """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: PlaceholderFormat) -> str
        Set: Name(self: PlaceholderFormat) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PlaceholderFormat) -> object """
        ...

    @property
    def Type(self) -> PpPlaceholderType:
        """ Get: Type(self: PlaceholderFormat) -> PpPlaceholderType """
        ...



class Placeholders(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Placeholders) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Placeholders) -> object """
        ...


    def FindByName(self, Index:object) -> Shape:
        """ FindByName(self: Placeholders, Index: object) -> Shape """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Player: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Player) -> Application """
        ...

    @property
    def CurrentPosition(self) -> int:
        """
        Get: CurrentPosition(self: Player) -> int
        Set: CurrentPosition(self: Player) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Player) -> object """
        ...

    @property
    def State(self) -> PpPlayerState:
        """ Get: State(self: Player) -> PpPlayerState """
        ...


    def GoToNextBookmark(self): # -> 
        """ GoToNextBookmark(self: Player) """
        ...

    def GoToPreviousBookmark(self): # -> 
        """ GoToPreviousBookmark(self: Player) """
        ...

    def Pause(self): # -> 
        """ Pause(self: Player) """
        ...

    def Play(self): # -> 
        """ Play(self: Player) """
        ...

    def Stop(self): # -> 
        """ Stop(self: Player) """
        ...


class PlaySettings: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActionVerb(self) -> str:
        """
        Get: ActionVerb(self: PlaySettings) -> str
        Set: ActionVerb(self: PlaySettings) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: PlaySettings) -> Application """
        ...

    @property
    def HideWhileNotPlaying(self): # -> MsoTriState
        """
        Get: HideWhileNotPlaying(self: PlaySettings) -> MsoTriState
        Set: HideWhileNotPlaying(self: PlaySettings) = value
        """
        ...

    @property
    def LoopUntilStopped(self): # -> MsoTriState
        """
        Get: LoopUntilStopped(self: PlaySettings) -> MsoTriState
        Set: LoopUntilStopped(self: PlaySettings) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PlaySettings) -> object """
        ...

    @property
    def PauseAnimation(self): # -> MsoTriState
        """
        Get: PauseAnimation(self: PlaySettings) -> MsoTriState
        Set: PauseAnimation(self: PlaySettings) = value
        """
        ...

    @property
    def PlayOnEntry(self): # -> MsoTriState
        """
        Get: PlayOnEntry(self: PlaySettings) -> MsoTriState
        Set: PlayOnEntry(self: PlaySettings) = value
        """
        ...

    @property
    def RewindMovie(self): # -> MsoTriState
        """
        Get: RewindMovie(self: PlaySettings) -> MsoTriState
        Set: RewindMovie(self: PlaySettings) = value
        """
        ...

    @property
    def StopAfterSlides(self) -> int:
        """
        Get: StopAfterSlides(self: PlaySettings) -> int
        Set: StopAfterSlides(self: PlaySettings) = value
        """
        ...



class PlotArea: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PlotArea) -> Application """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: PlotArea) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: PlotArea) -> int """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: PlotArea) -> ChartFillFormat """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: PlotArea) -> ChartFormat """
        ...

    @property
    def Height(self) -> float:
        """
        Get: Height(self: PlotArea) -> float
        Set: Height(self: PlotArea) = value
        """
        ...

    @property
    def InsideHeight(self) -> float:
        """
        Get: InsideHeight(self: PlotArea) -> float
        Set: InsideHeight(self: PlotArea) = value
        """
        ...

    @property
    def InsideLeft(self) -> float:
        """
        Get: InsideLeft(self: PlotArea) -> float
        Set: InsideLeft(self: PlotArea) = value
        """
        ...

    @property
    def InsideTop(self) -> float:
        """
        Get: InsideTop(self: PlotArea) -> float
        Set: InsideTop(self: PlotArea) = value
        """
        ...

    @property
    def InsideWidth(self) -> float:
        """
        Get: InsideWidth(self: PlotArea) -> float
        Set: InsideWidth(self: PlotArea) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: PlotArea) -> Interior """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: PlotArea) -> float
        Set: Left(self: PlotArea) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PlotArea) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PlotArea) -> object """
        ...

    @property
    def Position(self) -> XlChartElementPosition:
        """
        Get: Position(self: PlotArea) -> XlChartElementPosition
        Set: Position(self: PlotArea) = value
        """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: PlotArea) -> float
        Set: Top(self: PlotArea) = value
        """
        ...

    @property
    def Width(self) -> float:
        """
        Get: Width(self: PlotArea) -> float
        Set: Width(self: PlotArea) = value
        """
        ...


    def ClearFormats(self) -> object:
        """ ClearFormats(self: PlotArea) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: PlotArea) -> object """
        ...


class Point: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Point) -> Application """
        ...

    @property
    def ApplyPictToEnd(self) -> bool:
        """
        Get: ApplyPictToEnd(self: Point) -> bool
        Set: ApplyPictToEnd(self: Point) = value
        """
        ...

    @property
    def ApplyPictToFront(self) -> bool:
        """
        Get: ApplyPictToFront(self: Point) -> bool
        Set: ApplyPictToFront(self: Point) = value
        """
        ...

    @property
    def ApplyPictToSides(self) -> bool:
        """
        Get: ApplyPictToSides(self: Point) -> bool
        Set: ApplyPictToSides(self: Point) = value
        """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: Point) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Point) -> int """
        ...

    @property
    def DataLabel(self) -> DataLabel:
        """ Get: DataLabel(self: Point) -> DataLabel """
        ...

    @property
    def Explosion(self) -> int:
        """
        Get: Explosion(self: Point) -> int
        Set: Explosion(self: Point) = value
        """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: Point) -> ChartFillFormat """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: Point) -> ChartFormat """
        ...

    @property
    def Has3DEffect(self) -> bool:
        """
        Get: Has3DEffect(self: Point) -> bool
        Set: Has3DEffect(self: Point) = value
        """
        ...

    @property
    def HasDataLabel(self) -> bool:
        """
        Get: HasDataLabel(self: Point) -> bool
        Set: HasDataLabel(self: Point) = value
        """
        ...

    @property
    def Height(self) -> float:
        """ Get: Height(self: Point) -> float """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: Point) -> Interior """
        ...

    @property
    def InvertIfNegative(self) -> bool:
        """
        Get: InvertIfNegative(self: Point) -> bool
        Set: InvertIfNegative(self: Point) = value
        """
        ...

    @property
    def Left(self) -> float:
        """ Get: Left(self: Point) -> float """
        ...

    @property
    def MarkerBackgroundColor(self) -> int:
        """
        Get: MarkerBackgroundColor(self: Point) -> int
        Set: MarkerBackgroundColor(self: Point) = value
        """
        ...

    @property
    def MarkerBackgroundColorIndex(self) -> XlColorIndex:
        """
        Get: MarkerBackgroundColorIndex(self: Point) -> XlColorIndex
        Set: MarkerBackgroundColorIndex(self: Point) = value
        """
        ...

    @property
    def MarkerForegroundColor(self) -> int:
        """
        Get: MarkerForegroundColor(self: Point) -> int
        Set: MarkerForegroundColor(self: Point) = value
        """
        ...

    @property
    def MarkerForegroundColorIndex(self) -> XlColorIndex:
        """
        Get: MarkerForegroundColorIndex(self: Point) -> XlColorIndex
        Set: MarkerForegroundColorIndex(self: Point) = value
        """
        ...

    @property
    def MarkerSize(self) -> int:
        """
        Get: MarkerSize(self: Point) -> int
        Set: MarkerSize(self: Point) = value
        """
        ...

    @property
    def MarkerStyle(self) -> XlMarkerStyle:
        """
        Get: MarkerStyle(self: Point) -> XlMarkerStyle
        Set: MarkerStyle(self: Point) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Point) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Point) -> object """
        ...

    @property
    def PictureType(self) -> XlChartPictureType:
        """
        Get: PictureType(self: Point) -> XlChartPictureType
        Set: PictureType(self: Point) = value
        """
        ...

    @property
    def PictureUnit(self) -> int:
        """
        Get: PictureUnit(self: Point) -> int
        Set: PictureUnit(self: Point) = value
        """
        ...

    @property
    def PictureUnit2(self) -> float:
        """
        Get: PictureUnit2(self: Point) -> float
        Set: PictureUnit2(self: Point) = value
        """
        ...

    @property
    def SecondaryPlot(self) -> bool:
        """
        Get: SecondaryPlot(self: Point) -> bool
        Set: SecondaryPlot(self: Point) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: Point) -> bool
        Set: Shadow(self: Point) = value
        """
        ...

    @property
    def Top(self) -> float:
        """ Get: Top(self: Point) -> float """
        ...

    @property
    def Width(self) -> float:
        """ Get: Width(self: Point) -> float """
        ...


    def ApplyDataLabels(self, Type:XlDataLabelsType, LegendKey:object, AutoText:object, HasLeaderLines:object, ShowSeriesName:object, ShowCategoryName:object, ShowValue:object, ShowPercentage:object, ShowBubbleSize:object, Separator:object) -> object:
        """ ApplyDataLabels(self: Point, Type: XlDataLabelsType, LegendKey: object, AutoText: object, HasLeaderLines: object, ShowSeriesName: object, ShowCategoryName: object, ShowValue: object, ShowPercentage: object, ShowBubbleSize: object, Separator: object) -> object """
        ...

    def ClearFormats(self) -> object:
        """ ClearFormats(self: Point) -> object """
        ...

    def Copy(self) -> object:
        """ Copy(self: Point) -> object """
        ...

    def Delete(self) -> object:
        """ Delete(self: Point) -> object """
        ...

    def Paste(self) -> object:
        """ Paste(self: Point) -> object """
        ...

    def PieSliceLocation(self, loc:XlPieSliceLocation, Index:XlPieSliceIndex) -> float:
        """ PieSliceLocation(self: Point, loc: XlPieSliceLocation, Index: XlPieSliceIndex) -> float """
        ...

    def Select(self) -> object:
        """ Select(self: Point) -> object """
        ...

    def _ApplyDataLabels(self, Type:XlDataLabelsType, LegendKey:object, AutoText:object, HasLeaderLines:object) -> object:
        """ _ApplyDataLabels(self: Point, Type: XlDataLabelsType, LegendKey: object, AutoText: object, HasLeaderLines: object) -> object """
        ...


class Points(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Points) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Points) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Points) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Points) -> object """
        ...


    def Item(self, Index:int) -> Point:
        """ Item(self: Points, Index: int) -> Point """
        ...

    def _Default(self, Index:int) -> Point:
        """ _Default(self: Points, Index: int) -> Point """
        ...


class _PowerRex: # skipped bases: <type 'object'>
    """ no doc """
    def OnAsfEncoderEvent(self, erorCode:object, bstrErrorDesc:object): # -> 
        """ OnAsfEncoderEvent(self: _PowerRex, erorCode: object, bstrErrorDesc: object) """
        ...


class PowerRex(_PowerRex): # skipped bases: <type 'object'>
    """ no doc """
    pass

class PowerRexClass(__ComObject, PowerRex): # skipped bases: <type '_PowerRex'>, <type 'object'>
    """ PowerRexClass() """
    def OnAsfEncoderEvent(self, erorCode:object, bstrErrorDesc:object): # -> 
        """ OnAsfEncoderEvent(self: PowerRexClass, erorCode: object, bstrErrorDesc: object) """
        ...


class PpActionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpActionType, values: ppActionEndShow (6), ppActionFirstSlide (3), ppActionHyperlink (7), ppActionLastSlide (4), ppActionLastSlideViewed (5), ppActionMixed (-2), ppActionNamedSlideShow (10), ppActionNextSlide (1), ppActionNone (0), ppActionOLEVerb (11), ppActionPlay (12), ppActionPreviousSlide (2), ppActionRunMacro (8), ppActionRunProgram (9) """
    ppActionEndShow: PpActionType = ...
    ppActionFirstSlide: PpActionType = ...
    ppActionHyperlink: PpActionType = ...
    ppActionLastSlide: PpActionType = ...
    ppActionLastSlideViewed: PpActionType = ...
    ppActionMixed: PpActionType = ...
    ppActionNamedSlideShow: PpActionType = ...
    ppActionNextSlide: PpActionType = ...
    ppActionNone: PpActionType = ...
    ppActionOLEVerb: PpActionType = ...
    ppActionPlay: PpActionType = ...
    ppActionPreviousSlide: PpActionType = ...
    ppActionRunMacro: PpActionType = ...
    ppActionRunProgram: PpActionType = ...
    value__ = ...


class PpAdvanceMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpAdvanceMode, values: ppAdvanceModeMixed (-2), ppAdvanceOnClick (1), ppAdvanceOnTime (2) """
    ppAdvanceModeMixed: PpAdvanceMode = ...
    ppAdvanceOnClick: PpAdvanceMode = ...
    ppAdvanceOnTime: PpAdvanceMode = ...
    value__ = ...


class PpAfterEffect(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpAfterEffect, values: ppAfterEffectDim (2), ppAfterEffectHide (1), ppAfterEffectHideOnClick (3), ppAfterEffectMixed (-2), ppAfterEffectNothing (0) """
    ppAfterEffectDim: PpAfterEffect = ...
    ppAfterEffectHide: PpAfterEffect = ...
    ppAfterEffectHideOnClick: PpAfterEffect = ...
    ppAfterEffectMixed: PpAfterEffect = ...
    ppAfterEffectNothing: PpAfterEffect = ...
    value__ = ...


class PpAlertLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpAlertLevel, values: ppAlertsAll (2), ppAlertsNone (1) """
    ppAlertsAll: PpAlertLevel = ...
    ppAlertsNone: PpAlertLevel = ...
    value__ = ...


class PpArrangeStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpArrangeStyle, values: ppArrangeCascade (2), ppArrangeTiled (1) """
    ppArrangeCascade: PpArrangeStyle = ...
    ppArrangeTiled: PpArrangeStyle = ...
    value__ = ...


class PpAutoSize(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpAutoSize, values: ppAutoSizeMixed (-2), ppAutoSizeNone (0), ppAutoSizeShapeToFitText (1) """
    ppAutoSizeMixed: PpAutoSize = ...
    ppAutoSizeNone: PpAutoSize = ...
    ppAutoSizeShapeToFitText: PpAutoSize = ...
    value__ = ...


class PpBaselineAlignment(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpBaselineAlignment, values: ppBaselineAlignAuto (5), ppBaselineAlignBaseline (1), ppBaselineAlignCenter (3), ppBaselineAlignFarEast50 (4), ppBaselineAlignMixed (-2), ppBaselineAlignTop (2) """
    ppBaselineAlignAuto: PpBaselineAlignment = ...
    ppBaselineAlignBaseline: PpBaselineAlignment = ...
    ppBaselineAlignCenter: PpBaselineAlignment = ...
    ppBaselineAlignFarEast50: PpBaselineAlignment = ...
    ppBaselineAlignMixed: PpBaselineAlignment = ...
    ppBaselineAlignTop: PpBaselineAlignment = ...
    value__ = ...


class PpBorderType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpBorderType, values: ppBorderBottom (3), ppBorderDiagonalDown (5), ppBorderDiagonalUp (6), ppBorderLeft (2), ppBorderRight (4), ppBorderTop (1) """
    ppBorderBottom: PpBorderType = ...
    ppBorderDiagonalDown: PpBorderType = ...
    ppBorderDiagonalUp: PpBorderType = ...
    ppBorderLeft: PpBorderType = ...
    ppBorderRight: PpBorderType = ...
    ppBorderTop: PpBorderType = ...
    value__ = ...


class PpBulletType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpBulletType, values: ppBulletMixed (-2), ppBulletNone (0), ppBulletNumbered (2), ppBulletPicture (3), ppBulletUnnumbered (1) """
    ppBulletMixed: PpBulletType = ...
    ppBulletNone: PpBulletType = ...
    ppBulletNumbered: PpBulletType = ...
    ppBulletPicture: PpBulletType = ...
    ppBulletUnnumbered: PpBulletType = ...
    value__ = ...


class PpChangeCase(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpChangeCase, values: ppCaseLower (2), ppCaseSentence (1), ppCaseTitle (4), ppCaseToggle (5), ppCaseUpper (3) """
    ppCaseLower: PpChangeCase = ...
    ppCaseSentence: PpChangeCase = ...
    ppCaseTitle: PpChangeCase = ...
    ppCaseToggle: PpChangeCase = ...
    ppCaseUpper: PpChangeCase = ...
    value__ = ...


class PpChartUnitEffect(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpChartUnitEffect, values: ppAnimateByCategory (2), ppAnimateByCategoryElements (4), ppAnimateBySeries (1), ppAnimateBySeriesElements (3), ppAnimateChartAllAtOnce (5), ppAnimateChartMixed (-2) """
    ppAnimateByCategory: PpChartUnitEffect = ...
    ppAnimateByCategoryElements: PpChartUnitEffect = ...
    ppAnimateBySeries: PpChartUnitEffect = ...
    ppAnimateBySeriesElements: PpChartUnitEffect = ...
    ppAnimateChartAllAtOnce: PpChartUnitEffect = ...
    ppAnimateChartMixed: PpChartUnitEffect = ...
    value__ = ...


class PpCheckInVersionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpCheckInVersionType, values: ppCheckInMajorVersion (1), ppCheckInMinorVersion (0), ppCheckInOverwriteVersion (2) """
    ppCheckInMajorVersion: PpCheckInVersionType = ...
    ppCheckInMinorVersion: PpCheckInVersionType = ...
    ppCheckInOverwriteVersion: PpCheckInVersionType = ...
    value__ = ...


class PpColorSchemeIndex(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpColorSchemeIndex, values: ppAccent1 (6), ppAccent2 (7), ppAccent3 (8), ppBackground (1), ppFill (5), ppForeground (2), ppNotSchemeColor (0), ppSchemeColorMixed (-2), ppShadow (3), ppTitle (4) """
    ppAccent1: PpColorSchemeIndex = ...
    ppAccent2: PpColorSchemeIndex = ...
    ppAccent3: PpColorSchemeIndex = ...
    ppBackground: PpColorSchemeIndex = ...
    ppFill: PpColorSchemeIndex = ...
    ppForeground: PpColorSchemeIndex = ...
    ppNotSchemeColor: PpColorSchemeIndex = ...
    ppSchemeColorMixed: PpColorSchemeIndex = ...
    ppShadow: PpColorSchemeIndex = ...
    ppTitle: PpColorSchemeIndex = ...
    value__ = ...


class PpDateTimeFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpDateTimeFormat, values: ppDateTimeddddMMMMddyyyy (2), ppDateTimedMMMMyyyy (3), ppDateTimedMMMyy (5), ppDateTimeFigureOut (14), ppDateTimeFormatMixed (-2), ppDateTimeHmm (10), ppDateTimehmmAMPM (12), ppDateTimeHmmss (11), ppDateTimehmmssAMPM (13), ppDateTimeMdyy (1), ppDateTimeMMddyyHmm (8), ppDateTimeMMddyyhmmAMPM (9), ppDateTimeMMMMdyyyy (4), ppDateTimeMMMMyy (6), ppDateTimeMMyy (7), ppDateTimeUAQ1 (15), ppDateTimeUAQ2 (16), ppDateTimeUAQ3 (17), ppDateTimeUAQ4 (18), ppDateTimeUAQ5 (19), ppDateTimeUAQ6 (20), ppDateTimeUAQ7 (21) """
    ppDateTimeddddMMMMddyyyy: PpDateTimeFormat = ...
    ppDateTimedMMMMyyyy: PpDateTimeFormat = ...
    ppDateTimedMMMyy: PpDateTimeFormat = ...
    ppDateTimeFigureOut: PpDateTimeFormat = ...
    ppDateTimeFormatMixed: PpDateTimeFormat = ...
    ppDateTimeHmm: PpDateTimeFormat = ...
    ppDateTimehmmAMPM: PpDateTimeFormat = ...
    ppDateTimeHmmss: PpDateTimeFormat = ...
    ppDateTimehmmssAMPM: PpDateTimeFormat = ...
    ppDateTimeMdyy: PpDateTimeFormat = ...
    ppDateTimeMMddyyHmm: PpDateTimeFormat = ...
    ppDateTimeMMddyyhmmAMPM: PpDateTimeFormat = ...
    ppDateTimeMMMMdyyyy: PpDateTimeFormat = ...
    ppDateTimeMMMMyy: PpDateTimeFormat = ...
    ppDateTimeMMyy: PpDateTimeFormat = ...
    ppDateTimeUAQ1: PpDateTimeFormat = ...
    ppDateTimeUAQ2: PpDateTimeFormat = ...
    ppDateTimeUAQ3: PpDateTimeFormat = ...
    ppDateTimeUAQ4: PpDateTimeFormat = ...
    ppDateTimeUAQ5: PpDateTimeFormat = ...
    ppDateTimeUAQ6: PpDateTimeFormat = ...
    ppDateTimeUAQ7: PpDateTimeFormat = ...
    value__ = ...


class PpDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpDirection, values: ppDirectionLeftToRight (1), ppDirectionMixed (-2), ppDirectionRightToLeft (2) """
    ppDirectionLeftToRight: PpDirection = ...
    ppDirectionMixed: PpDirection = ...
    ppDirectionRightToLeft: PpDirection = ...
    value__ = ...


class PpEntryEffect(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpEntryEffect, values: ppEffectAirplaneLeft (3950), ppEffectAirplaneRight (3951), ppEffectAppear (3844), ppEffectBlindsHorizontal (769), ppEffectBlindsVertical (770), ppEffectBoxDown (3925), ppEffectBoxIn (3074), ppEffectBoxLeft (3922), ppEffectBoxOut (3073), ppEffectBoxRight (3924), ppEffectBoxUp (3923), ppEffectCheckerboardAcross (1025), ppEffectCheckerboardDown (1026), ppEffectCircleOut (3845), ppEffectCombHorizontal (3847), ppEffectCombVertical (3848), ppEffectConveyorLeft (3882), ppEffectConveyorRight (3883), ppEffectCoverDown (1284), ppEffectCoverLeft (1281), ppEffectCoverLeftDown (1287), ppEffectCoverLeftUp (1285), ppEffectCoverRight (1283), ppEffectCoverRightDown (1288), ppEffectCoverRightUp (1286), ppEffectCoverUp (1282), ppEffectCrawlFromDown (3344), ppEffectCrawlFromLeft (3341), ppEffectCrawlFromRight (3343), ppEffectCrawlFromUp (3342), ppEffectCrush (3943), ppEffectCubeDown (3917), ppEffectCubeLeft (3914), ppEffectCubeRight (3916), ppEffectCubeUp (3915), ppEffectCurtains (3938), ppEffectCut (257), ppEffectCutThroughBlack (258), ppEffectDiamondOut (3846), ppEffectDissolve (1537), ppEffectDoorsHorizontal (3885), ppEffectDoorsVertical (3884), ppEffectDrapeLeft (3936), ppEffectDrapeRight (3937), ppEffectFade (1793), ppEffectFadeSmoothly (3849), ppEffectFallOverLeft (3934), ppEffectFallOverRight (3935), ppEffectFerrisWheelLeft (3899), ppEffectFerrisWheelRight (3900), ppEffectFlashbulb (3909), ppEffectFlashOnceFast (3841), ppEffectFlashOnceMedium (3842), ppEffectFlashOnceSlow (3843), ppEffectFlipDown (3908), ppEffectFlipLeft (3905), ppEffectFlipRight (3907), ppEffectFlipUp (3906), ppEffectFlyFromBottom (3332), ppEffectFlyFromBottomLeft (3335), ppEffectFlyFromBottomRight (3336), ppEffectFlyFromLeft (3329), ppEffectFlyFromRight (3331), ppEffectFlyFromTop (3330), ppEffectFlyFromTopLeft (3333), ppEffectFlyFromTopRight (3334), ppEffectFlyThroughIn (3890), ppEffectFlyThroughInBounce (3892), ppEffectFlyThroughOut (3891), ppEffectFlyThroughOutBounce (3893), ppEffectFracture (3942), ppEffectGalleryLeft (3880), ppEffectGalleryRight (3881), ppEffectGlitterDiamondDown (3875), ppEffectGlitterDiamondLeft (3872), ppEffectGlitterDiamondRight (3874), ppEffectGlitterDiamondUp (3873), ppEffectGlitterHexagonDown (3879), ppEffectGlitterHexagonLeft (3876), ppEffectGlitterHexagonRight (3878), ppEffectGlitterHexagonUp (3877), ppEffectHoneycomb (3898), ppEffectMixed (-2), ppEffectNewsflash (3850), ppEffectNone (0), ppEffectOrbitDown (3929), ppEffectOrbitLeft (3926), ppEffectOrbitRight (3928), ppEffectOrbitUp (3927), ppEffectOrigamiLeft (3952), ppEffectOrigamiRight (3953), ppEffectPageCurlDoubleLeft (3948), ppEffectPageCurlDoubleRight (3949), ppEffectPageCurlSingleLeft (3946), ppEffectPageCurlSingleRight (3947), ppEffectPanDown (3933), ppEffectPanLeft (3930), ppEffectPanRight (3932), ppEffectPanUp (3931), ppEffectPeekFromDown (3338), ppEffectPeekFromLeft (3337), ppEffectPeekFromRight (3339), ppEffectPeekFromUp (3340), ppEffectPeelOffLeft (3944), ppEffectPeelOffRight (3945), ppEffectPlusOut (3851), ppEffectPrestige (3941), ppEffectPushDown (3852), ppEffectPushLeft (3853), ppEffectPushRight (3854), ppEffectPushUp (3855), ppEffectRandom (513), ppEffectRandomBarsHorizontal (2305), ppEffectRandomBarsVertical (2306), ppEffectRevealBlackLeft (3896), ppEffectRevealBlackRight (3897), ppEffectRevealSmoothLeft (3894), ppEffectRevealSmoothRight (3895), ppEffectRippleCenter (3867), ppEffectRippleLeftDown (3870), ppEffectRippleLeftUp (3869), ppEffectRippleRightDown (3871), ppEffectRippleRightUp (3868), ppEffectRotateDown (3921), ppEffectRotateLeft (3918), ppEffectRotateRight (3920), ppEffectRotateUp (3919), ppEffectShredRectangleIn (3912), ppEffectShredRectangleOut (3913), ppEffectShredStripsIn (3910), ppEffectShredStripsOut (3911), ppEffectSpiral (3357), ppEffectSplitHorizontalIn (3586), ppEffectSplitHorizontalOut (3585), ppEffectSplitVerticalIn (3588), ppEffectSplitVerticalOut (3587), ppEffectStretchAcross (3351), ppEffectStretchDown (3355), ppEffectStretchLeft (3352), ppEffectStretchRight (3354), ppEffectStretchUp (3353), ppEffectStripsDownLeft (2563), ppEffectStripsDownRight (2564), ppEffectStripsLeftDown (2567), ppEffectStripsLeftUp (2565), ppEffectStripsRightDown (2568), ppEffectStripsRightUp (2566), ppEffectStripsUpLeft (2561), ppEffectStripsUpRight (2562), ppEffectSwitchDown (3904), ppEffectSwitchLeft (3901), ppEffectSwitchRight (3903), ppEffectSwitchUp (3902), ppEffectSwivel (3356), ppEffectUncoverDown (2052), ppEffectUncoverLeft (2049), ppEffectUncoverLeftDown (2055), ppEffectUncoverLeftUp (2053), ppEffectUncoverRight (2051), ppEffectUncoverRightDown (2056), ppEffectUncoverRightUp (2054), ppEffectUncoverUp (2050), ppEffectVortexDown (3866), ppEffectVortexLeft (3863), ppEffectVortexRight (3865), ppEffectVortexUp (3864), ppEffectWarpIn (3888), ppEffectWarpOut (3889), ppEffectWedge (3856), ppEffectWheel1Spoke (3857), ppEffectWheel2Spokes (3858), ppEffectWheel3Spokes (3859), ppEffectWheel4Spokes (3860), ppEffectWheel8Spokes (3861), ppEffectWheelReverse1Spoke (3862), ppEffectWindLeft (3939), ppEffectWindowHorizontal (3887), ppEffectWindowVertical (3886), ppEffectWindRight (3940), ppEffectWipeDown (2820), ppEffectWipeLeft (2817), ppEffectWipeRight (2819), ppEffectWipeUp (2818), ppEffectZoomBottom (3350), ppEffectZoomCenter (3349), ppEffectZoomIn (3345), ppEffectZoomInSlightly (3346), ppEffectZoomOut (3347), ppEffectZoomOutSlightly (3348) """
    ppEffectAirplaneLeft: PpEntryEffect = ...
    ppEffectAirplaneRight: PpEntryEffect = ...
    ppEffectAppear: PpEntryEffect = ...
    ppEffectBlindsHorizontal: PpEntryEffect = ...
    ppEffectBlindsVertical: PpEntryEffect = ...
    ppEffectBoxDown: PpEntryEffect = ...
    ppEffectBoxIn: PpEntryEffect = ...
    ppEffectBoxLeft: PpEntryEffect = ...
    ppEffectBoxOut: PpEntryEffect = ...
    ppEffectBoxRight: PpEntryEffect = ...
    ppEffectBoxUp: PpEntryEffect = ...
    ppEffectCheckerboardAcross: PpEntryEffect = ...
    ppEffectCheckerboardDown: PpEntryEffect = ...
    ppEffectCircleOut: PpEntryEffect = ...
    ppEffectCombHorizontal: PpEntryEffect = ...
    ppEffectCombVertical: PpEntryEffect = ...
    ppEffectConveyorLeft: PpEntryEffect = ...
    ppEffectConveyorRight: PpEntryEffect = ...
    ppEffectCoverDown: PpEntryEffect = ...
    ppEffectCoverLeft: PpEntryEffect = ...
    ppEffectCoverLeftDown: PpEntryEffect = ...
    ppEffectCoverLeftUp: PpEntryEffect = ...
    ppEffectCoverRight: PpEntryEffect = ...
    ppEffectCoverRightDown: PpEntryEffect = ...
    ppEffectCoverRightUp: PpEntryEffect = ...
    ppEffectCoverUp: PpEntryEffect = ...
    ppEffectCrawlFromDown: PpEntryEffect = ...
    ppEffectCrawlFromLeft: PpEntryEffect = ...
    ppEffectCrawlFromRight: PpEntryEffect = ...
    ppEffectCrawlFromUp: PpEntryEffect = ...
    ppEffectCrush: PpEntryEffect = ...
    ppEffectCubeDown: PpEntryEffect = ...
    ppEffectCubeLeft: PpEntryEffect = ...
    ppEffectCubeRight: PpEntryEffect = ...
    ppEffectCubeUp: PpEntryEffect = ...
    ppEffectCurtains: PpEntryEffect = ...
    ppEffectCut: PpEntryEffect = ...
    ppEffectCutThroughBlack: PpEntryEffect = ...
    ppEffectDiamondOut: PpEntryEffect = ...
    ppEffectDissolve: PpEntryEffect = ...
    ppEffectDoorsHorizontal: PpEntryEffect = ...
    ppEffectDoorsVertical: PpEntryEffect = ...
    ppEffectDrapeLeft: PpEntryEffect = ...
    ppEffectDrapeRight: PpEntryEffect = ...
    ppEffectFade: PpEntryEffect = ...
    ppEffectFadeSmoothly: PpEntryEffect = ...
    ppEffectFallOverLeft: PpEntryEffect = ...
    ppEffectFallOverRight: PpEntryEffect = ...
    ppEffectFerrisWheelLeft: PpEntryEffect = ...
    ppEffectFerrisWheelRight: PpEntryEffect = ...
    ppEffectFlashbulb: PpEntryEffect = ...
    ppEffectFlashOnceFast: PpEntryEffect = ...
    ppEffectFlashOnceMedium: PpEntryEffect = ...
    ppEffectFlashOnceSlow: PpEntryEffect = ...
    ppEffectFlipDown: PpEntryEffect = ...
    ppEffectFlipLeft: PpEntryEffect = ...
    ppEffectFlipRight: PpEntryEffect = ...
    ppEffectFlipUp: PpEntryEffect = ...
    ppEffectFlyFromBottom: PpEntryEffect = ...
    ppEffectFlyFromBottomLeft: PpEntryEffect = ...
    ppEffectFlyFromBottomRight: PpEntryEffect = ...
    ppEffectFlyFromLeft: PpEntryEffect = ...
    ppEffectFlyFromRight: PpEntryEffect = ...
    ppEffectFlyFromTop: PpEntryEffect = ...
    ppEffectFlyFromTopLeft: PpEntryEffect = ...
    ppEffectFlyFromTopRight: PpEntryEffect = ...
    ppEffectFlyThroughIn: PpEntryEffect = ...
    ppEffectFlyThroughInBounce: PpEntryEffect = ...
    ppEffectFlyThroughOut: PpEntryEffect = ...
    ppEffectFlyThroughOutBounce: PpEntryEffect = ...
    ppEffectFracture: PpEntryEffect = ...
    ppEffectGalleryLeft: PpEntryEffect = ...
    ppEffectGalleryRight: PpEntryEffect = ...
    ppEffectGlitterDiamondDown: PpEntryEffect = ...
    ppEffectGlitterDiamondLeft: PpEntryEffect = ...
    ppEffectGlitterDiamondRight: PpEntryEffect = ...
    ppEffectGlitterDiamondUp: PpEntryEffect = ...
    ppEffectGlitterHexagonDown: PpEntryEffect = ...
    ppEffectGlitterHexagonLeft: PpEntryEffect = ...
    ppEffectGlitterHexagonRight: PpEntryEffect = ...
    ppEffectGlitterHexagonUp: PpEntryEffect = ...
    ppEffectHoneycomb: PpEntryEffect = ...
    ppEffectMixed: PpEntryEffect = ...
    ppEffectNewsflash: PpEntryEffect = ...
    ppEffectNone: PpEntryEffect = ...
    ppEffectOrbitDown: PpEntryEffect = ...
    ppEffectOrbitLeft: PpEntryEffect = ...
    ppEffectOrbitRight: PpEntryEffect = ...
    ppEffectOrbitUp: PpEntryEffect = ...
    ppEffectOrigamiLeft: PpEntryEffect = ...
    ppEffectOrigamiRight: PpEntryEffect = ...
    ppEffectPageCurlDoubleLeft: PpEntryEffect = ...
    ppEffectPageCurlDoubleRight: PpEntryEffect = ...
    ppEffectPageCurlSingleLeft: PpEntryEffect = ...
    ppEffectPageCurlSingleRight: PpEntryEffect = ...
    ppEffectPanDown: PpEntryEffect = ...
    ppEffectPanLeft: PpEntryEffect = ...
    ppEffectPanRight: PpEntryEffect = ...
    ppEffectPanUp: PpEntryEffect = ...
    ppEffectPeekFromDown: PpEntryEffect = ...
    ppEffectPeekFromLeft: PpEntryEffect = ...
    ppEffectPeekFromRight: PpEntryEffect = ...
    ppEffectPeekFromUp: PpEntryEffect = ...
    ppEffectPeelOffLeft: PpEntryEffect = ...
    ppEffectPeelOffRight: PpEntryEffect = ...
    ppEffectPlusOut: PpEntryEffect = ...
    ppEffectPrestige: PpEntryEffect = ...
    ppEffectPushDown: PpEntryEffect = ...
    ppEffectPushLeft: PpEntryEffect = ...
    ppEffectPushRight: PpEntryEffect = ...
    ppEffectPushUp: PpEntryEffect = ...
    ppEffectRandom: PpEntryEffect = ...
    ppEffectRandomBarsHorizontal: PpEntryEffect = ...
    ppEffectRandomBarsVertical: PpEntryEffect = ...
    ppEffectRevealBlackLeft: PpEntryEffect = ...
    ppEffectRevealBlackRight: PpEntryEffect = ...
    ppEffectRevealSmoothLeft: PpEntryEffect = ...
    ppEffectRevealSmoothRight: PpEntryEffect = ...
    ppEffectRippleCenter: PpEntryEffect = ...
    ppEffectRippleLeftDown: PpEntryEffect = ...
    ppEffectRippleLeftUp: PpEntryEffect = ...
    ppEffectRippleRightDown: PpEntryEffect = ...
    ppEffectRippleRightUp: PpEntryEffect = ...
    ppEffectRotateDown: PpEntryEffect = ...
    ppEffectRotateLeft: PpEntryEffect = ...
    ppEffectRotateRight: PpEntryEffect = ...
    ppEffectRotateUp: PpEntryEffect = ...
    ppEffectShredRectangleIn: PpEntryEffect = ...
    ppEffectShredRectangleOut: PpEntryEffect = ...
    ppEffectShredStripsIn: PpEntryEffect = ...
    ppEffectShredStripsOut: PpEntryEffect = ...
    ppEffectSpiral: PpEntryEffect = ...
    ppEffectSplitHorizontalIn: PpEntryEffect = ...
    ppEffectSplitHorizontalOut: PpEntryEffect = ...
    ppEffectSplitVerticalIn: PpEntryEffect = ...
    ppEffectSplitVerticalOut: PpEntryEffect = ...
    ppEffectStretchAcross: PpEntryEffect = ...
    ppEffectStretchDown: PpEntryEffect = ...
    ppEffectStretchLeft: PpEntryEffect = ...
    ppEffectStretchRight: PpEntryEffect = ...
    ppEffectStretchUp: PpEntryEffect = ...
    ppEffectStripsDownLeft: PpEntryEffect = ...
    ppEffectStripsDownRight: PpEntryEffect = ...
    ppEffectStripsLeftDown: PpEntryEffect = ...
    ppEffectStripsLeftUp: PpEntryEffect = ...
    ppEffectStripsRightDown: PpEntryEffect = ...
    ppEffectStripsRightUp: PpEntryEffect = ...
    ppEffectStripsUpLeft: PpEntryEffect = ...
    ppEffectStripsUpRight: PpEntryEffect = ...
    ppEffectSwitchDown: PpEntryEffect = ...
    ppEffectSwitchLeft: PpEntryEffect = ...
    ppEffectSwitchRight: PpEntryEffect = ...
    ppEffectSwitchUp: PpEntryEffect = ...
    ppEffectSwivel: PpEntryEffect = ...
    ppEffectUncoverDown: PpEntryEffect = ...
    ppEffectUncoverLeft: PpEntryEffect = ...
    ppEffectUncoverLeftDown: PpEntryEffect = ...
    ppEffectUncoverLeftUp: PpEntryEffect = ...
    ppEffectUncoverRight: PpEntryEffect = ...
    ppEffectUncoverRightDown: PpEntryEffect = ...
    ppEffectUncoverRightUp: PpEntryEffect = ...
    ppEffectUncoverUp: PpEntryEffect = ...
    ppEffectVortexDown: PpEntryEffect = ...
    ppEffectVortexLeft: PpEntryEffect = ...
    ppEffectVortexRight: PpEntryEffect = ...
    ppEffectVortexUp: PpEntryEffect = ...
    ppEffectWarpIn: PpEntryEffect = ...
    ppEffectWarpOut: PpEntryEffect = ...
    ppEffectWedge: PpEntryEffect = ...
    ppEffectWheel1Spoke: PpEntryEffect = ...
    ppEffectWheel2Spokes: PpEntryEffect = ...
    ppEffectWheel3Spokes: PpEntryEffect = ...
    ppEffectWheel4Spokes: PpEntryEffect = ...
    ppEffectWheel8Spokes: PpEntryEffect = ...
    ppEffectWheelReverse1Spoke: PpEntryEffect = ...
    ppEffectWindLeft: PpEntryEffect = ...
    ppEffectWindowHorizontal: PpEntryEffect = ...
    ppEffectWindowVertical: PpEntryEffect = ...
    ppEffectWindRight: PpEntryEffect = ...
    ppEffectWipeDown: PpEntryEffect = ...
    ppEffectWipeLeft: PpEntryEffect = ...
    ppEffectWipeRight: PpEntryEffect = ...
    ppEffectWipeUp: PpEntryEffect = ...
    ppEffectZoomBottom: PpEntryEffect = ...
    ppEffectZoomCenter: PpEntryEffect = ...
    ppEffectZoomIn: PpEntryEffect = ...
    ppEffectZoomInSlightly: PpEntryEffect = ...
    ppEffectZoomOut: PpEntryEffect = ...
    ppEffectZoomOutSlightly: PpEntryEffect = ...
    value__ = ...


class PpExportMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpExportMode, values: ppClipRelativeToSlide (2), ppRelativeToSlide (1), ppScaleToFit (3), ppScaleXY (4) """
    ppClipRelativeToSlide: PpExportMode = ...
    ppRelativeToSlide: PpExportMode = ...
    ppScaleToFit: PpExportMode = ...
    ppScaleXY: PpExportMode = ...
    value__ = ...


class PpFarEastLineBreakLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpFarEastLineBreakLevel, values: ppFarEastLineBreakLevelCustom (3), ppFarEastLineBreakLevelNormal (1), ppFarEastLineBreakLevelStrict (2) """
    ppFarEastLineBreakLevelCustom: PpFarEastLineBreakLevel = ...
    ppFarEastLineBreakLevelNormal: PpFarEastLineBreakLevel = ...
    ppFarEastLineBreakLevelStrict: PpFarEastLineBreakLevel = ...
    value__ = ...


class PpFileDialogType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpFileDialogType, values: ppFileDialogOpen (1), ppFileDialogSave (2) """
    ppFileDialogOpen: PpFileDialogType = ...
    ppFileDialogSave: PpFileDialogType = ...
    value__ = ...


class PpFixedFormatIntent(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpFixedFormatIntent, values: ppFixedFormatIntentPrint (2), ppFixedFormatIntentScreen (1) """
    ppFixedFormatIntentPrint: PpFixedFormatIntent = ...
    ppFixedFormatIntentScreen: PpFixedFormatIntent = ...
    value__ = ...


class PpFixedFormatType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpFixedFormatType, values: ppFixedFormatTypePDF (2), ppFixedFormatTypeXPS (1) """
    ppFixedFormatTypePDF: PpFixedFormatType = ...
    ppFixedFormatTypeXPS: PpFixedFormatType = ...
    value__ = ...


class PpFollowColors(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpFollowColors, values: ppFollowColorsMixed (-2), ppFollowColorsNone (0), ppFollowColorsScheme (1), ppFollowColorsTextAndBackground (2) """
    ppFollowColorsMixed: PpFollowColors = ...
    ppFollowColorsNone: PpFollowColors = ...
    ppFollowColorsScheme: PpFollowColors = ...
    ppFollowColorsTextAndBackground: PpFollowColors = ...
    value__ = ...


class PpFrameColors(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpFrameColors, values: ppFrameColorsBlackTextOnWhite (5), ppFrameColorsBrowserColors (1), ppFrameColorsPresentationSchemeAccentColor (3), ppFrameColorsPresentationSchemeTextColor (2), ppFrameColorsWhiteTextOnBlack (4) """
    ppFrameColorsBlackTextOnWhite: PpFrameColors = ...
    ppFrameColorsBrowserColors: PpFrameColors = ...
    ppFrameColorsPresentationSchemeAccentColor: PpFrameColors = ...
    ppFrameColorsPresentationSchemeTextColor: PpFrameColors = ...
    ppFrameColorsWhiteTextOnBlack: PpFrameColors = ...
    value__ = ...


class PpGuideOrientation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpGuideOrientation, values: ppHorizontalGuide (1), ppVerticalGuide (2) """
    ppHorizontalGuide: PpGuideOrientation = ...
    ppVerticalGuide: PpGuideOrientation = ...
    value__ = ...


class PpHTMLVersion(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpHTMLVersion, values: ppHTMLAutodetect (4), ppHTMLDual (3), ppHTMLv3 (1), ppHTMLv4 (2) """
    ppHTMLAutodetect: PpHTMLVersion = ...
    ppHTMLDual: PpHTMLVersion = ...
    ppHTMLv3: PpHTMLVersion = ...
    ppHTMLv4: PpHTMLVersion = ...
    value__ = ...


class PpIndentControl(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpIndentControl, values: ppIndentControlMixed (-2), ppIndentKeepAttr (2), ppIndentReplaceAttr (1) """
    ppIndentControlMixed: PpIndentControl = ...
    ppIndentKeepAttr: PpIndentControl = ...
    ppIndentReplaceAttr: PpIndentControl = ...
    value__ = ...


class PpMediaTaskStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpMediaTaskStatus, values: ppMediaTaskStatusDone (3), ppMediaTaskStatusFailed (4), ppMediaTaskStatusInProgress (1), ppMediaTaskStatusNone (0), ppMediaTaskStatusQueued (2) """
    ppMediaTaskStatusDone: PpMediaTaskStatus = ...
    ppMediaTaskStatusFailed: PpMediaTaskStatus = ...
    ppMediaTaskStatusInProgress: PpMediaTaskStatus = ...
    ppMediaTaskStatusNone: PpMediaTaskStatus = ...
    ppMediaTaskStatusQueued: PpMediaTaskStatus = ...
    value__ = ...


class PpMediaType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpMediaType, values: ppMediaTypeMixed (-2), ppMediaTypeMovie (3), ppMediaTypeOther (1), ppMediaTypeSound (2) """
    ppMediaTypeMixed: PpMediaType = ...
    ppMediaTypeMovie: PpMediaType = ...
    ppMediaTypeOther: PpMediaType = ...
    ppMediaTypeSound: PpMediaType = ...
    value__ = ...


class PpMouseActivation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpMouseActivation, values: ppMouseClick (1), ppMouseOver (2) """
    ppMouseClick: PpMouseActivation = ...
    ppMouseOver: PpMouseActivation = ...
    value__ = ...


class PpNumberedBulletStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpNumberedBulletStyle, values: ppBulletAlphaLCParenBoth (8), ppBulletAlphaLCParenRight (9), ppBulletAlphaLCPeriod (0), ppBulletAlphaUCParenBoth (10), ppBulletAlphaUCParenRight (11), ppBulletAlphaUCPeriod (1), ppBulletArabicAbjadDash (24), ppBulletArabicAlphaDash (23), ppBulletArabicDBPeriod (29), ppBulletArabicDBPlain (28), ppBulletArabicParenBoth (12), ppBulletArabicParenRight (2), ppBulletArabicPeriod (3), ppBulletArabicPlain (13), ppBulletCircleNumDBPlain (18), ppBulletCircleNumWDBlackPlain (20), ppBulletCircleNumWDWhitePlain (19), ppBulletHebrewAlphaDash (25), ppBulletHindiAlpha1Period (40), ppBulletHindiAlphaPeriod (36), ppBulletHindiNumParenRight (39), ppBulletHindiNumPeriod (37), ppBulletKanjiKoreanPeriod (27), ppBulletKanjiKoreanPlain (26), ppBulletKanjiSimpChinDBPeriod (38), ppBulletRomanLCParenBoth (4), ppBulletRomanLCParenRight (5), ppBulletRomanLCPeriod (6), ppBulletRomanUCParenBoth (14), ppBulletRomanUCParenRight (15), ppBulletRomanUCPeriod (7), ppBulletSimpChinPeriod (17), ppBulletSimpChinPlain (16), ppBulletStyleMixed (-2), ppBulletThaiAlphaParenBoth (32), ppBulletThaiAlphaParenRight (31), ppBulletThaiAlphaPeriod (30), ppBulletThaiNumParenBoth (35), ppBulletThaiNumParenRight (34), ppBulletThaiNumPeriod (33), ppBulletTradChinPeriod (22), ppBulletTradChinPlain (21) """
    ppBulletAlphaLCParenBoth: PpNumberedBulletStyle = ...
    ppBulletAlphaLCParenRight: PpNumberedBulletStyle = ...
    ppBulletAlphaLCPeriod: PpNumberedBulletStyle = ...
    ppBulletAlphaUCParenBoth: PpNumberedBulletStyle = ...
    ppBulletAlphaUCParenRight: PpNumberedBulletStyle = ...
    ppBulletAlphaUCPeriod: PpNumberedBulletStyle = ...
    ppBulletArabicAbjadDash: PpNumberedBulletStyle = ...
    ppBulletArabicAlphaDash: PpNumberedBulletStyle = ...
    ppBulletArabicDBPeriod: PpNumberedBulletStyle = ...
    ppBulletArabicDBPlain: PpNumberedBulletStyle = ...
    ppBulletArabicParenBoth: PpNumberedBulletStyle = ...
    ppBulletArabicParenRight: PpNumberedBulletStyle = ...
    ppBulletArabicPeriod: PpNumberedBulletStyle = ...
    ppBulletArabicPlain: PpNumberedBulletStyle = ...
    ppBulletCircleNumDBPlain: PpNumberedBulletStyle = ...
    ppBulletCircleNumWDBlackPlain: PpNumberedBulletStyle = ...
    ppBulletCircleNumWDWhitePlain: PpNumberedBulletStyle = ...
    ppBulletHebrewAlphaDash: PpNumberedBulletStyle = ...
    ppBulletHindiAlpha1Period: PpNumberedBulletStyle = ...
    ppBulletHindiAlphaPeriod: PpNumberedBulletStyle = ...
    ppBulletHindiNumParenRight: PpNumberedBulletStyle = ...
    ppBulletHindiNumPeriod: PpNumberedBulletStyle = ...
    ppBulletKanjiKoreanPeriod: PpNumberedBulletStyle = ...
    ppBulletKanjiKoreanPlain: PpNumberedBulletStyle = ...
    ppBulletKanjiSimpChinDBPeriod: PpNumberedBulletStyle = ...
    ppBulletRomanLCParenBoth: PpNumberedBulletStyle = ...
    ppBulletRomanLCParenRight: PpNumberedBulletStyle = ...
    ppBulletRomanLCPeriod: PpNumberedBulletStyle = ...
    ppBulletRomanUCParenBoth: PpNumberedBulletStyle = ...
    ppBulletRomanUCParenRight: PpNumberedBulletStyle = ...
    ppBulletRomanUCPeriod: PpNumberedBulletStyle = ...
    ppBulletSimpChinPeriod: PpNumberedBulletStyle = ...
    ppBulletSimpChinPlain: PpNumberedBulletStyle = ...
    ppBulletStyleMixed: PpNumberedBulletStyle = ...
    ppBulletThaiAlphaParenBoth: PpNumberedBulletStyle = ...
    ppBulletThaiAlphaParenRight: PpNumberedBulletStyle = ...
    ppBulletThaiAlphaPeriod: PpNumberedBulletStyle = ...
    ppBulletThaiNumParenBoth: PpNumberedBulletStyle = ...
    ppBulletThaiNumParenRight: PpNumberedBulletStyle = ...
    ppBulletThaiNumPeriod: PpNumberedBulletStyle = ...
    ppBulletTradChinPeriod: PpNumberedBulletStyle = ...
    ppBulletTradChinPlain: PpNumberedBulletStyle = ...
    value__ = ...


class PpParagraphAlignment(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpParagraphAlignment, values: ppAlignCenter (2), ppAlignDistribute (5), ppAlignJustify (4), ppAlignJustifyLow (7), ppAlignLeft (1), ppAlignmentMixed (-2), ppAlignRight (3), ppAlignThaiDistribute (6) """
    ppAlignCenter: PpParagraphAlignment = ...
    ppAlignDistribute: PpParagraphAlignment = ...
    ppAlignJustify: PpParagraphAlignment = ...
    ppAlignJustifyLow: PpParagraphAlignment = ...
    ppAlignLeft: PpParagraphAlignment = ...
    ppAlignmentMixed: PpParagraphAlignment = ...
    ppAlignRight: PpParagraphAlignment = ...
    ppAlignThaiDistribute: PpParagraphAlignment = ...
    value__ = ...


class PpPasteDataType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpPasteDataType, values: ppPasteBitmap (1), ppPasteDefault (0), ppPasteEnhancedMetafile (2), ppPasteGIF (4), ppPasteHTML (8), ppPasteJPG (5), ppPasteMetafilePicture (3), ppPasteOLEObject (10), ppPastePNG (6), ppPasteRTF (9), ppPasteShape (11), ppPasteText (7) """
    ppPasteBitmap: PpPasteDataType = ...
    ppPasteDefault: PpPasteDataType = ...
    ppPasteEnhancedMetafile: PpPasteDataType = ...
    ppPasteGIF: PpPasteDataType = ...
    ppPasteHTML: PpPasteDataType = ...
    ppPasteJPG: PpPasteDataType = ...
    ppPasteMetafilePicture: PpPasteDataType = ...
    ppPasteOLEObject: PpPasteDataType = ...
    ppPastePNG: PpPasteDataType = ...
    ppPasteRTF: PpPasteDataType = ...
    ppPasteShape: PpPasteDataType = ...
    ppPasteText: PpPasteDataType = ...
    value__ = ...


class PpPlaceholderType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpPlaceholderType, values: ppPlaceholderBitmap (9), ppPlaceholderBody (2), ppPlaceholderCenterTitle (3), ppPlaceholderChart (8), ppPlaceholderDate (16), ppPlaceholderFooter (15), ppPlaceholderHeader (14), ppPlaceholderMediaClip (10), ppPlaceholderMixed (-2), ppPlaceholderObject (7), ppPlaceholderOrgChart (11), ppPlaceholderPicture (18), ppPlaceholderSlideNumber (13), ppPlaceholderSubtitle (4), ppPlaceholderTable (12), ppPlaceholderTitle (1), ppPlaceholderVerticalBody (6), ppPlaceholderVerticalObject (17), ppPlaceholderVerticalTitle (5) """
    ppPlaceholderBitmap: PpPlaceholderType = ...
    ppPlaceholderBody: PpPlaceholderType = ...
    ppPlaceholderCenterTitle: PpPlaceholderType = ...
    ppPlaceholderChart: PpPlaceholderType = ...
    ppPlaceholderDate: PpPlaceholderType = ...
    ppPlaceholderFooter: PpPlaceholderType = ...
    ppPlaceholderHeader: PpPlaceholderType = ...
    ppPlaceholderMediaClip: PpPlaceholderType = ...
    ppPlaceholderMixed: PpPlaceholderType = ...
    ppPlaceholderObject: PpPlaceholderType = ...
    ppPlaceholderOrgChart: PpPlaceholderType = ...
    ppPlaceholderPicture: PpPlaceholderType = ...
    ppPlaceholderSlideNumber: PpPlaceholderType = ...
    ppPlaceholderSubtitle: PpPlaceholderType = ...
    ppPlaceholderTable: PpPlaceholderType = ...
    ppPlaceholderTitle: PpPlaceholderType = ...
    ppPlaceholderVerticalBody: PpPlaceholderType = ...
    ppPlaceholderVerticalObject: PpPlaceholderType = ...
    ppPlaceholderVerticalTitle: PpPlaceholderType = ...
    value__ = ...


class PpPlayerState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpPlayerState, values: ppNotReady (3), ppPaused (1), ppPlaying (0), ppStopped (2) """
    ppNotReady: PpPlayerState = ...
    ppPaused: PpPlayerState = ...
    ppPlaying: PpPlayerState = ...
    ppStopped: PpPlayerState = ...
    value__ = ...


class PpPrintColorType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpPrintColorType, values: ppPrintBlackAndWhite (2), ppPrintColor (1), ppPrintPureBlackAndWhite (3) """
    ppPrintBlackAndWhite: PpPrintColorType = ...
    ppPrintColor: PpPrintColorType = ...
    ppPrintPureBlackAndWhite: PpPrintColorType = ...
    value__ = ...


class PpPrintHandoutOrder(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpPrintHandoutOrder, values: ppPrintHandoutHorizontalFirst (2), ppPrintHandoutVerticalFirst (1) """
    ppPrintHandoutHorizontalFirst: PpPrintHandoutOrder = ...
    ppPrintHandoutVerticalFirst: PpPrintHandoutOrder = ...
    value__ = ...


class PpPrintOutputType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpPrintOutputType, values: ppPrintOutputBuildSlides (7), ppPrintOutputFourSlideHandouts (8), ppPrintOutputNineSlideHandouts (9), ppPrintOutputNotesPages (5), ppPrintOutputOneSlideHandouts (10), ppPrintOutputOutline (6), ppPrintOutputSixSlideHandouts (4), ppPrintOutputSlides (1), ppPrintOutputThreeSlideHandouts (3), ppPrintOutputTwoSlideHandouts (2) """
    ppPrintOutputBuildSlides: PpPrintOutputType = ...
    ppPrintOutputFourSlideHandouts: PpPrintOutputType = ...
    ppPrintOutputNineSlideHandouts: PpPrintOutputType = ...
    ppPrintOutputNotesPages: PpPrintOutputType = ...
    ppPrintOutputOneSlideHandouts: PpPrintOutputType = ...
    ppPrintOutputOutline: PpPrintOutputType = ...
    ppPrintOutputSixSlideHandouts: PpPrintOutputType = ...
    ppPrintOutputSlides: PpPrintOutputType = ...
    ppPrintOutputThreeSlideHandouts: PpPrintOutputType = ...
    ppPrintOutputTwoSlideHandouts: PpPrintOutputType = ...
    value__ = ...


class PpPrintRangeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpPrintRangeType, values: ppPrintAll (1), ppPrintCurrent (3), ppPrintNamedSlideShow (5), ppPrintSection (6), ppPrintSelection (2), ppPrintSlideRange (4) """
    ppPrintAll: PpPrintRangeType = ...
    ppPrintCurrent: PpPrintRangeType = ...
    ppPrintNamedSlideShow: PpPrintRangeType = ...
    ppPrintSection: PpPrintRangeType = ...
    ppPrintSelection: PpPrintRangeType = ...
    ppPrintSlideRange: PpPrintRangeType = ...
    value__ = ...


class PpProtectedViewCloseReason(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpProtectedViewCloseReason, values: ppProtectedViewCloseEdit (1), ppProtectedViewCloseForced (2), ppProtectedViewCloseNormal (0) """
    ppProtectedViewCloseEdit: PpProtectedViewCloseReason = ...
    ppProtectedViewCloseForced: PpProtectedViewCloseReason = ...
    ppProtectedViewCloseNormal: PpProtectedViewCloseReason = ...
    value__ = ...


class PpPublishSourceType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpPublishSourceType, values: ppPublishAll (1), ppPublishNamedSlideShow (3), ppPublishSlideRange (2) """
    ppPublishAll: PpPublishSourceType = ...
    ppPublishNamedSlideShow: PpPublishSourceType = ...
    ppPublishSlideRange: PpPublishSourceType = ...
    value__ = ...


class PpRemoveDocInfoType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpRemoveDocInfoType, values: ppRDIAll (99), ppRDIComments (1), ppRDIContentType (16), ppRDIDocumentManagementPolicy (15), ppRDIDocumentProperties (8), ppRDIDocumentServerProperties (14), ppRDIDocumentWorkspace (10), ppRDIInkAnnotations (11), ppRDIPublishPath (13), ppRDIRemovePersonalInformation (4), ppRDISlideUpdateInformation (17) """
    ppRDIAll: PpRemoveDocInfoType = ...
    ppRDIComments: PpRemoveDocInfoType = ...
    ppRDIContentType: PpRemoveDocInfoType = ...
    ppRDIDocumentManagementPolicy: PpRemoveDocInfoType = ...
    ppRDIDocumentProperties: PpRemoveDocInfoType = ...
    ppRDIDocumentServerProperties: PpRemoveDocInfoType = ...
    ppRDIDocumentWorkspace: PpRemoveDocInfoType = ...
    ppRDIInkAnnotations: PpRemoveDocInfoType = ...
    ppRDIPublishPath: PpRemoveDocInfoType = ...
    ppRDIRemovePersonalInformation: PpRemoveDocInfoType = ...
    ppRDISlideUpdateInformation: PpRemoveDocInfoType = ...
    value__ = ...


class PpResampleMediaProfile(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpResampleMediaProfile, values: ppResampleMediaProfileCustom (1), ppResampleMediaProfileSmall (2), ppResampleMediaProfileSmaller (3), ppResampleMediaProfileSmallest (4) """
    ppResampleMediaProfileCustom: PpResampleMediaProfile = ...
    ppResampleMediaProfileSmall: PpResampleMediaProfile = ...
    ppResampleMediaProfileSmaller: PpResampleMediaProfile = ...
    ppResampleMediaProfileSmallest: PpResampleMediaProfile = ...
    value__ = ...


class PpRevisionInfo(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpRevisionInfo, values: ppRevisionInfoBaseline (1), ppRevisionInfoMerged (2), ppRevisionInfoNone (0) """
    ppRevisionInfoBaseline: PpRevisionInfo = ...
    ppRevisionInfoMerged: PpRevisionInfo = ...
    ppRevisionInfoNone: PpRevisionInfo = ...
    value__ = ...


class PpSaveAsFileType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpSaveAsFileType, values: ppSaveAsAddIn (8), ppSaveAsBMP (19), ppSaveAsDefault (11), ppSaveAsEMF (23), ppSaveAsExternalConverter (64000), ppSaveAsGIF (16), ppSaveAsHTML (12), ppSaveAsHTMLDual (14), ppSaveAsHTMLv3 (13), ppSaveAsJPG (17), ppSaveAsMetaFile (15), ppSaveAsMP4 (39), ppSaveAsOpenDocumentPresentation (35), ppSaveAsOpenXMLAddin (30), ppSaveAsOpenXMLPicturePresentation (36), ppSaveAsOpenXMLPresentation (24), ppSaveAsOpenXMLPresentationMacroEnabled (25), ppSaveAsOpenXMLShow (28), ppSaveAsOpenXMLShowMacroEnabled (29), ppSaveAsOpenXMLTemplate (26), ppSaveAsOpenXMLTemplateMacroEnabled (27), ppSaveAsOpenXMLTheme (31), ppSaveAsPDF (32), ppSaveAsPNG (18), ppSaveAsPowerPoint3 (4), ppSaveAsPowerPoint4 (3), ppSaveAsPowerPoint4FarEast (10), ppSaveAsPowerPoint7 (2), ppSaveAsPresentation (1), ppSaveAsPresForReview (22), ppSaveAsRTF (6), ppSaveAsShow (7), ppSaveAsStrictOpenXMLPresentation (38), ppSaveAsTemplate (5), ppSaveAsTIF (21), ppSaveAsWebArchive (20), ppSaveAsWMV (37), ppSaveAsXMLPresentation (34), ppSaveAsXPS (33) """
    ppSaveAsAddIn: PpSaveAsFileType = ...
    ppSaveAsBMP: PpSaveAsFileType = ...
    ppSaveAsDefault: PpSaveAsFileType = ...
    ppSaveAsEMF: PpSaveAsFileType = ...
    ppSaveAsExternalConverter: PpSaveAsFileType = ...
    ppSaveAsGIF: PpSaveAsFileType = ...
    ppSaveAsHTML: PpSaveAsFileType = ...
    ppSaveAsHTMLDual: PpSaveAsFileType = ...
    ppSaveAsHTMLv3: PpSaveAsFileType = ...
    ppSaveAsJPG: PpSaveAsFileType = ...
    ppSaveAsMetaFile: PpSaveAsFileType = ...
    ppSaveAsMP4: PpSaveAsFileType = ...
    ppSaveAsOpenDocumentPresentation: PpSaveAsFileType = ...
    ppSaveAsOpenXMLAddin: PpSaveAsFileType = ...
    ppSaveAsOpenXMLPicturePresentation: PpSaveAsFileType = ...
    ppSaveAsOpenXMLPresentation: PpSaveAsFileType = ...
    ppSaveAsOpenXMLPresentationMacroEnabled: PpSaveAsFileType = ...
    ppSaveAsOpenXMLShow: PpSaveAsFileType = ...
    ppSaveAsOpenXMLShowMacroEnabled: PpSaveAsFileType = ...
    ppSaveAsOpenXMLTemplate: PpSaveAsFileType = ...
    ppSaveAsOpenXMLTemplateMacroEnabled: PpSaveAsFileType = ...
    ppSaveAsOpenXMLTheme: PpSaveAsFileType = ...
    ppSaveAsPDF: PpSaveAsFileType = ...
    ppSaveAsPNG: PpSaveAsFileType = ...
    ppSaveAsPowerPoint3: PpSaveAsFileType = ...
    ppSaveAsPowerPoint4: PpSaveAsFileType = ...
    ppSaveAsPowerPoint4FarEast: PpSaveAsFileType = ...
    ppSaveAsPowerPoint7: PpSaveAsFileType = ...
    ppSaveAsPresentation: PpSaveAsFileType = ...
    ppSaveAsPresForReview: PpSaveAsFileType = ...
    ppSaveAsRTF: PpSaveAsFileType = ...
    ppSaveAsShow: PpSaveAsFileType = ...
    ppSaveAsStrictOpenXMLPresentation: PpSaveAsFileType = ...
    ppSaveAsTemplate: PpSaveAsFileType = ...
    ppSaveAsTIF: PpSaveAsFileType = ...
    ppSaveAsWebArchive: PpSaveAsFileType = ...
    ppSaveAsWMV: PpSaveAsFileType = ...
    ppSaveAsXMLPresentation: PpSaveAsFileType = ...
    ppSaveAsXPS: PpSaveAsFileType = ...
    value__ = ...


class PpSelectionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpSelectionType, values: ppSelectionNone (0), ppSelectionShapes (2), ppSelectionSlides (1), ppSelectionText (3) """
    ppSelectionNone: PpSelectionType = ...
    ppSelectionShapes: PpSelectionType = ...
    ppSelectionSlides: PpSelectionType = ...
    ppSelectionText: PpSelectionType = ...
    value__ = ...


class PpShapeFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpShapeFormat, values: ppShapeFormatBMP (3), ppShapeFormatEMF (5), ppShapeFormatGIF (0), ppShapeFormatJPG (1), ppShapeFormatPNG (2), ppShapeFormatWMF (4) """
    ppShapeFormatBMP: PpShapeFormat = ...
    ppShapeFormatEMF: PpShapeFormat = ...
    ppShapeFormatGIF: PpShapeFormat = ...
    ppShapeFormatJPG: PpShapeFormat = ...
    ppShapeFormatPNG: PpShapeFormat = ...
    ppShapeFormatWMF: PpShapeFormat = ...
    value__ = ...


class PpSlideLayout(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpSlideLayout, values: ppLayoutBlank (12), ppLayoutChart (8), ppLayoutChartAndText (6), ppLayoutClipartAndText (10), ppLayoutClipArtAndVerticalText (26), ppLayoutComparison (34), ppLayoutContentWithCaption (35), ppLayoutCustom (32), ppLayoutFourObjects (24), ppLayoutLargeObject (15), ppLayoutMediaClipAndText (18), ppLayoutMixed (-2), ppLayoutObject (16), ppLayoutObjectAndText (14), ppLayoutObjectAndTwoObjects (30), ppLayoutObjectOverText (19), ppLayoutOrgchart (7), ppLayoutPictureWithCaption (36), ppLayoutSectionHeader (33), ppLayoutTable (4), ppLayoutText (2), ppLayoutTextAndChart (5), ppLayoutTextAndClipart (9), ppLayoutTextAndMediaClip (17), ppLayoutTextAndObject (13), ppLayoutTextAndTwoObjects (21), ppLayoutTextOverObject (20), ppLayoutTitle (1), ppLayoutTitleOnly (11), ppLayoutTwoColumnText (3), ppLayoutTwoObjects (29), ppLayoutTwoObjectsAndObject (31), ppLayoutTwoObjectsAndText (22), ppLayoutTwoObjectsOverText (23), ppLayoutVerticalText (25), ppLayoutVerticalTitleAndText (27), ppLayoutVerticalTitleAndTextOverChart (28) """
    ppLayoutBlank: PpSlideLayout = ...
    ppLayoutChart: PpSlideLayout = ...
    ppLayoutChartAndText: PpSlideLayout = ...
    ppLayoutClipartAndText: PpSlideLayout = ...
    ppLayoutClipArtAndVerticalText: PpSlideLayout = ...
    ppLayoutComparison: PpSlideLayout = ...
    ppLayoutContentWithCaption: PpSlideLayout = ...
    ppLayoutCustom: PpSlideLayout = ...
    ppLayoutFourObjects: PpSlideLayout = ...
    ppLayoutLargeObject: PpSlideLayout = ...
    ppLayoutMediaClipAndText: PpSlideLayout = ...
    ppLayoutMixed: PpSlideLayout = ...
    ppLayoutObject: PpSlideLayout = ...
    ppLayoutObjectAndText: PpSlideLayout = ...
    ppLayoutObjectAndTwoObjects: PpSlideLayout = ...
    ppLayoutObjectOverText: PpSlideLayout = ...
    ppLayoutOrgchart: PpSlideLayout = ...
    ppLayoutPictureWithCaption: PpSlideLayout = ...
    ppLayoutSectionHeader: PpSlideLayout = ...
    ppLayoutTable: PpSlideLayout = ...
    ppLayoutText: PpSlideLayout = ...
    ppLayoutTextAndChart: PpSlideLayout = ...
    ppLayoutTextAndClipart: PpSlideLayout = ...
    ppLayoutTextAndMediaClip: PpSlideLayout = ...
    ppLayoutTextAndObject: PpSlideLayout = ...
    ppLayoutTextAndTwoObjects: PpSlideLayout = ...
    ppLayoutTextOverObject: PpSlideLayout = ...
    ppLayoutTitle: PpSlideLayout = ...
    ppLayoutTitleOnly: PpSlideLayout = ...
    ppLayoutTwoColumnText: PpSlideLayout = ...
    ppLayoutTwoObjects: PpSlideLayout = ...
    ppLayoutTwoObjectsAndObject: PpSlideLayout = ...
    ppLayoutTwoObjectsAndText: PpSlideLayout = ...
    ppLayoutTwoObjectsOverText: PpSlideLayout = ...
    ppLayoutVerticalText: PpSlideLayout = ...
    ppLayoutVerticalTitleAndText: PpSlideLayout = ...
    ppLayoutVerticalTitleAndTextOverChart: PpSlideLayout = ...
    value__ = ...


class PpSlideShowAdvanceMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpSlideShowAdvanceMode, values: ppSlideShowManualAdvance (1), ppSlideShowRehearseNewTimings (3), ppSlideShowUseSlideTimings (2) """
    ppSlideShowManualAdvance: PpSlideShowAdvanceMode = ...
    ppSlideShowRehearseNewTimings: PpSlideShowAdvanceMode = ...
    ppSlideShowUseSlideTimings: PpSlideShowAdvanceMode = ...
    value__ = ...


class PpSlideShowPointerType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpSlideShowPointerType, values: ppSlideShowPointerAlwaysHidden (3), ppSlideShowPointerArrow (1), ppSlideShowPointerAutoArrow (4), ppSlideShowPointerEraser (5), ppSlideShowPointerNone (0), ppSlideShowPointerPen (2) """
    ppSlideShowPointerAlwaysHidden: PpSlideShowPointerType = ...
    ppSlideShowPointerArrow: PpSlideShowPointerType = ...
    ppSlideShowPointerAutoArrow: PpSlideShowPointerType = ...
    ppSlideShowPointerEraser: PpSlideShowPointerType = ...
    ppSlideShowPointerNone: PpSlideShowPointerType = ...
    ppSlideShowPointerPen: PpSlideShowPointerType = ...
    value__ = ...


class PpSlideShowRangeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpSlideShowRangeType, values: ppShowAll (1), ppShowNamedSlideShow (3), ppShowSlideRange (2) """
    ppShowAll: PpSlideShowRangeType = ...
    ppShowNamedSlideShow: PpSlideShowRangeType = ...
    ppShowSlideRange: PpSlideShowRangeType = ...
    value__ = ...


class PpSlideShowState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpSlideShowState, values: ppSlideShowBlackScreen (3), ppSlideShowDone (5), ppSlideShowPaused (2), ppSlideShowRunning (1), ppSlideShowWhiteScreen (4) """
    ppSlideShowBlackScreen: PpSlideShowState = ...
    ppSlideShowDone: PpSlideShowState = ...
    ppSlideShowPaused: PpSlideShowState = ...
    ppSlideShowRunning: PpSlideShowState = ...
    ppSlideShowWhiteScreen: PpSlideShowState = ...
    value__ = ...


class PpSlideShowType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpSlideShowType, values: ppShowTypeKiosk (3), ppShowTypeSpeaker (1), ppShowTypeWindow (2), ppShowTypeWindow2 (4) """
    ppShowTypeKiosk: PpSlideShowType = ...
    ppShowTypeSpeaker: PpSlideShowType = ...
    ppShowTypeWindow: PpSlideShowType = ...
    ppShowTypeWindow2: PpSlideShowType = ...
    value__ = ...


class PpSlideSizeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpSlideSizeType, values: ppSlideSize35MM (4), ppSlideSizeA3Paper (9), ppSlideSizeA4Paper (3), ppSlideSizeB4ISOPaper (10), ppSlideSizeB4JISPaper (12), ppSlideSizeB5ISOPaper (11), ppSlideSizeB5JISPaper (13), ppSlideSizeBanner (6), ppSlideSizeCustom (7), ppSlideSizeHagakiCard (14), ppSlideSizeLedgerPaper (8), ppSlideSizeLetterPaper (2), ppSlideSizeOnScreen (1), ppSlideSizeOnScreen16x10 (16), ppSlideSizeOnScreen16x9 (15), ppSlideSizeOverhead (5) """
    ppSlideSize35MM: PpSlideSizeType = ...
    ppSlideSizeA3Paper: PpSlideSizeType = ...
    ppSlideSizeA4Paper: PpSlideSizeType = ...
    ppSlideSizeB4ISOPaper: PpSlideSizeType = ...
    ppSlideSizeB4JISPaper: PpSlideSizeType = ...
    ppSlideSizeB5ISOPaper: PpSlideSizeType = ...
    ppSlideSizeB5JISPaper: PpSlideSizeType = ...
    ppSlideSizeBanner: PpSlideSizeType = ...
    ppSlideSizeCustom: PpSlideSizeType = ...
    ppSlideSizeHagakiCard: PpSlideSizeType = ...
    ppSlideSizeLedgerPaper: PpSlideSizeType = ...
    ppSlideSizeLetterPaper: PpSlideSizeType = ...
    ppSlideSizeOnScreen: PpSlideSizeType = ...
    ppSlideSizeOnScreen16x10: PpSlideSizeType = ...
    ppSlideSizeOnScreen16x9: PpSlideSizeType = ...
    ppSlideSizeOverhead: PpSlideSizeType = ...
    value__ = ...


class PpSoundEffectType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpSoundEffectType, values: ppSoundEffectsMixed (-2), ppSoundFile (2), ppSoundNone (0), ppSoundStopPrevious (1) """
    ppSoundEffectsMixed: PpSoundEffectType = ...
    ppSoundFile: PpSoundEffectType = ...
    ppSoundNone: PpSoundEffectType = ...
    ppSoundStopPrevious: PpSoundEffectType = ...
    value__ = ...


class PpSoundFormatType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpSoundFormatType, values: ppSoundFormatCDAudio (3), ppSoundFormatMIDI (2), ppSoundFormatMixed (-2), ppSoundFormatNone (0), ppSoundFormatWAV (1) """
    ppSoundFormatCDAudio: PpSoundFormatType = ...
    ppSoundFormatMIDI: PpSoundFormatType = ...
    ppSoundFormatMixed: PpSoundFormatType = ...
    ppSoundFormatNone: PpSoundFormatType = ...
    ppSoundFormatWAV: PpSoundFormatType = ...
    value__ = ...


class PpTabStopType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpTabStopType, values: ppTabStopCenter (2), ppTabStopDecimal (4), ppTabStopLeft (1), ppTabStopMixed (-2), ppTabStopRight (3) """
    ppTabStopCenter: PpTabStopType = ...
    ppTabStopDecimal: PpTabStopType = ...
    ppTabStopLeft: PpTabStopType = ...
    ppTabStopMixed: PpTabStopType = ...
    ppTabStopRight: PpTabStopType = ...
    value__ = ...


class PpTextLevelEffect(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpTextLevelEffect, values: ppAnimateByAllLevels (16), ppAnimateByFifthLevel (5), ppAnimateByFirstLevel (1), ppAnimateByFourthLevel (4), ppAnimateBySecondLevel (2), ppAnimateByThirdLevel (3), ppAnimateLevelMixed (-2), ppAnimateLevelNone (0) """
    ppAnimateByAllLevels: PpTextLevelEffect = ...
    ppAnimateByFifthLevel: PpTextLevelEffect = ...
    ppAnimateByFirstLevel: PpTextLevelEffect = ...
    ppAnimateByFourthLevel: PpTextLevelEffect = ...
    ppAnimateBySecondLevel: PpTextLevelEffect = ...
    ppAnimateByThirdLevel: PpTextLevelEffect = ...
    ppAnimateLevelMixed: PpTextLevelEffect = ...
    ppAnimateLevelNone: PpTextLevelEffect = ...
    value__ = ...


class PpTextStyleType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpTextStyleType, values: ppBodyStyle (3), ppDefaultStyle (1), ppTitleStyle (2) """
    ppBodyStyle: PpTextStyleType = ...
    ppDefaultStyle: PpTextStyleType = ...
    ppTitleStyle: PpTextStyleType = ...
    value__ = ...


class PpTextUnitEffect(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpTextUnitEffect, values: ppAnimateByCharacter (2), ppAnimateByParagraph (0), ppAnimateByWord (1), ppAnimateUnitMixed (-2) """
    ppAnimateByCharacter: PpTextUnitEffect = ...
    ppAnimateByParagraph: PpTextUnitEffect = ...
    ppAnimateByWord: PpTextUnitEffect = ...
    ppAnimateUnitMixed: PpTextUnitEffect = ...
    value__ = ...


class PpTransitionSpeed(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpTransitionSpeed, values: ppTransitionSpeedFast (3), ppTransitionSpeedMedium (2), ppTransitionSpeedMixed (-2), ppTransitionSpeedSlow (1) """
    ppTransitionSpeedFast: PpTransitionSpeed = ...
    ppTransitionSpeedMedium: PpTransitionSpeed = ...
    ppTransitionSpeedMixed: PpTransitionSpeed = ...
    ppTransitionSpeedSlow: PpTransitionSpeed = ...
    value__ = ...


class PpUpdateOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpUpdateOption, values: ppUpdateOptionAutomatic (2), ppUpdateOptionManual (1), ppUpdateOptionMixed (-2) """
    ppUpdateOptionAutomatic: PpUpdateOption = ...
    ppUpdateOptionManual: PpUpdateOption = ...
    ppUpdateOptionMixed: PpUpdateOption = ...
    value__ = ...


class PpViewType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpViewType, values: ppViewHandoutMaster (4), ppViewMasterThumbnails (12), ppViewNormal (9), ppViewNotesMaster (5), ppViewNotesPage (3), ppViewOutline (6), ppViewPrintPreview (10), ppViewSlide (1), ppViewSlideMaster (2), ppViewSlideSorter (7), ppViewThumbnails (11), ppViewTitleMaster (8) """
    ppViewHandoutMaster: PpViewType = ...
    ppViewMasterThumbnails: PpViewType = ...
    ppViewNormal: PpViewType = ...
    ppViewNotesMaster: PpViewType = ...
    ppViewNotesPage: PpViewType = ...
    ppViewOutline: PpViewType = ...
    ppViewPrintPreview: PpViewType = ...
    ppViewSlide: PpViewType = ...
    ppViewSlideMaster: PpViewType = ...
    ppViewSlideSorter: PpViewType = ...
    ppViewThumbnails: PpViewType = ...
    ppViewTitleMaster: PpViewType = ...
    value__ = ...


class PpWindowState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PpWindowState, values: ppWindowMaximized (3), ppWindowMinimized (2), ppWindowNormal (1) """
    ppWindowMaximized: PpWindowState = ...
    ppWindowMinimized: PpWindowState = ...
    ppWindowNormal: PpWindowState = ...
    value__ = ...


class PresEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    pass

class _Presentation: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: _Presentation) -> Application """
        ...

    @property
    def Broadcast(self) -> Broadcast:
        """ Get: Broadcast(self: _Presentation) -> Broadcast """
        ...

    @property
    def BuiltInDocumentProperties(self) -> object:
        """ Get: BuiltInDocumentProperties(self: _Presentation) -> object """
        ...

    @property
    def ChartDataPointTrack(self) -> bool:
        """
        Get: ChartDataPointTrack(self: _Presentation) -> bool
        Set: ChartDataPointTrack(self: _Presentation) = value
        """
        ...

    @property
    def Coauthoring(self) -> Coauthoring:
        """ Get: Coauthoring(self: _Presentation) -> Coauthoring """
        ...

    @property
    def ColorSchemes(self) -> ColorSchemes:
        """ Get: ColorSchemes(self: _Presentation) -> ColorSchemes """
        ...

    @property
    def CommandBars(self) -> CommandBars:
        """ Get: CommandBars(self: _Presentation) -> CommandBars """
        ...

    @property
    def Container(self) -> object:
        """ Get: Container(self: _Presentation) -> object """
        ...

    @property
    def ContentTypeProperties(self): # -> MetaProperties
        """ Get: ContentTypeProperties(self: _Presentation) -> MetaProperties """
        ...

    @property
    def CreateVideoStatus(self) -> PpMediaTaskStatus:
        """ Get: CreateVideoStatus(self: _Presentation) -> PpMediaTaskStatus """
        ...

    @property
    def CustomDocumentProperties(self) -> object:
        """ Get: CustomDocumentProperties(self: _Presentation) -> object """
        ...

    @property
    def CustomerData(self) -> CustomerData:
        """ Get: CustomerData(self: _Presentation) -> CustomerData """
        ...

    @property
    def CustomXMLParts(self): # -> CustomXMLParts
        """ Get: CustomXMLParts(self: _Presentation) -> CustomXMLParts """
        ...

    @property
    def DefaultLanguageID(self): # -> MsoLanguageID
        """
        Get: DefaultLanguageID(self: _Presentation) -> MsoLanguageID
        Set: DefaultLanguageID(self: _Presentation) = value
        """
        ...

    @property
    def DefaultShape(self) -> Shape:
        """ Get: DefaultShape(self: _Presentation) -> Shape """
        ...

    @property
    def Designs(self) -> Designs:
        """ Get: Designs(self: _Presentation) -> Designs """
        ...

    @property
    def DisplayComments(self): # -> MsoTriState
        """
        Get: DisplayComments(self: _Presentation) -> MsoTriState
        Set: DisplayComments(self: _Presentation) = value
        """
        ...

    @property
    def DocumentInspectors(self): # -> DocumentInspectors
        """ Get: DocumentInspectors(self: _Presentation) -> DocumentInspectors """
        ...

    @property
    def DocumentLibraryVersions(self): # -> DocumentLibraryVersions
        """ Get: DocumentLibraryVersions(self: _Presentation) -> DocumentLibraryVersions """
        ...

    @property
    def EncryptionProvider(self) -> str:
        """
        Get: EncryptionProvider(self: _Presentation) -> str
        Set: EncryptionProvider(self: _Presentation) = value
        """
        ...

    @property
    def EnvelopeVisible(self): # -> MsoTriState
        """
        Get: EnvelopeVisible(self: _Presentation) -> MsoTriState
        Set: EnvelopeVisible(self: _Presentation) = value
        """
        ...

    @property
    def ExtraColors(self) -> ExtraColors:
        """ Get: ExtraColors(self: _Presentation) -> ExtraColors """
        ...

    @property
    def FarEastLineBreakLanguage(self): # -> MsoFarEastLineBreakLanguageID
        """
        Get: FarEastLineBreakLanguage(self: _Presentation) -> MsoFarEastLineBreakLanguageID
        Set: FarEastLineBreakLanguage(self: _Presentation) = value
        """
        ...

    @property
    def FarEastLineBreakLevel(self) -> PpFarEastLineBreakLevel:
        """
        Get: FarEastLineBreakLevel(self: _Presentation) -> PpFarEastLineBreakLevel
        Set: FarEastLineBreakLevel(self: _Presentation) = value
        """
        ...

    @property
    def Final(self) -> bool:
        """
        Get: Final(self: _Presentation) -> bool
        Set: Final(self: _Presentation) = value
        """
        ...

    @property
    def Fonts(self) -> Fonts:
        """ Get: Fonts(self: _Presentation) -> Fonts """
        ...

    @property
    def FullName(self) -> str:
        """ Get: FullName(self: _Presentation) -> str """
        ...

    @property
    def GridDistance(self) -> Single:
        """
        Get: GridDistance(self: _Presentation) -> Single
        Set: GridDistance(self: _Presentation) = value
        """
        ...

    @property
    def Guides(self) -> Guides:
        """ Get: Guides(self: _Presentation) -> Guides """
        ...

    @property
    def HandoutMaster(self) -> Master:
        """ Get: HandoutMaster(self: _Presentation) -> Master """
        ...

    @property
    def HasHandoutMaster(self) -> bool:
        """ Get: HasHandoutMaster(self: _Presentation) -> bool """
        ...

    @property
    def HasNotesMaster(self) -> bool:
        """ Get: HasNotesMaster(self: _Presentation) -> bool """
        ...

    @property
    def HasRevisionInfo(self) -> PpRevisionInfo:
        """ Get: HasRevisionInfo(self: _Presentation) -> PpRevisionInfo """
        ...

    @property
    def HasSections(self) -> bool:
        """ Get: HasSections(self: _Presentation) -> bool """
        ...

    @property
    def HasTitleMaster(self): # -> MsoTriState
        """ Get: HasTitleMaster(self: _Presentation) -> MsoTriState """
        ...

    @property
    def HasVBProject(self) -> bool:
        """ Get: HasVBProject(self: _Presentation) -> bool """
        ...

    @property
    def HTMLProject(self): # -> HTMLProject
        """ Get: HTMLProject(self: _Presentation) -> HTMLProject """
        ...

    @property
    def InMergeMode(self) -> bool:
        """ Get: InMergeMode(self: _Presentation) -> bool """
        ...

    @property
    def LayoutDirection(self) -> PpDirection:
        """
        Get: LayoutDirection(self: _Presentation) -> PpDirection
        Set: LayoutDirection(self: _Presentation) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: _Presentation) -> str """
        ...

    @property
    def NoLineBreakAfter(self) -> str:
        """
        Get: NoLineBreakAfter(self: _Presentation) -> str
        Set: NoLineBreakAfter(self: _Presentation) = value
        """
        ...

    @property
    def NoLineBreakBefore(self) -> str:
        """
        Get: NoLineBreakBefore(self: _Presentation) -> str
        Set: NoLineBreakBefore(self: _Presentation) = value
        """
        ...

    @property
    def NotesMaster(self) -> Master:
        """ Get: NotesMaster(self: _Presentation) -> Master """
        ...

    @property
    def PageSetup(self) -> PageSetup:
        """ Get: PageSetup(self: _Presentation) -> PageSetup """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: _Presentation) -> object """
        ...

    @property
    def Password(self) -> str:
        """
        Get: Password(self: _Presentation) -> str
        Set: Password(self: _Presentation) = value
        """
        ...

    @property
    def PasswordEncryptionAlgorithm(self) -> str:
        """ Get: PasswordEncryptionAlgorithm(self: _Presentation) -> str """
        ...

    @property
    def PasswordEncryptionFileProperties(self) -> bool:
        """ Get: PasswordEncryptionFileProperties(self: _Presentation) -> bool """
        ...

    @property
    def PasswordEncryptionKeyLength(self) -> int:
        """ Get: PasswordEncryptionKeyLength(self: _Presentation) -> int """
        ...

    @property
    def PasswordEncryptionProvider(self) -> str:
        """ Get: PasswordEncryptionProvider(self: _Presentation) -> str """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: _Presentation) -> str """
        ...

    @property
    def Permission(self): # -> Permission
        """ Get: Permission(self: _Presentation) -> Permission """
        ...

    @property
    def PrintOptions(self) -> PrintOptions:
        """ Get: PrintOptions(self: _Presentation) -> PrintOptions """
        ...

    @property
    def PublishObjects(self) -> PublishObjects:
        """ Get: PublishObjects(self: _Presentation) -> PublishObjects """
        ...

    @property
    def ReadOnly(self): # -> MsoTriState
        """ Get: ReadOnly(self: _Presentation) -> MsoTriState """
        ...

    @property
    def RemovePersonalInformation(self): # -> MsoTriState
        """
        Get: RemovePersonalInformation(self: _Presentation) -> MsoTriState
        Set: RemovePersonalInformation(self: _Presentation) = value
        """
        ...

    @property
    def Research(self) -> Research:
        """ Get: Research(self: _Presentation) -> Research """
        ...

    @property
    def Saved(self): # -> MsoTriState
        """
        Get: Saved(self: _Presentation) -> MsoTriState
        Set: Saved(self: _Presentation) = value
        """
        ...

    @property
    def SectionCount(self) -> int:
        """ Get: SectionCount(self: _Presentation) -> int """
        ...

    @property
    def SectionProperties(self) -> SectionProperties:
        """ Get: SectionProperties(self: _Presentation) -> SectionProperties """
        ...

    @property
    def ServerPolicy(self): # -> ServerPolicy
        """ Get: ServerPolicy(self: _Presentation) -> ServerPolicy """
        ...

    @property
    def SharedWorkspace(self): # -> SharedWorkspace
        """ Get: SharedWorkspace(self: _Presentation) -> SharedWorkspace """
        ...

    @property
    def Signatures(self): # -> SignatureSet
        """ Get: Signatures(self: _Presentation) -> SignatureSet """
        ...

    @property
    def SlideMaster(self) -> Master:
        """ Get: SlideMaster(self: _Presentation) -> Master """
        ...

    @property
    def Slides(self) -> Slides:
        """ Get: Slides(self: _Presentation) -> Slides """
        ...

    @property
    def SlideShowSettings(self) -> SlideShowSettings:
        """ Get: SlideShowSettings(self: _Presentation) -> SlideShowSettings """
        ...

    @property
    def SlideShowWindow(self) -> SlideShowWindow:
        """ Get: SlideShowWindow(self: _Presentation) -> SlideShowWindow """
        ...

    @property
    def SnapToGrid(self): # -> MsoTriState
        """
        Get: SnapToGrid(self: _Presentation) -> MsoTriState
        Set: SnapToGrid(self: _Presentation) = value
        """
        ...

    @property
    def Sync(self): # -> Sync
        """ Get: Sync(self: _Presentation) -> Sync """
        ...

    @property
    def Tags(self) -> Tags:
        """ Get: Tags(self: _Presentation) -> Tags """
        ...

    @property
    def TemplateName(self) -> str:
        """ Get: TemplateName(self: _Presentation) -> str """
        ...

    @property
    def TitleMaster(self) -> Master:
        """ Get: TitleMaster(self: _Presentation) -> Master """
        ...

    @property
    def VBASigned(self): # -> MsoTriState
        """ Get: VBASigned(self: _Presentation) -> MsoTriState """
        ...

    @property
    def VBProject(self): # -> VBProject
        """ Get: VBProject(self: _Presentation) -> VBProject """
        ...

    @property
    def WebOptions(self) -> WebOptions:
        """ Get: WebOptions(self: _Presentation) -> WebOptions """
        ...

    @property
    def Windows(self) -> DocumentWindows:
        """ Get: Windows(self: _Presentation) -> DocumentWindows """
        ...

    @property
    def WritePassword(self) -> str:
        """
        Get: WritePassword(self: _Presentation) -> str
        Set: WritePassword(self: _Presentation) = value
        """
        ...


    def AcceptAll(self): # -> 
        """ AcceptAll(self: _Presentation) """
        ...

    def AddBaseline(self, FileName:str): # -> 
        """ AddBaseline(self: _Presentation, FileName: str) """
        ...

    def AddTitleMaster(self) -> Master:
        """ AddTitleMaster(self: _Presentation) -> Master """
        ...

    def AddToFavorites(self): # -> 
        """ AddToFavorites(self: _Presentation) """
        ...

    def ApplyTemplate(self, FileName:str): # -> 
        """ ApplyTemplate(self: _Presentation, FileName: str) """
        ...

    def ApplyTemplate2(self, FileName:str, VariantGUID:str): # -> 
        """ ApplyTemplate2(self: _Presentation, FileName: str, VariantGUID: str) """
        ...

    def ApplyTheme(self, themeName:str): # -> 
        """ ApplyTheme(self: _Presentation, themeName: str) """
        ...

    def CanCheckIn(self) -> bool:
        """ CanCheckIn(self: _Presentation) -> bool """
        ...

    def CheckIn(self, SaveChanges:bool, Comments:object, MakePublic:object): # -> 
        """ CheckIn(self: _Presentation, SaveChanges: bool, Comments: object, MakePublic: object) """
        ...

    def CheckInWithVersion(self, SaveChanges:bool, Comments:object, MakePublic:object, VersionType:object): # -> 
        """ CheckInWithVersion(self: _Presentation, SaveChanges: bool, Comments: object, MakePublic: object, VersionType: object) """
        ...

    def Close(self): # -> 
        """ Close(self: _Presentation) """
        ...

    def Convert(self): # -> 
        """ Convert(self: _Presentation) """
        ...

    def Convert2(self, FileName:str): # -> 
        """ Convert2(self: _Presentation, FileName: str) """
        ...

    def CreateVideo(self, FileName:str, UseTimingsAndNarrations:bool, DefaultSlideDuration:int, VertResolution:int, FramesPerSecond:int, Quality:int): # -> 
        """ CreateVideo(self: _Presentation, FileName: str, UseTimingsAndNarrations: bool, DefaultSlideDuration: int, VertResolution: int, FramesPerSecond: int, Quality: int) """
        ...

    def DeleteSection(self, Index:int): # -> 
        """ DeleteSection(self: _Presentation, Index: int) """
        ...

    def DisableSections(self): # -> 
        """ DisableSections(self: _Presentation) """
        ...

    def EndReview(self): # -> 
        """ EndReview(self: _Presentation) """
        ...

    def EnsureAllMediaUpgraded(self): # -> 
        """ EnsureAllMediaUpgraded(self: _Presentation) """
        ...

    def Export(self, Path:str, FilterName:str, ScaleWidth:int, ScaleHeight:int): # -> 
        """ Export(self: _Presentation, Path: str, FilterName: str, ScaleWidth: int, ScaleHeight: int) """
        ...

    def ExportAsFixedFormat(self, Path:str, FixedFormatType:PpFixedFormatType, Intent:PpFixedFormatIntent, FrameSlides, HandoutOrder:PpPrintHandoutOrder, OutputType:PpPrintOutputType, PrintHiddenSlides, PrintRange:PrintRange, RangeType:PpPrintRangeType, SlideShowName:str, IncludeDocProperties:bool, KeepIRMSettings:bool, DocStructureTags:bool, BitmapMissingFonts:bool, UseISO19005_1:bool, ExternalExporter:object): # ->  # Not found arg types: {'FrameSlides': 'MsoTriState', 'PrintHiddenSlides': 'MsoTriState'}
        """ ExportAsFixedFormat(self: _Presentation, Path: str, FixedFormatType: PpFixedFormatType, Intent: PpFixedFormatIntent, FrameSlides: MsoTriState, HandoutOrder: PpPrintHandoutOrder, OutputType: PpPrintOutputType, PrintHiddenSlides: MsoTriState, PrintRange: PrintRange, RangeType: PpPrintRangeType, SlideShowName: str, IncludeDocProperties: bool, KeepIRMSettings: bool, DocStructureTags: bool, BitmapMissingFonts: bool, UseISO19005_1: bool, ExternalExporter: object) """
        ...

    def ExportAsFixedFormat2(self, Path:str, FixedFormatType:PpFixedFormatType, Intent:PpFixedFormatIntent, FrameSlides, HandoutOrder:PpPrintHandoutOrder, OutputType:PpPrintOutputType, PrintHiddenSlides, PrintRange:PrintRange, RangeType:PpPrintRangeType, SlideShowName:str, IncludeDocProperties:bool, KeepIRMSettings:bool, DocStructureTags:bool, BitmapMissingFonts:bool, UseISO19005_1:bool, IncludeMarkup:bool, ExternalExporter:object): # ->  # Not found arg types: {'FrameSlides': 'MsoTriState', 'PrintHiddenSlides': 'MsoTriState'}
        """ ExportAsFixedFormat2(self: _Presentation, Path: str, FixedFormatType: PpFixedFormatType, Intent: PpFixedFormatIntent, FrameSlides: MsoTriState, HandoutOrder: PpPrintHandoutOrder, OutputType: PpPrintOutputType, PrintHiddenSlides: MsoTriState, PrintRange: PrintRange, RangeType: PpPrintRangeType, SlideShowName: str, IncludeDocProperties: bool, KeepIRMSettings: bool, DocStructureTags: bool, BitmapMissingFonts: bool, UseISO19005_1: bool, IncludeMarkup: bool, ExternalExporter: object) """
        ...

    def FollowHyperlink(self, Address:str, SubAddress:str, NewWindow:bool, AddHistory:bool, ExtraInfo:str, Method, HeaderInfo:str): # ->  # Not found arg types: {'Method': 'MsoExtraInfoMethod'}
        """ FollowHyperlink(self: _Presentation, Address: str, SubAddress: str, NewWindow: bool, AddHistory: bool, ExtraInfo: str, Method: MsoExtraInfoMethod, HeaderInfo: str) """
        ...

    def GetWorkflowTasks(self): # -> WorkflowTasks
        """ GetWorkflowTasks(self: _Presentation) -> WorkflowTasks """
        ...

    def GetWorkflowTemplates(self): # -> WorkflowTemplates
        """ GetWorkflowTemplates(self: _Presentation) -> WorkflowTemplates """
        ...

    def LockServerFile(self): # -> 
        """ LockServerFile(self: _Presentation) """
        ...

    def MakeIntoTemplate(self, IsDesignTemplate): # ->  # Not found arg types: {'IsDesignTemplate': 'MsoTriState'}
        """ MakeIntoTemplate(self: _Presentation, IsDesignTemplate: MsoTriState) """
        ...

    def Merge(self, Path:str): # -> 
        """ Merge(self: _Presentation, Path: str) """
        ...

    def MergeWithBaseline(self, withPresentation:str, baselinePresentation:str): # -> 
        """ MergeWithBaseline(self: _Presentation, withPresentation: str, baselinePresentation: str) """
        ...

    def NewSectionAfter(self, Index, AfterSlide, sectionTitle, newSectionIndex) -> int:
        """ NewSectionAfter(self: _Presentation, Index: int, AfterSlide: bool, sectionTitle: str) -> int """
        ...

    def NewWindow(self) -> DocumentWindow:
        """ NewWindow(self: _Presentation) -> DocumentWindow """
        ...

    def PrintOut(self, From:int, To:int, PrintToFile:str, Copies:int, Collate): # ->  # Not found arg types: {'Collate': 'MsoTriState'}
        """ PrintOut(self: _Presentation, From: int, To: int, PrintToFile: str, Copies: int, Collate: MsoTriState) """
        ...

    def PublishSlides(self, SlideLibraryUrl:str, Overwrite:bool, UseSlideOrder:bool): # -> 
        """ PublishSlides(self: _Presentation, SlideLibraryUrl: str, Overwrite: bool, UseSlideOrder: bool) """
        ...

    def RejectAll(self): # -> 
        """ RejectAll(self: _Presentation) """
        ...

    def ReloadAs(self, cp): # ->  # Not found arg types: {'cp': 'MsoEncoding'}
        """ ReloadAs(self: _Presentation, cp: MsoEncoding) """
        ...

    def RemoveBaseline(self): # -> 
        """ RemoveBaseline(self: _Presentation) """
        ...

    def RemoveDocumentInformation(self, Type:PpRemoveDocInfoType): # -> 
        """ RemoveDocumentInformation(self: _Presentation, Type: PpRemoveDocInfoType) """
        ...

    def ReplyWithChanges(self, ShowMessage:bool): # -> 
        """ ReplyWithChanges(self: _Presentation, ShowMessage: bool) """
        ...

    def Save(self): # -> 
        """ Save(self: _Presentation) """
        ...

    def SaveAs(self, FileName:str, FileFormat:PpSaveAsFileType, EmbedTrueTypeFonts): # ->  # Not found arg types: {'EmbedTrueTypeFonts': 'MsoTriState'}
        """ SaveAs(self: _Presentation, FileName: str, FileFormat: PpSaveAsFileType, EmbedTrueTypeFonts: MsoTriState) """
        ...

    def SaveCopyAs(self, FileName:str, FileFormat:PpSaveAsFileType, EmbedTrueTypeFonts): # ->  # Not found arg types: {'EmbedTrueTypeFonts': 'MsoTriState'}
        """ SaveCopyAs(self: _Presentation, FileName: str, FileFormat: PpSaveAsFileType, EmbedTrueTypeFonts: MsoTriState) """
        ...

    def sblt(self, s:str): # -> 
        """ sblt(self: _Presentation, s: str) """
        ...

    def sectionTitle(self, Index:int) -> str:
        """ sectionTitle(self: _Presentation, Index: int) -> str """
        ...

    def SendFaxOverInternet(self, Recipients:str, Subject:str, ShowMessage:bool): # -> 
        """ SendFaxOverInternet(self: _Presentation, Recipients: str, Subject: str, ShowMessage: bool) """
        ...

    def SendForReview(self, Recipients:str, Subject:str, ShowMessage:bool, IncludeAttachment:object): # -> 
        """ SendForReview(self: _Presentation, Recipients: str, Subject: str, ShowMessage: bool, IncludeAttachment: object) """
        ...

    def SetPasswordEncryptionOptions(self, PasswordEncryptionProvider:str, PasswordEncryptionAlgorithm:str, PasswordEncryptionKeyLength:int, PasswordEncryptionFileProperties:bool): # -> 
        """ SetPasswordEncryptionOptions(self: _Presentation, PasswordEncryptionProvider: str, PasswordEncryptionAlgorithm: str, PasswordEncryptionKeyLength: int, PasswordEncryptionFileProperties: bool) """
        ...

    def SetUndoText(self, Text:str): # -> 
        """ SetUndoText(self: _Presentation, Text: str) """
        ...

    def Unused(self): # -> 
        """ Unused(self: _Presentation) """
        ...

    def UpdateLinks(self): # -> 
        """ UpdateLinks(self: _Presentation) """
        ...

    def WebPagePreview(self): # -> 
        """ WebPagePreview(self: _Presentation) """
        ...


class Presentation(PresEvents_Event, _Presentation): # skipped bases: <type 'object'>
    """ no doc """
    pass

class PresentationClass(__ComObject, Presentation): # skipped bases: <type '_Presentation'>, <type 'PresEvents_Event'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PresentationClass) -> Application """
        ...

    @property
    def Broadcast(self) -> Broadcast:
        """ Get: Broadcast(self: PresentationClass) -> Broadcast """
        ...

    @property
    def BuiltInDocumentProperties(self) -> object:
        """ Get: BuiltInDocumentProperties(self: PresentationClass) -> object """
        ...

    @property
    def ChartDataPointTrack(self) -> bool:
        """
        Get: ChartDataPointTrack(self: PresentationClass) -> bool
        Set: ChartDataPointTrack(self: PresentationClass) = value
        """
        ...

    @property
    def Coauthoring(self) -> Coauthoring:
        """ Get: Coauthoring(self: PresentationClass) -> Coauthoring """
        ...

    @property
    def ColorSchemes(self) -> ColorSchemes:
        """ Get: ColorSchemes(self: PresentationClass) -> ColorSchemes """
        ...

    @property
    def CommandBars(self) -> CommandBars:
        """ Get: CommandBars(self: PresentationClass) -> CommandBars """
        ...

    @property
    def Container(self) -> object:
        """ Get: Container(self: PresentationClass) -> object """
        ...

    @property
    def ContentTypeProperties(self): # -> MetaProperties
        """ Get: ContentTypeProperties(self: PresentationClass) -> MetaProperties """
        ...

    @property
    def CreateVideoStatus(self) -> PpMediaTaskStatus:
        """ Get: CreateVideoStatus(self: PresentationClass) -> PpMediaTaskStatus """
        ...

    @property
    def CustomDocumentProperties(self) -> object:
        """ Get: CustomDocumentProperties(self: PresentationClass) -> object """
        ...

    @property
    def CustomerData(self) -> CustomerData:
        """ Get: CustomerData(self: PresentationClass) -> CustomerData """
        ...

    @property
    def CustomXMLParts(self): # -> CustomXMLParts
        """ Get: CustomXMLParts(self: PresentationClass) -> CustomXMLParts """
        ...

    @property
    def DefaultLanguageID(self): # -> MsoLanguageID
        """
        Get: DefaultLanguageID(self: PresentationClass) -> MsoLanguageID
        Set: DefaultLanguageID(self: PresentationClass) = value
        """
        ...

    @property
    def DefaultShape(self) -> Shape:
        """ Get: DefaultShape(self: PresentationClass) -> Shape """
        ...

    @property
    def Designs(self) -> Designs:
        """ Get: Designs(self: PresentationClass) -> Designs """
        ...

    @property
    def DisplayComments(self): # -> MsoTriState
        """
        Get: DisplayComments(self: PresentationClass) -> MsoTriState
        Set: DisplayComments(self: PresentationClass) = value
        """
        ...

    @property
    def DocumentInspectors(self): # -> DocumentInspectors
        """ Get: DocumentInspectors(self: PresentationClass) -> DocumentInspectors """
        ...

    @property
    def DocumentLibraryVersions(self): # -> DocumentLibraryVersions
        """ Get: DocumentLibraryVersions(self: PresentationClass) -> DocumentLibraryVersions """
        ...

    @property
    def EncryptionProvider(self) -> str:
        """
        Get: EncryptionProvider(self: PresentationClass) -> str
        Set: EncryptionProvider(self: PresentationClass) = value
        """
        ...

    @property
    def EnvelopeVisible(self): # -> MsoTriState
        """
        Get: EnvelopeVisible(self: PresentationClass) -> MsoTriState
        Set: EnvelopeVisible(self: PresentationClass) = value
        """
        ...

    @property
    def ExtraColors(self) -> ExtraColors:
        """ Get: ExtraColors(self: PresentationClass) -> ExtraColors """
        ...

    @property
    def FarEastLineBreakLanguage(self): # -> MsoFarEastLineBreakLanguageID
        """
        Get: FarEastLineBreakLanguage(self: PresentationClass) -> MsoFarEastLineBreakLanguageID
        Set: FarEastLineBreakLanguage(self: PresentationClass) = value
        """
        ...

    @property
    def FarEastLineBreakLevel(self) -> PpFarEastLineBreakLevel:
        """
        Get: FarEastLineBreakLevel(self: PresentationClass) -> PpFarEastLineBreakLevel
        Set: FarEastLineBreakLevel(self: PresentationClass) = value
        """
        ...

    @property
    def Final(self) -> bool:
        """
        Get: Final(self: PresentationClass) -> bool
        Set: Final(self: PresentationClass) = value
        """
        ...

    @property
    def Fonts(self) -> Fonts:
        """ Get: Fonts(self: PresentationClass) -> Fonts """
        ...

    @property
    def FullName(self) -> str:
        """ Get: FullName(self: PresentationClass) -> str """
        ...

    @property
    def GridDistance(self) -> Single:
        """
        Get: GridDistance(self: PresentationClass) -> Single
        Set: GridDistance(self: PresentationClass) = value
        """
        ...

    @property
    def Guides(self) -> Guides:
        """ Get: Guides(self: PresentationClass) -> Guides """
        ...

    @property
    def HandoutMaster(self) -> Master:
        """ Get: HandoutMaster(self: PresentationClass) -> Master """
        ...

    @property
    def HasHandoutMaster(self) -> bool:
        """ Get: HasHandoutMaster(self: PresentationClass) -> bool """
        ...

    @property
    def HasNotesMaster(self) -> bool:
        """ Get: HasNotesMaster(self: PresentationClass) -> bool """
        ...

    @property
    def HasRevisionInfo(self) -> PpRevisionInfo:
        """ Get: HasRevisionInfo(self: PresentationClass) -> PpRevisionInfo """
        ...

    @property
    def HasSections(self) -> bool:
        """ Get: HasSections(self: PresentationClass) -> bool """
        ...

    @property
    def HasTitleMaster(self): # -> MsoTriState
        """ Get: HasTitleMaster(self: PresentationClass) -> MsoTriState """
        ...

    @property
    def HasVBProject(self) -> bool:
        """ Get: HasVBProject(self: PresentationClass) -> bool """
        ...

    @property
    def HTMLProject(self): # -> HTMLProject
        """ Get: HTMLProject(self: PresentationClass) -> HTMLProject """
        ...

    @property
    def InMergeMode(self) -> bool:
        """ Get: InMergeMode(self: PresentationClass) -> bool """
        ...

    @property
    def LayoutDirection(self) -> PpDirection:
        """
        Get: LayoutDirection(self: PresentationClass) -> PpDirection
        Set: LayoutDirection(self: PresentationClass) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PresentationClass) -> str """
        ...

    @property
    def NoLineBreakAfter(self) -> str:
        """
        Get: NoLineBreakAfter(self: PresentationClass) -> str
        Set: NoLineBreakAfter(self: PresentationClass) = value
        """
        ...

    @property
    def NoLineBreakBefore(self) -> str:
        """
        Get: NoLineBreakBefore(self: PresentationClass) -> str
        Set: NoLineBreakBefore(self: PresentationClass) = value
        """
        ...

    @property
    def NotesMaster(self) -> Master:
        """ Get: NotesMaster(self: PresentationClass) -> Master """
        ...

    @property
    def PageSetup(self) -> PageSetup:
        """ Get: PageSetup(self: PresentationClass) -> PageSetup """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PresentationClass) -> object """
        ...

    @property
    def Password(self) -> str:
        """
        Get: Password(self: PresentationClass) -> str
        Set: Password(self: PresentationClass) = value
        """
        ...

    @property
    def PasswordEncryptionAlgorithm(self) -> str:
        """ Get: PasswordEncryptionAlgorithm(self: PresentationClass) -> str """
        ...

    @property
    def PasswordEncryptionFileProperties(self) -> bool:
        """ Get: PasswordEncryptionFileProperties(self: PresentationClass) -> bool """
        ...

    @property
    def PasswordEncryptionKeyLength(self) -> int:
        """ Get: PasswordEncryptionKeyLength(self: PresentationClass) -> int """
        ...

    @property
    def PasswordEncryptionProvider(self) -> str:
        """ Get: PasswordEncryptionProvider(self: PresentationClass) -> str """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: PresentationClass) -> str """
        ...

    @property
    def Permission(self): # -> Permission
        """ Get: Permission(self: PresentationClass) -> Permission """
        ...

    @property
    def PrintOptions(self) -> PrintOptions:
        """ Get: PrintOptions(self: PresentationClass) -> PrintOptions """
        ...

    @property
    def PublishObjects(self) -> PublishObjects:
        """ Get: PublishObjects(self: PresentationClass) -> PublishObjects """
        ...

    @property
    def ReadOnly(self): # -> MsoTriState
        """ Get: ReadOnly(self: PresentationClass) -> MsoTriState """
        ...

    @property
    def RemovePersonalInformation(self): # -> MsoTriState
        """
        Get: RemovePersonalInformation(self: PresentationClass) -> MsoTriState
        Set: RemovePersonalInformation(self: PresentationClass) = value
        """
        ...

    @property
    def Research(self) -> Research:
        """ Get: Research(self: PresentationClass) -> Research """
        ...

    @property
    def Saved(self): # -> MsoTriState
        """
        Get: Saved(self: PresentationClass) -> MsoTriState
        Set: Saved(self: PresentationClass) = value
        """
        ...

    @property
    def SectionCount(self) -> int:
        """ Get: SectionCount(self: PresentationClass) -> int """
        ...

    @property
    def SectionProperties(self) -> SectionProperties:
        """ Get: SectionProperties(self: PresentationClass) -> SectionProperties """
        ...

    @property
    def ServerPolicy(self): # -> ServerPolicy
        """ Get: ServerPolicy(self: PresentationClass) -> ServerPolicy """
        ...

    @property
    def SharedWorkspace(self): # -> SharedWorkspace
        """ Get: SharedWorkspace(self: PresentationClass) -> SharedWorkspace """
        ...

    @property
    def Signatures(self): # -> SignatureSet
        """ Get: Signatures(self: PresentationClass) -> SignatureSet """
        ...

    @property
    def SlideMaster(self) -> Master:
        """ Get: SlideMaster(self: PresentationClass) -> Master """
        ...

    @property
    def Slides(self) -> Slides:
        """ Get: Slides(self: PresentationClass) -> Slides """
        ...

    @property
    def SlideShowSettings(self) -> SlideShowSettings:
        """ Get: SlideShowSettings(self: PresentationClass) -> SlideShowSettings """
        ...

    @property
    def SlideShowWindow(self) -> SlideShowWindow:
        """ Get: SlideShowWindow(self: PresentationClass) -> SlideShowWindow """
        ...

    @property
    def SnapToGrid(self): # -> MsoTriState
        """
        Get: SnapToGrid(self: PresentationClass) -> MsoTriState
        Set: SnapToGrid(self: PresentationClass) = value
        """
        ...

    @property
    def Sync(self): # -> Sync
        """ Get: Sync(self: PresentationClass) -> Sync """
        ...

    @property
    def Tags(self) -> Tags:
        """ Get: Tags(self: PresentationClass) -> Tags """
        ...

    @property
    def TemplateName(self) -> str:
        """ Get: TemplateName(self: PresentationClass) -> str """
        ...

    @property
    def TitleMaster(self) -> Master:
        """ Get: TitleMaster(self: PresentationClass) -> Master """
        ...

    @property
    def VBASigned(self): # -> MsoTriState
        """ Get: VBASigned(self: PresentationClass) -> MsoTriState """
        ...

    @property
    def VBProject(self): # -> VBProject
        """ Get: VBProject(self: PresentationClass) -> VBProject """
        ...

    @property
    def WebOptions(self) -> WebOptions:
        """ Get: WebOptions(self: PresentationClass) -> WebOptions """
        ...

    @property
    def Windows(self) -> DocumentWindows:
        """ Get: Windows(self: PresentationClass) -> DocumentWindows """
        ...

    @property
    def WritePassword(self) -> str:
        """
        Get: WritePassword(self: PresentationClass) -> str
        Set: WritePassword(self: PresentationClass) = value
        """
        ...


    def AcceptAll(self): # -> 
        """ AcceptAll(self: PresentationClass) """
        ...

    def AddBaseline(self, FileName:str): # -> 
        """ AddBaseline(self: PresentationClass, FileName: str) """
        ...

    def AddTitleMaster(self) -> Master:
        """ AddTitleMaster(self: PresentationClass) -> Master """
        ...

    def AddToFavorites(self): # -> 
        """ AddToFavorites(self: PresentationClass) """
        ...

    def ApplyTemplate(self, FileName:str): # -> 
        """ ApplyTemplate(self: PresentationClass, FileName: str) """
        ...

    def ApplyTemplate2(self, FileName:str, VariantGUID:str): # -> 
        """ ApplyTemplate2(self: PresentationClass, FileName: str, VariantGUID: str) """
        ...

    def ApplyTheme(self, themeName:str): # -> 
        """ ApplyTheme(self: PresentationClass, themeName: str) """
        ...

    def CanCheckIn(self) -> bool:
        """ CanCheckIn(self: PresentationClass) -> bool """
        ...

    def CheckIn(self, SaveChanges:bool, Comments:object, MakePublic:object): # -> 
        """ CheckIn(self: PresentationClass, SaveChanges: bool, Comments: object, MakePublic: object) """
        ...

    def CheckInWithVersion(self, SaveChanges:bool, Comments:object, MakePublic:object, VersionType:object): # -> 
        """ CheckInWithVersion(self: PresentationClass, SaveChanges: bool, Comments: object, MakePublic: object, VersionType: object) """
        ...

    def Close(self): # -> 
        """ Close(self: PresentationClass) """
        ...

    def Convert(self): # -> 
        """ Convert(self: PresentationClass) """
        ...

    def Convert2(self, FileName:str): # -> 
        """ Convert2(self: PresentationClass, FileName: str) """
        ...

    def CreateVideo(self, FileName:str, UseTimingsAndNarrations:bool, DefaultSlideDuration:int, VertResolution:int, FramesPerSecond:int, Quality:int): # -> 
        """ CreateVideo(self: PresentationClass, FileName: str, UseTimingsAndNarrations: bool, DefaultSlideDuration: int, VertResolution: int, FramesPerSecond: int, Quality: int) """
        ...

    def DeleteSection(self, Index:int): # -> 
        """ DeleteSection(self: PresentationClass, Index: int) """
        ...

    def DisableSections(self): # -> 
        """ DisableSections(self: PresentationClass) """
        ...

    def EndReview(self): # -> 
        """ EndReview(self: PresentationClass) """
        ...

    def EnsureAllMediaUpgraded(self): # -> 
        """ EnsureAllMediaUpgraded(self: PresentationClass) """
        ...

    def Export(self, Path:str, FilterName:str, ScaleWidth:int, ScaleHeight:int): # -> 
        """ Export(self: PresentationClass, Path: str, FilterName: str, ScaleWidth: int, ScaleHeight: int) """
        ...

    def ExportAsFixedFormat(self, Path:str, FixedFormatType:PpFixedFormatType, Intent:PpFixedFormatIntent, FrameSlides, HandoutOrder:PpPrintHandoutOrder, OutputType:PpPrintOutputType, PrintHiddenSlides, PrintRange:PrintRange, RangeType:PpPrintRangeType, SlideShowName:str, IncludeDocProperties:bool, KeepIRMSettings:bool, DocStructureTags:bool, BitmapMissingFonts:bool, UseISO19005_1:bool, ExternalExporter:object): # ->  # Not found arg types: {'FrameSlides': 'MsoTriState', 'PrintHiddenSlides': 'MsoTriState'}
        """ ExportAsFixedFormat(self: PresentationClass, Path: str, FixedFormatType: PpFixedFormatType, Intent: PpFixedFormatIntent, FrameSlides: MsoTriState, HandoutOrder: PpPrintHandoutOrder, OutputType: PpPrintOutputType, PrintHiddenSlides: MsoTriState, PrintRange: PrintRange, RangeType: PpPrintRangeType, SlideShowName: str, IncludeDocProperties: bool, KeepIRMSettings: bool, DocStructureTags: bool, BitmapMissingFonts: bool, UseISO19005_1: bool, ExternalExporter: object) """
        ...

    def ExportAsFixedFormat2(self, Path:str, FixedFormatType:PpFixedFormatType, Intent:PpFixedFormatIntent, FrameSlides, HandoutOrder:PpPrintHandoutOrder, OutputType:PpPrintOutputType, PrintHiddenSlides, PrintRange:PrintRange, RangeType:PpPrintRangeType, SlideShowName:str, IncludeDocProperties:bool, KeepIRMSettings:bool, DocStructureTags:bool, BitmapMissingFonts:bool, UseISO19005_1:bool, IncludeMarkup:bool, ExternalExporter:object): # ->  # Not found arg types: {'FrameSlides': 'MsoTriState', 'PrintHiddenSlides': 'MsoTriState'}
        """ ExportAsFixedFormat2(self: PresentationClass, Path: str, FixedFormatType: PpFixedFormatType, Intent: PpFixedFormatIntent, FrameSlides: MsoTriState, HandoutOrder: PpPrintHandoutOrder, OutputType: PpPrintOutputType, PrintHiddenSlides: MsoTriState, PrintRange: PrintRange, RangeType: PpPrintRangeType, SlideShowName: str, IncludeDocProperties: bool, KeepIRMSettings: bool, DocStructureTags: bool, BitmapMissingFonts: bool, UseISO19005_1: bool, IncludeMarkup: bool, ExternalExporter: object) """
        ...

    def FollowHyperlink(self, Address:str, SubAddress:str, NewWindow:bool, AddHistory:bool, ExtraInfo:str, Method, HeaderInfo:str): # ->  # Not found arg types: {'Method': 'MsoExtraInfoMethod'}
        """ FollowHyperlink(self: PresentationClass, Address: str, SubAddress: str, NewWindow: bool, AddHistory: bool, ExtraInfo: str, Method: MsoExtraInfoMethod, HeaderInfo: str) """
        ...

    def GetWorkflowTasks(self): # -> WorkflowTasks
        """ GetWorkflowTasks(self: PresentationClass) -> WorkflowTasks """
        ...

    def GetWorkflowTemplates(self): # -> WorkflowTemplates
        """ GetWorkflowTemplates(self: PresentationClass) -> WorkflowTemplates """
        ...

    def LockServerFile(self): # -> 
        """ LockServerFile(self: PresentationClass) """
        ...

    def MakeIntoTemplate(self, IsDesignTemplate): # ->  # Not found arg types: {'IsDesignTemplate': 'MsoTriState'}
        """ MakeIntoTemplate(self: PresentationClass, IsDesignTemplate: MsoTriState) """
        ...

    def Merge(self, Path:str): # -> 
        """ Merge(self: PresentationClass, Path: str) """
        ...

    def MergeWithBaseline(self, withPresentation:str, baselinePresentation:str): # -> 
        """ MergeWithBaseline(self: PresentationClass, withPresentation: str, baselinePresentation: str) """
        ...

    def NewSectionAfter(self, Index, AfterSlide, sectionTitle, newSectionIndex) -> int:
        """ NewSectionAfter(self: PresentationClass, Index: int, AfterSlide: bool, sectionTitle: str) -> int """
        ...

    def NewWindow(self) -> DocumentWindow:
        """ NewWindow(self: PresentationClass) -> DocumentWindow """
        ...

    def PrintOut(self, From:int, To:int, PrintToFile:str, Copies:int, Collate): # ->  # Not found arg types: {'Collate': 'MsoTriState'}
        """ PrintOut(self: PresentationClass, From: int, To: int, PrintToFile: str, Copies: int, Collate: MsoTriState) """
        ...

    def PublishSlides(self, SlideLibraryUrl:str, Overwrite:bool, UseSlideOrder:bool): # -> 
        """ PublishSlides(self: PresentationClass, SlideLibraryUrl: str, Overwrite: bool, UseSlideOrder: bool) """
        ...

    def RejectAll(self): # -> 
        """ RejectAll(self: PresentationClass) """
        ...

    def ReloadAs(self, cp): # ->  # Not found arg types: {'cp': 'MsoEncoding'}
        """ ReloadAs(self: PresentationClass, cp: MsoEncoding) """
        ...

    def RemoveBaseline(self): # -> 
        """ RemoveBaseline(self: PresentationClass) """
        ...

    def RemoveDocumentInformation(self, Type:PpRemoveDocInfoType): # -> 
        """ RemoveDocumentInformation(self: PresentationClass, Type: PpRemoveDocInfoType) """
        ...

    def ReplyWithChanges(self, ShowMessage:bool): # -> 
        """ ReplyWithChanges(self: PresentationClass, ShowMessage: bool) """
        ...

    def Save(self): # -> 
        """ Save(self: PresentationClass) """
        ...

    def SaveAs(self, FileName:str, FileFormat:PpSaveAsFileType, EmbedTrueTypeFonts): # ->  # Not found arg types: {'EmbedTrueTypeFonts': 'MsoTriState'}
        """ SaveAs(self: PresentationClass, FileName: str, FileFormat: PpSaveAsFileType, EmbedTrueTypeFonts: MsoTriState) """
        ...

    def SaveCopyAs(self, FileName:str, FileFormat:PpSaveAsFileType, EmbedTrueTypeFonts): # ->  # Not found arg types: {'EmbedTrueTypeFonts': 'MsoTriState'}
        """ SaveCopyAs(self: PresentationClass, FileName: str, FileFormat: PpSaveAsFileType, EmbedTrueTypeFonts: MsoTriState) """
        ...

    def sblt(self, s:str): # -> 
        """ sblt(self: PresentationClass, s: str) """
        ...

    def sectionTitle(self, Index:int) -> str:
        """ sectionTitle(self: PresentationClass, Index: int) -> str """
        ...

    def SendFaxOverInternet(self, Recipients:str, Subject:str, ShowMessage:bool): # -> 
        """ SendFaxOverInternet(self: PresentationClass, Recipients: str, Subject: str, ShowMessage: bool) """
        ...

    def SendForReview(self, Recipients:str, Subject:str, ShowMessage:bool, IncludeAttachment:object): # -> 
        """ SendForReview(self: PresentationClass, Recipients: str, Subject: str, ShowMessage: bool, IncludeAttachment: object) """
        ...

    def SetPasswordEncryptionOptions(self, PasswordEncryptionProvider:str, PasswordEncryptionAlgorithm:str, PasswordEncryptionKeyLength:int, PasswordEncryptionFileProperties:bool): # -> 
        """ SetPasswordEncryptionOptions(self: PresentationClass, PasswordEncryptionProvider: str, PasswordEncryptionAlgorithm: str, PasswordEncryptionKeyLength: int, PasswordEncryptionFileProperties: bool) """
        ...

    def SetUndoText(self, Text:str): # -> 
        """ SetUndoText(self: PresentationClass, Text: str) """
        ...

    def Unused(self): # -> 
        """ Unused(self: PresentationClass) """
        ...

    def UpdateLinks(self): # -> 
        """ UpdateLinks(self: PresentationClass) """
        ...

    def WebPagePreview(self): # -> 
        """ WebPagePreview(self: PresentationClass) """
        ...


class Presentations(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Presentations) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Presentations) -> object """
        ...


    def Add(self, WithWindow) -> Presentation: # Not found arg types: {'WithWindow': 'MsoTriState'}
        """ Add(self: Presentations, WithWindow: MsoTriState) -> Presentation """
        ...

    def CanCheckOut(self, FileName:str) -> bool:
        """ CanCheckOut(self: Presentations, FileName: str) -> bool """
        ...

    def CheckOut(self, FileName:str): # -> 
        """ CheckOut(self: Presentations, FileName: str) """
        ...

    def Open(self, FileName:str, ReadOnly, Untitled, WithWindow) -> Presentation: # Not found arg types: {'Untitled': 'MsoTriState', 'ReadOnly': 'MsoTriState', 'WithWindow': 'MsoTriState'}
        """ Open(self: Presentations, FileName: str, ReadOnly: MsoTriState, Untitled: MsoTriState, WithWindow: MsoTriState) -> Presentation """
        ...

    def Open2007(self, FileName:str, ReadOnly, Untitled, WithWindow, OpenAndRepair) -> Presentation: # Not found arg types: {'Untitled': 'MsoTriState', 'ReadOnly': 'MsoTriState', 'WithWindow': 'MsoTriState', 'OpenAndRepair': 'MsoTriState'}
        """ Open2007(self: Presentations, FileName: str, ReadOnly: MsoTriState, Untitled: MsoTriState, WithWindow: MsoTriState, OpenAndRepair: MsoTriState) -> Presentation """
        ...

    def OpenOld(self, FileName:str, ReadOnly, Untitled, WithWindow) -> Presentation: # Not found arg types: {'Untitled': 'MsoTriState', 'ReadOnly': 'MsoTriState', 'WithWindow': 'MsoTriState'}
        """ OpenOld(self: Presentations, FileName: str, ReadOnly: MsoTriState, Untitled: MsoTriState, WithWindow: MsoTriState) -> Presentation """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class PresEvents: # skipped bases: <type 'object'>
    """ no doc """
    pass

class PresEvents_SinkHelper(PresEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_dwCookie = ...


class PrintOptions: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActivePrinter(self) -> str:
        """
        Get: ActivePrinter(self: PrintOptions) -> str
        Set: ActivePrinter(self: PrintOptions) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: PrintOptions) -> Application """
        ...

    @property
    def Collate(self): # -> MsoTriState
        """
        Get: Collate(self: PrintOptions) -> MsoTriState
        Set: Collate(self: PrintOptions) = value
        """
        ...

    @property
    def FitToPage(self): # -> MsoTriState
        """
        Get: FitToPage(self: PrintOptions) -> MsoTriState
        Set: FitToPage(self: PrintOptions) = value
        """
        ...

    @property
    def FrameSlides(self): # -> MsoTriState
        """
        Get: FrameSlides(self: PrintOptions) -> MsoTriState
        Set: FrameSlides(self: PrintOptions) = value
        """
        ...

    @property
    def HandoutOrder(self) -> PpPrintHandoutOrder:
        """
        Get: HandoutOrder(self: PrintOptions) -> PpPrintHandoutOrder
        Set: HandoutOrder(self: PrintOptions) = value
        """
        ...

    @property
    def HighQuality(self): # -> MsoTriState
        """
        Get: HighQuality(self: PrintOptions) -> MsoTriState
        Set: HighQuality(self: PrintOptions) = value
        """
        ...

    @property
    def NumberOfCopies(self) -> int:
        """
        Get: NumberOfCopies(self: PrintOptions) -> int
        Set: NumberOfCopies(self: PrintOptions) = value
        """
        ...

    @property
    def OutputType(self) -> PpPrintOutputType:
        """
        Get: OutputType(self: PrintOptions) -> PpPrintOutputType
        Set: OutputType(self: PrintOptions) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PrintOptions) -> object """
        ...

    @property
    def PrintColorType(self) -> PpPrintColorType:
        """
        Get: PrintColorType(self: PrintOptions) -> PpPrintColorType
        Set: PrintColorType(self: PrintOptions) = value
        """
        ...

    @property
    def PrintComments(self): # -> MsoTriState
        """
        Get: PrintComments(self: PrintOptions) -> MsoTriState
        Set: PrintComments(self: PrintOptions) = value
        """
        ...

    @property
    def PrintFontsAsGraphics(self): # -> MsoTriState
        """
        Get: PrintFontsAsGraphics(self: PrintOptions) -> MsoTriState
        Set: PrintFontsAsGraphics(self: PrintOptions) = value
        """
        ...

    @property
    def PrintHiddenSlides(self): # -> MsoTriState
        """
        Get: PrintHiddenSlides(self: PrintOptions) -> MsoTriState
        Set: PrintHiddenSlides(self: PrintOptions) = value
        """
        ...

    @property
    def PrintInBackground(self): # -> MsoTriState
        """
        Get: PrintInBackground(self: PrintOptions) -> MsoTriState
        Set: PrintInBackground(self: PrintOptions) = value
        """
        ...

    @property
    def Ranges(self) -> PrintRanges:
        """ Get: Ranges(self: PrintOptions) -> PrintRanges """
        ...

    @property
    def RangeType(self) -> PpPrintRangeType:
        """
        Get: RangeType(self: PrintOptions) -> PpPrintRangeType
        Set: RangeType(self: PrintOptions) = value
        """
        ...

    @property
    def sectionIndex(self) -> int:
        """
        Get: sectionIndex(self: PrintOptions) -> int
        Set: sectionIndex(self: PrintOptions) = value
        """
        ...

    @property
    def SlideShowName(self) -> str:
        """
        Get: SlideShowName(self: PrintOptions) -> str
        Set: SlideShowName(self: PrintOptions) = value
        """
        ...



class PrintRange: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PrintRange) -> Application """
        ...

    @property
    def End(self) -> int:
        """ Get: End(self: PrintRange) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PrintRange) -> object """
        ...

    @property
    def Start(self) -> int:
        """ Get: Start(self: PrintRange) -> int """
        ...


    def Delete(self): # -> 
        """ Delete(self: PrintRange) """
        ...


class PrintRanges(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PrintRanges) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PrintRanges) -> object """
        ...


    def Add(self, Start:int, End:int) -> PrintRange:
        """ Add(self: PrintRanges, Start: int, End: int) -> PrintRange """
        ...

    def ClearAll(self): # -> 
        """ ClearAll(self: PrintRanges) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class PropertyEffect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PropertyEffect) -> Application """
        ...

    @property
    def From(self) -> object:
        """
        Get: From(self: PropertyEffect) -> object
        Set: From(self: PropertyEffect) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PropertyEffect) -> object """
        ...

    @property
    def Points(self) -> AnimationPoints:
        """ Get: Points(self: PropertyEffect) -> AnimationPoints """
        ...

    @property
    def Property(self) -> MsoAnimProperty:
        """
        Get: Property(self: PropertyEffect) -> MsoAnimProperty
        Set: Property(self: PropertyEffect) = value
        """
        ...

    @property
    def To(self) -> object:
        """
        Get: To(self: PropertyEffect) -> object
        Set: To(self: PropertyEffect) = value
        """
        ...



class ProtectedViewWindow: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Active(self): # -> MsoTriState
        """ Get: Active(self: ProtectedViewWindow) -> MsoTriState """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: ProtectedViewWindow) -> Application """
        ...

    @property
    def Caption(self) -> str:
        """ Get: Caption(self: ProtectedViewWindow) -> str """
        ...

    @property
    def Height(self) -> Single:
        """
        Get: Height(self: ProtectedViewWindow) -> Single
        Set: Height(self: ProtectedViewWindow) = value
        """
        ...

    @property
    def HWND(self) -> int:
        """ Get: HWND(self: ProtectedViewWindow) -> int """
        ...

    @property
    def Left(self) -> Single:
        """
        Get: Left(self: ProtectedViewWindow) -> Single
        Set: Left(self: ProtectedViewWindow) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ProtectedViewWindow) -> object """
        ...

    @property
    def Presentation(self) -> Presentation:
        """ Get: Presentation(self: ProtectedViewWindow) -> Presentation """
        ...

    @property
    def SourceName(self) -> str:
        """ Get: SourceName(self: ProtectedViewWindow) -> str """
        ...

    @property
    def SourcePath(self) -> str:
        """ Get: SourcePath(self: ProtectedViewWindow) -> str """
        ...

    @property
    def Top(self) -> Single:
        """
        Get: Top(self: ProtectedViewWindow) -> Single
        Set: Top(self: ProtectedViewWindow) = value
        """
        ...

    @property
    def Width(self) -> Single:
        """
        Get: Width(self: ProtectedViewWindow) -> Single
        Set: Width(self: ProtectedViewWindow) = value
        """
        ...

    @property
    def WindowState(self) -> PpWindowState:
        """
        Get: WindowState(self: ProtectedViewWindow) -> PpWindowState
        Set: WindowState(self: ProtectedViewWindow) = value
        """
        ...


    def Activate(self): # -> 
        """ Activate(self: ProtectedViewWindow) """
        ...

    def Close(self): # -> 
        """ Close(self: ProtectedViewWindow) """
        ...

    def Edit(self, ModifyPassword:str) -> Presentation:
        """ Edit(self: ProtectedViewWindow, ModifyPassword: str) -> Presentation """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ProtectedViewWindows(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ProtectedViewWindows) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ProtectedViewWindows) -> object """
        ...


    def Open(self, FileName:str, ReadPassword:str, OpenAndRepair) -> ProtectedViewWindow: # Not found arg types: {'OpenAndRepair': 'MsoTriState'}
        """ Open(self: ProtectedViewWindows, FileName: str, ReadPassword: str, OpenAndRepair: MsoTriState) -> ProtectedViewWindow """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class PublishObject: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PublishObject) -> Application """
        ...

    @property
    def FileName(self) -> str:
        """
        Get: FileName(self: PublishObject) -> str
        Set: FileName(self: PublishObject) = value
        """
        ...

    @property
    def HTMLVersion(self) -> PpHTMLVersion:
        """
        Get: HTMLVersion(self: PublishObject) -> PpHTMLVersion
        Set: HTMLVersion(self: PublishObject) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PublishObject) -> object """
        ...

    @property
    def RangeEnd(self) -> int:
        """
        Get: RangeEnd(self: PublishObject) -> int
        Set: RangeEnd(self: PublishObject) = value
        """
        ...

    @property
    def RangeStart(self) -> int:
        """
        Get: RangeStart(self: PublishObject) -> int
        Set: RangeStart(self: PublishObject) = value
        """
        ...

    @property
    def SlideShowName(self) -> str:
        """
        Get: SlideShowName(self: PublishObject) -> str
        Set: SlideShowName(self: PublishObject) = value
        """
        ...

    @property
    def SourceType(self) -> PpPublishSourceType:
        """
        Get: SourceType(self: PublishObject) -> PpPublishSourceType
        Set: SourceType(self: PublishObject) = value
        """
        ...

    @property
    def SpeakerNotes(self): # -> MsoTriState
        """
        Get: SpeakerNotes(self: PublishObject) -> MsoTriState
        Set: SpeakerNotes(self: PublishObject) = value
        """
        ...


    def Publish(self): # -> 
        """ Publish(self: PublishObject) """
        ...


class PublishObjects(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PublishObjects) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: PublishObjects) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ResampleMediaTask: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AudioCompressionType(self) -> str:
        """ Get: AudioCompressionType(self: ResampleMediaTask) -> str """
        ...

    @property
    def AudioSamplingRate(self) -> int:
        """ Get: AudioSamplingRate(self: ResampleMediaTask) -> int """
        ...

    @property
    def ContainerType(self) -> str:
        """ Get: ContainerType(self: ResampleMediaTask) -> str """
        ...

    @property
    def IsEmbedded(self) -> bool:
        """ Get: IsEmbedded(self: ResampleMediaTask) -> bool """
        ...

    @property
    def IsLinked(self) -> bool:
        """ Get: IsLinked(self: ResampleMediaTask) -> bool """
        ...

    @property
    def profile(self) -> PpResampleMediaProfile:
        """ Get: profile(self: ResampleMediaTask) -> PpResampleMediaProfile """
        ...

    @property
    def SampleHeight(self) -> int:
        """ Get: SampleHeight(self: ResampleMediaTask) -> int """
        ...

    @property
    def SampleWidth(self) -> int:
        """ Get: SampleWidth(self: ResampleMediaTask) -> int """
        ...

    @property
    def Shape(self) -> Shape:
        """ Get: Shape(self: ResampleMediaTask) -> Shape """
        ...

    @property
    def VideoCompressionType(self) -> str:
        """ Get: VideoCompressionType(self: ResampleMediaTask) -> str """
        ...

    @property
    def VideoFrameRate(self) -> int:
        """ Get: VideoFrameRate(self: ResampleMediaTask) -> int """
        ...



class ResampleMediaTasks(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def PercentComplete(self) -> int:
        """ Get: PercentComplete(self: ResampleMediaTasks) -> int """
        ...


    def Cancel(self): # -> 
        """ Cancel(self: ResampleMediaTasks) """
        ...

    def Pause(self): # -> 
        """ Pause(self: ResampleMediaTasks) """
        ...

    def Resume(self): # -> 
        """ Resume(self: ResampleMediaTasks) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Research: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Research) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Research) -> object """
        ...


    def IsResearchService(self, ServiceID:str) -> bool:
        """ IsResearchService(self: Research, ServiceID: str) -> bool """
        ...

    def Query(self, ServiceID:str, QueryString:object, QueryLanguage:object, UseSelection:bool, LaunchQuery:bool) -> Tuple_[object, object]:
        """ Query(self: Research, ServiceID: str, QueryString: object, QueryLanguage: object, UseSelection: bool, LaunchQuery: bool) -> (object, object) """
        ...

    def SetLanguagePair(self, Language1:object, Language2:object) -> Tuple_[object, object]:
        """ SetLanguagePair(self: Research, Language1: object, Language2: object) -> (object, object) """
        ...


class RGBColor: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: RGBColor) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: RGBColor) -> object """
        ...

    @property
    def RGB(self) -> int:
        """
        Get: RGB(self: RGBColor) -> int
        Set: RGB(self: RGBColor) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class RotationEffect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: RotationEffect) -> Application """
        ...

    @property
    def By(self) -> Single:
        """
        Get: By(self: RotationEffect) -> Single
        Set: By(self: RotationEffect) = value
        """
        ...

    @property
    def From(self) -> Single:
        """
        Get: From(self: RotationEffect) -> Single
        Set: From(self: RotationEffect) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: RotationEffect) -> object """
        ...

    @property
    def To(self) -> Single:
        """
        Get: To(self: RotationEffect) -> Single
        Set: To(self: RotationEffect) = value
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
    def Height(self) -> Single:
        """
        Get: Height(self: Row) -> Single
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

    def Select(self): # -> 
        """ Select(self: Row) """
        ...


class Rows(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Rows) -> Application """
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


class Ruler: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Ruler) -> Application """
        ...

    @property
    def Levels(self) -> RulerLevels:
        """ Get: Levels(self: Ruler) -> RulerLevels """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Ruler) -> object """
        ...

    @property
    def TabStops(self) -> TabStops:
        """ Get: TabStops(self: Ruler) -> TabStops """
        ...



class RulerLevel: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: RulerLevel) -> Application """
        ...

    @property
    def FirstMargin(self) -> Single:
        """
        Get: FirstMargin(self: RulerLevel) -> Single
        Set: FirstMargin(self: RulerLevel) = value
        """
        ...

    @property
    def LeftMargin(self) -> Single:
        """
        Get: LeftMargin(self: RulerLevel) -> Single
        Set: LeftMargin(self: RulerLevel) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: RulerLevel) -> object """
        ...



class RulerLevels(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: RulerLevels) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: RulerLevels) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ScaleEffect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ScaleEffect) -> Application """
        ...

    @property
    def ByX(self) -> Single:
        """
        Get: ByX(self: ScaleEffect) -> Single
        Set: ByX(self: ScaleEffect) = value
        """
        ...

    @property
    def ByY(self) -> Single:
        """
        Get: ByY(self: ScaleEffect) -> Single
        Set: ByY(self: ScaleEffect) = value
        """
        ...

    @property
    def FromX(self) -> Single:
        """
        Get: FromX(self: ScaleEffect) -> Single
        Set: FromX(self: ScaleEffect) = value
        """
        ...

    @property
    def FromY(self) -> Single:
        """
        Get: FromY(self: ScaleEffect) -> Single
        Set: FromY(self: ScaleEffect) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ScaleEffect) -> object """
        ...

    @property
    def ToX(self) -> Single:
        """
        Get: ToX(self: ScaleEffect) -> Single
        Set: ToX(self: ScaleEffect) = value
        """
        ...

    @property
    def ToY(self) -> Single:
        """
        Get: ToY(self: ScaleEffect) -> Single
        Set: ToY(self: ScaleEffect) = value
        """
        ...



class SectionProperties: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: SectionProperties) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: SectionProperties) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: SectionProperties) -> object """
        ...


    def AddBeforeSlide(self, SlideIndex:int, sectionName:str) -> int:
        """ AddBeforeSlide(self: SectionProperties, SlideIndex: int, sectionName: str) -> int """
        ...

    def AddSection(self, sectionIndex:int, sectionName:object) -> int:
        """ AddSection(self: SectionProperties, sectionIndex: int, sectionName: object) -> int """
        ...

    def Delete(self, sectionIndex:int, deleteSlides:bool): # -> 
        """ Delete(self: SectionProperties, sectionIndex: int, deleteSlides: bool) """
        ...

    def FirstSlide(self, sectionIndex:int) -> int:
        """ FirstSlide(self: SectionProperties, sectionIndex: int) -> int """
        ...

    def Move(self, sectionIndex:int, toPos:int): # -> 
        """ Move(self: SectionProperties, sectionIndex: int, toPos: int) """
        ...

    def Name(self, sectionIndex:int) -> str:
        """ Name(self: SectionProperties, sectionIndex: int) -> str """
        ...

    def Rename(self, sectionIndex:int, sectionName:str): # -> 
        """ Rename(self: SectionProperties, sectionIndex: int, sectionName: str) """
        ...

    def SectionID(self, sectionIndex:int) -> str:
        """ SectionID(self: SectionProperties, sectionIndex: int) -> str """
        ...

    def SlidesCount(self, sectionIndex:int) -> int:
        """ SlidesCount(self: SectionProperties, sectionIndex: int) -> int """
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
    def HasChildShapeRange(self) -> bool:
        """ Get: HasChildShapeRange(self: Selection) -> bool """
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
    def SlideRange(self) -> SlideRange:
        """ Get: SlideRange(self: Selection) -> SlideRange """
        ...

    @property
    def TextRange(self) -> TextRange:
        """ Get: TextRange(self: Selection) -> TextRange """
        ...

    @property
    def TextRange2(self): # -> TextRange2
        """ Get: TextRange2(self: Selection) -> TextRange2 """
        ...

    @property
    def Type(self) -> PpSelectionType:
        """ Get: Type(self: Selection) -> PpSelectionType """
        ...


    def Copy(self): # -> 
        """ Copy(self: Selection) """
        ...

    def Cut(self): # -> 
        """ Cut(self: Selection) """
        ...

    def Delete(self): # -> 
        """ Delete(self: Selection) """
        ...

    def Unselect(self): # -> 
        """ Unselect(self: Selection) """
        ...


class Sequence(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Sequence) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Sequence) -> object """
        ...


    def AddEffect(self, Shape:Shape, effectId:MsoAnimEffect, Level:MsoAnimateByLevel, trigger:MsoAnimTriggerType, Index:int) -> Effect:
        """ AddEffect(self: Sequence, Shape: Shape, effectId: MsoAnimEffect, Level: MsoAnimateByLevel, trigger: MsoAnimTriggerType, Index: int) -> Effect """
        ...

    def AddTriggerEffect(self, pShape:Shape, effectId:MsoAnimEffect, trigger:MsoAnimTriggerType, pTriggerShape:Shape, bookmark:str, Level:MsoAnimateByLevel) -> Effect:
        """ AddTriggerEffect(self: Sequence, pShape: Shape, effectId: MsoAnimEffect, trigger: MsoAnimTriggerType, pTriggerShape: Shape, bookmark: str, Level: MsoAnimateByLevel) -> Effect """
        ...

    def Clone(self, Effect:Effect, Index:int) -> Effect:
        """ Clone(self: Sequence, Effect: Effect, Index: int) -> Effect """
        ...

    def ConvertToAfterEffect(self, Effect:Effect, After:MsoAnimAfterEffect, DimColor:int, DimSchemeColor:PpColorSchemeIndex) -> Effect:
        """ ConvertToAfterEffect(self: Sequence, Effect: Effect, After: MsoAnimAfterEffect, DimColor: int, DimSchemeColor: PpColorSchemeIndex) -> Effect """
        ...

    def ConvertToAnimateBackground(self, Effect:Effect, AnimateBackground) -> Effect: # Not found arg types: {'AnimateBackground': 'MsoTriState'}
        """ ConvertToAnimateBackground(self: Sequence, Effect: Effect, AnimateBackground: MsoTriState) -> Effect """
        ...

    def ConvertToAnimateInReverse(self, Effect:Effect, animateInReverse) -> Effect: # Not found arg types: {'animateInReverse': 'MsoTriState'}
        """ ConvertToAnimateInReverse(self: Sequence, Effect: Effect, animateInReverse: MsoTriState) -> Effect """
        ...

    def ConvertToBuildLevel(self, Effect:Effect, Level:MsoAnimateByLevel) -> Effect:
        """ ConvertToBuildLevel(self: Sequence, Effect: Effect, Level: MsoAnimateByLevel) -> Effect """
        ...

    def ConvertToTextUnitEffect(self, Effect:Effect, unitEffect:MsoAnimTextUnitEffect) -> Effect:
        """ ConvertToTextUnitEffect(self: Sequence, Effect: Effect, unitEffect: MsoAnimTextUnitEffect) -> Effect """
        ...

    def FindFirstAnimationFor(self, Shape:Shape) -> Effect:
        """ FindFirstAnimationFor(self: Sequence, Shape: Shape) -> Effect """
        ...

    def FindFirstAnimationForClick(self, click:int) -> Effect:
        """ FindFirstAnimationForClick(self: Sequence, click: int) -> Effect """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Sequences(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Sequences) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Sequences) -> object """
        ...


    def Add(self, Index:int) -> Sequence:
        """ Add(self: Sequences, Index: int) -> Sequence """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Series: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Series) -> Application """
        ...

    @property
    def ApplyPictToEnd(self) -> bool:
        """
        Get: ApplyPictToEnd(self: Series) -> bool
        Set: ApplyPictToEnd(self: Series) = value
        """
        ...

    @property
    def ApplyPictToFront(self) -> bool:
        """
        Get: ApplyPictToFront(self: Series) -> bool
        Set: ApplyPictToFront(self: Series) = value
        """
        ...

    @property
    def ApplyPictToSides(self) -> bool:
        """
        Get: ApplyPictToSides(self: Series) -> bool
        Set: ApplyPictToSides(self: Series) = value
        """
        ...

    @property
    def AxisGroup(self) -> XlAxisGroup:
        """
        Get: AxisGroup(self: Series) -> XlAxisGroup
        Set: AxisGroup(self: Series) = value
        """
        ...

    @property
    def BarShape(self) -> XlBarShape:
        """
        Get: BarShape(self: Series) -> XlBarShape
        Set: BarShape(self: Series) = value
        """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: Series) -> ChartBorder """
        ...

    @property
    def BubbleSizes(self) -> object:
        """
        Get: BubbleSizes(self: Series) -> object
        Set: BubbleSizes(self: Series) = value
        """
        ...

    @property
    def ChartType(self) -> XlChartType:
        """
        Get: ChartType(self: Series) -> XlChartType
        Set: ChartType(self: Series) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Series) -> int """
        ...

    @property
    def ErrorBars(self) -> ErrorBars:
        """ Get: ErrorBars(self: Series) -> ErrorBars """
        ...

    @property
    def Explosion(self) -> int:
        """
        Get: Explosion(self: Series) -> int
        Set: Explosion(self: Series) = value
        """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: Series) -> ChartFillFormat """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: Series) -> ChartFormat """
        ...

    @property
    def Formula(self) -> str:
        """
        Get: Formula(self: Series) -> str
        Set: Formula(self: Series) = value
        """
        ...

    @property
    def FormulaLocal(self) -> str:
        """
        Get: FormulaLocal(self: Series) -> str
        Set: FormulaLocal(self: Series) = value
        """
        ...

    @property
    def FormulaR1C1(self) -> str:
        """
        Get: FormulaR1C1(self: Series) -> str
        Set: FormulaR1C1(self: Series) = value
        """
        ...

    @property
    def FormulaR1C1Local(self) -> str:
        """
        Get: FormulaR1C1Local(self: Series) -> str
        Set: FormulaR1C1Local(self: Series) = value
        """
        ...

    @property
    def Has3DEffect(self) -> bool:
        """
        Get: Has3DEffect(self: Series) -> bool
        Set: Has3DEffect(self: Series) = value
        """
        ...

    @property
    def HasDataLabels(self) -> bool:
        """
        Get: HasDataLabels(self: Series) -> bool
        Set: HasDataLabels(self: Series) = value
        """
        ...

    @property
    def HasErrorBars(self) -> bool:
        """
        Get: HasErrorBars(self: Series) -> bool
        Set: HasErrorBars(self: Series) = value
        """
        ...

    @property
    def HasLeaderLines(self) -> bool:
        """
        Get: HasLeaderLines(self: Series) -> bool
        Set: HasLeaderLines(self: Series) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: Series) -> Interior """
        ...

    @property
    def InvertColor(self) -> int:
        """
        Get: InvertColor(self: Series) -> int
        Set: InvertColor(self: Series) = value
        """
        ...

    @property
    def InvertColorIndex(self) -> XlColorIndex:
        """
        Get: InvertColorIndex(self: Series) -> XlColorIndex
        Set: InvertColorIndex(self: Series) = value
        """
        ...

    @property
    def InvertIfNegative(self) -> bool:
        """
        Get: InvertIfNegative(self: Series) -> bool
        Set: InvertIfNegative(self: Series) = value
        """
        ...

    @property
    def IsFiltered(self) -> bool:
        """
        Get: IsFiltered(self: Series) -> bool
        Set: IsFiltered(self: Series) = value
        """
        ...

    @property
    def LeaderLines(self) -> LeaderLines:
        """ Get: LeaderLines(self: Series) -> LeaderLines """
        ...

    @property
    def MarkerBackgroundColor(self) -> int:
        """
        Get: MarkerBackgroundColor(self: Series) -> int
        Set: MarkerBackgroundColor(self: Series) = value
        """
        ...

    @property
    def MarkerBackgroundColorIndex(self) -> XlColorIndex:
        """
        Get: MarkerBackgroundColorIndex(self: Series) -> XlColorIndex
        Set: MarkerBackgroundColorIndex(self: Series) = value
        """
        ...

    @property
    def MarkerForegroundColor(self) -> int:
        """
        Get: MarkerForegroundColor(self: Series) -> int
        Set: MarkerForegroundColor(self: Series) = value
        """
        ...

    @property
    def MarkerForegroundColorIndex(self) -> XlColorIndex:
        """
        Get: MarkerForegroundColorIndex(self: Series) -> XlColorIndex
        Set: MarkerForegroundColorIndex(self: Series) = value
        """
        ...

    @property
    def MarkerSize(self) -> int:
        """
        Get: MarkerSize(self: Series) -> int
        Set: MarkerSize(self: Series) = value
        """
        ...

    @property
    def MarkerStyle(self) -> XlMarkerStyle:
        """
        Get: MarkerStyle(self: Series) -> XlMarkerStyle
        Set: MarkerStyle(self: Series) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Series) -> str
        Set: Name(self: Series) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Series) -> object """
        ...

    @property
    def PictureType(self) -> XlChartPictureType:
        """
        Get: PictureType(self: Series) -> XlChartPictureType
        Set: PictureType(self: Series) = value
        """
        ...

    @property
    def PictureUnit(self) -> int:
        """
        Get: PictureUnit(self: Series) -> int
        Set: PictureUnit(self: Series) = value
        """
        ...

    @property
    def PictureUnit2(self) -> float:
        """
        Get: PictureUnit2(self: Series) -> float
        Set: PictureUnit2(self: Series) = value
        """
        ...

    @property
    def PlotColorIndex(self) -> int:
        """ Get: PlotColorIndex(self: Series) -> int """
        ...

    @property
    def PlotOrder(self) -> int:
        """
        Get: PlotOrder(self: Series) -> int
        Set: PlotOrder(self: Series) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: Series) -> bool
        Set: Shadow(self: Series) = value
        """
        ...

    @property
    def Smooth(self) -> bool:
        """
        Get: Smooth(self: Series) -> bool
        Set: Smooth(self: Series) = value
        """
        ...

    @property
    def Type(self) -> int:
        """
        Get: Type(self: Series) -> int
        Set: Type(self: Series) = value
        """
        ...

    @property
    def Values(self) -> object:
        """
        Get: Values(self: Series) -> object
        Set: Values(self: Series) = value
        """
        ...

    @property
    def XValues(self) -> object:
        """
        Get: XValues(self: Series) -> object
        Set: XValues(self: Series) = value
        """
        ...


    def ApplyCustomType(self, ChartType:XlChartType): # -> 
        """ ApplyCustomType(self: Series, ChartType: XlChartType) """
        ...

    def ApplyDataLabels(self, Type:XlDataLabelsType, LegendKey:object, AutoText:object, HasLeaderLines:object, ShowSeriesName:object, ShowCategoryName:object, ShowValue:object, ShowPercentage:object, ShowBubbleSize:object, Separator:object) -> object:
        """ ApplyDataLabels(self: Series, Type: XlDataLabelsType, LegendKey: object, AutoText: object, HasLeaderLines: object, ShowSeriesName: object, ShowCategoryName: object, ShowValue: object, ShowPercentage: object, ShowBubbleSize: object, Separator: object) -> object """
        ...

    def ClearFormats(self) -> object:
        """ ClearFormats(self: Series) -> object """
        ...

    def Copy(self) -> object:
        """ Copy(self: Series) -> object """
        ...

    def DataLabels(self, Index:object) -> object:
        """ DataLabels(self: Series, Index: object) -> object """
        ...

    def Delete(self) -> object:
        """ Delete(self: Series) -> object """
        ...

    def ErrorBar(self, Direction:XlErrorBarDirection, Include:XlErrorBarInclude, Type:XlErrorBarType, Amount:object, MinusValues:object) -> object:
        """ ErrorBar(self: Series, Direction: XlErrorBarDirection, Include: XlErrorBarInclude, Type: XlErrorBarType, Amount: object, MinusValues: object) -> object """
        ...

    def Paste(self) -> object:
        """ Paste(self: Series) -> object """
        ...

    def Points(self, Index:object) -> object:
        """ Points(self: Series, Index: object) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: Series) -> object """
        ...

    def Trendlines(self, Index:object) -> object:
        """ Trendlines(self: Series, Index: object) -> object """
        ...

    def _ApplyDataLabels(self, Type:XlDataLabelsType, LegendKey:object, AutoText:object, HasLeaderLines:object) -> object:
        """ _ApplyDataLabels(self: Series, Type: XlDataLabelsType, LegendKey: object, AutoText: object, HasLeaderLines: object) -> object """
        ...


class SeriesCollection(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: SeriesCollection) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: SeriesCollection) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: SeriesCollection) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: SeriesCollection) -> object """
        ...


    def Add(self, Source:object, Rowcol:XlRowCol, SeriesLabels:object, CategoryLabels:object, Replace:object) -> Series:
        """ Add(self: SeriesCollection, Source: object, Rowcol: XlRowCol, SeriesLabels: object, CategoryLabels: object, Replace: object) -> Series """
        ...

    def Extend(self, Source:object, Rowcol:object, CategoryLabels:object) -> object:
        """ Extend(self: SeriesCollection, Source: object, Rowcol: object, CategoryLabels: object) -> object """
        ...

    def Item(self, Index:object) -> Series:
        """ Item(self: SeriesCollection, Index: object) -> Series """
        ...

    def NewSeries(self) -> Series:
        """ NewSeries(self: SeriesCollection) -> Series """
        ...

    def _Default(self, Index:object) -> Series:
        """ _Default(self: SeriesCollection, Index: object) -> Series """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class SeriesLines: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: SeriesLines) -> Application """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: SeriesLines) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: SeriesLines) -> int """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: SeriesLines) -> ChartFormat """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: SeriesLines) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: SeriesLines) -> object """
        ...


    def Delete(self) -> object:
        """ Delete(self: SeriesLines) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: SeriesLines) -> object """
        ...


class SetEffect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: SetEffect) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: SetEffect) -> object """
        ...

    @property
    def Property(self) -> MsoAnimProperty:
        """
        Get: Property(self: SetEffect) -> MsoAnimProperty
        Set: Property(self: SetEffect) = value
        """
        ...

    @property
    def To(self) -> object:
        """
        Get: To(self: SetEffect) -> object
        Set: To(self: SetEffect) = value
        """
        ...



class ShadowFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: ShadowFormat) -> object """
        ...

    @property
    def Blur(self) -> Single:
        """
        Get: Blur(self: ShadowFormat) -> Single
        Set: Blur(self: ShadowFormat) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: ShadowFormat) -> int """
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
    def OffsetX(self) -> Single:
        """
        Get: OffsetX(self: ShadowFormat) -> Single
        Set: OffsetX(self: ShadowFormat) = value
        """
        ...

    @property
    def OffsetY(self) -> Single:
        """
        Get: OffsetY(self: ShadowFormat) -> Single
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
    def Style(self): # -> MsoShadowStyle
        """
        Get: Style(self: ShadowFormat) -> MsoShadowStyle
        Set: Style(self: ShadowFormat) = value
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


    def IncrementOffsetX(self, Increment:Single): # -> 
        """ IncrementOffsetX(self: ShadowFormat, Increment: Single) """
        ...

    def IncrementOffsetY(self, Increment:Single): # -> 
        """ IncrementOffsetY(self: ShadowFormat, Increment: Single) """
        ...


class Shape: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActionSettings(self) -> ActionSettings:
        """ Get: ActionSettings(self: Shape) -> ActionSettings """
        ...

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
    def AnimationSettings(self) -> AnimationSettings:
        """ Get: AnimationSettings(self: Shape) -> AnimationSettings """
        ...

    @property
    def Application(self) -> object:
        """ Get: Application(self: Shape) -> object """
        ...

    @property
    def AutoShapeType(self): # -> MsoAutoShapeType
        """
        Get: AutoShapeType(self: Shape) -> MsoAutoShapeType
        Set: AutoShapeType(self: Shape) = value
        """
        ...

    @property
    def BackgroundStyle(self): # -> MsoBackgroundStyleIndex
        """
        Get: BackgroundStyle(self: Shape) -> MsoBackgroundStyleIndex
        Set: BackgroundStyle(self: Shape) = value
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
    def Callout(self) -> CalloutFormat:
        """ Get: Callout(self: Shape) -> CalloutFormat """
        ...

    @property
    def CanvasItems(self) -> CanvasShapes:
        """ Get: CanvasItems(self: Shape) -> CanvasShapes """
        ...

    @property
    def Chart(self) -> Chart:
        """ Get: Chart(self: Shape) -> Chart """
        ...

    @property
    def Child(self): # -> MsoTriState
        """ Get: Child(self: Shape) -> MsoTriState """
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
    def Creator(self) -> int:
        """ Get: Creator(self: Shape) -> int """
        ...

    @property
    def CustomerData(self) -> CustomerData:
        """ Get: CustomerData(self: Shape) -> CustomerData """
        ...

    @property
    def Diagram(self) -> Diagram:
        """ Get: Diagram(self: Shape) -> Diagram """
        ...

    @property
    def DiagramNode(self) -> DiagramNode:
        """ Get: DiagramNode(self: Shape) -> DiagramNode """
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
    def HasChart(self): # -> MsoTriState
        """ Get: HasChart(self: Shape) -> MsoTriState """
        ...

    @property
    def HasDiagram(self): # -> MsoTriState
        """ Get: HasDiagram(self: Shape) -> MsoTriState """
        ...

    @property
    def HasDiagramNode(self): # -> MsoTriState
        """ Get: HasDiagramNode(self: Shape) -> MsoTriState """
        ...

    @property
    def HasSmartArt(self): # -> MsoTriState
        """ Get: HasSmartArt(self: Shape) -> MsoTriState """
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
    def Height(self) -> Single:
        """
        Get: Height(self: Shape) -> Single
        Set: Height(self: Shape) = value
        """
        ...

    @property
    def HorizontalFlip(self): # -> MsoTriState
        """ Get: HorizontalFlip(self: Shape) -> MsoTriState """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: Shape) -> int """
        ...

    @property
    def Left(self) -> Single:
        """
        Get: Left(self: Shape) -> Single
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
    def MediaFormat(self) -> MediaFormat:
        """ Get: MediaFormat(self: Shape) -> MediaFormat """
        ...

    @property
    def MediaType(self) -> PpMediaType:
        """ Get: MediaType(self: Shape) -> PpMediaType """
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
    def ParentGroup(self) -> Shape:
        """ Get: ParentGroup(self: Shape) -> Shape """
        ...

    @property
    def PictureFormat(self) -> PictureFormat:
        """ Get: PictureFormat(self: Shape) -> PictureFormat """
        ...

    @property
    def PlaceholderFormat(self) -> PlaceholderFormat:
        """ Get: PlaceholderFormat(self: Shape) -> PlaceholderFormat """
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
    def RTF(self): # -> 
        """ Set: RTF(self: Shape) = value """
        ...

    @property
    def Script(self): # -> Script
        """ Get: Script(self: Shape) -> Script """
        ...

    @property
    def Shadow(self) -> ShadowFormat:
        """ Get: Shadow(self: Shape) -> ShadowFormat """
        ...

    @property
    def ShapeStyle(self): # -> MsoShapeStyleIndex
        """
        Get: ShapeStyle(self: Shape) -> MsoShapeStyleIndex
        Set: ShapeStyle(self: Shape) = value
        """
        ...

    @property
    def SmartArt(self): # -> SmartArt
        """ Get: SmartArt(self: Shape) -> SmartArt """
        ...

    @property
    def SoftEdge(self) -> SoftEdgeFormat:
        """ Get: SoftEdge(self: Shape) -> SoftEdgeFormat """
        ...

    @property
    def SoundFormat(self) -> SoundFormat:
        """ Get: SoundFormat(self: Shape) -> SoundFormat """
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
    def TextFrame2(self) -> TextFrame2:
        """ Get: TextFrame2(self: Shape) -> TextFrame2 """
        ...

    @property
    def ThreeD(self) -> ThreeDFormat:
        """ Get: ThreeD(self: Shape) -> ThreeDFormat """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: Shape) -> str
        Set: Title(self: Shape) = value
        """
        ...

    @property
    def Top(self) -> Single:
        """
        Get: Top(self: Shape) -> Single
        Set: Top(self: Shape) = value
        """
        ...

    @property
    def Type(self): # -> MsoShapeType
        """ Get: Type(self: Shape) -> MsoShapeType """
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
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: Shape) -> MsoTriState
        Set: Visible(self: Shape) = value
        """
        ...

    @property
    def Width(self) -> Single:
        """
        Get: Width(self: Shape) -> Single
        Set: Width(self: Shape) = value
        """
        ...

    @property
    def ZOrderPosition(self) -> int:
        """ Get: ZOrderPosition(self: Shape) -> int """
        ...


    def Apply(self): # -> 
        """ Apply(self: Shape) """
        ...

    def ApplyAnimation(self): # -> 
        """ ApplyAnimation(self: Shape) """
        ...

    def CanvasCropBottom(self, Increment:Single): # -> 
        """ CanvasCropBottom(self: Shape, Increment: Single) """
        ...

    def CanvasCropLeft(self, Increment:Single): # -> 
        """ CanvasCropLeft(self: Shape, Increment: Single) """
        ...

    def CanvasCropRight(self, Increment:Single): # -> 
        """ CanvasCropRight(self: Shape, Increment: Single) """
        ...

    def CanvasCropTop(self, Increment:Single): # -> 
        """ CanvasCropTop(self: Shape, Increment: Single) """
        ...

    def ConvertTextToSmartArt(self, Layout): # ->  # Not found arg types: {'Layout': 'SmartArtLayout'}
        """ ConvertTextToSmartArt(self: Shape, Layout: SmartArtLayout) """
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

    def Duplicate(self) -> ShapeRange:
        """ Duplicate(self: Shape) -> ShapeRange """
        ...

    def Export(self, PathName:str, Filter:PpShapeFormat, ScaleWidth:int, ScaleHeight:int, ExportMode:PpExportMode): # -> 
        """ Export(self: Shape, PathName: str, Filter: PpShapeFormat, ScaleWidth: int, ScaleHeight: int, ExportMode: PpExportMode) """
        ...

    def Flip(self, FlipCmd): # ->  # Not found arg types: {'FlipCmd': 'MsoFlipCmd'}
        """ Flip(self: Shape, FlipCmd: MsoFlipCmd) """
        ...

    def IncrementLeft(self, Increment:Single): # -> 
        """ IncrementLeft(self: Shape, Increment: Single) """
        ...

    def IncrementRotation(self, Increment:Single): # -> 
        """ IncrementRotation(self: Shape, Increment: Single) """
        ...

    def IncrementTop(self, Increment:Single): # -> 
        """ IncrementTop(self: Shape, Increment: Single) """
        ...

    def PickUp(self): # -> 
        """ PickUp(self: Shape) """
        ...

    def PickupAnimation(self): # -> 
        """ PickupAnimation(self: Shape) """
        ...

    def RerouteConnections(self): # -> 
        """ RerouteConnections(self: Shape) """
        ...

    def ScaleHeight(self, Factor:Single, RelativeToOriginalSize, fScale): # ->  # Not found arg types: {'RelativeToOriginalSize': 'MsoTriState', 'fScale': 'MsoScaleFrom'}
        """ ScaleHeight(self: Shape, Factor: Single, RelativeToOriginalSize: MsoTriState, fScale: MsoScaleFrom) """
        ...

    def ScaleWidth(self, Factor:Single, RelativeToOriginalSize, fScale): # ->  # Not found arg types: {'RelativeToOriginalSize': 'MsoTriState', 'fScale': 'MsoScaleFrom'}
        """ ScaleWidth(self: Shape, Factor: Single, RelativeToOriginalSize: MsoTriState, fScale: MsoScaleFrom) """
        ...

    def Select(self, Replace): # ->  # Not found arg types: {'Replace': 'MsoTriState'}
        """ Select(self: Shape, Replace: MsoTriState) """
        ...

    def SetShapesDefaultProperties(self): # -> 
        """ SetShapesDefaultProperties(self: Shape) """
        ...

    def Ungroup(self) -> ShapeRange:
        """ Ungroup(self: Shape) -> ShapeRange """
        ...

    def UpgradeMedia(self): # -> 
        """ UpgradeMedia(self: Shape) """
        ...

    def ZOrder(self, ZOrderCmd): # ->  # Not found arg types: {'ZOrderCmd': 'MsoZOrderCmd'}
        """ ZOrder(self: Shape, ZOrderCmd: MsoZOrderCmd) """
        ...


class ShapeNode: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: ShapeNode) -> object """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: ShapeNode) -> int """
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
    def Application(self) -> object:
        """ Get: Application(self: ShapeNodes) -> object """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ShapeNodes) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: ShapeNodes) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ShapeNodes) -> object """
        ...


    def Delete(self, Index:int): # -> 
        """ Delete(self: ShapeNodes, Index: int) """
        ...

    def Insert(self, Index:int, SegmentType, EditingType, X1:Single, Y1:Single, X2:Single, Y2:Single, X3:Single, Y3:Single): # ->  # Not found arg types: {'EditingType': 'MsoEditingType', 'SegmentType': 'MsoSegmentType'}
        """ Insert(self: ShapeNodes, Index: int, SegmentType: MsoSegmentType, EditingType: MsoEditingType, X1: Single, Y1: Single, X2: Single, Y2: Single, X3: Single, Y3: Single) """
        ...

    def SetEditingType(self, Index:int, EditingType): # ->  # Not found arg types: {'EditingType': 'MsoEditingType'}
        """ SetEditingType(self: ShapeNodes, Index: int, EditingType: MsoEditingType) """
        ...

    def SetPosition(self, Index:int, X1:Single, Y1:Single): # -> 
        """ SetPosition(self: ShapeNodes, Index: int, X1: Single, Y1: Single) """
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
    def ActionSettings(self) -> ActionSettings:
        """ Get: ActionSettings(self: ShapeRange) -> ActionSettings """
        ...

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
    def AnimationSettings(self) -> AnimationSettings:
        """ Get: AnimationSettings(self: ShapeRange) -> AnimationSettings """
        ...

    @property
    def Application(self) -> object:
        """ Get: Application(self: ShapeRange) -> object """
        ...

    @property
    def AutoShapeType(self): # -> MsoAutoShapeType
        """
        Get: AutoShapeType(self: ShapeRange) -> MsoAutoShapeType
        Set: AutoShapeType(self: ShapeRange) = value
        """
        ...

    @property
    def BackgroundStyle(self): # -> MsoBackgroundStyleIndex
        """
        Get: BackgroundStyle(self: ShapeRange) -> MsoBackgroundStyleIndex
        Set: BackgroundStyle(self: ShapeRange) = value
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
    def CanvasItems(self) -> CanvasShapes:
        """ Get: CanvasItems(self: ShapeRange) -> CanvasShapes """
        ...

    @property
    def Chart(self) -> Chart:
        """ Get: Chart(self: ShapeRange) -> Chart """
        ...

    @property
    def Child(self): # -> MsoTriState
        """ Get: Child(self: ShapeRange) -> MsoTriState """
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
    def Creator(self) -> int:
        """ Get: Creator(self: ShapeRange) -> int """
        ...

    @property
    def CustomerData(self) -> CustomerData:
        """ Get: CustomerData(self: ShapeRange) -> CustomerData """
        ...

    @property
    def Diagram(self) -> Diagram:
        """ Get: Diagram(self: ShapeRange) -> Diagram """
        ...

    @property
    def DiagramNode(self) -> DiagramNode:
        """ Get: DiagramNode(self: ShapeRange) -> DiagramNode """
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
    def HasChart(self): # -> MsoTriState
        """ Get: HasChart(self: ShapeRange) -> MsoTriState """
        ...

    @property
    def HasDiagram(self): # -> MsoTriState
        """ Get: HasDiagram(self: ShapeRange) -> MsoTriState """
        ...

    @property
    def HasDiagramNode(self): # -> MsoTriState
        """ Get: HasDiagramNode(self: ShapeRange) -> MsoTriState """
        ...

    @property
    def HasSmartArt(self): # -> MsoTriState
        """ Get: HasSmartArt(self: ShapeRange) -> MsoTriState """
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
    def Height(self) -> Single:
        """
        Get: Height(self: ShapeRange) -> Single
        Set: Height(self: ShapeRange) = value
        """
        ...

    @property
    def HorizontalFlip(self): # -> MsoTriState
        """ Get: HorizontalFlip(self: ShapeRange) -> MsoTriState """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: ShapeRange) -> int """
        ...

    @property
    def Left(self) -> Single:
        """
        Get: Left(self: ShapeRange) -> Single
        Set: Left(self: ShapeRange) = value
        """
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
    def MediaFormat(self) -> MediaFormat:
        """ Get: MediaFormat(self: ShapeRange) -> MediaFormat """
        ...

    @property
    def MediaType(self) -> PpMediaType:
        """ Get: MediaType(self: ShapeRange) -> PpMediaType """
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
    def ParentGroup(self) -> Shape:
        """ Get: ParentGroup(self: ShapeRange) -> Shape """
        ...

    @property
    def PictureFormat(self) -> PictureFormat:
        """ Get: PictureFormat(self: ShapeRange) -> PictureFormat """
        ...

    @property
    def PlaceholderFormat(self) -> PlaceholderFormat:
        """ Get: PlaceholderFormat(self: ShapeRange) -> PlaceholderFormat """
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
    def RTF(self): # -> 
        """ Set: RTF(self: ShapeRange) = value """
        ...

    @property
    def Script(self): # -> Script
        """ Get: Script(self: ShapeRange) -> Script """
        ...

    @property
    def Shadow(self) -> ShadowFormat:
        """ Get: Shadow(self: ShapeRange) -> ShadowFormat """
        ...

    @property
    def ShapeStyle(self): # -> MsoShapeStyleIndex
        """
        Get: ShapeStyle(self: ShapeRange) -> MsoShapeStyleIndex
        Set: ShapeStyle(self: ShapeRange) = value
        """
        ...

    @property
    def SmartArt(self): # -> SmartArt
        """ Get: SmartArt(self: ShapeRange) -> SmartArt """
        ...

    @property
    def SoftEdge(self) -> SoftEdgeFormat:
        """ Get: SoftEdge(self: ShapeRange) -> SoftEdgeFormat """
        ...

    @property
    def SoundFormat(self) -> SoundFormat:
        """ Get: SoundFormat(self: ShapeRange) -> SoundFormat """
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
    def TextFrame2(self) -> TextFrame2:
        """ Get: TextFrame2(self: ShapeRange) -> TextFrame2 """
        ...

    @property
    def ThreeD(self) -> ThreeDFormat:
        """ Get: ThreeD(self: ShapeRange) -> ThreeDFormat """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: ShapeRange) -> str
        Set: Title(self: ShapeRange) = value
        """
        ...

    @property
    def Top(self) -> Single:
        """
        Get: Top(self: ShapeRange) -> Single
        Set: Top(self: ShapeRange) = value
        """
        ...

    @property
    def Type(self): # -> MsoShapeType
        """ Get: Type(self: ShapeRange) -> MsoShapeType """
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
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: ShapeRange) -> MsoTriState
        Set: Visible(self: ShapeRange) = value
        """
        ...

    @property
    def Width(self) -> Single:
        """
        Get: Width(self: ShapeRange) -> Single
        Set: Width(self: ShapeRange) = value
        """
        ...

    @property
    def ZOrderPosition(self) -> int:
        """ Get: ZOrderPosition(self: ShapeRange) -> int """
        ...


    def Align(self, AlignCmd, RelativeTo): # ->  # Not found arg types: {'RelativeTo': 'MsoTriState', 'AlignCmd': 'MsoAlignCmd'}
        """ Align(self: ShapeRange, AlignCmd: MsoAlignCmd, RelativeTo: MsoTriState) """
        ...

    def Apply(self): # -> 
        """ Apply(self: ShapeRange) """
        ...

    def ApplyAnimation(self): # -> 
        """ ApplyAnimation(self: ShapeRange) """
        ...

    def CanvasCropBottom(self, Increment:Single): # -> 
        """ CanvasCropBottom(self: ShapeRange, Increment: Single) """
        ...

    def CanvasCropLeft(self, Increment:Single): # -> 
        """ CanvasCropLeft(self: ShapeRange, Increment: Single) """
        ...

    def CanvasCropRight(self, Increment:Single): # -> 
        """ CanvasCropRight(self: ShapeRange, Increment: Single) """
        ...

    def CanvasCropTop(self, Increment:Single): # -> 
        """ CanvasCropTop(self: ShapeRange, Increment: Single) """
        ...

    def ConvertTextToSmartArt(self, Layout): # ->  # Not found arg types: {'Layout': 'SmartArtLayout'}
        """ ConvertTextToSmartArt(self: ShapeRange, Layout: SmartArtLayout) """
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

    def Export(self, PathName:str, Filter:PpShapeFormat, ScaleWidth:int, ScaleHeight:int, ExportMode:PpExportMode): # -> 
        """ Export(self: ShapeRange, PathName: str, Filter: PpShapeFormat, ScaleWidth: int, ScaleHeight: int, ExportMode: PpExportMode) """
        ...

    def Flip(self, FlipCmd): # ->  # Not found arg types: {'FlipCmd': 'MsoFlipCmd'}
        """ Flip(self: ShapeRange, FlipCmd: MsoFlipCmd) """
        ...

    def GetPolygonalRepresentation(self, maxPointsInBuffer, pPoints, numPointsInPolygon, IsOpen): # -> Tuple_[Single, UInt32, MsoTriState]
        """ GetPolygonalRepresentation(self: ShapeRange, maxPointsInBuffer: UInt32, pPoints: Single) -> (Single, UInt32, MsoTriState) """
        ...

    def Group(self) -> Shape:
        """ Group(self: ShapeRange) -> Shape """
        ...

    def IncrementLeft(self, Increment:Single): # -> 
        """ IncrementLeft(self: ShapeRange, Increment: Single) """
        ...

    def IncrementRotation(self, Increment:Single): # -> 
        """ IncrementRotation(self: ShapeRange, Increment: Single) """
        ...

    def IncrementTop(self, Increment:Single): # -> 
        """ IncrementTop(self: ShapeRange, Increment: Single) """
        ...

    def MergeShapes(self, MergeCmd, PrimaryShape:Shape): # ->  # Not found arg types: {'MergeCmd': 'MsoMergeCmd'}
        """ MergeShapes(self: ShapeRange, MergeCmd: MsoMergeCmd, PrimaryShape: Shape) """
        ...

    def PickUp(self): # -> 
        """ PickUp(self: ShapeRange) """
        ...

    def PickupAnimation(self): # -> 
        """ PickupAnimation(self: ShapeRange) """
        ...

    def Regroup(self) -> Shape:
        """ Regroup(self: ShapeRange) -> Shape """
        ...

    def RerouteConnections(self): # -> 
        """ RerouteConnections(self: ShapeRange) """
        ...

    def ScaleHeight(self, Factor:Single, RelativeToOriginalSize, fScale): # ->  # Not found arg types: {'RelativeToOriginalSize': 'MsoTriState', 'fScale': 'MsoScaleFrom'}
        """ ScaleHeight(self: ShapeRange, Factor: Single, RelativeToOriginalSize: MsoTriState, fScale: MsoScaleFrom) """
        ...

    def ScaleWidth(self, Factor:Single, RelativeToOriginalSize, fScale): # ->  # Not found arg types: {'RelativeToOriginalSize': 'MsoTriState', 'fScale': 'MsoScaleFrom'}
        """ ScaleWidth(self: ShapeRange, Factor: Single, RelativeToOriginalSize: MsoTriState, fScale: MsoScaleFrom) """
        ...

    def Select(self, Replace): # ->  # Not found arg types: {'Replace': 'MsoTriState'}
        """ Select(self: ShapeRange, Replace: MsoTriState) """
        ...

    def SetShapesDefaultProperties(self): # -> 
        """ SetShapesDefaultProperties(self: ShapeRange) """
        ...

    def Ungroup(self) -> ShapeRange:
        """ Ungroup(self: ShapeRange) -> ShapeRange """
        ...

    def UpgradeMedia(self): # -> 
        """ UpgradeMedia(self: ShapeRange) """
        ...

    def ZOrder(self, ZOrderCmd): # ->  # Not found arg types: {'ZOrderCmd': 'MsoZOrderCmd'}
        """ ZOrder(self: ShapeRange, ZOrderCmd: MsoZOrderCmd) """
        ...

    def _Index(self, Index:int) -> object:
        """ _Index(self: ShapeRange, Index: int) -> object """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Shapes(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: Shapes) -> object """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Shapes) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Shapes) -> int """
        ...

    @property
    def HasTitle(self): # -> MsoTriState
        """ Get: HasTitle(self: Shapes) -> MsoTriState """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Shapes) -> object """
        ...

    @property
    def Placeholders(self) -> Placeholders:
        """ Get: Placeholders(self: Shapes) -> Placeholders """
        ...

    @property
    def Title(self) -> Shape:
        """ Get: Title(self: Shapes) -> Shape """
        ...


    def AddCallout(self, Type, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape: # Not found arg types: {'Type': 'MsoCalloutType'}
        """ AddCallout(self: Shapes, Type: MsoCalloutType, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddCanvas(self, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape:
        """ AddCanvas(self: Shapes, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddChart(self, Type:XlChartType, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape:
        """ AddChart(self: Shapes, Type: XlChartType, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddChart2(self, Style:int, Type:XlChartType, Left:Single, Top:Single, Width:Single, Height:Single, NewLayout:bool) -> Shape:
        """ AddChart2(self: Shapes, Style: int, Type: XlChartType, Left: Single, Top: Single, Width: Single, Height: Single, NewLayout: bool) -> Shape """
        ...

    def AddComment(self, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape:
        """ AddComment(self: Shapes, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddConnector(self, Type, BeginX:Single, BeginY:Single, EndX:Single, EndY:Single) -> Shape: # Not found arg types: {'Type': 'MsoConnectorType'}
        """ AddConnector(self: Shapes, Type: MsoConnectorType, BeginX: Single, BeginY: Single, EndX: Single, EndY: Single) -> Shape """
        ...

    def AddCurve(self, SafeArrayOfPoints:object) -> Shape:
        """ AddCurve(self: Shapes, SafeArrayOfPoints: object) -> Shape """
        ...

    def AddDiagram(self, Type, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape: # Not found arg types: {'Type': 'MsoDiagramType'}
        """ AddDiagram(self: Shapes, Type: MsoDiagramType, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddLabel(self, Orientation, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape: # Not found arg types: {'Orientation': 'MsoTextOrientation'}
        """ AddLabel(self: Shapes, Orientation: MsoTextOrientation, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddLine(self, BeginX:Single, BeginY:Single, EndX:Single, EndY:Single) -> Shape:
        """ AddLine(self: Shapes, BeginX: Single, BeginY: Single, EndX: Single, EndY: Single) -> Shape """
        ...

    def AddMediaObject(self, FileName:str, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape:
        """ AddMediaObject(self: Shapes, FileName: str, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddMediaObject2(self, FileName:str, LinkToFile, SaveWithDocument, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape: # Not found arg types: {'LinkToFile': 'MsoTriState', 'SaveWithDocument': 'MsoTriState'}
        """ AddMediaObject2(self: Shapes, FileName: str, LinkToFile: MsoTriState, SaveWithDocument: MsoTriState, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddMediaObjectFromEmbedTag(self, EmbedTag:str, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape:
        """ AddMediaObjectFromEmbedTag(self: Shapes, EmbedTag: str, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddOLEObject(self, Left:Single, Top:Single, Width:Single, Height:Single, ClassName:str, FileName:str, DisplayAsIcon, IconFileName:str, IconIndex:int, IconLabel:str, Link) -> Shape: # Not found arg types: {'DisplayAsIcon': 'MsoTriState', 'Link': 'MsoTriState'}
        """ AddOLEObject(self: Shapes, Left: Single, Top: Single, Width: Single, Height: Single, ClassName: str, FileName: str, DisplayAsIcon: MsoTriState, IconFileName: str, IconIndex: int, IconLabel: str, Link: MsoTriState) -> Shape """
        ...

    def AddPicture(self, FileName:str, LinkToFile, SaveWithDocument, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape: # Not found arg types: {'LinkToFile': 'MsoTriState', 'SaveWithDocument': 'MsoTriState'}
        """ AddPicture(self: Shapes, FileName: str, LinkToFile: MsoTriState, SaveWithDocument: MsoTriState, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddPicture2(self, FileName:str, LinkToFile, SaveWithDocument, Left:Single, Top:Single, Width:Single, Height:Single, compress) -> Shape: # Not found arg types: {'compress': 'MsoPictureCompress', 'LinkToFile': 'MsoTriState', 'SaveWithDocument': 'MsoTriState'}
        """ AddPicture2(self: Shapes, FileName: str, LinkToFile: MsoTriState, SaveWithDocument: MsoTriState, Left: Single, Top: Single, Width: Single, Height: Single, compress: MsoPictureCompress) -> Shape """
        ...

    def AddPlaceholder(self, Type:PpPlaceholderType, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape:
        """ AddPlaceholder(self: Shapes, Type: PpPlaceholderType, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddPolyline(self, SafeArrayOfPoints:object) -> Shape:
        """ AddPolyline(self: Shapes, SafeArrayOfPoints: object) -> Shape """
        ...

    def AddShape(self, Type, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape: # Not found arg types: {'Type': 'MsoAutoShapeType'}
        """ AddShape(self: Shapes, Type: MsoAutoShapeType, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddSmartArt(self, Layout, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape: # Not found arg types: {'Layout': 'SmartArtLayout'}
        """ AddSmartArt(self: Shapes, Layout: SmartArtLayout, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddTable(self, NumRows:int, NumColumns:int, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape:
        """ AddTable(self: Shapes, NumRows: int, NumColumns: int, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddTextbox(self, Orientation, Left:Single, Top:Single, Width:Single, Height:Single) -> Shape: # Not found arg types: {'Orientation': 'MsoTextOrientation'}
        """ AddTextbox(self: Shapes, Orientation: MsoTextOrientation, Left: Single, Top: Single, Width: Single, Height: Single) -> Shape """
        ...

    def AddTextEffect(self, PresetTextEffect, Text:str, FontName:str, FontSize:Single, FontBold, FontItalic, Left:Single, Top:Single) -> Shape: # Not found arg types: {'FontItalic': 'MsoTriState', 'FontBold': 'MsoTriState', 'PresetTextEffect': 'MsoPresetTextEffect'}
        """ AddTextEffect(self: Shapes, PresetTextEffect: MsoPresetTextEffect, Text: str, FontName: str, FontSize: Single, FontBold: MsoTriState, FontItalic: MsoTriState, Left: Single, Top: Single) -> Shape """
        ...

    def AddTitle(self) -> Shape:
        """ AddTitle(self: Shapes) -> Shape """
        ...

    def BuildFreeform(self, EditingType, X1:Single, Y1:Single) -> FreeformBuilder: # Not found arg types: {'EditingType': 'MsoEditingType'}
        """ BuildFreeform(self: Shapes, EditingType: MsoEditingType, X1: Single, Y1: Single) -> FreeformBuilder """
        ...

    def Paste(self) -> ShapeRange:
        """ Paste(self: Shapes) -> ShapeRange """
        ...

    def PasteSpecial(self, DataType:PpPasteDataType, DisplayAsIcon, IconFileName:str, IconIndex:int, IconLabel:str, Link) -> ShapeRange: # Not found arg types: {'DisplayAsIcon': 'MsoTriState', 'Link': 'MsoTriState'}
        """ PasteSpecial(self: Shapes, DataType: PpPasteDataType, DisplayAsIcon: MsoTriState, IconFileName: str, IconIndex: int, IconLabel: str, Link: MsoTriState) -> ShapeRange """
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


class SldEvents: # skipped bases: <type 'object'>
    """ no doc """
    pass

class SldEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    pass

class SldEvents_SinkHelper(SldEvents): # skipped bases: <type 'object'>
    """ no doc """
    m_dwCookie = ...


class _Slide: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: _Slide) -> Application """
        ...

    @property
    def Background(self) -> ShapeRange:
        """ Get: Background(self: _Slide) -> ShapeRange """
        ...

    @property
    def BackgroundStyle(self): # -> MsoBackgroundStyleIndex
        """
        Get: BackgroundStyle(self: _Slide) -> MsoBackgroundStyleIndex
        Set: BackgroundStyle(self: _Slide) = value
        """
        ...

    @property
    def ColorScheme(self) -> ColorScheme:
        """
        Get: ColorScheme(self: _Slide) -> ColorScheme
        Set: ColorScheme(self: _Slide) = value
        """
        ...

    @property
    def Comments(self) -> Comments:
        """ Get: Comments(self: _Slide) -> Comments """
        ...

    @property
    def CustomerData(self) -> CustomerData:
        """ Get: CustomerData(self: _Slide) -> CustomerData """
        ...

    @property
    def CustomLayout(self) -> CustomLayout:
        """
        Get: CustomLayout(self: _Slide) -> CustomLayout
        Set: CustomLayout(self: _Slide) = value
        """
        ...

    @property
    def Design(self) -> Design:
        """
        Get: Design(self: _Slide) -> Design
        Set: Design(self: _Slide) = value
        """
        ...

    @property
    def DisplayMasterShapes(self): # -> MsoTriState
        """
        Get: DisplayMasterShapes(self: _Slide) -> MsoTriState
        Set: DisplayMasterShapes(self: _Slide) = value
        """
        ...

    @property
    def FollowMasterBackground(self): # -> MsoTriState
        """
        Get: FollowMasterBackground(self: _Slide) -> MsoTriState
        Set: FollowMasterBackground(self: _Slide) = value
        """
        ...

    @property
    def HasNotesPage(self): # -> MsoTriState
        """ Get: HasNotesPage(self: _Slide) -> MsoTriState """
        ...

    @property
    def HeadersFooters(self) -> HeadersFooters:
        """ Get: HeadersFooters(self: _Slide) -> HeadersFooters """
        ...

    @property
    def Hyperlinks(self) -> Hyperlinks:
        """ Get: Hyperlinks(self: _Slide) -> Hyperlinks """
        ...

    @property
    def Layout(self) -> PpSlideLayout:
        """
        Get: Layout(self: _Slide) -> PpSlideLayout
        Set: Layout(self: _Slide) = value
        """
        ...

    @property
    def Master(self) -> Master:
        """ Get: Master(self: _Slide) -> Master """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: _Slide) -> str
        Set: Name(self: _Slide) = value
        """
        ...

    @property
    def NotesPage(self) -> SlideRange:
        """ Get: NotesPage(self: _Slide) -> SlideRange """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: _Slide) -> object """
        ...

    @property
    def PrintSteps(self) -> int:
        """ Get: PrintSteps(self: _Slide) -> int """
        ...

    @property
    def Scripts(self): # -> Scripts
        """ Get: Scripts(self: _Slide) -> Scripts """
        ...

    @property
    def sectionIndex(self) -> int:
        """ Get: sectionIndex(self: _Slide) -> int """
        ...

    @property
    def SectionNumber(self) -> int:
        """ Get: SectionNumber(self: _Slide) -> int """
        ...

    @property
    def Shapes(self) -> Shapes:
        """ Get: Shapes(self: _Slide) -> Shapes """
        ...

    @property
    def SlideID(self) -> int:
        """ Get: SlideID(self: _Slide) -> int """
        ...

    @property
    def SlideIndex(self) -> int:
        """ Get: SlideIndex(self: _Slide) -> int """
        ...

    @property
    def SlideNumber(self) -> int:
        """ Get: SlideNumber(self: _Slide) -> int """
        ...

    @property
    def SlideShowTransition(self) -> SlideShowTransition:
        """ Get: SlideShowTransition(self: _Slide) -> SlideShowTransition """
        ...

    @property
    def Tags(self) -> Tags:
        """ Get: Tags(self: _Slide) -> Tags """
        ...

    @property
    def ThemeColorScheme(self): # -> ThemeColorScheme
        """ Get: ThemeColorScheme(self: _Slide) -> ThemeColorScheme """
        ...

    @property
    def TimeLine(self) -> TimeLine:
        """ Get: TimeLine(self: _Slide) -> TimeLine """
        ...


    def ApplyTemplate(self, FileName:str): # -> 
        """ ApplyTemplate(self: _Slide, FileName: str) """
        ...

    def ApplyTemplate2(self, FileName:str, VariantGUID:str): # -> 
        """ ApplyTemplate2(self: _Slide, FileName: str, VariantGUID: str) """
        ...

    def ApplyTheme(self, themeName:str): # -> 
        """ ApplyTheme(self: _Slide, themeName: str) """
        ...

    def ApplyThemeColorScheme(self, themeColorSchemeName:str): # -> 
        """ ApplyThemeColorScheme(self: _Slide, themeColorSchemeName: str) """
        ...

    def Copy(self): # -> 
        """ Copy(self: _Slide) """
        ...

    def Cut(self): # -> 
        """ Cut(self: _Slide) """
        ...

    def Delete(self): # -> 
        """ Delete(self: _Slide) """
        ...

    def Duplicate(self) -> SlideRange:
        """ Duplicate(self: _Slide) -> SlideRange """
        ...

    def Export(self, FileName:str, FilterName:str, ScaleWidth:int, ScaleHeight:int): # -> 
        """ Export(self: _Slide, FileName: str, FilterName: str, ScaleWidth: int, ScaleHeight: int) """
        ...

    def MoveTo(self, toPos:int): # -> 
        """ MoveTo(self: _Slide, toPos: int) """
        ...

    def MoveToSectionStart(self, toSection:int): # -> 
        """ MoveToSectionStart(self: _Slide, toSection: int) """
        ...

    def PublishSlides(self, SlideLibraryUrl:str, Overwrite:bool, UseSlideOrder:bool): # -> 
        """ PublishSlides(self: _Slide, SlideLibraryUrl: str, Overwrite: bool, UseSlideOrder: bool) """
        ...

    def Select(self): # -> 
        """ Select(self: _Slide) """
        ...


class Slide(_Slide, SldEvents_Event): # skipped bases: <type 'object'>
    """ no doc """
    pass

class SlideClass(Slide, __ComObject): # skipped bases: <type 'SldEvents_Event'>, <type '_Slide'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: SlideClass) -> Application """
        ...

    @property
    def Background(self) -> ShapeRange:
        """ Get: Background(self: SlideClass) -> ShapeRange """
        ...

    @property
    def BackgroundStyle(self): # -> MsoBackgroundStyleIndex
        """
        Get: BackgroundStyle(self: SlideClass) -> MsoBackgroundStyleIndex
        Set: BackgroundStyle(self: SlideClass) = value
        """
        ...

    @property
    def ColorScheme(self) -> ColorScheme:
        """
        Get: ColorScheme(self: SlideClass) -> ColorScheme
        Set: ColorScheme(self: SlideClass) = value
        """
        ...

    @property
    def Comments(self) -> Comments:
        """ Get: Comments(self: SlideClass) -> Comments """
        ...

    @property
    def CustomerData(self) -> CustomerData:
        """ Get: CustomerData(self: SlideClass) -> CustomerData """
        ...

    @property
    def CustomLayout(self) -> CustomLayout:
        """
        Get: CustomLayout(self: SlideClass) -> CustomLayout
        Set: CustomLayout(self: SlideClass) = value
        """
        ...

    @property
    def Design(self) -> Design:
        """
        Get: Design(self: SlideClass) -> Design
        Set: Design(self: SlideClass) = value
        """
        ...

    @property
    def DisplayMasterShapes(self): # -> MsoTriState
        """
        Get: DisplayMasterShapes(self: SlideClass) -> MsoTriState
        Set: DisplayMasterShapes(self: SlideClass) = value
        """
        ...

    @property
    def FollowMasterBackground(self): # -> MsoTriState
        """
        Get: FollowMasterBackground(self: SlideClass) -> MsoTriState
        Set: FollowMasterBackground(self: SlideClass) = value
        """
        ...

    @property
    def HasNotesPage(self): # -> MsoTriState
        """ Get: HasNotesPage(self: SlideClass) -> MsoTriState """
        ...

    @property
    def HeadersFooters(self) -> HeadersFooters:
        """ Get: HeadersFooters(self: SlideClass) -> HeadersFooters """
        ...

    @property
    def Hyperlinks(self) -> Hyperlinks:
        """ Get: Hyperlinks(self: SlideClass) -> Hyperlinks """
        ...

    @property
    def Layout(self) -> PpSlideLayout:
        """
        Get: Layout(self: SlideClass) -> PpSlideLayout
        Set: Layout(self: SlideClass) = value
        """
        ...

    @property
    def Master(self) -> Master:
        """ Get: Master(self: SlideClass) -> Master """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SlideClass) -> str
        Set: Name(self: SlideClass) = value
        """
        ...

    @property
    def NotesPage(self) -> SlideRange:
        """ Get: NotesPage(self: SlideClass) -> SlideRange """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: SlideClass) -> object """
        ...

    @property
    def PrintSteps(self) -> int:
        """ Get: PrintSteps(self: SlideClass) -> int """
        ...

    @property
    def Scripts(self): # -> Scripts
        """ Get: Scripts(self: SlideClass) -> Scripts """
        ...

    @property
    def sectionIndex(self) -> int:
        """ Get: sectionIndex(self: SlideClass) -> int """
        ...

    @property
    def SectionNumber(self) -> int:
        """ Get: SectionNumber(self: SlideClass) -> int """
        ...

    @property
    def Shapes(self) -> Shapes:
        """ Get: Shapes(self: SlideClass) -> Shapes """
        ...

    @property
    def SlideID(self) -> int:
        """ Get: SlideID(self: SlideClass) -> int """
        ...

    @property
    def SlideIndex(self) -> int:
        """ Get: SlideIndex(self: SlideClass) -> int """
        ...

    @property
    def SlideNumber(self) -> int:
        """ Get: SlideNumber(self: SlideClass) -> int """
        ...

    @property
    def SlideShowTransition(self) -> SlideShowTransition:
        """ Get: SlideShowTransition(self: SlideClass) -> SlideShowTransition """
        ...

    @property
    def Tags(self) -> Tags:
        """ Get: Tags(self: SlideClass) -> Tags """
        ...

    @property
    def ThemeColorScheme(self): # -> ThemeColorScheme
        """ Get: ThemeColorScheme(self: SlideClass) -> ThemeColorScheme """
        ...

    @property
    def TimeLine(self) -> TimeLine:
        """ Get: TimeLine(self: SlideClass) -> TimeLine """
        ...


    def ApplyTemplate(self, FileName:str): # -> 
        """ ApplyTemplate(self: SlideClass, FileName: str) """
        ...

    def ApplyTemplate2(self, FileName:str, VariantGUID:str): # -> 
        """ ApplyTemplate2(self: SlideClass, FileName: str, VariantGUID: str) """
        ...

    def ApplyTheme(self, themeName:str): # -> 
        """ ApplyTheme(self: SlideClass, themeName: str) """
        ...

    def ApplyThemeColorScheme(self, themeColorSchemeName:str): # -> 
        """ ApplyThemeColorScheme(self: SlideClass, themeColorSchemeName: str) """
        ...

    def Copy(self): # -> 
        """ Copy(self: SlideClass) """
        ...

    def Cut(self): # -> 
        """ Cut(self: SlideClass) """
        ...

    def Delete(self): # -> 
        """ Delete(self: SlideClass) """
        ...

    def Duplicate(self) -> SlideRange:
        """ Duplicate(self: SlideClass) -> SlideRange """
        ...

    def Export(self, FileName:str, FilterName:str, ScaleWidth:int, ScaleHeight:int): # -> 
        """ Export(self: SlideClass, FileName: str, FilterName: str, ScaleWidth: int, ScaleHeight: int) """
        ...

    def MoveTo(self, toPos:int): # -> 
        """ MoveTo(self: SlideClass, toPos: int) """
        ...

    def MoveToSectionStart(self, toSection:int): # -> 
        """ MoveToSectionStart(self: SlideClass, toSection: int) """
        ...

    def PublishSlides(self, SlideLibraryUrl:str, Overwrite:bool, UseSlideOrder:bool): # -> 
        """ PublishSlides(self: SlideClass, SlideLibraryUrl: str, Overwrite: bool, UseSlideOrder: bool) """
        ...

    def Select(self): # -> 
        """ Select(self: SlideClass) """
        ...


class SlideNavigation: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: SlideNavigation) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: SlideNavigation) -> object """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: SlideNavigation) -> bool
        Set: Visible(self: SlideNavigation) = value
        """
        ...



class SlideRange(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: SlideRange) -> Application """
        ...

    @property
    def Background(self) -> ShapeRange:
        """ Get: Background(self: SlideRange) -> ShapeRange """
        ...

    @property
    def BackgroundStyle(self): # -> MsoBackgroundStyleIndex
        """
        Get: BackgroundStyle(self: SlideRange) -> MsoBackgroundStyleIndex
        Set: BackgroundStyle(self: SlideRange) = value
        """
        ...

    @property
    def ColorScheme(self) -> ColorScheme:
        """
        Get: ColorScheme(self: SlideRange) -> ColorScheme
        Set: ColorScheme(self: SlideRange) = value
        """
        ...

    @property
    def Comments(self) -> Comments:
        """ Get: Comments(self: SlideRange) -> Comments """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: SlideRange) -> int """
        ...

    @property
    def CustomerData(self) -> CustomerData:
        """ Get: CustomerData(self: SlideRange) -> CustomerData """
        ...

    @property
    def CustomLayout(self) -> CustomLayout:
        """
        Get: CustomLayout(self: SlideRange) -> CustomLayout
        Set: CustomLayout(self: SlideRange) = value
        """
        ...

    @property
    def Design(self) -> Design:
        """
        Get: Design(self: SlideRange) -> Design
        Set: Design(self: SlideRange) = value
        """
        ...

    @property
    def DisplayMasterShapes(self): # -> MsoTriState
        """
        Get: DisplayMasterShapes(self: SlideRange) -> MsoTriState
        Set: DisplayMasterShapes(self: SlideRange) = value
        """
        ...

    @property
    def FollowMasterBackground(self): # -> MsoTriState
        """
        Get: FollowMasterBackground(self: SlideRange) -> MsoTriState
        Set: FollowMasterBackground(self: SlideRange) = value
        """
        ...

    @property
    def HasNotesPage(self): # -> MsoTriState
        """ Get: HasNotesPage(self: SlideRange) -> MsoTriState """
        ...

    @property
    def HeadersFooters(self) -> HeadersFooters:
        """ Get: HeadersFooters(self: SlideRange) -> HeadersFooters """
        ...

    @property
    def Hyperlinks(self) -> Hyperlinks:
        """ Get: Hyperlinks(self: SlideRange) -> Hyperlinks """
        ...

    @property
    def Layout(self) -> PpSlideLayout:
        """
        Get: Layout(self: SlideRange) -> PpSlideLayout
        Set: Layout(self: SlideRange) = value
        """
        ...

    @property
    def Master(self) -> Master:
        """ Get: Master(self: SlideRange) -> Master """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SlideRange) -> str
        Set: Name(self: SlideRange) = value
        """
        ...

    @property
    def NotesPage(self) -> SlideRange:
        """ Get: NotesPage(self: SlideRange) -> SlideRange """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: SlideRange) -> object """
        ...

    @property
    def PrintSteps(self) -> int:
        """ Get: PrintSteps(self: SlideRange) -> int """
        ...

    @property
    def Scripts(self): # -> Scripts
        """ Get: Scripts(self: SlideRange) -> Scripts """
        ...

    @property
    def sectionIndex(self) -> int:
        """ Get: sectionIndex(self: SlideRange) -> int """
        ...

    @property
    def SectionNumber(self) -> int:
        """ Get: SectionNumber(self: SlideRange) -> int """
        ...

    @property
    def Shapes(self) -> Shapes:
        """ Get: Shapes(self: SlideRange) -> Shapes """
        ...

    @property
    def SlideID(self) -> int:
        """ Get: SlideID(self: SlideRange) -> int """
        ...

    @property
    def SlideIndex(self) -> int:
        """ Get: SlideIndex(self: SlideRange) -> int """
        ...

    @property
    def SlideNumber(self) -> int:
        """ Get: SlideNumber(self: SlideRange) -> int """
        ...

    @property
    def SlideShowTransition(self) -> SlideShowTransition:
        """ Get: SlideShowTransition(self: SlideRange) -> SlideShowTransition """
        ...

    @property
    def Tags(self) -> Tags:
        """ Get: Tags(self: SlideRange) -> Tags """
        ...

    @property
    def ThemeColorScheme(self): # -> ThemeColorScheme
        """ Get: ThemeColorScheme(self: SlideRange) -> ThemeColorScheme """
        ...

    @property
    def TimeLine(self) -> TimeLine:
        """ Get: TimeLine(self: SlideRange) -> TimeLine """
        ...


    def ApplyTemplate(self, FileName:str): # -> 
        """ ApplyTemplate(self: SlideRange, FileName: str) """
        ...

    def ApplyTemplate2(self, FileName:str, VariantGUID:str): # -> 
        """ ApplyTemplate2(self: SlideRange, FileName: str, VariantGUID: str) """
        ...

    def ApplyTheme(self, themeName:str): # -> 
        """ ApplyTheme(self: SlideRange, themeName: str) """
        ...

    def ApplyThemeColorScheme(self, themeColorSchemeName:str): # -> 
        """ ApplyThemeColorScheme(self: SlideRange, themeColorSchemeName: str) """
        ...

    def Copy(self): # -> 
        """ Copy(self: SlideRange) """
        ...

    def Cut(self): # -> 
        """ Cut(self: SlideRange) """
        ...

    def Delete(self): # -> 
        """ Delete(self: SlideRange) """
        ...

    def Duplicate(self) -> SlideRange:
        """ Duplicate(self: SlideRange) -> SlideRange """
        ...

    def Export(self, FileName:str, FilterName:str, ScaleWidth:int, ScaleHeight:int): # -> 
        """ Export(self: SlideRange, FileName: str, FilterName: str, ScaleWidth: int, ScaleHeight: int) """
        ...

    def MoveTo(self, toPos:int): # -> 
        """ MoveTo(self: SlideRange, toPos: int) """
        ...

    def MoveToSectionStart(self, toSection:int): # -> 
        """ MoveToSectionStart(self: SlideRange, toSection: int) """
        ...

    def PublishSlides(self, SlideLibraryUrl:str, Overwrite:bool, UseSlideOrder:bool): # -> 
        """ PublishSlides(self: SlideRange, SlideLibraryUrl: str, Overwrite: bool, UseSlideOrder: bool) """
        ...

    def Select(self): # -> 
        """ Select(self: SlideRange) """
        ...

    def _Index(self, Index:int) -> object:
        """ _Index(self: SlideRange, Index: int) -> object """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Slides(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Slides) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Slides) -> object """
        ...


    def Add(self, Index:int, Layout:PpSlideLayout) -> Slide:
        """ Add(self: Slides, Index: int, Layout: PpSlideLayout) -> Slide """
        ...

    def AddSlide(self, Index:int, pCustomLayout:CustomLayout) -> Slide:
        """ AddSlide(self: Slides, Index: int, pCustomLayout: CustomLayout) -> Slide """
        ...

    def FindBySlideID(self, SlideID:int) -> Slide:
        """ FindBySlideID(self: Slides, SlideID: int) -> Slide """
        ...

    def InsertFromFile(self, FileName:str, Index:int, SlideStart:int, SlideEnd:int) -> int:
        """ InsertFromFile(self: Slides, FileName: str, Index: int, SlideStart: int, SlideEnd: int) -> int """
        ...

    def Paste(self, Index:int) -> SlideRange:
        """ Paste(self: Slides, Index: int) -> SlideRange """
        ...

    def Range(self, Index:object) -> SlideRange:
        """ Range(self: Slides, Index: object) -> SlideRange """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class SlideShowSettings: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AdvanceMode(self) -> PpSlideShowAdvanceMode:
        """
        Get: AdvanceMode(self: SlideShowSettings) -> PpSlideShowAdvanceMode
        Set: AdvanceMode(self: SlideShowSettings) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: SlideShowSettings) -> Application """
        ...

    @property
    def EndingSlide(self) -> int:
        """
        Get: EndingSlide(self: SlideShowSettings) -> int
        Set: EndingSlide(self: SlideShowSettings) = value
        """
        ...

    @property
    def LoopUntilStopped(self): # -> MsoTriState
        """
        Get: LoopUntilStopped(self: SlideShowSettings) -> MsoTriState
        Set: LoopUntilStopped(self: SlideShowSettings) = value
        """
        ...

    @property
    def NamedSlideShows(self) -> NamedSlideShows:
        """ Get: NamedSlideShows(self: SlideShowSettings) -> NamedSlideShows """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: SlideShowSettings) -> object """
        ...

    @property
    def PointerColor(self) -> ColorFormat:
        """ Get: PointerColor(self: SlideShowSettings) -> ColorFormat """
        ...

    @property
    def RangeType(self) -> PpSlideShowRangeType:
        """
        Get: RangeType(self: SlideShowSettings) -> PpSlideShowRangeType
        Set: RangeType(self: SlideShowSettings) = value
        """
        ...

    @property
    def ShowMediaControls(self): # -> MsoTriState
        """
        Get: ShowMediaControls(self: SlideShowSettings) -> MsoTriState
        Set: ShowMediaControls(self: SlideShowSettings) = value
        """
        ...

    @property
    def ShowPresenterView(self): # -> MsoTriState
        """
        Get: ShowPresenterView(self: SlideShowSettings) -> MsoTriState
        Set: ShowPresenterView(self: SlideShowSettings) = value
        """
        ...

    @property
    def ShowScrollbar(self): # -> MsoTriState
        """
        Get: ShowScrollbar(self: SlideShowSettings) -> MsoTriState
        Set: ShowScrollbar(self: SlideShowSettings) = value
        """
        ...

    @property
    def ShowType(self) -> PpSlideShowType:
        """
        Get: ShowType(self: SlideShowSettings) -> PpSlideShowType
        Set: ShowType(self: SlideShowSettings) = value
        """
        ...

    @property
    def ShowWithAnimation(self): # -> MsoTriState
        """
        Get: ShowWithAnimation(self: SlideShowSettings) -> MsoTriState
        Set: ShowWithAnimation(self: SlideShowSettings) = value
        """
        ...

    @property
    def ShowWithNarration(self): # -> MsoTriState
        """
        Get: ShowWithNarration(self: SlideShowSettings) -> MsoTriState
        Set: ShowWithNarration(self: SlideShowSettings) = value
        """
        ...

    @property
    def SlideShowName(self) -> str:
        """
        Get: SlideShowName(self: SlideShowSettings) -> str
        Set: SlideShowName(self: SlideShowSettings) = value
        """
        ...

    @property
    def StartingSlide(self) -> int:
        """
        Get: StartingSlide(self: SlideShowSettings) -> int
        Set: StartingSlide(self: SlideShowSettings) = value
        """
        ...


    def Run(self) -> SlideShowWindow:
        """ Run(self: SlideShowSettings) -> SlideShowWindow """
        ...


class SlideShowTransition: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AdvanceOnClick(self): # -> MsoTriState
        """
        Get: AdvanceOnClick(self: SlideShowTransition) -> MsoTriState
        Set: AdvanceOnClick(self: SlideShowTransition) = value
        """
        ...

    @property
    def AdvanceOnTime(self): # -> MsoTriState
        """
        Get: AdvanceOnTime(self: SlideShowTransition) -> MsoTriState
        Set: AdvanceOnTime(self: SlideShowTransition) = value
        """
        ...

    @property
    def AdvanceTime(self) -> Single:
        """
        Get: AdvanceTime(self: SlideShowTransition) -> Single
        Set: AdvanceTime(self: SlideShowTransition) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: SlideShowTransition) -> Application """
        ...

    @property
    def Duration(self) -> Single:
        """
        Get: Duration(self: SlideShowTransition) -> Single
        Set: Duration(self: SlideShowTransition) = value
        """
        ...

    @property
    def EntryEffect(self) -> PpEntryEffect:
        """
        Get: EntryEffect(self: SlideShowTransition) -> PpEntryEffect
        Set: EntryEffect(self: SlideShowTransition) = value
        """
        ...

    @property
    def Hidden(self): # -> MsoTriState
        """
        Get: Hidden(self: SlideShowTransition) -> MsoTriState
        Set: Hidden(self: SlideShowTransition) = value
        """
        ...

    @property
    def LoopSoundUntilNext(self): # -> MsoTriState
        """
        Get: LoopSoundUntilNext(self: SlideShowTransition) -> MsoTriState
        Set: LoopSoundUntilNext(self: SlideShowTransition) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: SlideShowTransition) -> object """
        ...

    @property
    def SoundEffect(self) -> SoundEffect:
        """ Get: SoundEffect(self: SlideShowTransition) -> SoundEffect """
        ...

    @property
    def Speed(self) -> PpTransitionSpeed:
        """
        Get: Speed(self: SlideShowTransition) -> PpTransitionSpeed
        Set: Speed(self: SlideShowTransition) = value
        """
        ...



class SlideShowView: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AcceleratorsEnabled(self): # -> MsoTriState
        """
        Get: AcceleratorsEnabled(self: SlideShowView) -> MsoTriState
        Set: AcceleratorsEnabled(self: SlideShowView) = value
        """
        ...

    @property
    def AdvanceMode(self) -> PpSlideShowAdvanceMode:
        """ Get: AdvanceMode(self: SlideShowView) -> PpSlideShowAdvanceMode """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: SlideShowView) -> Application """
        ...

    @property
    def CurrentShowPosition(self) -> int:
        """ Get: CurrentShowPosition(self: SlideShowView) -> int """
        ...

    @property
    def IsNamedShow(self): # -> MsoTriState
        """ Get: IsNamedShow(self: SlideShowView) -> MsoTriState """
        ...

    @property
    def LastSlideViewed(self) -> Slide:
        """ Get: LastSlideViewed(self: SlideShowView) -> Slide """
        ...

    @property
    def MediaControlsHeight(self) -> Single:
        """ Get: MediaControlsHeight(self: SlideShowView) -> Single """
        ...

    @property
    def MediaControlsLeft(self) -> Single:
        """ Get: MediaControlsLeft(self: SlideShowView) -> Single """
        ...

    @property
    def MediaControlsTop(self) -> Single:
        """ Get: MediaControlsTop(self: SlideShowView) -> Single """
        ...

    @property
    def MediaControlsVisible(self): # -> MsoTriState
        """ Get: MediaControlsVisible(self: SlideShowView) -> MsoTriState """
        ...

    @property
    def MediaControlsWidth(self) -> Single:
        """ Get: MediaControlsWidth(self: SlideShowView) -> Single """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: SlideShowView) -> object """
        ...

    @property
    def PointerColor(self) -> ColorFormat:
        """ Get: PointerColor(self: SlideShowView) -> ColorFormat """
        ...

    @property
    def PointerType(self) -> PpSlideShowPointerType:
        """
        Get: PointerType(self: SlideShowView) -> PpSlideShowPointerType
        Set: PointerType(self: SlideShowView) = value
        """
        ...

    @property
    def PresentationElapsedTime(self) -> Single:
        """ Get: PresentationElapsedTime(self: SlideShowView) -> Single """
        ...

    @property
    def Slide(self) -> Slide:
        """ Get: Slide(self: SlideShowView) -> Slide """
        ...

    @property
    def SlideElapsedTime(self) -> Single:
        """
        Get: SlideElapsedTime(self: SlideShowView) -> Single
        Set: SlideElapsedTime(self: SlideShowView) = value
        """
        ...

    @property
    def SlideShowName(self) -> str:
        """ Get: SlideShowName(self: SlideShowView) -> str """
        ...

    @property
    def State(self) -> PpSlideShowState:
        """
        Get: State(self: SlideShowView) -> PpSlideShowState
        Set: State(self: SlideShowView) = value
        """
        ...

    @property
    def Zoom(self) -> int:
        """ Get: Zoom(self: SlideShowView) -> int """
        ...


    def DrawLine(self, BeginX:Single, BeginY:Single, EndX:Single, EndY:Single): # -> 
        """ DrawLine(self: SlideShowView, BeginX: Single, BeginY: Single, EndX: Single, EndY: Single) """
        ...

    def EndNamedShow(self): # -> 
        """ EndNamedShow(self: SlideShowView) """
        ...

    def EraseDrawing(self): # -> 
        """ EraseDrawing(self: SlideShowView) """
        ...

    def Exit(self): # -> 
        """ Exit(self: SlideShowView) """
        ...

    def First(self): # -> 
        """ First(self: SlideShowView) """
        ...

    def FirstAnimationIsAutomatic(self) -> bool:
        """ FirstAnimationIsAutomatic(self: SlideShowView) -> bool """
        ...

    def GetClickCount(self) -> int:
        """ GetClickCount(self: SlideShowView) -> int """
        ...

    def GetClickIndex(self) -> int:
        """ GetClickIndex(self: SlideShowView) -> int """
        ...

    def GotoClick(self, Index:int): # -> 
        """ GotoClick(self: SlideShowView, Index: int) """
        ...

    def GotoNamedShow(self, SlideShowName:str): # -> 
        """ GotoNamedShow(self: SlideShowView, SlideShowName: str) """
        ...

    def GotoSlide(self, Index:int, ResetSlide): # ->  # Not found arg types: {'ResetSlide': 'MsoTriState'}
        """ GotoSlide(self: SlideShowView, Index: int, ResetSlide: MsoTriState) """
        ...

    def InstallTracker(self, pTracker:MouseTracker, Presenter): # ->  # Not found arg types: {'Presenter': 'MsoTriState'}
        """ InstallTracker(self: SlideShowView, pTracker: MouseTracker, Presenter: MsoTriState) """
        ...

    def Last(self): # -> 
        """ Last(self: SlideShowView) """
        ...

    def Next(self): # -> 
        """ Next(self: SlideShowView) """
        ...

    def Player(self, ShapeId:object) -> Player:
        """ Player(self: SlideShowView, ShapeId: object) -> Player """
        ...

    def Previous(self): # -> 
        """ Previous(self: SlideShowView) """
        ...

    def ResetSlideTime(self): # -> 
        """ ResetSlideTime(self: SlideShowView) """
        ...


class SlideShowWindow: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Active(self): # -> MsoTriState
        """ Get: Active(self: SlideShowWindow) -> MsoTriState """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: SlideShowWindow) -> Application """
        ...

    @property
    def Height(self) -> Single:
        """
        Get: Height(self: SlideShowWindow) -> Single
        Set: Height(self: SlideShowWindow) = value
        """
        ...

    @property
    def HWND(self) -> int:
        """ Get: HWND(self: SlideShowWindow) -> int """
        ...

    @property
    def IsFullScreen(self): # -> MsoTriState
        """ Get: IsFullScreen(self: SlideShowWindow) -> MsoTriState """
        ...

    @property
    def Left(self) -> Single:
        """
        Get: Left(self: SlideShowWindow) -> Single
        Set: Left(self: SlideShowWindow) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: SlideShowWindow) -> object """
        ...

    @property
    def Presentation(self) -> Presentation:
        """ Get: Presentation(self: SlideShowWindow) -> Presentation """
        ...

    @property
    def SlideNavigation(self) -> SlideNavigation:
        """ Get: SlideNavigation(self: SlideShowWindow) -> SlideNavigation """
        ...

    @property
    def Top(self) -> Single:
        """
        Get: Top(self: SlideShowWindow) -> Single
        Set: Top(self: SlideShowWindow) = value
        """
        ...

    @property
    def View(self) -> SlideShowView:
        """ Get: View(self: SlideShowWindow) -> SlideShowView """
        ...

    @property
    def Width(self) -> Single:
        """
        Get: Width(self: SlideShowWindow) -> Single
        Set: Width(self: SlideShowWindow) = value
        """
        ...


    def Activate(self): # -> 
        """ Activate(self: SlideShowWindow) """
        ...


class SlideShowWindows(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: SlideShowWindows) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: SlideShowWindows) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class SoundEffect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: SoundEffect) -> Application """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SoundEffect) -> str
        Set: Name(self: SoundEffect) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: SoundEffect) -> object """
        ...

    @property
    def Type(self) -> PpSoundEffectType:
        """
        Get: Type(self: SoundEffect) -> PpSoundEffectType
        Set: Type(self: SoundEffect) = value
        """
        ...


    def ImportFromFile(self, FileName:str): # -> 
        """ ImportFromFile(self: SoundEffect, FileName: str) """
        ...

    def Play(self): # -> 
        """ Play(self: SoundEffect) """
        ...


class SoundFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SourceFullName(self) -> str:
        """ Get: SourceFullName(self: SoundFormat) -> str """
        ...

    @property
    def Type(self) -> PpSoundFormatType:
        """ Get: Type(self: SoundFormat) -> PpSoundFormatType """
        ...


    def Export(self, FileName:str) -> PpSoundFormatType:
        """ Export(self: SoundFormat, FileName: str) -> PpSoundFormatType """
        ...

    def Import(self, FileName:str): # -> 
        """ Import(self: SoundFormat, FileName: str) """
        ...

    def Play(self): # -> 
        """ Play(self: SoundFormat) """
        ...


class Table: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AlternativeText(self) -> str:
        """
        Get: AlternativeText(self: Table) -> str
        Set: AlternativeText(self: Table) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: Table) -> Application """
        ...

    @property
    def Background(self) -> TableBackground:
        """ Get: Background(self: Table) -> TableBackground """
        ...

    @property
    def Columns(self) -> Columns:
        """ Get: Columns(self: Table) -> Columns """
        ...

    @property
    def FirstCol(self) -> bool:
        """
        Get: FirstCol(self: Table) -> bool
        Set: FirstCol(self: Table) = value
        """
        ...

    @property
    def FirstRow(self) -> bool:
        """
        Get: FirstRow(self: Table) -> bool
        Set: FirstRow(self: Table) = value
        """
        ...

    @property
    def HorizBanding(self) -> bool:
        """
        Get: HorizBanding(self: Table) -> bool
        Set: HorizBanding(self: Table) = value
        """
        ...

    @property
    def LastCol(self) -> bool:
        """
        Get: LastCol(self: Table) -> bool
        Set: LastCol(self: Table) = value
        """
        ...

    @property
    def LastRow(self) -> bool:
        """
        Get: LastRow(self: Table) -> bool
        Set: LastRow(self: Table) = value
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
    def Style(self) -> TableStyle:
        """ Get: Style(self: Table) -> TableStyle """
        ...

    @property
    def TableDirection(self) -> PpDirection:
        """
        Get: TableDirection(self: Table) -> PpDirection
        Set: TableDirection(self: Table) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: Table) -> str
        Set: Title(self: Table) = value
        """
        ...

    @property
    def VertBanding(self) -> bool:
        """
        Get: VertBanding(self: Table) -> bool
        Set: VertBanding(self: Table) = value
        """
        ...


    def ApplyStyle(self, StyleID:str, SaveFormatting:bool): # -> 
        """ ApplyStyle(self: Table, StyleID: str, SaveFormatting: bool) """
        ...

    def Cell(self, Row:int, Column:int) -> Cell:
        """ Cell(self: Table, Row: int, Column: int) -> Cell """
        ...

    def MergeBorders(self): # -> 
        """ MergeBorders(self: Table) """
        ...

    def ScaleProportionally(self, scale:Single): # -> 
        """ ScaleProportionally(self: Table, scale: Single) """
        ...


class TableBackground: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Fill(self) -> FillFormat:
        """ Get: Fill(self: TableBackground) -> FillFormat """
        ...

    @property
    def Picture(self) -> PictureFormat:
        """ Get: Picture(self: TableBackground) -> PictureFormat """
        ...

    @property
    def Reflection(self) -> ReflectionFormat:
        """ Get: Reflection(self: TableBackground) -> ReflectionFormat """
        ...

    @property
    def Shadow(self) -> ShadowFormat:
        """ Get: Shadow(self: TableBackground) -> ShadowFormat """
        ...



class TableStyle: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Id(self) -> str:
        """ Get: Id(self: TableStyle) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: TableStyle) -> str """
        ...



class TabStop: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: TabStop) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TabStop) -> object """
        ...

    @property
    def Position(self) -> Single:
        """
        Get: Position(self: TabStop) -> Single
        Set: Position(self: TabStop) = value
        """
        ...

    @property
    def Type(self) -> PpTabStopType:
        """
        Get: Type(self: TabStop) -> PpTabStopType
        Set: Type(self: TabStop) = value
        """
        ...


    def Clear(self): # -> 
        """ Clear(self: TabStop) """
        ...


class TabStops(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: TabStops) -> Application """
        ...

    @property
    def DefaultSpacing(self) -> Single:
        """
        Get: DefaultSpacing(self: TabStops) -> Single
        Set: DefaultSpacing(self: TabStops) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TabStops) -> object """
        ...


    def Add(self, Type:PpTabStopType, Position:Single) -> TabStop:
        """ Add(self: TabStops, Type: PpTabStopType, Position: Single) -> TabStop """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Tags(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Tags) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Tags) -> object """
        ...


    def Add(self, Name:str, Value:str): # -> 
        """ Add(self: Tags, Name: str, Value: str) """
        ...

    def AddBinary(self, Name:str, FilePath:str): # -> 
        """ AddBinary(self: Tags, Name: str, FilePath: str) """
        ...

    def BinaryValue(self, Name:str) -> int:
        """ BinaryValue(self: Tags, Name: str) -> int """
        ...

    def Delete(self, Name:str): # -> 
        """ Delete(self: Tags, Name: str) """
        ...

    def Name(self, Index:int) -> str:
        """ Name(self: Tags, Index: int) -> str """
        ...

    def Value(self, Index:int) -> str:
        """ Value(self: Tags, Index: int) -> str """
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
    def Application(self) -> object:
        """ Get: Application(self: TextEffectFormat) -> object """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: TextEffectFormat) -> int """
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
    def FontSize(self) -> Single:
        """
        Get: FontSize(self: TextEffectFormat) -> Single
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
    def Tracking(self) -> Single:
        """
        Get: Tracking(self: TextEffectFormat) -> Single
        Set: Tracking(self: TextEffectFormat) = value
        """
        ...


    def ToggleVerticalText(self): # -> 
        """ ToggleVerticalText(self: TextEffectFormat) """
        ...


class TextFrame: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: TextFrame) -> object """
        ...

    @property
    def AutoSize(self) -> PpAutoSize:
        """
        Get: AutoSize(self: TextFrame) -> PpAutoSize
        Set: AutoSize(self: TextFrame) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: TextFrame) -> int """
        ...

    @property
    def HasText(self): # -> MsoTriState
        """ Get: HasText(self: TextFrame) -> MsoTriState """
        ...

    @property
    def HorizontalAnchor(self): # -> MsoHorizontalAnchor
        """
        Get: HorizontalAnchor(self: TextFrame) -> MsoHorizontalAnchor
        Set: HorizontalAnchor(self: TextFrame) = value
        """
        ...

    @property
    def MarginBottom(self) -> Single:
        """
        Get: MarginBottom(self: TextFrame) -> Single
        Set: MarginBottom(self: TextFrame) = value
        """
        ...

    @property
    def MarginLeft(self) -> Single:
        """
        Get: MarginLeft(self: TextFrame) -> Single
        Set: MarginLeft(self: TextFrame) = value
        """
        ...

    @property
    def MarginRight(self) -> Single:
        """
        Get: MarginRight(self: TextFrame) -> Single
        Set: MarginRight(self: TextFrame) = value
        """
        ...

    @property
    def MarginTop(self) -> Single:
        """
        Get: MarginTop(self: TextFrame) -> Single
        Set: MarginTop(self: TextFrame) = value
        """
        ...

    @property
    def Orientation(self): # -> MsoTextOrientation
        """
        Get: Orientation(self: TextFrame) -> MsoTextOrientation
        Set: Orientation(self: TextFrame) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TextFrame) -> object """
        ...

    @property
    def Ruler(self) -> Ruler:
        """ Get: Ruler(self: TextFrame) -> Ruler """
        ...

    @property
    def TextRange(self) -> TextRange:
        """ Get: TextRange(self: TextFrame) -> TextRange """
        ...

    @property
    def VerticalAnchor(self): # -> MsoVerticalAnchor
        """
        Get: VerticalAnchor(self: TextFrame) -> MsoVerticalAnchor
        Set: VerticalAnchor(self: TextFrame) = value
        """
        ...

    @property
    def WordWrap(self): # -> MsoTriState
        """
        Get: WordWrap(self: TextFrame) -> MsoTriState
        Set: WordWrap(self: TextFrame) = value
        """
        ...


    def DeleteText(self): # -> 
        """ DeleteText(self: TextFrame) """
        ...


class TextFrame2: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: TextFrame2) -> object """
        ...

    @property
    def AutoSize(self): # -> MsoAutoSize
        """
        Get: AutoSize(self: TextFrame2) -> MsoAutoSize
        Set: AutoSize(self: TextFrame2) = value
        """
        ...

    @property
    def Column(self): # -> TextColumn2
        """ Get: Column(self: TextFrame2) -> TextColumn2 """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: TextFrame2) -> int """
        ...

    @property
    def HasText(self): # -> MsoTriState
        """ Get: HasText(self: TextFrame2) -> MsoTriState """
        ...

    @property
    def HorizontalAnchor(self): # -> MsoHorizontalAnchor
        """
        Get: HorizontalAnchor(self: TextFrame2) -> MsoHorizontalAnchor
        Set: HorizontalAnchor(self: TextFrame2) = value
        """
        ...

    @property
    def MarginBottom(self) -> Single:
        """
        Get: MarginBottom(self: TextFrame2) -> Single
        Set: MarginBottom(self: TextFrame2) = value
        """
        ...

    @property
    def MarginLeft(self) -> Single:
        """
        Get: MarginLeft(self: TextFrame2) -> Single
        Set: MarginLeft(self: TextFrame2) = value
        """
        ...

    @property
    def MarginRight(self) -> Single:
        """
        Get: MarginRight(self: TextFrame2) -> Single
        Set: MarginRight(self: TextFrame2) = value
        """
        ...

    @property
    def MarginTop(self) -> Single:
        """
        Get: MarginTop(self: TextFrame2) -> Single
        Set: MarginTop(self: TextFrame2) = value
        """
        ...

    @property
    def NoTextRotation(self): # -> MsoTriState
        """
        Get: NoTextRotation(self: TextFrame2) -> MsoTriState
        Set: NoTextRotation(self: TextFrame2) = value
        """
        ...

    @property
    def Orientation(self): # -> MsoTextOrientation
        """
        Get: Orientation(self: TextFrame2) -> MsoTextOrientation
        Set: Orientation(self: TextFrame2) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TextFrame2) -> object """
        ...

    @property
    def PathFormat(self): # -> MsoPathFormat
        """
        Get: PathFormat(self: TextFrame2) -> MsoPathFormat
        Set: PathFormat(self: TextFrame2) = value
        """
        ...

    @property
    def Ruler(self): # -> Ruler2
        """ Get: Ruler(self: TextFrame2) -> Ruler2 """
        ...

    @property
    def TextRange(self): # -> TextRange2
        """ Get: TextRange(self: TextFrame2) -> TextRange2 """
        ...

    @property
    def ThreeD(self) -> ThreeDFormat:
        """ Get: ThreeD(self: TextFrame2) -> ThreeDFormat """
        ...

    @property
    def VerticalAnchor(self): # -> MsoVerticalAnchor
        """
        Get: VerticalAnchor(self: TextFrame2) -> MsoVerticalAnchor
        Set: VerticalAnchor(self: TextFrame2) = value
        """
        ...

    @property
    def WarpFormat(self): # -> MsoWarpFormat
        """
        Get: WarpFormat(self: TextFrame2) -> MsoWarpFormat
        Set: WarpFormat(self: TextFrame2) = value
        """
        ...

    @property
    def WordArtFormat(self): # -> MsoPresetTextEffect
        """
        Get: WordArtFormat(self: TextFrame2) -> MsoPresetTextEffect
        Set: WordArtFormat(self: TextFrame2) = value
        """
        ...

    @property
    def WordWrap(self): # -> MsoTriState
        """
        Get: WordWrap(self: TextFrame2) -> MsoTriState
        Set: WordWrap(self: TextFrame2) = value
        """
        ...


    def DeleteText(self): # -> 
        """ DeleteText(self: TextFrame2) """
        ...


class TextRange(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def ActionSettings(self) -> ActionSettings:
        """ Get: ActionSettings(self: TextRange) -> ActionSettings """
        ...

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
    def Font(self) -> Font:
        """ Get: Font(self: TextRange) -> Font """
        ...

    @property
    def IndentLevel(self) -> int:
        """
        Get: IndentLevel(self: TextRange) -> int
        Set: IndentLevel(self: TextRange) = value
        """
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
    def ParagraphFormat(self) -> ParagraphFormat:
        """ Get: ParagraphFormat(self: TextRange) -> ParagraphFormat """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TextRange) -> object """
        ...

    @property
    def Start(self) -> int:
        """ Get: Start(self: TextRange) -> int """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: TextRange) -> str
        Set: Text(self: TextRange) = value
        """
        ...


    def AddPeriods(self): # -> 
        """ AddPeriods(self: TextRange) """
        ...

    def ChangeCase(self, Type:PpChangeCase): # -> 
        """ ChangeCase(self: TextRange, Type: PpChangeCase) """
        ...

    def Characters(self, Start:int, Length:int) -> TextRange:
        """ Characters(self: TextRange, Start: int, Length: int) -> TextRange """
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

    def Find(self, FindWhat:str, After:int, MatchCase, WholeWords) -> TextRange: # Not found arg types: {'MatchCase': 'MsoTriState', 'WholeWords': 'MsoTriState'}
        """ Find(self: TextRange, FindWhat: str, After: int, MatchCase: MsoTriState, WholeWords: MsoTriState) -> TextRange """
        ...

    def InsertAfter(self, NewText:str) -> TextRange:
        """ InsertAfter(self: TextRange, NewText: str) -> TextRange """
        ...

    def InsertBefore(self, NewText:str) -> TextRange:
        """ InsertBefore(self: TextRange, NewText: str) -> TextRange """
        ...

    def InsertDateTime(self, DateTimeFormat:PpDateTimeFormat, InsertAsField) -> TextRange: # Not found arg types: {'InsertAsField': 'MsoTriState'}
        """ InsertDateTime(self: TextRange, DateTimeFormat: PpDateTimeFormat, InsertAsField: MsoTriState) -> TextRange """
        ...

    def InsertSlideNumber(self) -> TextRange:
        """ InsertSlideNumber(self: TextRange) -> TextRange """
        ...

    def InsertSymbol(self, FontName:str, CharNumber:int, Unicode) -> TextRange: # Not found arg types: {'Unicode': 'MsoTriState'}
        """ InsertSymbol(self: TextRange, FontName: str, CharNumber: int, Unicode: MsoTriState) -> TextRange """
        ...

    def Lines(self, Start:int, Length:int) -> TextRange:
        """ Lines(self: TextRange, Start: int, Length: int) -> TextRange """
        ...

    def LtrRun(self): # -> 
        """ LtrRun(self: TextRange) """
        ...

    def Paragraphs(self, Start:int, Length:int) -> TextRange:
        """ Paragraphs(self: TextRange, Start: int, Length: int) -> TextRange """
        ...

    def Paste(self) -> TextRange:
        """ Paste(self: TextRange) -> TextRange """
        ...

    def PasteSpecial(self, DataType:PpPasteDataType, DisplayAsIcon, IconFileName:str, IconIndex:int, IconLabel:str, Link) -> TextRange: # Not found arg types: {'DisplayAsIcon': 'MsoTriState', 'Link': 'MsoTriState'}
        """ PasteSpecial(self: TextRange, DataType: PpPasteDataType, DisplayAsIcon: MsoTriState, IconFileName: str, IconIndex: int, IconLabel: str, Link: MsoTriState) -> TextRange """
        ...

    def RemovePeriods(self): # -> 
        """ RemovePeriods(self: TextRange) """
        ...

    def Replace(self, FindWhat:str, ReplaceWhat:str, After:int, MatchCase, WholeWords) -> TextRange: # Not found arg types: {'MatchCase': 'MsoTriState', 'WholeWords': 'MsoTriState'}
        """ Replace(self: TextRange, FindWhat: str, ReplaceWhat: str, After: int, MatchCase: MsoTriState, WholeWords: MsoTriState) -> TextRange """
        ...

    def RotatedBounds(self, X1, Y1, X2, Y2, X3, Y3, x4, y4) -> Tuple_[Single, Single, Single, Single, Single, Single, Single, Single]:
        """ RotatedBounds(self: TextRange) -> (Single, Single, Single, Single, Single, Single, Single, Single) """
        ...

    def RtlRun(self): # -> 
        """ RtlRun(self: TextRange) """
        ...

    def Runs(self, Start:int, Length:int) -> TextRange:
        """ Runs(self: TextRange, Start: int, Length: int) -> TextRange """
        ...

    def Select(self): # -> 
        """ Select(self: TextRange) """
        ...

    def Sentences(self, Start:int, Length:int) -> TextRange:
        """ Sentences(self: TextRange, Start: int, Length: int) -> TextRange """
        ...

    def TrimText(self) -> TextRange:
        """ TrimText(self: TextRange) -> TextRange """
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
    def Levels(self) -> TextStyleLevels:
        """ Get: Levels(self: TextStyle) -> TextStyleLevels """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TextStyle) -> object """
        ...

    @property
    def Ruler(self) -> Ruler:
        """ Get: Ruler(self: TextStyle) -> Ruler """
        ...

    @property
    def TextFrame(self) -> TextFrame:
        """ Get: TextFrame(self: TextStyle) -> TextFrame """
        ...



class TextStyleLevel: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: TextStyleLevel) -> Application """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: TextStyleLevel) -> Font """
        ...

    @property
    def ParagraphFormat(self) -> ParagraphFormat:
        """ Get: ParagraphFormat(self: TextStyleLevel) -> ParagraphFormat """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TextStyleLevel) -> object """
        ...



class TextStyleLevels(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: TextStyleLevels) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TextStyleLevels) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class TextStyles(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: TextStyles) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TextStyles) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class Theme: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Theme) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Theme) -> object """
        ...

    @property
    def ThemeVariants(self) -> ThemeVariants:
        """ Get: ThemeVariants(self: Theme) -> ThemeVariants """
        ...



class ThemeVariant: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ThemeVariant) -> Application """
        ...

    @property
    def Height(self) -> int:
        """ Get: Height(self: ThemeVariant) -> int """
        ...

    @property
    def Id(self) -> str:
        """ Get: Id(self: ThemeVariant) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ThemeVariant) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ThemeVariant) -> object """
        ...

    @property
    def Width(self) -> int:
        """ Get: Width(self: ThemeVariant) -> int """
        ...



class ThemeVariants(Collection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ThemeVariants) -> Application """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ThemeVariants) -> object """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ThreeDFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> object:
        """ Get: Application(self: ThreeDFormat) -> object """
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
    def Creator(self) -> int:
        """ Get: Creator(self: ThreeDFormat) -> int """
        ...

    @property
    def Depth(self) -> Single:
        """
        Get: Depth(self: ThreeDFormat) -> Single
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
    def LightAngle(self) -> Single:
        """
        Get: LightAngle(self: ThreeDFormat) -> Single
        Set: LightAngle(self: ThreeDFormat) = value
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
    def PresetCamera(self): # -> MsoPresetCamera
        """ Get: PresetCamera(self: ThreeDFormat) -> MsoPresetCamera """
        ...

    @property
    def PresetExtrusionDirection(self): # -> MsoPresetExtrusionDirection
        """ Get: PresetExtrusionDirection(self: ThreeDFormat) -> MsoPresetExtrusionDirection """
        ...

    @property
    def PresetLighting(self): # -> MsoLightRigType
        """
        Get: PresetLighting(self: ThreeDFormat) -> MsoLightRigType
        Set: PresetLighting(self: ThreeDFormat) = value
        """
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
    def ProjectText(self): # -> MsoTriState
        """
        Get: ProjectText(self: ThreeDFormat) -> MsoTriState
        Set: ProjectText(self: ThreeDFormat) = value
        """
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
    def RotationZ(self) -> Single:
        """
        Get: RotationZ(self: ThreeDFormat) -> Single
        Set: RotationZ(self: ThreeDFormat) = value
        """
        ...

    @property
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: ThreeDFormat) -> MsoTriState
        Set: Visible(self: ThreeDFormat) = value
        """
        ...

    @property
    def Z(self) -> Single:
        """
        Get: Z(self: ThreeDFormat) -> Single
        Set: Z(self: ThreeDFormat) = value
        """
        ...


    def IncrementRotationHorizontal(self, Increment:Single): # -> 
        """ IncrementRotationHorizontal(self: ThreeDFormat, Increment: Single) """
        ...

    def IncrementRotationVertical(self, Increment:Single): # -> 
        """ IncrementRotationVertical(self: ThreeDFormat, Increment: Single) """
        ...

    def IncrementRotationX(self, Increment:Single): # -> 
        """ IncrementRotationX(self: ThreeDFormat, Increment: Single) """
        ...

    def IncrementRotationY(self, Increment:Single): # -> 
        """ IncrementRotationY(self: ThreeDFormat, Increment: Single) """
        ...

    def IncrementRotationZ(self, Increment:Single): # -> 
        """ IncrementRotationZ(self: ThreeDFormat, Increment: Single) """
        ...

    def ResetRotation(self): # -> 
        """ ResetRotation(self: ThreeDFormat) """
        ...

    def SetExtrusionDirection(self, PresetExtrusionDirection): # ->  # Not found arg types: {'PresetExtrusionDirection': 'MsoPresetExtrusionDirection'}
        """ SetExtrusionDirection(self: ThreeDFormat, PresetExtrusionDirection: MsoPresetExtrusionDirection) """
        ...

    def SetPresetCamera(self, PresetCamera): # ->  # Not found arg types: {'PresetCamera': 'MsoPresetCamera'}
        """ SetPresetCamera(self: ThreeDFormat, PresetCamera: MsoPresetCamera) """
        ...

    def SetThreeDFormat(self, PresetThreeDFormat): # ->  # Not found arg types: {'PresetThreeDFormat': 'MsoPresetThreeDFormat'}
        """ SetThreeDFormat(self: ThreeDFormat, PresetThreeDFormat: MsoPresetThreeDFormat) """
        ...


class TickLabels: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Alignment(self) -> int:
        """
        Get: Alignment(self: TickLabels) -> int
        Set: Alignment(self: TickLabels) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: TickLabels) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: TickLabels) -> object
        Set: AutoScaleFont(self: TickLabels) = value
        """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: TickLabels) -> int """
        ...

    @property
    def Depth(self) -> int:
        """ Get: Depth(self: TickLabels) -> int """
        ...

    @property
    def Font(self) -> ChartFont:
        """ Get: Font(self: TickLabels) -> ChartFont """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: TickLabels) -> ChartFormat """
        ...

    @property
    def MultiLevel(self) -> bool:
        """
        Get: MultiLevel(self: TickLabels) -> bool
        Set: MultiLevel(self: TickLabels) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: TickLabels) -> str """
        ...

    @property
    def NumberFormat(self) -> str:
        """
        Get: NumberFormat(self: TickLabels) -> str
        Set: NumberFormat(self: TickLabels) = value
        """
        ...

    @property
    def NumberFormatLinked(self) -> bool:
        """
        Get: NumberFormatLinked(self: TickLabels) -> bool
        Set: NumberFormatLinked(self: TickLabels) = value
        """
        ...

    @property
    def NumberFormatLocal(self) -> object:
        """
        Get: NumberFormatLocal(self: TickLabels) -> object
        Set: NumberFormatLocal(self: TickLabels) = value
        """
        ...

    @property
    def Offset(self) -> int:
        """
        Get: Offset(self: TickLabels) -> int
        Set: Offset(self: TickLabels) = value
        """
        ...

    @property
    def Orientation(self) -> XlTickLabelOrientation:
        """
        Get: Orientation(self: TickLabels) -> XlTickLabelOrientation
        Set: Orientation(self: TickLabels) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TickLabels) -> object """
        ...

    @property
    def ReadingOrder(self) -> int:
        """
        Get: ReadingOrder(self: TickLabels) -> int
        Set: ReadingOrder(self: TickLabels) = value
        """
        ...


    def Delete(self) -> object:
        """ Delete(self: TickLabels) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: TickLabels) -> object """
        ...


class TimeLine: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: TimeLine) -> Application """
        ...

    @property
    def InteractiveSequences(self) -> Sequences:
        """ Get: InteractiveSequences(self: TimeLine) -> Sequences """
        ...

    @property
    def MainSequence(self) -> Sequence:
        """ Get: MainSequence(self: TimeLine) -> Sequence """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: TimeLine) -> object """
        ...



class Timing: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Accelerate(self) -> Single:
        """
        Get: Accelerate(self: Timing) -> Single
        Set: Accelerate(self: Timing) = value
        """
        ...

    @property
    def Application(self) -> Application:
        """ Get: Application(self: Timing) -> Application """
        ...

    @property
    def AutoReverse(self): # -> MsoTriState
        """
        Get: AutoReverse(self: Timing) -> MsoTriState
        Set: AutoReverse(self: Timing) = value
        """
        ...

    @property
    def BounceEnd(self): # -> MsoTriState
        """
        Get: BounceEnd(self: Timing) -> MsoTriState
        Set: BounceEnd(self: Timing) = value
        """
        ...

    @property
    def BounceEndIntensity(self) -> Single:
        """
        Get: BounceEndIntensity(self: Timing) -> Single
        Set: BounceEndIntensity(self: Timing) = value
        """
        ...

    @property
    def Decelerate(self) -> Single:
        """
        Get: Decelerate(self: Timing) -> Single
        Set: Decelerate(self: Timing) = value
        """
        ...

    @property
    def Duration(self) -> Single:
        """
        Get: Duration(self: Timing) -> Single
        Set: Duration(self: Timing) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Timing) -> object """
        ...

    @property
    def RepeatCount(self) -> int:
        """
        Get: RepeatCount(self: Timing) -> int
        Set: RepeatCount(self: Timing) = value
        """
        ...

    @property
    def RepeatDuration(self) -> Single:
        """
        Get: RepeatDuration(self: Timing) -> Single
        Set: RepeatDuration(self: Timing) = value
        """
        ...

    @property
    def Restart(self) -> MsoAnimEffectRestart:
        """
        Get: Restart(self: Timing) -> MsoAnimEffectRestart
        Set: Restart(self: Timing) = value
        """
        ...

    @property
    def RewindAtEnd(self): # -> MsoTriState
        """
        Get: RewindAtEnd(self: Timing) -> MsoTriState
        Set: RewindAtEnd(self: Timing) = value
        """
        ...

    @property
    def SmoothEnd(self): # -> MsoTriState
        """
        Get: SmoothEnd(self: Timing) -> MsoTriState
        Set: SmoothEnd(self: Timing) = value
        """
        ...

    @property
    def SmoothStart(self): # -> MsoTriState
        """
        Get: SmoothStart(self: Timing) -> MsoTriState
        Set: SmoothStart(self: Timing) = value
        """
        ...

    @property
    def Speed(self) -> Single:
        """
        Get: Speed(self: Timing) -> Single
        Set: Speed(self: Timing) = value
        """
        ...

    @property
    def TriggerBookmark(self) -> str:
        """
        Get: TriggerBookmark(self: Timing) -> str
        Set: TriggerBookmark(self: Timing) = value
        """
        ...

    @property
    def TriggerDelayTime(self) -> Single:
        """
        Get: TriggerDelayTime(self: Timing) -> Single
        Set: TriggerDelayTime(self: Timing) = value
        """
        ...

    @property
    def TriggerShape(self) -> Shape:
        """
        Get: TriggerShape(self: Timing) -> Shape
        Set: TriggerShape(self: Timing) = value
        """
        ...

    @property
    def TriggerType(self) -> MsoAnimTriggerType:
        """
        Get: TriggerType(self: Timing) -> MsoAnimTriggerType
        Set: TriggerType(self: Timing) = value
        """
        ...



class Trendline: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Trendline) -> Application """
        ...

    @property
    def Backward(self) -> int:
        """
        Get: Backward(self: Trendline) -> int
        Set: Backward(self: Trendline) = value
        """
        ...

    @property
    def Backward2(self) -> float:
        """
        Get: Backward2(self: Trendline) -> float
        Set: Backward2(self: Trendline) = value
        """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: Trendline) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Trendline) -> int """
        ...

    @property
    def DataLabel(self) -> DataLabel:
        """ Get: DataLabel(self: Trendline) -> DataLabel """
        ...

    @property
    def DisplayEquation(self) -> bool:
        """
        Get: DisplayEquation(self: Trendline) -> bool
        Set: DisplayEquation(self: Trendline) = value
        """
        ...

    @property
    def DisplayRSquared(self) -> bool:
        """
        Get: DisplayRSquared(self: Trendline) -> bool
        Set: DisplayRSquared(self: Trendline) = value
        """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: Trendline) -> ChartFormat """
        ...

    @property
    def Forward(self) -> int:
        """
        Get: Forward(self: Trendline) -> int
        Set: Forward(self: Trendline) = value
        """
        ...

    @property
    def Forward2(self) -> float:
        """
        Get: Forward2(self: Trendline) -> float
        Set: Forward2(self: Trendline) = value
        """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: Trendline) -> int """
        ...

    @property
    def Intercept(self) -> float:
        """
        Get: Intercept(self: Trendline) -> float
        Set: Intercept(self: Trendline) = value
        """
        ...

    @property
    def InterceptIsAuto(self) -> bool:
        """
        Get: InterceptIsAuto(self: Trendline) -> bool
        Set: InterceptIsAuto(self: Trendline) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Trendline) -> str
        Set: Name(self: Trendline) = value
        """
        ...

    @property
    def NameIsAuto(self) -> bool:
        """
        Get: NameIsAuto(self: Trendline) -> bool
        Set: NameIsAuto(self: Trendline) = value
        """
        ...

    @property
    def Order(self) -> int:
        """
        Get: Order(self: Trendline) -> int
        Set: Order(self: Trendline) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Trendline) -> object """
        ...

    @property
    def Period(self) -> int:
        """
        Get: Period(self: Trendline) -> int
        Set: Period(self: Trendline) = value
        """
        ...

    @property
    def Type(self) -> XlTrendlineType:
        """
        Get: Type(self: Trendline) -> XlTrendlineType
        Set: Type(self: Trendline) = value
        """
        ...


    def ClearFormats(self) -> object:
        """ ClearFormats(self: Trendline) -> object """
        ...

    def Delete(self) -> object:
        """ Delete(self: Trendline) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: Trendline) -> object """
        ...


class Trendlines(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Trendlines) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: Trendlines) -> int """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Trendlines) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Trendlines) -> object """
        ...


    def Add(self, Type:XlTrendlineType, Order:object, Period:object, Forward:object, Backward:object, Intercept:object, DisplayEquation:object, DisplayRSquared:object, Name:object) -> Trendline:
        """ Add(self: Trendlines, Type: XlTrendlineType, Order: object, Period: object, Forward: object, Backward: object, Intercept: object, DisplayEquation: object, DisplayRSquared: object, Name: object) -> Trendline """
        ...

    def Item(self, Index:object) -> Trendline:
        """ Item(self: Trendlines, Index: object) -> Trendline """
        ...

    def _Default(self, Index:object) -> Trendline:
        """ _Default(self: Trendlines, Index: object) -> Trendline """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class UpBars: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: UpBars) -> Application """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: UpBars) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: UpBars) -> int """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: UpBars) -> ChartFillFormat """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: UpBars) -> ChartFormat """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: UpBars) -> Interior """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: UpBars) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: UpBars) -> object """
        ...


    def Delete(self) -> object:
        """ Delete(self: UpBars) -> object """
        ...

    def Select(self) -> object:
        """ Select(self: UpBars) -> object """
        ...


class View: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: View) -> Application """
        ...

    @property
    def DisplaySlideMiniature(self): # -> MsoTriState
        """
        Get: DisplaySlideMiniature(self: View) -> MsoTriState
        Set: DisplaySlideMiniature(self: View) = value
        """
        ...

    @property
    def MediaControlsHeight(self) -> Single:
        """ Get: MediaControlsHeight(self: View) -> Single """
        ...

    @property
    def MediaControlsLeft(self) -> Single:
        """ Get: MediaControlsLeft(self: View) -> Single """
        ...

    @property
    def MediaControlsTop(self) -> Single:
        """ Get: MediaControlsTop(self: View) -> Single """
        ...

    @property
    def MediaControlsVisible(self): # -> MsoTriState
        """ Get: MediaControlsVisible(self: View) -> MsoTriState """
        ...

    @property
    def MediaControlsWidth(self) -> Single:
        """ Get: MediaControlsWidth(self: View) -> Single """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: View) -> object """
        ...

    @property
    def PrintOptions(self) -> PrintOptions:
        """ Get: PrintOptions(self: View) -> PrintOptions """
        ...

    @property
    def Slide(self) -> object:
        """
        Get: Slide(self: View) -> object
        Set: Slide(self: View) = value
        """
        ...

    @property
    def Type(self) -> PpViewType:
        """ Get: Type(self: View) -> PpViewType """
        ...

    @property
    def Zoom(self) -> int:
        """
        Get: Zoom(self: View) -> int
        Set: Zoom(self: View) = value
        """
        ...

    @property
    def ZoomToFit(self): # -> MsoTriState
        """
        Get: ZoomToFit(self: View) -> MsoTriState
        Set: ZoomToFit(self: View) = value
        """
        ...


    def GotoSlide(self, Index:int): # -> 
        """ GotoSlide(self: View, Index: int) """
        ...

    def Paste(self): # -> 
        """ Paste(self: View) """
        ...

    def PasteSpecial(self, DataType:PpPasteDataType, DisplayAsIcon, IconFileName:str, IconIndex:int, IconLabel:str, Link): # ->  # Not found arg types: {'DisplayAsIcon': 'MsoTriState', 'Link': 'MsoTriState'}
        """ PasteSpecial(self: View, DataType: PpPasteDataType, DisplayAsIcon: MsoTriState, IconFileName: str, IconIndex: int, IconLabel: str, Link: MsoTriState) """
        ...

    def Player(self, ShapeId:object) -> Player:
        """ Player(self: View, ShapeId: object) -> Player """
        ...

    def PrintOut(self, From:int, To:int, PrintToFile:str, Copies:int, Collate): # ->  # Not found arg types: {'Collate': 'MsoTriState'}
        """ PrintOut(self: View, From: int, To: int, PrintToFile: str, Copies: int, Collate: MsoTriState) """
        ...


class Walls: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Walls) -> Application """
        ...

    @property
    def Border(self) -> ChartBorder:
        """ Get: Border(self: Walls) -> ChartBorder """
        ...

    @property
    def Creator(self) -> int:
        """ Get: Creator(self: Walls) -> int """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: Walls) -> ChartFillFormat """
        ...

    @property
    def Format(self) -> ChartFormat:
        """ Get: Format(self: Walls) -> ChartFormat """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: Walls) -> Interior """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Walls) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Walls) -> object """
        ...

    @property
    def PictureType(self) -> object:
        """
        Get: PictureType(self: Walls) -> object
        Set: PictureType(self: Walls) = value
        """
        ...

    @property
    def PictureUnit(self) -> object:
        """
        Get: PictureUnit(self: Walls) -> object
        Set: PictureUnit(self: Walls) = value
        """
        ...

    @property
    def Thickness(self) -> int:
        """
        Get: Thickness(self: Walls) -> int
        Set: Thickness(self: Walls) = value
        """
        ...


    def ClearFormats(self) -> object:
        """ ClearFormats(self: Walls) -> object """
        ...

    def Paste(self): # -> 
        """ Paste(self: Walls) """
        ...

    def Select(self) -> object:
        """ Select(self: Walls) -> object """
        ...


class WebOptions: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AllowPNG(self): # -> MsoTriState
        """
        Get: AllowPNG(self: WebOptions) -> MsoTriState
        Set: AllowPNG(self: WebOptions) = value
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
    def FolderSuffix(self) -> str:
        """ Get: FolderSuffix(self: WebOptions) -> str """
        ...

    @property
    def FrameColors(self) -> PpFrameColors:
        """
        Get: FrameColors(self: WebOptions) -> PpFrameColors
        Set: FrameColors(self: WebOptions) = value
        """
        ...

    @property
    def HTMLVersion(self) -> PpHTMLVersion:
        """
        Get: HTMLVersion(self: WebOptions) -> PpHTMLVersion
        Set: HTMLVersion(self: WebOptions) = value
        """
        ...

    @property
    def IncludeNavigation(self): # -> MsoTriState
        """
        Get: IncludeNavigation(self: WebOptions) -> MsoTriState
        Set: IncludeNavigation(self: WebOptions) = value
        """
        ...

    @property
    def OrganizeInFolder(self): # -> MsoTriState
        """
        Get: OrganizeInFolder(self: WebOptions) -> MsoTriState
        Set: OrganizeInFolder(self: WebOptions) = value
        """
        ...

    @property
    def RelyOnVML(self): # -> MsoTriState
        """
        Get: RelyOnVML(self: WebOptions) -> MsoTriState
        Set: RelyOnVML(self: WebOptions) = value
        """
        ...

    @property
    def ResizeGraphics(self): # -> MsoTriState
        """
        Get: ResizeGraphics(self: WebOptions) -> MsoTriState
        Set: ResizeGraphics(self: WebOptions) = value
        """
        ...

    @property
    def ScreenSize(self): # -> MsoScreenSize
        """
        Get: ScreenSize(self: WebOptions) -> MsoScreenSize
        Set: ScreenSize(self: WebOptions) = value
        """
        ...

    @property
    def ShowSlideAnimation(self): # -> MsoTriState
        """
        Get: ShowSlideAnimation(self: WebOptions) -> MsoTriState
        Set: ShowSlideAnimation(self: WebOptions) = value
        """
        ...

    @property
    def TargetBrowser(self): # -> MsoTargetBrowser
        """
        Get: TargetBrowser(self: WebOptions) -> MsoTargetBrowser
        Set: TargetBrowser(self: WebOptions) = value
        """
        ...

    @property
    def UseLongFileNames(self): # -> MsoTriState
        """
        Get: UseLongFileNames(self: WebOptions) -> MsoTriState
        Set: UseLongFileNames(self: WebOptions) = value
        """
        ...


    def UseDefaultFolderSuffix(self): # -> 
        """ UseDefaultFolderSuffix(self: WebOptions) """
        ...


class XlAxisCrosses(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlAxisCrosses, values: xlAxisCrossesAutomatic (-4105), xlAxisCrossesCustom (-4114), xlAxisCrossesMaximum (2), xlAxisCrossesMinimum (4) """
    value__ = ...
    xlAxisCrossesAutomatic: XlAxisCrosses = ...
    xlAxisCrossesCustom: XlAxisCrosses = ...
    xlAxisCrossesMaximum: XlAxisCrosses = ...
    xlAxisCrossesMinimum: XlAxisCrosses = ...


class XlAxisGroup(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlAxisGroup, values: xlPrimary (1), xlSecondary (2) """
    value__ = ...
    xlPrimary: XlAxisGroup = ...
    xlSecondary: XlAxisGroup = ...


class XlAxisType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlAxisType, values: xlCategory (1), xlSeriesAxis (3), xlValue (2) """
    value__ = ...
    xlCategory: XlAxisType = ...
    xlSeriesAxis: XlAxisType = ...
    xlValue: XlAxisType = ...


class XlBackground(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlBackground, values: xlBackgroundAutomatic (-4105), xlBackgroundOpaque (3), xlBackgroundTransparent (2) """
    value__ = ...
    xlBackgroundAutomatic: XlBackground = ...
    xlBackgroundOpaque: XlBackground = ...
    xlBackgroundTransparent: XlBackground = ...


class XlBarShape(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlBarShape, values: xlBox (0), xlConeToMax (5), xlConeToPoint (4), xlCylinder (3), xlPyramidToMax (2), xlPyramidToPoint (1) """
    value__ = ...
    xlBox: XlBarShape = ...
    xlConeToMax: XlBarShape = ...
    xlConeToPoint: XlBarShape = ...
    xlCylinder: XlBarShape = ...
    xlPyramidToMax: XlBarShape = ...
    xlPyramidToPoint: XlBarShape = ...


class XlBorderWeight(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlBorderWeight, values: xlHairline (1), xlMedium (-4138), xlThick (4), xlThin (2) """
    value__ = ...
    xlHairline: XlBorderWeight = ...
    xlMedium: XlBorderWeight = ...
    xlThick: XlBorderWeight = ...
    xlThin: XlBorderWeight = ...


class XlCategoryLabelLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlCategoryLabelLevel, values: xlCategoryLabelLevelAll (-1), xlCategoryLabelLevelCustom (-2), xlCategoryLabelLevelNone (-3) """
    value__ = ...
    xlCategoryLabelLevelAll: XlCategoryLabelLevel = ...
    xlCategoryLabelLevelCustom: XlCategoryLabelLevel = ...
    xlCategoryLabelLevelNone: XlCategoryLabelLevel = ...


class XlCategoryType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlCategoryType, values: xlAutomaticScale (-4105), xlCategoryScale (2), xlTimeScale (3) """
    value__ = ...
    xlAutomaticScale: XlCategoryType = ...
    xlCategoryScale: XlCategoryType = ...
    xlTimeScale: XlCategoryType = ...


class XlChartElementPosition(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlChartElementPosition, values: xlChartElementPositionAutomatic (-4105), xlChartElementPositionCustom (-4114) """
    value__ = ...
    xlChartElementPositionAutomatic: XlChartElementPosition = ...
    xlChartElementPositionCustom: XlChartElementPosition = ...


class XlChartGallery(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlChartGallery, values: xlAnyGallery (23), xlBuiltIn (21), xlUserDefined (22) """
    value__ = ...
    xlAnyGallery: XlChartGallery = ...
    xlBuiltIn: XlChartGallery = ...
    xlUserDefined: XlChartGallery = ...


class XlChartItem(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlChartItem, values: xlAxis (21), xlAxisTitle (17), xlChartArea (2), xlChartTitle (4), xlCorners (6), xlDataLabel (0), xlDataTable (7), xlDisplayUnitLabel (30), xlDownBars (20), xlDropLines (26), xlErrorBars (9), xlFloor (23), xlHiLoLines (25), xlLeaderLines (29), xlLegend (24), xlLegendEntry (12), xlLegendKey (13), xlMajorGridlines (15), xlMinorGridlines (16), xlNothing (28), xlPivotChartDropZone (32), xlPivotChartFieldButton (31), xlPlotArea (19), xlRadarAxisLabels (27), xlSeries (3), xlSeriesLines (22), xlShape (14), xlTrendline (8), xlUpBars (18), xlWalls (5), xlXErrorBars (10), xlYErrorBars (11) """
    value__ = ...
    xlAxis: XlChartItem = ...
    xlAxisTitle: XlChartItem = ...
    xlChartArea: XlChartItem = ...
    xlChartTitle: XlChartItem = ...
    xlCorners: XlChartItem = ...
    xlDataLabel: XlChartItem = ...
    xlDataTable: XlChartItem = ...
    xlDisplayUnitLabel: XlChartItem = ...
    xlDownBars: XlChartItem = ...
    xlDropLines: XlChartItem = ...
    xlErrorBars: XlChartItem = ...
    xlFloor: XlChartItem = ...
    xlHiLoLines: XlChartItem = ...
    xlLeaderLines: XlChartItem = ...
    xlLegend: XlChartItem = ...
    xlLegendEntry: XlChartItem = ...
    xlLegendKey: XlChartItem = ...
    xlMajorGridlines: XlChartItem = ...
    xlMinorGridlines: XlChartItem = ...
    xlNothing: XlChartItem = ...
    xlPivotChartDropZone: XlChartItem = ...
    xlPivotChartFieldButton: XlChartItem = ...
    xlPlotArea: XlChartItem = ...
    xlRadarAxisLabels: XlChartItem = ...
    xlSeries: XlChartItem = ...
    xlSeriesLines: XlChartItem = ...
    xlShape: XlChartItem = ...
    xlTrendline: XlChartItem = ...
    xlUpBars: XlChartItem = ...
    xlWalls: XlChartItem = ...
    xlXErrorBars: XlChartItem = ...
    xlYErrorBars: XlChartItem = ...


class XlChartPicturePlacement(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlChartPicturePlacement, values: xlAllFaces (7), xlEnd (2), xlEndSides (3), xlFront (4), xlFrontEnd (6), xlFrontSides (5), xlSides (1) """
    value__ = ...
    xlAllFaces: XlChartPicturePlacement = ...
    xlEnd: XlChartPicturePlacement = ...
    xlEndSides: XlChartPicturePlacement = ...
    xlFront: XlChartPicturePlacement = ...
    xlFrontEnd: XlChartPicturePlacement = ...
    xlFrontSides: XlChartPicturePlacement = ...
    xlSides: XlChartPicturePlacement = ...


class XlChartPictureType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlChartPictureType, values: xlStack (2), xlStackScale (3), xlStretch (1) """
    value__ = ...
    xlStack: XlChartPictureType = ...
    xlStackScale: XlChartPictureType = ...
    xlStretch: XlChartPictureType = ...


class XlChartSplitType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlChartSplitType, values: xlSplitByCustomSplit (4), xlSplitByPercentValue (3), xlSplitByPosition (1), xlSplitByValue (2) """
    value__ = ...
    xlSplitByCustomSplit: XlChartSplitType = ...
    xlSplitByPercentValue: XlChartSplitType = ...
    xlSplitByPosition: XlChartSplitType = ...
    xlSplitByValue: XlChartSplitType = ...


class XlColorIndex(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlColorIndex, values: xlColorIndexAutomatic (-4105), xlColorIndexNone (-4142) """
    value__ = ...
    xlColorIndexAutomatic: XlColorIndex = ...
    xlColorIndexNone: XlColorIndex = ...


class XlConstants(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlConstants, values: xl3DBar (-4099), xl3DSurface (-4103), xlAbove (0), xlAutomatic (-4105), xlBar (2), xlBelow (1), xlBoth (1), xlBottom (-4107), xlCenter (-4108), xlChecker (9), xlCircle (8), xlColumn (3), xlCombination (-4111), xlCorner (2), xlCrissCross (16), xlCross (4), xlCustom (-4114), xlDefaultAutoFormat (-1), xlDiamond (2), xlDistributed (-4117), xlFill (5), xlFixedValue (1), xlGeneral (1), xlGray16 (17), xlGray25 (-4124), xlGray50 (-4125), xlGray75 (-4126), xlGray8 (18), xlGrid (15), xlHigh (-4127), xlInside (2), xlJustify (-4130), xlLeft (-4131), xlLightDown (13), xlLightHorizontal (11), xlLightUp (14), xlLightVertical (12), xlLow (-4134), xlMaximum (2), xlMinimum (4), xlMinusValues (3), xlNextToAxis (4), xlNone (-4142), xlOpaque (3), xlOutside (3), xlPercent (2), xlPlus (9), xlPlusValues (2), xlRight (-4152), xlScale (3), xlSemiGray75 (10), xlShowLabel (4), xlShowLabelAndPercent (5), xlShowPercent (3), xlShowValue (2), xlSingle (2), xlSolid (1), xlSquare (1), xlStar (5), xlStError (4), xlTop (-4160), xlTransparent (2), xlTriangle (3) """
    value__ = ...
    xl3DBar: XlConstants = ...
    xl3DSurface: XlConstants = ...
    xlAbove: XlConstants = ...
    xlAutomatic: XlConstants = ...
    xlBar: XlConstants = ...
    xlBelow: XlConstants = ...
    xlBoth: XlConstants = ...
    xlBottom: XlConstants = ...
    xlCenter: XlConstants = ...
    xlChecker: XlConstants = ...
    xlCircle: XlConstants = ...
    xlColumn: XlConstants = ...
    xlCombination: XlConstants = ...
    xlCorner: XlConstants = ...
    xlCrissCross: XlConstants = ...
    xlCross: XlConstants = ...
    xlCustom: XlConstants = ...
    xlDefaultAutoFormat: XlConstants = ...
    xlDiamond: XlConstants = ...
    xlDistributed: XlConstants = ...
    xlFill: XlConstants = ...
    xlFixedValue: XlConstants = ...
    xlGeneral: XlConstants = ...
    xlGray16: XlConstants = ...
    xlGray25: XlConstants = ...
    xlGray50: XlConstants = ...
    xlGray75: XlConstants = ...
    xlGray8: XlConstants = ...
    xlGrid: XlConstants = ...
    xlHigh: XlConstants = ...
    xlInside: XlConstants = ...
    xlJustify: XlConstants = ...
    xlLeft: XlConstants = ...
    xlLightDown: XlConstants = ...
    xlLightHorizontal: XlConstants = ...
    xlLightUp: XlConstants = ...
    xlLightVertical: XlConstants = ...
    xlLow: XlConstants = ...
    xlMaximum: XlConstants = ...
    xlMinimum: XlConstants = ...
    xlMinusValues: XlConstants = ...
    xlNextToAxis: XlConstants = ...
    xlNone: XlConstants = ...
    xlOpaque: XlConstants = ...
    xlOutside: XlConstants = ...
    xlPercent: XlConstants = ...
    xlPlus: XlConstants = ...
    xlPlusValues: XlConstants = ...
    xlRight: XlConstants = ...
    xlScale: XlConstants = ...
    xlSemiGray75: XlConstants = ...
    xlShowLabel: XlConstants = ...
    xlShowLabelAndPercent: XlConstants = ...
    xlShowPercent: XlConstants = ...
    xlShowValue: XlConstants = ...
    xlSingle: XlConstants = ...
    xlSolid: XlConstants = ...
    xlSquare: XlConstants = ...
    xlStar: XlConstants = ...
    xlStError: XlConstants = ...
    xlTop: XlConstants = ...
    xlTransparent: XlConstants = ...
    xlTriangle: XlConstants = ...


class XlCopyPictureFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlCopyPictureFormat, values: xlBitmap (2), xlPicture (-4147) """
    value__ = ...
    xlBitmap: XlCopyPictureFormat = ...
    xlPicture: XlCopyPictureFormat = ...


class XlDataLabelPosition(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlDataLabelPosition, values: xlLabelPositionAbove (0), xlLabelPositionBelow (1), xlLabelPositionBestFit (5), xlLabelPositionCenter (-4108), xlLabelPositionCustom (7), xlLabelPositionInsideBase (4), xlLabelPositionInsideEnd (3), xlLabelPositionLeft (-4131), xlLabelPositionMixed (6), xlLabelPositionOutsideEnd (2), xlLabelPositionRight (-4152) """
    value__ = ...
    xlLabelPositionAbove: XlDataLabelPosition = ...
    xlLabelPositionBelow: XlDataLabelPosition = ...
    xlLabelPositionBestFit: XlDataLabelPosition = ...
    xlLabelPositionCenter: XlDataLabelPosition = ...
    xlLabelPositionCustom: XlDataLabelPosition = ...
    xlLabelPositionInsideBase: XlDataLabelPosition = ...
    xlLabelPositionInsideEnd: XlDataLabelPosition = ...
    xlLabelPositionLeft: XlDataLabelPosition = ...
    xlLabelPositionMixed: XlDataLabelPosition = ...
    xlLabelPositionOutsideEnd: XlDataLabelPosition = ...
    xlLabelPositionRight: XlDataLabelPosition = ...


class XlDataLabelSeparator(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlDataLabelSeparator, values: xlDataLabelSeparatorDefault (1) """
    value__ = ...
    xlDataLabelSeparatorDefault: XlDataLabelSeparator = ...


class XlDataLabelsType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlDataLabelsType, values: xlDataLabelsShowBubbleSizes (6), xlDataLabelsShowLabel (4), xlDataLabelsShowLabelAndPercent (5), xlDataLabelsShowNone (-4142), xlDataLabelsShowPercent (3), xlDataLabelsShowValue (2) """
    value__ = ...
    xlDataLabelsShowBubbleSizes: XlDataLabelsType = ...
    xlDataLabelsShowLabel: XlDataLabelsType = ...
    xlDataLabelsShowLabelAndPercent: XlDataLabelsType = ...
    xlDataLabelsShowNone: XlDataLabelsType = ...
    xlDataLabelsShowPercent: XlDataLabelsType = ...
    xlDataLabelsShowValue: XlDataLabelsType = ...


class XlDisplayBlanksAs(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlDisplayBlanksAs, values: xlInterpolated (3), xlNotPlotted (1), xlZero (2) """
    value__ = ...
    xlInterpolated: XlDisplayBlanksAs = ...
    xlNotPlotted: XlDisplayBlanksAs = ...
    xlZero: XlDisplayBlanksAs = ...


class XlDisplayUnit(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlDisplayUnit, values: xlHundredMillions (-8), xlHundreds (-2), xlHundredThousands (-5), xlMillionMillions (-10), xlMillions (-6), xlTenMillions (-7), xlTenThousands (-4), xlThousandMillions (-9), xlThousands (-3) """
    value__ = ...
    xlHundredMillions: XlDisplayUnit = ...
    xlHundreds: XlDisplayUnit = ...
    xlHundredThousands: XlDisplayUnit = ...
    xlMillionMillions: XlDisplayUnit = ...
    xlMillions: XlDisplayUnit = ...
    xlTenMillions: XlDisplayUnit = ...
    xlTenThousands: XlDisplayUnit = ...
    xlThousandMillions: XlDisplayUnit = ...
    xlThousands: XlDisplayUnit = ...


class XlEndStyleCap(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlEndStyleCap, values: xlCap (1), xlNoCap (2) """
    value__ = ...
    xlCap: XlEndStyleCap = ...
    xlNoCap: XlEndStyleCap = ...


class XlErrorBarDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlErrorBarDirection, values: xlChartX (-4168), xlChartY (1) """
    value__ = ...
    xlChartX: XlErrorBarDirection = ...
    xlChartY: XlErrorBarDirection = ...


class XlErrorBarInclude(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlErrorBarInclude, values: xlErrorBarIncludeBoth (1), xlErrorBarIncludeMinusValues (3), xlErrorBarIncludeNone (-4142), xlErrorBarIncludePlusValues (2) """
    value__ = ...
    xlErrorBarIncludeBoth: XlErrorBarInclude = ...
    xlErrorBarIncludeMinusValues: XlErrorBarInclude = ...
    xlErrorBarIncludeNone: XlErrorBarInclude = ...
    xlErrorBarIncludePlusValues: XlErrorBarInclude = ...


class XlErrorBarType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlErrorBarType, values: xlErrorBarTypeCustom (-4114), xlErrorBarTypeFixedValue (1), xlErrorBarTypePercent (2), xlErrorBarTypeStDev (-4155), xlErrorBarTypeStError (4) """
    value__ = ...
    xlErrorBarTypeCustom: XlErrorBarType = ...
    xlErrorBarTypeFixedValue: XlErrorBarType = ...
    xlErrorBarTypePercent: XlErrorBarType = ...
    xlErrorBarTypeStDev: XlErrorBarType = ...
    xlErrorBarTypeStError: XlErrorBarType = ...


class XlHAlign(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlHAlign, values: xlHAlignCenter (-4108), xlHAlignCenterAcrossSelection (7), xlHAlignDistributed (-4117), xlHAlignFill (5), xlHAlignGeneral (1), xlHAlignJustify (-4130), xlHAlignLeft (-4131), xlHAlignRight (-4152) """
    value__ = ...
    xlHAlignCenter: XlHAlign = ...
    xlHAlignCenterAcrossSelection: XlHAlign = ...
    xlHAlignDistributed: XlHAlign = ...
    xlHAlignFill: XlHAlign = ...
    xlHAlignGeneral: XlHAlign = ...
    xlHAlignJustify: XlHAlign = ...
    xlHAlignLeft: XlHAlign = ...
    xlHAlignRight: XlHAlign = ...


class XlLegendPosition(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlLegendPosition, values: xlLegendPositionBottom (-4107), xlLegendPositionCorner (2), xlLegendPositionCustom (-4161), xlLegendPositionLeft (-4131), xlLegendPositionRight (-4152), xlLegendPositionTop (-4160) """
    value__ = ...
    xlLegendPositionBottom: XlLegendPosition = ...
    xlLegendPositionCorner: XlLegendPosition = ...
    xlLegendPositionCustom: XlLegendPosition = ...
    xlLegendPositionLeft: XlLegendPosition = ...
    xlLegendPositionRight: XlLegendPosition = ...
    xlLegendPositionTop: XlLegendPosition = ...


class XlLineStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlLineStyle, values: xlContinuous (1), xlDash (-4115), xlDashDot (4), xlDashDotDot (5), xlDot (-4118), xlDouble (-4119), xlLineStyleNone (-4142), xlSlantDashDot (13) """
    value__ = ...
    xlContinuous: XlLineStyle = ...
    xlDash: XlLineStyle = ...
    xlDashDot: XlLineStyle = ...
    xlDashDotDot: XlLineStyle = ...
    xlDot: XlLineStyle = ...
    xlDouble: XlLineStyle = ...
    xlLineStyleNone: XlLineStyle = ...
    xlSlantDashDot: XlLineStyle = ...


class XlMarkerStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlMarkerStyle, values: xlMarkerStyleAutomatic (-4105), xlMarkerStyleCircle (8), xlMarkerStyleDash (-4115), xlMarkerStyleDiamond (2), xlMarkerStyleDot (-4118), xlMarkerStyleNone (-4142), xlMarkerStylePicture (-4147), xlMarkerStylePlus (9), xlMarkerStyleSquare (1), xlMarkerStyleStar (5), xlMarkerStyleTriangle (3), xlMarkerStyleX (-4168) """
    value__ = ...
    xlMarkerStyleAutomatic: XlMarkerStyle = ...
    xlMarkerStyleCircle: XlMarkerStyle = ...
    xlMarkerStyleDash: XlMarkerStyle = ...
    xlMarkerStyleDiamond: XlMarkerStyle = ...
    xlMarkerStyleDot: XlMarkerStyle = ...
    xlMarkerStyleNone: XlMarkerStyle = ...
    xlMarkerStylePicture: XlMarkerStyle = ...
    xlMarkerStylePlus: XlMarkerStyle = ...
    xlMarkerStyleSquare: XlMarkerStyle = ...
    xlMarkerStyleStar: XlMarkerStyle = ...
    xlMarkerStyleTriangle: XlMarkerStyle = ...
    xlMarkerStyleX: XlMarkerStyle = ...


class XlOrientation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlOrientation, values: xlDownward (-4170), xlHorizontal (-4128), xlUpward (-4171), xlVertical (-4166) """
    value__ = ...
    xlDownward: XlOrientation = ...
    xlHorizontal: XlOrientation = ...
    xlUpward: XlOrientation = ...
    xlVertical: XlOrientation = ...


class XlPattern(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlPattern, values: xlPatternAutomatic (-4105), xlPatternChecker (9), xlPatternCrissCross (16), xlPatternDown (-4121), xlPatternGray16 (17), xlPatternGray25 (-4124), xlPatternGray50 (-4125), xlPatternGray75 (-4126), xlPatternGray8 (18), xlPatternGrid (15), xlPatternHorizontal (-4128), xlPatternLightDown (13), xlPatternLightHorizontal (11), xlPatternLightUp (14), xlPatternLightVertical (12), xlPatternLinearGradient (4000), xlPatternNone (-4142), xlPatternRectangularGradient (4001), xlPatternSemiGray75 (10), xlPatternSolid (1), xlPatternUp (-4162), xlPatternVertical (-4166) """
    value__ = ...
    xlPatternAutomatic: XlPattern = ...
    xlPatternChecker: XlPattern = ...
    xlPatternCrissCross: XlPattern = ...
    xlPatternDown: XlPattern = ...
    xlPatternGray16: XlPattern = ...
    xlPatternGray25: XlPattern = ...
    xlPatternGray50: XlPattern = ...
    xlPatternGray75: XlPattern = ...
    xlPatternGray8: XlPattern = ...
    xlPatternGrid: XlPattern = ...
    xlPatternHorizontal: XlPattern = ...
    xlPatternLightDown: XlPattern = ...
    xlPatternLightHorizontal: XlPattern = ...
    xlPatternLightUp: XlPattern = ...
    xlPatternLightVertical: XlPattern = ...
    xlPatternLinearGradient: XlPattern = ...
    xlPatternNone: XlPattern = ...
    xlPatternRectangularGradient: XlPattern = ...
    xlPatternSemiGray75: XlPattern = ...
    xlPatternSolid: XlPattern = ...
    xlPatternUp: XlPattern = ...
    xlPatternVertical: XlPattern = ...


class XlPictureAppearance(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlPictureAppearance, values: xlPrinter (2), xlScreen (1) """
    value__ = ...
    xlPrinter: XlPictureAppearance = ...
    xlScreen: XlPictureAppearance = ...


class XlPieSliceIndex(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlPieSliceIndex, values: xlCenterPoint (5), xlInnerCenterPoint (8), xlInnerClockwisePoint (7), xlInnerCounterClockwisePoint (9), xlMidClockwiseRadiusPoint (4), xlMidCounterClockwiseRadiusPoint (6), xlOuterCenterPoint (2), xlOuterClockwisePoint (3), xlOuterCounterClockwisePoint (1) """
    value__ = ...
    xlCenterPoint: XlPieSliceIndex = ...
    xlInnerCenterPoint: XlPieSliceIndex = ...
    xlInnerClockwisePoint: XlPieSliceIndex = ...
    xlInnerCounterClockwisePoint: XlPieSliceIndex = ...
    xlMidClockwiseRadiusPoint: XlPieSliceIndex = ...
    xlMidCounterClockwiseRadiusPoint: XlPieSliceIndex = ...
    xlOuterCenterPoint: XlPieSliceIndex = ...
    xlOuterClockwisePoint: XlPieSliceIndex = ...
    xlOuterCounterClockwisePoint: XlPieSliceIndex = ...


class XlPieSliceLocation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlPieSliceLocation, values: xlHorizontalCoordinate (1), xlVerticalCoordinate (2) """
    value__ = ...
    xlHorizontalCoordinate: XlPieSliceLocation = ...
    xlVerticalCoordinate: XlPieSliceLocation = ...


class XlPivotFieldOrientation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlPivotFieldOrientation, values: xlColumnField (2), xlDataField (4), xlHidden (0), xlPageField (3), xlRowField (1) """
    value__ = ...
    xlColumnField: XlPivotFieldOrientation = ...
    xlDataField: XlPivotFieldOrientation = ...
    xlHidden: XlPivotFieldOrientation = ...
    xlPageField: XlPivotFieldOrientation = ...
    xlRowField: XlPivotFieldOrientation = ...


class XlReadingOrder(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlReadingOrder, values: xlContext (-5002), xlLTR (-5003), xlRTL (-5004) """
    value__ = ...
    xlContext: XlReadingOrder = ...
    xlLTR: XlReadingOrder = ...
    xlRTL: XlReadingOrder = ...


class XlRgbColor(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlRgbColor, values: rgbAliceBlue (16775408), rgbAntiqueWhite (14150650), rgbAqua (16776960), rgbAquamarine (13959039), rgbAzure (16777200), rgbBeige (14480885), rgbBisque (12903679), rgbBlack (0), rgbBlanchedAlmond (13495295), rgbBlue (16711680), rgbBlueViolet (14822282), rgbBrown (2763429), rgbBurlyWood (8894686), rgbCadetBlue (10526303), rgbChartreuse (65407), rgbCoral (5275647), rgbCornflowerBlue (15570276), rgbCornsilk (14481663), rgbCrimson (3937500), rgbDarkBlue (9109504), rgbDarkCyan (9145088), rgbDarkGoldenrod (755384), rgbDarkGray (11119017), rgbDarkGreen (25600), rgbDarkGrey (11119017), rgbDarkKhaki (7059389), rgbDarkMagenta (9109643), rgbDarkOliveGreen (3107669), rgbDarkOrange (36095), rgbDarkOrchid (13382297), rgbDarkRed (139), rgbDarkSalmon (8034025), rgbDarkSeaGreen (9419919), rgbDarkSlateBlue (9125192), rgbDarkSlateGray (5197615), rgbDarkSlateGrey (5197615), rgbDarkTurquoise (13749760), rgbDarkViolet (13828244), rgbDeepPink (9639167), rgbDeepSkyBlue (16760576), rgbDimGray (6908265), rgbDimGrey (6908265), rgbDodgerBlue (16748574), rgbFireBrick (2237106), rgbFloralWhite (15792895), rgbForestGreen (2263842), rgbFuchsia (16711935), rgbGainsboro (14474460), rgbGhostWhite (16775416), rgbGold (55295), rgbGoldenrod (2139610), rgbGray (8421504), rgbGreen (32768), rgbGreenYellow (3145645), rgbGrey (8421504), rgbHoneydew (15794160), rgbHotPink (11823615), rgbIndianRed (6053069), rgbIndigo (8519755), rgbIvory (15794175), rgbKhaki (9234160), rgbLavender (16443110), rgbLavenderBlush (16118015), rgbLawnGreen (64636), rgbLemonChiffon (13499135), rgbLightBlue (15128749), rgbLightCoral (8421616), rgbLightCyan (9145088), rgbLightGoldenrodYellow (13826810), rgbLightGray (13882323), rgbLightGreen (9498256), rgbLightGrey (13882323), rgbLightPink (12695295), rgbLightSalmon (8036607), rgbLightSeaGreen (11186720), rgbLightSkyBlue (16436871), rgbLightSlateGray (10061943), rgbLightSlateGrey (10061943), rgbLightSteelBlue (14599344), rgbLightYellow (14745599), rgbLime (65280), rgbLimeGreen (3329330), rgbLinen (15134970), rgbMaroon (128), rgbMediumAquamarine (11206502), rgbMediumBlue (13434880), rgbMediumOrchid (13850042), rgbMediumPurple (14381203), rgbMediumSeaGreen (7451452), rgbMediumSlateBlue (15624315), rgbMediumSpringGreen (10156544), rgbMediumTurquoise (13422920), rgbMediumVioletRed (8721863), rgbMidnightBlue (7346457), rgbMintCream (16449525), rgbMistyRose (14804223), rgbMoccasin (11920639), rgbNavajoWhite (11394815), rgbNavy (8388608), rgbNavyBlue (8388608), rgbOldLace (15136253), rgbOlive (32896), rgbOliveDrab (2330219), rgbOrange (42495), rgbOrangeRed (17919), rgbOrchid (14053594), rgbPaleGoldenrod (7071982), rgbPaleGreen (10025880), rgbPaleTurquoise (15658671), rgbPaleVioletRed (9662683), rgbPapayaWhip (14020607), rgbPeachPuff (12180223), rgbPeru (4163021), rgbPink (13353215), rgbPlum (14524637), rgbPowderBlue (15130800), rgbPurple (8388736), rgbRed (255), rgbRosyBrown (9408444), rgbRoyalBlue (14772545), rgbSalmon (7504122), rgbSandyBrown (6333684), rgbSeaGreen (5737262), rgbSeashell (15660543), rgbSienna (2970272), rgbSilver (12632256), rgbSkyBlue (15453831), rgbSlateBlue (13458026), rgbSlateGray (9470064), rgbSlateGrey (9470064), rgbSnow (16448255), rgbSpringGreen (8388352), rgbSteelBlue (11829830), rgbTan (9221330), rgbTeal (8421376), rgbThistle (14204888), rgbTomato (4678655), rgbTurquoise (13688896), rgbViolet (15631086), rgbWheat (11788021), rgbWhite (16777215), rgbWhiteSmoke (16119285), rgbYellow (65535), rgbYellowGreen (3329434) """
    rgbAliceBlue: XlRgbColor = ...
    rgbAntiqueWhite: XlRgbColor = ...
    rgbAqua: XlRgbColor = ...
    rgbAquamarine: XlRgbColor = ...
    rgbAzure: XlRgbColor = ...
    rgbBeige: XlRgbColor = ...
    rgbBisque: XlRgbColor = ...
    rgbBlack: XlRgbColor = ...
    rgbBlanchedAlmond: XlRgbColor = ...
    rgbBlue: XlRgbColor = ...
    rgbBlueViolet: XlRgbColor = ...
    rgbBrown: XlRgbColor = ...
    rgbBurlyWood: XlRgbColor = ...
    rgbCadetBlue: XlRgbColor = ...
    rgbChartreuse: XlRgbColor = ...
    rgbCoral: XlRgbColor = ...
    rgbCornflowerBlue: XlRgbColor = ...
    rgbCornsilk: XlRgbColor = ...
    rgbCrimson: XlRgbColor = ...
    rgbDarkBlue: XlRgbColor = ...
    rgbDarkCyan: XlRgbColor = ...
    rgbDarkGoldenrod: XlRgbColor = ...
    rgbDarkGray: XlRgbColor = ...
    rgbDarkGreen: XlRgbColor = ...
    rgbDarkGrey: XlRgbColor = ...
    rgbDarkKhaki: XlRgbColor = ...
    rgbDarkMagenta: XlRgbColor = ...
    rgbDarkOliveGreen: XlRgbColor = ...
    rgbDarkOrange: XlRgbColor = ...
    rgbDarkOrchid: XlRgbColor = ...
    rgbDarkRed: XlRgbColor = ...
    rgbDarkSalmon: XlRgbColor = ...
    rgbDarkSeaGreen: XlRgbColor = ...
    rgbDarkSlateBlue: XlRgbColor = ...
    rgbDarkSlateGray: XlRgbColor = ...
    rgbDarkSlateGrey: XlRgbColor = ...
    rgbDarkTurquoise: XlRgbColor = ...
    rgbDarkViolet: XlRgbColor = ...
    rgbDeepPink: XlRgbColor = ...
    rgbDeepSkyBlue: XlRgbColor = ...
    rgbDimGray: XlRgbColor = ...
    rgbDimGrey: XlRgbColor = ...
    rgbDodgerBlue: XlRgbColor = ...
    rgbFireBrick: XlRgbColor = ...
    rgbFloralWhite: XlRgbColor = ...
    rgbForestGreen: XlRgbColor = ...
    rgbFuchsia: XlRgbColor = ...
    rgbGainsboro: XlRgbColor = ...
    rgbGhostWhite: XlRgbColor = ...
    rgbGold: XlRgbColor = ...
    rgbGoldenrod: XlRgbColor = ...
    rgbGray: XlRgbColor = ...
    rgbGreen: XlRgbColor = ...
    rgbGreenYellow: XlRgbColor = ...
    rgbGrey: XlRgbColor = ...
    rgbHoneydew: XlRgbColor = ...
    rgbHotPink: XlRgbColor = ...
    rgbIndianRed: XlRgbColor = ...
    rgbIndigo: XlRgbColor = ...
    rgbIvory: XlRgbColor = ...
    rgbKhaki: XlRgbColor = ...
    rgbLavender: XlRgbColor = ...
    rgbLavenderBlush: XlRgbColor = ...
    rgbLawnGreen: XlRgbColor = ...
    rgbLemonChiffon: XlRgbColor = ...
    rgbLightBlue: XlRgbColor = ...
    rgbLightCoral: XlRgbColor = ...
    rgbLightCyan: XlRgbColor = ...
    rgbLightGoldenrodYellow: XlRgbColor = ...
    rgbLightGray: XlRgbColor = ...
    rgbLightGreen: XlRgbColor = ...
    rgbLightGrey: XlRgbColor = ...
    rgbLightPink: XlRgbColor = ...
    rgbLightSalmon: XlRgbColor = ...
    rgbLightSeaGreen: XlRgbColor = ...
    rgbLightSkyBlue: XlRgbColor = ...
    rgbLightSlateGray: XlRgbColor = ...
    rgbLightSlateGrey: XlRgbColor = ...
    rgbLightSteelBlue: XlRgbColor = ...
    rgbLightYellow: XlRgbColor = ...
    rgbLime: XlRgbColor = ...
    rgbLimeGreen: XlRgbColor = ...
    rgbLinen: XlRgbColor = ...
    rgbMaroon: XlRgbColor = ...
    rgbMediumAquamarine: XlRgbColor = ...
    rgbMediumBlue: XlRgbColor = ...
    rgbMediumOrchid: XlRgbColor = ...
    rgbMediumPurple: XlRgbColor = ...
    rgbMediumSeaGreen: XlRgbColor = ...
    rgbMediumSlateBlue: XlRgbColor = ...
    rgbMediumSpringGreen: XlRgbColor = ...
    rgbMediumTurquoise: XlRgbColor = ...
    rgbMediumVioletRed: XlRgbColor = ...
    rgbMidnightBlue: XlRgbColor = ...
    rgbMintCream: XlRgbColor = ...
    rgbMistyRose: XlRgbColor = ...
    rgbMoccasin: XlRgbColor = ...
    rgbNavajoWhite: XlRgbColor = ...
    rgbNavy: XlRgbColor = ...
    rgbNavyBlue: XlRgbColor = ...
    rgbOldLace: XlRgbColor = ...
    rgbOlive: XlRgbColor = ...
    rgbOliveDrab: XlRgbColor = ...
    rgbOrange: XlRgbColor = ...
    rgbOrangeRed: XlRgbColor = ...
    rgbOrchid: XlRgbColor = ...
    rgbPaleGoldenrod: XlRgbColor = ...
    rgbPaleGreen: XlRgbColor = ...
    rgbPaleTurquoise: XlRgbColor = ...
    rgbPaleVioletRed: XlRgbColor = ...
    rgbPapayaWhip: XlRgbColor = ...
    rgbPeachPuff: XlRgbColor = ...
    rgbPeru: XlRgbColor = ...
    rgbPink: XlRgbColor = ...
    rgbPlum: XlRgbColor = ...
    rgbPowderBlue: XlRgbColor = ...
    rgbPurple: XlRgbColor = ...
    rgbRed: XlRgbColor = ...
    rgbRosyBrown: XlRgbColor = ...
    rgbRoyalBlue: XlRgbColor = ...
    rgbSalmon: XlRgbColor = ...
    rgbSandyBrown: XlRgbColor = ...
    rgbSeaGreen: XlRgbColor = ...
    rgbSeashell: XlRgbColor = ...
    rgbSienna: XlRgbColor = ...
    rgbSilver: XlRgbColor = ...
    rgbSkyBlue: XlRgbColor = ...
    rgbSlateBlue: XlRgbColor = ...
    rgbSlateGray: XlRgbColor = ...
    rgbSlateGrey: XlRgbColor = ...
    rgbSnow: XlRgbColor = ...
    rgbSpringGreen: XlRgbColor = ...
    rgbSteelBlue: XlRgbColor = ...
    rgbTan: XlRgbColor = ...
    rgbTeal: XlRgbColor = ...
    rgbThistle: XlRgbColor = ...
    rgbTomato: XlRgbColor = ...
    rgbTurquoise: XlRgbColor = ...
    rgbViolet: XlRgbColor = ...
    rgbWheat: XlRgbColor = ...
    rgbWhite: XlRgbColor = ...
    rgbWhiteSmoke: XlRgbColor = ...
    rgbYellow: XlRgbColor = ...
    rgbYellowGreen: XlRgbColor = ...
    value__ = ...


class XlRowCol(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlRowCol, values: xlColumns (2), xlRows (1) """
    value__ = ...
    xlColumns: XlRowCol = ...
    xlRows: XlRowCol = ...


class XlScaleType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlScaleType, values: xlScaleLinear (-4132), xlScaleLogarithmic (-4133) """
    value__ = ...
    xlScaleLinear: XlScaleType = ...
    xlScaleLogarithmic: XlScaleType = ...


class XlSeriesNameLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlSeriesNameLevel, values: xlSeriesNameLevelAll (-1), xlSeriesNameLevelCustom (-2), xlSeriesNameLevelNone (-3) """
    value__ = ...
    xlSeriesNameLevelAll: XlSeriesNameLevel = ...
    xlSeriesNameLevelCustom: XlSeriesNameLevel = ...
    xlSeriesNameLevelNone: XlSeriesNameLevel = ...


class XlSizeRepresents(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlSizeRepresents, values: xlSizeIsArea (1), xlSizeIsWidth (2) """
    value__ = ...
    xlSizeIsArea: XlSizeRepresents = ...
    xlSizeIsWidth: XlSizeRepresents = ...


class XlTickLabelOrientation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlTickLabelOrientation, values: xlTickLabelOrientationAutomatic (-4105), xlTickLabelOrientationDownward (-4170), xlTickLabelOrientationHorizontal (-4128), xlTickLabelOrientationUpward (-4171), xlTickLabelOrientationVertical (-4166) """
    value__ = ...
    xlTickLabelOrientationAutomatic: XlTickLabelOrientation = ...
    xlTickLabelOrientationDownward: XlTickLabelOrientation = ...
    xlTickLabelOrientationHorizontal: XlTickLabelOrientation = ...
    xlTickLabelOrientationUpward: XlTickLabelOrientation = ...
    xlTickLabelOrientationVertical: XlTickLabelOrientation = ...


class XlTickLabelPosition(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlTickLabelPosition, values: xlTickLabelPositionHigh (-4127), xlTickLabelPositionLow (-4134), xlTickLabelPositionNextToAxis (4), xlTickLabelPositionNone (-4142) """
    value__ = ...
    xlTickLabelPositionHigh: XlTickLabelPosition = ...
    xlTickLabelPositionLow: XlTickLabelPosition = ...
    xlTickLabelPositionNextToAxis: XlTickLabelPosition = ...
    xlTickLabelPositionNone: XlTickLabelPosition = ...


class XlTickMark(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlTickMark, values: xlTickMarkCross (4), xlTickMarkInside (2), xlTickMarkNone (-4142), xlTickMarkOutside (3) """
    value__ = ...
    xlTickMarkCross: XlTickMark = ...
    xlTickMarkInside: XlTickMark = ...
    xlTickMarkNone: XlTickMark = ...
    xlTickMarkOutside: XlTickMark = ...


class XlTimeUnit(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlTimeUnit, values: xlDays (0), xlMonths (1), xlYears (2) """
    value__ = ...
    xlDays: XlTimeUnit = ...
    xlMonths: XlTimeUnit = ...
    xlYears: XlTimeUnit = ...


class XlTrendlineType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlTrendlineType, values: xlExponential (5), xlLinear (-4132), xlLogarithmic (-4133), xlMovingAvg (6), xlPolynomial (3), xlPower (4) """
    value__ = ...
    xlExponential: XlTrendlineType = ...
    xlLinear: XlTrendlineType = ...
    xlLogarithmic: XlTrendlineType = ...
    xlMovingAvg: XlTrendlineType = ...
    xlPolynomial: XlTrendlineType = ...
    xlPower: XlTrendlineType = ...


class XlUnderlineStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlUnderlineStyle, values: xlUnderlineStyleDouble (-4119), xlUnderlineStyleDoubleAccounting (5), xlUnderlineStyleNone (-4142), xlUnderlineStyleSingle (2), xlUnderlineStyleSingleAccounting (4) """
    value__ = ...
    xlUnderlineStyleDouble: XlUnderlineStyle = ...
    xlUnderlineStyleDoubleAccounting: XlUnderlineStyle = ...
    xlUnderlineStyleNone: XlUnderlineStyle = ...
    xlUnderlineStyleSingle: XlUnderlineStyle = ...
    xlUnderlineStyleSingleAccounting: XlUnderlineStyle = ...


class XlVAlign(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlVAlign, values: xlVAlignBottom (-4107), xlVAlignCenter (-4108), xlVAlignDistributed (-4117), xlVAlignJustify (-4130), xlVAlignTop (-4160) """
    value__ = ...
    xlVAlignBottom: XlVAlign = ...
    xlVAlignCenter: XlVAlign = ...
    xlVAlignDistributed: XlVAlign = ...
    xlVAlignJustify: XlVAlign = ...
    xlVAlignTop: XlVAlign = ...


