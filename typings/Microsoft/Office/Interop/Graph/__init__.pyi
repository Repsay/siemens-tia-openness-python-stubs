# encoding: utf-8
# module Microsoft.Office.Interop.Graph calls itself Graph
# from Microsoft.Office.Interop.Graph, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualStudio.CommandBars import CommandBars

from System import Enum, Single

from System.Collections import IEnumerable

"""The following names are not found in the module: (MsoFillType, 
    MsoGradientColorType, MsoGradientStyle, MsoPatternType, 
    MsoPresetGradientType, MsoPresetTexture, MsoTextureType, MsoTriState, 
    __ComObject, field#)
"""

# no functions
# classes

class Application: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Application) -> Application """
        ...

    @property
    def AutoCorrect(self) -> AutoCorrect:
        """ Get: AutoCorrect(self: Application) -> AutoCorrect """
        ...

    @property
    def CellDragAndDrop(self) -> bool:
        """
        Get: CellDragAndDrop(self: Application) -> bool
        Set: CellDragAndDrop(self: Application) = value
        """
        ...

    @property
    def ChartWizardDisplay(self) -> object:
        """
        Get: ChartWizardDisplay(self: Application) -> object
        Set: ChartWizardDisplay(self: Application) = value
        """
        ...

    @property
    def CommandBars(self) -> CommandBars:
        """ Get: CommandBars(self: Application) -> CommandBars """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Application) -> XlCreator """
        ...

    @property
    def DataSheet(self) -> DataSheet:
        """
        Get: DataSheet(self: Application) -> DataSheet
        Set: DataSheet(self: Application) = value
        """
        ...

    @property
    def DisplayAlerts(self) -> bool:
        """
        Get: DisplayAlerts(self: Application) -> bool
        Set: DisplayAlerts(self: Application) = value
        """
        ...

    @property
    def HasLinks(self) -> bool:
        """
        Get: HasLinks(self: Application) -> bool
        Set: HasLinks(self: Application) = value
        """
        ...

    @property
    def Height(self) -> float:
        """
        Get: Height(self: Application) -> float
        Set: Height(self: Application) = value
        """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: Application) -> float
        Set: Left(self: Application) = value
        """
        ...

    @property
    def MoveAfterReturn(self) -> bool:
        """
        Get: MoveAfterReturn(self: Application) -> bool
        Set: MoveAfterReturn(self: Application) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Application) -> str
        Set: Name(self: Application) = value
        """
        ...

    @property
    def Parent(self) -> Application:
        """ Get: Parent(self: Application) -> Application """
        ...

    @property
    def PlotBy(self) -> XlRowCol:
        """
        Get: PlotBy(self: Application) -> XlRowCol
        Set: PlotBy(self: Application) = value
        """
        ...

    @property
    def ShowChartTipNames(self) -> bool:
        """
        Get: ShowChartTipNames(self: Application) -> bool
        Set: ShowChartTipNames(self: Application) = value
        """
        ...

    @property
    def ShowChartTipValues(self) -> bool:
        """
        Get: ShowChartTipValues(self: Application) -> bool
        Set: ShowChartTipValues(self: Application) = value
        """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: Application) -> float
        Set: Top(self: Application) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: Application) -> str """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: Application) -> bool
        Set: Visible(self: Application) = value
        """
        ...

    @property
    def Width(self) -> float:
        """
        Get: Width(self: Application) -> float
        Set: Width(self: Application) = value
        """
        ...

    @property
    def WindowState(self) -> XlWindowState:
        """
        Get: WindowState(self: Application) -> XlWindowState
        Set: WindowState(self: Application) = value
        """
        ...


    def AddChartAutoFormat(self, Name:str, Description:object): # -> 
        """ AddChartAutoFormat(self: Application, Name: str, Description: object) """
        ...

    def Chart(self) -> Chart:
        """ Chart(self: Application) -> Chart """
        ...

    def DeleteChartAutoFormat(self, Name:str): # -> 
        """ DeleteChartAutoFormat(self: Application, Name: str) """
        ...

    def Evaluate(self, Name:str) -> object:
        """ Evaluate(self: Application, Name: str) -> object """
        ...

    def FileImport(self, FileName:str, Password:object, ImportRange:object, WorksheetName:object, OverwriteCells:object): # -> 
        """ FileImport(self: Application, FileName: str, Password: object, ImportRange: object, WorksheetName: object, OverwriteCells: object) """
        ...

    def ImportChart(self, FileName:str, Password:object, ImportRange:object, WorksheetName:object, OverwriteCells:object): # -> 
        """ ImportChart(self: Application, FileName: str, Password: object, ImportRange: object, WorksheetName: object, OverwriteCells: object) """
        ...

    def Quit(self): # -> 
        """ Quit(self: Application) """
        ...

    def SaveAs(self, FileName:str): # -> 
        """ SaveAs(self: Application, FileName: str) """
        ...

    def SaveAsOldFileFormat(self, MajorVersion:object, MinorVersion:object): # -> 
        """ SaveAsOldFileFormat(self: Application, MajorVersion: object, MinorVersion: object) """
        ...

    def SetDefaultChart(self, FormatName:object, Gallery:object): # -> 
        """ SetDefaultChart(self: Application, FormatName: object, Gallery: object) """
        ...

    def Update(self): # -> 
        """ Update(self: Application) """
        ...


class AutoCorrect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: AutoCorrect) -> Application """
        ...

    @property
    def CapitalizeNamesOfDays(self) -> bool:
        """
        Get: CapitalizeNamesOfDays(self: AutoCorrect) -> bool
        Set: CapitalizeNamesOfDays(self: AutoCorrect) = value
        """
        ...

    @property
    def CorrectCapsLock(self) -> bool:
        """
        Get: CorrectCapsLock(self: AutoCorrect) -> bool
        Set: CorrectCapsLock(self: AutoCorrect) = value
        """
        ...

    @property
    def CorrectSentenceCap(self) -> bool:
        """
        Get: CorrectSentenceCap(self: AutoCorrect) -> bool
        Set: CorrectSentenceCap(self: AutoCorrect) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: AutoCorrect) -> XlCreator """
        ...

    @property
    def DisplayAutoCorrectOptions(self) -> bool:
        """
        Get: DisplayAutoCorrectOptions(self: AutoCorrect) -> bool
        Set: DisplayAutoCorrectOptions(self: AutoCorrect) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: AutoCorrect) -> object """
        ...

    @property
    def ReplaceText(self) -> bool:
        """
        Get: ReplaceText(self: AutoCorrect) -> bool
        Set: ReplaceText(self: AutoCorrect) = value
        """
        ...

    @property
    def TwoInitialCapitals(self) -> bool:
        """
        Get: TwoInitialCapitals(self: AutoCorrect) -> bool
        Set: TwoInitialCapitals(self: AutoCorrect) = value
        """
        ...


    def AddReplacement(self, What:str, Replacement:str) -> object:
        """ AddReplacement(self: AutoCorrect, What: str, Replacement: str) -> object """
        ...

    def DeleteReplacement(self, What:str) -> object:
        """ DeleteReplacement(self: AutoCorrect, What: str) -> object """
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
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Axes) -> XlCreator """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Axes) -> object """
        ...


    def Item(self, Type:XlAxisType, AxisGroup:XlAxisGroup) -> Axis:
        """ Item(self: Axes, Type: XlAxisType, AxisGroup: XlAxisGroup) -> Axis """
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
    def Border(self) -> Border:
        """ Get: Border(self: Axis) -> Border """
        ...

    @property
    def CategoryType(self) -> XlCategoryType:
        """
        Get: CategoryType(self: Axis) -> XlCategoryType
        Set: CategoryType(self: Axis) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Axis) -> XlCreator """
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
    def Border(self) -> Border:
        """ Get: Border(self: AxisTitle) -> Border """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: AxisTitle) -> str
        Set: Caption(self: AxisTitle) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: AxisTitle) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: AxisTitle) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: AxisTitle) -> Font """
        ...

    @property
    def HorizontalAlignment(self) -> object:
        """
        Get: HorizontalAlignment(self: AxisTitle) -> object
        Set: HorizontalAlignment(self: AxisTitle) = value
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


    def Delete(self) -> object:
        """ Delete(self: AxisTitle) -> object """
        ...


class Border: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Border) -> Application """
        ...

    @property
    def Color(self) -> object:
        """
        Get: Color(self: Border) -> object
        Set: Color(self: Border) = value
        """
        ...

    @property
    def ColorIndex(self) -> object:
        """
        Get: ColorIndex(self: Border) -> object
        Set: ColorIndex(self: Border) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Border) -> XlCreator """
        ...

    @property
    def LineStyle(self) -> object:
        """
        Get: LineStyle(self: Border) -> object
        Set: LineStyle(self: Border) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Border) -> object """
        ...

    @property
    def ThemeColor(self) -> object:
        """
        Get: ThemeColor(self: Border) -> object
        Set: ThemeColor(self: Border) = value
        """
        ...

    @property
    def TintAndShade(self) -> object:
        """
        Get: TintAndShade(self: Border) -> object
        Set: TintAndShade(self: Border) = value
        """
        ...

    @property
    def Weight(self) -> object:
        """
        Get: Weight(self: Border) -> object
        Set: Weight(self: Border) = value
        """
        ...



class Chart: # skipped bases: <type 'object'>
    """ no doc """
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
    def ChartArea(self) -> ChartArea:
        """ Get: ChartArea(self: Chart) -> ChartArea """
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
    def CommandBars(self) -> CommandBars:
        """ Get: CommandBars(self: Chart) -> CommandBars """
        ...

    @property
    def Corners(self) -> Corners:
        """ Get: Corners(self: Chart) -> Corners """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Chart) -> XlCreator """
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
    def HasLegend(self) -> bool:
        """
        Get: HasLegend(self: Chart) -> bool
        Set: HasLegend(self: Chart) = value
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
    def Height(self) -> object:
        """
        Get: Height(self: Chart) -> object
        Set: Height(self: Chart) = value
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
    def Left(self) -> object:
        """
        Get: Left(self: Chart) -> object
        Set: Left(self: Chart) = value
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
        """ Get: Name(self: Chart) -> str """
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
    def PlotOnX(self) -> int:
        """
        Get: PlotOnX(self: Chart) -> int
        Set: PlotOnX(self: Chart) = value
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
    def SubType(self) -> object:
        """
        Get: SubType(self: Chart) -> object
        Set: SubType(self: Chart) = value
        """
        ...

    @property
    def SurfaceGroup(self) -> ChartGroup:
        """ Get: SurfaceGroup(self: Chart) -> ChartGroup """
        ...

    @property
    def Top(self) -> object:
        """
        Get: Top(self: Chart) -> object
        Set: Top(self: Chart) = value
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

    @property
    def WallsAndGridlines2D(self) -> bool:
        """
        Get: WallsAndGridlines2D(self: Chart) -> bool
        Set: WallsAndGridlines2D(self: Chart) = value
        """
        ...

    @property
    def Width(self) -> object:
        """
        Get: Width(self: Chart) -> object
        Set: Width(self: Chart) = value
        """
        ...


    def Activate(self): # -> 
        """ Activate(self: Chart) """
        ...

    def ApplyCustomType(self, ChartType:XlChartType, TypeName:object): # -> 
        """ ApplyCustomType(self: Chart, ChartType: XlChartType, TypeName: object) """
        ...

    def ApplyDataLabels(self, Type:object, LegendKey:object, AutoText:object, HasLeaderLines:object): # -> 
        """ ApplyDataLabels(self: Chart, Type: object, LegendKey: object, AutoText: object, HasLeaderLines: object) """
        ...

    def AreaGroups(self, Index:object) -> object:
        """ AreaGroups(self: Chart, Index: object) -> object """
        ...

    def AutoFormat(self, Gallery:int, Format:object): # -> 
        """ AutoFormat(self: Chart, Gallery: int, Format: object) """
        ...

    def Axes(self, Type:object, AxisGroup:object) -> object:
        """ Axes(self: Chart, Type: object, AxisGroup: object) -> object """
        ...

    def BarGroups(self, Index:object) -> object:
        """ BarGroups(self: Chart, Index: object) -> object """
        ...

    def ChartGroups(self, Index:object) -> object:
        """ ChartGroups(self: Chart, Index: object) -> object """
        ...

    def ColumnGroups(self, Index:object) -> object:
        """ ColumnGroups(self: Chart, Index: object) -> object """
        ...

    def Deselect(self): # -> 
        """ Deselect(self: Chart) """
        ...

    def DoughnutGroups(self, Index:object) -> object:
        """ DoughnutGroups(self: Chart, Index: object) -> object """
        ...

    def Export(self, FileName:str, FilterName:object, Interactive:object) -> bool:
        """ Export(self: Chart, FileName: str, FilterName: object, Interactive: object) -> bool """
        ...

    def LineGroups(self, Index:object) -> object:
        """ LineGroups(self: Chart, Index: object) -> object """
        ...

    def OmitBackground(self) -> object:
        """ OmitBackground(self: Chart) -> object """
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

    def SeriesCollection(self, Index:object) -> object:
        """ SeriesCollection(self: Chart, Index: object) -> object """
        ...

    def SetEchoOn(self, EchoOn:object) -> object:
        """ SetEchoOn(self: Chart, EchoOn: object) -> object """
        ...

    def XYGroups(self, Index:object) -> object:
        """ XYGroups(self: Chart, Index: object) -> object """
        ...

    def _Dummy44(self): # -> 
        """ _Dummy44(self: Chart) """
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
    def Border(self) -> Border:
        """ Get: Border(self: ChartArea) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ChartArea) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: ChartArea) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: ChartArea) -> Font """
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


class ChartColorFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ChartColorFormat) -> Application """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ChartColorFormat) -> XlCreator """
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
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ChartFillFormat) -> XlCreator """
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
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ChartGroup) -> XlCreator """
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
    def SubType(self) -> int:
        """
        Get: SubType(self: ChartGroup) -> int
        Set: SubType(self: ChartGroup) = value
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
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ChartGroups) -> XlCreator """
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
    def Border(self) -> Border:
        """ Get: Border(self: ChartTitle) -> Border """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: ChartTitle) -> str
        Set: Caption(self: ChartTitle) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ChartTitle) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: ChartTitle) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: ChartTitle) -> Font """
        ...

    @property
    def HorizontalAlignment(self) -> object:
        """
        Get: HorizontalAlignment(self: ChartTitle) -> object
        Set: HorizontalAlignment(self: ChartTitle) = value
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


    def Delete(self) -> object:
        """ Delete(self: ChartTitle) -> object """
        ...


class Constants(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Constants, values: xl3DBar (-4099), xl3DSurface (-4103), xlAll (-4104), xlAutomatic (-4105), xlBar (2), xlBidi (-5000), xlBidiCalendar (3), xlBoth (1), xlBottom (-4107), xlCenter (-4108), xlChecker (9), xlCircle (8), xlColumn (3), xlCombination (-4111), xlComplete (4), xlContext (-5002), xlCorner (2), xlCrissCross (16), xlCross (4), xlCustom (-4114), xlDefault (-4143), xlDefaultAutoFormat (-1), xlDiamond (2), xlDistributed (-4117), xlDoubleAccounting (5), xlFixedValue (1), xlFormats (-4122), xlFullScript (1), xlGray16 (17), xlGray25 (-4124), xlGray50 (-4125), xlGray75 (-4126), xlGray8 (18), xlGregorian (2), xlGrid (15), xlHigh (-4127), xlHindiNumerals (3), xlInside (2), xlJustify (-4130), xlLatin (-5001), xlLeft (-4131), xlLightDown (13), xlLightHorizontal (11), xlLightUp (14), xlLightVertical (12), xlLogicalCursor (1), xlLow (-4134), xlLTR (-5003), xlManual (-4135), xlMaximum (2), xlMinimum (4), xlMinusValues (3), xlMixedAuthorizedScript (4), xlMixedScript (3), xlModule (-4141), xlNextToAxis (4), xlNone (-4142), xlNotes (-4144), xlOff (-4146), xlOn (1), xlOpaque (3), xlPartial (3), xlPartialScript (2), xlPercent (2), xlPlus (9), xlPlusValues (2), xlRight (-4152), xlRTL (-5004), xlScale (3), xlSemiGray75 (10), xlShowLabel (4), xlShowLabelAndPercent (5), xlShowPercent (3), xlShowValue (2), xlSimple (-4154), xlSingle (2), xlSingleAccounting (4), xlSolid (1), xlSquare (1), xlStar (5), xlStError (4), xlSystem (1), xlToolbarButton (2), xlTop (-4160), xlTransparent (2), xlTriangle (3), xlVisualCursor (2), xlWizardDisplayAlways (1), xlWizardDisplayDefault (0), xlWizardDisplayNever (2) """
    value__ = ...
    xl3DBar: Constants = ...
    xl3DSurface: Constants = ...
    xlAll: Constants = ...
    xlAutomatic: Constants = ...
    xlBar: Constants = ...
    xlBidi: Constants = ...
    xlBidiCalendar: Constants = ...
    xlBoth: Constants = ...
    xlBottom: Constants = ...
    xlCenter: Constants = ...
    xlChecker: Constants = ...
    xlCircle: Constants = ...
    xlColumn: Constants = ...
    xlCombination: Constants = ...
    xlComplete: Constants = ...
    xlContext: Constants = ...
    xlCorner: Constants = ...
    xlCrissCross: Constants = ...
    xlCross: Constants = ...
    xlCustom: Constants = ...
    xlDefault: Constants = ...
    xlDefaultAutoFormat: Constants = ...
    xlDiamond: Constants = ...
    xlDistributed: Constants = ...
    xlDoubleAccounting: Constants = ...
    xlFixedValue: Constants = ...
    xlFormats: Constants = ...
    xlFullScript: Constants = ...
    xlGray16: Constants = ...
    xlGray25: Constants = ...
    xlGray50: Constants = ...
    xlGray75: Constants = ...
    xlGray8: Constants = ...
    xlGregorian: Constants = ...
    xlGrid: Constants = ...
    xlHigh: Constants = ...
    xlHindiNumerals: Constants = ...
    xlInside: Constants = ...
    xlJustify: Constants = ...
    xlLatin: Constants = ...
    xlLeft: Constants = ...
    xlLightDown: Constants = ...
    xlLightHorizontal: Constants = ...
    xlLightUp: Constants = ...
    xlLightVertical: Constants = ...
    xlLogicalCursor: Constants = ...
    xlLow: Constants = ...
    xlLTR: Constants = ...
    xlManual: Constants = ...
    xlMaximum: Constants = ...
    xlMinimum: Constants = ...
    xlMinusValues: Constants = ...
    xlMixedAuthorizedScript: Constants = ...
    xlMixedScript: Constants = ...
    xlModule: Constants = ...
    xlNextToAxis: Constants = ...
    xlNone: Constants = ...
    xlNotes: Constants = ...
    xlOff: Constants = ...
    xlOn: Constants = ...
    xlOpaque: Constants = ...
    xlPartial: Constants = ...
    xlPartialScript: Constants = ...
    xlPercent: Constants = ...
    xlPlus: Constants = ...
    xlPlusValues: Constants = ...
    xlRight: Constants = ...
    xlRTL: Constants = ...
    xlScale: Constants = ...
    xlSemiGray75: Constants = ...
    xlShowLabel: Constants = ...
    xlShowLabelAndPercent: Constants = ...
    xlShowPercent: Constants = ...
    xlShowValue: Constants = ...
    xlSimple: Constants = ...
    xlSingle: Constants = ...
    xlSingleAccounting: Constants = ...
    xlSolid: Constants = ...
    xlSquare: Constants = ...
    xlStar: Constants = ...
    xlStError: Constants = ...
    xlSystem: Constants = ...
    xlToolbarButton: Constants = ...
    xlTop: Constants = ...
    xlTransparent: Constants = ...
    xlTriangle: Constants = ...
    xlVisualCursor: Constants = ...
    xlWizardDisplayAlways: Constants = ...
    xlWizardDisplayDefault: Constants = ...
    xlWizardDisplayNever: Constants = ...


class Corners: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Corners) -> Application """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Corners) -> XlCreator """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Corners) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Corners) -> object """
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
    def Border(self) -> Border:
        """ Get: Border(self: DataLabel) -> Border """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: DataLabel) -> str
        Set: Caption(self: DataLabel) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: DataLabel) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: DataLabel) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: DataLabel) -> Font """
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


    def Delete(self) -> object:
        """ Delete(self: DataLabel) -> object """
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
    def Border(self) -> Border:
        """ Get: Border(self: DataLabels) -> Border """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: DataLabels) -> int """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: DataLabels) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: DataLabels) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: DataLabels) -> Font """
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

    def _Dummy11(self): # -> 
        """ _Dummy11(self: DataLabels) """
        ...

    def _Dummy14(self): # -> 
        """ _Dummy14(self: DataLabels) """
        ...

    def _Dummy15(self): # -> 
        """ _Dummy15(self: DataLabels) """
        ...

    def _Dummy34(self): # -> 
        """ _Dummy34(self: DataLabels) """
        ...

    def _Dummy8(self): # -> 
        """ _Dummy8(self: DataLabels) """
        ...


class DataSheet: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: DataSheet) -> Application """
        ...

    @property
    def Cells(self) -> Range:
        """ Get: Cells(self: DataSheet) -> Range """
        ...

    @property
    def Columns(self) -> Range:
        """ Get: Columns(self: DataSheet) -> Range """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: DataSheet) -> XlCreator """
        ...

    @property
    def Font(self) -> Font:
        """
        Get: Font(self: DataSheet) -> Font
        Set: Font(self: DataSheet) = value
        """
        ...

    @property
    def Height(self) -> float:
        """
        Get: Height(self: DataSheet) -> float
        Set: Height(self: DataSheet) = value
        """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: DataSheet) -> float
        Set: Left(self: DataSheet) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: DataSheet) -> object """
        ...

    @property
    def Rows(self) -> Range:
        """ Get: Rows(self: DataSheet) -> Range """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: DataSheet) -> float
        Set: Top(self: DataSheet) = value
        """
        ...

    @property
    def Width(self) -> float:
        """
        Get: Width(self: DataSheet) -> float
        Set: Width(self: DataSheet) = value
        """
        ...


    def Activate(self): # -> 
        """ Activate(self: DataSheet) """
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
    def Border(self) -> Border:
        """ Get: Border(self: DataTable) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: DataTable) -> XlCreator """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: DataTable) -> Font """
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
    def Border(self) -> Border:
        """ Get: Border(self: DisplayUnitLabel) -> Border """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: DisplayUnitLabel) -> str
        Set: Caption(self: DisplayUnitLabel) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: DisplayUnitLabel) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: DisplayUnitLabel) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: DisplayUnitLabel) -> Font """
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


    def Delete(self) -> object:
        """ Delete(self: DisplayUnitLabel) -> object """
        ...


class DownBars: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: DownBars) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: DownBars) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: DownBars) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: DownBars) -> ChartFillFormat """
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


class DropLines: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: DropLines) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: DropLines) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: DropLines) -> XlCreator """
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


class ErrorBars: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ErrorBars) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: ErrorBars) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ErrorBars) -> XlCreator """
        ...

    @property
    def EndStyle(self) -> XlEndStyleCap:
        """
        Get: EndStyle(self: ErrorBars) -> XlEndStyleCap
        Set: EndStyle(self: ErrorBars) = value
        """
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


class Floor: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Floor) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: Floor) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Floor) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: Floor) -> ChartFillFormat """
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


    def ClearFormats(self) -> object:
        """ ClearFormats(self: Floor) -> object """
        ...


class Font: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Font) -> Application """
        ...

    @property
    def Background(self) -> object:
        """
        Get: Background(self: Font) -> object
        Set: Background(self: Font) = value
        """
        ...

    @property
    def Bold(self) -> object:
        """
        Get: Bold(self: Font) -> object
        Set: Bold(self: Font) = value
        """
        ...

    @property
    def Color(self) -> object:
        """
        Get: Color(self: Font) -> object
        Set: Color(self: Font) = value
        """
        ...

    @property
    def ColorIndex(self) -> object:
        """
        Get: ColorIndex(self: Font) -> object
        Set: ColorIndex(self: Font) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Font) -> XlCreator """
        ...

    @property
    def FontStyle(self) -> object:
        """
        Get: FontStyle(self: Font) -> object
        Set: FontStyle(self: Font) = value
        """
        ...

    @property
    def Italic(self) -> object:
        """
        Get: Italic(self: Font) -> object
        Set: Italic(self: Font) = value
        """
        ...

    @property
    def Name(self) -> object:
        """
        Get: Name(self: Font) -> object
        Set: Name(self: Font) = value
        """
        ...

    @property
    def OutlineFont(self) -> object:
        """
        Get: OutlineFont(self: Font) -> object
        Set: OutlineFont(self: Font) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Font) -> object """
        ...

    @property
    def Shadow(self) -> object:
        """
        Get: Shadow(self: Font) -> object
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
    def Strikethrough(self) -> object:
        """
        Get: Strikethrough(self: Font) -> object
        Set: Strikethrough(self: Font) = value
        """
        ...

    @property
    def Subscript(self) -> object:
        """
        Get: Subscript(self: Font) -> object
        Set: Subscript(self: Font) = value
        """
        ...

    @property
    def Superscript(self) -> object:
        """
        Get: Superscript(self: Font) -> object
        Set: Superscript(self: Font) = value
        """
        ...

    @property
    def ThemeColor(self) -> object:
        """
        Get: ThemeColor(self: Font) -> object
        Set: ThemeColor(self: Font) = value
        """
        ...

    @property
    def ThemeFont(self) -> XlThemeFont:
        """
        Get: ThemeFont(self: Font) -> XlThemeFont
        Set: ThemeFont(self: Font) = value
        """
        ...

    @property
    def TintAndShade(self) -> object:
        """
        Get: TintAndShade(self: Font) -> object
        Set: TintAndShade(self: Font) = value
        """
        ...

    @property
    def Underline(self) -> object:
        """
        Get: Underline(self: Font) -> object
        Set: Underline(self: Font) = value
        """
        ...



class _Global: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: _Global) -> Application """
        ...

    @property
    def CommandBars(self) -> CommandBars:
        """ Get: CommandBars(self: _Global) -> CommandBars """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: _Global) -> XlCreator """
        ...

    @property
    def Parent(self) -> Application:
        """ Get: Parent(self: _Global) -> Application """
        ...



class Global(_Global): # skipped bases: <type 'object'>
    """ no doc """
    pass

class GlobalClass(__ComObject, Global): # skipped bases: <type '_Global'>, <type 'object'>
    """ GlobalClass() """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: GlobalClass) -> Application """
        ...

    @property
    def CommandBars(self) -> CommandBars:
        """ Get: CommandBars(self: GlobalClass) -> CommandBars """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: GlobalClass) -> XlCreator """
        ...

    @property
    def Parent(self) -> Application:
        """ Get: Parent(self: GlobalClass) -> Application """
        ...



class Gridlines: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Gridlines) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: Gridlines) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Gridlines) -> XlCreator """
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


class HiLoLines: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: HiLoLines) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: HiLoLines) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: HiLoLines) -> XlCreator """
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


class IApplication: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IApplication) -> Application """
        ...

    @property
    def AutoCorrect(self) -> AutoCorrect:
        """ Get: AutoCorrect(self: IApplication) -> AutoCorrect """
        ...

    @property
    def CellDragAndDrop(self) -> bool:
        """
        Get: CellDragAndDrop(self: IApplication) -> bool
        Set: CellDragAndDrop(self: IApplication) = value
        """
        ...

    @property
    def ChartWizardDisplay(self) -> object:
        """
        Get: ChartWizardDisplay(self: IApplication) -> object
        Set: ChartWizardDisplay(self: IApplication) = value
        """
        ...

    @property
    def CommandBars(self) -> CommandBars:
        """ Get: CommandBars(self: IApplication) -> CommandBars """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IApplication) -> XlCreator """
        ...

    @property
    def DataSheet(self) -> DataSheet:
        """
        Get: DataSheet(self: IApplication) -> DataSheet
        Set: DataSheet(self: IApplication) = value
        """
        ...

    @property
    def DisplayAlerts(self) -> bool:
        """
        Get: DisplayAlerts(self: IApplication) -> bool
        Set: DisplayAlerts(self: IApplication) = value
        """
        ...

    @property
    def HasLinks(self) -> bool:
        """
        Get: HasLinks(self: IApplication) -> bool
        Set: HasLinks(self: IApplication) = value
        """
        ...

    @property
    def Height(self) -> float:
        """
        Get: Height(self: IApplication) -> float
        Set: Height(self: IApplication) = value
        """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: IApplication) -> float
        Set: Left(self: IApplication) = value
        """
        ...

    @property
    def MoveAfterReturn(self) -> bool:
        """
        Get: MoveAfterReturn(self: IApplication) -> bool
        Set: MoveAfterReturn(self: IApplication) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: IApplication) -> str
        Set: Name(self: IApplication) = value
        """
        ...

    @property
    def Parent(self) -> Application:
        """ Get: Parent(self: IApplication) -> Application """
        ...

    @property
    def PlotBy(self) -> XlRowCol:
        """
        Get: PlotBy(self: IApplication) -> XlRowCol
        Set: PlotBy(self: IApplication) = value
        """
        ...

    @property
    def ShowChartTipNames(self) -> bool:
        """
        Get: ShowChartTipNames(self: IApplication) -> bool
        Set: ShowChartTipNames(self: IApplication) = value
        """
        ...

    @property
    def ShowChartTipValues(self) -> bool:
        """
        Get: ShowChartTipValues(self: IApplication) -> bool
        Set: ShowChartTipValues(self: IApplication) = value
        """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: IApplication) -> float
        Set: Top(self: IApplication) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: IApplication) -> str """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: IApplication) -> bool
        Set: Visible(self: IApplication) = value
        """
        ...

    @property
    def Width(self) -> float:
        """
        Get: Width(self: IApplication) -> float
        Set: Width(self: IApplication) = value
        """
        ...

    @property
    def WindowState(self) -> XlWindowState:
        """
        Get: WindowState(self: IApplication) -> XlWindowState
        Set: WindowState(self: IApplication) = value
        """
        ...


    def AddChartAutoFormat(self, Name:str, Description:object): # -> 
        """ AddChartAutoFormat(self: IApplication, Name: str, Description: object) """
        ...

    def Chart(self) -> Chart:
        """ Chart(self: IApplication) -> Chart """
        ...

    def DeleteChartAutoFormat(self, Name:str): # -> 
        """ DeleteChartAutoFormat(self: IApplication, Name: str) """
        ...

    def Evaluate(self, Name:str) -> object:
        """ Evaluate(self: IApplication, Name: str) -> object """
        ...

    def FileImport(self, FileName:str, Password:object, ImportRange:object, WorksheetName:object, OverwriteCells:object): # -> 
        """ FileImport(self: IApplication, FileName: str, Password: object, ImportRange: object, WorksheetName: object, OverwriteCells: object) """
        ...

    def ImportChart(self, FileName:str, Password:object, ImportRange:object, WorksheetName:object, OverwriteCells:object): # -> 
        """ ImportChart(self: IApplication, FileName: str, Password: object, ImportRange: object, WorksheetName: object, OverwriteCells: object) """
        ...

    def Quit(self): # -> 
        """ Quit(self: IApplication) """
        ...

    def SaveAs(self, FileName:str): # -> 
        """ SaveAs(self: IApplication, FileName: str) """
        ...

    def SaveAsOldFileFormat(self, MajorVersion:object, MinorVersion:object): # -> 
        """ SaveAsOldFileFormat(self: IApplication, MajorVersion: object, MinorVersion: object) """
        ...

    def SetDefaultChart(self, FormatName:object, Gallery:object): # -> 
        """ SetDefaultChart(self: IApplication, FormatName: object, Gallery: object) """
        ...

    def Update(self): # -> 
        """ Update(self: IApplication) """
        ...


class IAutoCorrect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IAutoCorrect) -> Application """
        ...

    @property
    def CapitalizeNamesOfDays(self) -> bool:
        """
        Get: CapitalizeNamesOfDays(self: IAutoCorrect) -> bool
        Set: CapitalizeNamesOfDays(self: IAutoCorrect) = value
        """
        ...

    @property
    def CorrectCapsLock(self) -> bool:
        """
        Get: CorrectCapsLock(self: IAutoCorrect) -> bool
        Set: CorrectCapsLock(self: IAutoCorrect) = value
        """
        ...

    @property
    def CorrectSentenceCap(self) -> bool:
        """
        Get: CorrectSentenceCap(self: IAutoCorrect) -> bool
        Set: CorrectSentenceCap(self: IAutoCorrect) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IAutoCorrect) -> XlCreator """
        ...

    @property
    def DisplayAutoCorrectOptions(self) -> bool:
        """
        Get: DisplayAutoCorrectOptions(self: IAutoCorrect) -> bool
        Set: DisplayAutoCorrectOptions(self: IAutoCorrect) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IAutoCorrect) -> object """
        ...

    @property
    def ReplaceText(self) -> bool:
        """
        Get: ReplaceText(self: IAutoCorrect) -> bool
        Set: ReplaceText(self: IAutoCorrect) = value
        """
        ...

    @property
    def TwoInitialCapitals(self) -> bool:
        """
        Get: TwoInitialCapitals(self: IAutoCorrect) -> bool
        Set: TwoInitialCapitals(self: IAutoCorrect) = value
        """
        ...


    def AddReplacement(self, What:str, Replacement:str) -> object:
        """ AddReplacement(self: IAutoCorrect, What: str, Replacement: str) -> object """
        ...

    def DeleteReplacement(self, What:str) -> object:
        """ DeleteReplacement(self: IAutoCorrect, What: str) -> object """
        ...


class IAxes(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IAxes) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: IAxes) -> int """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IAxes) -> XlCreator """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IAxes) -> object """
        ...


    def Item(self, Type:XlAxisType, AxisGroup:XlAxisGroup) -> Axis:
        """ Item(self: IAxes, Type: XlAxisType, AxisGroup: XlAxisGroup) -> Axis """
        ...


class IAxis: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IAxis) -> Application """
        ...

    @property
    def AxisBetweenCategories(self) -> bool:
        """
        Get: AxisBetweenCategories(self: IAxis) -> bool
        Set: AxisBetweenCategories(self: IAxis) = value
        """
        ...

    @property
    def AxisGroup(self) -> XlAxisGroup:
        """ Get: AxisGroup(self: IAxis) -> XlAxisGroup """
        ...

    @property
    def AxisTitle(self) -> AxisTitle:
        """ Get: AxisTitle(self: IAxis) -> AxisTitle """
        ...

    @property
    def BaseUnit(self) -> XlTimeUnit:
        """
        Get: BaseUnit(self: IAxis) -> XlTimeUnit
        Set: BaseUnit(self: IAxis) = value
        """
        ...

    @property
    def BaseUnitIsAuto(self) -> bool:
        """
        Get: BaseUnitIsAuto(self: IAxis) -> bool
        Set: BaseUnitIsAuto(self: IAxis) = value
        """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IAxis) -> Border """
        ...

    @property
    def CategoryType(self) -> XlCategoryType:
        """
        Get: CategoryType(self: IAxis) -> XlCategoryType
        Set: CategoryType(self: IAxis) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IAxis) -> XlCreator """
        ...

    @property
    def Crosses(self) -> XlAxisCrosses:
        """
        Get: Crosses(self: IAxis) -> XlAxisCrosses
        Set: Crosses(self: IAxis) = value
        """
        ...

    @property
    def CrossesAt(self) -> float:
        """
        Get: CrossesAt(self: IAxis) -> float
        Set: CrossesAt(self: IAxis) = value
        """
        ...

    @property
    def DisplayUnit(self) -> XlDisplayUnit:
        """
        Get: DisplayUnit(self: IAxis) -> XlDisplayUnit
        Set: DisplayUnit(self: IAxis) = value
        """
        ...

    @property
    def DisplayUnitCustom(self) -> float:
        """
        Get: DisplayUnitCustom(self: IAxis) -> float
        Set: DisplayUnitCustom(self: IAxis) = value
        """
        ...

    @property
    def DisplayUnitLabel(self) -> DisplayUnitLabel:
        """ Get: DisplayUnitLabel(self: IAxis) -> DisplayUnitLabel """
        ...

    @property
    def HasDisplayUnitLabel(self) -> bool:
        """
        Get: HasDisplayUnitLabel(self: IAxis) -> bool
        Set: HasDisplayUnitLabel(self: IAxis) = value
        """
        ...

    @property
    def HasMajorGridlines(self) -> bool:
        """
        Get: HasMajorGridlines(self: IAxis) -> bool
        Set: HasMajorGridlines(self: IAxis) = value
        """
        ...

    @property
    def HasMinorGridlines(self) -> bool:
        """
        Get: HasMinorGridlines(self: IAxis) -> bool
        Set: HasMinorGridlines(self: IAxis) = value
        """
        ...

    @property
    def HasTitle(self) -> bool:
        """
        Get: HasTitle(self: IAxis) -> bool
        Set: HasTitle(self: IAxis) = value
        """
        ...

    @property
    def Height(self) -> float:
        """ Get: Height(self: IAxis) -> float """
        ...

    @property
    def Left(self) -> float:
        """ Get: Left(self: IAxis) -> float """
        ...

    @property
    def MajorGridlines(self) -> Gridlines:
        """ Get: MajorGridlines(self: IAxis) -> Gridlines """
        ...

    @property
    def MajorTickMark(self) -> XlTickMark:
        """
        Get: MajorTickMark(self: IAxis) -> XlTickMark
        Set: MajorTickMark(self: IAxis) = value
        """
        ...

    @property
    def MajorUnit(self) -> float:
        """
        Get: MajorUnit(self: IAxis) -> float
        Set: MajorUnit(self: IAxis) = value
        """
        ...

    @property
    def MajorUnitIsAuto(self) -> bool:
        """
        Get: MajorUnitIsAuto(self: IAxis) -> bool
        Set: MajorUnitIsAuto(self: IAxis) = value
        """
        ...

    @property
    def MajorUnitScale(self) -> XlTimeUnit:
        """
        Get: MajorUnitScale(self: IAxis) -> XlTimeUnit
        Set: MajorUnitScale(self: IAxis) = value
        """
        ...

    @property
    def MaximumScale(self) -> float:
        """
        Get: MaximumScale(self: IAxis) -> float
        Set: MaximumScale(self: IAxis) = value
        """
        ...

    @property
    def MaximumScaleIsAuto(self) -> bool:
        """
        Get: MaximumScaleIsAuto(self: IAxis) -> bool
        Set: MaximumScaleIsAuto(self: IAxis) = value
        """
        ...

    @property
    def MinimumScale(self) -> float:
        """
        Get: MinimumScale(self: IAxis) -> float
        Set: MinimumScale(self: IAxis) = value
        """
        ...

    @property
    def MinimumScaleIsAuto(self) -> bool:
        """
        Get: MinimumScaleIsAuto(self: IAxis) -> bool
        Set: MinimumScaleIsAuto(self: IAxis) = value
        """
        ...

    @property
    def MinorGridlines(self) -> Gridlines:
        """ Get: MinorGridlines(self: IAxis) -> Gridlines """
        ...

    @property
    def MinorTickMark(self) -> XlTickMark:
        """
        Get: MinorTickMark(self: IAxis) -> XlTickMark
        Set: MinorTickMark(self: IAxis) = value
        """
        ...

    @property
    def MinorUnit(self) -> float:
        """
        Get: MinorUnit(self: IAxis) -> float
        Set: MinorUnit(self: IAxis) = value
        """
        ...

    @property
    def MinorUnitIsAuto(self) -> bool:
        """
        Get: MinorUnitIsAuto(self: IAxis) -> bool
        Set: MinorUnitIsAuto(self: IAxis) = value
        """
        ...

    @property
    def MinorUnitScale(self) -> XlTimeUnit:
        """
        Get: MinorUnitScale(self: IAxis) -> XlTimeUnit
        Set: MinorUnitScale(self: IAxis) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IAxis) -> object """
        ...

    @property
    def ReversePlotOrder(self) -> bool:
        """
        Get: ReversePlotOrder(self: IAxis) -> bool
        Set: ReversePlotOrder(self: IAxis) = value
        """
        ...

    @property
    def ScaleType(self) -> XlScaleType:
        """
        Get: ScaleType(self: IAxis) -> XlScaleType
        Set: ScaleType(self: IAxis) = value
        """
        ...

    @property
    def TickLabelPosition(self) -> XlTickLabelPosition:
        """
        Get: TickLabelPosition(self: IAxis) -> XlTickLabelPosition
        Set: TickLabelPosition(self: IAxis) = value
        """
        ...

    @property
    def TickLabels(self) -> TickLabels:
        """ Get: TickLabels(self: IAxis) -> TickLabels """
        ...

    @property
    def TickLabelSpacing(self) -> int:
        """
        Get: TickLabelSpacing(self: IAxis) -> int
        Set: TickLabelSpacing(self: IAxis) = value
        """
        ...

    @property
    def TickMarkSpacing(self) -> int:
        """
        Get: TickMarkSpacing(self: IAxis) -> int
        Set: TickMarkSpacing(self: IAxis) = value
        """
        ...

    @property
    def Top(self) -> float:
        """ Get: Top(self: IAxis) -> float """
        ...

    @property
    def Type(self) -> XlAxisType:
        """
        Get: Type(self: IAxis) -> XlAxisType
        Set: Type(self: IAxis) = value
        """
        ...

    @property
    def Width(self) -> float:
        """ Get: Width(self: IAxis) -> float """
        ...


    def Delete(self) -> object:
        """ Delete(self: IAxis) -> object """
        ...


class IAxisTitle: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IAxisTitle) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: IAxisTitle) -> object
        Set: AutoScaleFont(self: IAxisTitle) = value
        """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IAxisTitle) -> Border """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: IAxisTitle) -> str
        Set: Caption(self: IAxisTitle) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IAxisTitle) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: IAxisTitle) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: IAxisTitle) -> Font """
        ...

    @property
    def HorizontalAlignment(self) -> object:
        """
        Get: HorizontalAlignment(self: IAxisTitle) -> object
        Set: HorizontalAlignment(self: IAxisTitle) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: IAxisTitle) -> Interior """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: IAxisTitle) -> float
        Set: Left(self: IAxisTitle) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IAxisTitle) -> str """
        ...

    @property
    def Orientation(self) -> object:
        """
        Get: Orientation(self: IAxisTitle) -> object
        Set: Orientation(self: IAxisTitle) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IAxisTitle) -> object """
        ...

    @property
    def ReadingOrder(self) -> int:
        """
        Get: ReadingOrder(self: IAxisTitle) -> int
        Set: ReadingOrder(self: IAxisTitle) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: IAxisTitle) -> bool
        Set: Shadow(self: IAxisTitle) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: IAxisTitle) -> str
        Set: Text(self: IAxisTitle) = value
        """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: IAxisTitle) -> float
        Set: Top(self: IAxisTitle) = value
        """
        ...

    @property
    def VerticalAlignment(self) -> object:
        """
        Get: VerticalAlignment(self: IAxisTitle) -> object
        Set: VerticalAlignment(self: IAxisTitle) = value
        """
        ...


    def Delete(self) -> object:
        """ Delete(self: IAxisTitle) -> object """
        ...


class IBorder: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IBorder) -> Application """
        ...

    @property
    def Color(self) -> object:
        """
        Get: Color(self: IBorder) -> object
        Set: Color(self: IBorder) = value
        """
        ...

    @property
    def ColorIndex(self) -> object:
        """
        Get: ColorIndex(self: IBorder) -> object
        Set: ColorIndex(self: IBorder) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IBorder) -> XlCreator """
        ...

    @property
    def LineStyle(self) -> object:
        """
        Get: LineStyle(self: IBorder) -> object
        Set: LineStyle(self: IBorder) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IBorder) -> object """
        ...

    @property
    def ThemeColor(self) -> object:
        """
        Get: ThemeColor(self: IBorder) -> object
        Set: ThemeColor(self: IBorder) = value
        """
        ...

    @property
    def TintAndShade(self) -> object:
        """
        Get: TintAndShade(self: IBorder) -> object
        Set: TintAndShade(self: IBorder) = value
        """
        ...

    @property
    def Weight(self) -> object:
        """
        Get: Weight(self: IBorder) -> object
        Set: Weight(self: IBorder) = value
        """
        ...



class ICanvasShapes: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IChart: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IChart) -> Application """
        ...

    @property
    def Area3DGroup(self) -> ChartGroup:
        """ Get: Area3DGroup(self: IChart) -> ChartGroup """
        ...

    @property
    def AutoScaling(self) -> bool:
        """
        Get: AutoScaling(self: IChart) -> bool
        Set: AutoScaling(self: IChart) = value
        """
        ...

    @property
    def Bar3DGroup(self) -> ChartGroup:
        """ Get: Bar3DGroup(self: IChart) -> ChartGroup """
        ...

    @property
    def BarShape(self) -> XlBarShape:
        """
        Get: BarShape(self: IChart) -> XlBarShape
        Set: BarShape(self: IChart) = value
        """
        ...

    @property
    def ChartArea(self) -> ChartArea:
        """ Get: ChartArea(self: IChart) -> ChartArea """
        ...

    @property
    def ChartTitle(self) -> ChartTitle:
        """ Get: ChartTitle(self: IChart) -> ChartTitle """
        ...

    @property
    def ChartType(self) -> XlChartType:
        """
        Get: ChartType(self: IChart) -> XlChartType
        Set: ChartType(self: IChart) = value
        """
        ...

    @property
    def Column3DGroup(self) -> ChartGroup:
        """ Get: Column3DGroup(self: IChart) -> ChartGroup """
        ...

    @property
    def CommandBars(self) -> CommandBars:
        """ Get: CommandBars(self: IChart) -> CommandBars """
        ...

    @property
    def Corners(self) -> Corners:
        """ Get: Corners(self: IChart) -> Corners """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IChart) -> XlCreator """
        ...

    @property
    def DataTable(self) -> DataTable:
        """ Get: DataTable(self: IChart) -> DataTable """
        ...

    @property
    def DepthPercent(self) -> int:
        """
        Get: DepthPercent(self: IChart) -> int
        Set: DepthPercent(self: IChart) = value
        """
        ...

    @property
    def DisplayBlanksAs(self) -> XlDisplayBlanksAs:
        """
        Get: DisplayBlanksAs(self: IChart) -> XlDisplayBlanksAs
        Set: DisplayBlanksAs(self: IChart) = value
        """
        ...

    @property
    def Elevation(self) -> int:
        """
        Get: Elevation(self: IChart) -> int
        Set: Elevation(self: IChart) = value
        """
        ...

    @property
    def Floor(self) -> Floor:
        """ Get: Floor(self: IChart) -> Floor """
        ...

    @property
    def GapDepth(self) -> int:
        """
        Get: GapDepth(self: IChart) -> int
        Set: GapDepth(self: IChart) = value
        """
        ...

    @property
    def HasDataTable(self) -> bool:
        """
        Get: HasDataTable(self: IChart) -> bool
        Set: HasDataTable(self: IChart) = value
        """
        ...

    @property
    def HasLegend(self) -> bool:
        """
        Get: HasLegend(self: IChart) -> bool
        Set: HasLegend(self: IChart) = value
        """
        ...

    @property
    def HasTitle(self) -> bool:
        """
        Get: HasTitle(self: IChart) -> bool
        Set: HasTitle(self: IChart) = value
        """
        ...

    @property
    def Height(self) -> object:
        """
        Get: Height(self: IChart) -> object
        Set: Height(self: IChart) = value
        """
        ...

    @property
    def HeightPercent(self) -> int:
        """
        Get: HeightPercent(self: IChart) -> int
        Set: HeightPercent(self: IChart) = value
        """
        ...

    @property
    def Left(self) -> object:
        """
        Get: Left(self: IChart) -> object
        Set: Left(self: IChart) = value
        """
        ...

    @property
    def Legend(self) -> Legend:
        """ Get: Legend(self: IChart) -> Legend """
        ...

    @property
    def Line3DGroup(self) -> ChartGroup:
        """ Get: Line3DGroup(self: IChart) -> ChartGroup """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IChart) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IChart) -> object """
        ...

    @property
    def Perspective(self) -> int:
        """
        Get: Perspective(self: IChart) -> int
        Set: Perspective(self: IChart) = value
        """
        ...

    @property
    def Pie3DGroup(self) -> ChartGroup:
        """ Get: Pie3DGroup(self: IChart) -> ChartGroup """
        ...

    @property
    def PlotArea(self) -> PlotArea:
        """ Get: PlotArea(self: IChart) -> PlotArea """
        ...

    @property
    def PlotOnX(self) -> int:
        """
        Get: PlotOnX(self: IChart) -> int
        Set: PlotOnX(self: IChart) = value
        """
        ...

    @property
    def RightAngleAxes(self) -> object:
        """
        Get: RightAngleAxes(self: IChart) -> object
        Set: RightAngleAxes(self: IChart) = value
        """
        ...

    @property
    def Rotation(self) -> object:
        """
        Get: Rotation(self: IChart) -> object
        Set: Rotation(self: IChart) = value
        """
        ...

    @property
    def SubType(self) -> object:
        """
        Get: SubType(self: IChart) -> object
        Set: SubType(self: IChart) = value
        """
        ...

    @property
    def SurfaceGroup(self) -> ChartGroup:
        """ Get: SurfaceGroup(self: IChart) -> ChartGroup """
        ...

    @property
    def Top(self) -> object:
        """
        Get: Top(self: IChart) -> object
        Set: Top(self: IChart) = value
        """
        ...

    @property
    def Type(self) -> int:
        """
        Get: Type(self: IChart) -> int
        Set: Type(self: IChart) = value
        """
        ...

    @property
    def Walls(self) -> Walls:
        """ Get: Walls(self: IChart) -> Walls """
        ...

    @property
    def WallsAndGridlines2D(self) -> bool:
        """
        Get: WallsAndGridlines2D(self: IChart) -> bool
        Set: WallsAndGridlines2D(self: IChart) = value
        """
        ...

    @property
    def Width(self) -> object:
        """
        Get: Width(self: IChart) -> object
        Set: Width(self: IChart) = value
        """
        ...


    def Activate(self): # -> 
        """ Activate(self: IChart) """
        ...

    def ApplyCustomType(self, ChartType:XlChartType, TypeName:object): # -> 
        """ ApplyCustomType(self: IChart, ChartType: XlChartType, TypeName: object) """
        ...

    def ApplyDataLabels(self, Type:object, LegendKey:object, AutoText:object, HasLeaderLines:object): # -> 
        """ ApplyDataLabels(self: IChart, Type: object, LegendKey: object, AutoText: object, HasLeaderLines: object) """
        ...

    def AreaGroups(self, Index:object) -> object:
        """ AreaGroups(self: IChart, Index: object) -> object """
        ...

    def AutoFormat(self, Gallery:int, Format:object): # -> 
        """ AutoFormat(self: IChart, Gallery: int, Format: object) """
        ...

    def Axes(self, Type:object, AxisGroup:object) -> object:
        """ Axes(self: IChart, Type: object, AxisGroup: object) -> object """
        ...

    def BarGroups(self, Index:object) -> object:
        """ BarGroups(self: IChart, Index: object) -> object """
        ...

    def ChartGroups(self, Index:object) -> object:
        """ ChartGroups(self: IChart, Index: object) -> object """
        ...

    def ColumnGroups(self, Index:object) -> object:
        """ ColumnGroups(self: IChart, Index: object) -> object """
        ...

    def Deselect(self): # -> 
        """ Deselect(self: IChart) """
        ...

    def DoughnutGroups(self, Index:object) -> object:
        """ DoughnutGroups(self: IChart, Index: object) -> object """
        ...

    def Export(self, FileName:str, FilterName:object, Interactive:object) -> bool:
        """ Export(self: IChart, FileName: str, FilterName: object, Interactive: object) -> bool """
        ...

    def LineGroups(self, Index:object) -> object:
        """ LineGroups(self: IChart, Index: object) -> object """
        ...

    def OmitBackground(self) -> object:
        """ OmitBackground(self: IChart) -> object """
        ...

    def PieGroups(self, Index:object) -> object:
        """ PieGroups(self: IChart, Index: object) -> object """
        ...

    def RadarGroups(self, Index:object) -> object:
        """ RadarGroups(self: IChart, Index: object) -> object """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: IChart) """
        ...

    def SeriesCollection(self, Index:object) -> object:
        """ SeriesCollection(self: IChart, Index: object) -> object """
        ...

    def SetEchoOn(self, EchoOn:object) -> object:
        """ SetEchoOn(self: IChart, EchoOn: object) -> object """
        ...

    def XYGroups(self, Index:object) -> object:
        """ XYGroups(self: IChart, Index: object) -> object """
        ...

    def _Dummy44(self): # -> 
        """ _Dummy44(self: IChart) """
        ...


class IChartArea: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IChartArea) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: IChartArea) -> object
        Set: AutoScaleFont(self: IChartArea) = value
        """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IChartArea) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IChartArea) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: IChartArea) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: IChartArea) -> Font """
        ...

    @property
    def Height(self) -> float:
        """
        Get: Height(self: IChartArea) -> float
        Set: Height(self: IChartArea) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: IChartArea) -> Interior """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: IChartArea) -> float
        Set: Left(self: IChartArea) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IChartArea) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IChartArea) -> object """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: IChartArea) -> bool
        Set: Shadow(self: IChartArea) = value
        """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: IChartArea) -> float
        Set: Top(self: IChartArea) = value
        """
        ...

    @property
    def Width(self) -> float:
        """
        Get: Width(self: IChartArea) -> float
        Set: Width(self: IChartArea) = value
        """
        ...


    def Clear(self) -> object:
        """ Clear(self: IChartArea) -> object """
        ...

    def ClearContents(self) -> object:
        """ ClearContents(self: IChartArea) -> object """
        ...

    def ClearFormats(self) -> object:
        """ ClearFormats(self: IChartArea) -> object """
        ...

    def Copy(self) -> object:
        """ Copy(self: IChartArea) -> object """
        ...


class IChartColorFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IChartColorFormat) -> Application """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IChartColorFormat) -> XlCreator """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IChartColorFormat) -> object """
        ...

    @property
    def RGB(self) -> int:
        """ Get: RGB(self: IChartColorFormat) -> int """
        ...

    @property
    def SchemeColor(self) -> int:
        """
        Get: SchemeColor(self: IChartColorFormat) -> int
        Set: SchemeColor(self: IChartColorFormat) = value
        """
        ...

    @property
    def Type(self) -> int:
        """ Get: Type(self: IChartColorFormat) -> int """
        ...

    @property
    def _Default(self) -> int:
        """ Get: _Default(self: IChartColorFormat) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IChartFillFormat: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IChartFillFormat) -> Application """
        ...

    @property
    def BackColor(self) -> ChartColorFormat:
        """ Get: BackColor(self: IChartFillFormat) -> ChartColorFormat """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IChartFillFormat) -> XlCreator """
        ...

    @property
    def ForeColor(self) -> ChartColorFormat:
        """ Get: ForeColor(self: IChartFillFormat) -> ChartColorFormat """
        ...

    @property
    def GradientColorType(self): # -> MsoGradientColorType
        """ Get: GradientColorType(self: IChartFillFormat) -> MsoGradientColorType """
        ...

    @property
    def GradientDegree(self) -> Single:
        """ Get: GradientDegree(self: IChartFillFormat) -> Single """
        ...

    @property
    def GradientStyle(self): # -> MsoGradientStyle
        """ Get: GradientStyle(self: IChartFillFormat) -> MsoGradientStyle """
        ...

    @property
    def GradientVariant(self) -> int:
        """ Get: GradientVariant(self: IChartFillFormat) -> int """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IChartFillFormat) -> object """
        ...

    @property
    def Pattern(self): # -> MsoPatternType
        """ Get: Pattern(self: IChartFillFormat) -> MsoPatternType """
        ...

    @property
    def PresetGradientType(self): # -> MsoPresetGradientType
        """ Get: PresetGradientType(self: IChartFillFormat) -> MsoPresetGradientType """
        ...

    @property
    def PresetTexture(self): # -> MsoPresetTexture
        """ Get: PresetTexture(self: IChartFillFormat) -> MsoPresetTexture """
        ...

    @property
    def TextureName(self) -> str:
        """ Get: TextureName(self: IChartFillFormat) -> str """
        ...

    @property
    def TextureType(self): # -> MsoTextureType
        """ Get: TextureType(self: IChartFillFormat) -> MsoTextureType """
        ...

    @property
    def Type(self): # -> MsoFillType
        """ Get: Type(self: IChartFillFormat) -> MsoFillType """
        ...

    @property
    def Visible(self): # -> MsoTriState
        """
        Get: Visible(self: IChartFillFormat) -> MsoTriState
        Set: Visible(self: IChartFillFormat) = value
        """
        ...


    def OneColorGradient(self, Style, Variant:int, Degree:Single): # ->  # Not found arg types: {'Style': 'MsoGradientStyle'}
        """ OneColorGradient(self: IChartFillFormat, Style: MsoGradientStyle, Variant: int, Degree: Single) """
        ...

    def Patterned(self, Pattern): # ->  # Not found arg types: {'Pattern': 'MsoPatternType'}
        """ Patterned(self: IChartFillFormat, Pattern: MsoPatternType) """
        ...

    def PresetGradient(self, Style, Variant:int, PresetGradientType): # ->  # Not found arg types: {'Style': 'MsoGradientStyle', 'PresetGradientType': 'MsoPresetGradientType'}
        """ PresetGradient(self: IChartFillFormat, Style: MsoGradientStyle, Variant: int, PresetGradientType: MsoPresetGradientType) """
        ...

    def PresetTextured(self, PresetTexture): # ->  # Not found arg types: {'PresetTexture': 'MsoPresetTexture'}
        """ PresetTextured(self: IChartFillFormat, PresetTexture: MsoPresetTexture) """
        ...

    def Solid(self): # -> 
        """ Solid(self: IChartFillFormat) """
        ...

    def TwoColorGradient(self, Style, Variant:int): # ->  # Not found arg types: {'Style': 'MsoGradientStyle'}
        """ TwoColorGradient(self: IChartFillFormat, Style: MsoGradientStyle, Variant: int) """
        ...

    def UserPicture(self, PictureFile:object, PictureFormat:object, PictureStackUnit:object, PicturePlacement:object): # -> 
        """ UserPicture(self: IChartFillFormat, PictureFile: object, PictureFormat: object, PictureStackUnit: object, PicturePlacement: object) """
        ...

    def UserTextured(self, TextureFile:str): # -> 
        """ UserTextured(self: IChartFillFormat, TextureFile: str) """
        ...


class IChartGroup: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IChartGroup) -> Application """
        ...

    @property
    def AxisGroup(self) -> XlAxisGroup:
        """
        Get: AxisGroup(self: IChartGroup) -> XlAxisGroup
        Set: AxisGroup(self: IChartGroup) = value
        """
        ...

    @property
    def BubbleScale(self) -> int:
        """
        Get: BubbleScale(self: IChartGroup) -> int
        Set: BubbleScale(self: IChartGroup) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IChartGroup) -> XlCreator """
        ...

    @property
    def DoughnutHoleSize(self) -> int:
        """
        Get: DoughnutHoleSize(self: IChartGroup) -> int
        Set: DoughnutHoleSize(self: IChartGroup) = value
        """
        ...

    @property
    def DownBars(self) -> DownBars:
        """ Get: DownBars(self: IChartGroup) -> DownBars """
        ...

    @property
    def DropLines(self) -> DropLines:
        """ Get: DropLines(self: IChartGroup) -> DropLines """
        ...

    @property
    def FirstSliceAngle(self) -> int:
        """
        Get: FirstSliceAngle(self: IChartGroup) -> int
        Set: FirstSliceAngle(self: IChartGroup) = value
        """
        ...

    @property
    def GapWidth(self) -> int:
        """
        Get: GapWidth(self: IChartGroup) -> int
        Set: GapWidth(self: IChartGroup) = value
        """
        ...

    @property
    def Has3DShading(self) -> bool:
        """
        Get: Has3DShading(self: IChartGroup) -> bool
        Set: Has3DShading(self: IChartGroup) = value
        """
        ...

    @property
    def HasDropLines(self) -> bool:
        """
        Get: HasDropLines(self: IChartGroup) -> bool
        Set: HasDropLines(self: IChartGroup) = value
        """
        ...

    @property
    def HasHiLoLines(self) -> bool:
        """
        Get: HasHiLoLines(self: IChartGroup) -> bool
        Set: HasHiLoLines(self: IChartGroup) = value
        """
        ...

    @property
    def HasRadarAxisLabels(self) -> bool:
        """
        Get: HasRadarAxisLabels(self: IChartGroup) -> bool
        Set: HasRadarAxisLabels(self: IChartGroup) = value
        """
        ...

    @property
    def HasSeriesLines(self) -> bool:
        """
        Get: HasSeriesLines(self: IChartGroup) -> bool
        Set: HasSeriesLines(self: IChartGroup) = value
        """
        ...

    @property
    def HasUpDownBars(self) -> bool:
        """
        Get: HasUpDownBars(self: IChartGroup) -> bool
        Set: HasUpDownBars(self: IChartGroup) = value
        """
        ...

    @property
    def HiLoLines(self) -> HiLoLines:
        """ Get: HiLoLines(self: IChartGroup) -> HiLoLines """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: IChartGroup) -> int """
        ...

    @property
    def Overlap(self) -> int:
        """
        Get: Overlap(self: IChartGroup) -> int
        Set: Overlap(self: IChartGroup) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IChartGroup) -> object """
        ...

    @property
    def RadarAxisLabels(self) -> TickLabels:
        """ Get: RadarAxisLabels(self: IChartGroup) -> TickLabels """
        ...

    @property
    def SecondPlotSize(self) -> int:
        """
        Get: SecondPlotSize(self: IChartGroup) -> int
        Set: SecondPlotSize(self: IChartGroup) = value
        """
        ...

    @property
    def SeriesLines(self) -> SeriesLines:
        """ Get: SeriesLines(self: IChartGroup) -> SeriesLines """
        ...

    @property
    def ShowNegativeBubbles(self) -> bool:
        """
        Get: ShowNegativeBubbles(self: IChartGroup) -> bool
        Set: ShowNegativeBubbles(self: IChartGroup) = value
        """
        ...

    @property
    def SizeRepresents(self) -> XlSizeRepresents:
        """
        Get: SizeRepresents(self: IChartGroup) -> XlSizeRepresents
        Set: SizeRepresents(self: IChartGroup) = value
        """
        ...

    @property
    def SplitType(self) -> XlChartSplitType:
        """
        Get: SplitType(self: IChartGroup) -> XlChartSplitType
        Set: SplitType(self: IChartGroup) = value
        """
        ...

    @property
    def SplitValue(self) -> object:
        """
        Get: SplitValue(self: IChartGroup) -> object
        Set: SplitValue(self: IChartGroup) = value
        """
        ...

    @property
    def SubType(self) -> int:
        """
        Get: SubType(self: IChartGroup) -> int
        Set: SubType(self: IChartGroup) = value
        """
        ...

    @property
    def Type(self) -> int:
        """
        Get: Type(self: IChartGroup) -> int
        Set: Type(self: IChartGroup) = value
        """
        ...

    @property
    def UpBars(self) -> UpBars:
        """ Get: UpBars(self: IChartGroup) -> UpBars """
        ...

    @property
    def VaryByCategories(self) -> bool:
        """
        Get: VaryByCategories(self: IChartGroup) -> bool
        Set: VaryByCategories(self: IChartGroup) = value
        """
        ...


    def SeriesCollection(self, Index:object) -> object:
        """ SeriesCollection(self: IChartGroup, Index: object) -> object """
        ...


class IChartGroups(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IChartGroups) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: IChartGroups) -> int """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IChartGroups) -> XlCreator """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IChartGroups) -> object """
        ...


    def Item(self, Index:object) -> ChartGroup:
        """ Item(self: IChartGroups, Index: object) -> ChartGroup """
        ...


class IChartTitle: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IChartTitle) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: IChartTitle) -> object
        Set: AutoScaleFont(self: IChartTitle) = value
        """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IChartTitle) -> Border """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: IChartTitle) -> str
        Set: Caption(self: IChartTitle) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IChartTitle) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: IChartTitle) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: IChartTitle) -> Font """
        ...

    @property
    def HorizontalAlignment(self) -> object:
        """
        Get: HorizontalAlignment(self: IChartTitle) -> object
        Set: HorizontalAlignment(self: IChartTitle) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: IChartTitle) -> Interior """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: IChartTitle) -> float
        Set: Left(self: IChartTitle) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IChartTitle) -> str """
        ...

    @property
    def Orientation(self) -> object:
        """
        Get: Orientation(self: IChartTitle) -> object
        Set: Orientation(self: IChartTitle) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IChartTitle) -> object """
        ...

    @property
    def ReadingOrder(self) -> int:
        """
        Get: ReadingOrder(self: IChartTitle) -> int
        Set: ReadingOrder(self: IChartTitle) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: IChartTitle) -> bool
        Set: Shadow(self: IChartTitle) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: IChartTitle) -> str
        Set: Text(self: IChartTitle) = value
        """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: IChartTitle) -> float
        Set: Top(self: IChartTitle) = value
        """
        ...

    @property
    def VerticalAlignment(self) -> object:
        """
        Get: VerticalAlignment(self: IChartTitle) -> object
        Set: VerticalAlignment(self: IChartTitle) = value
        """
        ...


    def Delete(self) -> object:
        """ Delete(self: IChartTitle) -> object """
        ...


class IConnectorFormat: # skipped bases: <type 'object'>
    """ no doc """
    pass

class ICorners: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ICorners) -> Application """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ICorners) -> XlCreator """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ICorners) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ICorners) -> object """
        ...



class IDataLabel: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IDataLabel) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: IDataLabel) -> object
        Set: AutoScaleFont(self: IDataLabel) = value
        """
        ...

    @property
    def AutoText(self) -> bool:
        """
        Get: AutoText(self: IDataLabel) -> bool
        Set: AutoText(self: IDataLabel) = value
        """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IDataLabel) -> Border """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: IDataLabel) -> str
        Set: Caption(self: IDataLabel) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IDataLabel) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: IDataLabel) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: IDataLabel) -> Font """
        ...

    @property
    def HorizontalAlignment(self) -> object:
        """
        Get: HorizontalAlignment(self: IDataLabel) -> object
        Set: HorizontalAlignment(self: IDataLabel) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: IDataLabel) -> Interior """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: IDataLabel) -> float
        Set: Left(self: IDataLabel) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IDataLabel) -> str """
        ...

    @property
    def NumberFormat(self) -> str:
        """
        Get: NumberFormat(self: IDataLabel) -> str
        Set: NumberFormat(self: IDataLabel) = value
        """
        ...

    @property
    def NumberFormatLocal(self) -> object:
        """
        Get: NumberFormatLocal(self: IDataLabel) -> object
        Set: NumberFormatLocal(self: IDataLabel) = value
        """
        ...

    @property
    def Orientation(self) -> object:
        """
        Get: Orientation(self: IDataLabel) -> object
        Set: Orientation(self: IDataLabel) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IDataLabel) -> object """
        ...

    @property
    def Position(self) -> XlDataLabelPosition:
        """
        Get: Position(self: IDataLabel) -> XlDataLabelPosition
        Set: Position(self: IDataLabel) = value
        """
        ...

    @property
    def ReadingOrder(self) -> int:
        """
        Get: ReadingOrder(self: IDataLabel) -> int
        Set: ReadingOrder(self: IDataLabel) = value
        """
        ...

    @property
    def Separator(self) -> object:
        """
        Get: Separator(self: IDataLabel) -> object
        Set: Separator(self: IDataLabel) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: IDataLabel) -> bool
        Set: Shadow(self: IDataLabel) = value
        """
        ...

    @property
    def ShowBubbleSize(self) -> bool:
        """
        Get: ShowBubbleSize(self: IDataLabel) -> bool
        Set: ShowBubbleSize(self: IDataLabel) = value
        """
        ...

    @property
    def ShowCategoryName(self) -> bool:
        """
        Get: ShowCategoryName(self: IDataLabel) -> bool
        Set: ShowCategoryName(self: IDataLabel) = value
        """
        ...

    @property
    def ShowLegendKey(self) -> bool:
        """
        Get: ShowLegendKey(self: IDataLabel) -> bool
        Set: ShowLegendKey(self: IDataLabel) = value
        """
        ...

    @property
    def ShowPercentage(self) -> bool:
        """
        Get: ShowPercentage(self: IDataLabel) -> bool
        Set: ShowPercentage(self: IDataLabel) = value
        """
        ...

    @property
    def ShowSeriesName(self) -> bool:
        """
        Get: ShowSeriesName(self: IDataLabel) -> bool
        Set: ShowSeriesName(self: IDataLabel) = value
        """
        ...

    @property
    def ShowValue(self) -> bool:
        """
        Get: ShowValue(self: IDataLabel) -> bool
        Set: ShowValue(self: IDataLabel) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: IDataLabel) -> str
        Set: Text(self: IDataLabel) = value
        """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: IDataLabel) -> float
        Set: Top(self: IDataLabel) = value
        """
        ...

    @property
    def Type(self) -> object:
        """
        Get: Type(self: IDataLabel) -> object
        Set: Type(self: IDataLabel) = value
        """
        ...

    @property
    def VerticalAlignment(self) -> object:
        """
        Get: VerticalAlignment(self: IDataLabel) -> object
        Set: VerticalAlignment(self: IDataLabel) = value
        """
        ...


    def Delete(self) -> object:
        """ Delete(self: IDataLabel) -> object """
        ...


class IDataLabels(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IDataLabels) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: IDataLabels) -> object
        Set: AutoScaleFont(self: IDataLabels) = value
        """
        ...

    @property
    def AutoText(self) -> bool:
        """
        Get: AutoText(self: IDataLabels) -> bool
        Set: AutoText(self: IDataLabels) = value
        """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IDataLabels) -> Border """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: IDataLabels) -> int """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IDataLabels) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: IDataLabels) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: IDataLabels) -> Font """
        ...

    @property
    def HorizontalAlignment(self) -> object:
        """
        Get: HorizontalAlignment(self: IDataLabels) -> object
        Set: HorizontalAlignment(self: IDataLabels) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: IDataLabels) -> Interior """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IDataLabels) -> str """
        ...

    @property
    def NumberFormat(self) -> str:
        """
        Get: NumberFormat(self: IDataLabels) -> str
        Set: NumberFormat(self: IDataLabels) = value
        """
        ...

    @property
    def NumberFormatLocal(self) -> object:
        """
        Get: NumberFormatLocal(self: IDataLabels) -> object
        Set: NumberFormatLocal(self: IDataLabels) = value
        """
        ...

    @property
    def Orientation(self) -> object:
        """
        Get: Orientation(self: IDataLabels) -> object
        Set: Orientation(self: IDataLabels) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IDataLabels) -> object """
        ...

    @property
    def Position(self) -> XlDataLabelPosition:
        """
        Get: Position(self: IDataLabels) -> XlDataLabelPosition
        Set: Position(self: IDataLabels) = value
        """
        ...

    @property
    def ReadingOrder(self) -> int:
        """
        Get: ReadingOrder(self: IDataLabels) -> int
        Set: ReadingOrder(self: IDataLabels) = value
        """
        ...

    @property
    def Separator(self) -> object:
        """
        Get: Separator(self: IDataLabels) -> object
        Set: Separator(self: IDataLabels) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: IDataLabels) -> bool
        Set: Shadow(self: IDataLabels) = value
        """
        ...

    @property
    def ShowBubbleSize(self) -> bool:
        """
        Get: ShowBubbleSize(self: IDataLabels) -> bool
        Set: ShowBubbleSize(self: IDataLabels) = value
        """
        ...

    @property
    def ShowCategoryName(self) -> bool:
        """
        Get: ShowCategoryName(self: IDataLabels) -> bool
        Set: ShowCategoryName(self: IDataLabels) = value
        """
        ...

    @property
    def ShowLegendKey(self) -> bool:
        """
        Get: ShowLegendKey(self: IDataLabels) -> bool
        Set: ShowLegendKey(self: IDataLabels) = value
        """
        ...

    @property
    def ShowPercentage(self) -> bool:
        """
        Get: ShowPercentage(self: IDataLabels) -> bool
        Set: ShowPercentage(self: IDataLabels) = value
        """
        ...

    @property
    def ShowSeriesName(self) -> bool:
        """
        Get: ShowSeriesName(self: IDataLabels) -> bool
        Set: ShowSeriesName(self: IDataLabels) = value
        """
        ...

    @property
    def ShowValue(self) -> bool:
        """
        Get: ShowValue(self: IDataLabels) -> bool
        Set: ShowValue(self: IDataLabels) = value
        """
        ...

    @property
    def Type(self) -> object:
        """
        Get: Type(self: IDataLabels) -> object
        Set: Type(self: IDataLabels) = value
        """
        ...

    @property
    def VerticalAlignment(self) -> object:
        """
        Get: VerticalAlignment(self: IDataLabels) -> object
        Set: VerticalAlignment(self: IDataLabels) = value
        """
        ...


    def Delete(self) -> object:
        """ Delete(self: IDataLabels) -> object """
        ...

    def Item(self, Index:object) -> DataLabel:
        """ Item(self: IDataLabels, Index: object) -> DataLabel """
        ...

    def _Dummy11(self): # -> 
        """ _Dummy11(self: IDataLabels) """
        ...

    def _Dummy14(self): # -> 
        """ _Dummy14(self: IDataLabels) """
        ...

    def _Dummy15(self): # -> 
        """ _Dummy15(self: IDataLabels) """
        ...

    def _Dummy34(self): # -> 
        """ _Dummy34(self: IDataLabels) """
        ...

    def _Dummy8(self): # -> 
        """ _Dummy8(self: IDataLabels) """
        ...


class IDataSheet: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IDataSheet) -> Application """
        ...

    @property
    def Cells(self) -> Range:
        """ Get: Cells(self: IDataSheet) -> Range """
        ...

    @property
    def Columns(self) -> Range:
        """ Get: Columns(self: IDataSheet) -> Range """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IDataSheet) -> XlCreator """
        ...

    @property
    def Font(self) -> Font:
        """
        Get: Font(self: IDataSheet) -> Font
        Set: Font(self: IDataSheet) = value
        """
        ...

    @property
    def Height(self) -> float:
        """
        Get: Height(self: IDataSheet) -> float
        Set: Height(self: IDataSheet) = value
        """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: IDataSheet) -> float
        Set: Left(self: IDataSheet) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IDataSheet) -> object """
        ...

    @property
    def Rows(self) -> Range:
        """ Get: Rows(self: IDataSheet) -> Range """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: IDataSheet) -> float
        Set: Top(self: IDataSheet) = value
        """
        ...

    @property
    def Width(self) -> float:
        """
        Get: Width(self: IDataSheet) -> float
        Set: Width(self: IDataSheet) = value
        """
        ...


    def Activate(self): # -> 
        """ Activate(self: IDataSheet) """
        ...


class IDataTable: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IDataTable) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: IDataTable) -> object
        Set: AutoScaleFont(self: IDataTable) = value
        """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IDataTable) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IDataTable) -> XlCreator """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: IDataTable) -> Font """
        ...

    @property
    def HasBorderHorizontal(self) -> bool:
        """
        Get: HasBorderHorizontal(self: IDataTable) -> bool
        Set: HasBorderHorizontal(self: IDataTable) = value
        """
        ...

    @property
    def HasBorderOutline(self) -> bool:
        """
        Get: HasBorderOutline(self: IDataTable) -> bool
        Set: HasBorderOutline(self: IDataTable) = value
        """
        ...

    @property
    def HasBorderVertical(self) -> bool:
        """
        Get: HasBorderVertical(self: IDataTable) -> bool
        Set: HasBorderVertical(self: IDataTable) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IDataTable) -> object """
        ...

    @property
    def ShowLegendKey(self) -> bool:
        """
        Get: ShowLegendKey(self: IDataTable) -> bool
        Set: ShowLegendKey(self: IDataTable) = value
        """
        ...


    def Delete(self): # -> 
        """ Delete(self: IDataTable) """
        ...


class IDisplayUnitLabel: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IDisplayUnitLabel) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: IDisplayUnitLabel) -> object
        Set: AutoScaleFont(self: IDisplayUnitLabel) = value
        """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IDisplayUnitLabel) -> Border """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: IDisplayUnitLabel) -> str
        Set: Caption(self: IDisplayUnitLabel) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IDisplayUnitLabel) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: IDisplayUnitLabel) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: IDisplayUnitLabel) -> Font """
        ...

    @property
    def HorizontalAlignment(self) -> object:
        """
        Get: HorizontalAlignment(self: IDisplayUnitLabel) -> object
        Set: HorizontalAlignment(self: IDisplayUnitLabel) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: IDisplayUnitLabel) -> Interior """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: IDisplayUnitLabel) -> float
        Set: Left(self: IDisplayUnitLabel) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IDisplayUnitLabel) -> str """
        ...

    @property
    def Orientation(self) -> object:
        """
        Get: Orientation(self: IDisplayUnitLabel) -> object
        Set: Orientation(self: IDisplayUnitLabel) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IDisplayUnitLabel) -> object """
        ...

    @property
    def ReadingOrder(self) -> int:
        """
        Get: ReadingOrder(self: IDisplayUnitLabel) -> int
        Set: ReadingOrder(self: IDisplayUnitLabel) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: IDisplayUnitLabel) -> bool
        Set: Shadow(self: IDisplayUnitLabel) = value
        """
        ...

    @property
    def Text(self) -> str:
        """
        Get: Text(self: IDisplayUnitLabel) -> str
        Set: Text(self: IDisplayUnitLabel) = value
        """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: IDisplayUnitLabel) -> float
        Set: Top(self: IDisplayUnitLabel) = value
        """
        ...

    @property
    def VerticalAlignment(self) -> object:
        """
        Get: VerticalAlignment(self: IDisplayUnitLabel) -> object
        Set: VerticalAlignment(self: IDisplayUnitLabel) = value
        """
        ...


    def Delete(self) -> object:
        """ Delete(self: IDisplayUnitLabel) -> object """
        ...


class IDownBars: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IDownBars) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IDownBars) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IDownBars) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: IDownBars) -> ChartFillFormat """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: IDownBars) -> Interior """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IDownBars) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IDownBars) -> object """
        ...


    def Delete(self) -> object:
        """ Delete(self: IDownBars) -> object """
        ...


class IDropLines: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IDropLines) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IDropLines) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IDropLines) -> XlCreator """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IDropLines) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IDropLines) -> object """
        ...


    def Delete(self) -> object:
        """ Delete(self: IDropLines) -> object """
        ...


class IErrorBars: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IErrorBars) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IErrorBars) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IErrorBars) -> XlCreator """
        ...

    @property
    def EndStyle(self) -> XlEndStyleCap:
        """
        Get: EndStyle(self: IErrorBars) -> XlEndStyleCap
        Set: EndStyle(self: IErrorBars) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IErrorBars) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IErrorBars) -> object """
        ...


    def ClearFormats(self) -> object:
        """ ClearFormats(self: IErrorBars) -> object """
        ...

    def Delete(self) -> object:
        """ Delete(self: IErrorBars) -> object """
        ...


class IFloor: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IFloor) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IFloor) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IFloor) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: IFloor) -> ChartFillFormat """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: IFloor) -> Interior """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IFloor) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IFloor) -> object """
        ...

    @property
    def PictureType(self) -> object:
        """
        Get: PictureType(self: IFloor) -> object
        Set: PictureType(self: IFloor) = value
        """
        ...


    def ClearFormats(self) -> object:
        """ ClearFormats(self: IFloor) -> object """
        ...


class IFont: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IFont) -> Application """
        ...

    @property
    def Background(self) -> object:
        """
        Get: Background(self: IFont) -> object
        Set: Background(self: IFont) = value
        """
        ...

    @property
    def Bold(self) -> object:
        """
        Get: Bold(self: IFont) -> object
        Set: Bold(self: IFont) = value
        """
        ...

    @property
    def Color(self) -> object:
        """
        Get: Color(self: IFont) -> object
        Set: Color(self: IFont) = value
        """
        ...

    @property
    def ColorIndex(self) -> object:
        """
        Get: ColorIndex(self: IFont) -> object
        Set: ColorIndex(self: IFont) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IFont) -> XlCreator """
        ...

    @property
    def FontStyle(self) -> object:
        """
        Get: FontStyle(self: IFont) -> object
        Set: FontStyle(self: IFont) = value
        """
        ...

    @property
    def Italic(self) -> object:
        """
        Get: Italic(self: IFont) -> object
        Set: Italic(self: IFont) = value
        """
        ...

    @property
    def Name(self) -> object:
        """
        Get: Name(self: IFont) -> object
        Set: Name(self: IFont) = value
        """
        ...

    @property
    def OutlineFont(self) -> object:
        """
        Get: OutlineFont(self: IFont) -> object
        Set: OutlineFont(self: IFont) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IFont) -> object """
        ...

    @property
    def Shadow(self) -> object:
        """
        Get: Shadow(self: IFont) -> object
        Set: Shadow(self: IFont) = value
        """
        ...

    @property
    def Size(self) -> object:
        """
        Get: Size(self: IFont) -> object
        Set: Size(self: IFont) = value
        """
        ...

    @property
    def Strikethrough(self) -> object:
        """
        Get: Strikethrough(self: IFont) -> object
        Set: Strikethrough(self: IFont) = value
        """
        ...

    @property
    def Subscript(self) -> object:
        """
        Get: Subscript(self: IFont) -> object
        Set: Subscript(self: IFont) = value
        """
        ...

    @property
    def Superscript(self) -> object:
        """
        Get: Superscript(self: IFont) -> object
        Set: Superscript(self: IFont) = value
        """
        ...

    @property
    def ThemeColor(self) -> object:
        """
        Get: ThemeColor(self: IFont) -> object
        Set: ThemeColor(self: IFont) = value
        """
        ...

    @property
    def ThemeFont(self) -> XlThemeFont:
        """
        Get: ThemeFont(self: IFont) -> XlThemeFont
        Set: ThemeFont(self: IFont) = value
        """
        ...

    @property
    def TintAndShade(self) -> object:
        """
        Get: TintAndShade(self: IFont) -> object
        Set: TintAndShade(self: IFont) = value
        """
        ...

    @property
    def Underline(self) -> object:
        """
        Get: Underline(self: IFont) -> object
        Set: Underline(self: IFont) = value
        """
        ...



class IFreeformBuilder: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IGridlines: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IGridlines) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IGridlines) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IGridlines) -> XlCreator """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IGridlines) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IGridlines) -> object """
        ...


    def Delete(self) -> object:
        """ Delete(self: IGridlines) -> object """
        ...


class IGroupShapes: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IHiLoLines: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IHiLoLines) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IHiLoLines) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IHiLoLines) -> XlCreator """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IHiLoLines) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IHiLoLines) -> object """
        ...


    def Delete(self) -> object:
        """ Delete(self: IHiLoLines) -> object """
        ...


class IInterior: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IInterior) -> Application """
        ...

    @property
    def Color(self) -> object:
        """
        Get: Color(self: IInterior) -> object
        Set: Color(self: IInterior) = value
        """
        ...

    @property
    def ColorIndex(self) -> object:
        """
        Get: ColorIndex(self: IInterior) -> object
        Set: ColorIndex(self: IInterior) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IInterior) -> XlCreator """
        ...

    @property
    def Gradient(self) -> object:
        """ Get: Gradient(self: IInterior) -> object """
        ...

    @property
    def InvertIfNegative(self) -> object:
        """
        Get: InvertIfNegative(self: IInterior) -> object
        Set: InvertIfNegative(self: IInterior) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IInterior) -> object """
        ...

    @property
    def Pattern(self) -> object:
        """
        Get: Pattern(self: IInterior) -> object
        Set: Pattern(self: IInterior) = value
        """
        ...

    @property
    def PatternColor(self) -> object:
        """
        Get: PatternColor(self: IInterior) -> object
        Set: PatternColor(self: IInterior) = value
        """
        ...

    @property
    def PatternColorIndex(self) -> object:
        """
        Get: PatternColorIndex(self: IInterior) -> object
        Set: PatternColorIndex(self: IInterior) = value
        """
        ...

    @property
    def PatternThemeColor(self) -> object:
        """
        Get: PatternThemeColor(self: IInterior) -> object
        Set: PatternThemeColor(self: IInterior) = value
        """
        ...

    @property
    def PatternTintAndShade(self) -> object:
        """
        Get: PatternTintAndShade(self: IInterior) -> object
        Set: PatternTintAndShade(self: IInterior) = value
        """
        ...

    @property
    def ThemeColor(self) -> object:
        """
        Get: ThemeColor(self: IInterior) -> object
        Set: ThemeColor(self: IInterior) = value
        """
        ...

    @property
    def TintAndShade(self) -> object:
        """
        Get: TintAndShade(self: IInterior) -> object
        Set: TintAndShade(self: IInterior) = value
        """
        ...



class ILeaderLines: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ILeaderLines) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: ILeaderLines) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ILeaderLines) -> XlCreator """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ILeaderLines) -> object """
        ...


    def Delete(self): # -> 
        """ Delete(self: ILeaderLines) """
        ...


class ILegend: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ILegend) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: ILegend) -> object
        Set: AutoScaleFont(self: ILegend) = value
        """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: ILegend) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ILegend) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: ILegend) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: ILegend) -> Font """
        ...

    @property
    def Height(self) -> float:
        """
        Get: Height(self: ILegend) -> float
        Set: Height(self: ILegend) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: ILegend) -> Interior """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: ILegend) -> float
        Set: Left(self: ILegend) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ILegend) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ILegend) -> object """
        ...

    @property
    def Position(self) -> XlLegendPosition:
        """
        Get: Position(self: ILegend) -> XlLegendPosition
        Set: Position(self: ILegend) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: ILegend) -> bool
        Set: Shadow(self: ILegend) = value
        """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: ILegend) -> float
        Set: Top(self: ILegend) = value
        """
        ...

    @property
    def Width(self) -> float:
        """
        Get: Width(self: ILegend) -> float
        Set: Width(self: ILegend) = value
        """
        ...


    def Clear(self) -> object:
        """ Clear(self: ILegend) -> object """
        ...

    def Delete(self) -> object:
        """ Delete(self: ILegend) -> object """
        ...

    def LegendEntries(self, Index:object) -> object:
        """ LegendEntries(self: ILegend, Index: object) -> object """
        ...


class ILegendEntries(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ILegendEntries) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ILegendEntries) -> int """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ILegendEntries) -> XlCreator """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ILegendEntries) -> object """
        ...


    def Item(self, Index:object) -> LegendEntry:
        """ Item(self: ILegendEntries, Index: object) -> LegendEntry """
        ...


class ILegendEntry: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ILegendEntry) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: ILegendEntry) -> object
        Set: AutoScaleFont(self: ILegendEntry) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ILegendEntry) -> XlCreator """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: ILegendEntry) -> Font """
        ...

    @property
    def Height(self) -> float:
        """ Get: Height(self: ILegendEntry) -> float """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: ILegendEntry) -> int """
        ...

    @property
    def Left(self) -> float:
        """ Get: Left(self: ILegendEntry) -> float """
        ...

    @property
    def LegendKey(self) -> LegendKey:
        """ Get: LegendKey(self: ILegendEntry) -> LegendKey """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ILegendEntry) -> object """
        ...

    @property
    def Top(self) -> float:
        """ Get: Top(self: ILegendEntry) -> float """
        ...

    @property
    def Width(self) -> float:
        """ Get: Width(self: ILegendEntry) -> float """
        ...


    def Delete(self) -> object:
        """ Delete(self: ILegendEntry) -> object """
        ...


class ILegendKey: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ILegendKey) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: ILegendKey) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ILegendKey) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: ILegendKey) -> ChartFillFormat """
        ...

    @property
    def Height(self) -> float:
        """ Get: Height(self: ILegendKey) -> float """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: ILegendKey) -> Interior """
        ...

    @property
    def InvertIfNegative(self) -> bool:
        """
        Get: InvertIfNegative(self: ILegendKey) -> bool
        Set: InvertIfNegative(self: ILegendKey) = value
        """
        ...

    @property
    def Left(self) -> float:
        """ Get: Left(self: ILegendKey) -> float """
        ...

    @property
    def MarkerBackgroundColor(self) -> int:
        """
        Get: MarkerBackgroundColor(self: ILegendKey) -> int
        Set: MarkerBackgroundColor(self: ILegendKey) = value
        """
        ...

    @property
    def MarkerBackgroundColorIndex(self) -> XlColorIndex:
        """
        Get: MarkerBackgroundColorIndex(self: ILegendKey) -> XlColorIndex
        Set: MarkerBackgroundColorIndex(self: ILegendKey) = value
        """
        ...

    @property
    def MarkerForegroundColor(self) -> int:
        """
        Get: MarkerForegroundColor(self: ILegendKey) -> int
        Set: MarkerForegroundColor(self: ILegendKey) = value
        """
        ...

    @property
    def MarkerForegroundColorIndex(self) -> XlColorIndex:
        """
        Get: MarkerForegroundColorIndex(self: ILegendKey) -> XlColorIndex
        Set: MarkerForegroundColorIndex(self: ILegendKey) = value
        """
        ...

    @property
    def MarkerSize(self) -> int:
        """
        Get: MarkerSize(self: ILegendKey) -> int
        Set: MarkerSize(self: ILegendKey) = value
        """
        ...

    @property
    def MarkerStyle(self) -> XlMarkerStyle:
        """
        Get: MarkerStyle(self: ILegendKey) -> XlMarkerStyle
        Set: MarkerStyle(self: ILegendKey) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ILegendKey) -> object """
        ...

    @property
    def PictureType(self) -> int:
        """
        Get: PictureType(self: ILegendKey) -> int
        Set: PictureType(self: ILegendKey) = value
        """
        ...

    @property
    def PictureUnit(self) -> int:
        """
        Get: PictureUnit(self: ILegendKey) -> int
        Set: PictureUnit(self: ILegendKey) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: ILegendKey) -> bool
        Set: Shadow(self: ILegendKey) = value
        """
        ...

    @property
    def Smooth(self) -> bool:
        """
        Get: Smooth(self: ILegendKey) -> bool
        Set: Smooth(self: ILegendKey) = value
        """
        ...

    @property
    def Top(self) -> float:
        """ Get: Top(self: ILegendKey) -> float """
        ...

    @property
    def Width(self) -> float:
        """ Get: Width(self: ILegendKey) -> float """
        ...


    def ClearFormats(self) -> object:
        """ ClearFormats(self: ILegendKey) -> object """
        ...

    def Delete(self) -> object:
        """ Delete(self: ILegendKey) -> object """
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
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Interior) -> XlCreator """
        ...

    @property
    def Gradient(self) -> object:
        """ Get: Gradient(self: Interior) -> object """
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

    @property
    def PatternThemeColor(self) -> object:
        """
        Get: PatternThemeColor(self: Interior) -> object
        Set: PatternThemeColor(self: Interior) = value
        """
        ...

    @property
    def PatternTintAndShade(self) -> object:
        """
        Get: PatternTintAndShade(self: Interior) -> object
        Set: PatternTintAndShade(self: Interior) = value
        """
        ...

    @property
    def ThemeColor(self) -> object:
        """
        Get: ThemeColor(self: Interior) -> object
        Set: ThemeColor(self: Interior) = value
        """
        ...

    @property
    def TintAndShade(self) -> object:
        """
        Get: TintAndShade(self: Interior) -> object
        Set: TintAndShade(self: Interior) = value
        """
        ...



class IPlotArea: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IPlotArea) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IPlotArea) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IPlotArea) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: IPlotArea) -> ChartFillFormat """
        ...

    @property
    def Height(self) -> float:
        """
        Get: Height(self: IPlotArea) -> float
        Set: Height(self: IPlotArea) = value
        """
        ...

    @property
    def InsideHeight(self) -> float:
        """ Get: InsideHeight(self: IPlotArea) -> float """
        ...

    @property
    def InsideLeft(self) -> float:
        """ Get: InsideLeft(self: IPlotArea) -> float """
        ...

    @property
    def InsideTop(self) -> float:
        """ Get: InsideTop(self: IPlotArea) -> float """
        ...

    @property
    def InsideWidth(self) -> float:
        """ Get: InsideWidth(self: IPlotArea) -> float """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: IPlotArea) -> Interior """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: IPlotArea) -> float
        Set: Left(self: IPlotArea) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IPlotArea) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IPlotArea) -> object """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: IPlotArea) -> float
        Set: Top(self: IPlotArea) = value
        """
        ...

    @property
    def Width(self) -> float:
        """
        Get: Width(self: IPlotArea) -> float
        Set: Width(self: IPlotArea) = value
        """
        ...


    def ClearFormats(self) -> object:
        """ ClearFormats(self: IPlotArea) -> object """
        ...


class IPoint: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IPoint) -> Application """
        ...

    @property
    def ApplyPictToEnd(self) -> bool:
        """
        Get: ApplyPictToEnd(self: IPoint) -> bool
        Set: ApplyPictToEnd(self: IPoint) = value
        """
        ...

    @property
    def ApplyPictToFront(self) -> bool:
        """
        Get: ApplyPictToFront(self: IPoint) -> bool
        Set: ApplyPictToFront(self: IPoint) = value
        """
        ...

    @property
    def ApplyPictToSides(self) -> bool:
        """
        Get: ApplyPictToSides(self: IPoint) -> bool
        Set: ApplyPictToSides(self: IPoint) = value
        """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IPoint) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IPoint) -> XlCreator """
        ...

    @property
    def DataLabel(self) -> DataLabel:
        """ Get: DataLabel(self: IPoint) -> DataLabel """
        ...

    @property
    def Explosion(self) -> int:
        """
        Get: Explosion(self: IPoint) -> int
        Set: Explosion(self: IPoint) = value
        """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: IPoint) -> ChartFillFormat """
        ...

    @property
    def HasDataLabel(self) -> bool:
        """
        Get: HasDataLabel(self: IPoint) -> bool
        Set: HasDataLabel(self: IPoint) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: IPoint) -> Interior """
        ...

    @property
    def InvertIfNegative(self) -> bool:
        """
        Get: InvertIfNegative(self: IPoint) -> bool
        Set: InvertIfNegative(self: IPoint) = value
        """
        ...

    @property
    def MarkerBackgroundColor(self) -> int:
        """
        Get: MarkerBackgroundColor(self: IPoint) -> int
        Set: MarkerBackgroundColor(self: IPoint) = value
        """
        ...

    @property
    def MarkerBackgroundColorIndex(self) -> XlColorIndex:
        """
        Get: MarkerBackgroundColorIndex(self: IPoint) -> XlColorIndex
        Set: MarkerBackgroundColorIndex(self: IPoint) = value
        """
        ...

    @property
    def MarkerForegroundColor(self) -> int:
        """
        Get: MarkerForegroundColor(self: IPoint) -> int
        Set: MarkerForegroundColor(self: IPoint) = value
        """
        ...

    @property
    def MarkerForegroundColorIndex(self) -> XlColorIndex:
        """
        Get: MarkerForegroundColorIndex(self: IPoint) -> XlColorIndex
        Set: MarkerForegroundColorIndex(self: IPoint) = value
        """
        ...

    @property
    def MarkerSize(self) -> int:
        """
        Get: MarkerSize(self: IPoint) -> int
        Set: MarkerSize(self: IPoint) = value
        """
        ...

    @property
    def MarkerStyle(self) -> XlMarkerStyle:
        """
        Get: MarkerStyle(self: IPoint) -> XlMarkerStyle
        Set: MarkerStyle(self: IPoint) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IPoint) -> object """
        ...

    @property
    def PictureType(self) -> XlChartPictureType:
        """
        Get: PictureType(self: IPoint) -> XlChartPictureType
        Set: PictureType(self: IPoint) = value
        """
        ...

    @property
    def PictureUnit(self) -> int:
        """
        Get: PictureUnit(self: IPoint) -> int
        Set: PictureUnit(self: IPoint) = value
        """
        ...

    @property
    def SecondaryPlot(self) -> bool:
        """
        Get: SecondaryPlot(self: IPoint) -> bool
        Set: SecondaryPlot(self: IPoint) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: IPoint) -> bool
        Set: Shadow(self: IPoint) = value
        """
        ...


    def ApplyDataLabels(self, Type:XlDataLabelsType, LegendKey:object, AutoText:object, HasLeaderLines:object, ShowSeriesName:object, ShowCategoryName:object, ShowValue:object, ShowPercentage:object, ShowBubbleSize:object, Separator:object) -> object:
        """ ApplyDataLabels(self: IPoint, Type: XlDataLabelsType, LegendKey: object, AutoText: object, HasLeaderLines: object, ShowSeriesName: object, ShowCategoryName: object, ShowValue: object, ShowPercentage: object, ShowBubbleSize: object, Separator: object) -> object """
        ...

    def ClearFormats(self) -> object:
        """ ClearFormats(self: IPoint) -> object """
        ...

    def Delete(self) -> object:
        """ Delete(self: IPoint) -> object """
        ...

    def _ApplyDataLabels(self, Type:XlDataLabelsType, LegendKey:object, AutoText:object, HasLeaderLines:object) -> object:
        """ _ApplyDataLabels(self: IPoint, Type: XlDataLabelsType, LegendKey: object, AutoText: object, HasLeaderLines: object) -> object """
        ...


class IPoints(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IPoints) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: IPoints) -> int """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IPoints) -> XlCreator """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IPoints) -> object """
        ...


    def Item(self, Index:int) -> Point:
        """ Item(self: IPoints, Index: int) -> Point """
        ...


class IRange(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IRange) -> Application """
        ...

    @property
    def Cells(self) -> Range:
        """ Get: Cells(self: IRange) -> Range """
        ...

    @property
    def Columns(self) -> Range:
        """ Get: Columns(self: IRange) -> Range """
        ...

    @property
    def ColumnWidth(self) -> object:
        """
        Get: ColumnWidth(self: IRange) -> object
        Set: ColumnWidth(self: IRange) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IRange) -> XlCreator """
        ...

    @property
    def Include(self) -> object:
        """
        Get: Include(self: IRange) -> object
        Set: Include(self: IRange) = value
        """
        ...

    @property
    def NumberFormat(self) -> object:
        """
        Get: NumberFormat(self: IRange) -> object
        Set: NumberFormat(self: IRange) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IRange) -> object """
        ...

    @property
    def Rows(self) -> Range:
        """ Get: Rows(self: IRange) -> Range """
        ...


    def AutoFit(self): # -> 
        """ AutoFit(self: IRange) """
        ...

    def Clear(self): # -> 
        """ Clear(self: IRange) """
        ...

    def ClearContents(self): # -> 
        """ ClearContents(self: IRange) """
        ...

    def ClearFormats(self): # -> 
        """ ClearFormats(self: IRange) """
        ...

    def Copy(self, Destination:object): # -> 
        """ Copy(self: IRange, Destination: object) """
        ...

    def Cut(self, Destination:object): # -> 
        """ Cut(self: IRange, Destination: object) """
        ...

    def Delete(self, Shift:object): # -> 
        """ Delete(self: IRange, Shift: object) """
        ...

    def ImportData(self, FileName:object, Range:object): # -> 
        """ ImportData(self: IRange, FileName: object, Range: object) """
        ...

    def Insert(self, Shift:object): # -> 
        """ Insert(self: IRange, Shift: object) """
        ...

    def Paste(self, Link:object): # -> 
        """ Paste(self: IRange, Link: object) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ISeries: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ISeries) -> Application """
        ...

    @property
    def ApplyPictToEnd(self) -> bool:
        """
        Get: ApplyPictToEnd(self: ISeries) -> bool
        Set: ApplyPictToEnd(self: ISeries) = value
        """
        ...

    @property
    def ApplyPictToFront(self) -> bool:
        """
        Get: ApplyPictToFront(self: ISeries) -> bool
        Set: ApplyPictToFront(self: ISeries) = value
        """
        ...

    @property
    def ApplyPictToSides(self) -> bool:
        """
        Get: ApplyPictToSides(self: ISeries) -> bool
        Set: ApplyPictToSides(self: ISeries) = value
        """
        ...

    @property
    def AxisGroup(self) -> XlAxisGroup:
        """
        Get: AxisGroup(self: ISeries) -> XlAxisGroup
        Set: AxisGroup(self: ISeries) = value
        """
        ...

    @property
    def BarShape(self) -> XlBarShape:
        """
        Get: BarShape(self: ISeries) -> XlBarShape
        Set: BarShape(self: ISeries) = value
        """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: ISeries) -> Border """
        ...

    @property
    def ChartType(self) -> XlChartType:
        """
        Get: ChartType(self: ISeries) -> XlChartType
        Set: ChartType(self: ISeries) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ISeries) -> XlCreator """
        ...

    @property
    def ErrorBars(self) -> ErrorBars:
        """ Get: ErrorBars(self: ISeries) -> ErrorBars """
        ...

    @property
    def Explosion(self) -> int:
        """
        Get: Explosion(self: ISeries) -> int
        Set: Explosion(self: ISeries) = value
        """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: ISeries) -> ChartFillFormat """
        ...

    @property
    def Has3DEffect(self) -> bool:
        """
        Get: Has3DEffect(self: ISeries) -> bool
        Set: Has3DEffect(self: ISeries) = value
        """
        ...

    @property
    def HasDataLabels(self) -> bool:
        """
        Get: HasDataLabels(self: ISeries) -> bool
        Set: HasDataLabels(self: ISeries) = value
        """
        ...

    @property
    def HasErrorBars(self) -> bool:
        """
        Get: HasErrorBars(self: ISeries) -> bool
        Set: HasErrorBars(self: ISeries) = value
        """
        ...

    @property
    def HasLeaderLines(self) -> bool:
        """
        Get: HasLeaderLines(self: ISeries) -> bool
        Set: HasLeaderLines(self: ISeries) = value
        """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: ISeries) -> Interior """
        ...

    @property
    def InvertIfNegative(self) -> bool:
        """
        Get: InvertIfNegative(self: ISeries) -> bool
        Set: InvertIfNegative(self: ISeries) = value
        """
        ...

    @property
    def LeaderLines(self) -> LeaderLines:
        """ Get: LeaderLines(self: ISeries) -> LeaderLines """
        ...

    @property
    def MarkerBackgroundColor(self) -> int:
        """
        Get: MarkerBackgroundColor(self: ISeries) -> int
        Set: MarkerBackgroundColor(self: ISeries) = value
        """
        ...

    @property
    def MarkerBackgroundColorIndex(self) -> XlColorIndex:
        """
        Get: MarkerBackgroundColorIndex(self: ISeries) -> XlColorIndex
        Set: MarkerBackgroundColorIndex(self: ISeries) = value
        """
        ...

    @property
    def MarkerForegroundColor(self) -> int:
        """
        Get: MarkerForegroundColor(self: ISeries) -> int
        Set: MarkerForegroundColor(self: ISeries) = value
        """
        ...

    @property
    def MarkerForegroundColorIndex(self) -> XlColorIndex:
        """
        Get: MarkerForegroundColorIndex(self: ISeries) -> XlColorIndex
        Set: MarkerForegroundColorIndex(self: ISeries) = value
        """
        ...

    @property
    def MarkerSize(self) -> int:
        """
        Get: MarkerSize(self: ISeries) -> int
        Set: MarkerSize(self: ISeries) = value
        """
        ...

    @property
    def MarkerStyle(self) -> XlMarkerStyle:
        """
        Get: MarkerStyle(self: ISeries) -> XlMarkerStyle
        Set: MarkerStyle(self: ISeries) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ISeries) -> object """
        ...

    @property
    def PictureType(self) -> XlChartPictureType:
        """
        Get: PictureType(self: ISeries) -> XlChartPictureType
        Set: PictureType(self: ISeries) = value
        """
        ...

    @property
    def PictureUnit(self) -> int:
        """
        Get: PictureUnit(self: ISeries) -> int
        Set: PictureUnit(self: ISeries) = value
        """
        ...

    @property
    def Shadow(self) -> bool:
        """
        Get: Shadow(self: ISeries) -> bool
        Set: Shadow(self: ISeries) = value
        """
        ...

    @property
    def Smooth(self) -> bool:
        """
        Get: Smooth(self: ISeries) -> bool
        Set: Smooth(self: ISeries) = value
        """
        ...

    @property
    def Type(self) -> int:
        """
        Get: Type(self: ISeries) -> int
        Set: Type(self: ISeries) = value
        """
        ...


    def ApplyCustomType(self, ChartType:XlChartType): # -> 
        """ ApplyCustomType(self: ISeries, ChartType: XlChartType) """
        ...

    def ApplyDataLabels(self, Type:XlDataLabelsType, LegendKey:object, AutoText:object, HasLeaderLines:object, ShowSeriesName:object, ShowCategoryName:object, ShowValue:object, ShowPercentage:object, ShowBubbleSize:object, Separator:object) -> object:
        """ ApplyDataLabels(self: ISeries, Type: XlDataLabelsType, LegendKey: object, AutoText: object, HasLeaderLines: object, ShowSeriesName: object, ShowCategoryName: object, ShowValue: object, ShowPercentage: object, ShowBubbleSize: object, Separator: object) -> object """
        ...

    def ClearFormats(self) -> object:
        """ ClearFormats(self: ISeries) -> object """
        ...

    def DataLabels(self, Index:object) -> object:
        """ DataLabels(self: ISeries, Index: object) -> object """
        ...

    def Delete(self) -> object:
        """ Delete(self: ISeries) -> object """
        ...

    def ErrorBar(self, Direction:XlErrorBarDirection, Include:XlErrorBarInclude, Type:XlErrorBarType, Amount:object, MinusValues:object) -> object:
        """ ErrorBar(self: ISeries, Direction: XlErrorBarDirection, Include: XlErrorBarInclude, Type: XlErrorBarType, Amount: object, MinusValues: object) -> object """
        ...

    def Points(self, Index:object) -> object:
        """ Points(self: ISeries, Index: object) -> object """
        ...

    def Trendlines(self, Index:object) -> object:
        """ Trendlines(self: ISeries, Index: object) -> object """
        ...

    def _ApplyDataLabels(self, Type:XlDataLabelsType, LegendKey:object, AutoText:object, HasLeaderLines:object) -> object:
        """ _ApplyDataLabels(self: ISeries, Type: XlDataLabelsType, LegendKey: object, AutoText: object, HasLeaderLines: object) -> object """
        ...


class ISeriesCollection(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ISeriesCollection) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ISeriesCollection) -> int """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ISeriesCollection) -> XlCreator """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ISeriesCollection) -> object """
        ...


    def Item(self, Index:object) -> Series:
        """ Item(self: ISeriesCollection, Index: object) -> Series """
        ...


class ISeriesLines: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ISeriesLines) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: ISeriesLines) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ISeriesLines) -> XlCreator """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ISeriesLines) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ISeriesLines) -> object """
        ...


    def Delete(self) -> object:
        """ Delete(self: ISeriesLines) -> object """
        ...


class IShape: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IShapeRange: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IShapes: # skipped bases: <type 'object'>
    """ no doc """
    pass

class ITextFrame: # skipped bases: <type 'object'>
    """ no doc """
    pass

class ITickLabels: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ITickLabels) -> Application """
        ...

    @property
    def AutoScaleFont(self) -> object:
        """
        Get: AutoScaleFont(self: ITickLabels) -> object
        Set: AutoScaleFont(self: ITickLabels) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ITickLabels) -> XlCreator """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: ITickLabels) -> Font """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ITickLabels) -> str """
        ...

    @property
    def NumberFormat(self) -> str:
        """
        Get: NumberFormat(self: ITickLabels) -> str
        Set: NumberFormat(self: ITickLabels) = value
        """
        ...

    @property
    def NumberFormatLocal(self) -> object:
        """
        Get: NumberFormatLocal(self: ITickLabels) -> object
        Set: NumberFormatLocal(self: ITickLabels) = value
        """
        ...

    @property
    def Offset(self) -> int:
        """
        Get: Offset(self: ITickLabels) -> int
        Set: Offset(self: ITickLabels) = value
        """
        ...

    @property
    def Orientation(self) -> XlTickLabelOrientation:
        """
        Get: Orientation(self: ITickLabels) -> XlTickLabelOrientation
        Set: Orientation(self: ITickLabels) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ITickLabels) -> object """
        ...

    @property
    def ReadingOrder(self) -> int:
        """
        Get: ReadingOrder(self: ITickLabels) -> int
        Set: ReadingOrder(self: ITickLabels) = value
        """
        ...


    def Delete(self) -> object:
        """ Delete(self: ITickLabels) -> object """
        ...


class ITrendline: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ITrendline) -> Application """
        ...

    @property
    def Backward(self) -> int:
        """
        Get: Backward(self: ITrendline) -> int
        Set: Backward(self: ITrendline) = value
        """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: ITrendline) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ITrendline) -> XlCreator """
        ...

    @property
    def DataLabel(self) -> DataLabel:
        """ Get: DataLabel(self: ITrendline) -> DataLabel """
        ...

    @property
    def DisplayEquation(self) -> bool:
        """
        Get: DisplayEquation(self: ITrendline) -> bool
        Set: DisplayEquation(self: ITrendline) = value
        """
        ...

    @property
    def DisplayRSquared(self) -> bool:
        """
        Get: DisplayRSquared(self: ITrendline) -> bool
        Set: DisplayRSquared(self: ITrendline) = value
        """
        ...

    @property
    def Forward(self) -> int:
        """
        Get: Forward(self: ITrendline) -> int
        Set: Forward(self: ITrendline) = value
        """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: ITrendline) -> int """
        ...

    @property
    def Intercept(self) -> float:
        """
        Get: Intercept(self: ITrendline) -> float
        Set: Intercept(self: ITrendline) = value
        """
        ...

    @property
    def InterceptIsAuto(self) -> bool:
        """
        Get: InterceptIsAuto(self: ITrendline) -> bool
        Set: InterceptIsAuto(self: ITrendline) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ITrendline) -> str
        Set: Name(self: ITrendline) = value
        """
        ...

    @property
    def NameIsAuto(self) -> bool:
        """
        Get: NameIsAuto(self: ITrendline) -> bool
        Set: NameIsAuto(self: ITrendline) = value
        """
        ...

    @property
    def Order(self) -> int:
        """
        Get: Order(self: ITrendline) -> int
        Set: Order(self: ITrendline) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ITrendline) -> object """
        ...

    @property
    def Period(self) -> int:
        """
        Get: Period(self: ITrendline) -> int
        Set: Period(self: ITrendline) = value
        """
        ...

    @property
    def Type(self) -> XlTrendlineType:
        """
        Get: Type(self: ITrendline) -> XlTrendlineType
        Set: Type(self: ITrendline) = value
        """
        ...


    def ClearFormats(self) -> object:
        """ ClearFormats(self: ITrendline) -> object """
        ...

    def Delete(self) -> object:
        """ Delete(self: ITrendline) -> object """
        ...


class ITrendlines(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: ITrendlines) -> Application """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ITrendlines) -> int """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: ITrendlines) -> XlCreator """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ITrendlines) -> object """
        ...


    def Add(self, Type:XlTrendlineType, Order:object, Period:object, Forward:object, Backward:object, Intercept:object, DisplayEquation:object, DisplayRSquared:object, Name:object) -> Trendline:
        """ Add(self: ITrendlines, Type: XlTrendlineType, Order: object, Period: object, Forward: object, Backward: object, Intercept: object, DisplayEquation: object, DisplayRSquared: object, Name: object) -> Trendline """
        ...

    def Item(self, Index:object) -> Trendline:
        """ Item(self: ITrendlines, Index: object) -> Trendline """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class IUpBars: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IUpBars) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IUpBars) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IUpBars) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: IUpBars) -> ChartFillFormat """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: IUpBars) -> Interior """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IUpBars) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IUpBars) -> object """
        ...


    def Delete(self) -> object:
        """ Delete(self: IUpBars) -> object """
        ...


class IWalls: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: IWalls) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: IWalls) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: IWalls) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: IWalls) -> ChartFillFormat """
        ...

    @property
    def Interior(self) -> Interior:
        """ Get: Interior(self: IWalls) -> Interior """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IWalls) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: IWalls) -> object """
        ...

    @property
    def PictureType(self) -> object:
        """
        Get: PictureType(self: IWalls) -> object
        Set: PictureType(self: IWalls) = value
        """
        ...

    @property
    def PictureUnit(self) -> object:
        """
        Get: PictureUnit(self: IWalls) -> object
        Set: PictureUnit(self: IWalls) = value
        """
        ...


    def ClearFormats(self) -> object:
        """ ClearFormats(self: IWalls) -> object """
        ...


class LeaderLines: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: LeaderLines) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: LeaderLines) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: LeaderLines) -> XlCreator """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: LeaderLines) -> object """
        ...


    def Delete(self): # -> 
        """ Delete(self: LeaderLines) """
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
    def Border(self) -> Border:
        """ Get: Border(self: Legend) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Legend) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: Legend) -> ChartFillFormat """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: Legend) -> Font """
        ...

    @property
    def Height(self) -> float:
        """
        Get: Height(self: Legend) -> float
        Set: Height(self: Legend) = value
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
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: LegendEntries) -> XlCreator """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: LegendEntries) -> object """
        ...


    def Item(self, Index:object) -> LegendEntry:
        """ Item(self: LegendEntries, Index: object) -> LegendEntry """
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
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: LegendEntry) -> XlCreator """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: LegendEntry) -> Font """
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


class LegendKey: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: LegendKey) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: LegendKey) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: LegendKey) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: LegendKey) -> ChartFillFormat """
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


class PlotArea: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: PlotArea) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: PlotArea) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: PlotArea) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: PlotArea) -> ChartFillFormat """
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
        """ Get: InsideHeight(self: PlotArea) -> float """
        ...

    @property
    def InsideLeft(self) -> float:
        """ Get: InsideLeft(self: PlotArea) -> float """
        ...

    @property
    def InsideTop(self) -> float:
        """ Get: InsideTop(self: PlotArea) -> float """
        ...

    @property
    def InsideWidth(self) -> float:
        """ Get: InsideWidth(self: PlotArea) -> float """
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
    def Border(self) -> Border:
        """ Get: Border(self: Point) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Point) -> XlCreator """
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
    def HasDataLabel(self) -> bool:
        """
        Get: HasDataLabel(self: Point) -> bool
        Set: HasDataLabel(self: Point) = value
        """
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


    def ApplyDataLabels(self, Type:XlDataLabelsType, LegendKey:object, AutoText:object, HasLeaderLines:object, ShowSeriesName:object, ShowCategoryName:object, ShowValue:object, ShowPercentage:object, ShowBubbleSize:object, Separator:object) -> object:
        """ ApplyDataLabels(self: Point, Type: XlDataLabelsType, LegendKey: object, AutoText: object, HasLeaderLines: object, ShowSeriesName: object, ShowCategoryName: object, ShowValue: object, ShowPercentage: object, ShowBubbleSize: object, Separator: object) -> object """
        ...

    def ClearFormats(self) -> object:
        """ ClearFormats(self: Point) -> object """
        ...

    def Delete(self) -> object:
        """ Delete(self: Point) -> object """
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
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Points) -> XlCreator """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Points) -> object """
        ...


    def Item(self, Index:int) -> Point:
        """ Item(self: Points, Index: int) -> Point """
        ...


class Range(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Range) -> Application """
        ...

    @property
    def Cells(self) -> Range:
        """ Get: Cells(self: Range) -> Range """
        ...

    @property
    def Columns(self) -> Range:
        """ Get: Columns(self: Range) -> Range """
        ...

    @property
    def ColumnWidth(self) -> object:
        """
        Get: ColumnWidth(self: Range) -> object
        Set: ColumnWidth(self: Range) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Range) -> XlCreator """
        ...

    @property
    def Include(self) -> object:
        """
        Get: Include(self: Range) -> object
        Set: Include(self: Range) = value
        """
        ...

    @property
    def NumberFormat(self) -> object:
        """
        Get: NumberFormat(self: Range) -> object
        Set: NumberFormat(self: Range) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: Range) -> object """
        ...

    @property
    def Rows(self) -> Range:
        """ Get: Rows(self: Range) -> Range """
        ...


    def AutoFit(self): # -> 
        """ AutoFit(self: Range) """
        ...

    def Clear(self): # -> 
        """ Clear(self: Range) """
        ...

    def ClearContents(self): # -> 
        """ ClearContents(self: Range) """
        ...

    def ClearFormats(self): # -> 
        """ ClearFormats(self: Range) """
        ...

    def Copy(self, Destination:object): # -> 
        """ Copy(self: Range, Destination: object) """
        ...

    def Cut(self, Destination:object): # -> 
        """ Cut(self: Range, Destination: object) """
        ...

    def Delete(self, Shift:object): # -> 
        """ Delete(self: Range, Shift: object) """
        ...

    def ImportData(self, FileName:object, Range:object): # -> 
        """ ImportData(self: Range, FileName: object, Range: object) """
        ...

    def Insert(self, Shift:object): # -> 
        """ Insert(self: Range, Shift: object) """
        ...

    def Paste(self, Link:object): # -> 
        """ Paste(self: Range, Link: object) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
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
    def Border(self) -> Border:
        """ Get: Border(self: Series) -> Border """
        ...

    @property
    def ChartType(self) -> XlChartType:
        """
        Get: ChartType(self: Series) -> XlChartType
        Set: ChartType(self: Series) = value
        """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Series) -> XlCreator """
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
    def InvertIfNegative(self) -> bool:
        """
        Get: InvertIfNegative(self: Series) -> bool
        Set: InvertIfNegative(self: Series) = value
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


    def ApplyCustomType(self, ChartType:XlChartType): # -> 
        """ ApplyCustomType(self: Series, ChartType: XlChartType) """
        ...

    def ApplyDataLabels(self, Type:XlDataLabelsType, LegendKey:object, AutoText:object, HasLeaderLines:object, ShowSeriesName:object, ShowCategoryName:object, ShowValue:object, ShowPercentage:object, ShowBubbleSize:object, Separator:object) -> object:
        """ ApplyDataLabels(self: Series, Type: XlDataLabelsType, LegendKey: object, AutoText: object, HasLeaderLines: object, ShowSeriesName: object, ShowCategoryName: object, ShowValue: object, ShowPercentage: object, ShowBubbleSize: object, Separator: object) -> object """
        ...

    def ClearFormats(self) -> object:
        """ ClearFormats(self: Series) -> object """
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

    def Points(self, Index:object) -> object:
        """ Points(self: Series, Index: object) -> object """
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
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: SeriesCollection) -> XlCreator """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: SeriesCollection) -> object """
        ...


    def Item(self, Index:object) -> Series:
        """ Item(self: SeriesCollection, Index: object) -> Series """
        ...


class SeriesLines: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: SeriesLines) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: SeriesLines) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: SeriesLines) -> XlCreator """
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


class TickLabels: # skipped bases: <type 'object'>
    """ no doc """
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
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: TickLabels) -> XlCreator """
        ...

    @property
    def Font(self) -> Font:
        """ Get: Font(self: TickLabels) -> Font """
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
    def Border(self) -> Border:
        """ Get: Border(self: Trendline) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Trendline) -> XlCreator """
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
    def Forward(self) -> int:
        """
        Get: Forward(self: Trendline) -> int
        Set: Forward(self: Trendline) = value
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
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Trendlines) -> XlCreator """
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
    def Border(self) -> Border:
        """ Get: Border(self: UpBars) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: UpBars) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: UpBars) -> ChartFillFormat """
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


class Walls: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: Walls) -> Application """
        ...

    @property
    def Border(self) -> Border:
        """ Get: Border(self: Walls) -> Border """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: Walls) -> XlCreator """
        ...

    @property
    def Fill(self) -> ChartFillFormat:
        """ Get: Fill(self: Walls) -> ChartFillFormat """
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


    def ClearFormats(self) -> object:
        """ ClearFormats(self: Walls) -> object """
        ...


class XlAllocation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlAllocation, values: xlAutomaticAllocation (2), xlManualAllocation (1) """
    value__ = ...
    xlAutomaticAllocation: XlAllocation = ...
    xlManualAllocation: XlAllocation = ...


class XlAllocationMethod(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlAllocationMethod, values: xlEqualAllocation (1), xlWeightedAllocation (2) """
    value__ = ...
    xlEqualAllocation: XlAllocationMethod = ...
    xlWeightedAllocation: XlAllocationMethod = ...


class XlAllocationValue(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlAllocationValue, values: xlAllocateIncrement (2), xlAllocateValue (1) """
    value__ = ...
    xlAllocateIncrement: XlAllocationValue = ...
    xlAllocateValue: XlAllocationValue = ...


class XlArabicModes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlArabicModes, values: xlArabicBothStrict (3), xlArabicNone (0), xlArabicStrictAlefHamza (1), xlArabicStrictFinalYaa (2) """
    value__ = ...
    xlArabicBothStrict: XlArabicModes = ...
    xlArabicNone: XlArabicModes = ...
    xlArabicStrictAlefHamza: XlArabicModes = ...
    xlArabicStrictFinalYaa: XlArabicModes = ...


class XlArrowHeadLength(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlArrowHeadLength, values: xlArrowHeadLengthLong (3), xlArrowHeadLengthMedium (-4138), xlArrowHeadLengthShort (1) """
    value__ = ...
    xlArrowHeadLengthLong: XlArrowHeadLength = ...
    xlArrowHeadLengthMedium: XlArrowHeadLength = ...
    xlArrowHeadLengthShort: XlArrowHeadLength = ...


class XlArrowHeadStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlArrowHeadStyle, values: xlArrowHeadStyleClosed (3), xlArrowHeadStyleDoubleClosed (5), xlArrowHeadStyleDoubleOpen (4), xlArrowHeadStyleNone (-4142), xlArrowHeadStyleOpen (2) """
    value__ = ...
    xlArrowHeadStyleClosed: XlArrowHeadStyle = ...
    xlArrowHeadStyleDoubleClosed: XlArrowHeadStyle = ...
    xlArrowHeadStyleDoubleOpen: XlArrowHeadStyle = ...
    xlArrowHeadStyleNone: XlArrowHeadStyle = ...
    xlArrowHeadStyleOpen: XlArrowHeadStyle = ...


class XlArrowHeadWidth(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlArrowHeadWidth, values: xlArrowHeadWidthMedium (-4138), xlArrowHeadWidthNarrow (1), xlArrowHeadWidthWide (3) """
    value__ = ...
    xlArrowHeadWidthMedium: XlArrowHeadWidth = ...
    xlArrowHeadWidthNarrow: XlArrowHeadWidth = ...
    xlArrowHeadWidthWide: XlArrowHeadWidth = ...


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


class XlCalculatedMemberType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlCalculatedMemberType, values: xlCalculatedMember (0), xlCalculatedSet (1) """
    value__ = ...
    xlCalculatedMember: XlCalculatedMemberType = ...
    xlCalculatedSet: XlCalculatedMemberType = ...


class XlCategoryType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlCategoryType, values: xlAutomaticScale (-4105), xlCategoryScale (2), xlTimeScale (3) """
    value__ = ...
    xlAutomaticScale: XlCategoryType = ...
    xlCategoryScale: XlCategoryType = ...
    xlTimeScale: XlCategoryType = ...


class XlCellChangedState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlCellChangedState, values: xlCellChangeApplied (3), xlCellChanged (2), xlCellNotChanged (1) """
    value__ = ...
    xlCellChangeApplied: XlCellChangedState = ...
    xlCellChanged: XlCellChangedState = ...
    xlCellNotChanged: XlCellChangedState = ...


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


class XlChartType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlChartType, values: xl3DArea (-4098), xl3DAreaStacked (78), xl3DAreaStacked100 (79), xl3DBarClustered (60), xl3DBarStacked (61), xl3DBarStacked100 (62), xl3DColumn (-4100), xl3DColumnClustered (54), xl3DColumnStacked (55), xl3DColumnStacked100 (56), xl3DLine (-4101), xl3DPie (-4102), xl3DPieExploded (70), xlArea (1), xlAreaStacked (76), xlAreaStacked100 (77), xlBarClustered (57), xlBarOfPie (71), xlBarStacked (58), xlBarStacked100 (59), xlBubble (15), xlBubble3DEffect (87), xlColumnClustered (51), xlColumnStacked (52), xlColumnStacked100 (53), xlConeBarClustered (102), xlConeBarStacked (103), xlConeBarStacked100 (104), xlConeCol (105), xlConeColClustered (99), xlConeColStacked (100), xlConeColStacked100 (101), xlCylinderBarClustered (95), xlCylinderBarStacked (96), xlCylinderBarStacked100 (97), xlCylinderCol (98), xlCylinderColClustered (92), xlCylinderColStacked (93), xlCylinderColStacked100 (94), xlDoughnut (-4120), xlDoughnutExploded (80), xlLine (4), xlLineMarkers (65), xlLineMarkersStacked (66), xlLineMarkersStacked100 (67), xlLineStacked (63), xlLineStacked100 (64), xlPie (5), xlPieExploded (69), xlPieOfPie (68), xlPyramidBarClustered (109), xlPyramidBarStacked (110), xlPyramidBarStacked100 (111), xlPyramidCol (112), xlPyramidColClustered (106), xlPyramidColStacked (107), xlPyramidColStacked100 (108), xlRadar (-4151), xlRadarFilled (82), xlRadarMarkers (81), xlStockHLC (88), xlStockOHLC (89), xlStockVHLC (90), xlStockVOHLC (91), xlSurface (83), xlSurfaceTopView (85), xlSurfaceTopViewWireframe (86), xlSurfaceWireframe (84), xlXYScatter (-4169), xlXYScatterLines (74), xlXYScatterLinesNoMarkers (75), xlXYScatterSmooth (72), xlXYScatterSmoothNoMarkers (73) """
    value__ = ...
    xl3DArea: XlChartType = ...
    xl3DAreaStacked: XlChartType = ...
    xl3DAreaStacked100: XlChartType = ...
    xl3DBarClustered: XlChartType = ...
    xl3DBarStacked: XlChartType = ...
    xl3DBarStacked100: XlChartType = ...
    xl3DColumn: XlChartType = ...
    xl3DColumnClustered: XlChartType = ...
    xl3DColumnStacked: XlChartType = ...
    xl3DColumnStacked100: XlChartType = ...
    xl3DLine: XlChartType = ...
    xl3DPie: XlChartType = ...
    xl3DPieExploded: XlChartType = ...
    xlArea: XlChartType = ...
    xlAreaStacked: XlChartType = ...
    xlAreaStacked100: XlChartType = ...
    xlBarClustered: XlChartType = ...
    xlBarOfPie: XlChartType = ...
    xlBarStacked: XlChartType = ...
    xlBarStacked100: XlChartType = ...
    xlBubble: XlChartType = ...
    xlBubble3DEffect: XlChartType = ...
    xlColumnClustered: XlChartType = ...
    xlColumnStacked: XlChartType = ...
    xlColumnStacked100: XlChartType = ...
    xlConeBarClustered: XlChartType = ...
    xlConeBarStacked: XlChartType = ...
    xlConeBarStacked100: XlChartType = ...
    xlConeCol: XlChartType = ...
    xlConeColClustered: XlChartType = ...
    xlConeColStacked: XlChartType = ...
    xlConeColStacked100: XlChartType = ...
    xlCylinderBarClustered: XlChartType = ...
    xlCylinderBarStacked: XlChartType = ...
    xlCylinderBarStacked100: XlChartType = ...
    xlCylinderCol: XlChartType = ...
    xlCylinderColClustered: XlChartType = ...
    xlCylinderColStacked: XlChartType = ...
    xlCylinderColStacked100: XlChartType = ...
    xlDoughnut: XlChartType = ...
    xlDoughnutExploded: XlChartType = ...
    xlLine: XlChartType = ...
    xlLineMarkers: XlChartType = ...
    xlLineMarkersStacked: XlChartType = ...
    xlLineMarkersStacked100: XlChartType = ...
    xlLineStacked: XlChartType = ...
    xlLineStacked100: XlChartType = ...
    xlPie: XlChartType = ...
    xlPieExploded: XlChartType = ...
    xlPieOfPie: XlChartType = ...
    xlPyramidBarClustered: XlChartType = ...
    xlPyramidBarStacked: XlChartType = ...
    xlPyramidBarStacked100: XlChartType = ...
    xlPyramidCol: XlChartType = ...
    xlPyramidColClustered: XlChartType = ...
    xlPyramidColStacked: XlChartType = ...
    xlPyramidColStacked100: XlChartType = ...
    xlRadar: XlChartType = ...
    xlRadarFilled: XlChartType = ...
    xlRadarMarkers: XlChartType = ...
    xlStockHLC: XlChartType = ...
    xlStockOHLC: XlChartType = ...
    xlStockVHLC: XlChartType = ...
    xlStockVOHLC: XlChartType = ...
    xlSurface: XlChartType = ...
    xlSurfaceTopView: XlChartType = ...
    xlSurfaceTopViewWireframe: XlChartType = ...
    xlSurfaceWireframe: XlChartType = ...
    xlXYScatter: XlChartType = ...
    xlXYScatterLines: XlChartType = ...
    xlXYScatterLinesNoMarkers: XlChartType = ...
    xlXYScatterSmooth: XlChartType = ...
    xlXYScatterSmoothNoMarkers: XlChartType = ...


class XlCmdType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlCmdType, values: xlCmdCube (1), xlCmdDefault (4), xlCmdSql (2), xlCmdTable (3) """
    value__ = ...
    xlCmdCube: XlCmdType = ...
    xlCmdDefault: XlCmdType = ...
    xlCmdSql: XlCmdType = ...
    xlCmdTable: XlCmdType = ...


class XlColorIndex(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlColorIndex, values: xlColorIndexAutomatic (-4105), xlColorIndexNone (-4142) """
    value__ = ...
    xlColorIndexAutomatic: XlColorIndex = ...
    xlColorIndexNone: XlColorIndex = ...


class XlColumnDataType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlColumnDataType, values: xlDMYFormat (4), xlDYMFormat (7), xlEMDFormat (10), xlGeneralFormat (1), xlMDYFormat (3), xlMYDFormat (6), xlSkipColumn (9), xlTextFormat (2), xlYDMFormat (8), xlYMDFormat (5) """
    value__ = ...
    xlDMYFormat: XlColumnDataType = ...
    xlDYMFormat: XlColumnDataType = ...
    xlEMDFormat: XlColumnDataType = ...
    xlGeneralFormat: XlColumnDataType = ...
    xlMDYFormat: XlColumnDataType = ...
    xlMYDFormat: XlColumnDataType = ...
    xlSkipColumn: XlColumnDataType = ...
    xlTextFormat: XlColumnDataType = ...
    xlYDMFormat: XlColumnDataType = ...
    xlYMDFormat: XlColumnDataType = ...


class XlConsolidationFunction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlConsolidationFunction, values: xlAverage (-4106), xlCount (-4112), xlCountNums (-4113), xlMax (-4136), xlMin (-4139), xlProduct (-4149), xlStDev (-4155), xlStDevP (-4156), xlSum (-4157), xlUnknown (1000), xlVar (-4164), xlVarP (-4165) """
    value__ = ...
    xlAverage: XlConsolidationFunction = ...
    xlCount: XlConsolidationFunction = ...
    xlCountNums: XlConsolidationFunction = ...
    xlMax: XlConsolidationFunction = ...
    xlMin: XlConsolidationFunction = ...
    xlProduct: XlConsolidationFunction = ...
    xlStDev: XlConsolidationFunction = ...
    xlStDevP: XlConsolidationFunction = ...
    xlSum: XlConsolidationFunction = ...
    xlUnknown: XlConsolidationFunction = ...
    xlVar: XlConsolidationFunction = ...
    xlVarP: XlConsolidationFunction = ...


class XlCopyPictureFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlCopyPictureFormat, values: xlBitmap (2), xlPicture (-4147) """
    value__ = ...
    xlBitmap: XlCopyPictureFormat = ...
    xlPicture: XlCopyPictureFormat = ...


class XlCreator(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlCreator, values: xlCreatorCode (1480803660) """
    value__ = ...
    xlCreatorCode: XlCreator = ...


class XlCubeFieldType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlCubeFieldType, values: xlHierarchy (1), xlMeasure (2), xlSet (3) """
    value__ = ...
    xlHierarchy: XlCubeFieldType = ...
    xlMeasure: XlCubeFieldType = ...
    xlSet: XlCubeFieldType = ...


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


class XlDataSeriesDate(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlDataSeriesDate, values: xlDay (1), xlMonth (3), xlWeekday (2), xlYear (4) """
    value__ = ...
    xlDay: XlDataSeriesDate = ...
    xlMonth: XlDataSeriesDate = ...
    xlWeekday: XlDataSeriesDate = ...
    xlYear: XlDataSeriesDate = ...


class XlDataSeriesType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlDataSeriesType, values: xlAutoFill (4), xlChronological (3), xlDataSeriesLinear (-4132), xlGrowth (2) """
    value__ = ...
    xlAutoFill: XlDataSeriesType = ...
    xlChronological: XlDataSeriesType = ...
    xlDataSeriesLinear: XlDataSeriesType = ...
    xlGrowth: XlDataSeriesType = ...


class XlDeleteShiftDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlDeleteShiftDirection, values: xlShiftToLeft (-4159), xlShiftUp (-4162) """
    value__ = ...
    xlShiftToLeft: XlDeleteShiftDirection = ...
    xlShiftUp: XlDeleteShiftDirection = ...


class XlDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlDirection, values: xlDown (-4121), xlToLeft (-4159), xlToRight (-4161), xlUp (-4162) """
    value__ = ...
    xlDown: XlDirection = ...
    xlToLeft: XlDirection = ...
    xlToRight: XlDirection = ...
    xlUp: XlDirection = ...


class XlDisplayBlanksAs(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlDisplayBlanksAs, values: xlInterpolated (3), xlNotPlotted (1), xlZero (2) """
    value__ = ...
    xlInterpolated: XlDisplayBlanksAs = ...
    xlNotPlotted: XlDisplayBlanksAs = ...
    xlZero: XlDisplayBlanksAs = ...


class XlDisplayDrawingObjects(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlDisplayDrawingObjects, values: xlDisplayShapes (-4104), xlHide (3), xlPlaceholders (2) """
    value__ = ...
    xlDisplayShapes: XlDisplayDrawingObjects = ...
    xlHide: XlDisplayDrawingObjects = ...
    xlPlaceholders: XlDisplayDrawingObjects = ...


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
    """ enum XlErrorBarDirection, values: xlX (-4168), xlY (1) """
    value__ = ...
    xlX: XlErrorBarDirection = ...
    xlY: XlErrorBarDirection = ...


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


class XlFindLookIn(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlFindLookIn, values: xlComments (-4144), xlFormulas (-4123), xlValues (-4163) """
    value__ = ...
    xlComments: XlFindLookIn = ...
    xlFormulas: XlFindLookIn = ...
    xlValues: XlFindLookIn = ...


class XlFixedFormatQuality(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlFixedFormatQuality, values: xlQualityMinimum (1), xlQualityStandard (0) """
    value__ = ...
    xlQualityMinimum: XlFixedFormatQuality = ...
    xlQualityStandard: XlFixedFormatQuality = ...


class XlFixedFormatType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlFixedFormatType, values: xlTypePDF (0), xlTypeXPS (1) """
    value__ = ...
    xlTypePDF: XlFixedFormatType = ...
    xlTypeXPS: XlFixedFormatType = ...


class XlGenerateTableRefs(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlGenerateTableRefs, values: xlGenerateTableRefA1 (0), xlGenerateTableRefStruct (1) """
    value__ = ...
    xlGenerateTableRefA1: XlGenerateTableRefs = ...
    xlGenerateTableRefStruct: XlGenerateTableRefs = ...


class XlGradientFillType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlGradientFillType, values: xlGradientFillLinear (0), xlGradientFillPath (1) """
    value__ = ...
    xlGradientFillLinear: XlGradientFillType = ...
    xlGradientFillPath: XlGradientFillType = ...


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


class XlHebrewModes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlHebrewModes, values: xlHebrewFullScript (0), xlHebrewMixedAuthorizedScript (3), xlHebrewMixedScript (2), xlHebrewPartialScript (1) """
    value__ = ...
    xlHebrewFullScript: XlHebrewModes = ...
    xlHebrewMixedAuthorizedScript: XlHebrewModes = ...
    xlHebrewMixedScript: XlHebrewModes = ...
    xlHebrewPartialScript: XlHebrewModes = ...


class XlImportDataAs(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlImportDataAs, values: xlPivotTableReport (1), xlQueryTable (0), xlTable (2) """
    value__ = ...
    xlPivotTableReport: XlImportDataAs = ...
    xlQueryTable: XlImportDataAs = ...
    xlTable: XlImportDataAs = ...


class XlInsertFormatOrigin(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlInsertFormatOrigin, values: xlFormatFromLeftOrAbove (0), xlFormatFromRightOrBelow (1) """
    value__ = ...
    xlFormatFromLeftOrAbove: XlInsertFormatOrigin = ...
    xlFormatFromRightOrBelow: XlInsertFormatOrigin = ...


class XlInsertShiftDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlInsertShiftDirection, values: xlShiftDown (-4121), xlShiftToRight (-4161) """
    value__ = ...
    xlShiftDown: XlInsertShiftDirection = ...
    xlShiftToRight: XlInsertShiftDirection = ...


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


class XlLocationInTable(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlLocationInTable, values: xlColumnHeader (-4110), xlColumnItem (5), xlDataHeader (3), xlDataItem (7), xlPageHeader (2), xlPageItem (6), xlRowHeader (-4153), xlRowItem (4), xlTableBody (8) """
    value__ = ...
    xlColumnHeader: XlLocationInTable = ...
    xlColumnItem: XlLocationInTable = ...
    xlDataHeader: XlLocationInTable = ...
    xlDataItem: XlLocationInTable = ...
    xlPageHeader: XlLocationInTable = ...
    xlPageItem: XlLocationInTable = ...
    xlRowHeader: XlLocationInTable = ...
    xlRowItem: XlLocationInTable = ...
    xlTableBody: XlLocationInTable = ...


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


class XlOartHorizontalOverflow(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlOartHorizontalOverflow, values: xlOartHorizontalOverflowClip (1), xlOartHorizontalOverflowOverflow (0) """
    value__ = ...
    xlOartHorizontalOverflowClip: XlOartHorizontalOverflow = ...
    xlOartHorizontalOverflowOverflow: XlOartHorizontalOverflow = ...


class XlOartVerticalOverflow(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlOartVerticalOverflow, values: xlOartVerticalOverflowClip (1), xlOartVerticalOverflowEllipsis (2), xlOartVerticalOverflowOverflow (0) """
    value__ = ...
    xlOartVerticalOverflowClip: XlOartVerticalOverflow = ...
    xlOartVerticalOverflowEllipsis: XlOartVerticalOverflow = ...
    xlOartVerticalOverflowOverflow: XlOartVerticalOverflow = ...


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


class XlPictureConvertorType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlPictureConvertorType, values: xlBMP (1), xlCGM (7), xlDRW (4), xlDXF (5), xlEPS (8), xlHGL (6), xlPCT (13), xlPCX (10), xlPIC (11), xlPLT (12), xlTIF (9), xlWMF (2), xlWPG (3) """
    value__ = ...
    xlBMP: XlPictureConvertorType = ...
    xlCGM: XlPictureConvertorType = ...
    xlDRW: XlPictureConvertorType = ...
    xlDXF: XlPictureConvertorType = ...
    xlEPS: XlPictureConvertorType = ...
    xlHGL: XlPictureConvertorType = ...
    xlPCT: XlPictureConvertorType = ...
    xlPCX: XlPictureConvertorType = ...
    xlPIC: XlPictureConvertorType = ...
    xlPLT: XlPictureConvertorType = ...
    xlTIF: XlPictureConvertorType = ...
    xlWMF: XlPictureConvertorType = ...
    xlWPG: XlPictureConvertorType = ...


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


class XlPivotFieldDataType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlPivotFieldDataType, values: xlDate (2), xlNumber (-4145), xlText (-4158) """
    value__ = ...
    xlDate: XlPivotFieldDataType = ...
    xlNumber: XlPivotFieldDataType = ...
    xlText: XlPivotFieldDataType = ...


class XlPivotFieldRepeatLabels(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlPivotFieldRepeatLabels, values: xlDoNotRepeatLabels (1), xlRepeatLabels (2) """
    value__ = ...
    xlDoNotRepeatLabels: XlPivotFieldRepeatLabels = ...
    xlRepeatLabels: XlPivotFieldRepeatLabels = ...


class XlPivotFormatType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlPivotFormatType, values: xlPTClassic (20), xlPTNone (21), xlReport1 (0), xlReport10 (9), xlReport2 (1), xlReport3 (2), xlReport4 (3), xlReport5 (4), xlReport6 (5), xlReport7 (6), xlReport8 (7), xlReport9 (8), xlTable1 (10), xlTable10 (19), xlTable2 (11), xlTable3 (12), xlTable4 (13), xlTable5 (14), xlTable6 (15), xlTable7 (16), xlTable8 (17), xlTable9 (18) """
    value__ = ...
    xlPTClassic: XlPivotFormatType = ...
    xlPTNone: XlPivotFormatType = ...
    xlReport1: XlPivotFormatType = ...
    xlReport10: XlPivotFormatType = ...
    xlReport2: XlPivotFormatType = ...
    xlReport3: XlPivotFormatType = ...
    xlReport4: XlPivotFormatType = ...
    xlReport5: XlPivotFormatType = ...
    xlReport6: XlPivotFormatType = ...
    xlReport7: XlPivotFormatType = ...
    xlReport8: XlPivotFormatType = ...
    xlReport9: XlPivotFormatType = ...
    xlTable1: XlPivotFormatType = ...
    xlTable10: XlPivotFormatType = ...
    xlTable2: XlPivotFormatType = ...
    xlTable3: XlPivotFormatType = ...
    xlTable4: XlPivotFormatType = ...
    xlTable5: XlPivotFormatType = ...
    xlTable6: XlPivotFormatType = ...
    xlTable7: XlPivotFormatType = ...
    xlTable8: XlPivotFormatType = ...
    xlTable9: XlPivotFormatType = ...


class XlPivotTableSourceType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlPivotTableSourceType, values: xlConsolidation (3), xlDatabase (1), xlExternal (2), xlPivotTable (-4148), xlScenario (4) """
    value__ = ...
    xlConsolidation: XlPivotTableSourceType = ...
    xlDatabase: XlPivotTableSourceType = ...
    xlExternal: XlPivotTableSourceType = ...
    xlPivotTable: XlPivotTableSourceType = ...
    xlScenario: XlPivotTableSourceType = ...


class XlPortugueseReform(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlPortugueseReform, values: xlPortugueseBoth (3), xlPortuguesePostReform (2), xlPortuguesePreReform (1) """
    value__ = ...
    xlPortugueseBoth: XlPortugueseReform = ...
    xlPortuguesePostReform: XlPortugueseReform = ...
    xlPortuguesePreReform: XlPortugueseReform = ...


class XlQueryType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlQueryType, values: xlADORecordset (7), xlDAORecordset (2), xlODBCQuery (1), xlOLEDBQuery (5), xlTextImport (6), xlWebQuery (4) """
    value__ = ...
    xlADORecordset: XlQueryType = ...
    xlDAORecordset: XlQueryType = ...
    xlODBCQuery: XlQueryType = ...
    xlOLEDBQuery: XlQueryType = ...
    xlTextImport: XlQueryType = ...
    xlWebQuery: XlQueryType = ...


class XlRangeValueDataType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlRangeValueDataType, values: xlRangeValueDefault (10), xlRangeValueMSPersistXML (12), xlRangeValueXMLSpreadsheet (11) """
    value__ = ...
    xlRangeValueDefault: XlRangeValueDataType = ...
    xlRangeValueMSPersistXML: XlRangeValueDataType = ...
    xlRangeValueXMLSpreadsheet: XlRangeValueDataType = ...


class XlReferenceStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlReferenceStyle, values: xlA1 (1), xlR1C1 (-4150) """
    value__ = ...
    xlA1: XlReferenceStyle = ...
    xlR1C1: XlReferenceStyle = ...


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


class XlSheetType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlSheetType, values: xlChart (-4109), xlDialogSheet (-4116), xlExcel4IntlMacroSheet (4), xlExcel4MacroSheet (3), xlWorksheet (-4167) """
    value__ = ...
    xlChart: XlSheetType = ...
    xlDialogSheet: XlSheetType = ...
    xlExcel4IntlMacroSheet: XlSheetType = ...
    xlExcel4MacroSheet: XlSheetType = ...
    xlWorksheet: XlSheetType = ...


class XlSizeRepresents(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlSizeRepresents, values: xlSizeIsArea (1), xlSizeIsWidth (2) """
    value__ = ...
    xlSizeIsArea: XlSizeRepresents = ...
    xlSizeIsWidth: XlSizeRepresents = ...


class XlSlicerCrossFilterType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlSlicerCrossFilterType, values: xlSlicerCrossFilterShowItemsWithDataAtTop (2), xlSlicerCrossFilterShowItemsWithNoData (3), xlSlicerNoCrossFilter (1) """
    value__ = ...
    xlSlicerCrossFilterShowItemsWithDataAtTop: XlSlicerCrossFilterType = ...
    xlSlicerCrossFilterShowItemsWithNoData: XlSlicerCrossFilterType = ...
    xlSlicerNoCrossFilter: XlSlicerCrossFilterType = ...


class XlSlicerSort(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlSlicerSort, values: xlSlicerSortAscending (2), xlSlicerSortDataSourceOrder (1), xlSlicerSortDescending (3) """
    value__ = ...
    xlSlicerSortAscending: XlSlicerSort = ...
    xlSlicerSortDataSourceOrder: XlSlicerSort = ...
    xlSlicerSortDescending: XlSlicerSort = ...


class XlSpanishModes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlSpanishModes, values: xlSpanishTuteoAndVoseo (1), xlSpanishTuteoOnly (0), xlSpanishVoseoOnly (2) """
    value__ = ...
    xlSpanishTuteoAndVoseo: XlSpanishModes = ...
    xlSpanishTuteoOnly: XlSpanishModes = ...
    xlSpanishVoseoOnly: XlSpanishModes = ...


class XlSubtototalLocationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlSubtototalLocationType, values: xlAtBottom (2), xlAtTop (1) """
    value__ = ...
    xlAtBottom: XlSubtototalLocationType = ...
    xlAtTop: XlSubtototalLocationType = ...


class XlThemeFont(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlThemeFont, values: xlThemeFontMajor (1), xlThemeFontMinor (2), xlThemeFontNone (0) """
    value__ = ...
    xlThemeFontMajor: XlThemeFont = ...
    xlThemeFontMinor: XlThemeFont = ...
    xlThemeFontNone: XlThemeFont = ...


class XlThreadMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlThreadMode, values: xlThreadModeAutomatic (0), xlThreadModeManual (1) """
    value__ = ...
    xlThreadModeAutomatic: XlThreadMode = ...
    xlThreadModeManual: XlThreadMode = ...


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


class XlWebFormatting(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlWebFormatting, values: xlWebFormattingAll (1), xlWebFormattingNone (3), xlWebFormattingRTF (2) """
    value__ = ...
    xlWebFormattingAll: XlWebFormatting = ...
    xlWebFormattingNone: XlWebFormatting = ...
    xlWebFormattingRTF: XlWebFormatting = ...


class XlWebSelectionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlWebSelectionType, values: xlAllTables (2), xlEntirePage (1), xlSpecifiedTables (3) """
    value__ = ...
    xlAllTables: XlWebSelectionType = ...
    xlEntirePage: XlWebSelectionType = ...
    xlSpecifiedTables: XlWebSelectionType = ...


class XlWindowState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlWindowState, values: xlMaximized (-4137), xlMinimized (-4140), xlNormal (-4143) """
    value__ = ...
    xlMaximized: XlWindowState = ...
    xlMinimized: XlWindowState = ...
    xlNormal: XlWindowState = ...


class XlWindowType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XlWindowType, values: xlChartAsWindow (5), xlChartInPlace (4), xlClipboard (3), xlInfo (-4129), xlWorkbook (1) """
    value__ = ...
    xlChartAsWindow: XlWindowType = ...
    xlChartInPlace: XlWindowType = ...
    xlClipboard: XlWindowType = ...
    xlInfo: XlWindowType = ...
    xlWorkbook: XlWindowType = ...


class _IGlobal: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Application:
        """ Get: Application(self: _IGlobal) -> Application """
        ...

    @property
    def CommandBars(self) -> CommandBars:
        """ Get: CommandBars(self: _IGlobal) -> CommandBars """
        ...

    @property
    def Creator(self) -> XlCreator:
        """ Get: Creator(self: _IGlobal) -> XlCreator """
        ...

    @property
    def Parent(self) -> Application:
        """ Get: Parent(self: _IGlobal) -> Application """
        ...



