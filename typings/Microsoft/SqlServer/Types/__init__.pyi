# encoding: utf-8
# module Microsoft.SqlServer.Types calls itself Types
# from Microsoft.SqlServer.Types, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Server import IBinarySerialize

from System import (Array, Byte, Enum, IComparable, Int16, Nullable, UInt32, 
    UInt64)

from System.Collections import IEnumerable

from System.Data.SqlTypes import (INullable, SqlBoolean, SqlBytes, SqlChars, 
    SqlDouble, SqlInt16, SqlInt32, SqlString, SqlXml)

from typing import Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, IAggregate, 
    field#)
"""

# no functions
# classes

class GeographyCollectionAggregate(IBinarySerialize, IAggregate): # skipped bases: <type 'object'>
    """ GeographyCollectionAggregate() """
    def Accumulate(self, g:SqlGeography): # -> 
        """ Accumulate(self: GeographyCollectionAggregate, g: SqlGeography) """
        ...

    def Init(self): # -> 
        """ Init(self: GeographyCollectionAggregate) """
        ...

    def Merge(self, group:GeographyCollectionAggregate): # -> 
        """ Merge(self: GeographyCollectionAggregate, group: GeographyCollectionAggregate) """
        ...

    def Terminate(self) -> SqlGeography:
        """ Terminate(self: GeographyCollectionAggregate) -> SqlGeography """
        ...


class GeographyConvexHullAggregate(IBinarySerialize, IAggregate): # skipped bases: <type 'object'>
    """ GeographyConvexHullAggregate() """
    def Accumulate(self, g:SqlGeography): # -> 
        """ Accumulate(self: GeographyConvexHullAggregate, g: SqlGeography) """
        ...

    def Init(self): # -> 
        """ Init(self: GeographyConvexHullAggregate) """
        ...

    def Merge(self, group:GeographyConvexHullAggregate): # -> 
        """ Merge(self: GeographyConvexHullAggregate, group: GeographyConvexHullAggregate) """
        ...

    def Terminate(self) -> SqlGeography:
        """ Terminate(self: GeographyConvexHullAggregate) -> SqlGeography """
        ...


class GeographyEnvelopeAggregate(IAggregate): # skipped bases: <type 'object'>
    """ GeographyEnvelopeAggregate() """
    def Accumulate(self, g:SqlGeography): # -> 
        """ Accumulate(self: GeographyEnvelopeAggregate, g: SqlGeography) """
        ...

    def Init(self): # -> 
        """ Init(self: GeographyEnvelopeAggregate) """
        ...

    def Merge(self, group:GeographyEnvelopeAggregate): # -> 
        """ Merge(self: GeographyEnvelopeAggregate, group: GeographyEnvelopeAggregate) """
        ...

    def Terminate(self) -> SqlGeography:
        """ Terminate(self: GeographyEnvelopeAggregate) -> SqlGeography """
        ...


class GeographyTessellationFunction: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FillRow(obj, cellId, cellAttributes, spatialReferenceId) -> Tuple_[SqlBytes, Int16, int]:
        """ FillRow(obj: object) -> (SqlBytes, Int16, int) """
        ...

    @staticmethod
    def InitMethod(geographyObject:SqlGeography, densityGrid0:int, densityGrid1:int, densityGrid2:int, densityGrid3:int, cardinality:int, tessellationMode:int, distanceBuffer:SqlDouble) -> IEnumerable:
        """ InitMethod(geographyObject: SqlGeography, densityGrid0: int, densityGrid1: int, densityGrid2: int, densityGrid3: int, cardinality: int, tessellationMode: int, distanceBuffer: SqlDouble) -> IEnumerable """
        ...


class GeographyUnionAggregate(IBinarySerialize, IAggregate): # skipped bases: <type 'object'>
    """ GeographyUnionAggregate() """
    def Accumulate(self, g:SqlGeography): # -> 
        """ Accumulate(self: GeographyUnionAggregate, g: SqlGeography) """
        ...

    def Init(self): # -> 
        """ Init(self: GeographyUnionAggregate) """
        ...

    def Merge(self, group:GeographyUnionAggregate): # -> 
        """ Merge(self: GeographyUnionAggregate, group: GeographyUnionAggregate) """
        ...

    def Terminate(self) -> SqlGeography:
        """ Terminate(self: GeographyUnionAggregate) -> SqlGeography """
        ...


class GeometryCollectionAggregate(IBinarySerialize, IAggregate): # skipped bases: <type 'object'>
    """ GeometryCollectionAggregate() """
    def Accumulate(self, g:SqlGeometry): # -> 
        """ Accumulate(self: GeometryCollectionAggregate, g: SqlGeometry) """
        ...

    def Init(self): # -> 
        """ Init(self: GeometryCollectionAggregate) """
        ...

    def Merge(self, group:GeometryCollectionAggregate): # -> 
        """ Merge(self: GeometryCollectionAggregate, group: GeometryCollectionAggregate) """
        ...

    def Terminate(self) -> SqlGeometry:
        """ Terminate(self: GeometryCollectionAggregate) -> SqlGeometry """
        ...


class GeometryConvexHullAggregate(IBinarySerialize, IAggregate): # skipped bases: <type 'object'>
    """ GeometryConvexHullAggregate() """
    def Accumulate(self, g:SqlGeometry): # -> 
        """ Accumulate(self: GeometryConvexHullAggregate, g: SqlGeometry) """
        ...

    def Init(self): # -> 
        """ Init(self: GeometryConvexHullAggregate) """
        ...

    def Merge(self, group:GeometryConvexHullAggregate): # -> 
        """ Merge(self: GeometryConvexHullAggregate, group: GeometryConvexHullAggregate) """
        ...

    def Terminate(self) -> SqlGeometry:
        """ Terminate(self: GeometryConvexHullAggregate) -> SqlGeometry """
        ...


class GeometryEnvelopeAggregate(IAggregate): # skipped bases: <type 'object'>
    """ GeometryEnvelopeAggregate() """
    def Accumulate(self, g:SqlGeometry): # -> 
        """ Accumulate(self: GeometryEnvelopeAggregate, g: SqlGeometry) """
        ...

    def Init(self): # -> 
        """ Init(self: GeometryEnvelopeAggregate) """
        ...

    def Merge(self, group:GeometryEnvelopeAggregate): # -> 
        """ Merge(self: GeometryEnvelopeAggregate, group: GeometryEnvelopeAggregate) """
        ...

    def Terminate(self) -> SqlGeometry:
        """ Terminate(self: GeometryEnvelopeAggregate) -> SqlGeometry """
        ...


class GeometryTessellationFunction: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def FillRow(obj, cellId, cellAttributes, spatialReferenceId) -> Tuple_[SqlBytes, Int16, int]:
        """ FillRow(obj: object) -> (SqlBytes, Int16, int) """
        ...

    @staticmethod
    def InitMethod(geometryObject:SqlGeometry, rootX:float, rootY:float, maxX:float, maxY:float, densityGrid0:int, densityGrid1:int, densityGrid2:int, densityGrid3:int, cardinality:int, tessellationMode:int, distanceBuffer:SqlDouble) -> IEnumerable:
        """ InitMethod(geometryObject: SqlGeometry, rootX: float, rootY: float, maxX: float, maxY: float, densityGrid0: int, densityGrid1: int, densityGrid2: int, densityGrid3: int, cardinality: int, tessellationMode: int, distanceBuffer: SqlDouble) -> IEnumerable """
        ...


class GeometryUnionAggregate(IBinarySerialize, IAggregate): # skipped bases: <type 'object'>
    """ GeometryUnionAggregate() """
    def Accumulate(self, g:SqlGeometry): # -> 
        """ Accumulate(self: GeometryUnionAggregate, g: SqlGeometry) """
        ...

    def Init(self): # -> 
        """ Init(self: GeometryUnionAggregate) """
        ...

    def Merge(self, group:GeometryUnionAggregate): # -> 
        """ Merge(self: GeometryUnionAggregate, group: GeometryUnionAggregate) """
        ...

    def Terminate(self) -> SqlGeometry:
        """ Terminate(self: GeometryUnionAggregate) -> SqlGeometry """
        ...


class HierarchyIdException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    HierarchyIdException(message: str, innerException: Exception)
    HierarchyIdException(message: str)
    HierarchyIdException()
    """
    SerializeObjectState = ...


class IGeographySink: # skipped bases: <type 'object'>
    """ no doc """
    def AddLine(self, latitude:float, longitude:float, z:Nullable, m:Nullable): # -> 
        """ AddLine(self: IGeographySink, latitude: float, longitude: float, z: Nullable[float], m: Nullable[float]) """
        ...

    def BeginFigure(self, latitude:float, longitude:float, z:Nullable, m:Nullable): # -> 
        """ BeginFigure(self: IGeographySink, latitude: float, longitude: float, z: Nullable[float], m: Nullable[float]) """
        ...

    def BeginGeography(self, type:OpenGisGeographyType): # -> 
        """ BeginGeography(self: IGeographySink, type: OpenGisGeographyType) """
        ...

    def EndFigure(self): # -> 
        """ EndFigure(self: IGeographySink) """
        ...

    def EndGeography(self): # -> 
        """ EndGeography(self: IGeographySink) """
        ...

    def SetSrid(self, srid:int): # -> 
        """ SetSrid(self: IGeographySink, srid: int) """
        ...


class IGeographySink110(IGeographySink): # skipped bases: <type 'object'>
    """ no doc """
    def AddCircularArc(self, x1:float, y1:float, z1:Nullable, m1:Nullable, x2:float, y2:float, z2:Nullable, m2:Nullable): # -> 
        """ AddCircularArc(self: IGeographySink110, x1: float, y1: float, z1: Nullable[float], m1: Nullable[float], x2: float, y2: float, z2: Nullable[float], m2: Nullable[float]) """
        ...


class IGeometrySink: # skipped bases: <type 'object'>
    """ no doc """
    def AddLine(self, x:float, y:float, z:Nullable, m:Nullable): # -> 
        """ AddLine(self: IGeometrySink, x: float, y: float, z: Nullable[float], m: Nullable[float]) """
        ...

    def BeginFigure(self, x:float, y:float, z:Nullable, m:Nullable): # -> 
        """ BeginFigure(self: IGeometrySink, x: float, y: float, z: Nullable[float], m: Nullable[float]) """
        ...

    def BeginGeometry(self, type:OpenGisGeometryType): # -> 
        """ BeginGeometry(self: IGeometrySink, type: OpenGisGeometryType) """
        ...

    def EndFigure(self): # -> 
        """ EndFigure(self: IGeometrySink) """
        ...

    def EndGeometry(self): # -> 
        """ EndGeometry(self: IGeometrySink) """
        ...

    def SetSrid(self, srid:int): # -> 
        """ SetSrid(self: IGeometrySink, srid: int) """
        ...


class IGeometrySink110(IGeometrySink): # skipped bases: <type 'object'>
    """ no doc """
    def AddCircularArc(self, x1:float, y1:float, z1:Nullable, m1:Nullable, x2:float, y2:float, z2:Nullable, m2:Nullable): # -> 
        """ AddCircularArc(self: IGeometrySink110, x1: float, y1: float, z1: Nullable[float], m1: Nullable[float], x2: float, y2: float, z2: Nullable[float], m2: Nullable[float]) """
        ...


class ISqlSpatialGridIndexable: # skipped bases: <type 'object'>
    """ no doc """
    def BufferForDistanceQuery(self, distance, disableInternalFiltering) -> Tuple_[ISqlSpatialGridIndexable, bool]:
        """ BufferForDistanceQuery(self: ISqlSpatialGridIndexable, distance: float) -> (ISqlSpatialGridIndexable, bool) """
        ...

    def GetBoundingBoxCorners(self, minX, minY, maxX, maxY) -> Tuple_[float, float, float, float]:
        """ GetBoundingBoxCorners(self: ISqlSpatialGridIndexable) -> (float, float, float, float) """
        ...

    def GetGridCoverage(self, isTopmostGrid, rGridMinX, rGridMinY, rGridWidth, rGridHeight, rFuzzX, rFuzzY, cGridRows, cGridColumns, touched, contained, cCellsTouched, cCellsContained, fGeometryExceedsGrid, fHasAmbiguousTouchedCells) -> Tuple_[int, int, bool, bool]:
        """ GetGridCoverage(self: ISqlSpatialGridIndexable, isTopmostGrid: bool, rGridMinX: float, rGridMinY: float, rGridWidth: float, rGridHeight: float, rFuzzX: float, rFuzzY: float, cGridRows: int, cGridColumns: int, touched: Array[bool], contained: Array[bool]) -> (int, int, bool, bool) """
        ...

    def InteriorBufferForDistanceQuery(self, distance:float) -> ISqlSpatialGridIndexable:
        """ InteriorBufferForDistanceQuery(self: ISqlSpatialGridIndexable, distance: float) -> ISqlSpatialGridIndexable """
        ...


class OpenGisGeographyType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OpenGisGeographyType, values: CircularString (8), CompoundCurve (9), CurvePolygon (10), FullGlobe (11), GeometryCollection (7), LineString (2), MultiLineString (5), MultiPoint (4), MultiPolygon (6), Point (1), Polygon (3) """
    CircularString: OpenGisGeographyType = ...
    CompoundCurve: OpenGisGeographyType = ...
    CurvePolygon: OpenGisGeographyType = ...
    FullGlobe: OpenGisGeographyType = ...
    GeometryCollection: OpenGisGeographyType = ...
    LineString: OpenGisGeographyType = ...
    MultiLineString: OpenGisGeographyType = ...
    MultiPoint: OpenGisGeographyType = ...
    MultiPolygon: OpenGisGeographyType = ...
    Point: OpenGisGeographyType = ...
    Polygon: OpenGisGeographyType = ...
    value__ = ...


class OpenGisGeometryType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OpenGisGeometryType, values: CircularString (8), CompoundCurve (9), CurvePolygon (10), GeometryCollection (7), LineString (2), MultiLineString (5), MultiPoint (4), MultiPolygon (6), Point (1), Polygon (3) """
    CircularString: OpenGisGeometryType = ...
    CompoundCurve: OpenGisGeometryType = ...
    CurvePolygon: OpenGisGeometryType = ...
    GeometryCollection: OpenGisGeometryType = ...
    LineString: OpenGisGeometryType = ...
    MultiLineString: OpenGisGeometryType = ...
    MultiPoint: OpenGisGeometryType = ...
    MultiPolygon: OpenGisGeometryType = ...
    Point: OpenGisGeometryType = ...
    Polygon: OpenGisGeometryType = ...
    value__ = ...


class SpaceFillingCurve: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Hilbert(order:int, x:UInt32, y:UInt32) -> UInt64:
        """ Hilbert(order: int, x: UInt32, y: UInt32) -> UInt64 """
        ...

    @staticmethod
    def ReverseHilbert(order, hilbert, ox, oy) -> Tuple_[UInt32, UInt32]:
        """ ReverseHilbert(order: int, hilbert: UInt64) -> (UInt32, UInt32) """
        ...

    __all__: list = ...


class SpatialGridCoverage: # skipped bases: <type 'object'>, <type 'object'>
    """ SpatialGridCoverage() """
    @staticmethod
    def FillRow(obj, id, attribute, wkb) -> Tuple_[int, Byte, Array]:
        """ FillRow(obj: object) -> (int, Byte, Array[Byte]) """
        ...

    @staticmethod
    def Geodetic(geography:SqlGeography, rows:int, columns:int) -> IEnumerable:
        """ Geodetic(geography: SqlGeography, rows: int, columns: int) -> IEnumerable """
        ...

    @staticmethod
    def Planar(geometry:SqlGeometry, rootX:float, rootY:float, maxX:float, maxY:float, rows:int, columns:int) -> IEnumerable:
        """ Planar(geometry: SqlGeometry, rootX: float, rootY: float, maxX: float, maxY: float, rows: int, columns: int) -> IEnumerable """
        ...


class SpatialTessellationFunction: # skipped bases: <type 'object'>, <type 'object'>
    """ SpatialTessellationFunction() """
    @staticmethod
    def FillRow(obj, cellId, cellAttributes, cellIdLimit, wkbCoverage) -> Tuple_[Array, Byte, Array, Array]:
        """ FillRow(obj: object) -> (Array[Byte], Byte, Array[Byte], Array[Byte]) """
        ...

    @staticmethod
    def Geodetic(geography:SqlGeography, cardinality:int, maxDepth:int, options:int, distanceBuffer:SqlDouble) -> IEnumerable:
        """ Geodetic(geography: SqlGeography, cardinality: int, maxDepth: int, options: int, distanceBuffer: SqlDouble) -> IEnumerable """
        ...

    @staticmethod
    def GetAttribute(obj:object) -> int:
        """ GetAttribute(obj: object) -> int """
        ...

    @staticmethod
    def GetCoverage(obj:object) -> SqlGeometry:
        """ GetCoverage(obj: object) -> SqlGeometry """
        ...

    @staticmethod
    def GetId(obj:object) -> str:
        """ GetId(obj: object) -> str """
        ...

    @staticmethod
    def GetIsAncestor(obj:object) -> bool:
        """ GetIsAncestor(obj: object) -> bool """
        ...

    @staticmethod
    def Planar(geometry:SqlGeometry, rootX:float, rootY:float, maxX:float, maxY:float, cardinality:int, maxDepth:int, options:int, distanceBuffer:SqlDouble) -> IEnumerable:
        """ Planar(geometry: SqlGeometry, rootX: float, rootY: float, maxX: float, maxY: float, cardinality: int, maxDepth: int, options: int, distanceBuffer: SqlDouble) -> IEnumerable """
        ...


class SqlGeography(ISqlSpatialGridIndexable, IBinarySerialize, INullable): # skipped bases: <type 'object'>
    """ SqlGeography() """
    @property
    def HasM(self) -> bool:
        """ Get: HasM(self: SqlGeography) -> bool """
        ...

    @property
    def HasZ(self) -> bool:
        """ Get: HasZ(self: SqlGeography) -> bool """
        ...

    @property
    def Lat(self) -> SqlDouble:
        """ Get: Lat(self: SqlGeography) -> SqlDouble """
        ...

    @property
    def Long(self) -> SqlDouble:
        """ Get: Long(self: SqlGeography) -> SqlDouble """
        ...

    @property
    def M(self) -> SqlDouble:
        """ Get: M(self: SqlGeography) -> SqlDouble """
        ...

    @property
    def Null(self) -> SqlGeography:
        """ Get: Null() -> SqlGeography """
        ...

    @property
    def STSrid(self) -> SqlInt32:
        """
        Get: STSrid(self: SqlGeography) -> SqlInt32
        Set: STSrid(self: SqlGeography) = value
        """
        ...

    @property
    def Z(self) -> SqlDouble:
        """ Get: Z(self: SqlGeography) -> SqlDouble """
        ...


    def AsBinaryZM(self) -> SqlBytes:
        """ AsBinaryZM(self: SqlGeography) -> SqlBytes """
        ...

    def AsGml(self) -> SqlXml:
        """ AsGml(self: SqlGeography) -> SqlXml """
        ...

    def AsTextZM(self) -> SqlChars:
        """ AsTextZM(self: SqlGeography) -> SqlChars """
        ...

    def BufferWithCurves(self, distance:float) -> SqlGeography:
        """ BufferWithCurves(self: SqlGeography, distance: float) -> SqlGeography """
        ...

    def BufferWithTolerance(self, distance:float, tolerance:float, relative:bool) -> SqlGeography:
        """ BufferWithTolerance(self: SqlGeography, distance: float, tolerance: float, relative: bool) -> SqlGeography """
        ...

    def CurveToLineWithTolerance(self, tolerance:float, relative:bool) -> SqlGeography:
        """ CurveToLineWithTolerance(self: SqlGeography, tolerance: float, relative: bool) -> SqlGeography """
        ...

    @staticmethod
    def Deserialize(bytes:SqlBytes) -> SqlGeography:
        """ Deserialize(bytes: SqlBytes) -> SqlGeography """
        ...

    def EnvelopeAngle(self) -> SqlDouble:
        """ EnvelopeAngle(self: SqlGeography) -> SqlDouble """
        ...

    def EnvelopeCenter(self) -> SqlGeography:
        """ EnvelopeCenter(self: SqlGeography) -> SqlGeography """
        ...

    def Filter(self, other:SqlGeography) -> SqlBoolean:
        """ Filter(self: SqlGeography, other: SqlGeography) -> SqlBoolean """
        ...

    @staticmethod
    def GeomFromGml(xml:SqlXml, srid:int) -> SqlGeography:
        """ GeomFromGml(xml: SqlXml, srid: int) -> SqlGeography """
        ...

    def InstanceOf(self, geometryType:str) -> SqlBoolean:
        """ InstanceOf(self: SqlGeography, geometryType: str) -> SqlBoolean """
        ...

    def IsValidDetailed(self) -> str:
        """ IsValidDetailed(self: SqlGeography) -> str """
        ...

    def MakeValid(self) -> SqlGeography:
        """ MakeValid(self: SqlGeography) -> SqlGeography """
        ...

    def MinDbCompatibilityLevel(self) -> int:
        """ MinDbCompatibilityLevel(self: SqlGeography) -> int """
        ...

    def NumRings(self) -> SqlInt32:
        """ NumRings(self: SqlGeography) -> SqlInt32 """
        ...

    @staticmethod
    def Parse(s:SqlString) -> SqlGeography:
        """ Parse(s: SqlString) -> SqlGeography """
        ...

    @staticmethod
    def Point(latitude:float, longitude:float, srid:int) -> SqlGeography:
        """ Point(latitude: float, longitude: float, srid: int) -> SqlGeography """
        ...

    def Populate(self, sink:IGeographySink): # -> 
        """ Populate(self: SqlGeography, sink: IGeographySink)Populate(self: SqlGeography, sink: IGeographySink110) """
        ...

    def Reduce(self, tolerance:float) -> SqlGeography:
        """ Reduce(self: SqlGeography, tolerance: float) -> SqlGeography """
        ...

    def ReorientObject(self) -> SqlGeography:
        """ ReorientObject(self: SqlGeography) -> SqlGeography """
        ...

    def RingN(self, n:int) -> SqlGeography:
        """ RingN(self: SqlGeography, n: int) -> SqlGeography """
        ...

    def Serialize(self) -> SqlBytes:
        """ Serialize(self: SqlGeography) -> SqlBytes """
        ...

    def ShortestLineTo(self, other:SqlGeography) -> SqlGeography:
        """ ShortestLineTo(self: SqlGeography, other: SqlGeography) -> SqlGeography """
        ...

    def STArea(self) -> SqlDouble:
        """ STArea(self: SqlGeography) -> SqlDouble """
        ...

    def STAsBinary(self) -> SqlBytes:
        """ STAsBinary(self: SqlGeography) -> SqlBytes """
        ...

    def STAsText(self) -> SqlChars:
        """ STAsText(self: SqlGeography) -> SqlChars """
        ...

    def STBuffer(self, distance:float) -> SqlGeography:
        """ STBuffer(self: SqlGeography, distance: float) -> SqlGeography """
        ...

    def STContains(self, other:SqlGeography) -> SqlBoolean:
        """ STContains(self: SqlGeography, other: SqlGeography) -> SqlBoolean """
        ...

    def STConvexHull(self) -> SqlGeography:
        """ STConvexHull(self: SqlGeography) -> SqlGeography """
        ...

    def STCurveN(self, n:int) -> SqlGeography:
        """ STCurveN(self: SqlGeography, n: int) -> SqlGeography """
        ...

    def STCurveToLine(self) -> SqlGeography:
        """ STCurveToLine(self: SqlGeography) -> SqlGeography """
        ...

    def STDifference(self, other:SqlGeography) -> SqlGeography:
        """ STDifference(self: SqlGeography, other: SqlGeography) -> SqlGeography """
        ...

    def STDimension(self) -> SqlInt32:
        """ STDimension(self: SqlGeography) -> SqlInt32 """
        ...

    def STDisjoint(self, other:SqlGeography) -> SqlBoolean:
        """ STDisjoint(self: SqlGeography, other: SqlGeography) -> SqlBoolean """
        ...

    def STDistance(self, other:SqlGeography) -> SqlDouble:
        """ STDistance(self: SqlGeography, other: SqlGeography) -> SqlDouble """
        ...

    def STEndPoint(self) -> SqlGeography:
        """ STEndPoint(self: SqlGeography) -> SqlGeography """
        ...

    def STEquals(self, other:SqlGeography) -> SqlBoolean:
        """ STEquals(self: SqlGeography, other: SqlGeography) -> SqlBoolean """
        ...

    @staticmethod
    def STGeomCollFromText(geometryCollectionTaggedText:SqlChars, srid:int) -> SqlGeography:
        """ STGeomCollFromText(geometryCollectionTaggedText: SqlChars, srid: int) -> SqlGeography """
        ...

    @staticmethod
    def STGeomCollFromWKB(wkbGeometryCollection:SqlBytes, srid:int) -> SqlGeography:
        """ STGeomCollFromWKB(wkbGeometryCollection: SqlBytes, srid: int) -> SqlGeography """
        ...

    def STGeometryN(self, n:int) -> SqlGeography:
        """ STGeometryN(self: SqlGeography, n: int) -> SqlGeography """
        ...

    def STGeometryType(self) -> SqlString:
        """ STGeometryType(self: SqlGeography) -> SqlString """
        ...

    @staticmethod
    def STGeomFromText(geometryTaggedText:SqlChars, srid:int) -> SqlGeography:
        """ STGeomFromText(geometryTaggedText: SqlChars, srid: int) -> SqlGeography """
        ...

    @staticmethod
    def STGeomFromWKB(wkbGeometry:SqlBytes, srid:int) -> SqlGeography:
        """ STGeomFromWKB(wkbGeometry: SqlBytes, srid: int) -> SqlGeography """
        ...

    def STIntersection(self, other:SqlGeography) -> SqlGeography:
        """ STIntersection(self: SqlGeography, other: SqlGeography) -> SqlGeography """
        ...

    def STIntersects(self, other:SqlGeography) -> SqlBoolean:
        """ STIntersects(self: SqlGeography, other: SqlGeography) -> SqlBoolean """
        ...

    def STIsClosed(self) -> SqlBoolean:
        """ STIsClosed(self: SqlGeography) -> SqlBoolean """
        ...

    def STIsEmpty(self) -> SqlBoolean:
        """ STIsEmpty(self: SqlGeography) -> SqlBoolean """
        ...

    def STIsValid(self) -> SqlBoolean:
        """ STIsValid(self: SqlGeography) -> SqlBoolean """
        ...

    def STLength(self) -> SqlDouble:
        """ STLength(self: SqlGeography) -> SqlDouble """
        ...

    @staticmethod
    def STLineFromText(lineStringTaggedText:SqlChars, srid:int) -> SqlGeography:
        """ STLineFromText(lineStringTaggedText: SqlChars, srid: int) -> SqlGeography """
        ...

    @staticmethod
    def STLineFromWKB(wkbLineString:SqlBytes, srid:int) -> SqlGeography:
        """ STLineFromWKB(wkbLineString: SqlBytes, srid: int) -> SqlGeography """
        ...

    @staticmethod
    def STMLineFromText(multiLineStringTaggedText:SqlChars, srid:int) -> SqlGeography:
        """ STMLineFromText(multiLineStringTaggedText: SqlChars, srid: int) -> SqlGeography """
        ...

    @staticmethod
    def STMLineFromWKB(wkbMultiLineString:SqlBytes, srid:int) -> SqlGeography:
        """ STMLineFromWKB(wkbMultiLineString: SqlBytes, srid: int) -> SqlGeography """
        ...

    @staticmethod
    def STMPointFromText(multiPointTaggedText:SqlChars, srid:int) -> SqlGeography:
        """ STMPointFromText(multiPointTaggedText: SqlChars, srid: int) -> SqlGeography """
        ...

    @staticmethod
    def STMPointFromWKB(wkbMultiPoint:SqlBytes, srid:int) -> SqlGeography:
        """ STMPointFromWKB(wkbMultiPoint: SqlBytes, srid: int) -> SqlGeography """
        ...

    @staticmethod
    def STMPolyFromText(multiPolygonTaggedText:SqlChars, srid:int) -> SqlGeography:
        """ STMPolyFromText(multiPolygonTaggedText: SqlChars, srid: int) -> SqlGeography """
        ...

    @staticmethod
    def STMPolyFromWKB(wkbMultiPolygon:SqlBytes, srid:int) -> SqlGeography:
        """ STMPolyFromWKB(wkbMultiPolygon: SqlBytes, srid: int) -> SqlGeography """
        ...

    def STNumCurves(self) -> SqlInt32:
        """ STNumCurves(self: SqlGeography) -> SqlInt32 """
        ...

    def STNumGeometries(self) -> SqlInt32:
        """ STNumGeometries(self: SqlGeography) -> SqlInt32 """
        ...

    def STNumPoints(self) -> SqlInt32:
        """ STNumPoints(self: SqlGeography) -> SqlInt32 """
        ...

    def STOverlaps(self, other:SqlGeography) -> SqlBoolean:
        """ STOverlaps(self: SqlGeography, other: SqlGeography) -> SqlBoolean """
        ...

    @staticmethod
    def STPointFromText(pointTaggedText:SqlChars, srid:int) -> SqlGeography:
        """ STPointFromText(pointTaggedText: SqlChars, srid: int) -> SqlGeography """
        ...

    @staticmethod
    def STPointFromWKB(wkbPoint:SqlBytes, srid:int) -> SqlGeography:
        """ STPointFromWKB(wkbPoint: SqlBytes, srid: int) -> SqlGeography """
        ...

    def STPointN(self, n:int) -> SqlGeography:
        """ STPointN(self: SqlGeography, n: int) -> SqlGeography """
        ...

    @staticmethod
    def STPolyFromText(polygonTaggedText:SqlChars, srid:int) -> SqlGeography:
        """ STPolyFromText(polygonTaggedText: SqlChars, srid: int) -> SqlGeography """
        ...

    @staticmethod
    def STPolyFromWKB(wkbPolygon:SqlBytes, srid:int) -> SqlGeography:
        """ STPolyFromWKB(wkbPolygon: SqlBytes, srid: int) -> SqlGeography """
        ...

    def STStartPoint(self) -> SqlGeography:
        """ STStartPoint(self: SqlGeography) -> SqlGeography """
        ...

    def STSymDifference(self, other:SqlGeography) -> SqlGeography:
        """ STSymDifference(self: SqlGeography, other: SqlGeography) -> SqlGeography """
        ...

    def STUnion(self, other:SqlGeography) -> SqlGeography:
        """ STUnion(self: SqlGeography, other: SqlGeography) -> SqlGeography """
        ...

    def STWithin(self, other:SqlGeography) -> SqlBoolean:
        """ STWithin(self: SqlGeography, other: SqlGeography) -> SqlBoolean """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlGeography) -> str """
        ...



class SqlGeographyBuilder(IGeographySink110): # skipped bases: <type 'IGeographySink'>, <type 'object'>
    """ SqlGeographyBuilder() """
    @property
    def ConstructedGeography(self) -> SqlGeography:
        """ Get: ConstructedGeography(self: SqlGeographyBuilder) -> SqlGeography """
        ...


    def AddLine(self, latitude:float, longitude:float, z:Nullable = ..., m:Nullable = ...): # -> 
        """ AddLine(self: SqlGeographyBuilder, latitude: float, longitude: float, z: Nullable[float], m: Nullable[float])AddLine(self: SqlGeographyBuilder, latitude: float, longitude: float) """
        ...

    def BeginFigure(self, latitude:float, longitude:float, z:Nullable = ..., m:Nullable = ...): # -> 
        """ BeginFigure(self: SqlGeographyBuilder, latitude: float, longitude: float, z: Nullable[float], m: Nullable[float])BeginFigure(self: SqlGeographyBuilder, latitude: float, longitude: float) """
        ...

    def BeginGeography(self, type:OpenGisGeographyType): # -> 
        """ BeginGeography(self: SqlGeographyBuilder, type: OpenGisGeographyType) """
        ...

    def EndFigure(self): # -> 
        """ EndFigure(self: SqlGeographyBuilder) """
        ...

    def EndGeography(self): # -> 
        """ EndGeography(self: SqlGeographyBuilder) """
        ...

    def SetSrid(self, srid:int): # -> 
        """ SetSrid(self: SqlGeographyBuilder, srid: int) """
        ...


class SqlGeometry(ISqlSpatialGridIndexable, IBinarySerialize, INullable): # skipped bases: <type 'object'>
    """ SqlGeometry() """
    @property
    def HasM(self) -> bool:
        """ Get: HasM(self: SqlGeometry) -> bool """
        ...

    @property
    def HasZ(self) -> bool:
        """ Get: HasZ(self: SqlGeometry) -> bool """
        ...

    @property
    def M(self) -> SqlDouble:
        """ Get: M(self: SqlGeometry) -> SqlDouble """
        ...

    @property
    def Null(self) -> SqlGeometry:
        """ Get: Null() -> SqlGeometry """
        ...

    @property
    def STSrid(self) -> SqlInt32:
        """
        Get: STSrid(self: SqlGeometry) -> SqlInt32
        Set: STSrid(self: SqlGeometry) = value
        """
        ...

    @property
    def STX(self) -> SqlDouble:
        """ Get: STX(self: SqlGeometry) -> SqlDouble """
        ...

    @property
    def STY(self) -> SqlDouble:
        """ Get: STY(self: SqlGeometry) -> SqlDouble """
        ...

    @property
    def Z(self) -> SqlDouble:
        """ Get: Z(self: SqlGeometry) -> SqlDouble """
        ...


    def AsBinaryZM(self) -> SqlBytes:
        """ AsBinaryZM(self: SqlGeometry) -> SqlBytes """
        ...

    def AsGml(self) -> SqlXml:
        """ AsGml(self: SqlGeometry) -> SqlXml """
        ...

    def AsTextZM(self) -> SqlChars:
        """ AsTextZM(self: SqlGeometry) -> SqlChars """
        ...

    def BufferWithCurves(self, distance:float) -> SqlGeometry:
        """ BufferWithCurves(self: SqlGeometry, distance: float) -> SqlGeometry """
        ...

    def BufferWithTolerance(self, distance:float, tolerance:float, relative:bool) -> SqlGeometry:
        """ BufferWithTolerance(self: SqlGeometry, distance: float, tolerance: float, relative: bool) -> SqlGeometry """
        ...

    def CurveToLineWithTolerance(self, tolerance:float, relative:bool) -> SqlGeometry:
        """ CurveToLineWithTolerance(self: SqlGeometry, tolerance: float, relative: bool) -> SqlGeometry """
        ...

    @staticmethod
    def Deserialize(bytes:SqlBytes) -> SqlGeometry:
        """ Deserialize(bytes: SqlBytes) -> SqlGeometry """
        ...

    def Filter(self, other:SqlGeometry) -> SqlBoolean:
        """ Filter(self: SqlGeometry, other: SqlGeometry) -> SqlBoolean """
        ...

    @staticmethod
    def GeomFromGml(xml:SqlXml, srid:int) -> SqlGeometry:
        """ GeomFromGml(xml: SqlXml, srid: int) -> SqlGeometry """
        ...

    def InstanceOf(self, geometryType:str) -> SqlBoolean:
        """ InstanceOf(self: SqlGeometry, geometryType: str) -> SqlBoolean """
        ...

    def IsValidDetailed(self) -> str:
        """ IsValidDetailed(self: SqlGeometry) -> str """
        ...

    def MakeValid(self) -> SqlGeometry:
        """ MakeValid(self: SqlGeometry) -> SqlGeometry """
        ...

    def MinDbCompatibilityLevel(self) -> int:
        """ MinDbCompatibilityLevel(self: SqlGeometry) -> int """
        ...

    @staticmethod
    def Parse(s:SqlString) -> SqlGeometry:
        """ Parse(s: SqlString) -> SqlGeometry """
        ...

    @staticmethod
    def Point(x:float, y:float, srid:int) -> SqlGeometry:
        """ Point(x: float, y: float, srid: int) -> SqlGeometry """
        ...

    def Populate(self, sink:IGeometrySink): # -> 
        """ Populate(self: SqlGeometry, sink: IGeometrySink)Populate(self: SqlGeometry, sink: IGeometrySink110) """
        ...

    def Reduce(self, tolerance:float) -> SqlGeometry:
        """ Reduce(self: SqlGeometry, tolerance: float) -> SqlGeometry """
        ...

    def Serialize(self) -> SqlBytes:
        """ Serialize(self: SqlGeometry) -> SqlBytes """
        ...

    def ShortestLineTo(self, other:SqlGeometry) -> SqlGeometry:
        """ ShortestLineTo(self: SqlGeometry, other: SqlGeometry) -> SqlGeometry """
        ...

    def STArea(self) -> SqlDouble:
        """ STArea(self: SqlGeometry) -> SqlDouble """
        ...

    def STAsBinary(self) -> SqlBytes:
        """ STAsBinary(self: SqlGeometry) -> SqlBytes """
        ...

    def STAsText(self) -> SqlChars:
        """ STAsText(self: SqlGeometry) -> SqlChars """
        ...

    def STBoundary(self) -> SqlGeometry:
        """ STBoundary(self: SqlGeometry) -> SqlGeometry """
        ...

    def STBuffer(self, distance:float) -> SqlGeometry:
        """ STBuffer(self: SqlGeometry, distance: float) -> SqlGeometry """
        ...

    def STCentroid(self) -> SqlGeometry:
        """ STCentroid(self: SqlGeometry) -> SqlGeometry """
        ...

    def STContains(self, other:SqlGeometry) -> SqlBoolean:
        """ STContains(self: SqlGeometry, other: SqlGeometry) -> SqlBoolean """
        ...

    def STConvexHull(self) -> SqlGeometry:
        """ STConvexHull(self: SqlGeometry) -> SqlGeometry """
        ...

    def STCrosses(self, other:SqlGeometry) -> SqlBoolean:
        """ STCrosses(self: SqlGeometry, other: SqlGeometry) -> SqlBoolean """
        ...

    def STCurveN(self, n:int) -> SqlGeometry:
        """ STCurveN(self: SqlGeometry, n: int) -> SqlGeometry """
        ...

    def STCurveToLine(self) -> SqlGeometry:
        """ STCurveToLine(self: SqlGeometry) -> SqlGeometry """
        ...

    def STDifference(self, other:SqlGeometry) -> SqlGeometry:
        """ STDifference(self: SqlGeometry, other: SqlGeometry) -> SqlGeometry """
        ...

    def STDimension(self) -> SqlInt32:
        """ STDimension(self: SqlGeometry) -> SqlInt32 """
        ...

    def STDisjoint(self, other:SqlGeometry) -> SqlBoolean:
        """ STDisjoint(self: SqlGeometry, other: SqlGeometry) -> SqlBoolean """
        ...

    def STDistance(self, other:SqlGeometry) -> SqlDouble:
        """ STDistance(self: SqlGeometry, other: SqlGeometry) -> SqlDouble """
        ...

    def STEndPoint(self) -> SqlGeometry:
        """ STEndPoint(self: SqlGeometry) -> SqlGeometry """
        ...

    def STEnvelope(self) -> SqlGeometry:
        """ STEnvelope(self: SqlGeometry) -> SqlGeometry """
        ...

    def STEquals(self, other:SqlGeometry) -> SqlBoolean:
        """ STEquals(self: SqlGeometry, other: SqlGeometry) -> SqlBoolean """
        ...

    def STExteriorRing(self) -> SqlGeometry:
        """ STExteriorRing(self: SqlGeometry) -> SqlGeometry """
        ...

    @staticmethod
    def STGeomCollFromText(geometryCollectionTaggedText:SqlChars, srid:int) -> SqlGeometry:
        """ STGeomCollFromText(geometryCollectionTaggedText: SqlChars, srid: int) -> SqlGeometry """
        ...

    @staticmethod
    def STGeomCollFromWKB(wkbGeometryCollection:SqlBytes, srid:int) -> SqlGeometry:
        """ STGeomCollFromWKB(wkbGeometryCollection: SqlBytes, srid: int) -> SqlGeometry """
        ...

    def STGeometryN(self, n:int) -> SqlGeometry:
        """ STGeometryN(self: SqlGeometry, n: int) -> SqlGeometry """
        ...

    def STGeometryType(self) -> SqlString:
        """ STGeometryType(self: SqlGeometry) -> SqlString """
        ...

    @staticmethod
    def STGeomFromText(geometryTaggedText:SqlChars, srid:int) -> SqlGeometry:
        """ STGeomFromText(geometryTaggedText: SqlChars, srid: int) -> SqlGeometry """
        ...

    @staticmethod
    def STGeomFromWKB(wkbGeometry:SqlBytes, srid:int) -> SqlGeometry:
        """ STGeomFromWKB(wkbGeometry: SqlBytes, srid: int) -> SqlGeometry """
        ...

    def STInteriorRingN(self, n:int) -> SqlGeometry:
        """ STInteriorRingN(self: SqlGeometry, n: int) -> SqlGeometry """
        ...

    def STIntersection(self, other:SqlGeometry) -> SqlGeometry:
        """ STIntersection(self: SqlGeometry, other: SqlGeometry) -> SqlGeometry """
        ...

    def STIntersects(self, other:SqlGeometry) -> SqlBoolean:
        """ STIntersects(self: SqlGeometry, other: SqlGeometry) -> SqlBoolean """
        ...

    def STIsClosed(self) -> SqlBoolean:
        """ STIsClosed(self: SqlGeometry) -> SqlBoolean """
        ...

    def STIsEmpty(self) -> SqlBoolean:
        """ STIsEmpty(self: SqlGeometry) -> SqlBoolean """
        ...

    def STIsRing(self) -> SqlBoolean:
        """ STIsRing(self: SqlGeometry) -> SqlBoolean """
        ...

    def STIsSimple(self) -> SqlBoolean:
        """ STIsSimple(self: SqlGeometry) -> SqlBoolean """
        ...

    def STIsValid(self) -> SqlBoolean:
        """ STIsValid(self: SqlGeometry) -> SqlBoolean """
        ...

    def STLength(self) -> SqlDouble:
        """ STLength(self: SqlGeometry) -> SqlDouble """
        ...

    @staticmethod
    def STLineFromText(lineStringTaggedText:SqlChars, srid:int) -> SqlGeometry:
        """ STLineFromText(lineStringTaggedText: SqlChars, srid: int) -> SqlGeometry """
        ...

    @staticmethod
    def STLineFromWKB(wkbLineString:SqlBytes, srid:int) -> SqlGeometry:
        """ STLineFromWKB(wkbLineString: SqlBytes, srid: int) -> SqlGeometry """
        ...

    @staticmethod
    def STMLineFromText(multiLineStringTaggedText:SqlChars, srid:int) -> SqlGeometry:
        """ STMLineFromText(multiLineStringTaggedText: SqlChars, srid: int) -> SqlGeometry """
        ...

    @staticmethod
    def STMLineFromWKB(wkbMultiLineString:SqlBytes, srid:int) -> SqlGeometry:
        """ STMLineFromWKB(wkbMultiLineString: SqlBytes, srid: int) -> SqlGeometry """
        ...

    @staticmethod
    def STMPointFromText(multiPointTaggedText:SqlChars, srid:int) -> SqlGeometry:
        """ STMPointFromText(multiPointTaggedText: SqlChars, srid: int) -> SqlGeometry """
        ...

    @staticmethod
    def STMPointFromWKB(wkbMultiPoint:SqlBytes, srid:int) -> SqlGeometry:
        """ STMPointFromWKB(wkbMultiPoint: SqlBytes, srid: int) -> SqlGeometry """
        ...

    @staticmethod
    def STMPolyFromText(multiPolygonTaggedText:SqlChars, srid:int) -> SqlGeometry:
        """ STMPolyFromText(multiPolygonTaggedText: SqlChars, srid: int) -> SqlGeometry """
        ...

    @staticmethod
    def STMPolyFromWKB(wkbMultiPolygon:SqlBytes, srid:int) -> SqlGeometry:
        """ STMPolyFromWKB(wkbMultiPolygon: SqlBytes, srid: int) -> SqlGeometry """
        ...

    def STNumCurves(self) -> SqlInt32:
        """ STNumCurves(self: SqlGeometry) -> SqlInt32 """
        ...

    def STNumGeometries(self) -> SqlInt32:
        """ STNumGeometries(self: SqlGeometry) -> SqlInt32 """
        ...

    def STNumInteriorRing(self) -> SqlInt32:
        """ STNumInteriorRing(self: SqlGeometry) -> SqlInt32 """
        ...

    def STNumPoints(self) -> SqlInt32:
        """ STNumPoints(self: SqlGeometry) -> SqlInt32 """
        ...

    def STOverlaps(self, other:SqlGeometry) -> SqlBoolean:
        """ STOverlaps(self: SqlGeometry, other: SqlGeometry) -> SqlBoolean """
        ...

    @staticmethod
    def STPointFromText(pointTaggedText:SqlChars, srid:int) -> SqlGeometry:
        """ STPointFromText(pointTaggedText: SqlChars, srid: int) -> SqlGeometry """
        ...

    @staticmethod
    def STPointFromWKB(wkbPoint:SqlBytes, srid:int) -> SqlGeometry:
        """ STPointFromWKB(wkbPoint: SqlBytes, srid: int) -> SqlGeometry """
        ...

    def STPointN(self, n:int) -> SqlGeometry:
        """ STPointN(self: SqlGeometry, n: int) -> SqlGeometry """
        ...

    def STPointOnSurface(self) -> SqlGeometry:
        """ STPointOnSurface(self: SqlGeometry) -> SqlGeometry """
        ...

    @staticmethod
    def STPolyFromText(polygonTaggedText:SqlChars, srid:int) -> SqlGeometry:
        """ STPolyFromText(polygonTaggedText: SqlChars, srid: int) -> SqlGeometry """
        ...

    @staticmethod
    def STPolyFromWKB(wkbPolygon:SqlBytes, srid:int) -> SqlGeometry:
        """ STPolyFromWKB(wkbPolygon: SqlBytes, srid: int) -> SqlGeometry """
        ...

    def STRelate(self, other:SqlGeometry, intersectionPatternMatrix:str) -> SqlBoolean:
        """ STRelate(self: SqlGeometry, other: SqlGeometry, intersectionPatternMatrix: str) -> SqlBoolean """
        ...

    def STStartPoint(self) -> SqlGeometry:
        """ STStartPoint(self: SqlGeometry) -> SqlGeometry """
        ...

    def STSymDifference(self, other:SqlGeometry) -> SqlGeometry:
        """ STSymDifference(self: SqlGeometry, other: SqlGeometry) -> SqlGeometry """
        ...

    def STTouches(self, other:SqlGeometry) -> SqlBoolean:
        """ STTouches(self: SqlGeometry, other: SqlGeometry) -> SqlBoolean """
        ...

    def STUnion(self, other:SqlGeometry) -> SqlGeometry:
        """ STUnion(self: SqlGeometry, other: SqlGeometry) -> SqlGeometry """
        ...

    def STWithin(self, other:SqlGeometry) -> SqlBoolean:
        """ STWithin(self: SqlGeometry, other: SqlGeometry) -> SqlBoolean """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlGeometry) -> str """
        ...



class SqlGeometryBuilder(IGeometrySink110): # skipped bases: <type 'IGeometrySink'>, <type 'object'>
    """ SqlGeometryBuilder() """
    @property
    def ConstructedGeometry(self) -> SqlGeometry:
        """ Get: ConstructedGeometry(self: SqlGeometryBuilder) -> SqlGeometry """
        ...


    def AddLine(self, x:float, y:float, z:Nullable = ..., m:Nullable = ...): # -> 
        """ AddLine(self: SqlGeometryBuilder, x: float, y: float, z: Nullable[float], m: Nullable[float])AddLine(self: SqlGeometryBuilder, x: float, y: float) """
        ...

    def BeginFigure(self, x:float, y:float, z:Nullable = ..., m:Nullable = ...): # -> 
        """ BeginFigure(self: SqlGeometryBuilder, x: float, y: float, z: Nullable[float], m: Nullable[float])BeginFigure(self: SqlGeometryBuilder, x: float, y: float) """
        ...

    def BeginGeometry(self, type:OpenGisGeometryType): # -> 
        """ BeginGeometry(self: SqlGeometryBuilder, type: OpenGisGeometryType) """
        ...

    def EndFigure(self): # -> 
        """ EndFigure(self: SqlGeometryBuilder) """
        ...

    def EndGeometry(self): # -> 
        """ EndGeometry(self: SqlGeometryBuilder) """
        ...

    def SetSrid(self, srid:int): # -> 
        """ SetSrid(self: SqlGeometryBuilder, srid: int) """
        ...


class SqlHierarchyId(IComparable, IBinarySerialize, INullable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Null(self) -> SqlHierarchyId:
        """ Get: Null() -> SqlHierarchyId """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: SqlHierarchyId, obj: object) -> bool """
        ...

    def GetAncestor(self, n:int) -> SqlHierarchyId:
        """ GetAncestor(self: SqlHierarchyId, n: int) -> SqlHierarchyId """
        ...

    def GetDescendant(self, child1:SqlHierarchyId, child2:SqlHierarchyId) -> SqlHierarchyId:
        """ GetDescendant(self: SqlHierarchyId, child1: SqlHierarchyId, child2: SqlHierarchyId) -> SqlHierarchyId """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SqlHierarchyId) -> int """
        ...

    def GetLevel(self) -> SqlInt16:
        """ GetLevel(self: SqlHierarchyId) -> SqlInt16 """
        ...

    def GetReparentedValue(self, oldRoot:SqlHierarchyId, newRoot:SqlHierarchyId) -> SqlHierarchyId:
        """ GetReparentedValue(self: SqlHierarchyId, oldRoot: SqlHierarchyId, newRoot: SqlHierarchyId) -> SqlHierarchyId """
        ...

    @staticmethod
    def GetRoot() -> SqlHierarchyId:
        """ GetRoot() -> SqlHierarchyId """
        ...

    def IsDescendantOf(self, parent:SqlHierarchyId) -> SqlBoolean:
        """ IsDescendantOf(self: SqlHierarchyId, parent: SqlHierarchyId) -> SqlBoolean """
        ...

    @staticmethod
    def Parse(input:SqlString) -> SqlHierarchyId:
        """ Parse(input: SqlString) -> SqlHierarchyId """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlHierarchyId) -> str """
        ...



