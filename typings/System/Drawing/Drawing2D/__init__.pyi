# encoding: utf-8
# module System.Drawing.Drawing2D calls itself Drawing2D
# from System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Byte, Enum, ICloneable, IDisposable, 
    MarshalByRefObject, Single)

from System.Drawing import (Brush, Color, FontFamily, Pen, PointF, Rectangle, 
    RectangleF, StringFormat)

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: field#
"""

# no functions
# classes

class CustomLineCap(IDisposable, ICloneable, MarshalByRefObject): # skipped bases: <type 'object'>
    """
    CustomLineCap(fillPath: GraphicsPath, strokePath: GraphicsPath)
    CustomLineCap(fillPath: GraphicsPath, strokePath: GraphicsPath, baseCap: LineCap)
    CustomLineCap(fillPath: GraphicsPath, strokePath: GraphicsPath, baseCap: LineCap, baseInset: Single)
    """
    @property
    def BaseCap(self) -> LineCap:
        """
        Get: BaseCap(self: CustomLineCap) -> LineCap
        Set: BaseCap(self: CustomLineCap) = value
        """
        ...

    @property
    def BaseInset(self) -> Single:
        """
        Get: BaseInset(self: CustomLineCap) -> Single
        Set: BaseInset(self: CustomLineCap) = value
        """
        ...

    @property
    def StrokeJoin(self) -> LineJoin:
        """
        Get: StrokeJoin(self: CustomLineCap) -> LineJoin
        Set: StrokeJoin(self: CustomLineCap) = value
        """
        ...

    @property
    def WidthScale(self) -> Single:
        """
        Get: WidthScale(self: CustomLineCap) -> Single
        Set: WidthScale(self: CustomLineCap) = value
        """
        ...


    def GetStrokeCaps(self, startCap, endCap) -> Tuple_[LineCap, LineCap]:
        """ GetStrokeCaps(self: CustomLineCap) -> (LineCap, LineCap) """
        ...

    def SetStrokeCaps(self, startCap:LineCap, endCap:LineCap): # -> 
        """ SetStrokeCaps(self: CustomLineCap, startCap: LineCap, endCap: LineCap) """
        ...

    def __new__(cls, fillPath:GraphicsPath, strokePath:GraphicsPath, baseCap:LineCap = ..., baseInset:Single = ...) -> Self:
        """
        __new__(cls: type, fillPath: GraphicsPath, strokePath: GraphicsPath)
        __new__(cls: type, fillPath: GraphicsPath, strokePath: GraphicsPath, baseCap: LineCap)
        __new__(cls: type, fillPath: GraphicsPath, strokePath: GraphicsPath, baseCap: LineCap, baseInset: Single)
        """
        ...


class AdjustableArrowCap(CustomLineCap): # skipped bases: <type 'IDisposable'>, <type 'ICloneable'>, <type 'object'>
    """
    AdjustableArrowCap(width: Single, height: Single)
    AdjustableArrowCap(width: Single, height: Single, isFilled: bool)
    """
    @property
    def Filled(self) -> bool:
        """
        Get: Filled(self: AdjustableArrowCap) -> bool
        Set: Filled(self: AdjustableArrowCap) = value
        """
        ...

    @property
    def Height(self) -> Single:
        """
        Get: Height(self: AdjustableArrowCap) -> Single
        Set: Height(self: AdjustableArrowCap) = value
        """
        ...

    @property
    def MiddleInset(self) -> Single:
        """
        Get: MiddleInset(self: AdjustableArrowCap) -> Single
        Set: MiddleInset(self: AdjustableArrowCap) = value
        """
        ...

    @property
    def Width(self) -> Single:
        """
        Get: Width(self: AdjustableArrowCap) -> Single
        Set: Width(self: AdjustableArrowCap) = value
        """
        ...



class Blend: # skipped bases: <type 'object'>, <type 'object'>
    """
    Blend()
    Blend(count: int)
    """
    @property
    def Factors(self) -> Array:
        """
        Get: Factors(self: Blend) -> Array[Single]
        Set: Factors(self: Blend) = value
        """
        ...

    @property
    def Positions(self) -> Array:
        """
        Get: Positions(self: Blend) -> Array[Single]
        Set: Positions(self: Blend) = value
        """
        ...



class ColorBlend: # skipped bases: <type 'object'>, <type 'object'>
    """
    ColorBlend()
    ColorBlend(count: int)
    """
    @property
    def Colors(self) -> Array:
        """
        Get: Colors(self: ColorBlend) -> Array[Color]
        Set: Colors(self: ColorBlend) = value
        """
        ...

    @property
    def Positions(self) -> Array:
        """
        Get: Positions(self: ColorBlend) -> Array[Single]
        Set: Positions(self: ColorBlend) = value
        """
        ...



class CombineMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CombineMode, values: Complement (5), Exclude (4), Intersect (1), Replace (0), Union (2), Xor (3) """
    Complement: CombineMode = ...
    Exclude: CombineMode = ...
    Intersect: CombineMode = ...
    Replace: CombineMode = ...
    Union: CombineMode = ...
    value__ = ...
    Xor: CombineMode = ...


class CompositingMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CompositingMode, values: SourceCopy (1), SourceOver (0) """
    SourceCopy: CompositingMode = ...
    SourceOver: CompositingMode = ...
    value__ = ...


class CompositingQuality(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CompositingQuality, values: AssumeLinear (4), Default (0), GammaCorrected (3), HighQuality (2), HighSpeed (1), Invalid (-1) """
    AssumeLinear: CompositingQuality = ...
    Default: CompositingQuality = ...
    GammaCorrected: CompositingQuality = ...
    HighQuality: CompositingQuality = ...
    HighSpeed: CompositingQuality = ...
    Invalid: CompositingQuality = ...
    value__ = ...


class CoordinateSpace(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CoordinateSpace, values: Device (2), Page (1), World (0) """
    Device: CoordinateSpace = ...
    Page: CoordinateSpace = ...
    value__ = ...
    World: CoordinateSpace = ...


class DashCap(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DashCap, values: Flat (0), Round (2), Triangle (3) """
    Flat: DashCap = ...
    Round: DashCap = ...
    Triangle: DashCap = ...
    value__ = ...


class DashStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DashStyle, values: Custom (5), Dash (1), DashDot (3), DashDotDot (4), Dot (2), Solid (0) """
    Custom: DashStyle = ...
    Dash: DashStyle = ...
    DashDot: DashStyle = ...
    DashDotDot: DashStyle = ...
    Dot: DashStyle = ...
    Solid: DashStyle = ...
    value__ = ...


class FillMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FillMode, values: Alternate (0), Winding (1) """
    Alternate: FillMode = ...
    value__ = ...
    Winding: FillMode = ...


class FlushIntention(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FlushIntention, values: Flush (0), Sync (1) """
    Flush: FlushIntention = ...
    Sync: FlushIntention = ...
    value__ = ...


class GraphicsContainer(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    pass

class GraphicsPath(IDisposable, ICloneable, MarshalByRefObject): # skipped bases: <type 'object'>
    """
    GraphicsPath()
    GraphicsPath(fillMode: FillMode)
    GraphicsPath(pts: Array[PointF], types: Array[Byte])
    GraphicsPath(pts: Array[PointF], types: Array[Byte], fillMode: FillMode)
    GraphicsPath(pts: Array[Point], types: Array[Byte])
    GraphicsPath(pts: Array[Point], types: Array[Byte], fillMode: FillMode)
    """
    @property
    def FillMode(self) -> FillMode:
        """
        Get: FillMode(self: GraphicsPath) -> FillMode
        Set: FillMode(self: GraphicsPath) = value
        """
        ...

    @property
    def PathData(self) -> PathData:
        """ Get: PathData(self: GraphicsPath) -> PathData """
        ...

    @property
    def PathPoints(self) -> Array:
        """ Get: PathPoints(self: GraphicsPath) -> Array[PointF] """
        ...

    @property
    def PathTypes(self) -> Array:
        """ Get: PathTypes(self: GraphicsPath) -> Array[Byte] """
        ...

    @property
    def PointCount(self) -> int:
        """ Get: PointCount(self: GraphicsPath) -> int """
        ...


    def AddArc(self, *__args): # -> 
        """ AddArc(self: GraphicsPath, rect: RectangleF, startAngle: Single, sweepAngle: Single)AddArc(self: GraphicsPath, x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single)AddArc(self: GraphicsPath, rect: Rectangle, startAngle: Single, sweepAngle: Single)AddArc(self: GraphicsPath, x: int, y: int, width: int, height: int, startAngle: Single, sweepAngle: Single) """
        ...

    def AddBezier(self, *__args): # -> 
        """ AddBezier(self: GraphicsPath, pt1: PointF, pt2: PointF, pt3: PointF, pt4: PointF)AddBezier(self: GraphicsPath, x1: Single, y1: Single, x2: Single, y2: Single, x3: Single, y3: Single, x4: Single, y4: Single)AddBezier(self: GraphicsPath, pt1: Point, pt2: Point, pt3: Point, pt4: Point)AddBezier(self: GraphicsPath, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int) """
        ...

    def AddBeziers(self, points:Array): # -> 
        """ AddBeziers(self: GraphicsPath, points: Array[PointF])AddBeziers(self: GraphicsPath, *points: Array[Point]) """
        ...

    def AddClosedCurve(self, points:Array, tension:Single = ...): # -> 
        """ AddClosedCurve(self: GraphicsPath, points: Array[PointF])AddClosedCurve(self: GraphicsPath, points: Array[PointF], tension: Single)AddClosedCurve(self: GraphicsPath, points: Array[Point])AddClosedCurve(self: GraphicsPath, points: Array[Point], tension: Single) """
        ...

    def AddCurve(self, points:Array, *__args:Single): # -> 
        """ AddCurve(self: GraphicsPath, points: Array[PointF])AddCurve(self: GraphicsPath, points: Array[PointF], tension: Single)AddCurve(self: GraphicsPath, points: Array[PointF], offset: int, numberOfSegments: int, tension: Single)AddCurve(self: GraphicsPath, points: Array[Point])AddCurve(self: GraphicsPath, points: Array[Point], tension: Single)AddCurve(self: GraphicsPath, points: Array[Point], offset: int, numberOfSegments: int, tension: Single) """
        ...

    def AddEllipse(self, *__args:RectangleF): # -> 
        """ AddEllipse(self: GraphicsPath, rect: RectangleF)AddEllipse(self: GraphicsPath, x: Single, y: Single, width: Single, height: Single)AddEllipse(self: GraphicsPath, rect: Rectangle)AddEllipse(self: GraphicsPath, x: int, y: int, width: int, height: int) """
        ...

    def AddLine(self, *__args): # -> 
        """ AddLine(self: GraphicsPath, pt1: PointF, pt2: PointF)AddLine(self: GraphicsPath, x1: Single, y1: Single, x2: Single, y2: Single)AddLine(self: GraphicsPath, pt1: Point, pt2: Point)AddLine(self: GraphicsPath, x1: int, y1: int, x2: int, y2: int) """
        ...

    def AddLines(self, points:Array): # -> 
        """ AddLines(self: GraphicsPath, points: Array[PointF])AddLines(self: GraphicsPath, points: Array[Point]) """
        ...

    def AddPath(self, addingPath:GraphicsPath, connect:bool): # -> 
        """ AddPath(self: GraphicsPath, addingPath: GraphicsPath, connect: bool) """
        ...

    def AddPie(self, *__args): # -> 
        """ AddPie(self: GraphicsPath, rect: Rectangle, startAngle: Single, sweepAngle: Single)AddPie(self: GraphicsPath, x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single)AddPie(self: GraphicsPath, x: int, y: int, width: int, height: int, startAngle: Single, sweepAngle: Single) """
        ...

    def AddPolygon(self, points:Array): # -> 
        """ AddPolygon(self: GraphicsPath, points: Array[PointF])AddPolygon(self: GraphicsPath, points: Array[Point]) """
        ...

    def AddRectangle(self, rect:Rectangle): # -> 
        """ AddRectangle(self: GraphicsPath, rect: Rectangle)AddRectangle(self: GraphicsPath, rect: RectangleF) """
        ...

    def AddRectangles(self, rects:Array): # -> 
        """ AddRectangles(self: GraphicsPath, rects: Array[RectangleF])AddRectangles(self: GraphicsPath, rects: Array[Rectangle]) """
        ...

    def AddString(self, s, family, style, emSize, *__args): # -> 
        """ AddString(self: GraphicsPath, s: str, family: FontFamily, style: int, emSize: Single, origin: PointF, format: StringFormat)AddString(self: GraphicsPath, s: str, family: FontFamily, style: int, emSize: Single, origin: Point, format: StringFormat)AddString(self: GraphicsPath, s: str, family: FontFamily, style: int, emSize: Single, layoutRect: RectangleF, format: StringFormat)AddString(self: GraphicsPath, s: str, family: FontFamily, style: int, emSize: Single, layoutRect: Rectangle, format: StringFormat) """
        ...

    def ClearMarkers(self): # -> 
        """ ClearMarkers(self: GraphicsPath) """
        ...

    def CloseAllFigures(self): # -> 
        """ CloseAllFigures(self: GraphicsPath) """
        ...

    def CloseFigure(self): # -> 
        """ CloseFigure(self: GraphicsPath) """
        ...

    def Flatten(self, matrix:Matrix = ..., flatness:Single = ...): # -> 
        """ Flatten(self: GraphicsPath)Flatten(self: GraphicsPath, matrix: Matrix)Flatten(self: GraphicsPath, matrix: Matrix, flatness: Single) """
        ...

    def GetBounds(self, matrix:Matrix = ..., pen:Pen = ...) -> RectangleF:
        """
        GetBounds(self: GraphicsPath) -> RectangleF
        GetBounds(self: GraphicsPath, matrix: Matrix) -> RectangleF
        GetBounds(self: GraphicsPath, matrix: Matrix, pen: Pen) -> RectangleF
        """
        ...

    def GetLastPoint(self) -> PointF:
        """ GetLastPoint(self: GraphicsPath) -> PointF """
        ...

    def IsOutlineVisible(self, *__args) -> bool:
        """
        IsOutlineVisible(self: GraphicsPath, x: Single, y: Single, pen: Pen) -> bool
        IsOutlineVisible(self: GraphicsPath, point: PointF, pen: Pen) -> bool
        IsOutlineVisible(self: GraphicsPath, x: Single, y: Single, pen: Pen, graphics: Graphics) -> bool
        IsOutlineVisible(self: GraphicsPath, pt: PointF, pen: Pen, graphics: Graphics) -> bool
        IsOutlineVisible(self: GraphicsPath, x: int, y: int, pen: Pen) -> bool
        IsOutlineVisible(self: GraphicsPath, point: Point, pen: Pen) -> bool
        IsOutlineVisible(self: GraphicsPath, x: int, y: int, pen: Pen, graphics: Graphics) -> bool
        IsOutlineVisible(self: GraphicsPath, pt: Point, pen: Pen, graphics: Graphics) -> bool
        """
        ...

    def IsVisible(self, *__args:PointF) -> bool:
        """
        IsVisible(self: GraphicsPath, x: Single, y: Single) -> bool
        IsVisible(self: GraphicsPath, point: PointF) -> bool
        IsVisible(self: GraphicsPath, x: Single, y: Single, graphics: Graphics) -> bool
        IsVisible(self: GraphicsPath, pt: PointF, graphics: Graphics) -> bool
        IsVisible(self: GraphicsPath, x: int, y: int) -> bool
        IsVisible(self: GraphicsPath, point: Point) -> bool
        IsVisible(self: GraphicsPath, x: int, y: int, graphics: Graphics) -> bool
        IsVisible(self: GraphicsPath, pt: Point, graphics: Graphics) -> bool
        """
        ...

    def Reset(self): # -> 
        """ Reset(self: GraphicsPath) """
        ...

    def Reverse(self): # -> 
        """ Reverse(self: GraphicsPath) """
        ...

    def SetMarkers(self): # -> 
        """ SetMarkers(self: GraphicsPath) """
        ...

    def StartFigure(self): # -> 
        """ StartFigure(self: GraphicsPath) """
        ...

    def Transform(self, matrix:Matrix): # -> 
        """ Transform(self: GraphicsPath, matrix: Matrix) """
        ...

    def Warp(self, destPoints:Array, srcRect:RectangleF, matrix:Matrix = ..., warpMode:WarpMode = ..., flatness:Single = ...): # -> 
        """ Warp(self: GraphicsPath, destPoints: Array[PointF], srcRect: RectangleF)Warp(self: GraphicsPath, destPoints: Array[PointF], srcRect: RectangleF, matrix: Matrix)Warp(self: GraphicsPath, destPoints: Array[PointF], srcRect: RectangleF, matrix: Matrix, warpMode: WarpMode)Warp(self: GraphicsPath, destPoints: Array[PointF], srcRect: RectangleF, matrix: Matrix, warpMode: WarpMode, flatness: Single) """
        ...

    def Widen(self, pen:Pen, matrix:Matrix = ..., flatness:Single = ...): # -> 
        """ Widen(self: GraphicsPath, pen: Pen)Widen(self: GraphicsPath, pen: Pen, matrix: Matrix)Widen(self: GraphicsPath, pen: Pen, matrix: Matrix, flatness: Single) """
        ...

    def __new__(cls, *__args:FillMode) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, fillMode: FillMode)
        __new__(cls: type, pts: Array[PointF], types: Array[Byte])
        __new__(cls: type, pts: Array[PointF], types: Array[Byte], fillMode: FillMode)
        __new__(cls: type, pts: Array[Point], types: Array[Byte])
        __new__(cls: type, pts: Array[Point], types: Array[Byte], fillMode: FillMode)
        """
        ...


class GraphicsPathIterator(IDisposable, MarshalByRefObject): # skipped bases: <type 'object'>
    """ GraphicsPathIterator(path: GraphicsPath) """
    @property
    def Count(self) -> int:
        """ Get: Count(self: GraphicsPathIterator) -> int """
        ...

    @property
    def SubpathCount(self) -> int:
        """ Get: SubpathCount(self: GraphicsPathIterator) -> int """
        ...


    def CopyData(self, points:Array, types:Array, startIndex:int, endIndex:int) -> Tuple_[int, Array, Array]:
        """ CopyData(self: GraphicsPathIterator, points: Array[PointF], types: Array[Byte], startIndex: int, endIndex: int) -> (int, Array[PointF], Array[Byte]) """
        ...

    def Enumerate(self, points:Array, types:Array) -> Tuple_[int, Array, Array]:
        """ Enumerate(self: GraphicsPathIterator, points: Array[PointF], types: Array[Byte]) -> (int, Array[PointF], Array[Byte]) """
        ...

    def HasCurve(self) -> bool:
        """ HasCurve(self: GraphicsPathIterator) -> bool """
        ...

    def NextMarker(self, *__args:GraphicsPath) -> int:
        """
        NextMarker(self: GraphicsPathIterator) -> (int, int, int)
        NextMarker(self: GraphicsPathIterator, path: GraphicsPath) -> int
        """
        ...

    def NextPathType(self, pathType, startIndex, endIndex) -> Tuple_[int, Byte, int, int]:
        """ NextPathType(self: GraphicsPathIterator) -> (int, Byte, int, int) """
        ...

    def NextSubpath(self, *__args:GraphicsPath) -> Tuple_[int, bool]:
        """
        NextSubpath(self: GraphicsPathIterator) -> (int, int, int, bool)
        NextSubpath(self: GraphicsPathIterator, path: GraphicsPath) -> (int, bool)
        """
        ...

    def Rewind(self): # -> 
        """ Rewind(self: GraphicsPathIterator) """
        ...

    def __new__(cls, path:GraphicsPath) -> Self:
        """ __new__(cls: type, path: GraphicsPath) """
        ...


class GraphicsState(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    pass

class HatchBrush(Brush): # skipped bases: <type 'IDisposable'>, <type 'ICloneable'>, <type 'object'>
    """
    HatchBrush(hatchstyle: HatchStyle, foreColor: Color)
    HatchBrush(hatchstyle: HatchStyle, foreColor: Color, backColor: Color)
    """
    @property
    def BackgroundColor(self) -> Color:
        """ Get: BackgroundColor(self: HatchBrush) -> Color """
        ...

    @property
    def ForegroundColor(self) -> Color:
        """ Get: ForegroundColor(self: HatchBrush) -> Color """
        ...

    @property
    def HatchStyle(self) -> HatchStyle:
        """ Get: HatchStyle(self: HatchBrush) -> HatchStyle """
        ...


    def __new__(cls, hatchstyle:HatchStyle, foreColor:Color, backColor:Color = ...) -> Self:
        """
        __new__(cls: type, hatchstyle: HatchStyle, foreColor: Color)
        __new__(cls: type, hatchstyle: HatchStyle, foreColor: Color, backColor: Color)
        """
        ...


class HatchStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HatchStyle, values: BackwardDiagonal (3), Cross (4), DarkDownwardDiagonal (20), DarkHorizontal (29), DarkUpwardDiagonal (21), DarkVertical (28), DashedDownwardDiagonal (30), DashedHorizontal (32), DashedUpwardDiagonal (31), DashedVertical (33), DiagonalBrick (38), DiagonalCross (5), Divot (42), DottedDiamond (44), DottedGrid (43), ForwardDiagonal (2), Horizontal (0), HorizontalBrick (39), LargeCheckerBoard (50), LargeConfetti (35), LargeGrid (4), LightDownwardDiagonal (18), LightHorizontal (25), LightUpwardDiagonal (19), LightVertical (24), Max (4), Min (0), NarrowHorizontal (27), NarrowVertical (26), OutlinedDiamond (51), Percent05 (6), Percent10 (7), Percent20 (8), Percent25 (9), Percent30 (10), Percent40 (11), Percent50 (12), Percent60 (13), Percent70 (14), Percent75 (15), Percent80 (16), Percent90 (17), Plaid (41), Shingle (45), SmallCheckerBoard (49), SmallConfetti (34), SmallGrid (48), SolidDiamond (52), Sphere (47), Trellis (46), Vertical (1), Wave (37), Weave (40), WideDownwardDiagonal (22), WideUpwardDiagonal (23), ZigZag (36) """
    BackwardDiagonal: HatchStyle = ...
    Cross: HatchStyle = ...
    DarkDownwardDiagonal: HatchStyle = ...
    DarkHorizontal: HatchStyle = ...
    DarkUpwardDiagonal: HatchStyle = ...
    DarkVertical: HatchStyle = ...
    DashedDownwardDiagonal: HatchStyle = ...
    DashedHorizontal: HatchStyle = ...
    DashedUpwardDiagonal: HatchStyle = ...
    DashedVertical: HatchStyle = ...
    DiagonalBrick: HatchStyle = ...
    DiagonalCross: HatchStyle = ...
    Divot: HatchStyle = ...
    DottedDiamond: HatchStyle = ...
    DottedGrid: HatchStyle = ...
    ForwardDiagonal: HatchStyle = ...
    Horizontal: HatchStyle = ...
    HorizontalBrick: HatchStyle = ...
    LargeCheckerBoard: HatchStyle = ...
    LargeConfetti: HatchStyle = ...
    LargeGrid: HatchStyle = ...
    LightDownwardDiagonal: HatchStyle = ...
    LightHorizontal: HatchStyle = ...
    LightUpwardDiagonal: HatchStyle = ...
    LightVertical: HatchStyle = ...
    Max: HatchStyle = ...
    Min: HatchStyle = ...
    NarrowHorizontal: HatchStyle = ...
    NarrowVertical: HatchStyle = ...
    OutlinedDiamond: HatchStyle = ...
    Percent05: HatchStyle = ...
    Percent10: HatchStyle = ...
    Percent20: HatchStyle = ...
    Percent25: HatchStyle = ...
    Percent30: HatchStyle = ...
    Percent40: HatchStyle = ...
    Percent50: HatchStyle = ...
    Percent60: HatchStyle = ...
    Percent70: HatchStyle = ...
    Percent75: HatchStyle = ...
    Percent80: HatchStyle = ...
    Percent90: HatchStyle = ...
    Plaid: HatchStyle = ...
    Shingle: HatchStyle = ...
    SmallCheckerBoard: HatchStyle = ...
    SmallConfetti: HatchStyle = ...
    SmallGrid: HatchStyle = ...
    SolidDiamond: HatchStyle = ...
    Sphere: HatchStyle = ...
    Trellis: HatchStyle = ...
    value__ = ...
    Vertical: HatchStyle = ...
    Wave: HatchStyle = ...
    Weave: HatchStyle = ...
    WideDownwardDiagonal: HatchStyle = ...
    WideUpwardDiagonal: HatchStyle = ...
    ZigZag: HatchStyle = ...


class InterpolationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InterpolationMode, values: Bicubic (4), Bilinear (3), Default (0), High (2), HighQualityBicubic (7), HighQualityBilinear (6), Invalid (-1), Low (1), NearestNeighbor (5) """
    Bicubic: InterpolationMode = ...
    Bilinear: InterpolationMode = ...
    Default: InterpolationMode = ...
    High: InterpolationMode = ...
    HighQualityBicubic: InterpolationMode = ...
    HighQualityBilinear: InterpolationMode = ...
    Invalid: InterpolationMode = ...
    Low: InterpolationMode = ...
    NearestNeighbor: InterpolationMode = ...
    value__ = ...


class LinearGradientBrush(Brush): # skipped bases: <type 'IDisposable'>, <type 'ICloneable'>, <type 'object'>
    """
    LinearGradientBrush(point1: PointF, point2: PointF, color1: Color, color2: Color)
    LinearGradientBrush(point1: Point, point2: Point, color1: Color, color2: Color)
    LinearGradientBrush(rect: RectangleF, color1: Color, color2: Color, linearGradientMode: LinearGradientMode)
    LinearGradientBrush(rect: Rectangle, color1: Color, color2: Color, linearGradientMode: LinearGradientMode)
    LinearGradientBrush(rect: RectangleF, color1: Color, color2: Color, angle: Single)
    LinearGradientBrush(rect: RectangleF, color1: Color, color2: Color, angle: Single, isAngleScaleable: bool)
    LinearGradientBrush(rect: Rectangle, color1: Color, color2: Color, angle: Single)
    LinearGradientBrush(rect: Rectangle, color1: Color, color2: Color, angle: Single, isAngleScaleable: bool)
    """
    @property
    def Blend(self) -> Blend:
        """
        Get: Blend(self: LinearGradientBrush) -> Blend
        Set: Blend(self: LinearGradientBrush) = value
        """
        ...

    @property
    def GammaCorrection(self) -> bool:
        """
        Get: GammaCorrection(self: LinearGradientBrush) -> bool
        Set: GammaCorrection(self: LinearGradientBrush) = value
        """
        ...

    @property
    def InterpolationColors(self) -> ColorBlend:
        """
        Get: InterpolationColors(self: LinearGradientBrush) -> ColorBlend
        Set: InterpolationColors(self: LinearGradientBrush) = value
        """
        ...

    @property
    def LinearColors(self) -> Array:
        """
        Get: LinearColors(self: LinearGradientBrush) -> Array[Color]
        Set: LinearColors(self: LinearGradientBrush) = value
        """
        ...

    @property
    def Rectangle(self) -> RectangleF:
        """ Get: Rectangle(self: LinearGradientBrush) -> RectangleF """
        ...

    @property
    def Transform(self) -> Matrix:
        """
        Get: Transform(self: LinearGradientBrush) -> Matrix
        Set: Transform(self: LinearGradientBrush) = value
        """
        ...

    @property
    def WrapMode(self) -> WrapMode:
        """
        Get: WrapMode(self: LinearGradientBrush) -> WrapMode
        Set: WrapMode(self: LinearGradientBrush) = value
        """
        ...


    def MultiplyTransform(self, matrix:Matrix, order:MatrixOrder = ...): # -> 
        """ MultiplyTransform(self: LinearGradientBrush, matrix: Matrix)MultiplyTransform(self: LinearGradientBrush, matrix: Matrix, order: MatrixOrder) """
        ...

    def ResetTransform(self): # -> 
        """ ResetTransform(self: LinearGradientBrush) """
        ...

    def RotateTransform(self, angle:Single, order:MatrixOrder = ...): # -> 
        """ RotateTransform(self: LinearGradientBrush, angle: Single)RotateTransform(self: LinearGradientBrush, angle: Single, order: MatrixOrder) """
        ...

    def ScaleTransform(self, sx:Single, sy:Single, order:MatrixOrder = ...): # -> 
        """ ScaleTransform(self: LinearGradientBrush, sx: Single, sy: Single)ScaleTransform(self: LinearGradientBrush, sx: Single, sy: Single, order: MatrixOrder) """
        ...

    def SetBlendTriangularShape(self, focus:Single, scale:Single = ...): # -> 
        """ SetBlendTriangularShape(self: LinearGradientBrush, focus: Single)SetBlendTriangularShape(self: LinearGradientBrush, focus: Single, scale: Single) """
        ...

    def SetSigmaBellShape(self, focus:Single, scale:Single = ...): # -> 
        """ SetSigmaBellShape(self: LinearGradientBrush, focus: Single)SetSigmaBellShape(self: LinearGradientBrush, focus: Single, scale: Single) """
        ...

    def TranslateTransform(self, dx:Single, dy:Single, order:MatrixOrder = ...): # -> 
        """ TranslateTransform(self: LinearGradientBrush, dx: Single, dy: Single)TranslateTransform(self: LinearGradientBrush, dx: Single, dy: Single, order: MatrixOrder) """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, point1: PointF, point2: PointF, color1: Color, color2: Color)
        __new__(cls: type, point1: Point, point2: Point, color1: Color, color2: Color)
        __new__(cls: type, rect: RectangleF, color1: Color, color2: Color, linearGradientMode: LinearGradientMode)
        __new__(cls: type, rect: Rectangle, color1: Color, color2: Color, linearGradientMode: LinearGradientMode)
        __new__(cls: type, rect: RectangleF, color1: Color, color2: Color, angle: Single)
        __new__(cls: type, rect: RectangleF, color1: Color, color2: Color, angle: Single, isAngleScaleable: bool)
        __new__(cls: type, rect: Rectangle, color1: Color, color2: Color, angle: Single)
        __new__(cls: type, rect: Rectangle, color1: Color, color2: Color, angle: Single, isAngleScaleable: bool)
        """
        ...


class LinearGradientMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LinearGradientMode, values: BackwardDiagonal (3), ForwardDiagonal (2), Horizontal (0), Vertical (1) """
    BackwardDiagonal: LinearGradientMode = ...
    ForwardDiagonal: LinearGradientMode = ...
    Horizontal: LinearGradientMode = ...
    value__ = ...
    Vertical: LinearGradientMode = ...


class LineCap(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LineCap, values: AnchorMask (240), ArrowAnchor (20), Custom (255), DiamondAnchor (19), Flat (0), NoAnchor (16), Round (2), RoundAnchor (18), Square (1), SquareAnchor (17), Triangle (3) """
    AnchorMask: LineCap = ...
    ArrowAnchor: LineCap = ...
    Custom: LineCap = ...
    DiamondAnchor: LineCap = ...
    Flat: LineCap = ...
    NoAnchor: LineCap = ...
    Round: LineCap = ...
    RoundAnchor: LineCap = ...
    Square: LineCap = ...
    SquareAnchor: LineCap = ...
    Triangle: LineCap = ...
    value__ = ...


class LineJoin(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LineJoin, values: Bevel (1), Miter (0), MiterClipped (3), Round (2) """
    Bevel: LineJoin = ...
    Miter: LineJoin = ...
    MiterClipped: LineJoin = ...
    Round: LineJoin = ...
    value__ = ...


class Matrix(IDisposable, MarshalByRefObject): # skipped bases: <type 'object'>
    """
    Matrix()
    Matrix(m11: Single, m12: Single, m21: Single, m22: Single, dx: Single, dy: Single)
    Matrix(rect: RectangleF, plgpts: Array[PointF])
    Matrix(rect: Rectangle, plgpts: Array[Point])
    """
    @property
    def Elements(self) -> Array:
        """ Get: Elements(self: Matrix) -> Array[Single] """
        ...

    @property
    def IsIdentity(self) -> bool:
        """ Get: IsIdentity(self: Matrix) -> bool """
        ...

    @property
    def IsInvertible(self) -> bool:
        """ Get: IsInvertible(self: Matrix) -> bool """
        ...

    @property
    def OffsetX(self) -> Single:
        """ Get: OffsetX(self: Matrix) -> Single """
        ...

    @property
    def OffsetY(self) -> Single:
        """ Get: OffsetY(self: Matrix) -> Single """
        ...


    def Clone(self) -> Matrix:
        """ Clone(self: Matrix) -> Matrix """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: Matrix, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Matrix) -> int """
        ...

    def Invert(self): # -> 
        """ Invert(self: Matrix) """
        ...

    def Multiply(self, matrix:Matrix, order:MatrixOrder = ...): # -> 
        """ Multiply(self: Matrix, matrix: Matrix)Multiply(self: Matrix, matrix: Matrix, order: MatrixOrder) """
        ...

    def Reset(self): # -> 
        """ Reset(self: Matrix) """
        ...

    def Rotate(self, angle:Single, order:MatrixOrder = ...): # -> 
        """ Rotate(self: Matrix, angle: Single)Rotate(self: Matrix, angle: Single, order: MatrixOrder) """
        ...

    def RotateAt(self, angle:Single, point:PointF, order:MatrixOrder = ...): # -> 
        """ RotateAt(self: Matrix, angle: Single, point: PointF)RotateAt(self: Matrix, angle: Single, point: PointF, order: MatrixOrder) """
        ...

    def Scale(self, scaleX:Single, scaleY:Single, order:MatrixOrder = ...): # -> 
        """ Scale(self: Matrix, scaleX: Single, scaleY: Single)Scale(self: Matrix, scaleX: Single, scaleY: Single, order: MatrixOrder) """
        ...

    def Shear(self, shearX:Single, shearY:Single, order:MatrixOrder = ...): # -> 
        """ Shear(self: Matrix, shearX: Single, shearY: Single)Shear(self: Matrix, shearX: Single, shearY: Single, order: MatrixOrder) """
        ...

    def TransformPoints(self, pts:Array): # -> 
        """ TransformPoints(self: Matrix, pts: Array[PointF])TransformPoints(self: Matrix, pts: Array[Point]) """
        ...

    def TransformVectors(self, pts:Array): # -> 
        """ TransformVectors(self: Matrix, pts: Array[PointF])TransformVectors(self: Matrix, pts: Array[Point]) """
        ...

    def Translate(self, offsetX:Single, offsetY:Single, order:MatrixOrder = ...): # -> 
        """ Translate(self: Matrix, offsetX: Single, offsetY: Single)Translate(self: Matrix, offsetX: Single, offsetY: Single, order: MatrixOrder) """
        ...

    def VectorTransformPoints(self, pts:Array): # -> 
        """ VectorTransformPoints(self: Matrix, pts: Array[Point]) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, m11: Single, m12: Single, m21: Single, m22: Single, dx: Single, dy: Single)
        __new__(cls: type, rect: RectangleF, plgpts: Array[PointF])
        __new__(cls: type, rect: Rectangle, plgpts: Array[Point])
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MatrixOrder(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MatrixOrder, values: Append (1), Prepend (0) """
    Append: MatrixOrder = ...
    Prepend: MatrixOrder = ...
    value__ = ...


class PathData: # skipped bases: <type 'object'>, <type 'object'>
    """ PathData() """
    @property
    def Points(self) -> Array:
        """
        Get: Points(self: PathData) -> Array[PointF]
        Set: Points(self: PathData) = value
        """
        ...

    @property
    def Types(self) -> Array:
        """
        Get: Types(self: PathData) -> Array[Byte]
        Set: Types(self: PathData) = value
        """
        ...



class PathGradientBrush(Brush): # skipped bases: <type 'IDisposable'>, <type 'ICloneable'>, <type 'object'>
    """
    PathGradientBrush(points: Array[PointF])
    PathGradientBrush(points: Array[PointF], wrapMode: WrapMode)
    PathGradientBrush(points: Array[Point])
    PathGradientBrush(points: Array[Point], wrapMode: WrapMode)
    PathGradientBrush(path: GraphicsPath)
    """
    @property
    def Blend(self) -> Blend:
        """
        Get: Blend(self: PathGradientBrush) -> Blend
        Set: Blend(self: PathGradientBrush) = value
        """
        ...

    @property
    def CenterColor(self) -> Color:
        """
        Get: CenterColor(self: PathGradientBrush) -> Color
        Set: CenterColor(self: PathGradientBrush) = value
        """
        ...

    @property
    def CenterPoint(self) -> PointF:
        """
        Get: CenterPoint(self: PathGradientBrush) -> PointF
        Set: CenterPoint(self: PathGradientBrush) = value
        """
        ...

    @property
    def FocusScales(self) -> PointF:
        """
        Get: FocusScales(self: PathGradientBrush) -> PointF
        Set: FocusScales(self: PathGradientBrush) = value
        """
        ...

    @property
    def InterpolationColors(self) -> ColorBlend:
        """
        Get: InterpolationColors(self: PathGradientBrush) -> ColorBlend
        Set: InterpolationColors(self: PathGradientBrush) = value
        """
        ...

    @property
    def Rectangle(self) -> RectangleF:
        """ Get: Rectangle(self: PathGradientBrush) -> RectangleF """
        ...

    @property
    def SurroundColors(self) -> Array:
        """
        Get: SurroundColors(self: PathGradientBrush) -> Array[Color]
        Set: SurroundColors(self: PathGradientBrush) = value
        """
        ...

    @property
    def Transform(self) -> Matrix:
        """
        Get: Transform(self: PathGradientBrush) -> Matrix
        Set: Transform(self: PathGradientBrush) = value
        """
        ...

    @property
    def WrapMode(self) -> WrapMode:
        """
        Get: WrapMode(self: PathGradientBrush) -> WrapMode
        Set: WrapMode(self: PathGradientBrush) = value
        """
        ...


    def MultiplyTransform(self, matrix:Matrix, order:MatrixOrder = ...): # -> 
        """ MultiplyTransform(self: PathGradientBrush, matrix: Matrix)MultiplyTransform(self: PathGradientBrush, matrix: Matrix, order: MatrixOrder) """
        ...

    def ResetTransform(self): # -> 
        """ ResetTransform(self: PathGradientBrush) """
        ...

    def RotateTransform(self, angle:Single, order:MatrixOrder = ...): # -> 
        """ RotateTransform(self: PathGradientBrush, angle: Single)RotateTransform(self: PathGradientBrush, angle: Single, order: MatrixOrder) """
        ...

    def ScaleTransform(self, sx:Single, sy:Single, order:MatrixOrder = ...): # -> 
        """ ScaleTransform(self: PathGradientBrush, sx: Single, sy: Single)ScaleTransform(self: PathGradientBrush, sx: Single, sy: Single, order: MatrixOrder) """
        ...

    def SetBlendTriangularShape(self, focus:Single, scale:Single = ...): # -> 
        """ SetBlendTriangularShape(self: PathGradientBrush, focus: Single)SetBlendTriangularShape(self: PathGradientBrush, focus: Single, scale: Single) """
        ...

    def SetSigmaBellShape(self, focus:Single, scale:Single = ...): # -> 
        """ SetSigmaBellShape(self: PathGradientBrush, focus: Single)SetSigmaBellShape(self: PathGradientBrush, focus: Single, scale: Single) """
        ...

    def TranslateTransform(self, dx:Single, dy:Single, order:MatrixOrder = ...): # -> 
        """ TranslateTransform(self: PathGradientBrush, dx: Single, dy: Single)TranslateTransform(self: PathGradientBrush, dx: Single, dy: Single, order: MatrixOrder) """
        ...

    def __new__(cls, *__args:Array) -> Self:
        """
        __new__(cls: type, points: Array[PointF])
        __new__(cls: type, points: Array[PointF], wrapMode: WrapMode)
        __new__(cls: type, points: Array[Point])
        __new__(cls: type, points: Array[Point], wrapMode: WrapMode)
        __new__(cls: type, path: GraphicsPath)
        """
        ...


class PathPointType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PathPointType, values: Bezier (3), Bezier3 (3), CloseSubpath (128), DashMode (16), Line (1), PathMarker (32), PathTypeMask (7), Start (0) """
    Bezier: PathPointType = ...
    Bezier3: PathPointType = ...
    CloseSubpath: PathPointType = ...
    DashMode: PathPointType = ...
    Line: PathPointType = ...
    PathMarker: PathPointType = ...
    PathTypeMask: PathPointType = ...
    Start: PathPointType = ...
    value__ = ...


class PenAlignment(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PenAlignment, values: Center (0), Inset (1), Left (3), Outset (2), Right (4) """
    Center: PenAlignment = ...
    Inset: PenAlignment = ...
    Left: PenAlignment = ...
    Outset: PenAlignment = ...
    Right: PenAlignment = ...
    value__ = ...


class PenType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PenType, values: HatchFill (1), LinearGradient (4), PathGradient (3), SolidColor (0), TextureFill (2) """
    HatchFill: PenType = ...
    LinearGradient: PenType = ...
    PathGradient: PenType = ...
    SolidColor: PenType = ...
    TextureFill: PenType = ...
    value__ = ...


class PixelOffsetMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PixelOffsetMode, values: Default (0), Half (4), HighQuality (2), HighSpeed (1), Invalid (-1), None (3) """
    Default: PixelOffsetMode = ...
    Half: PixelOffsetMode = ...
    HighQuality: PixelOffsetMode = ...
    HighSpeed: PixelOffsetMode = ...
    Invalid: PixelOffsetMode = ...
    value__ = ...


class QualityMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum QualityMode, values: Default (0), High (2), Invalid (-1), Low (1) """
    Default: QualityMode = ...
    High: QualityMode = ...
    Invalid: QualityMode = ...
    Low: QualityMode = ...
    value__ = ...


class RegionData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Data(self) -> Array:
        """
        Get: Data(self: RegionData) -> Array[Byte]
        Set: Data(self: RegionData) = value
        """
        ...



class SmoothingMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SmoothingMode, values: AntiAlias (4), Default (0), HighQuality (2), HighSpeed (1), Invalid (-1), None (3) """
    AntiAlias: SmoothingMode = ...
    Default: SmoothingMode = ...
    HighQuality: SmoothingMode = ...
    HighSpeed: SmoothingMode = ...
    Invalid: SmoothingMode = ...
    value__ = ...


class WarpMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WarpMode, values: Bilinear (1), Perspective (0) """
    Bilinear: WarpMode = ...
    Perspective: WarpMode = ...
    value__ = ...


class WrapMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WrapMode, values: Clamp (4), Tile (0), TileFlipX (1), TileFlipXY (3), TileFlipY (2) """
    Clamp: WrapMode = ...
    Tile: WrapMode = ...
    TileFlipX: WrapMode = ...
    TileFlipXY: WrapMode = ...
    TileFlipY: WrapMode = ...
    value__ = ...


