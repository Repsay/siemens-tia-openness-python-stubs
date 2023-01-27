# encoding: utf-8
# module System.Drawing calls itself Drawing
# from System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Drawing.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Attribute, Byte, Enum, EventHandler, Guid, 
    ICloneable, IDisposable, IntPtr, MarshalByRefObject, Single, Type)

from System.ComponentModel import (ExpandableObjectConverter, 
    ITypeDescriptorContext, TypeConverter)

from System.Drawing.Drawing2D import (CompositingMode, CompositingQuality, 
    CoordinateSpace, CustomLineCap, DashCap, DashStyle, FillMode, 
    FlushIntention, GraphicsContainer, GraphicsPath, GraphicsState, 
    InterpolationMode, LineCap, LineJoin, Matrix, MatrixOrder, PenAlignment, 
    PenType, PixelOffsetMode, RegionData, SmoothingMode, WrapMode)

from System.Drawing.Imaging import (BitmapData, ColorPalette, 
    EncoderParameters, FrameDimension, ImageFormat, ImageLockMode, Metafile, 
    PixelFormat, PropertyItem)

from System.Drawing.Text import HotkeyPrefix, TextRenderingHint

from System.Globalization import CultureInfo

from System.IO import Stream

from System.Runtime.Serialization import ISerializable

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (EnumerateMetafileProc, 
    GetThumbnailImageAbort, ISystemColorTracker, field#)
"""

# no functions
# classes

class Image(IDisposable, ICloneable, MarshalByRefObject, ISerializable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Flags(self) -> int:
        """ Get: Flags(self: Image) -> int """
        ...

    @property
    def FrameDimensionsList(self) -> Array:
        """ Get: FrameDimensionsList(self: Image) -> Array[Guid] """
        ...

    @property
    def Height(self) -> int:
        """ Get: Height(self: Image) -> int """
        ...

    @property
    def HorizontalResolution(self) -> Single:
        """ Get: HorizontalResolution(self: Image) -> Single """
        ...

    @property
    def Palette(self) -> ColorPalette:
        """
        Get: Palette(self: Image) -> ColorPalette
        Set: Palette(self: Image) = value
        """
        ...

    @property
    def PhysicalDimension(self) -> SizeF:
        """ Get: PhysicalDimension(self: Image) -> SizeF """
        ...

    @property
    def PixelFormat(self) -> PixelFormat:
        """ Get: PixelFormat(self: Image) -> PixelFormat """
        ...

    @property
    def PropertyIdList(self) -> Array:
        """ Get: PropertyIdList(self: Image) -> Array[int] """
        ...

    @property
    def PropertyItems(self) -> Array:
        """ Get: PropertyItems(self: Image) -> Array[PropertyItem] """
        ...

    @property
    def RawFormat(self) -> ImageFormat:
        """ Get: RawFormat(self: Image) -> ImageFormat """
        ...

    @property
    def Size(self) -> Size:
        """ Get: Size(self: Image) -> Size """
        ...

    @property
    def Tag(self) -> object:
        """
        Get: Tag(self: Image) -> object
        Set: Tag(self: Image) = value
        """
        ...

    @property
    def VerticalResolution(self) -> Single:
        """ Get: VerticalResolution(self: Image) -> Single """
        ...

    @property
    def Width(self) -> int:
        """ Get: Width(self: Image) -> int """
        ...


    @staticmethod
    def FromFile(filename:str, useEmbeddedColorManagement:bool = ...) -> Image:
        """
        FromFile(filename: str) -> Image
        FromFile(filename: str, useEmbeddedColorManagement: bool) -> Image
        """
        ...

    @staticmethod
    def FromHbitmap(hbitmap:IntPtr, hpalette:IntPtr = ...) -> Bitmap:
        """
        FromHbitmap(hbitmap: IntPtr) -> Bitmap
        FromHbitmap(hbitmap: IntPtr, hpalette: IntPtr) -> Bitmap
        """
        ...

    @staticmethod
    def FromStream(stream:Stream, useEmbeddedColorManagement:bool = ..., validateImageData:bool = ...) -> Image:
        """
        FromStream(stream: Stream) -> Image
        FromStream(stream: Stream, useEmbeddedColorManagement: bool) -> Image
        FromStream(stream: Stream, useEmbeddedColorManagement: bool, validateImageData: bool) -> Image
        """
        ...

    def GetBounds(self, pageUnit:GraphicsUnit) -> Tuple_[RectangleF, GraphicsUnit]:
        """ GetBounds(self: Image, pageUnit: GraphicsUnit) -> (RectangleF, GraphicsUnit) """
        ...

    def GetEncoderParameterList(self, encoder:Guid) -> EncoderParameters:
        """ GetEncoderParameterList(self: Image, encoder: Guid) -> EncoderParameters """
        ...

    def GetFrameCount(self, dimension:FrameDimension) -> int:
        """ GetFrameCount(self: Image, dimension: FrameDimension) -> int """
        ...

    @staticmethod
    def GetPixelFormatSize(pixfmt:PixelFormat) -> int:
        """ GetPixelFormatSize(pixfmt: PixelFormat) -> int """
        ...

    def GetPropertyItem(self, propid:int) -> PropertyItem:
        """ GetPropertyItem(self: Image, propid: int) -> PropertyItem """
        ...

    def GetThumbnailImage(self, thumbWidth:int, thumbHeight:int, callback, callbackData:IntPtr) -> Image: # Not found arg types: {'callback': 'GetThumbnailImageAbort'}
        """ GetThumbnailImage(self: Image, thumbWidth: int, thumbHeight: int, callback: GetThumbnailImageAbort, callbackData: IntPtr) -> Image """
        ...

    def GetThumbnailImageAbort(self, *args): #cannot find CLR method
        """ GetThumbnailImageAbort(object: object, method: IntPtr) """
        ...

    @staticmethod
    def IsAlphaPixelFormat(pixfmt:PixelFormat) -> bool:
        """ IsAlphaPixelFormat(pixfmt: PixelFormat) -> bool """
        ...

    @staticmethod
    def IsCanonicalPixelFormat(pixfmt:PixelFormat) -> bool:
        """ IsCanonicalPixelFormat(pixfmt: PixelFormat) -> bool """
        ...

    @staticmethod
    def IsExtendedPixelFormat(pixfmt:PixelFormat) -> bool:
        """ IsExtendedPixelFormat(pixfmt: PixelFormat) -> bool """
        ...

    def RemovePropertyItem(self, propid:int): # -> 
        """ RemovePropertyItem(self: Image, propid: int) """
        ...

    def RotateFlip(self, rotateFlipType:RotateFlipType): # -> 
        """ RotateFlip(self: Image, rotateFlipType: RotateFlipType) """
        ...

    def Save(self, *__args:str): # -> 
        """ Save(self: Image, filename: str)Save(self: Image, filename: str, format: ImageFormat)Save(self: Image, filename: str, encoder: ImageCodecInfo, encoderParams: EncoderParameters)Save(self: Image, stream: Stream, format: ImageFormat)Save(self: Image, stream: Stream, encoder: ImageCodecInfo, encoderParams: EncoderParameters) """
        ...

    def SaveAdd(self, *__args:EncoderParameters): # -> 
        """ SaveAdd(self: Image, encoderParams: EncoderParameters)SaveAdd(self: Image, image: Image, encoderParams: EncoderParameters) """
        ...

    def SelectActiveFrame(self, dimension:FrameDimension, frameIndex:int) -> int:
        """ SelectActiveFrame(self: Image, dimension: FrameDimension, frameIndex: int) -> int """
        ...

    def SetPropertyItem(self, propitem:PropertyItem): # -> 
        """ SetPropertyItem(self: Image, propitem: PropertyItem) """
        ...



class Bitmap(Image): # skipped bases: <type 'IDisposable'>, <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """
    Bitmap(filename: str)
    Bitmap(filename: str, useIcm: bool)
    Bitmap(type: Type, resource: str)
    Bitmap(stream: Stream)
    Bitmap(stream: Stream, useIcm: bool)
    Bitmap(width: int, height: int, stride: int, format: PixelFormat, scan0: IntPtr)
    Bitmap(width: int, height: int, format: PixelFormat)
    Bitmap(width: int, height: int)
    Bitmap(width: int, height: int, g: Graphics)
    Bitmap(original: Image)
    Bitmap(original: Image, width: int, height: int)
    Bitmap(original: Image, newSize: Size)
    """
    @staticmethod
    def FromHicon(hicon:IntPtr) -> Bitmap:
        """ FromHicon(hicon: IntPtr) -> Bitmap """
        ...

    @staticmethod
    def FromResource(hinstance:IntPtr, bitmapName:str) -> Bitmap:
        """ FromResource(hinstance: IntPtr, bitmapName: str) -> Bitmap """
        ...

    def GetHbitmap(self, background:Color = ...) -> IntPtr:
        """
        GetHbitmap(self: Bitmap) -> IntPtr
        GetHbitmap(self: Bitmap, background: Color) -> IntPtr
        """
        ...

    def GetHicon(self) -> IntPtr:
        """ GetHicon(self: Bitmap) -> IntPtr """
        ...

    def GetPixel(self, x:int, y:int) -> Color:
        """ GetPixel(self: Bitmap, x: int, y: int) -> Color """
        ...

    def LockBits(self, rect:Rectangle, flags:ImageLockMode, format:PixelFormat, bitmapData:BitmapData = ...) -> BitmapData:
        """
        LockBits(self: Bitmap, rect: Rectangle, flags: ImageLockMode, format: PixelFormat) -> BitmapData
        LockBits(self: Bitmap, rect: Rectangle, flags: ImageLockMode, format: PixelFormat, bitmapData: BitmapData) -> BitmapData
        """
        ...

    def MakeTransparent(self, transparentColor:Color = ...): # -> 
        """ MakeTransparent(self: Bitmap)MakeTransparent(self: Bitmap, transparentColor: Color) """
        ...

    def SetPixel(self, x:int, y:int, color:Color): # -> 
        """ SetPixel(self: Bitmap, x: int, y: int, color: Color) """
        ...

    def SetResolution(self, xDpi:Single, yDpi:Single): # -> 
        """ SetResolution(self: Bitmap, xDpi: Single, yDpi: Single) """
        ...

    def UnlockBits(self, bitmapdata:BitmapData): # -> 
        """ UnlockBits(self: Bitmap, bitmapdata: BitmapData) """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, filename: str)
        __new__(cls: type, filename: str, useIcm: bool)
        __new__(cls: type, type: Type, resource: str)
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, useIcm: bool)
        __new__(cls: type, width: int, height: int, stride: int, format: PixelFormat, scan0: IntPtr)
        __new__(cls: type, width: int, height: int, format: PixelFormat)
        __new__(cls: type, width: int, height: int)
        __new__(cls: type, width: int, height: int, g: Graphics)
        __new__(cls: type, original: Image)
        __new__(cls: type, original: Image, width: int, height: int)
        __new__(cls: type, original: Image, newSize: Size)
        """
        ...


class BitmapSuffixInSameAssemblyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ BitmapSuffixInSameAssemblyAttribute() """
    pass

class BitmapSuffixInSatelliteAssemblyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ BitmapSuffixInSatelliteAssemblyAttribute() """
    pass

class Brush(IDisposable, ICloneable, MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    def SetNativeBrush(self, *args): #cannot find CLR method
        """ SetNativeBrush(self: Brush, brush: IntPtr) """
        ...


class Brushes: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AliceBlue(self) -> Brush:
        """ Get: AliceBlue() -> Brush """
        ...

    @property
    def AntiqueWhite(self) -> Brush:
        """ Get: AntiqueWhite() -> Brush """
        ...

    @property
    def Aqua(self) -> Brush:
        """ Get: Aqua() -> Brush """
        ...

    @property
    def Aquamarine(self) -> Brush:
        """ Get: Aquamarine() -> Brush """
        ...

    @property
    def Azure(self) -> Brush:
        """ Get: Azure() -> Brush """
        ...

    @property
    def Beige(self) -> Brush:
        """ Get: Beige() -> Brush """
        ...

    @property
    def Bisque(self) -> Brush:
        """ Get: Bisque() -> Brush """
        ...

    @property
    def Black(self) -> Brush:
        """ Get: Black() -> Brush """
        ...

    @property
    def BlanchedAlmond(self) -> Brush:
        """ Get: BlanchedAlmond() -> Brush """
        ...

    @property
    def Blue(self) -> Brush:
        """ Get: Blue() -> Brush """
        ...

    @property
    def BlueViolet(self) -> Brush:
        """ Get: BlueViolet() -> Brush """
        ...

    @property
    def Brown(self) -> Brush:
        """ Get: Brown() -> Brush """
        ...

    @property
    def BurlyWood(self) -> Brush:
        """ Get: BurlyWood() -> Brush """
        ...

    @property
    def CadetBlue(self) -> Brush:
        """ Get: CadetBlue() -> Brush """
        ...

    @property
    def Chartreuse(self) -> Brush:
        """ Get: Chartreuse() -> Brush """
        ...

    @property
    def Chocolate(self) -> Brush:
        """ Get: Chocolate() -> Brush """
        ...

    @property
    def Coral(self) -> Brush:
        """ Get: Coral() -> Brush """
        ...

    @property
    def CornflowerBlue(self) -> Brush:
        """ Get: CornflowerBlue() -> Brush """
        ...

    @property
    def Cornsilk(self) -> Brush:
        """ Get: Cornsilk() -> Brush """
        ...

    @property
    def Crimson(self) -> Brush:
        """ Get: Crimson() -> Brush """
        ...

    @property
    def Cyan(self) -> Brush:
        """ Get: Cyan() -> Brush """
        ...

    @property
    def DarkBlue(self) -> Brush:
        """ Get: DarkBlue() -> Brush """
        ...

    @property
    def DarkCyan(self) -> Brush:
        """ Get: DarkCyan() -> Brush """
        ...

    @property
    def DarkGoldenrod(self) -> Brush:
        """ Get: DarkGoldenrod() -> Brush """
        ...

    @property
    def DarkGray(self) -> Brush:
        """ Get: DarkGray() -> Brush """
        ...

    @property
    def DarkGreen(self) -> Brush:
        """ Get: DarkGreen() -> Brush """
        ...

    @property
    def DarkKhaki(self) -> Brush:
        """ Get: DarkKhaki() -> Brush """
        ...

    @property
    def DarkMagenta(self) -> Brush:
        """ Get: DarkMagenta() -> Brush """
        ...

    @property
    def DarkOliveGreen(self) -> Brush:
        """ Get: DarkOliveGreen() -> Brush """
        ...

    @property
    def DarkOrange(self) -> Brush:
        """ Get: DarkOrange() -> Brush """
        ...

    @property
    def DarkOrchid(self) -> Brush:
        """ Get: DarkOrchid() -> Brush """
        ...

    @property
    def DarkRed(self) -> Brush:
        """ Get: DarkRed() -> Brush """
        ...

    @property
    def DarkSalmon(self) -> Brush:
        """ Get: DarkSalmon() -> Brush """
        ...

    @property
    def DarkSeaGreen(self) -> Brush:
        """ Get: DarkSeaGreen() -> Brush """
        ...

    @property
    def DarkSlateBlue(self) -> Brush:
        """ Get: DarkSlateBlue() -> Brush """
        ...

    @property
    def DarkSlateGray(self) -> Brush:
        """ Get: DarkSlateGray() -> Brush """
        ...

    @property
    def DarkTurquoise(self) -> Brush:
        """ Get: DarkTurquoise() -> Brush """
        ...

    @property
    def DarkViolet(self) -> Brush:
        """ Get: DarkViolet() -> Brush """
        ...

    @property
    def DeepPink(self) -> Brush:
        """ Get: DeepPink() -> Brush """
        ...

    @property
    def DeepSkyBlue(self) -> Brush:
        """ Get: DeepSkyBlue() -> Brush """
        ...

    @property
    def DimGray(self) -> Brush:
        """ Get: DimGray() -> Brush """
        ...

    @property
    def DodgerBlue(self) -> Brush:
        """ Get: DodgerBlue() -> Brush """
        ...

    @property
    def Firebrick(self) -> Brush:
        """ Get: Firebrick() -> Brush """
        ...

    @property
    def FloralWhite(self) -> Brush:
        """ Get: FloralWhite() -> Brush """
        ...

    @property
    def ForestGreen(self) -> Brush:
        """ Get: ForestGreen() -> Brush """
        ...

    @property
    def Fuchsia(self) -> Brush:
        """ Get: Fuchsia() -> Brush """
        ...

    @property
    def Gainsboro(self) -> Brush:
        """ Get: Gainsboro() -> Brush """
        ...

    @property
    def GhostWhite(self) -> Brush:
        """ Get: GhostWhite() -> Brush """
        ...

    @property
    def Gold(self) -> Brush:
        """ Get: Gold() -> Brush """
        ...

    @property
    def Goldenrod(self) -> Brush:
        """ Get: Goldenrod() -> Brush """
        ...

    @property
    def Gray(self) -> Brush:
        """ Get: Gray() -> Brush """
        ...

    @property
    def Green(self) -> Brush:
        """ Get: Green() -> Brush """
        ...

    @property
    def GreenYellow(self) -> Brush:
        """ Get: GreenYellow() -> Brush """
        ...

    @property
    def Honeydew(self) -> Brush:
        """ Get: Honeydew() -> Brush """
        ...

    @property
    def HotPink(self) -> Brush:
        """ Get: HotPink() -> Brush """
        ...

    @property
    def IndianRed(self) -> Brush:
        """ Get: IndianRed() -> Brush """
        ...

    @property
    def Indigo(self) -> Brush:
        """ Get: Indigo() -> Brush """
        ...

    @property
    def Ivory(self) -> Brush:
        """ Get: Ivory() -> Brush """
        ...

    @property
    def Khaki(self) -> Brush:
        """ Get: Khaki() -> Brush """
        ...

    @property
    def Lavender(self) -> Brush:
        """ Get: Lavender() -> Brush """
        ...

    @property
    def LavenderBlush(self) -> Brush:
        """ Get: LavenderBlush() -> Brush """
        ...

    @property
    def LawnGreen(self) -> Brush:
        """ Get: LawnGreen() -> Brush """
        ...

    @property
    def LemonChiffon(self) -> Brush:
        """ Get: LemonChiffon() -> Brush """
        ...

    @property
    def LightBlue(self) -> Brush:
        """ Get: LightBlue() -> Brush """
        ...

    @property
    def LightCoral(self) -> Brush:
        """ Get: LightCoral() -> Brush """
        ...

    @property
    def LightCyan(self) -> Brush:
        """ Get: LightCyan() -> Brush """
        ...

    @property
    def LightGoldenrodYellow(self) -> Brush:
        """ Get: LightGoldenrodYellow() -> Brush """
        ...

    @property
    def LightGray(self) -> Brush:
        """ Get: LightGray() -> Brush """
        ...

    @property
    def LightGreen(self) -> Brush:
        """ Get: LightGreen() -> Brush """
        ...

    @property
    def LightPink(self) -> Brush:
        """ Get: LightPink() -> Brush """
        ...

    @property
    def LightSalmon(self) -> Brush:
        """ Get: LightSalmon() -> Brush """
        ...

    @property
    def LightSeaGreen(self) -> Brush:
        """ Get: LightSeaGreen() -> Brush """
        ...

    @property
    def LightSkyBlue(self) -> Brush:
        """ Get: LightSkyBlue() -> Brush """
        ...

    @property
    def LightSlateGray(self) -> Brush:
        """ Get: LightSlateGray() -> Brush """
        ...

    @property
    def LightSteelBlue(self) -> Brush:
        """ Get: LightSteelBlue() -> Brush """
        ...

    @property
    def LightYellow(self) -> Brush:
        """ Get: LightYellow() -> Brush """
        ...

    @property
    def Lime(self) -> Brush:
        """ Get: Lime() -> Brush """
        ...

    @property
    def LimeGreen(self) -> Brush:
        """ Get: LimeGreen() -> Brush """
        ...

    @property
    def Linen(self) -> Brush:
        """ Get: Linen() -> Brush """
        ...

    @property
    def Magenta(self) -> Brush:
        """ Get: Magenta() -> Brush """
        ...

    @property
    def Maroon(self) -> Brush:
        """ Get: Maroon() -> Brush """
        ...

    @property
    def MediumAquamarine(self) -> Brush:
        """ Get: MediumAquamarine() -> Brush """
        ...

    @property
    def MediumBlue(self) -> Brush:
        """ Get: MediumBlue() -> Brush """
        ...

    @property
    def MediumOrchid(self) -> Brush:
        """ Get: MediumOrchid() -> Brush """
        ...

    @property
    def MediumPurple(self) -> Brush:
        """ Get: MediumPurple() -> Brush """
        ...

    @property
    def MediumSeaGreen(self) -> Brush:
        """ Get: MediumSeaGreen() -> Brush """
        ...

    @property
    def MediumSlateBlue(self) -> Brush:
        """ Get: MediumSlateBlue() -> Brush """
        ...

    @property
    def MediumSpringGreen(self) -> Brush:
        """ Get: MediumSpringGreen() -> Brush """
        ...

    @property
    def MediumTurquoise(self) -> Brush:
        """ Get: MediumTurquoise() -> Brush """
        ...

    @property
    def MediumVioletRed(self) -> Brush:
        """ Get: MediumVioletRed() -> Brush """
        ...

    @property
    def MidnightBlue(self) -> Brush:
        """ Get: MidnightBlue() -> Brush """
        ...

    @property
    def MintCream(self) -> Brush:
        """ Get: MintCream() -> Brush """
        ...

    @property
    def MistyRose(self) -> Brush:
        """ Get: MistyRose() -> Brush """
        ...

    @property
    def Moccasin(self) -> Brush:
        """ Get: Moccasin() -> Brush """
        ...

    @property
    def NavajoWhite(self) -> Brush:
        """ Get: NavajoWhite() -> Brush """
        ...

    @property
    def Navy(self) -> Brush:
        """ Get: Navy() -> Brush """
        ...

    @property
    def OldLace(self) -> Brush:
        """ Get: OldLace() -> Brush """
        ...

    @property
    def Olive(self) -> Brush:
        """ Get: Olive() -> Brush """
        ...

    @property
    def OliveDrab(self) -> Brush:
        """ Get: OliveDrab() -> Brush """
        ...

    @property
    def Orange(self) -> Brush:
        """ Get: Orange() -> Brush """
        ...

    @property
    def OrangeRed(self) -> Brush:
        """ Get: OrangeRed() -> Brush """
        ...

    @property
    def Orchid(self) -> Brush:
        """ Get: Orchid() -> Brush """
        ...

    @property
    def PaleGoldenrod(self) -> Brush:
        """ Get: PaleGoldenrod() -> Brush """
        ...

    @property
    def PaleGreen(self) -> Brush:
        """ Get: PaleGreen() -> Brush """
        ...

    @property
    def PaleTurquoise(self) -> Brush:
        """ Get: PaleTurquoise() -> Brush """
        ...

    @property
    def PaleVioletRed(self) -> Brush:
        """ Get: PaleVioletRed() -> Brush """
        ...

    @property
    def PapayaWhip(self) -> Brush:
        """ Get: PapayaWhip() -> Brush """
        ...

    @property
    def PeachPuff(self) -> Brush:
        """ Get: PeachPuff() -> Brush """
        ...

    @property
    def Peru(self) -> Brush:
        """ Get: Peru() -> Brush """
        ...

    @property
    def Pink(self) -> Brush:
        """ Get: Pink() -> Brush """
        ...

    @property
    def Plum(self) -> Brush:
        """ Get: Plum() -> Brush """
        ...

    @property
    def PowderBlue(self) -> Brush:
        """ Get: PowderBlue() -> Brush """
        ...

    @property
    def Purple(self) -> Brush:
        """ Get: Purple() -> Brush """
        ...

    @property
    def Red(self) -> Brush:
        """ Get: Red() -> Brush """
        ...

    @property
    def RosyBrown(self) -> Brush:
        """ Get: RosyBrown() -> Brush """
        ...

    @property
    def RoyalBlue(self) -> Brush:
        """ Get: RoyalBlue() -> Brush """
        ...

    @property
    def SaddleBrown(self) -> Brush:
        """ Get: SaddleBrown() -> Brush """
        ...

    @property
    def Salmon(self) -> Brush:
        """ Get: Salmon() -> Brush """
        ...

    @property
    def SandyBrown(self) -> Brush:
        """ Get: SandyBrown() -> Brush """
        ...

    @property
    def SeaGreen(self) -> Brush:
        """ Get: SeaGreen() -> Brush """
        ...

    @property
    def SeaShell(self) -> Brush:
        """ Get: SeaShell() -> Brush """
        ...

    @property
    def Sienna(self) -> Brush:
        """ Get: Sienna() -> Brush """
        ...

    @property
    def Silver(self) -> Brush:
        """ Get: Silver() -> Brush """
        ...

    @property
    def SkyBlue(self) -> Brush:
        """ Get: SkyBlue() -> Brush """
        ...

    @property
    def SlateBlue(self) -> Brush:
        """ Get: SlateBlue() -> Brush """
        ...

    @property
    def SlateGray(self) -> Brush:
        """ Get: SlateGray() -> Brush """
        ...

    @property
    def Snow(self) -> Brush:
        """ Get: Snow() -> Brush """
        ...

    @property
    def SpringGreen(self) -> Brush:
        """ Get: SpringGreen() -> Brush """
        ...

    @property
    def SteelBlue(self) -> Brush:
        """ Get: SteelBlue() -> Brush """
        ...

    @property
    def Tan(self) -> Brush:
        """ Get: Tan() -> Brush """
        ...

    @property
    def Teal(self) -> Brush:
        """ Get: Teal() -> Brush """
        ...

    @property
    def Thistle(self) -> Brush:
        """ Get: Thistle() -> Brush """
        ...

    @property
    def Tomato(self) -> Brush:
        """ Get: Tomato() -> Brush """
        ...

    @property
    def Transparent(self) -> Brush:
        """ Get: Transparent() -> Brush """
        ...

    @property
    def Turquoise(self) -> Brush:
        """ Get: Turquoise() -> Brush """
        ...

    @property
    def Violet(self) -> Brush:
        """ Get: Violet() -> Brush """
        ...

    @property
    def Wheat(self) -> Brush:
        """ Get: Wheat() -> Brush """
        ...

    @property
    def White(self) -> Brush:
        """ Get: White() -> Brush """
        ...

    @property
    def WhiteSmoke(self) -> Brush:
        """ Get: WhiteSmoke() -> Brush """
        ...

    @property
    def Yellow(self) -> Brush:
        """ Get: Yellow() -> Brush """
        ...

    @property
    def YellowGreen(self) -> Brush:
        """ Get: YellowGreen() -> Brush """
        ...




class BufferedGraphics(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Graphics(self) -> Graphics:
        """ Get: Graphics(self: BufferedGraphics) -> Graphics """
        ...


    def Render(self, *__args:IntPtr): # -> 
        """ Render(self: BufferedGraphics)Render(self: BufferedGraphics, targetDC: IntPtr)Render(self: BufferedGraphics, target: Graphics) """
        ...


class BufferedGraphicsContext(IDisposable): # skipped bases: <type 'object'>
    """ BufferedGraphicsContext() """
    @property
    def MaximumBuffer(self) -> Size:
        """
        Get: MaximumBuffer(self: BufferedGraphicsContext) -> Size
        Set: MaximumBuffer(self: BufferedGraphicsContext) = value
        """
        ...


    def Allocate(self, *__args) -> BufferedGraphics:
        """
        Allocate(self: BufferedGraphicsContext, targetGraphics: Graphics, targetRectangle: Rectangle) -> BufferedGraphics
        Allocate(self: BufferedGraphicsContext, targetDC: IntPtr, targetRectangle: Rectangle) -> BufferedGraphics
        """
        ...

    def Invalidate(self): # -> 
        """ Invalidate(self: BufferedGraphicsContext) """
        ...


class BufferedGraphicsManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> BufferedGraphicsContext:
        """ Get: Current() -> BufferedGraphicsContext """
        ...




class CharacterRange: # skipped bases: <type 'object'>, <type 'object'>
    """ CharacterRange(First: int, Length: int) """
    @property
    def First(self) -> int:
        """
        Get: First(self: CharacterRange) -> int
        Set: First(self: CharacterRange) = value
        """
        ...

    @property
    def Length(self) -> int:
        """
        Get: Length(self: CharacterRange) -> int
        Set: Length(self: CharacterRange) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: CharacterRange, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CharacterRange) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Color: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def A(self) -> Byte:
        """ Get: A(self: Color) -> Byte """
        ...

    @property
    def AliceBlue(self) -> Color:
        """ Get: AliceBlue() -> Color """
        ...

    @property
    def AntiqueWhite(self) -> Color:
        """ Get: AntiqueWhite() -> Color """
        ...

    @property
    def Aqua(self) -> Color:
        """ Get: Aqua() -> Color """
        ...

    @property
    def Aquamarine(self) -> Color:
        """ Get: Aquamarine() -> Color """
        ...

    @property
    def Azure(self) -> Color:
        """ Get: Azure() -> Color """
        ...

    @property
    def B(self) -> Byte:
        """ Get: B(self: Color) -> Byte """
        ...

    @property
    def Beige(self) -> Color:
        """ Get: Beige() -> Color """
        ...

    @property
    def Bisque(self) -> Color:
        """ Get: Bisque() -> Color """
        ...

    @property
    def Black(self) -> Color:
        """ Get: Black() -> Color """
        ...

    @property
    def BlanchedAlmond(self) -> Color:
        """ Get: BlanchedAlmond() -> Color """
        ...

    @property
    def Blue(self) -> Color:
        """ Get: Blue() -> Color """
        ...

    @property
    def BlueViolet(self) -> Color:
        """ Get: BlueViolet() -> Color """
        ...

    @property
    def Brown(self) -> Color:
        """ Get: Brown() -> Color """
        ...

    @property
    def BurlyWood(self) -> Color:
        """ Get: BurlyWood() -> Color """
        ...

    @property
    def CadetBlue(self) -> Color:
        """ Get: CadetBlue() -> Color """
        ...

    @property
    def Chartreuse(self) -> Color:
        """ Get: Chartreuse() -> Color """
        ...

    @property
    def Chocolate(self) -> Color:
        """ Get: Chocolate() -> Color """
        ...

    @property
    def Coral(self) -> Color:
        """ Get: Coral() -> Color """
        ...

    @property
    def CornflowerBlue(self) -> Color:
        """ Get: CornflowerBlue() -> Color """
        ...

    @property
    def Cornsilk(self) -> Color:
        """ Get: Cornsilk() -> Color """
        ...

    @property
    def Crimson(self) -> Color:
        """ Get: Crimson() -> Color """
        ...

    @property
    def Cyan(self) -> Color:
        """ Get: Cyan() -> Color """
        ...

    @property
    def DarkBlue(self) -> Color:
        """ Get: DarkBlue() -> Color """
        ...

    @property
    def DarkCyan(self) -> Color:
        """ Get: DarkCyan() -> Color """
        ...

    @property
    def DarkGoldenrod(self) -> Color:
        """ Get: DarkGoldenrod() -> Color """
        ...

    @property
    def DarkGray(self) -> Color:
        """ Get: DarkGray() -> Color """
        ...

    @property
    def DarkGreen(self) -> Color:
        """ Get: DarkGreen() -> Color """
        ...

    @property
    def DarkKhaki(self) -> Color:
        """ Get: DarkKhaki() -> Color """
        ...

    @property
    def DarkMagenta(self) -> Color:
        """ Get: DarkMagenta() -> Color """
        ...

    @property
    def DarkOliveGreen(self) -> Color:
        """ Get: DarkOliveGreen() -> Color """
        ...

    @property
    def DarkOrange(self) -> Color:
        """ Get: DarkOrange() -> Color """
        ...

    @property
    def DarkOrchid(self) -> Color:
        """ Get: DarkOrchid() -> Color """
        ...

    @property
    def DarkRed(self) -> Color:
        """ Get: DarkRed() -> Color """
        ...

    @property
    def DarkSalmon(self) -> Color:
        """ Get: DarkSalmon() -> Color """
        ...

    @property
    def DarkSeaGreen(self) -> Color:
        """ Get: DarkSeaGreen() -> Color """
        ...

    @property
    def DarkSlateBlue(self) -> Color:
        """ Get: DarkSlateBlue() -> Color """
        ...

    @property
    def DarkSlateGray(self) -> Color:
        """ Get: DarkSlateGray() -> Color """
        ...

    @property
    def DarkTurquoise(self) -> Color:
        """ Get: DarkTurquoise() -> Color """
        ...

    @property
    def DarkViolet(self) -> Color:
        """ Get: DarkViolet() -> Color """
        ...

    @property
    def DeepPink(self) -> Color:
        """ Get: DeepPink() -> Color """
        ...

    @property
    def DeepSkyBlue(self) -> Color:
        """ Get: DeepSkyBlue() -> Color """
        ...

    @property
    def DimGray(self) -> Color:
        """ Get: DimGray() -> Color """
        ...

    @property
    def DodgerBlue(self) -> Color:
        """ Get: DodgerBlue() -> Color """
        ...

    @property
    def Firebrick(self) -> Color:
        """ Get: Firebrick() -> Color """
        ...

    @property
    def FloralWhite(self) -> Color:
        """ Get: FloralWhite() -> Color """
        ...

    @property
    def ForestGreen(self) -> Color:
        """ Get: ForestGreen() -> Color """
        ...

    @property
    def Fuchsia(self) -> Color:
        """ Get: Fuchsia() -> Color """
        ...

    @property
    def G(self) -> Byte:
        """ Get: G(self: Color) -> Byte """
        ...

    @property
    def Gainsboro(self) -> Color:
        """ Get: Gainsboro() -> Color """
        ...

    @property
    def GhostWhite(self) -> Color:
        """ Get: GhostWhite() -> Color """
        ...

    @property
    def Gold(self) -> Color:
        """ Get: Gold() -> Color """
        ...

    @property
    def Goldenrod(self) -> Color:
        """ Get: Goldenrod() -> Color """
        ...

    @property
    def Gray(self) -> Color:
        """ Get: Gray() -> Color """
        ...

    @property
    def Green(self) -> Color:
        """ Get: Green() -> Color """
        ...

    @property
    def GreenYellow(self) -> Color:
        """ Get: GreenYellow() -> Color """
        ...

    @property
    def Honeydew(self) -> Color:
        """ Get: Honeydew() -> Color """
        ...

    @property
    def HotPink(self) -> Color:
        """ Get: HotPink() -> Color """
        ...

    @property
    def IndianRed(self) -> Color:
        """ Get: IndianRed() -> Color """
        ...

    @property
    def Indigo(self) -> Color:
        """ Get: Indigo() -> Color """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: Color) -> bool """
        ...

    @property
    def IsKnownColor(self) -> bool:
        """ Get: IsKnownColor(self: Color) -> bool """
        ...

    @property
    def IsNamedColor(self) -> bool:
        """ Get: IsNamedColor(self: Color) -> bool """
        ...

    @property
    def IsSystemColor(self) -> bool:
        """ Get: IsSystemColor(self: Color) -> bool """
        ...

    @property
    def Ivory(self) -> Color:
        """ Get: Ivory() -> Color """
        ...

    @property
    def Khaki(self) -> Color:
        """ Get: Khaki() -> Color """
        ...

    @property
    def Lavender(self) -> Color:
        """ Get: Lavender() -> Color """
        ...

    @property
    def LavenderBlush(self) -> Color:
        """ Get: LavenderBlush() -> Color """
        ...

    @property
    def LawnGreen(self) -> Color:
        """ Get: LawnGreen() -> Color """
        ...

    @property
    def LemonChiffon(self) -> Color:
        """ Get: LemonChiffon() -> Color """
        ...

    @property
    def LightBlue(self) -> Color:
        """ Get: LightBlue() -> Color """
        ...

    @property
    def LightCoral(self) -> Color:
        """ Get: LightCoral() -> Color """
        ...

    @property
    def LightCyan(self) -> Color:
        """ Get: LightCyan() -> Color """
        ...

    @property
    def LightGoldenrodYellow(self) -> Color:
        """ Get: LightGoldenrodYellow() -> Color """
        ...

    @property
    def LightGray(self) -> Color:
        """ Get: LightGray() -> Color """
        ...

    @property
    def LightGreen(self) -> Color:
        """ Get: LightGreen() -> Color """
        ...

    @property
    def LightPink(self) -> Color:
        """ Get: LightPink() -> Color """
        ...

    @property
    def LightSalmon(self) -> Color:
        """ Get: LightSalmon() -> Color """
        ...

    @property
    def LightSeaGreen(self) -> Color:
        """ Get: LightSeaGreen() -> Color """
        ...

    @property
    def LightSkyBlue(self) -> Color:
        """ Get: LightSkyBlue() -> Color """
        ...

    @property
    def LightSlateGray(self) -> Color:
        """ Get: LightSlateGray() -> Color """
        ...

    @property
    def LightSteelBlue(self) -> Color:
        """ Get: LightSteelBlue() -> Color """
        ...

    @property
    def LightYellow(self) -> Color:
        """ Get: LightYellow() -> Color """
        ...

    @property
    def Lime(self) -> Color:
        """ Get: Lime() -> Color """
        ...

    @property
    def LimeGreen(self) -> Color:
        """ Get: LimeGreen() -> Color """
        ...

    @property
    def Linen(self) -> Color:
        """ Get: Linen() -> Color """
        ...

    @property
    def Magenta(self) -> Color:
        """ Get: Magenta() -> Color """
        ...

    @property
    def Maroon(self) -> Color:
        """ Get: Maroon() -> Color """
        ...

    @property
    def MediumAquamarine(self) -> Color:
        """ Get: MediumAquamarine() -> Color """
        ...

    @property
    def MediumBlue(self) -> Color:
        """ Get: MediumBlue() -> Color """
        ...

    @property
    def MediumOrchid(self) -> Color:
        """ Get: MediumOrchid() -> Color """
        ...

    @property
    def MediumPurple(self) -> Color:
        """ Get: MediumPurple() -> Color """
        ...

    @property
    def MediumSeaGreen(self) -> Color:
        """ Get: MediumSeaGreen() -> Color """
        ...

    @property
    def MediumSlateBlue(self) -> Color:
        """ Get: MediumSlateBlue() -> Color """
        ...

    @property
    def MediumSpringGreen(self) -> Color:
        """ Get: MediumSpringGreen() -> Color """
        ...

    @property
    def MediumTurquoise(self) -> Color:
        """ Get: MediumTurquoise() -> Color """
        ...

    @property
    def MediumVioletRed(self) -> Color:
        """ Get: MediumVioletRed() -> Color """
        ...

    @property
    def MidnightBlue(self) -> Color:
        """ Get: MidnightBlue() -> Color """
        ...

    @property
    def MintCream(self) -> Color:
        """ Get: MintCream() -> Color """
        ...

    @property
    def MistyRose(self) -> Color:
        """ Get: MistyRose() -> Color """
        ...

    @property
    def Moccasin(self) -> Color:
        """ Get: Moccasin() -> Color """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Color) -> str """
        ...

    @property
    def NavajoWhite(self) -> Color:
        """ Get: NavajoWhite() -> Color """
        ...

    @property
    def Navy(self) -> Color:
        """ Get: Navy() -> Color """
        ...

    @property
    def OldLace(self) -> Color:
        """ Get: OldLace() -> Color """
        ...

    @property
    def Olive(self) -> Color:
        """ Get: Olive() -> Color """
        ...

    @property
    def OliveDrab(self) -> Color:
        """ Get: OliveDrab() -> Color """
        ...

    @property
    def Orange(self) -> Color:
        """ Get: Orange() -> Color """
        ...

    @property
    def OrangeRed(self) -> Color:
        """ Get: OrangeRed() -> Color """
        ...

    @property
    def Orchid(self) -> Color:
        """ Get: Orchid() -> Color """
        ...

    @property
    def PaleGoldenrod(self) -> Color:
        """ Get: PaleGoldenrod() -> Color """
        ...

    @property
    def PaleGreen(self) -> Color:
        """ Get: PaleGreen() -> Color """
        ...

    @property
    def PaleTurquoise(self) -> Color:
        """ Get: PaleTurquoise() -> Color """
        ...

    @property
    def PaleVioletRed(self) -> Color:
        """ Get: PaleVioletRed() -> Color """
        ...

    @property
    def PapayaWhip(self) -> Color:
        """ Get: PapayaWhip() -> Color """
        ...

    @property
    def PeachPuff(self) -> Color:
        """ Get: PeachPuff() -> Color """
        ...

    @property
    def Peru(self) -> Color:
        """ Get: Peru() -> Color """
        ...

    @property
    def Pink(self) -> Color:
        """ Get: Pink() -> Color """
        ...

    @property
    def Plum(self) -> Color:
        """ Get: Plum() -> Color """
        ...

    @property
    def PowderBlue(self) -> Color:
        """ Get: PowderBlue() -> Color """
        ...

    @property
    def Purple(self) -> Color:
        """ Get: Purple() -> Color """
        ...

    @property
    def R(self) -> Byte:
        """ Get: R(self: Color) -> Byte """
        ...

    @property
    def Red(self) -> Color:
        """ Get: Red() -> Color """
        ...

    @property
    def RosyBrown(self) -> Color:
        """ Get: RosyBrown() -> Color """
        ...

    @property
    def RoyalBlue(self) -> Color:
        """ Get: RoyalBlue() -> Color """
        ...

    @property
    def SaddleBrown(self) -> Color:
        """ Get: SaddleBrown() -> Color """
        ...

    @property
    def Salmon(self) -> Color:
        """ Get: Salmon() -> Color """
        ...

    @property
    def SandyBrown(self) -> Color:
        """ Get: SandyBrown() -> Color """
        ...

    @property
    def SeaGreen(self) -> Color:
        """ Get: SeaGreen() -> Color """
        ...

    @property
    def SeaShell(self) -> Color:
        """ Get: SeaShell() -> Color """
        ...

    @property
    def Sienna(self) -> Color:
        """ Get: Sienna() -> Color """
        ...

    @property
    def Silver(self) -> Color:
        """ Get: Silver() -> Color """
        ...

    @property
    def SkyBlue(self) -> Color:
        """ Get: SkyBlue() -> Color """
        ...

    @property
    def SlateBlue(self) -> Color:
        """ Get: SlateBlue() -> Color """
        ...

    @property
    def SlateGray(self) -> Color:
        """ Get: SlateGray() -> Color """
        ...

    @property
    def Snow(self) -> Color:
        """ Get: Snow() -> Color """
        ...

    @property
    def SpringGreen(self) -> Color:
        """ Get: SpringGreen() -> Color """
        ...

    @property
    def SteelBlue(self) -> Color:
        """ Get: SteelBlue() -> Color """
        ...

    @property
    def Tan(self) -> Color:
        """ Get: Tan() -> Color """
        ...

    @property
    def Teal(self) -> Color:
        """ Get: Teal() -> Color """
        ...

    @property
    def Thistle(self) -> Color:
        """ Get: Thistle() -> Color """
        ...

    @property
    def Tomato(self) -> Color:
        """ Get: Tomato() -> Color """
        ...

    @property
    def Transparent(self) -> Color:
        """ Get: Transparent() -> Color """
        ...

    @property
    def Turquoise(self) -> Color:
        """ Get: Turquoise() -> Color """
        ...

    @property
    def Violet(self) -> Color:
        """ Get: Violet() -> Color """
        ...

    @property
    def Wheat(self) -> Color:
        """ Get: Wheat() -> Color """
        ...

    @property
    def White(self) -> Color:
        """ Get: White() -> Color """
        ...

    @property
    def WhiteSmoke(self) -> Color:
        """ Get: WhiteSmoke() -> Color """
        ...

    @property
    def Yellow(self) -> Color:
        """ Get: Yellow() -> Color """
        ...

    @property
    def YellowGreen(self) -> Color:
        """ Get: YellowGreen() -> Color """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Color, obj: object) -> bool """
        ...

    @staticmethod
    def FromArgb(*__args:int) -> Color:
        """
        FromArgb(argb: int) -> Color
        FromArgb(red: int, green: int, blue: int) -> Color
        FromArgb(alpha: int, red: int, green: int, blue: int) -> Color
        FromArgb(alpha: int, baseColor: Color) -> Color
        """
        ...

    @staticmethod
    def FromKnownColor(color:KnownColor) -> Color:
        """ FromKnownColor(color: KnownColor) -> Color """
        ...

    @staticmethod
    def FromName(name:str) -> Color:
        """ FromName(name: str) -> Color """
        ...

    def GetBrightness(self) -> Single:
        """ GetBrightness(self: Color) -> Single """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Color) -> int """
        ...

    def GetHue(self) -> Single:
        """ GetHue(self: Color) -> Single """
        ...

    def GetSaturation(self) -> Single:
        """ GetSaturation(self: Color) -> Single """
        ...

    def ToArgb(self) -> int:
        """ ToArgb(self: Color) -> int """
        ...

    def ToKnownColor(self) -> KnownColor:
        """ ToKnownColor(self: Color) -> KnownColor """
        ...

    def ToString(self) -> str:
        """ ToString(self: Color) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Empty: Color = ...


class ColorConverter(TypeConverter): # skipped bases: <type 'object'>
    """ ColorConverter() """
    pass

class ColorTranslator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FromHtml(htmlColor:str) -> Color:
        """ FromHtml(htmlColor: str) -> Color """
        ...

    @staticmethod
    def FromOle(oleColor:int) -> Color:
        """ FromOle(oleColor: int) -> Color """
        ...

    @staticmethod
    def FromWin32(win32Color:int) -> Color:
        """ FromWin32(win32Color: int) -> Color """
        ...

    @staticmethod
    def ToHtml(c:Color) -> str:
        """ ToHtml(c: Color) -> str """
        ...

    @staticmethod
    def ToOle(c:Color) -> int:
        """ ToOle(c: Color) -> int """
        ...

    @staticmethod
    def ToWin32(c:Color) -> int:
        """ ToWin32(c: Color) -> int """
        ...


class ContentAlignment(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ContentAlignment, values: BottomCenter (512), BottomLeft (256), BottomRight (1024), MiddleCenter (32), MiddleLeft (16), MiddleRight (64), TopCenter (2), TopLeft (1), TopRight (4) """
    BottomCenter: ContentAlignment = ...
    BottomLeft: ContentAlignment = ...
    BottomRight: ContentAlignment = ...
    MiddleCenter: ContentAlignment = ...
    MiddleLeft: ContentAlignment = ...
    MiddleRight: ContentAlignment = ...
    TopCenter: ContentAlignment = ...
    TopLeft: ContentAlignment = ...
    TopRight: ContentAlignment = ...
    value__ = ...


class CopyPixelOperation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CopyPixelOperation, values: Blackness (66), CaptureBlt (1073741824), DestinationInvert (5570569), MergeCopy (12583114), MergePaint (12255782), NoMirrorBitmap (-2147483648), NotSourceCopy (3342344), NotSourceErase (1114278), PatCopy (15728673), PatInvert (5898313), PatPaint (16452105), SourceAnd (8913094), SourceCopy (13369376), SourceErase (4457256), SourceInvert (6684742), SourcePaint (15597702), Whiteness (16711778) """
    Blackness: CopyPixelOperation = ...
    CaptureBlt: CopyPixelOperation = ...
    DestinationInvert: CopyPixelOperation = ...
    MergeCopy: CopyPixelOperation = ...
    MergePaint: CopyPixelOperation = ...
    NoMirrorBitmap: CopyPixelOperation = ...
    NotSourceCopy: CopyPixelOperation = ...
    NotSourceErase: CopyPixelOperation = ...
    PatCopy: CopyPixelOperation = ...
    PatInvert: CopyPixelOperation = ...
    PatPaint: CopyPixelOperation = ...
    SourceAnd: CopyPixelOperation = ...
    SourceCopy: CopyPixelOperation = ...
    SourceErase: CopyPixelOperation = ...
    SourceInvert: CopyPixelOperation = ...
    SourcePaint: CopyPixelOperation = ...
    value__ = ...
    Whiteness: CopyPixelOperation = ...


class Font(IDisposable, ICloneable, MarshalByRefObject, ISerializable): # skipped bases: <type 'object'>
    """
    Font(prototype: Font, newStyle: FontStyle)
    Font(family: FontFamily, emSize: Single, style: FontStyle, unit: GraphicsUnit)
    Font(family: FontFamily, emSize: Single, style: FontStyle, unit: GraphicsUnit, gdiCharSet: Byte)
    Font(family: FontFamily, emSize: Single, style: FontStyle, unit: GraphicsUnit, gdiCharSet: Byte, gdiVerticalFont: bool)
    Font(familyName: str, emSize: Single, style: FontStyle, unit: GraphicsUnit, gdiCharSet: Byte)
    Font(familyName: str, emSize: Single, style: FontStyle, unit: GraphicsUnit, gdiCharSet: Byte, gdiVerticalFont: bool)
    Font(family: FontFamily, emSize: Single, style: FontStyle)
    Font(family: FontFamily, emSize: Single, unit: GraphicsUnit)
    Font(family: FontFamily, emSize: Single)
    Font(familyName: str, emSize: Single, style: FontStyle, unit: GraphicsUnit)
    Font(familyName: str, emSize: Single, style: FontStyle)
    Font(familyName: str, emSize: Single, unit: GraphicsUnit)
    Font(familyName: str, emSize: Single)
    """
    @property
    def Bold(self) -> bool:
        """ Get: Bold(self: Font) -> bool """
        ...

    @property
    def FontFamily(self) -> FontFamily:
        """ Get: FontFamily(self: Font) -> FontFamily """
        ...

    @property
    def GdiCharSet(self) -> Byte:
        """ Get: GdiCharSet(self: Font) -> Byte """
        ...

    @property
    def GdiVerticalFont(self) -> bool:
        """ Get: GdiVerticalFont(self: Font) -> bool """
        ...

    @property
    def Height(self) -> int:
        """ Get: Height(self: Font) -> int """
        ...

    @property
    def IsSystemFont(self) -> bool:
        """ Get: IsSystemFont(self: Font) -> bool """
        ...

    @property
    def Italic(self) -> bool:
        """ Get: Italic(self: Font) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Font) -> str """
        ...

    @property
    def OriginalFontName(self) -> str:
        """ Get: OriginalFontName(self: Font) -> str """
        ...

    @property
    def Size(self) -> Single:
        """ Get: Size(self: Font) -> Single """
        ...

    @property
    def SizeInPoints(self) -> Single:
        """ Get: SizeInPoints(self: Font) -> Single """
        ...

    @property
    def Strikeout(self) -> bool:
        """ Get: Strikeout(self: Font) -> bool """
        ...

    @property
    def Style(self) -> FontStyle:
        """ Get: Style(self: Font) -> FontStyle """
        ...

    @property
    def SystemFontName(self) -> str:
        """ Get: SystemFontName(self: Font) -> str """
        ...

    @property
    def Underline(self) -> bool:
        """ Get: Underline(self: Font) -> bool """
        ...

    @property
    def Unit(self) -> GraphicsUnit:
        """ Get: Unit(self: Font) -> GraphicsUnit """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Font, obj: object) -> bool """
        ...

    @staticmethod
    def FromHdc(hdc:IntPtr) -> Font:
        """ FromHdc(hdc: IntPtr) -> Font """
        ...

    @staticmethod
    def FromHfont(hfont:IntPtr) -> Font:
        """ FromHfont(hfont: IntPtr) -> Font """
        ...

    @staticmethod
    def FromLogFont(lf:object, hdc:IntPtr = ...) -> Font:
        """
        FromLogFont(lf: object, hdc: IntPtr) -> Font
        FromLogFont(lf: object) -> Font
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Font) -> int """
        ...

    def GetHeight(self, *__args:Graphics) -> Single:
        """
        GetHeight(self: Font, graphics: Graphics) -> Single
        GetHeight(self: Font) -> Single
        GetHeight(self: Font, dpi: Single) -> Single
        """
        ...

    def ToHfont(self) -> IntPtr:
        """ ToHfont(self: Font) -> IntPtr """
        ...

    def ToLogFont(self, logFont:object, graphics:Graphics = ...): # -> 
        """ ToLogFont(self: Font, logFont: object)ToLogFont(self: Font, logFont: object, graphics: Graphics) """
        ...

    def ToString(self) -> str:
        """ ToString(self: Font) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, prototype: Font, newStyle: FontStyle)
        __new__(cls: type, family: FontFamily, emSize: Single, style: FontStyle, unit: GraphicsUnit)
        __new__(cls: type, family: FontFamily, emSize: Single, style: FontStyle, unit: GraphicsUnit, gdiCharSet: Byte)
        __new__(cls: type, family: FontFamily, emSize: Single, style: FontStyle, unit: GraphicsUnit, gdiCharSet: Byte, gdiVerticalFont: bool)
        __new__(cls: type, familyName: str, emSize: Single, style: FontStyle, unit: GraphicsUnit, gdiCharSet: Byte)
        __new__(cls: type, familyName: str, emSize: Single, style: FontStyle, unit: GraphicsUnit, gdiCharSet: Byte, gdiVerticalFont: bool)
        __new__(cls: type, family: FontFamily, emSize: Single, style: FontStyle)
        __new__(cls: type, family: FontFamily, emSize: Single, unit: GraphicsUnit)
        __new__(cls: type, family: FontFamily, emSize: Single)
        __new__(cls: type, familyName: str, emSize: Single, style: FontStyle, unit: GraphicsUnit)
        __new__(cls: type, familyName: str, emSize: Single, style: FontStyle)
        __new__(cls: type, familyName: str, emSize: Single, unit: GraphicsUnit)
        __new__(cls: type, familyName: str, emSize: Single)
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class FontConverter(TypeConverter): # skipped bases: <type 'object'>
    """ FontConverter() """
    def FontNameConverter(self, *args): #cannot find CLR method
        """ FontNameConverter() """
        ...

    def FontUnitConverter(self, *args): #cannot find CLR method
        """ FontUnitConverter() """
        ...



class FontFamily(IDisposable, MarshalByRefObject): # skipped bases: <type 'object'>
    """
    FontFamily(name: str)
    FontFamily(name: str, fontCollection: FontCollection)
    FontFamily(genericFamily: GenericFontFamilies)
    """
    @property
    def Families(self) -> Array:
        """ Get: Families() -> Array[FontFamily] """
        ...

    @property
    def GenericMonospace(self) -> FontFamily:
        """ Get: GenericMonospace() -> FontFamily """
        ...

    @property
    def GenericSansSerif(self) -> FontFamily:
        """ Get: GenericSansSerif() -> FontFamily """
        ...

    @property
    def GenericSerif(self) -> FontFamily:
        """ Get: GenericSerif() -> FontFamily """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: FontFamily) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: FontFamily, obj: object) -> bool """
        ...

    def GetCellAscent(self, style:FontStyle) -> int:
        """ GetCellAscent(self: FontFamily, style: FontStyle) -> int """
        ...

    def GetCellDescent(self, style:FontStyle) -> int:
        """ GetCellDescent(self: FontFamily, style: FontStyle) -> int """
        ...

    def GetEmHeight(self, style:FontStyle) -> int:
        """ GetEmHeight(self: FontFamily, style: FontStyle) -> int """
        ...

    @staticmethod
    def GetFamilies(graphics:Graphics) -> Array:
        """ GetFamilies(graphics: Graphics) -> Array[FontFamily] """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: FontFamily) -> int """
        ...

    def GetLineSpacing(self, style:FontStyle) -> int:
        """ GetLineSpacing(self: FontFamily, style: FontStyle) -> int """
        ...

    def GetName(self, language:int) -> str:
        """ GetName(self: FontFamily, language: int) -> str """
        ...

    def IsStyleAvailable(self, style:FontStyle) -> bool:
        """ IsStyleAvailable(self: FontFamily, style: FontStyle) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: FontFamily) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, fontCollection: FontCollection)
        __new__(cls: type, genericFamily: GenericFontFamilies)
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __str__(self, *args): #cannot find CLR method
        ...



class FontStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) FontStyle, values: Bold (1), Italic (2), Regular (0), Strikeout (8), Underline (4) """
    Bold: FontStyle = ...
    Italic: FontStyle = ...
    Regular: FontStyle = ...
    Strikeout: FontStyle = ...
    Underline: FontStyle = ...
    value__ = ...


class Graphics(MarshalByRefObject, IDeviceContext): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def Clip(self) -> Region:
        """
        Get: Clip(self: Graphics) -> Region
        Set: Clip(self: Graphics) = value
        """
        ...

    @property
    def ClipBounds(self) -> RectangleF:
        """ Get: ClipBounds(self: Graphics) -> RectangleF """
        ...

    @property
    def CompositingMode(self) -> CompositingMode:
        """
        Get: CompositingMode(self: Graphics) -> CompositingMode
        Set: CompositingMode(self: Graphics) = value
        """
        ...

    @property
    def CompositingQuality(self) -> CompositingQuality:
        """
        Get: CompositingQuality(self: Graphics) -> CompositingQuality
        Set: CompositingQuality(self: Graphics) = value
        """
        ...

    @property
    def DpiX(self) -> Single:
        """ Get: DpiX(self: Graphics) -> Single """
        ...

    @property
    def DpiY(self) -> Single:
        """ Get: DpiY(self: Graphics) -> Single """
        ...

    @property
    def InterpolationMode(self) -> InterpolationMode:
        """
        Get: InterpolationMode(self: Graphics) -> InterpolationMode
        Set: InterpolationMode(self: Graphics) = value
        """
        ...

    @property
    def IsClipEmpty(self) -> bool:
        """ Get: IsClipEmpty(self: Graphics) -> bool """
        ...

    @property
    def IsVisibleClipEmpty(self) -> bool:
        """ Get: IsVisibleClipEmpty(self: Graphics) -> bool """
        ...

    @property
    def PageScale(self) -> Single:
        """
        Get: PageScale(self: Graphics) -> Single
        Set: PageScale(self: Graphics) = value
        """
        ...

    @property
    def PageUnit(self) -> GraphicsUnit:
        """
        Get: PageUnit(self: Graphics) -> GraphicsUnit
        Set: PageUnit(self: Graphics) = value
        """
        ...

    @property
    def PixelOffsetMode(self) -> PixelOffsetMode:
        """
        Get: PixelOffsetMode(self: Graphics) -> PixelOffsetMode
        Set: PixelOffsetMode(self: Graphics) = value
        """
        ...

    @property
    def RenderingOrigin(self) -> Point:
        """
        Get: RenderingOrigin(self: Graphics) -> Point
        Set: RenderingOrigin(self: Graphics) = value
        """
        ...

    @property
    def SmoothingMode(self) -> SmoothingMode:
        """
        Get: SmoothingMode(self: Graphics) -> SmoothingMode
        Set: SmoothingMode(self: Graphics) = value
        """
        ...

    @property
    def TextContrast(self) -> int:
        """
        Get: TextContrast(self: Graphics) -> int
        Set: TextContrast(self: Graphics) = value
        """
        ...

    @property
    def TextRenderingHint(self) -> TextRenderingHint:
        """
        Get: TextRenderingHint(self: Graphics) -> TextRenderingHint
        Set: TextRenderingHint(self: Graphics) = value
        """
        ...

    @property
    def Transform(self) -> Matrix:
        """
        Get: Transform(self: Graphics) -> Matrix
        Set: Transform(self: Graphics) = value
        """
        ...

    @property
    def VisibleClipBounds(self) -> RectangleF:
        """ Get: VisibleClipBounds(self: Graphics) -> RectangleF """
        ...


    def AddMetafileComment(self, data:Array): # -> 
        """ AddMetafileComment(self: Graphics, data: Array[Byte]) """
        ...

    def BeginContainer(self, dstrect:RectangleF = ..., srcrect:RectangleF = ..., unit:GraphicsUnit = ...) -> GraphicsContainer:
        """
        BeginContainer(self: Graphics) -> GraphicsContainer
        BeginContainer(self: Graphics, dstrect: RectangleF, srcrect: RectangleF, unit: GraphicsUnit) -> GraphicsContainer
        BeginContainer(self: Graphics, dstrect: Rectangle, srcrect: Rectangle, unit: GraphicsUnit) -> GraphicsContainer
        """
        ...

    def Clear(self, color:Color): # -> 
        """ Clear(self: Graphics, color: Color) """
        ...

    def CopyFromScreen(self, *__args): # -> 
        """ CopyFromScreen(self: Graphics, upperLeftSource: Point, upperLeftDestination: Point, blockRegionSize: Size)CopyFromScreen(self: Graphics, sourceX: int, sourceY: int, destinationX: int, destinationY: int, blockRegionSize: Size)CopyFromScreen(self: Graphics, upperLeftSource: Point, upperLeftDestination: Point, blockRegionSize: Size, copyPixelOperation: CopyPixelOperation)CopyFromScreen(self: Graphics, sourceX: int, sourceY: int, destinationX: int, destinationY: int, blockRegionSize: Size, copyPixelOperation: CopyPixelOperation) """
        ...

    def Dispose(self): # -> 
        """ Dispose(self: Graphics) """
        ...

    def DrawArc(self, pen, *__args): # -> 
        """ DrawArc(self: Graphics, pen: Pen, x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single)DrawArc(self: Graphics, pen: Pen, rect: RectangleF, startAngle: Single, sweepAngle: Single)DrawArc(self: Graphics, pen: Pen, x: int, y: int, width: int, height: int, startAngle: int, sweepAngle: int)DrawArc(self: Graphics, pen: Pen, rect: Rectangle, startAngle: Single, sweepAngle: Single) """
        ...

    def DrawBezier(self, pen, *__args): # -> 
        """ DrawBezier(self: Graphics, pen: Pen, x1: Single, y1: Single, x2: Single, y2: Single, x3: Single, y3: Single, x4: Single, y4: Single)DrawBezier(self: Graphics, pen: Pen, pt1: PointF, pt2: PointF, pt3: PointF, pt4: PointF)DrawBezier(self: Graphics, pen: Pen, pt1: Point, pt2: Point, pt3: Point, pt4: Point) """
        ...

    def DrawBeziers(self, pen:Pen, points:Array): # -> 
        """ DrawBeziers(self: Graphics, pen: Pen, points: Array[PointF])DrawBeziers(self: Graphics, pen: Pen, points: Array[Point]) """
        ...

    def DrawClosedCurve(self, pen:Pen, points:Array, tension:Single = ..., fillmode:FillMode = ...): # -> 
        """ DrawClosedCurve(self: Graphics, pen: Pen, points: Array[PointF])DrawClosedCurve(self: Graphics, pen: Pen, points: Array[PointF], tension: Single, fillmode: FillMode)DrawClosedCurve(self: Graphics, pen: Pen, points: Array[Point])DrawClosedCurve(self: Graphics, pen: Pen, points: Array[Point], tension: Single, fillmode: FillMode) """
        ...

    def DrawCurve(self, pen:Pen, points:Array, *__args:Single): # -> 
        """ DrawCurve(self: Graphics, pen: Pen, points: Array[PointF])DrawCurve(self: Graphics, pen: Pen, points: Array[PointF], tension: Single)DrawCurve(self: Graphics, pen: Pen, points: Array[PointF], offset: int, numberOfSegments: int)DrawCurve(self: Graphics, pen: Pen, points: Array[PointF], offset: int, numberOfSegments: int, tension: Single)DrawCurve(self: Graphics, pen: Pen, points: Array[Point])DrawCurve(self: Graphics, pen: Pen, points: Array[Point], tension: Single)DrawCurve(self: Graphics, pen: Pen, points: Array[Point], offset: int, numberOfSegments: int, tension: Single) """
        ...

    def DrawEllipse(self, pen:Pen, *__args:RectangleF): # -> 
        """ DrawEllipse(self: Graphics, pen: Pen, rect: RectangleF)DrawEllipse(self: Graphics, pen: Pen, x: Single, y: Single, width: Single, height: Single)DrawEllipse(self: Graphics, pen: Pen, rect: Rectangle)DrawEllipse(self: Graphics, pen: Pen, x: int, y: int, width: int, height: int) """
        ...

    def DrawIcon(self, icon:Icon, *__args:Rectangle): # -> 
        """ DrawIcon(self: Graphics, icon: Icon, x: int, y: int)DrawIcon(self: Graphics, icon: Icon, targetRect: Rectangle) """
        ...

    def DrawIconUnstretched(self, icon:Icon, targetRect:Rectangle): # -> 
        """ DrawIconUnstretched(self: Graphics, icon: Icon, targetRect: Rectangle) """
        ...

    def DrawImage(self, image:Image, *__args:Array): # -> 
        """ DrawImage(self: Graphics, image: Image, x: int, y: int)DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcX: Single, srcY: Single, srcWidth: Single, srcHeight: Single, srcUnit: GraphicsUnit, imageAttrs: ImageAttributes, callback: DrawImageAbort, callbackData: IntPtr)DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcX: Single, srcY: Single, srcWidth: Single, srcHeight: Single, srcUnit: GraphicsUnit, imageAttrs: ImageAttributes, callback: DrawImageAbort)DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcX: Single, srcY: Single, srcWidth: Single, srcHeight: Single, srcUnit: GraphicsUnit, imageAttrs: ImageAttributes)DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcX: Single, srcY: Single, srcWidth: Single, srcHeight: Single, srcUnit: GraphicsUnit)DrawImage(self: Graphics, image: Image, destPoints: Array[Point], srcRect: Rectangle, srcUnit: GraphicsUnit, imageAttr: ImageAttributes, callback: DrawImageAbort, callbackData: int)DrawImage(self: Graphics, image: Image, destPoints: Array[Point], srcRect: Rectangle, srcUnit: GraphicsUnit, imageAttr: ImageAttributes, callback: DrawImageAbort)DrawImage(self: Graphics, image: Image, destPoints: Array[Point], srcRect: Rectangle, srcUnit: GraphicsUnit, imageAttr: ImageAttributes)DrawImage(self: Graphics, image: Image, destPoints: Array[Point], srcRect: Rectangle, srcUnit: GraphicsUnit)DrawImage(self: Graphics, image: Image, destPoints: Array[PointF], srcRect: RectangleF, srcUnit: GraphicsUnit, imageAttr: ImageAttributes, callback: DrawImageAbort, callbackData: int)DrawImage(self: Graphics, image: Image, destPoints: Array[PointF], srcRect: RectangleF, srcUnit: GraphicsUnit, imageAttr: ImageAttributes, callback: DrawImageAbort)DrawImage(self: Graphics, image: Image, destPoints: Array[PointF], srcRect: RectangleF, srcUnit: GraphicsUnit, imageAttr: ImageAttributes)DrawImage(self: Graphics, image: Image, destPoints: Array[PointF], srcRect: RectangleF, srcUnit: GraphicsUnit)DrawImage(self: Graphics, image: Image, destRect: RectangleF, srcRect: RectangleF, srcUnit: GraphicsUnit)DrawImage(self: Graphics, image: Image, x: int, y: int, srcRect: Rectangle, srcUnit: GraphicsUnit)DrawImage(self: Graphics, image: Image, x: Single, y: Single, srcRect: RectangleF, srcUnit: GraphicsUnit)DrawImage(self: Graphics, image: Image, destPoints: Array[Point])DrawImage(self: Graphics, image: Image, destPoints: Array[PointF])DrawImage(self: Graphics, image: Image, point: Point)DrawImage(self: Graphics, image: Image, x: Single, y: Single, width: Single, height: Single)DrawImage(self: Graphics, image: Image, rect: RectangleF)DrawImage(self: Graphics, image: Image, x: Single, y: Single)DrawImage(self: Graphics, image: Image, point: PointF)DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcX: int, srcY: int, srcWidth: int, srcHeight: int, srcUnit: GraphicsUnit, imageAttrs: ImageAttributes, callback: DrawImageAbort, callbackData: IntPtr)DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcX: int, srcY: int, srcWidth: int, srcHeight: int, srcUnit: GraphicsUnit, imageAttr: ImageAttributes)DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcRect: Rectangle, srcUnit: GraphicsUnit)DrawImage(self: Graphics, image: Image, x: int, y: int, width: int, height: int)DrawImage(self: Graphics, image: Image, rect: Rectangle)DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcX: int, srcY: int, srcWidth: int, srcHeight: int, srcUnit: GraphicsUnit)DrawImage(self: Graphics, image: Image, destRect: Rectangle, srcX: int, srcY: int, srcWidth: int, srcHeight: int, srcUnit: GraphicsUnit, imageAttr: ImageAttributes, callback: DrawImageAbort) """
        ...

    def DrawImageAbort(self, *args): #cannot find CLR method
        """ DrawImageAbort(object: object, method: IntPtr) """
        ...

    def DrawImageUnscaled(self, image:Image, *__args:Point): # -> 
        """ DrawImageUnscaled(self: Graphics, image: Image, point: Point)DrawImageUnscaled(self: Graphics, image: Image, x: int, y: int)DrawImageUnscaled(self: Graphics, image: Image, rect: Rectangle)DrawImageUnscaled(self: Graphics, image: Image, x: int, y: int, width: int, height: int) """
        ...

    def DrawImageUnscaledAndClipped(self, image:Image, rect:Rectangle): # -> 
        """ DrawImageUnscaledAndClipped(self: Graphics, image: Image, rect: Rectangle) """
        ...

    def DrawLine(self, pen, *__args): # -> 
        """ DrawLine(self: Graphics, pen: Pen, x1: int, y1: int, x2: int, y2: int)DrawLine(self: Graphics, pen: Pen, x1: Single, y1: Single, x2: Single, y2: Single)DrawLine(self: Graphics, pen: Pen, pt1: PointF, pt2: PointF)DrawLine(self: Graphics, pen: Pen, pt1: Point, pt2: Point) """
        ...

    def DrawLines(self, pen:Pen, points:Array): # -> 
        """ DrawLines(self: Graphics, pen: Pen, points: Array[PointF])DrawLines(self: Graphics, pen: Pen, points: Array[Point]) """
        ...

    def DrawPath(self, pen:Pen, path:GraphicsPath): # -> 
        """ DrawPath(self: Graphics, pen: Pen, path: GraphicsPath) """
        ...

    def DrawPie(self, pen, *__args): # -> 
        """ DrawPie(self: Graphics, pen: Pen, rect: RectangleF, startAngle: Single, sweepAngle: Single)DrawPie(self: Graphics, pen: Pen, x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single)DrawPie(self: Graphics, pen: Pen, rect: Rectangle, startAngle: Single, sweepAngle: Single)DrawPie(self: Graphics, pen: Pen, x: int, y: int, width: int, height: int, startAngle: int, sweepAngle: int) """
        ...

    def DrawPolygon(self, pen:Pen, points:Array): # -> 
        """ DrawPolygon(self: Graphics, pen: Pen, points: Array[PointF])DrawPolygon(self: Graphics, pen: Pen, points: Array[Point]) """
        ...

    def DrawRectangle(self, pen:Pen, *__args:Rectangle): # -> 
        """ DrawRectangle(self: Graphics, pen: Pen, rect: Rectangle)DrawRectangle(self: Graphics, pen: Pen, x: Single, y: Single, width: Single, height: Single)DrawRectangle(self: Graphics, pen: Pen, x: int, y: int, width: int, height: int) """
        ...

    def DrawRectangles(self, pen:Pen, rects:Array): # -> 
        """ DrawRectangles(self: Graphics, pen: Pen, rects: Array[RectangleF])DrawRectangles(self: Graphics, pen: Pen, rects: Array[Rectangle]) """
        ...

    def DrawString(self, s:str, font:Font, brush:Brush, *__args:RectangleF): # -> 
        """ DrawString(self: Graphics, s: str, font: Font, brush: Brush, x: Single, y: Single)DrawString(self: Graphics, s: str, font: Font, brush: Brush, layoutRectangle: RectangleF)DrawString(self: Graphics, s: str, font: Font, brush: Brush, layoutRectangle: RectangleF, format: StringFormat)DrawString(self: Graphics, s: str, font: Font, brush: Brush, point: PointF)DrawString(self: Graphics, s: str, font: Font, brush: Brush, x: Single, y: Single, format: StringFormat)DrawString(self: Graphics, s: str, font: Font, brush: Brush, point: PointF, format: StringFormat) """
        ...

    def EndContainer(self, container:GraphicsContainer): # -> 
        """ EndContainer(self: Graphics, container: GraphicsContainer) """
        ...

    def EnumerateMetafile(self, metafile, *__args): # -> 
        """ EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: PointF, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: PointF, srcRect: RectangleF, unit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: Point, srcRect: Rectangle, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: Point, srcRect: Rectangle, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: Point, srcRect: Rectangle, unit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: RectangleF, srcRect: RectangleF, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: RectangleF, srcRect: RectangleF, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: PointF, srcRect: RectangleF, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: RectangleF, srcRect: RectangleF, unit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: Rectangle, srcRect: Rectangle, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: Rectangle, srcRect: Rectangle, unit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[PointF], srcRect: RectangleF, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[PointF], srcRect: RectangleF, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[PointF], srcRect: RectangleF, unit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[Point], srcRect: Rectangle, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: Rectangle, srcRect: Rectangle, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: PointF, srcRect: RectangleF, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[Point], callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[Point], callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: PointF, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: PointF, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: Point, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: Point, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoint: Point, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: RectangleF, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: RectangleF, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: RectangleF, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: Rectangle, callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: Rectangle, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destRect: Rectangle, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[PointF], callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[PointF], callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[PointF], callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[Point], callback: EnumerateMetafileProc)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[Point], srcRect: Rectangle, srcUnit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr)EnumerateMetafile(self: Graphics, metafile: Metafile, destPoints: Array[Point], srcRect: Rectangle, unit: GraphicsUnit, callback: EnumerateMetafileProc, callbackData: IntPtr, imageAttr: ImageAttributes) """
        ...

    def EnumerateMetafileProc(self, *args): #cannot find CLR method
        """ EnumerateMetafileProc(object: object, method: IntPtr) """
        ...

    def ExcludeClip(self, *__args:Region): # -> 
        """ ExcludeClip(self: Graphics, region: Region)ExcludeClip(self: Graphics, rect: Rectangle) """
        ...

    def FillClosedCurve(self, brush:Brush, points:Array, fillmode:FillMode = ..., tension:Single = ...): # -> 
        """ FillClosedCurve(self: Graphics, brush: Brush, points: Array[PointF])FillClosedCurve(self: Graphics, brush: Brush, points: Array[PointF], fillmode: FillMode)FillClosedCurve(self: Graphics, brush: Brush, points: Array[PointF], fillmode: FillMode, tension: Single)FillClosedCurve(self: Graphics, brush: Brush, points: Array[Point])FillClosedCurve(self: Graphics, brush: Brush, points: Array[Point], fillmode: FillMode)FillClosedCurve(self: Graphics, brush: Brush, points: Array[Point], fillmode: FillMode, tension: Single) """
        ...

    def FillEllipse(self, brush:Brush, *__args:RectangleF): # -> 
        """ FillEllipse(self: Graphics, brush: Brush, x: Single, y: Single, width: Single, height: Single)FillEllipse(self: Graphics, brush: Brush, rect: RectangleF)FillEllipse(self: Graphics, brush: Brush, rect: Rectangle)FillEllipse(self: Graphics, brush: Brush, x: int, y: int, width: int, height: int) """
        ...

    def FillPath(self, brush:Brush, path:GraphicsPath): # -> 
        """ FillPath(self: Graphics, brush: Brush, path: GraphicsPath) """
        ...

    def FillPie(self, brush, *__args): # -> 
        """ FillPie(self: Graphics, brush: Brush, rect: Rectangle, startAngle: Single, sweepAngle: Single)FillPie(self: Graphics, brush: Brush, x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single)FillPie(self: Graphics, brush: Brush, x: int, y: int, width: int, height: int, startAngle: int, sweepAngle: int) """
        ...

    def FillPolygon(self, brush:Brush, points:Array, fillMode:FillMode = ...): # -> 
        """ FillPolygon(self: Graphics, brush: Brush, points: Array[Point])FillPolygon(self: Graphics, brush: Brush, points: Array[PointF])FillPolygon(self: Graphics, brush: Brush, points: Array[PointF], fillMode: FillMode)FillPolygon(self: Graphics, brush: Brush, points: Array[Point], fillMode: FillMode) """
        ...

    def FillRectangle(self, brush:Brush, *__args:Rectangle): # -> 
        """ FillRectangle(self: Graphics, brush: Brush, x: Single, y: Single, width: Single, height: Single)FillRectangle(self: Graphics, brush: Brush, rect: Rectangle)FillRectangle(self: Graphics, brush: Brush, x: int, y: int, width: int, height: int)FillRectangle(self: Graphics, brush: Brush, rect: RectangleF) """
        ...

    def FillRectangles(self, brush:Brush, rects:Array): # -> 
        """ FillRectangles(self: Graphics, brush: Brush, rects: Array[Rectangle])FillRectangles(self: Graphics, brush: Brush, rects: Array[RectangleF]) """
        ...

    def FillRegion(self, brush:Brush, region:Region): # -> 
        """ FillRegion(self: Graphics, brush: Brush, region: Region) """
        ...

    def Flush(self, intention:FlushIntention = ...): # -> 
        """ Flush(self: Graphics)Flush(self: Graphics, intention: FlushIntention) """
        ...

    @staticmethod
    def FromHdc(hdc:IntPtr, hdevice:IntPtr = ...) -> Graphics:
        """
        FromHdc(hdc: IntPtr) -> Graphics
        FromHdc(hdc: IntPtr, hdevice: IntPtr) -> Graphics
        """
        ...

    @staticmethod
    def FromHdcInternal(hdc:IntPtr) -> Graphics:
        """ FromHdcInternal(hdc: IntPtr) -> Graphics """
        ...

    @staticmethod
    def FromHwnd(hwnd:IntPtr) -> Graphics:
        """ FromHwnd(hwnd: IntPtr) -> Graphics """
        ...

    @staticmethod
    def FromHwndInternal(hwnd:IntPtr) -> Graphics:
        """ FromHwndInternal(hwnd: IntPtr) -> Graphics """
        ...

    @staticmethod
    def FromImage(image:Image) -> Graphics:
        """ FromImage(image: Image) -> Graphics """
        ...

    def GetContextInfo(self) -> object:
        """ GetContextInfo(self: Graphics) -> object """
        ...

    @staticmethod
    def GetHalftonePalette() -> IntPtr:
        """ GetHalftonePalette() -> IntPtr """
        ...

    def GetNearestColor(self, color:Color) -> Color:
        """ GetNearestColor(self: Graphics, color: Color) -> Color """
        ...

    def IntersectClip(self, *__args:Rectangle): # -> 
        """ IntersectClip(self: Graphics, rect: Rectangle)IntersectClip(self: Graphics, rect: RectangleF)IntersectClip(self: Graphics, region: Region) """
        ...

    def IsVisible(self, *__args:Rectangle) -> bool:
        """
        IsVisible(self: Graphics, rect: Rectangle) -> bool
        IsVisible(self: Graphics, x: int, y: int) -> bool
        IsVisible(self: Graphics, point: Point) -> bool
        IsVisible(self: Graphics, x: Single, y: Single) -> bool
        IsVisible(self: Graphics, point: PointF) -> bool
        IsVisible(self: Graphics, x: int, y: int, width: int, height: int) -> bool
        IsVisible(self: Graphics, x: Single, y: Single, width: Single, height: Single) -> bool
        IsVisible(self: Graphics, rect: RectangleF) -> bool
        """
        ...

    def MeasureCharacterRanges(self, text:str, font:Font, layoutRect:RectangleF, stringFormat:StringFormat) -> Array:
        """ MeasureCharacterRanges(self: Graphics, text: str, font: Font, layoutRect: RectangleF, stringFormat: StringFormat) -> Array[Region] """
        ...

    def MeasureString(self, text:str, font:Font, *__args:SizeF) -> SizeF:
        """
        MeasureString(self: Graphics, text: str, font: Font, layoutArea: SizeF, stringFormat: StringFormat) -> SizeF
        MeasureString(self: Graphics, text: str, font: Font) -> SizeF
        MeasureString(self: Graphics, text: str, font: Font, width: int, format: StringFormat) -> SizeF
        MeasureString(self: Graphics, text: str, font: Font, layoutArea: SizeF, stringFormat: StringFormat) -> (SizeF, int, int)
        MeasureString(self: Graphics, text: str, font: Font, origin: PointF, stringFormat: StringFormat) -> SizeF
        MeasureString(self: Graphics, text: str, font: Font, layoutArea: SizeF) -> SizeF
        MeasureString(self: Graphics, text: str, font: Font, width: int) -> SizeF
        """
        ...

    def MultiplyTransform(self, matrix:Matrix, order:MatrixOrder = ...): # -> 
        """ MultiplyTransform(self: Graphics, matrix: Matrix)MultiplyTransform(self: Graphics, matrix: Matrix, order: MatrixOrder) """
        ...

    def ReleaseHdcInternal(self, hdc:IntPtr): # -> 
        """ ReleaseHdcInternal(self: Graphics, hdc: IntPtr) """
        ...

    def ResetClip(self): # -> 
        """ ResetClip(self: Graphics) """
        ...

    def ResetTransform(self): # -> 
        """ ResetTransform(self: Graphics) """
        ...

    def Restore(self, gstate:GraphicsState): # -> 
        """ Restore(self: Graphics, gstate: GraphicsState) """
        ...

    def RotateTransform(self, angle:Single, order:MatrixOrder = ...): # -> 
        """ RotateTransform(self: Graphics, angle: Single)RotateTransform(self: Graphics, angle: Single, order: MatrixOrder) """
        ...

    def Save(self) -> GraphicsState:
        """ Save(self: Graphics) -> GraphicsState """
        ...

    def ScaleTransform(self, sx:Single, sy:Single, order:MatrixOrder = ...): # -> 
        """ ScaleTransform(self: Graphics, sx: Single, sy: Single)ScaleTransform(self: Graphics, sx: Single, sy: Single, order: MatrixOrder) """
        ...

    def SetClip(self, *__args:Rectangle): # -> 
        """ SetClip(self: Graphics, rect: Rectangle)SetClip(self: Graphics, region: Region, combineMode: CombineMode)SetClip(self: Graphics, g: Graphics)SetClip(self: Graphics, g: Graphics, combineMode: CombineMode)SetClip(self: Graphics, rect: Rectangle, combineMode: CombineMode)SetClip(self: Graphics, rect: RectangleF)SetClip(self: Graphics, rect: RectangleF, combineMode: CombineMode)SetClip(self: Graphics, path: GraphicsPath)SetClip(self: Graphics, path: GraphicsPath, combineMode: CombineMode) """
        ...

    def TransformPoints(self, destSpace:CoordinateSpace, srcSpace:CoordinateSpace, pts:Array): # -> 
        """ TransformPoints(self: Graphics, destSpace: CoordinateSpace, srcSpace: CoordinateSpace, pts: Array[PointF])TransformPoints(self: Graphics, destSpace: CoordinateSpace, srcSpace: CoordinateSpace, pts: Array[Point]) """
        ...

    def TranslateClip(self, dx:int, dy:int): # -> 
        """ TranslateClip(self: Graphics, dx: int, dy: int)TranslateClip(self: Graphics, dx: Single, dy: Single) """
        ...

    def TranslateTransform(self, dx:Single, dy:Single, order:MatrixOrder = ...): # -> 
        """ TranslateTransform(self: Graphics, dx: Single, dy: Single)TranslateTransform(self: Graphics, dx: Single, dy: Single, order: MatrixOrder) """
        ...



class GraphicsUnit(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GraphicsUnit, values: Display (1), Document (5), Inch (4), Millimeter (6), Pixel (2), Point (3), World (0) """
    Display: GraphicsUnit = ...
    Document: GraphicsUnit = ...
    Inch: GraphicsUnit = ...
    Millimeter: GraphicsUnit = ...
    Pixel: GraphicsUnit = ...
    Point: GraphicsUnit = ...
    value__ = ...
    World: GraphicsUnit = ...


class Icon(IDisposable, ICloneable, MarshalByRefObject, ISerializable): # skipped bases: <type 'object'>
    """
    Icon(fileName: str)
    Icon(fileName: str, size: Size)
    Icon(fileName: str, width: int, height: int)
    Icon(original: Icon, size: Size)
    Icon(original: Icon, width: int, height: int)
    Icon(type: Type, resource: str)
    Icon(stream: Stream)
    Icon(stream: Stream, size: Size)
    Icon(stream: Stream, width: int, height: int)
    """
    @property
    def Handle(self) -> IntPtr:
        """ Get: Handle(self: Icon) -> IntPtr """
        ...

    @property
    def Height(self) -> int:
        """ Get: Height(self: Icon) -> int """
        ...

    @property
    def Size(self) -> Size:
        """ Get: Size(self: Icon) -> Size """
        ...

    @property
    def Width(self) -> int:
        """ Get: Width(self: Icon) -> int """
        ...


    @staticmethod
    def ExtractAssociatedIcon(filePath:str) -> Icon:
        """ ExtractAssociatedIcon(filePath: str) -> Icon """
        ...

    @staticmethod
    def FromHandle(handle:IntPtr) -> Icon:
        """ FromHandle(handle: IntPtr) -> Icon """
        ...

    def Save(self, outputStream:Stream): # -> 
        """ Save(self: Icon, outputStream: Stream) """
        ...

    def ToBitmap(self) -> Bitmap:
        """ ToBitmap(self: Icon) -> Bitmap """
        ...

    def ToString(self) -> str:
        """ ToString(self: Icon) -> str """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, fileName: str)
        __new__(cls: type, fileName: str, size: Size)
        __new__(cls: type, fileName: str, width: int, height: int)
        __new__(cls: type, original: Icon, size: Size)
        __new__(cls: type, original: Icon, width: int, height: int)
        __new__(cls: type, type: Type, resource: str)
        __new__(cls: type, stream: Stream)
        __new__(cls: type, stream: Stream, size: Size)
        __new__(cls: type, stream: Stream, width: int, height: int)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class IconConverter(ExpandableObjectConverter): # skipped bases: <type 'object'>
    """ IconConverter() """
    def CanConvertFrom(self, *__args) -> bool:
        """ CanConvertFrom(self: IconConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool """
        ...

    def CanConvertTo(self, *__args) -> bool:
        """ CanConvertTo(self: IconConverter, context: ITypeDescriptorContext, destinationType: Type) -> bool """
        ...

    def ConvertFrom(self, *__args) -> object:
        """ ConvertFrom(self: IconConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object """
        ...

    def ConvertTo(self, *__args) -> object:
        """ ConvertTo(self: IconConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object """
        ...


class IDeviceContext(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def GetHdc(self) -> IntPtr:
        """ GetHdc(self: IDeviceContext) -> IntPtr """
        ...

    def ReleaseHdc(self): # -> 
        """ ReleaseHdc(self: IDeviceContext) """
        ...


class ImageAnimator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Animate(image:Image, onFrameChangedHandler:EventHandler): # -> 
        """ Animate(image: Image, onFrameChangedHandler: EventHandler) """
        ...

    @staticmethod
    def CanAnimate(image:Image) -> bool:
        """ CanAnimate(image: Image) -> bool """
        ...

    @staticmethod
    def StopAnimate(image:Image, onFrameChangedHandler:EventHandler): # -> 
        """ StopAnimate(image: Image, onFrameChangedHandler: EventHandler) """
        ...

    @staticmethod
    def UpdateFrames(image:Image = ...): # -> 
        """ UpdateFrames(image: Image)UpdateFrames() """
        ...


class ImageConverter(TypeConverter): # skipped bases: <type 'object'>
    """ ImageConverter() """
    pass

class ImageFormatConverter(TypeConverter): # skipped bases: <type 'object'>
    """ ImageFormatConverter() """
    pass

class KnownColor(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum KnownColor, values: ActiveBorder (1), ActiveCaption (2), ActiveCaptionText (3), AliceBlue (28), AntiqueWhite (29), AppWorkspace (4), Aqua (30), Aquamarine (31), Azure (32), Beige (33), Bisque (34), Black (35), BlanchedAlmond (36), Blue (37), BlueViolet (38), Brown (39), BurlyWood (40), ButtonFace (168), ButtonHighlight (169), ButtonShadow (170), CadetBlue (41), Chartreuse (42), Chocolate (43), Control (5), ControlDark (6), ControlDarkDark (7), ControlLight (8), ControlLightLight (9), ControlText (10), Coral (44), CornflowerBlue (45), Cornsilk (46), Crimson (47), Cyan (48), DarkBlue (49), DarkCyan (50), DarkGoldenrod (51), DarkGray (52), DarkGreen (53), DarkKhaki (54), DarkMagenta (55), DarkOliveGreen (56), DarkOrange (57), DarkOrchid (58), DarkRed (59), DarkSalmon (60), DarkSeaGreen (61), DarkSlateBlue (62), DarkSlateGray (63), DarkTurquoise (64), DarkViolet (65), DeepPink (66), DeepSkyBlue (67), Desktop (11), DimGray (68), DodgerBlue (69), Firebrick (70), FloralWhite (71), ForestGreen (72), Fuchsia (73), Gainsboro (74), GhostWhite (75), Gold (76), Goldenrod (77), GradientActiveCaption (171), GradientInactiveCaption (172), Gray (78), GrayText (12), Green (79), GreenYellow (80), Highlight (13), HighlightText (14), Honeydew (81), HotPink (82), HotTrack (15), InactiveBorder (16), InactiveCaption (17), InactiveCaptionText (18), IndianRed (83), Indigo (84), Info (19), InfoText (20), Ivory (85), Khaki (86), Lavender (87), LavenderBlush (88), LawnGreen (89), LemonChiffon (90), LightBlue (91), LightCoral (92), LightCyan (93), LightGoldenrodYellow (94), LightGray (95), LightGreen (96), LightPink (97), LightSalmon (98), LightSeaGreen (99), LightSkyBlue (100), LightSlateGray (101), LightSteelBlue (102), LightYellow (103), Lime (104), LimeGreen (105), Linen (106), Magenta (107), Maroon (108), MediumAquamarine (109), MediumBlue (110), MediumOrchid (111), MediumPurple (112), MediumSeaGreen (113), MediumSlateBlue (114), MediumSpringGreen (115), MediumTurquoise (116), MediumVioletRed (117), Menu (21), MenuBar (173), MenuHighlight (174), MenuText (22), MidnightBlue (118), MintCream (119), MistyRose (120), Moccasin (121), NavajoWhite (122), Navy (123), OldLace (124), Olive (125), OliveDrab (126), Orange (127), OrangeRed (128), Orchid (129), PaleGoldenrod (130), PaleGreen (131), PaleTurquoise (132), PaleVioletRed (133), PapayaWhip (134), PeachPuff (135), Peru (136), Pink (137), Plum (138), PowderBlue (139), Purple (140), Red (141), RosyBrown (142), RoyalBlue (143), SaddleBrown (144), Salmon (145), SandyBrown (146), ScrollBar (23), SeaGreen (147), SeaShell (148), Sienna (149), Silver (150), SkyBlue (151), SlateBlue (152), SlateGray (153), Snow (154), SpringGreen (155), SteelBlue (156), Tan (157), Teal (158), Thistle (159), Tomato (160), Transparent (27), Turquoise (161), Violet (162), Wheat (163), White (164), WhiteSmoke (165), Window (24), WindowFrame (25), WindowText (26), Yellow (166), YellowGreen (167) """
    ActiveBorder: KnownColor = ...
    ActiveCaption: KnownColor = ...
    ActiveCaptionText: KnownColor = ...
    AliceBlue: KnownColor = ...
    AntiqueWhite: KnownColor = ...
    AppWorkspace: KnownColor = ...
    Aqua: KnownColor = ...
    Aquamarine: KnownColor = ...
    Azure: KnownColor = ...
    Beige: KnownColor = ...
    Bisque: KnownColor = ...
    Black: KnownColor = ...
    BlanchedAlmond: KnownColor = ...
    Blue: KnownColor = ...
    BlueViolet: KnownColor = ...
    Brown: KnownColor = ...
    BurlyWood: KnownColor = ...
    ButtonFace: KnownColor = ...
    ButtonHighlight: KnownColor = ...
    ButtonShadow: KnownColor = ...
    CadetBlue: KnownColor = ...
    Chartreuse: KnownColor = ...
    Chocolate: KnownColor = ...
    Control: KnownColor = ...
    ControlDark: KnownColor = ...
    ControlDarkDark: KnownColor = ...
    ControlLight: KnownColor = ...
    ControlLightLight: KnownColor = ...
    ControlText: KnownColor = ...
    Coral: KnownColor = ...
    CornflowerBlue: KnownColor = ...
    Cornsilk: KnownColor = ...
    Crimson: KnownColor = ...
    Cyan: KnownColor = ...
    DarkBlue: KnownColor = ...
    DarkCyan: KnownColor = ...
    DarkGoldenrod: KnownColor = ...
    DarkGray: KnownColor = ...
    DarkGreen: KnownColor = ...
    DarkKhaki: KnownColor = ...
    DarkMagenta: KnownColor = ...
    DarkOliveGreen: KnownColor = ...
    DarkOrange: KnownColor = ...
    DarkOrchid: KnownColor = ...
    DarkRed: KnownColor = ...
    DarkSalmon: KnownColor = ...
    DarkSeaGreen: KnownColor = ...
    DarkSlateBlue: KnownColor = ...
    DarkSlateGray: KnownColor = ...
    DarkTurquoise: KnownColor = ...
    DarkViolet: KnownColor = ...
    DeepPink: KnownColor = ...
    DeepSkyBlue: KnownColor = ...
    Desktop: KnownColor = ...
    DimGray: KnownColor = ...
    DodgerBlue: KnownColor = ...
    Firebrick: KnownColor = ...
    FloralWhite: KnownColor = ...
    ForestGreen: KnownColor = ...
    Fuchsia: KnownColor = ...
    Gainsboro: KnownColor = ...
    GhostWhite: KnownColor = ...
    Gold: KnownColor = ...
    Goldenrod: KnownColor = ...
    GradientActiveCaption: KnownColor = ...
    GradientInactiveCaption: KnownColor = ...
    Gray: KnownColor = ...
    GrayText: KnownColor = ...
    Green: KnownColor = ...
    GreenYellow: KnownColor = ...
    Highlight: KnownColor = ...
    HighlightText: KnownColor = ...
    Honeydew: KnownColor = ...
    HotPink: KnownColor = ...
    HotTrack: KnownColor = ...
    InactiveBorder: KnownColor = ...
    InactiveCaption: KnownColor = ...
    InactiveCaptionText: KnownColor = ...
    IndianRed: KnownColor = ...
    Indigo: KnownColor = ...
    Info: KnownColor = ...
    InfoText: KnownColor = ...
    Ivory: KnownColor = ...
    Khaki: KnownColor = ...
    Lavender: KnownColor = ...
    LavenderBlush: KnownColor = ...
    LawnGreen: KnownColor = ...
    LemonChiffon: KnownColor = ...
    LightBlue: KnownColor = ...
    LightCoral: KnownColor = ...
    LightCyan: KnownColor = ...
    LightGoldenrodYellow: KnownColor = ...
    LightGray: KnownColor = ...
    LightGreen: KnownColor = ...
    LightPink: KnownColor = ...
    LightSalmon: KnownColor = ...
    LightSeaGreen: KnownColor = ...
    LightSkyBlue: KnownColor = ...
    LightSlateGray: KnownColor = ...
    LightSteelBlue: KnownColor = ...
    LightYellow: KnownColor = ...
    Lime: KnownColor = ...
    LimeGreen: KnownColor = ...
    Linen: KnownColor = ...
    Magenta: KnownColor = ...
    Maroon: KnownColor = ...
    MediumAquamarine: KnownColor = ...
    MediumBlue: KnownColor = ...
    MediumOrchid: KnownColor = ...
    MediumPurple: KnownColor = ...
    MediumSeaGreen: KnownColor = ...
    MediumSlateBlue: KnownColor = ...
    MediumSpringGreen: KnownColor = ...
    MediumTurquoise: KnownColor = ...
    MediumVioletRed: KnownColor = ...
    Menu: KnownColor = ...
    MenuBar: KnownColor = ...
    MenuHighlight: KnownColor = ...
    MenuText: KnownColor = ...
    MidnightBlue: KnownColor = ...
    MintCream: KnownColor = ...
    MistyRose: KnownColor = ...
    Moccasin: KnownColor = ...
    NavajoWhite: KnownColor = ...
    Navy: KnownColor = ...
    OldLace: KnownColor = ...
    Olive: KnownColor = ...
    OliveDrab: KnownColor = ...
    Orange: KnownColor = ...
    OrangeRed: KnownColor = ...
    Orchid: KnownColor = ...
    PaleGoldenrod: KnownColor = ...
    PaleGreen: KnownColor = ...
    PaleTurquoise: KnownColor = ...
    PaleVioletRed: KnownColor = ...
    PapayaWhip: KnownColor = ...
    PeachPuff: KnownColor = ...
    Peru: KnownColor = ...
    Pink: KnownColor = ...
    Plum: KnownColor = ...
    PowderBlue: KnownColor = ...
    Purple: KnownColor = ...
    Red: KnownColor = ...
    RosyBrown: KnownColor = ...
    RoyalBlue: KnownColor = ...
    SaddleBrown: KnownColor = ...
    Salmon: KnownColor = ...
    SandyBrown: KnownColor = ...
    ScrollBar: KnownColor = ...
    SeaGreen: KnownColor = ...
    SeaShell: KnownColor = ...
    Sienna: KnownColor = ...
    Silver: KnownColor = ...
    SkyBlue: KnownColor = ...
    SlateBlue: KnownColor = ...
    SlateGray: KnownColor = ...
    Snow: KnownColor = ...
    SpringGreen: KnownColor = ...
    SteelBlue: KnownColor = ...
    Tan: KnownColor = ...
    Teal: KnownColor = ...
    Thistle: KnownColor = ...
    Tomato: KnownColor = ...
    Transparent: KnownColor = ...
    Turquoise: KnownColor = ...
    value__ = ...
    Violet: KnownColor = ...
    Wheat: KnownColor = ...
    White: KnownColor = ...
    WhiteSmoke: KnownColor = ...
    Window: KnownColor = ...
    WindowFrame: KnownColor = ...
    WindowText: KnownColor = ...
    Yellow: KnownColor = ...
    YellowGreen: KnownColor = ...


class Pen(IDisposable, ICloneable, MarshalByRefObject, ISystemColorTracker): # skipped bases: <type 'object'>
    """
    Pen(color: Color)
    Pen(color: Color, width: Single)
    Pen(brush: Brush)
    Pen(brush: Brush, width: Single)
    """
    @property
    def Alignment(self) -> PenAlignment:
        """
        Get: Alignment(self: Pen) -> PenAlignment
        Set: Alignment(self: Pen) = value
        """
        ...

    @property
    def Brush(self) -> Brush:
        """
        Get: Brush(self: Pen) -> Brush
        Set: Brush(self: Pen) = value
        """
        ...

    @property
    def Color(self) -> Color:
        """
        Get: Color(self: Pen) -> Color
        Set: Color(self: Pen) = value
        """
        ...

    @property
    def CompoundArray(self) -> Array:
        """
        Get: CompoundArray(self: Pen) -> Array[Single]
        Set: CompoundArray(self: Pen) = value
        """
        ...

    @property
    def CustomEndCap(self) -> CustomLineCap:
        """
        Get: CustomEndCap(self: Pen) -> CustomLineCap
        Set: CustomEndCap(self: Pen) = value
        """
        ...

    @property
    def CustomStartCap(self) -> CustomLineCap:
        """
        Get: CustomStartCap(self: Pen) -> CustomLineCap
        Set: CustomStartCap(self: Pen) = value
        """
        ...

    @property
    def DashCap(self) -> DashCap:
        """
        Get: DashCap(self: Pen) -> DashCap
        Set: DashCap(self: Pen) = value
        """
        ...

    @property
    def DashOffset(self) -> Single:
        """
        Get: DashOffset(self: Pen) -> Single
        Set: DashOffset(self: Pen) = value
        """
        ...

    @property
    def DashPattern(self) -> Array:
        """
        Get: DashPattern(self: Pen) -> Array[Single]
        Set: DashPattern(self: Pen) = value
        """
        ...

    @property
    def DashStyle(self) -> DashStyle:
        """
        Get: DashStyle(self: Pen) -> DashStyle
        Set: DashStyle(self: Pen) = value
        """
        ...

    @property
    def EndCap(self) -> LineCap:
        """
        Get: EndCap(self: Pen) -> LineCap
        Set: EndCap(self: Pen) = value
        """
        ...

    @property
    def LineJoin(self) -> LineJoin:
        """
        Get: LineJoin(self: Pen) -> LineJoin
        Set: LineJoin(self: Pen) = value
        """
        ...

    @property
    def MiterLimit(self) -> Single:
        """
        Get: MiterLimit(self: Pen) -> Single
        Set: MiterLimit(self: Pen) = value
        """
        ...

    @property
    def PenType(self) -> PenType:
        """ Get: PenType(self: Pen) -> PenType """
        ...

    @property
    def StartCap(self) -> LineCap:
        """
        Get: StartCap(self: Pen) -> LineCap
        Set: StartCap(self: Pen) = value
        """
        ...

    @property
    def Transform(self) -> Matrix:
        """
        Get: Transform(self: Pen) -> Matrix
        Set: Transform(self: Pen) = value
        """
        ...

    @property
    def Width(self) -> Single:
        """
        Get: Width(self: Pen) -> Single
        Set: Width(self: Pen) = value
        """
        ...


    def MultiplyTransform(self, matrix:Matrix, order:MatrixOrder = ...): # -> 
        """ MultiplyTransform(self: Pen, matrix: Matrix)MultiplyTransform(self: Pen, matrix: Matrix, order: MatrixOrder) """
        ...

    def ResetTransform(self): # -> 
        """ ResetTransform(self: Pen) """
        ...

    def RotateTransform(self, angle:Single, order:MatrixOrder = ...): # -> 
        """ RotateTransform(self: Pen, angle: Single)RotateTransform(self: Pen, angle: Single, order: MatrixOrder) """
        ...

    def ScaleTransform(self, sx:Single, sy:Single, order:MatrixOrder = ...): # -> 
        """ ScaleTransform(self: Pen, sx: Single, sy: Single)ScaleTransform(self: Pen, sx: Single, sy: Single, order: MatrixOrder) """
        ...

    def SetLineCap(self, startCap:LineCap, endCap:LineCap, dashCap:DashCap): # -> 
        """ SetLineCap(self: Pen, startCap: LineCap, endCap: LineCap, dashCap: DashCap) """
        ...

    def TranslateTransform(self, dx:Single, dy:Single, order:MatrixOrder = ...): # -> 
        """ TranslateTransform(self: Pen, dx: Single, dy: Single)TranslateTransform(self: Pen, dx: Single, dy: Single, order: MatrixOrder) """
        ...

    def __new__(cls, *__args:Color) -> Self:
        """
        __new__(cls: type, color: Color)
        __new__(cls: type, color: Color, width: Single)
        __new__(cls: type, brush: Brush)
        __new__(cls: type, brush: Brush, width: Single)
        """
        ...


class Pens: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AliceBlue(self) -> Pen:
        """ Get: AliceBlue() -> Pen """
        ...

    @property
    def AntiqueWhite(self) -> Pen:
        """ Get: AntiqueWhite() -> Pen """
        ...

    @property
    def Aqua(self) -> Pen:
        """ Get: Aqua() -> Pen """
        ...

    @property
    def Aquamarine(self) -> Pen:
        """ Get: Aquamarine() -> Pen """
        ...

    @property
    def Azure(self) -> Pen:
        """ Get: Azure() -> Pen """
        ...

    @property
    def Beige(self) -> Pen:
        """ Get: Beige() -> Pen """
        ...

    @property
    def Bisque(self) -> Pen:
        """ Get: Bisque() -> Pen """
        ...

    @property
    def Black(self) -> Pen:
        """ Get: Black() -> Pen """
        ...

    @property
    def BlanchedAlmond(self) -> Pen:
        """ Get: BlanchedAlmond() -> Pen """
        ...

    @property
    def Blue(self) -> Pen:
        """ Get: Blue() -> Pen """
        ...

    @property
    def BlueViolet(self) -> Pen:
        """ Get: BlueViolet() -> Pen """
        ...

    @property
    def Brown(self) -> Pen:
        """ Get: Brown() -> Pen """
        ...

    @property
    def BurlyWood(self) -> Pen:
        """ Get: BurlyWood() -> Pen """
        ...

    @property
    def CadetBlue(self) -> Pen:
        """ Get: CadetBlue() -> Pen """
        ...

    @property
    def Chartreuse(self) -> Pen:
        """ Get: Chartreuse() -> Pen """
        ...

    @property
    def Chocolate(self) -> Pen:
        """ Get: Chocolate() -> Pen """
        ...

    @property
    def Coral(self) -> Pen:
        """ Get: Coral() -> Pen """
        ...

    @property
    def CornflowerBlue(self) -> Pen:
        """ Get: CornflowerBlue() -> Pen """
        ...

    @property
    def Cornsilk(self) -> Pen:
        """ Get: Cornsilk() -> Pen """
        ...

    @property
    def Crimson(self) -> Pen:
        """ Get: Crimson() -> Pen """
        ...

    @property
    def Cyan(self) -> Pen:
        """ Get: Cyan() -> Pen """
        ...

    @property
    def DarkBlue(self) -> Pen:
        """ Get: DarkBlue() -> Pen """
        ...

    @property
    def DarkCyan(self) -> Pen:
        """ Get: DarkCyan() -> Pen """
        ...

    @property
    def DarkGoldenrod(self) -> Pen:
        """ Get: DarkGoldenrod() -> Pen """
        ...

    @property
    def DarkGray(self) -> Pen:
        """ Get: DarkGray() -> Pen """
        ...

    @property
    def DarkGreen(self) -> Pen:
        """ Get: DarkGreen() -> Pen """
        ...

    @property
    def DarkKhaki(self) -> Pen:
        """ Get: DarkKhaki() -> Pen """
        ...

    @property
    def DarkMagenta(self) -> Pen:
        """ Get: DarkMagenta() -> Pen """
        ...

    @property
    def DarkOliveGreen(self) -> Pen:
        """ Get: DarkOliveGreen() -> Pen """
        ...

    @property
    def DarkOrange(self) -> Pen:
        """ Get: DarkOrange() -> Pen """
        ...

    @property
    def DarkOrchid(self) -> Pen:
        """ Get: DarkOrchid() -> Pen """
        ...

    @property
    def DarkRed(self) -> Pen:
        """ Get: DarkRed() -> Pen """
        ...

    @property
    def DarkSalmon(self) -> Pen:
        """ Get: DarkSalmon() -> Pen """
        ...

    @property
    def DarkSeaGreen(self) -> Pen:
        """ Get: DarkSeaGreen() -> Pen """
        ...

    @property
    def DarkSlateBlue(self) -> Pen:
        """ Get: DarkSlateBlue() -> Pen """
        ...

    @property
    def DarkSlateGray(self) -> Pen:
        """ Get: DarkSlateGray() -> Pen """
        ...

    @property
    def DarkTurquoise(self) -> Pen:
        """ Get: DarkTurquoise() -> Pen """
        ...

    @property
    def DarkViolet(self) -> Pen:
        """ Get: DarkViolet() -> Pen """
        ...

    @property
    def DeepPink(self) -> Pen:
        """ Get: DeepPink() -> Pen """
        ...

    @property
    def DeepSkyBlue(self) -> Pen:
        """ Get: DeepSkyBlue() -> Pen """
        ...

    @property
    def DimGray(self) -> Pen:
        """ Get: DimGray() -> Pen """
        ...

    @property
    def DodgerBlue(self) -> Pen:
        """ Get: DodgerBlue() -> Pen """
        ...

    @property
    def Firebrick(self) -> Pen:
        """ Get: Firebrick() -> Pen """
        ...

    @property
    def FloralWhite(self) -> Pen:
        """ Get: FloralWhite() -> Pen """
        ...

    @property
    def ForestGreen(self) -> Pen:
        """ Get: ForestGreen() -> Pen """
        ...

    @property
    def Fuchsia(self) -> Pen:
        """ Get: Fuchsia() -> Pen """
        ...

    @property
    def Gainsboro(self) -> Pen:
        """ Get: Gainsboro() -> Pen """
        ...

    @property
    def GhostWhite(self) -> Pen:
        """ Get: GhostWhite() -> Pen """
        ...

    @property
    def Gold(self) -> Pen:
        """ Get: Gold() -> Pen """
        ...

    @property
    def Goldenrod(self) -> Pen:
        """ Get: Goldenrod() -> Pen """
        ...

    @property
    def Gray(self) -> Pen:
        """ Get: Gray() -> Pen """
        ...

    @property
    def Green(self) -> Pen:
        """ Get: Green() -> Pen """
        ...

    @property
    def GreenYellow(self) -> Pen:
        """ Get: GreenYellow() -> Pen """
        ...

    @property
    def Honeydew(self) -> Pen:
        """ Get: Honeydew() -> Pen """
        ...

    @property
    def HotPink(self) -> Pen:
        """ Get: HotPink() -> Pen """
        ...

    @property
    def IndianRed(self) -> Pen:
        """ Get: IndianRed() -> Pen """
        ...

    @property
    def Indigo(self) -> Pen:
        """ Get: Indigo() -> Pen """
        ...

    @property
    def Ivory(self) -> Pen:
        """ Get: Ivory() -> Pen """
        ...

    @property
    def Khaki(self) -> Pen:
        """ Get: Khaki() -> Pen """
        ...

    @property
    def Lavender(self) -> Pen:
        """ Get: Lavender() -> Pen """
        ...

    @property
    def LavenderBlush(self) -> Pen:
        """ Get: LavenderBlush() -> Pen """
        ...

    @property
    def LawnGreen(self) -> Pen:
        """ Get: LawnGreen() -> Pen """
        ...

    @property
    def LemonChiffon(self) -> Pen:
        """ Get: LemonChiffon() -> Pen """
        ...

    @property
    def LightBlue(self) -> Pen:
        """ Get: LightBlue() -> Pen """
        ...

    @property
    def LightCoral(self) -> Pen:
        """ Get: LightCoral() -> Pen """
        ...

    @property
    def LightCyan(self) -> Pen:
        """ Get: LightCyan() -> Pen """
        ...

    @property
    def LightGoldenrodYellow(self) -> Pen:
        """ Get: LightGoldenrodYellow() -> Pen """
        ...

    @property
    def LightGray(self) -> Pen:
        """ Get: LightGray() -> Pen """
        ...

    @property
    def LightGreen(self) -> Pen:
        """ Get: LightGreen() -> Pen """
        ...

    @property
    def LightPink(self) -> Pen:
        """ Get: LightPink() -> Pen """
        ...

    @property
    def LightSalmon(self) -> Pen:
        """ Get: LightSalmon() -> Pen """
        ...

    @property
    def LightSeaGreen(self) -> Pen:
        """ Get: LightSeaGreen() -> Pen """
        ...

    @property
    def LightSkyBlue(self) -> Pen:
        """ Get: LightSkyBlue() -> Pen """
        ...

    @property
    def LightSlateGray(self) -> Pen:
        """ Get: LightSlateGray() -> Pen """
        ...

    @property
    def LightSteelBlue(self) -> Pen:
        """ Get: LightSteelBlue() -> Pen """
        ...

    @property
    def LightYellow(self) -> Pen:
        """ Get: LightYellow() -> Pen """
        ...

    @property
    def Lime(self) -> Pen:
        """ Get: Lime() -> Pen """
        ...

    @property
    def LimeGreen(self) -> Pen:
        """ Get: LimeGreen() -> Pen """
        ...

    @property
    def Linen(self) -> Pen:
        """ Get: Linen() -> Pen """
        ...

    @property
    def Magenta(self) -> Pen:
        """ Get: Magenta() -> Pen """
        ...

    @property
    def Maroon(self) -> Pen:
        """ Get: Maroon() -> Pen """
        ...

    @property
    def MediumAquamarine(self) -> Pen:
        """ Get: MediumAquamarine() -> Pen """
        ...

    @property
    def MediumBlue(self) -> Pen:
        """ Get: MediumBlue() -> Pen """
        ...

    @property
    def MediumOrchid(self) -> Pen:
        """ Get: MediumOrchid() -> Pen """
        ...

    @property
    def MediumPurple(self) -> Pen:
        """ Get: MediumPurple() -> Pen """
        ...

    @property
    def MediumSeaGreen(self) -> Pen:
        """ Get: MediumSeaGreen() -> Pen """
        ...

    @property
    def MediumSlateBlue(self) -> Pen:
        """ Get: MediumSlateBlue() -> Pen """
        ...

    @property
    def MediumSpringGreen(self) -> Pen:
        """ Get: MediumSpringGreen() -> Pen """
        ...

    @property
    def MediumTurquoise(self) -> Pen:
        """ Get: MediumTurquoise() -> Pen """
        ...

    @property
    def MediumVioletRed(self) -> Pen:
        """ Get: MediumVioletRed() -> Pen """
        ...

    @property
    def MidnightBlue(self) -> Pen:
        """ Get: MidnightBlue() -> Pen """
        ...

    @property
    def MintCream(self) -> Pen:
        """ Get: MintCream() -> Pen """
        ...

    @property
    def MistyRose(self) -> Pen:
        """ Get: MistyRose() -> Pen """
        ...

    @property
    def Moccasin(self) -> Pen:
        """ Get: Moccasin() -> Pen """
        ...

    @property
    def NavajoWhite(self) -> Pen:
        """ Get: NavajoWhite() -> Pen """
        ...

    @property
    def Navy(self) -> Pen:
        """ Get: Navy() -> Pen """
        ...

    @property
    def OldLace(self) -> Pen:
        """ Get: OldLace() -> Pen """
        ...

    @property
    def Olive(self) -> Pen:
        """ Get: Olive() -> Pen """
        ...

    @property
    def OliveDrab(self) -> Pen:
        """ Get: OliveDrab() -> Pen """
        ...

    @property
    def Orange(self) -> Pen:
        """ Get: Orange() -> Pen """
        ...

    @property
    def OrangeRed(self) -> Pen:
        """ Get: OrangeRed() -> Pen """
        ...

    @property
    def Orchid(self) -> Pen:
        """ Get: Orchid() -> Pen """
        ...

    @property
    def PaleGoldenrod(self) -> Pen:
        """ Get: PaleGoldenrod() -> Pen """
        ...

    @property
    def PaleGreen(self) -> Pen:
        """ Get: PaleGreen() -> Pen """
        ...

    @property
    def PaleTurquoise(self) -> Pen:
        """ Get: PaleTurquoise() -> Pen """
        ...

    @property
    def PaleVioletRed(self) -> Pen:
        """ Get: PaleVioletRed() -> Pen """
        ...

    @property
    def PapayaWhip(self) -> Pen:
        """ Get: PapayaWhip() -> Pen """
        ...

    @property
    def PeachPuff(self) -> Pen:
        """ Get: PeachPuff() -> Pen """
        ...

    @property
    def Peru(self) -> Pen:
        """ Get: Peru() -> Pen """
        ...

    @property
    def Pink(self) -> Pen:
        """ Get: Pink() -> Pen """
        ...

    @property
    def Plum(self) -> Pen:
        """ Get: Plum() -> Pen """
        ...

    @property
    def PowderBlue(self) -> Pen:
        """ Get: PowderBlue() -> Pen """
        ...

    @property
    def Purple(self) -> Pen:
        """ Get: Purple() -> Pen """
        ...

    @property
    def Red(self) -> Pen:
        """ Get: Red() -> Pen """
        ...

    @property
    def RosyBrown(self) -> Pen:
        """ Get: RosyBrown() -> Pen """
        ...

    @property
    def RoyalBlue(self) -> Pen:
        """ Get: RoyalBlue() -> Pen """
        ...

    @property
    def SaddleBrown(self) -> Pen:
        """ Get: SaddleBrown() -> Pen """
        ...

    @property
    def Salmon(self) -> Pen:
        """ Get: Salmon() -> Pen """
        ...

    @property
    def SandyBrown(self) -> Pen:
        """ Get: SandyBrown() -> Pen """
        ...

    @property
    def SeaGreen(self) -> Pen:
        """ Get: SeaGreen() -> Pen """
        ...

    @property
    def SeaShell(self) -> Pen:
        """ Get: SeaShell() -> Pen """
        ...

    @property
    def Sienna(self) -> Pen:
        """ Get: Sienna() -> Pen """
        ...

    @property
    def Silver(self) -> Pen:
        """ Get: Silver() -> Pen """
        ...

    @property
    def SkyBlue(self) -> Pen:
        """ Get: SkyBlue() -> Pen """
        ...

    @property
    def SlateBlue(self) -> Pen:
        """ Get: SlateBlue() -> Pen """
        ...

    @property
    def SlateGray(self) -> Pen:
        """ Get: SlateGray() -> Pen """
        ...

    @property
    def Snow(self) -> Pen:
        """ Get: Snow() -> Pen """
        ...

    @property
    def SpringGreen(self) -> Pen:
        """ Get: SpringGreen() -> Pen """
        ...

    @property
    def SteelBlue(self) -> Pen:
        """ Get: SteelBlue() -> Pen """
        ...

    @property
    def Tan(self) -> Pen:
        """ Get: Tan() -> Pen """
        ...

    @property
    def Teal(self) -> Pen:
        """ Get: Teal() -> Pen """
        ...

    @property
    def Thistle(self) -> Pen:
        """ Get: Thistle() -> Pen """
        ...

    @property
    def Tomato(self) -> Pen:
        """ Get: Tomato() -> Pen """
        ...

    @property
    def Transparent(self) -> Pen:
        """ Get: Transparent() -> Pen """
        ...

    @property
    def Turquoise(self) -> Pen:
        """ Get: Turquoise() -> Pen """
        ...

    @property
    def Violet(self) -> Pen:
        """ Get: Violet() -> Pen """
        ...

    @property
    def Wheat(self) -> Pen:
        """ Get: Wheat() -> Pen """
        ...

    @property
    def White(self) -> Pen:
        """ Get: White() -> Pen """
        ...

    @property
    def WhiteSmoke(self) -> Pen:
        """ Get: WhiteSmoke() -> Pen """
        ...

    @property
    def Yellow(self) -> Pen:
        """ Get: Yellow() -> Pen """
        ...

    @property
    def YellowGreen(self) -> Pen:
        """ Get: YellowGreen() -> Pen """
        ...




class Point: # skipped bases: <type 'object'>, <type 'object'>
    """
    Point(x: int, y: int)
    Point(sz: Size)
    Point(dw: int)
    """
    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: Point) -> bool """
        ...

    @property
    def X(self) -> int:
        """
        Get: X(self: Point) -> int
        Set: X(self: Point) = value
        """
        ...

    @property
    def Y(self) -> int:
        """
        Get: Y(self: Point) -> int
        Set: Y(self: Point) = value
        """
        ...


    @staticmethod
    def Add(pt:Point, sz:Size) -> Point:
        """ Add(pt: Point, sz: Size) -> Point """
        ...

    @staticmethod
    def Ceiling(value:PointF) -> Point:
        """ Ceiling(value: PointF) -> Point """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: Point, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Point) -> int """
        ...

    def Offset(self, *__args:Point): # -> 
        """ Offset(self: Point, dx: int, dy: int)Offset(self: Point, p: Point) """
        ...

    @staticmethod
    def Round(value:PointF) -> Point:
        """ Round(value: PointF) -> Point """
        ...

    @staticmethod
    def Subtract(pt:Point, sz:Size) -> Point:
        """ Subtract(pt: Point, sz: Size) -> Point """
        ...

    def ToString(self) -> str:
        """ ToString(self: Point) -> str """
        ...

    @staticmethod
    def Truncate(value:PointF) -> Point:
        """ Truncate(value: PointF) -> Point """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    Empty: Point = ...


class PointConverter(TypeConverter): # skipped bases: <type 'object'>
    """ PointConverter() """
    pass

class PointF: # skipped bases: <type 'object'>, <type 'object'>
    """ PointF(x: Single, y: Single) """
    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: PointF) -> bool """
        ...

    @property
    def X(self) -> Single:
        """
        Get: X(self: PointF) -> Single
        Set: X(self: PointF) = value
        """
        ...

    @property
    def Y(self) -> Single:
        """
        Get: Y(self: PointF) -> Single
        Set: Y(self: PointF) = value
        """
        ...


    @staticmethod
    def Add(pt:PointF, sz:Size) -> PointF:
        """
        Add(pt: PointF, sz: Size) -> PointF
        Add(pt: PointF, sz: SizeF) -> PointF
        """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: PointF, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: PointF) -> int """
        ...

    @staticmethod
    def Subtract(pt:PointF, sz:Size) -> PointF:
        """
        Subtract(pt: PointF, sz: Size) -> PointF
        Subtract(pt: PointF, sz: SizeF) -> PointF
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: PointF) -> str """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        ...

    Empty: PointF = ...


class Rectangle: # skipped bases: <type 'object'>, <type 'object'>
    """
    Rectangle(x: int, y: int, width: int, height: int)
    Rectangle(location: Point, size: Size)
    """
    @property
    def Bottom(self) -> int:
        """ Get: Bottom(self: Rectangle) -> int """
        ...

    @property
    def Height(self) -> int:
        """
        Get: Height(self: Rectangle) -> int
        Set: Height(self: Rectangle) = value
        """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: Rectangle) -> bool """
        ...

    @property
    def Left(self) -> int:
        """ Get: Left(self: Rectangle) -> int """
        ...

    @property
    def Location(self) -> Point:
        """
        Get: Location(self: Rectangle) -> Point
        Set: Location(self: Rectangle) = value
        """
        ...

    @property
    def Right(self) -> int:
        """ Get: Right(self: Rectangle) -> int """
        ...

    @property
    def Size(self) -> Size:
        """
        Get: Size(self: Rectangle) -> Size
        Set: Size(self: Rectangle) = value
        """
        ...

    @property
    def Top(self) -> int:
        """ Get: Top(self: Rectangle) -> int """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: Rectangle) -> int
        Set: Width(self: Rectangle) = value
        """
        ...

    @property
    def X(self) -> int:
        """
        Get: X(self: Rectangle) -> int
        Set: X(self: Rectangle) = value
        """
        ...

    @property
    def Y(self) -> int:
        """
        Get: Y(self: Rectangle) -> int
        Set: Y(self: Rectangle) = value
        """
        ...


    @staticmethod
    def Ceiling(value:RectangleF) -> Rectangle:
        """ Ceiling(value: RectangleF) -> Rectangle """
        ...

    def Contains(self, *__args:Point) -> bool:
        """
        Contains(self: Rectangle, x: int, y: int) -> bool
        Contains(self: Rectangle, pt: Point) -> bool
        Contains(self: Rectangle, rect: Rectangle) -> bool
        """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: Rectangle, obj: object) -> bool """
        ...

    @staticmethod
    def FromLTRB(left:int, top:int, right:int, bottom:int) -> Rectangle:
        """ FromLTRB(left: int, top: int, right: int, bottom: int) -> Rectangle """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Rectangle) -> int """
        ...

    def Inflate(self, *__args:Size): # -> 
        """ Inflate(self: Rectangle, width: int, height: int)Inflate(self: Rectangle, size: Size)Inflate(rect: Rectangle, x: int, y: int) -> Rectangle """
        ...

    def Intersect(self, *__args:Rectangle): # -> 
        """ Intersect(self: Rectangle, rect: Rectangle)Intersect(a: Rectangle, b: Rectangle) -> Rectangle """
        ...

    def IntersectsWith(self, rect:Rectangle) -> bool:
        """ IntersectsWith(self: Rectangle, rect: Rectangle) -> bool """
        ...

    def Offset(self, *__args:Point): # -> 
        """ Offset(self: Rectangle, pos: Point)Offset(self: Rectangle, x: int, y: int) """
        ...

    @staticmethod
    def Round(value:RectangleF) -> Rectangle:
        """ Round(value: RectangleF) -> Rectangle """
        ...

    def ToString(self) -> str:
        """ ToString(self: Rectangle) -> str """
        ...

    @staticmethod
    def Truncate(value:RectangleF) -> Rectangle:
        """ Truncate(value: RectangleF) -> Rectangle """
        ...

    @staticmethod
    def Union(a:Rectangle, b:Rectangle) -> Rectangle:
        """ Union(a: Rectangle, b: Rectangle) -> Rectangle """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Empty: Rectangle = ...


class RectangleConverter(TypeConverter): # skipped bases: <type 'object'>
    """ RectangleConverter() """
    pass

class RectangleF: # skipped bases: <type 'object'>, <type 'object'>
    """
    RectangleF(x: Single, y: Single, width: Single, height: Single)
    RectangleF(location: PointF, size: SizeF)
    """
    @property
    def Bottom(self) -> Single:
        """ Get: Bottom(self: RectangleF) -> Single """
        ...

    @property
    def Height(self) -> Single:
        """
        Get: Height(self: RectangleF) -> Single
        Set: Height(self: RectangleF) = value
        """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: RectangleF) -> bool """
        ...

    @property
    def Left(self) -> Single:
        """ Get: Left(self: RectangleF) -> Single """
        ...

    @property
    def Location(self) -> PointF:
        """
        Get: Location(self: RectangleF) -> PointF
        Set: Location(self: RectangleF) = value
        """
        ...

    @property
    def Right(self) -> Single:
        """ Get: Right(self: RectangleF) -> Single """
        ...

    @property
    def Size(self) -> SizeF:
        """
        Get: Size(self: RectangleF) -> SizeF
        Set: Size(self: RectangleF) = value
        """
        ...

    @property
    def Top(self) -> Single:
        """ Get: Top(self: RectangleF) -> Single """
        ...

    @property
    def Width(self) -> Single:
        """
        Get: Width(self: RectangleF) -> Single
        Set: Width(self: RectangleF) = value
        """
        ...

    @property
    def X(self) -> Single:
        """
        Get: X(self: RectangleF) -> Single
        Set: X(self: RectangleF) = value
        """
        ...

    @property
    def Y(self) -> Single:
        """
        Get: Y(self: RectangleF) -> Single
        Set: Y(self: RectangleF) = value
        """
        ...


    def Contains(self, *__args:PointF) -> bool:
        """
        Contains(self: RectangleF, x: Single, y: Single) -> bool
        Contains(self: RectangleF, pt: PointF) -> bool
        Contains(self: RectangleF, rect: RectangleF) -> bool
        """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: RectangleF, obj: object) -> bool """
        ...

    @staticmethod
    def FromLTRB(left:Single, top:Single, right:Single, bottom:Single) -> RectangleF:
        """ FromLTRB(left: Single, top: Single, right: Single, bottom: Single) -> RectangleF """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RectangleF) -> int """
        ...

    def Inflate(self, *__args:SizeF): # -> 
        """ Inflate(self: RectangleF, x: Single, y: Single)Inflate(self: RectangleF, size: SizeF)Inflate(rect: RectangleF, x: Single, y: Single) -> RectangleF """
        ...

    def Intersect(self, *__args:RectangleF): # -> 
        """ Intersect(self: RectangleF, rect: RectangleF)Intersect(a: RectangleF, b: RectangleF) -> RectangleF """
        ...

    def IntersectsWith(self, rect:RectangleF) -> bool:
        """ IntersectsWith(self: RectangleF, rect: RectangleF) -> bool """
        ...

    def Offset(self, *__args:PointF): # -> 
        """ Offset(self: RectangleF, pos: PointF)Offset(self: RectangleF, x: Single, y: Single) """
        ...

    def ToString(self) -> str:
        """ ToString(self: RectangleF) -> str """
        ...

    @staticmethod
    def Union(a:RectangleF, b:RectangleF) -> RectangleF:
        """ Union(a: RectangleF, b: RectangleF) -> RectangleF """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Empty: RectangleF = ...


class Region(IDisposable, MarshalByRefObject): # skipped bases: <type 'object'>
    """
    Region()
    Region(rect: RectangleF)
    Region(rect: Rectangle)
    Region(path: GraphicsPath)
    Region(rgnData: RegionData)
    """
    def Clone(self) -> Region:
        """ Clone(self: Region) -> Region """
        ...

    def Complement(self, *__args:RectangleF): # -> 
        """ Complement(self: Region, rect: RectangleF)Complement(self: Region, rect: Rectangle)Complement(self: Region, path: GraphicsPath)Complement(self: Region, region: Region) """
        ...

    def Equals(self, *__args) -> bool:
        """ Equals(self: Region, region: Region, g: Graphics) -> bool """
        ...

    def Exclude(self, *__args:Rectangle): # -> 
        """ Exclude(self: Region, rect: Rectangle)Exclude(self: Region, rect: RectangleF)Exclude(self: Region, path: GraphicsPath)Exclude(self: Region, region: Region) """
        ...

    @staticmethod
    def FromHrgn(hrgn:IntPtr) -> Region:
        """ FromHrgn(hrgn: IntPtr) -> Region """
        ...

    def GetBounds(self, g:Graphics) -> RectangleF:
        """ GetBounds(self: Region, g: Graphics) -> RectangleF """
        ...

    def GetHrgn(self, g:Graphics) -> IntPtr:
        """ GetHrgn(self: Region, g: Graphics) -> IntPtr """
        ...

    def GetRegionData(self) -> RegionData:
        """ GetRegionData(self: Region) -> RegionData """
        ...

    def GetRegionScans(self, matrix:Matrix) -> Array:
        """ GetRegionScans(self: Region, matrix: Matrix) -> Array[RectangleF] """
        ...

    def Intersect(self, *__args:Region): # -> 
        """ Intersect(self: Region, region: Region)Intersect(self: Region, rect: RectangleF)Intersect(self: Region, rect: Rectangle)Intersect(self: Region, path: GraphicsPath) """
        ...

    def IsEmpty(self, g:Graphics) -> bool:
        """ IsEmpty(self: Region, g: Graphics) -> bool """
        ...

    def IsInfinite(self, g:Graphics) -> bool:
        """ IsInfinite(self: Region, g: Graphics) -> bool """
        ...

    def IsVisible(self, *__args:PointF) -> bool:
        """
        IsVisible(self: Region, x: Single, y: Single) -> bool
        IsVisible(self: Region, point: PointF) -> bool
        IsVisible(self: Region, x: Single, y: Single, g: Graphics) -> bool
        IsVisible(self: Region, point: PointF, g: Graphics) -> bool
        IsVisible(self: Region, x: Single, y: Single, width: Single, height: Single) -> bool
        IsVisible(self: Region, rect: RectangleF) -> bool
        IsVisible(self: Region, x: Single, y: Single, width: Single, height: Single, g: Graphics) -> bool
        IsVisible(self: Region, rect: RectangleF, g: Graphics) -> bool
        IsVisible(self: Region, x: int, y: int, g: Graphics) -> bool
        IsVisible(self: Region, point: Point) -> bool
        IsVisible(self: Region, point: Point, g: Graphics) -> bool
        IsVisible(self: Region, x: int, y: int, width: int, height: int) -> bool
        IsVisible(self: Region, rect: Rectangle) -> bool
        IsVisible(self: Region, x: int, y: int, width: int, height: int, g: Graphics) -> bool
        IsVisible(self: Region, rect: Rectangle, g: Graphics) -> bool
        """
        ...

    def MakeEmpty(self): # -> 
        """ MakeEmpty(self: Region) """
        ...

    def MakeInfinite(self): # -> 
        """ MakeInfinite(self: Region) """
        ...

    def ReleaseHrgn(self, regionHandle:IntPtr): # -> 
        """ ReleaseHrgn(self: Region, regionHandle: IntPtr) """
        ...

    def Transform(self, matrix:Matrix): # -> 
        """ Transform(self: Region, matrix: Matrix) """
        ...

    def Translate(self, dx:Single, dy:Single): # -> 
        """ Translate(self: Region, dx: Single, dy: Single)Translate(self: Region, dx: int, dy: int) """
        ...

    def Union(self, *__args:Rectangle): # -> 
        """ Union(self: Region, rect: Rectangle)Union(self: Region, rect: RectangleF)Union(self: Region, path: GraphicsPath)Union(self: Region, region: Region) """
        ...

    def Xor(self, *__args:RectangleF): # -> 
        """ Xor(self: Region, rect: RectangleF)Xor(self: Region, rect: Rectangle)Xor(self: Region, path: GraphicsPath)Xor(self: Region, region: Region) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, *__args:RectangleF) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, rect: RectangleF)
        __new__(cls: type, rect: Rectangle)
        __new__(cls: type, path: GraphicsPath)
        __new__(cls: type, rgnData: RegionData)
        """
        ...


class RotateFlipType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RotateFlipType, values: Rotate180FlipNone (2), Rotate180FlipX (6), Rotate180FlipXY (0), Rotate180FlipY (4), Rotate270FlipNone (3), Rotate270FlipX (7), Rotate270FlipXY (1), Rotate270FlipY (5), Rotate90FlipNone (1), Rotate90FlipX (5), Rotate90FlipXY (3), Rotate90FlipY (7), RotateNoneFlipNone (0), RotateNoneFlipX (4), RotateNoneFlipXY (2), RotateNoneFlipY (6) """
    Rotate180FlipNone: RotateFlipType = ...
    Rotate180FlipX: RotateFlipType = ...
    Rotate180FlipXY: RotateFlipType = ...
    Rotate180FlipY: RotateFlipType = ...
    Rotate270FlipNone: RotateFlipType = ...
    Rotate270FlipX: RotateFlipType = ...
    Rotate270FlipXY: RotateFlipType = ...
    Rotate270FlipY: RotateFlipType = ...
    Rotate90FlipNone: RotateFlipType = ...
    Rotate90FlipX: RotateFlipType = ...
    Rotate90FlipXY: RotateFlipType = ...
    Rotate90FlipY: RotateFlipType = ...
    RotateNoneFlipNone: RotateFlipType = ...
    RotateNoneFlipX: RotateFlipType = ...
    RotateNoneFlipXY: RotateFlipType = ...
    RotateNoneFlipY: RotateFlipType = ...
    value__ = ...


class Size: # skipped bases: <type 'object'>, <type 'object'>
    """
    Size(pt: Point)
    Size(width: int, height: int)
    """
    @property
    def Height(self) -> int:
        """
        Get: Height(self: Size) -> int
        Set: Height(self: Size) = value
        """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: Size) -> bool """
        ...

    @property
    def Width(self) -> int:
        """
        Get: Width(self: Size) -> int
        Set: Width(self: Size) = value
        """
        ...


    @staticmethod
    def Add(sz1:Size, sz2:Size) -> Size:
        """ Add(sz1: Size, sz2: Size) -> Size """
        ...

    @staticmethod
    def Ceiling(value:SizeF) -> Size:
        """ Ceiling(value: SizeF) -> Size """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: Size, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Size) -> int """
        ...

    @staticmethod
    def Round(value:SizeF) -> Size:
        """ Round(value: SizeF) -> Size """
        ...

    @staticmethod
    def Subtract(sz1:Size, sz2:Size) -> Size:
        """ Subtract(sz1: Size, sz2: Size) -> Size """
        ...

    def ToString(self) -> str:
        """ ToString(self: Size) -> str """
        ...

    @staticmethod
    def Truncate(value:SizeF) -> Size:
        """ Truncate(value: SizeF) -> Size """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(sz1: Size, sz2: Size) -> Size """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(sz1: Size, sz2: Size) -> Size """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    Empty: Size = ...


class SizeConverter(TypeConverter): # skipped bases: <type 'object'>
    """ SizeConverter() """
    pass

class SizeF: # skipped bases: <type 'object'>, <type 'object'>
    """
    SizeF(size: SizeF)
    SizeF(pt: PointF)
    SizeF(width: Single, height: Single)
    """
    @property
    def Height(self) -> Single:
        """
        Get: Height(self: SizeF) -> Single
        Set: Height(self: SizeF) = value
        """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: SizeF) -> bool """
        ...

    @property
    def Width(self) -> Single:
        """
        Get: Width(self: SizeF) -> Single
        Set: Width(self: SizeF) = value
        """
        ...


    @staticmethod
    def Add(sz1:SizeF, sz2:SizeF) -> SizeF:
        """ Add(sz1: SizeF, sz2: SizeF) -> SizeF """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: SizeF, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SizeF) -> int """
        ...

    @staticmethod
    def Subtract(sz1:SizeF, sz2:SizeF) -> SizeF:
        """ Subtract(sz1: SizeF, sz2: SizeF) -> SizeF """
        ...

    def ToPointF(self) -> PointF:
        """ ToPointF(self: SizeF) -> PointF """
        ...

    def ToSize(self) -> Size:
        """ ToSize(self: SizeF) -> Size """
        ...

    def ToString(self) -> str:
        """ ToString(self: SizeF) -> str """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(sz1: SizeF, sz2: SizeF) -> SizeF """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(sz1: SizeF, sz2: SizeF) -> SizeF """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    Empty: SizeF = ...


class SizeFConverter(TypeConverter): # skipped bases: <type 'object'>
    """ SizeFConverter() """
    pass

class SolidBrush(ISystemColorTracker, Brush): # skipped bases: <type 'IDisposable'>, <type 'ICloneable'>, <type 'object'>
    """ SolidBrush(color: Color) """
    @property
    def Color(self) -> Color:
        """
        Get: Color(self: SolidBrush) -> Color
        Set: Color(self: SolidBrush) = value
        """
        ...


    def __new__(cls, color:Color) -> Self:
        """ __new__(cls: type, color: Color) """
        ...


class StringAlignment(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StringAlignment, values: Center (1), Far (2), Near (0) """
    Center: StringAlignment = ...
    Far: StringAlignment = ...
    Near: StringAlignment = ...
    value__ = ...


class StringDigitSubstitute(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StringDigitSubstitute, values: National (2), None (1), Traditional (3), User (0) """
    National: StringDigitSubstitute = ...
    Traditional: StringDigitSubstitute = ...
    User: StringDigitSubstitute = ...
    value__ = ...


class StringFormat(IDisposable, ICloneable, MarshalByRefObject): # skipped bases: <type 'object'>
    """
    StringFormat()
    StringFormat(options: StringFormatFlags)
    StringFormat(options: StringFormatFlags, language: int)
    StringFormat(format: StringFormat)
    """
    @property
    def Alignment(self) -> StringAlignment:
        """
        Get: Alignment(self: StringFormat) -> StringAlignment
        Set: Alignment(self: StringFormat) = value
        """
        ...

    @property
    def DigitSubstitutionLanguage(self) -> int:
        """ Get: DigitSubstitutionLanguage(self: StringFormat) -> int """
        ...

    @property
    def DigitSubstitutionMethod(self) -> StringDigitSubstitute:
        """ Get: DigitSubstitutionMethod(self: StringFormat) -> StringDigitSubstitute """
        ...

    @property
    def FormatFlags(self) -> StringFormatFlags:
        """
        Get: FormatFlags(self: StringFormat) -> StringFormatFlags
        Set: FormatFlags(self: StringFormat) = value
        """
        ...

    @property
    def GenericDefault(self) -> StringFormat:
        """ Get: GenericDefault() -> StringFormat """
        ...

    @property
    def GenericTypographic(self) -> StringFormat:
        """ Get: GenericTypographic() -> StringFormat """
        ...

    @property
    def HotkeyPrefix(self) -> HotkeyPrefix:
        """
        Get: HotkeyPrefix(self: StringFormat) -> HotkeyPrefix
        Set: HotkeyPrefix(self: StringFormat) = value
        """
        ...

    @property
    def LineAlignment(self) -> StringAlignment:
        """
        Get: LineAlignment(self: StringFormat) -> StringAlignment
        Set: LineAlignment(self: StringFormat) = value
        """
        ...

    @property
    def Trimming(self) -> StringTrimming:
        """
        Get: Trimming(self: StringFormat) -> StringTrimming
        Set: Trimming(self: StringFormat) = value
        """
        ...


    def GetTabStops(self, firstTabOffset) -> Tuple_[Array, Single]:
        """ GetTabStops(self: StringFormat) -> (Array[Single], Single) """
        ...

    def SetDigitSubstitution(self, language:int, substitute:StringDigitSubstitute): # -> 
        """ SetDigitSubstitution(self: StringFormat, language: int, substitute: StringDigitSubstitute) """
        ...

    def SetMeasurableCharacterRanges(self, ranges:Array): # -> 
        """ SetMeasurableCharacterRanges(self: StringFormat, ranges: Array[CharacterRange]) """
        ...

    def SetTabStops(self, firstTabOffset:Single, tabStops:Array): # -> 
        """ SetTabStops(self: StringFormat, firstTabOffset: Single, tabStops: Array[Single]) """
        ...

    def ToString(self) -> str:
        """ ToString(self: StringFormat) -> str """
        ...

    def __new__(cls, *__args:StringFormatFlags) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, options: StringFormatFlags)
        __new__(cls: type, options: StringFormatFlags, language: int)
        __new__(cls: type, format: StringFormat)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...



class StringFormatFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) StringFormatFlags, values: DirectionRightToLeft (1), DirectionVertical (2), DisplayFormatControl (32), FitBlackBox (4), LineLimit (8192), MeasureTrailingSpaces (2048), NoClip (16384), NoFontFallback (1024), NoWrap (4096) """
    DirectionRightToLeft: StringFormatFlags = ...
    DirectionVertical: StringFormatFlags = ...
    DisplayFormatControl: StringFormatFlags = ...
    FitBlackBox: StringFormatFlags = ...
    LineLimit: StringFormatFlags = ...
    MeasureTrailingSpaces: StringFormatFlags = ...
    NoClip: StringFormatFlags = ...
    NoFontFallback: StringFormatFlags = ...
    NoWrap: StringFormatFlags = ...
    value__ = ...


class StringTrimming(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StringTrimming, values: Character (1), EllipsisCharacter (3), EllipsisPath (5), EllipsisWord (4), None (0), Word (2) """
    Character: StringTrimming = ...
    EllipsisCharacter: StringTrimming = ...
    EllipsisPath: StringTrimming = ...
    EllipsisWord: StringTrimming = ...
    value__ = ...
    Word: StringTrimming = ...


class StringUnit(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StringUnit, values: Display (1), Document (5), Em (32), Inch (4), Millimeter (6), Pixel (2), Point (3), World (0) """
    Display: StringUnit = ...
    Document: StringUnit = ...
    Em: StringUnit = ...
    Inch: StringUnit = ...
    Millimeter: StringUnit = ...
    Pixel: StringUnit = ...
    Point: StringUnit = ...
    value__ = ...
    World: StringUnit = ...


class SystemBrushes: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ActiveBorder(self) -> Brush:
        """ Get: ActiveBorder() -> Brush """
        ...

    @property
    def ActiveCaption(self) -> Brush:
        """ Get: ActiveCaption() -> Brush """
        ...

    @property
    def ActiveCaptionText(self) -> Brush:
        """ Get: ActiveCaptionText() -> Brush """
        ...

    @property
    def AppWorkspace(self) -> Brush:
        """ Get: AppWorkspace() -> Brush """
        ...

    @property
    def ButtonFace(self) -> Brush:
        """ Get: ButtonFace() -> Brush """
        ...

    @property
    def ButtonHighlight(self) -> Brush:
        """ Get: ButtonHighlight() -> Brush """
        ...

    @property
    def ButtonShadow(self) -> Brush:
        """ Get: ButtonShadow() -> Brush """
        ...

    @property
    def Control(self) -> Brush:
        """ Get: Control() -> Brush """
        ...

    @property
    def ControlDark(self) -> Brush:
        """ Get: ControlDark() -> Brush """
        ...

    @property
    def ControlDarkDark(self) -> Brush:
        """ Get: ControlDarkDark() -> Brush """
        ...

    @property
    def ControlLight(self) -> Brush:
        """ Get: ControlLight() -> Brush """
        ...

    @property
    def ControlLightLight(self) -> Brush:
        """ Get: ControlLightLight() -> Brush """
        ...

    @property
    def ControlText(self) -> Brush:
        """ Get: ControlText() -> Brush """
        ...

    @property
    def Desktop(self) -> Brush:
        """ Get: Desktop() -> Brush """
        ...

    @property
    def GradientActiveCaption(self) -> Brush:
        """ Get: GradientActiveCaption() -> Brush """
        ...

    @property
    def GradientInactiveCaption(self) -> Brush:
        """ Get: GradientInactiveCaption() -> Brush """
        ...

    @property
    def GrayText(self) -> Brush:
        """ Get: GrayText() -> Brush """
        ...

    @property
    def Highlight(self) -> Brush:
        """ Get: Highlight() -> Brush """
        ...

    @property
    def HighlightText(self) -> Brush:
        """ Get: HighlightText() -> Brush """
        ...

    @property
    def HotTrack(self) -> Brush:
        """ Get: HotTrack() -> Brush """
        ...

    @property
    def InactiveBorder(self) -> Brush:
        """ Get: InactiveBorder() -> Brush """
        ...

    @property
    def InactiveCaption(self) -> Brush:
        """ Get: InactiveCaption() -> Brush """
        ...

    @property
    def InactiveCaptionText(self) -> Brush:
        """ Get: InactiveCaptionText() -> Brush """
        ...

    @property
    def Info(self) -> Brush:
        """ Get: Info() -> Brush """
        ...

    @property
    def InfoText(self) -> Brush:
        """ Get: InfoText() -> Brush """
        ...

    @property
    def Menu(self) -> Brush:
        """ Get: Menu() -> Brush """
        ...

    @property
    def MenuBar(self) -> Brush:
        """ Get: MenuBar() -> Brush """
        ...

    @property
    def MenuHighlight(self) -> Brush:
        """ Get: MenuHighlight() -> Brush """
        ...

    @property
    def MenuText(self) -> Brush:
        """ Get: MenuText() -> Brush """
        ...

    @property
    def ScrollBar(self) -> Brush:
        """ Get: ScrollBar() -> Brush """
        ...

    @property
    def Window(self) -> Brush:
        """ Get: Window() -> Brush """
        ...

    @property
    def WindowFrame(self) -> Brush:
        """ Get: WindowFrame() -> Brush """
        ...

    @property
    def WindowText(self) -> Brush:
        """ Get: WindowText() -> Brush """
        ...


    @staticmethod
    def FromSystemColor(c:Color) -> Brush:
        """ FromSystemColor(c: Color) -> Brush """
        ...



class SystemColors: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ActiveBorder(self) -> Color:
        """ Get: ActiveBorder() -> Color """
        ...

    @property
    def ActiveCaption(self) -> Color:
        """ Get: ActiveCaption() -> Color """
        ...

    @property
    def ActiveCaptionText(self) -> Color:
        """ Get: ActiveCaptionText() -> Color """
        ...

    @property
    def AppWorkspace(self) -> Color:
        """ Get: AppWorkspace() -> Color """
        ...

    @property
    def ButtonFace(self) -> Color:
        """ Get: ButtonFace() -> Color """
        ...

    @property
    def ButtonHighlight(self) -> Color:
        """ Get: ButtonHighlight() -> Color """
        ...

    @property
    def ButtonShadow(self) -> Color:
        """ Get: ButtonShadow() -> Color """
        ...

    @property
    def Control(self) -> Color:
        """ Get: Control() -> Color """
        ...

    @property
    def ControlDark(self) -> Color:
        """ Get: ControlDark() -> Color """
        ...

    @property
    def ControlDarkDark(self) -> Color:
        """ Get: ControlDarkDark() -> Color """
        ...

    @property
    def ControlLight(self) -> Color:
        """ Get: ControlLight() -> Color """
        ...

    @property
    def ControlLightLight(self) -> Color:
        """ Get: ControlLightLight() -> Color """
        ...

    @property
    def ControlText(self) -> Color:
        """ Get: ControlText() -> Color """
        ...

    @property
    def Desktop(self) -> Color:
        """ Get: Desktop() -> Color """
        ...

    @property
    def GradientActiveCaption(self) -> Color:
        """ Get: GradientActiveCaption() -> Color """
        ...

    @property
    def GradientInactiveCaption(self) -> Color:
        """ Get: GradientInactiveCaption() -> Color """
        ...

    @property
    def GrayText(self) -> Color:
        """ Get: GrayText() -> Color """
        ...

    @property
    def Highlight(self) -> Color:
        """ Get: Highlight() -> Color """
        ...

    @property
    def HighlightText(self) -> Color:
        """ Get: HighlightText() -> Color """
        ...

    @property
    def HotTrack(self) -> Color:
        """ Get: HotTrack() -> Color """
        ...

    @property
    def InactiveBorder(self) -> Color:
        """ Get: InactiveBorder() -> Color """
        ...

    @property
    def InactiveCaption(self) -> Color:
        """ Get: InactiveCaption() -> Color """
        ...

    @property
    def InactiveCaptionText(self) -> Color:
        """ Get: InactiveCaptionText() -> Color """
        ...

    @property
    def Info(self) -> Color:
        """ Get: Info() -> Color """
        ...

    @property
    def InfoText(self) -> Color:
        """ Get: InfoText() -> Color """
        ...

    @property
    def Menu(self) -> Color:
        """ Get: Menu() -> Color """
        ...

    @property
    def MenuBar(self) -> Color:
        """ Get: MenuBar() -> Color """
        ...

    @property
    def MenuHighlight(self) -> Color:
        """ Get: MenuHighlight() -> Color """
        ...

    @property
    def MenuText(self) -> Color:
        """ Get: MenuText() -> Color """
        ...

    @property
    def ScrollBar(self) -> Color:
        """ Get: ScrollBar() -> Color """
        ...

    @property
    def Window(self) -> Color:
        """ Get: Window() -> Color """
        ...

    @property
    def WindowFrame(self) -> Color:
        """ Get: WindowFrame() -> Color """
        ...

    @property
    def WindowText(self) -> Color:
        """ Get: WindowText() -> Color """
        ...




class SystemFonts: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CaptionFont(self) -> Font:
        """ Get: CaptionFont() -> Font """
        ...

    @property
    def DefaultFont(self) -> Font:
        """ Get: DefaultFont() -> Font """
        ...

    @property
    def DialogFont(self) -> Font:
        """ Get: DialogFont() -> Font """
        ...

    @property
    def IconTitleFont(self) -> Font:
        """ Get: IconTitleFont() -> Font """
        ...

    @property
    def MenuFont(self) -> Font:
        """ Get: MenuFont() -> Font """
        ...

    @property
    def MessageBoxFont(self) -> Font:
        """ Get: MessageBoxFont() -> Font """
        ...

    @property
    def SmallCaptionFont(self) -> Font:
        """ Get: SmallCaptionFont() -> Font """
        ...

    @property
    def StatusFont(self) -> Font:
        """ Get: StatusFont() -> Font """
        ...


    @staticmethod
    def GetFontByName(systemFontName:str) -> Font:
        """ GetFontByName(systemFontName: str) -> Font """
        ...



class SystemIcons: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Application(self) -> Icon:
        """ Get: Application() -> Icon """
        ...

    @property
    def Asterisk(self) -> Icon:
        """ Get: Asterisk() -> Icon """
        ...

    @property
    def Error(self) -> Icon:
        """ Get: Error() -> Icon """
        ...

    @property
    def Exclamation(self) -> Icon:
        """ Get: Exclamation() -> Icon """
        ...

    @property
    def Hand(self) -> Icon:
        """ Get: Hand() -> Icon """
        ...

    @property
    def Information(self) -> Icon:
        """ Get: Information() -> Icon """
        ...

    @property
    def Question(self) -> Icon:
        """ Get: Question() -> Icon """
        ...

    @property
    def Shield(self) -> Icon:
        """ Get: Shield() -> Icon """
        ...

    @property
    def Warning(self) -> Icon:
        """ Get: Warning() -> Icon """
        ...

    @property
    def WinLogo(self) -> Icon:
        """ Get: WinLogo() -> Icon """
        ...




class SystemPens: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ActiveBorder(self) -> Pen:
        """ Get: ActiveBorder() -> Pen """
        ...

    @property
    def ActiveCaption(self) -> Pen:
        """ Get: ActiveCaption() -> Pen """
        ...

    @property
    def ActiveCaptionText(self) -> Pen:
        """ Get: ActiveCaptionText() -> Pen """
        ...

    @property
    def AppWorkspace(self) -> Pen:
        """ Get: AppWorkspace() -> Pen """
        ...

    @property
    def ButtonFace(self) -> Pen:
        """ Get: ButtonFace() -> Pen """
        ...

    @property
    def ButtonHighlight(self) -> Pen:
        """ Get: ButtonHighlight() -> Pen """
        ...

    @property
    def ButtonShadow(self) -> Pen:
        """ Get: ButtonShadow() -> Pen """
        ...

    @property
    def Control(self) -> Pen:
        """ Get: Control() -> Pen """
        ...

    @property
    def ControlDark(self) -> Pen:
        """ Get: ControlDark() -> Pen """
        ...

    @property
    def ControlDarkDark(self) -> Pen:
        """ Get: ControlDarkDark() -> Pen """
        ...

    @property
    def ControlLight(self) -> Pen:
        """ Get: ControlLight() -> Pen """
        ...

    @property
    def ControlLightLight(self) -> Pen:
        """ Get: ControlLightLight() -> Pen """
        ...

    @property
    def ControlText(self) -> Pen:
        """ Get: ControlText() -> Pen """
        ...

    @property
    def Desktop(self) -> Pen:
        """ Get: Desktop() -> Pen """
        ...

    @property
    def GradientActiveCaption(self) -> Pen:
        """ Get: GradientActiveCaption() -> Pen """
        ...

    @property
    def GradientInactiveCaption(self) -> Pen:
        """ Get: GradientInactiveCaption() -> Pen """
        ...

    @property
    def GrayText(self) -> Pen:
        """ Get: GrayText() -> Pen """
        ...

    @property
    def Highlight(self) -> Pen:
        """ Get: Highlight() -> Pen """
        ...

    @property
    def HighlightText(self) -> Pen:
        """ Get: HighlightText() -> Pen """
        ...

    @property
    def HotTrack(self) -> Pen:
        """ Get: HotTrack() -> Pen """
        ...

    @property
    def InactiveBorder(self) -> Pen:
        """ Get: InactiveBorder() -> Pen """
        ...

    @property
    def InactiveCaption(self) -> Pen:
        """ Get: InactiveCaption() -> Pen """
        ...

    @property
    def InactiveCaptionText(self) -> Pen:
        """ Get: InactiveCaptionText() -> Pen """
        ...

    @property
    def Info(self) -> Pen:
        """ Get: Info() -> Pen """
        ...

    @property
    def InfoText(self) -> Pen:
        """ Get: InfoText() -> Pen """
        ...

    @property
    def Menu(self) -> Pen:
        """ Get: Menu() -> Pen """
        ...

    @property
    def MenuBar(self) -> Pen:
        """ Get: MenuBar() -> Pen """
        ...

    @property
    def MenuHighlight(self) -> Pen:
        """ Get: MenuHighlight() -> Pen """
        ...

    @property
    def MenuText(self) -> Pen:
        """ Get: MenuText() -> Pen """
        ...

    @property
    def ScrollBar(self) -> Pen:
        """ Get: ScrollBar() -> Pen """
        ...

    @property
    def Window(self) -> Pen:
        """ Get: Window() -> Pen """
        ...

    @property
    def WindowFrame(self) -> Pen:
        """ Get: WindowFrame() -> Pen """
        ...

    @property
    def WindowText(self) -> Pen:
        """ Get: WindowText() -> Pen """
        ...


    @staticmethod
    def FromSystemColor(c:Color) -> Pen:
        """ FromSystemColor(c: Color) -> Pen """
        ...



class TextureBrush(Brush): # skipped bases: <type 'IDisposable'>, <type 'ICloneable'>, <type 'object'>
    """
    TextureBrush(bitmap: Image)
    TextureBrush(image: Image, wrapMode: WrapMode)
    TextureBrush(image: Image, wrapMode: WrapMode, dstRect: RectangleF)
    TextureBrush(image: Image, wrapMode: WrapMode, dstRect: Rectangle)
    TextureBrush(image: Image, dstRect: RectangleF)
    TextureBrush(image: Image, dstRect: RectangleF, imageAttr: ImageAttributes)
    TextureBrush(image: Image, dstRect: Rectangle)
    TextureBrush(image: Image, dstRect: Rectangle, imageAttr: ImageAttributes)
    """
    @property
    def Image(self) -> Image:
        """ Get: Image(self: TextureBrush) -> Image """
        ...

    @property
    def Transform(self) -> Matrix:
        """
        Get: Transform(self: TextureBrush) -> Matrix
        Set: Transform(self: TextureBrush) = value
        """
        ...

    @property
    def WrapMode(self) -> WrapMode:
        """
        Get: WrapMode(self: TextureBrush) -> WrapMode
        Set: WrapMode(self: TextureBrush) = value
        """
        ...


    def MultiplyTransform(self, matrix:Matrix, order:MatrixOrder = ...): # -> 
        """ MultiplyTransform(self: TextureBrush, matrix: Matrix)MultiplyTransform(self: TextureBrush, matrix: Matrix, order: MatrixOrder) """
        ...

    def ResetTransform(self): # -> 
        """ ResetTransform(self: TextureBrush) """
        ...

    def RotateTransform(self, angle:Single, order:MatrixOrder = ...): # -> 
        """ RotateTransform(self: TextureBrush, angle: Single)RotateTransform(self: TextureBrush, angle: Single, order: MatrixOrder) """
        ...

    def ScaleTransform(self, sx:Single, sy:Single, order:MatrixOrder = ...): # -> 
        """ ScaleTransform(self: TextureBrush, sx: Single, sy: Single)ScaleTransform(self: TextureBrush, sx: Single, sy: Single, order: MatrixOrder) """
        ...

    def TranslateTransform(self, dx:Single, dy:Single, order:MatrixOrder = ...): # -> 
        """ TranslateTransform(self: TextureBrush, dx: Single, dy: Single)TranslateTransform(self: TextureBrush, dx: Single, dy: Single, order: MatrixOrder) """
        ...

    def __new__(cls, *__args:Image) -> Self:
        """
        __new__(cls: type, bitmap: Image)
        __new__(cls: type, image: Image, wrapMode: WrapMode)
        __new__(cls: type, image: Image, wrapMode: WrapMode, dstRect: RectangleF)
        __new__(cls: type, image: Image, wrapMode: WrapMode, dstRect: Rectangle)
        __new__(cls: type, image: Image, dstRect: RectangleF)
        __new__(cls: type, image: Image, dstRect: RectangleF, imageAttr: ImageAttributes)
        __new__(cls: type, image: Image, dstRect: Rectangle)
        __new__(cls: type, image: Image, dstRect: Rectangle, imageAttr: ImageAttributes)
        """
        ...


class ToolboxBitmapAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ToolboxBitmapAttribute(imageFile: str)
    ToolboxBitmapAttribute(t: Type)
    ToolboxBitmapAttribute(t: Type, name: str)
    """
    def GetImage(self, *__args:object) -> Image:
        """
        GetImage(self: ToolboxBitmapAttribute, component: object) -> Image
        GetImage(self: ToolboxBitmapAttribute, component: object, large: bool) -> Image
        GetImage(self: ToolboxBitmapAttribute, type: Type) -> Image
        GetImage(self: ToolboxBitmapAttribute, type: Type, large: bool) -> Image
        GetImage(self: ToolboxBitmapAttribute, type: Type, imgName: str, large: bool) -> Image
        """
        ...

    @staticmethod
    def GetImageFromResource(t:Type, imageName:str, large:bool) -> Image:
        """ GetImageFromResource(t: Type, imageName: str, large: bool) -> Image """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, imageFile: str)
        __new__(cls: type, t: Type)
        __new__(cls: type, t: Type, name: str)
        """
        ...

    Default: ToolboxBitmapAttribute = ...


# variables with complex values

