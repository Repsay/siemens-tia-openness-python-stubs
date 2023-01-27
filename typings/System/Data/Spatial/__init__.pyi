# encoding: utf-8
# module System.Data.Spatial calls itself Spatial
# from System.Data.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Nullable


# no functions
# classes

class DbGeography: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Area(self) -> Nullable:
        """ Get: Area(self: DbGeography) -> Nullable[float] """
        ...

    @property
    def CoordinateSystemId(self) -> int:
        """ Get: CoordinateSystemId(self: DbGeography) -> int """
        ...

    @property
    def DefaultCoordinateSystemId(self) -> int:
        """ Get: DefaultCoordinateSystemId() -> int """
        ...

    @property
    def Dimension(self) -> int:
        """ Get: Dimension(self: DbGeography) -> int """
        ...

    @property
    def ElementCount(self) -> Nullable:
        """ Get: ElementCount(self: DbGeography) -> Nullable[int] """
        ...

    @property
    def Elevation(self) -> Nullable:
        """ Get: Elevation(self: DbGeography) -> Nullable[float] """
        ...

    @property
    def EndPoint(self) -> DbGeography:
        """ Get: EndPoint(self: DbGeography) -> DbGeography """
        ...

    @property
    def IsClosed(self) -> Nullable:
        """ Get: IsClosed(self: DbGeography) -> Nullable[bool] """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: DbGeography) -> bool """
        ...

    @property
    def Latitude(self) -> Nullable:
        """ Get: Latitude(self: DbGeography) -> Nullable[float] """
        ...

    @property
    def Length(self) -> Nullable:
        """ Get: Length(self: DbGeography) -> Nullable[float] """
        ...

    @property
    def Longitude(self) -> Nullable:
        """ Get: Longitude(self: DbGeography) -> Nullable[float] """
        ...

    @property
    def Measure(self) -> Nullable:
        """ Get: Measure(self: DbGeography) -> Nullable[float] """
        ...

    @property
    def PointCount(self) -> Nullable:
        """ Get: PointCount(self: DbGeography) -> Nullable[int] """
        ...

    @property
    def ProviderValue(self) -> object:
        """ Get: ProviderValue(self: DbGeography) -> object """
        ...

    @property
    def SpatialTypeName(self) -> str:
        """ Get: SpatialTypeName(self: DbGeography) -> str """
        ...

    @property
    def StartPoint(self) -> DbGeography:
        """ Get: StartPoint(self: DbGeography) -> DbGeography """
        ...

    @property
    def WellKnownValue(self) -> DbGeographyWellKnownValue:
        """
        Get: WellKnownValue(self: DbGeography) -> DbGeographyWellKnownValue
        Set: WellKnownValue(self: DbGeography) = value
        """
        ...


    def AsBinary(self) -> Array:
        """ AsBinary(self: DbGeography) -> Array[Byte] """
        ...

    def AsGml(self) -> str:
        """ AsGml(self: DbGeography) -> str """
        ...

    def AsText(self) -> str:
        """ AsText(self: DbGeography) -> str """
        ...

    def Buffer(self, distance:Nullable) -> DbGeography:
        """ Buffer(self: DbGeography, distance: Nullable[float]) -> DbGeography """
        ...

    def Difference(self, other:DbGeography) -> DbGeography:
        """ Difference(self: DbGeography, other: DbGeography) -> DbGeography """
        ...

    def Disjoint(self, other:DbGeography) -> bool:
        """ Disjoint(self: DbGeography, other: DbGeography) -> bool """
        ...

    def Distance(self, other:DbGeography) -> Nullable:
        """ Distance(self: DbGeography, other: DbGeography) -> Nullable[float] """
        ...

    def ElementAt(self, index:int) -> DbGeography:
        """ ElementAt(self: DbGeography, index: int) -> DbGeography """
        ...

    @staticmethod
    def FromBinary(wellKnownBinary:Array, coordinateSystemId:int = ...) -> DbGeography:
        """
        FromBinary(wellKnownBinary: Array[Byte]) -> DbGeography
        FromBinary(wellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeography
        """
        ...

    @staticmethod
    def FromGml(geographyMarkup:str, coordinateSystemId:int = ...) -> DbGeography:
        """
        FromGml(geographyMarkup: str) -> DbGeography
        FromGml(geographyMarkup: str, coordinateSystemId: int) -> DbGeography
        """
        ...

    @staticmethod
    def FromText(wellKnownText:str, coordinateSystemId:int = ...) -> DbGeography:
        """
        FromText(wellKnownText: str) -> DbGeography
        FromText(wellKnownText: str, coordinateSystemId: int) -> DbGeography
        """
        ...

    @staticmethod
    def GeographyCollectionFromBinary(geographyCollectionWellKnownBinary:Array, coordinateSystemId:int) -> DbGeography:
        """ GeographyCollectionFromBinary(geographyCollectionWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeography """
        ...

    @staticmethod
    def GeographyCollectionFromText(geographyCollectionWellKnownText:str, coordinateSystemId:int) -> DbGeography:
        """ GeographyCollectionFromText(geographyCollectionWellKnownText: str, coordinateSystemId: int) -> DbGeography """
        ...

    def Intersection(self, other:DbGeography) -> DbGeography:
        """ Intersection(self: DbGeography, other: DbGeography) -> DbGeography """
        ...

    def Intersects(self, other:DbGeography) -> bool:
        """ Intersects(self: DbGeography, other: DbGeography) -> bool """
        ...

    @staticmethod
    def LineFromBinary(lineWellKnownBinary:Array, coordinateSystemId:int) -> DbGeography:
        """ LineFromBinary(lineWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeography """
        ...

    @staticmethod
    def LineFromText(lineWellKnownText:str, coordinateSystemId:int) -> DbGeography:
        """ LineFromText(lineWellKnownText: str, coordinateSystemId: int) -> DbGeography """
        ...

    @staticmethod
    def MultiLineFromBinary(multiLineWellKnownBinary:Array, coordinateSystemId:int) -> DbGeography:
        """ MultiLineFromBinary(multiLineWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeography """
        ...

    @staticmethod
    def MultiLineFromText(multiLineWellKnownText:str, coordinateSystemId:int) -> DbGeography:
        """ MultiLineFromText(multiLineWellKnownText: str, coordinateSystemId: int) -> DbGeography """
        ...

    @staticmethod
    def MultiPointFromBinary(multiPointWellKnownBinary:Array, coordinateSystemId:int) -> DbGeography:
        """ MultiPointFromBinary(multiPointWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeography """
        ...

    @staticmethod
    def MultiPointFromText(multiPointWellKnownText:str, coordinateSystemId:int) -> DbGeography:
        """ MultiPointFromText(multiPointWellKnownText: str, coordinateSystemId: int) -> DbGeography """
        ...

    @staticmethod
    def MultiPolygonFromBinary(multiPolygonWellKnownBinary:Array, coordinateSystemId:int) -> DbGeography:
        """ MultiPolygonFromBinary(multiPolygonWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeography """
        ...

    @staticmethod
    def MultiPolygonFromText(multiPolygonWellKnownText:str, coordinateSystemId:int) -> DbGeography:
        """ MultiPolygonFromText(multiPolygonWellKnownText: str, coordinateSystemId: int) -> DbGeography """
        ...

    def PointAt(self, index:int) -> DbGeography:
        """ PointAt(self: DbGeography, index: int) -> DbGeography """
        ...

    @staticmethod
    def PointFromBinary(pointWellKnownBinary:Array, coordinateSystemId:int) -> DbGeography:
        """ PointFromBinary(pointWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeography """
        ...

    @staticmethod
    def PointFromText(pointWellKnownText:str, coordinateSystemId:int) -> DbGeography:
        """ PointFromText(pointWellKnownText: str, coordinateSystemId: int) -> DbGeography """
        ...

    @staticmethod
    def PolygonFromBinary(polygonWellKnownBinary:Array, coordinateSystemId:int) -> DbGeography:
        """ PolygonFromBinary(polygonWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeography """
        ...

    @staticmethod
    def PolygonFromText(polygonWellKnownText:str, coordinateSystemId:int) -> DbGeography:
        """ PolygonFromText(polygonWellKnownText: str, coordinateSystemId: int) -> DbGeography """
        ...

    def SpatialEquals(self, other:DbGeography) -> bool:
        """ SpatialEquals(self: DbGeography, other: DbGeography) -> bool """
        ...

    def SymmetricDifference(self, other:DbGeography) -> DbGeography:
        """ SymmetricDifference(self: DbGeography, other: DbGeography) -> DbGeography """
        ...

    def ToString(self) -> str:
        """ ToString(self: DbGeography) -> str """
        ...

    def Union(self, other:DbGeography) -> DbGeography:
        """ Union(self: DbGeography, other: DbGeography) -> DbGeography """
        ...



class DbGeographyWellKnownValue: # skipped bases: <type 'object'>, <type 'object'>
    """ DbGeographyWellKnownValue() """
    @property
    def CoordinateSystemId(self) -> int:
        """
        Get: CoordinateSystemId(self: DbGeographyWellKnownValue) -> int
        Set: CoordinateSystemId(self: DbGeographyWellKnownValue) = value
        """
        ...

    @property
    def WellKnownBinary(self) -> Array:
        """
        Get: WellKnownBinary(self: DbGeographyWellKnownValue) -> Array[Byte]
        Set: WellKnownBinary(self: DbGeographyWellKnownValue) = value
        """
        ...

    @property
    def WellKnownText(self) -> str:
        """
        Get: WellKnownText(self: DbGeographyWellKnownValue) -> str
        Set: WellKnownText(self: DbGeographyWellKnownValue) = value
        """
        ...



class DbGeometry: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Area(self) -> Nullable:
        """ Get: Area(self: DbGeometry) -> Nullable[float] """
        ...

    @property
    def Boundary(self) -> DbGeometry:
        """ Get: Boundary(self: DbGeometry) -> DbGeometry """
        ...

    @property
    def Centroid(self) -> DbGeometry:
        """ Get: Centroid(self: DbGeometry) -> DbGeometry """
        ...

    @property
    def ConvexHull(self) -> DbGeometry:
        """ Get: ConvexHull(self: DbGeometry) -> DbGeometry """
        ...

    @property
    def CoordinateSystemId(self) -> int:
        """ Get: CoordinateSystemId(self: DbGeometry) -> int """
        ...

    @property
    def DefaultCoordinateSystemId(self) -> int:
        """ Get: DefaultCoordinateSystemId() -> int """
        ...

    @property
    def Dimension(self) -> int:
        """ Get: Dimension(self: DbGeometry) -> int """
        ...

    @property
    def ElementCount(self) -> Nullable:
        """ Get: ElementCount(self: DbGeometry) -> Nullable[int] """
        ...

    @property
    def Elevation(self) -> Nullable:
        """ Get: Elevation(self: DbGeometry) -> Nullable[float] """
        ...

    @property
    def EndPoint(self) -> DbGeometry:
        """ Get: EndPoint(self: DbGeometry) -> DbGeometry """
        ...

    @property
    def Envelope(self) -> DbGeometry:
        """ Get: Envelope(self: DbGeometry) -> DbGeometry """
        ...

    @property
    def ExteriorRing(self) -> DbGeometry:
        """ Get: ExteriorRing(self: DbGeometry) -> DbGeometry """
        ...

    @property
    def InteriorRingCount(self) -> Nullable:
        """ Get: InteriorRingCount(self: DbGeometry) -> Nullable[int] """
        ...

    @property
    def IsClosed(self) -> Nullable:
        """ Get: IsClosed(self: DbGeometry) -> Nullable[bool] """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: DbGeometry) -> bool """
        ...

    @property
    def IsRing(self) -> Nullable:
        """ Get: IsRing(self: DbGeometry) -> Nullable[bool] """
        ...

    @property
    def IsSimple(self) -> bool:
        """ Get: IsSimple(self: DbGeometry) -> bool """
        ...

    @property
    def IsValid(self) -> bool:
        """ Get: IsValid(self: DbGeometry) -> bool """
        ...

    @property
    def Length(self) -> Nullable:
        """ Get: Length(self: DbGeometry) -> Nullable[float] """
        ...

    @property
    def Measure(self) -> Nullable:
        """ Get: Measure(self: DbGeometry) -> Nullable[float] """
        ...

    @property
    def PointCount(self) -> Nullable:
        """ Get: PointCount(self: DbGeometry) -> Nullable[int] """
        ...

    @property
    def PointOnSurface(self) -> DbGeometry:
        """ Get: PointOnSurface(self: DbGeometry) -> DbGeometry """
        ...

    @property
    def ProviderValue(self) -> object:
        """ Get: ProviderValue(self: DbGeometry) -> object """
        ...

    @property
    def SpatialTypeName(self) -> str:
        """ Get: SpatialTypeName(self: DbGeometry) -> str """
        ...

    @property
    def StartPoint(self) -> DbGeometry:
        """ Get: StartPoint(self: DbGeometry) -> DbGeometry """
        ...

    @property
    def WellKnownValue(self) -> DbGeometryWellKnownValue:
        """
        Get: WellKnownValue(self: DbGeometry) -> DbGeometryWellKnownValue
        Set: WellKnownValue(self: DbGeometry) = value
        """
        ...

    @property
    def XCoordinate(self) -> Nullable:
        """ Get: XCoordinate(self: DbGeometry) -> Nullable[float] """
        ...

    @property
    def YCoordinate(self) -> Nullable:
        """ Get: YCoordinate(self: DbGeometry) -> Nullable[float] """
        ...


    def AsBinary(self) -> Array:
        """ AsBinary(self: DbGeometry) -> Array[Byte] """
        ...

    def AsGml(self) -> str:
        """ AsGml(self: DbGeometry) -> str """
        ...

    def AsText(self) -> str:
        """ AsText(self: DbGeometry) -> str """
        ...

    def Buffer(self, distance:Nullable) -> DbGeometry:
        """ Buffer(self: DbGeometry, distance: Nullable[float]) -> DbGeometry """
        ...

    def Contains(self, other:DbGeometry) -> bool:
        """ Contains(self: DbGeometry, other: DbGeometry) -> bool """
        ...

    def Crosses(self, other:DbGeometry) -> bool:
        """ Crosses(self: DbGeometry, other: DbGeometry) -> bool """
        ...

    def Difference(self, other:DbGeometry) -> DbGeometry:
        """ Difference(self: DbGeometry, other: DbGeometry) -> DbGeometry """
        ...

    def Disjoint(self, other:DbGeometry) -> bool:
        """ Disjoint(self: DbGeometry, other: DbGeometry) -> bool """
        ...

    def Distance(self, other:DbGeometry) -> Nullable:
        """ Distance(self: DbGeometry, other: DbGeometry) -> Nullable[float] """
        ...

    def ElementAt(self, index:int) -> DbGeometry:
        """ ElementAt(self: DbGeometry, index: int) -> DbGeometry """
        ...

    @staticmethod
    def FromBinary(wellKnownBinary:Array, coordinateSystemId:int = ...) -> DbGeometry:
        """
        FromBinary(wellKnownBinary: Array[Byte]) -> DbGeometry
        FromBinary(wellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeometry
        """
        ...

    @staticmethod
    def FromGml(geometryMarkup:str, coordinateSystemId:int = ...) -> DbGeometry:
        """
        FromGml(geometryMarkup: str) -> DbGeometry
        FromGml(geometryMarkup: str, coordinateSystemId: int) -> DbGeometry
        """
        ...

    @staticmethod
    def FromText(wellKnownText:str, coordinateSystemId:int = ...) -> DbGeometry:
        """
        FromText(wellKnownText: str) -> DbGeometry
        FromText(wellKnownText: str, coordinateSystemId: int) -> DbGeometry
        """
        ...

    @staticmethod
    def GeometryCollectionFromBinary(geometryCollectionWellKnownBinary:Array, coordinateSystemId:int) -> DbGeometry:
        """ GeometryCollectionFromBinary(geometryCollectionWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeometry """
        ...

    @staticmethod
    def GeometryCollectionFromText(geometryCollectionWellKnownText:str, coordinateSystemId:int) -> DbGeometry:
        """ GeometryCollectionFromText(geometryCollectionWellKnownText: str, coordinateSystemId: int) -> DbGeometry """
        ...

    def InteriorRingAt(self, index:int) -> DbGeometry:
        """ InteriorRingAt(self: DbGeometry, index: int) -> DbGeometry """
        ...

    def Intersection(self, other:DbGeometry) -> DbGeometry:
        """ Intersection(self: DbGeometry, other: DbGeometry) -> DbGeometry """
        ...

    def Intersects(self, other:DbGeometry) -> bool:
        """ Intersects(self: DbGeometry, other: DbGeometry) -> bool """
        ...

    @staticmethod
    def LineFromBinary(lineWellKnownBinary:Array, coordinateSystemId:int) -> DbGeometry:
        """ LineFromBinary(lineWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeometry """
        ...

    @staticmethod
    def LineFromText(lineWellKnownText:str, coordinateSystemId:int) -> DbGeometry:
        """ LineFromText(lineWellKnownText: str, coordinateSystemId: int) -> DbGeometry """
        ...

    @staticmethod
    def MultiLineFromBinary(multiLineWellKnownBinary:Array, coordinateSystemId:int) -> DbGeometry:
        """ MultiLineFromBinary(multiLineWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeometry """
        ...

    @staticmethod
    def MultiLineFromText(multiLineWellKnownText:str, coordinateSystemId:int) -> DbGeometry:
        """ MultiLineFromText(multiLineWellKnownText: str, coordinateSystemId: int) -> DbGeometry """
        ...

    @staticmethod
    def MultiPointFromBinary(multiPointWellKnownBinary:Array, coordinateSystemId:int) -> DbGeometry:
        """ MultiPointFromBinary(multiPointWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeometry """
        ...

    @staticmethod
    def MultiPointFromText(multiPointWellKnownText:str, coordinateSystemId:int) -> DbGeometry:
        """ MultiPointFromText(multiPointWellKnownText: str, coordinateSystemId: int) -> DbGeometry """
        ...

    @staticmethod
    def MultiPolygonFromBinary(multiPolygonWellKnownBinary:Array, coordinateSystemId:int) -> DbGeometry:
        """ MultiPolygonFromBinary(multiPolygonWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeometry """
        ...

    @staticmethod
    def MultiPolygonFromText(multiPolygonWellKnownText:str, coordinateSystemId:int) -> DbGeometry:
        """ MultiPolygonFromText(multiPolygonWellKnownText: str, coordinateSystemId: int) -> DbGeometry """
        ...

    def Overlaps(self, other:DbGeometry) -> bool:
        """ Overlaps(self: DbGeometry, other: DbGeometry) -> bool """
        ...

    def PointAt(self, index:int) -> DbGeometry:
        """ PointAt(self: DbGeometry, index: int) -> DbGeometry """
        ...

    @staticmethod
    def PointFromBinary(pointWellKnownBinary:Array, coordinateSystemId:int) -> DbGeometry:
        """ PointFromBinary(pointWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeometry """
        ...

    @staticmethod
    def PointFromText(pointWellKnownText:str, coordinateSystemId:int) -> DbGeometry:
        """ PointFromText(pointWellKnownText: str, coordinateSystemId: int) -> DbGeometry """
        ...

    @staticmethod
    def PolygonFromBinary(polygonWellKnownBinary:Array, coordinateSystemId:int) -> DbGeometry:
        """ PolygonFromBinary(polygonWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeometry """
        ...

    @staticmethod
    def PolygonFromText(polygonWellKnownText:str, coordinateSystemId:int) -> DbGeometry:
        """ PolygonFromText(polygonWellKnownText: str, coordinateSystemId: int) -> DbGeometry """
        ...

    def Relate(self, other:DbGeometry, matrix:str) -> bool:
        """ Relate(self: DbGeometry, other: DbGeometry, matrix: str) -> bool """
        ...

    def SpatialEquals(self, other:DbGeometry) -> bool:
        """ SpatialEquals(self: DbGeometry, other: DbGeometry) -> bool """
        ...

    def SymmetricDifference(self, other:DbGeometry) -> DbGeometry:
        """ SymmetricDifference(self: DbGeometry, other: DbGeometry) -> DbGeometry """
        ...

    def ToString(self) -> str:
        """ ToString(self: DbGeometry) -> str """
        ...

    def Touches(self, other:DbGeometry) -> bool:
        """ Touches(self: DbGeometry, other: DbGeometry) -> bool """
        ...

    def Union(self, other:DbGeometry) -> DbGeometry:
        """ Union(self: DbGeometry, other: DbGeometry) -> DbGeometry """
        ...

    def Within(self, other:DbGeometry) -> bool:
        """ Within(self: DbGeometry, other: DbGeometry) -> bool """
        ...



class DbGeometryWellKnownValue: # skipped bases: <type 'object'>, <type 'object'>
    """ DbGeometryWellKnownValue() """
    @property
    def CoordinateSystemId(self) -> int:
        """
        Get: CoordinateSystemId(self: DbGeometryWellKnownValue) -> int
        Set: CoordinateSystemId(self: DbGeometryWellKnownValue) = value
        """
        ...

    @property
    def WellKnownBinary(self) -> Array:
        """
        Get: WellKnownBinary(self: DbGeometryWellKnownValue) -> Array[Byte]
        Set: WellKnownBinary(self: DbGeometryWellKnownValue) = value
        """
        ...

    @property
    def WellKnownText(self) -> str:
        """
        Get: WellKnownText(self: DbGeometryWellKnownValue) -> str
        Set: WellKnownText(self: DbGeometryWellKnownValue) = value
        """
        ...



class DbSpatialDataReader: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetGeography(self, ordinal:int) -> DbGeography:
        """ GetGeography(self: DbSpatialDataReader, ordinal: int) -> DbGeography """
        ...

    def GetGeometry(self, ordinal:int) -> DbGeometry:
        """ GetGeometry(self: DbSpatialDataReader, ordinal: int) -> DbGeometry """
        ...


class DbSpatialServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Default(self) -> DbSpatialServices:
        """ Get: Default() -> DbSpatialServices """
        ...


    def AsBinary(self, *__args:DbGeography) -> Array:
        """
        AsBinary(self: DbSpatialServices, geographyValue: DbGeography) -> Array[Byte]
        AsBinary(self: DbSpatialServices, geometryValue: DbGeometry) -> Array[Byte]
        """
        ...

    def AsGml(self, *__args:DbGeography) -> str:
        """
        AsGml(self: DbSpatialServices, geographyValue: DbGeography) -> str
        AsGml(self: DbSpatialServices, geometryValue: DbGeometry) -> str
        """
        ...

    def AsText(self, *__args:DbGeography) -> str:
        """
        AsText(self: DbSpatialServices, geographyValue: DbGeography) -> str
        AsText(self: DbSpatialServices, geometryValue: DbGeometry) -> str
        """
        ...

    def AsTextIncludingElevationAndMeasure(self, *__args:DbGeography) -> str:
        """
        AsTextIncludingElevationAndMeasure(self: DbSpatialServices, geographyValue: DbGeography) -> str
        AsTextIncludingElevationAndMeasure(self: DbSpatialServices, geometryValue: DbGeometry) -> str
        """
        ...

    def Buffer(self, *__args) -> DbGeography:
        """
        Buffer(self: DbSpatialServices, geographyValue: DbGeography, distance: float) -> DbGeography
        Buffer(self: DbSpatialServices, geometryValue: DbGeometry, distance: float) -> DbGeometry
        """
        ...

    def Contains(self, geometryValue:DbGeometry, otherGeometry:DbGeometry) -> bool:
        """ Contains(self: DbSpatialServices, geometryValue: DbGeometry, otherGeometry: DbGeometry) -> bool """
        ...

    def CreateGeography(self, *args): #cannot find CLR method
        """ CreateGeography(spatialServices: DbSpatialServices, providerValue: object) -> DbGeography """
        ...

    def CreateGeometry(self, *args): #cannot find CLR method
        """ CreateGeometry(spatialServices: DbSpatialServices, providerValue: object) -> DbGeometry """
        ...

    def CreateProviderValue(self, wellKnownValue:DbGeographyWellKnownValue) -> object:
        """
        CreateProviderValue(self: DbSpatialServices, wellKnownValue: DbGeographyWellKnownValue) -> object
        CreateProviderValue(self: DbSpatialServices, wellKnownValue: DbGeometryWellKnownValue) -> object
        """
        ...

    def CreateWellKnownValue(self, *__args:DbGeography) -> DbGeographyWellKnownValue:
        """
        CreateWellKnownValue(self: DbSpatialServices, geographyValue: DbGeography) -> DbGeographyWellKnownValue
        CreateWellKnownValue(self: DbSpatialServices, geometryValue: DbGeometry) -> DbGeometryWellKnownValue
        """
        ...

    def Crosses(self, geometryValue:DbGeometry, otherGeometry:DbGeometry) -> bool:
        """ Crosses(self: DbSpatialServices, geometryValue: DbGeometry, otherGeometry: DbGeometry) -> bool """
        ...

    def Difference(self, *__args) -> DbGeography:
        """
        Difference(self: DbSpatialServices, geographyValue: DbGeography, otherGeography: DbGeography) -> DbGeography
        Difference(self: DbSpatialServices, geometryValue: DbGeometry, otherGeometry: DbGeometry) -> DbGeometry
        """
        ...

    def Disjoint(self, *__args) -> bool:
        """
        Disjoint(self: DbSpatialServices, geographyValue: DbGeography, otherGeography: DbGeography) -> bool
        Disjoint(self: DbSpatialServices, geometryValue: DbGeometry, otherGeometry: DbGeometry) -> bool
        """
        ...

    def Distance(self, *__args) -> float:
        """
        Distance(self: DbSpatialServices, geographyValue: DbGeography, otherGeography: DbGeography) -> float
        Distance(self: DbSpatialServices, geometryValue: DbGeometry, otherGeometry: DbGeometry) -> float
        """
        ...

    def ElementAt(self, *__args) -> DbGeography:
        """
        ElementAt(self: DbSpatialServices, geographyValue: DbGeography, index: int) -> DbGeography
        ElementAt(self: DbSpatialServices, geometryValue: DbGeometry, index: int) -> DbGeometry
        """
        ...

    def GeographyCollectionFromBinary(self, geographyCollectionWellKnownBinary:Array, coordinateSystemId:int) -> DbGeography:
        """ GeographyCollectionFromBinary(self: DbSpatialServices, geographyCollectionWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeography """
        ...

    def GeographyCollectionFromText(self, geographyCollectionWellKnownText:str, coordinateSystemId:int) -> DbGeography:
        """ GeographyCollectionFromText(self: DbSpatialServices, geographyCollectionWellKnownText: str, coordinateSystemId: int) -> DbGeography """
        ...

    def GeographyFromBinary(self, wellKnownBinary:Array, coordinateSystemId:int = ...) -> DbGeography:
        """
        GeographyFromBinary(self: DbSpatialServices, wellKnownBinary: Array[Byte]) -> DbGeography
        GeographyFromBinary(self: DbSpatialServices, wellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeography
        """
        ...

    def GeographyFromGml(self, geographyMarkup:str, coordinateSystemId:int = ...) -> DbGeography:
        """
        GeographyFromGml(self: DbSpatialServices, geographyMarkup: str) -> DbGeography
        GeographyFromGml(self: DbSpatialServices, geographyMarkup: str, coordinateSystemId: int) -> DbGeography
        """
        ...

    def GeographyFromProviderValue(self, providerValue:object) -> DbGeography:
        """ GeographyFromProviderValue(self: DbSpatialServices, providerValue: object) -> DbGeography """
        ...

    def GeographyFromText(self, wellKnownText:str, coordinateSystemId:int = ...) -> DbGeography:
        """
        GeographyFromText(self: DbSpatialServices, wellKnownText: str) -> DbGeography
        GeographyFromText(self: DbSpatialServices, wellKnownText: str, coordinateSystemId: int) -> DbGeography
        """
        ...

    def GeographyLineFromBinary(self, lineWellKnownBinary:Array, coordinateSystemId:int) -> DbGeography:
        """ GeographyLineFromBinary(self: DbSpatialServices, lineWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeography """
        ...

    def GeographyLineFromText(self, lineWellKnownText:str, coordinateSystemId:int) -> DbGeography:
        """ GeographyLineFromText(self: DbSpatialServices, lineWellKnownText: str, coordinateSystemId: int) -> DbGeography """
        ...

    def GeographyMultiLineFromBinary(self, multiLineWellKnownBinary:Array, coordinateSystemId:int) -> DbGeography:
        """ GeographyMultiLineFromBinary(self: DbSpatialServices, multiLineWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeography """
        ...

    def GeographyMultiLineFromText(self, multiLineWellKnownText:str, coordinateSystemId:int) -> DbGeography:
        """ GeographyMultiLineFromText(self: DbSpatialServices, multiLineWellKnownText: str, coordinateSystemId: int) -> DbGeography """
        ...

    def GeographyMultiPointFromBinary(self, multiPointWellKnownBinary:Array, coordinateSystemId:int) -> DbGeography:
        """ GeographyMultiPointFromBinary(self: DbSpatialServices, multiPointWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeography """
        ...

    def GeographyMultiPointFromText(self, multiPointWellKnownText:str, coordinateSystemId:int) -> DbGeography:
        """ GeographyMultiPointFromText(self: DbSpatialServices, multiPointWellKnownText: str, coordinateSystemId: int) -> DbGeography """
        ...

    def GeographyMultiPolygonFromBinary(self, multiPolygonWellKnownBinary:Array, coordinateSystemId:int) -> DbGeography:
        """ GeographyMultiPolygonFromBinary(self: DbSpatialServices, multiPolygonWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeography """
        ...

    def GeographyMultiPolygonFromText(self, multiPolygonWellKnownText:str, coordinateSystemId:int) -> DbGeography:
        """ GeographyMultiPolygonFromText(self: DbSpatialServices, multiPolygonWellKnownText: str, coordinateSystemId: int) -> DbGeography """
        ...

    def GeographyPointFromBinary(self, pointWellKnownBinary:Array, coordinateSystemId:int) -> DbGeography:
        """ GeographyPointFromBinary(self: DbSpatialServices, pointWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeography """
        ...

    def GeographyPointFromText(self, pointWellKnownText:str, coordinateSystemId:int) -> DbGeography:
        """ GeographyPointFromText(self: DbSpatialServices, pointWellKnownText: str, coordinateSystemId: int) -> DbGeography """
        ...

    def GeographyPolygonFromBinary(self, polygonWellKnownBinary:Array, coordinateSystemId:int) -> DbGeography:
        """ GeographyPolygonFromBinary(self: DbSpatialServices, polygonWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeography """
        ...

    def GeographyPolygonFromText(self, polygonWellKnownText:str, coordinateSystemId:int) -> DbGeography:
        """ GeographyPolygonFromText(self: DbSpatialServices, polygonWellKnownText: str, coordinateSystemId: int) -> DbGeography """
        ...

    def GeometryCollectionFromBinary(self, geometryCollectionWellKnownBinary:Array, coordinateSystemId:int) -> DbGeometry:
        """ GeometryCollectionFromBinary(self: DbSpatialServices, geometryCollectionWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeometry """
        ...

    def GeometryCollectionFromText(self, geometryCollectionWellKnownText:str, coordinateSystemId:int) -> DbGeometry:
        """ GeometryCollectionFromText(self: DbSpatialServices, geometryCollectionWellKnownText: str, coordinateSystemId: int) -> DbGeometry """
        ...

    def GeometryFromBinary(self, wellKnownBinary:Array, coordinateSystemId:int = ...) -> DbGeometry:
        """
        GeometryFromBinary(self: DbSpatialServices, wellKnownBinary: Array[Byte]) -> DbGeometry
        GeometryFromBinary(self: DbSpatialServices, wellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeometry
        """
        ...

    def GeometryFromGml(self, geometryMarkup:str, coordinateSystemId:int = ...) -> DbGeometry:
        """
        GeometryFromGml(self: DbSpatialServices, geometryMarkup: str) -> DbGeometry
        GeometryFromGml(self: DbSpatialServices, geometryMarkup: str, coordinateSystemId: int) -> DbGeometry
        """
        ...

    def GeometryFromProviderValue(self, providerValue:object) -> DbGeometry:
        """ GeometryFromProviderValue(self: DbSpatialServices, providerValue: object) -> DbGeometry """
        ...

    def GeometryFromText(self, wellKnownText:str, coordinateSystemId:int = ...) -> DbGeometry:
        """
        GeometryFromText(self: DbSpatialServices, wellKnownText: str) -> DbGeometry
        GeometryFromText(self: DbSpatialServices, wellKnownText: str, coordinateSystemId: int) -> DbGeometry
        """
        ...

    def GeometryLineFromBinary(self, lineWellKnownBinary:Array, coordinateSystemId:int) -> DbGeometry:
        """ GeometryLineFromBinary(self: DbSpatialServices, lineWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeometry """
        ...

    def GeometryLineFromText(self, lineWellKnownText:str, coordinateSystemId:int) -> DbGeometry:
        """ GeometryLineFromText(self: DbSpatialServices, lineWellKnownText: str, coordinateSystemId: int) -> DbGeometry """
        ...

    def GeometryMultiLineFromBinary(self, multiLineWellKnownBinary:Array, coordinateSystemId:int) -> DbGeometry:
        """ GeometryMultiLineFromBinary(self: DbSpatialServices, multiLineWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeometry """
        ...

    def GeometryMultiLineFromText(self, multiLineWellKnownText:str, coordinateSystemId:int) -> DbGeometry:
        """ GeometryMultiLineFromText(self: DbSpatialServices, multiLineWellKnownText: str, coordinateSystemId: int) -> DbGeometry """
        ...

    def GeometryMultiPointFromBinary(self, multiPointWellKnownBinary:Array, coordinateSystemId:int) -> DbGeometry:
        """ GeometryMultiPointFromBinary(self: DbSpatialServices, multiPointWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeometry """
        ...

    def GeometryMultiPointFromText(self, multiPointWellKnownText:str, coordinateSystemId:int) -> DbGeometry:
        """ GeometryMultiPointFromText(self: DbSpatialServices, multiPointWellKnownText: str, coordinateSystemId: int) -> DbGeometry """
        ...

    def GeometryMultiPolygonFromBinary(self, multiPolygonWellKnownBinary:Array, coordinateSystemId:int) -> DbGeometry:
        """ GeometryMultiPolygonFromBinary(self: DbSpatialServices, multiPolygonWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeometry """
        ...

    def GeometryMultiPolygonFromText(self, multiPolygonKnownText:str, coordinateSystemId:int) -> DbGeometry:
        """ GeometryMultiPolygonFromText(self: DbSpatialServices, multiPolygonKnownText: str, coordinateSystemId: int) -> DbGeometry """
        ...

    def GeometryPointFromBinary(self, pointWellKnownBinary:Array, coordinateSystemId:int) -> DbGeometry:
        """ GeometryPointFromBinary(self: DbSpatialServices, pointWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeometry """
        ...

    def GeometryPointFromText(self, pointWellKnownText:str, coordinateSystemId:int) -> DbGeometry:
        """ GeometryPointFromText(self: DbSpatialServices, pointWellKnownText: str, coordinateSystemId: int) -> DbGeometry """
        ...

    def GeometryPolygonFromBinary(self, polygonWellKnownBinary:Array, coordinateSystemId:int) -> DbGeometry:
        """ GeometryPolygonFromBinary(self: DbSpatialServices, polygonWellKnownBinary: Array[Byte], coordinateSystemId: int) -> DbGeometry """
        ...

    def GeometryPolygonFromText(self, polygonWellKnownText:str, coordinateSystemId:int) -> DbGeometry:
        """ GeometryPolygonFromText(self: DbSpatialServices, polygonWellKnownText: str, coordinateSystemId: int) -> DbGeometry """
        ...

    def GetArea(self, *__args:DbGeography) -> Nullable:
        """
        GetArea(self: DbSpatialServices, geographyValue: DbGeography) -> Nullable[float]
        GetArea(self: DbSpatialServices, geometryValue: DbGeometry) -> Nullable[float]
        """
        ...

    def GetBoundary(self, geometryValue:DbGeometry) -> DbGeometry:
        """ GetBoundary(self: DbSpatialServices, geometryValue: DbGeometry) -> DbGeometry """
        ...

    def GetCentroid(self, geometryValue:DbGeometry) -> DbGeometry:
        """ GetCentroid(self: DbSpatialServices, geometryValue: DbGeometry) -> DbGeometry """
        ...

    def GetConvexHull(self, geometryValue:DbGeometry) -> DbGeometry:
        """ GetConvexHull(self: DbSpatialServices, geometryValue: DbGeometry) -> DbGeometry """
        ...

    def GetCoordinateSystemId(self, *__args:DbGeography) -> int:
        """
        GetCoordinateSystemId(self: DbSpatialServices, geographyValue: DbGeography) -> int
        GetCoordinateSystemId(self: DbSpatialServices, geometryValue: DbGeometry) -> int
        """
        ...

    def GetDimension(self, *__args:DbGeography) -> int:
        """
        GetDimension(self: DbSpatialServices, geographyValue: DbGeography) -> int
        GetDimension(self: DbSpatialServices, geometryValue: DbGeometry) -> int
        """
        ...

    def GetElementCount(self, *__args:DbGeography) -> Nullable:
        """
        GetElementCount(self: DbSpatialServices, geographyValue: DbGeography) -> Nullable[int]
        GetElementCount(self: DbSpatialServices, geometryValue: DbGeometry) -> Nullable[int]
        """
        ...

    def GetElevation(self, *__args:DbGeography) -> Nullable:
        """
        GetElevation(self: DbSpatialServices, geographyValue: DbGeography) -> Nullable[float]
        GetElevation(self: DbSpatialServices, geometryValue: DbGeometry) -> Nullable[float]
        """
        ...

    def GetEndPoint(self, *__args:DbGeography) -> DbGeography:
        """
        GetEndPoint(self: DbSpatialServices, geographyValue: DbGeography) -> DbGeography
        GetEndPoint(self: DbSpatialServices, geometryValue: DbGeometry) -> DbGeometry
        """
        ...

    def GetEnvelope(self, geometryValue:DbGeometry) -> DbGeometry:
        """ GetEnvelope(self: DbSpatialServices, geometryValue: DbGeometry) -> DbGeometry """
        ...

    def GetExteriorRing(self, geometryValue:DbGeometry) -> DbGeometry:
        """ GetExteriorRing(self: DbSpatialServices, geometryValue: DbGeometry) -> DbGeometry """
        ...

    def GetInteriorRingCount(self, geometryValue:DbGeometry) -> Nullable:
        """ GetInteriorRingCount(self: DbSpatialServices, geometryValue: DbGeometry) -> Nullable[int] """
        ...

    def GetIsClosed(self, *__args:DbGeography) -> Nullable:
        """
        GetIsClosed(self: DbSpatialServices, geographyValue: DbGeography) -> Nullable[bool]
        GetIsClosed(self: DbSpatialServices, geometryValue: DbGeometry) -> Nullable[bool]
        """
        ...

    def GetIsEmpty(self, *__args:DbGeography) -> bool:
        """
        GetIsEmpty(self: DbSpatialServices, geographyValue: DbGeography) -> bool
        GetIsEmpty(self: DbSpatialServices, geometryValue: DbGeometry) -> bool
        """
        ...

    def GetIsRing(self, geometryValue:DbGeometry) -> Nullable:
        """ GetIsRing(self: DbSpatialServices, geometryValue: DbGeometry) -> Nullable[bool] """
        ...

    def GetIsSimple(self, geometryValue:DbGeometry) -> bool:
        """ GetIsSimple(self: DbSpatialServices, geometryValue: DbGeometry) -> bool """
        ...

    def GetIsValid(self, geometryValue:DbGeometry) -> bool:
        """ GetIsValid(self: DbSpatialServices, geometryValue: DbGeometry) -> bool """
        ...

    def GetLatitude(self, geographyValue:DbGeography) -> Nullable:
        """ GetLatitude(self: DbSpatialServices, geographyValue: DbGeography) -> Nullable[float] """
        ...

    def GetLength(self, *__args:DbGeography) -> Nullable:
        """
        GetLength(self: DbSpatialServices, geographyValue: DbGeography) -> Nullable[float]
        GetLength(self: DbSpatialServices, geometryValue: DbGeometry) -> Nullable[float]
        """
        ...

    def GetLongitude(self, geographyValue:DbGeography) -> Nullable:
        """ GetLongitude(self: DbSpatialServices, geographyValue: DbGeography) -> Nullable[float] """
        ...

    def GetMeasure(self, *__args:DbGeography) -> Nullable:
        """
        GetMeasure(self: DbSpatialServices, geographyValue: DbGeography) -> Nullable[float]
        GetMeasure(self: DbSpatialServices, geometryValue: DbGeometry) -> Nullable[float]
        """
        ...

    def GetPointCount(self, *__args:DbGeography) -> Nullable:
        """
        GetPointCount(self: DbSpatialServices, geographyValue: DbGeography) -> Nullable[int]
        GetPointCount(self: DbSpatialServices, geometryValue: DbGeometry) -> Nullable[int]
        """
        ...

    def GetPointOnSurface(self, geometryValue:DbGeometry) -> DbGeometry:
        """ GetPointOnSurface(self: DbSpatialServices, geometryValue: DbGeometry) -> DbGeometry """
        ...

    def GetSpatialTypeName(self, *__args:DbGeography) -> str:
        """
        GetSpatialTypeName(self: DbSpatialServices, geographyValue: DbGeography) -> str
        GetSpatialTypeName(self: DbSpatialServices, geometryValue: DbGeometry) -> str
        """
        ...

    def GetStartPoint(self, *__args:DbGeography) -> DbGeography:
        """
        GetStartPoint(self: DbSpatialServices, geographyValue: DbGeography) -> DbGeography
        GetStartPoint(self: DbSpatialServices, geometryValue: DbGeometry) -> DbGeometry
        """
        ...

    def GetXCoordinate(self, geometryValue:DbGeometry) -> Nullable:
        """ GetXCoordinate(self: DbSpatialServices, geometryValue: DbGeometry) -> Nullable[float] """
        ...

    def GetYCoordinate(self, geometryValue:DbGeometry) -> Nullable:
        """ GetYCoordinate(self: DbSpatialServices, geometryValue: DbGeometry) -> Nullable[float] """
        ...

    def InteriorRingAt(self, geometryValue:DbGeometry, index:int) -> DbGeometry:
        """ InteriorRingAt(self: DbSpatialServices, geometryValue: DbGeometry, index: int) -> DbGeometry """
        ...

    def Intersection(self, *__args) -> DbGeography:
        """
        Intersection(self: DbSpatialServices, geographyValue: DbGeography, otherGeography: DbGeography) -> DbGeography
        Intersection(self: DbSpatialServices, geometryValue: DbGeometry, otherGeometry: DbGeometry) -> DbGeometry
        """
        ...

    def Intersects(self, *__args) -> bool:
        """
        Intersects(self: DbSpatialServices, geographyValue: DbGeography, otherGeography: DbGeography) -> bool
        Intersects(self: DbSpatialServices, geometryValue: DbGeometry, otherGeometry: DbGeometry) -> bool
        """
        ...

    def Overlaps(self, geometryValue:DbGeometry, otherGeometry:DbGeometry) -> bool:
        """ Overlaps(self: DbSpatialServices, geometryValue: DbGeometry, otherGeometry: DbGeometry) -> bool """
        ...

    def PointAt(self, *__args) -> DbGeography:
        """
        PointAt(self: DbSpatialServices, geographyValue: DbGeography, index: int) -> DbGeography
        PointAt(self: DbSpatialServices, geometryValue: DbGeometry, index: int) -> DbGeometry
        """
        ...

    def Relate(self, geometryValue:DbGeometry, otherGeometry:DbGeometry, matrix:str) -> bool:
        """ Relate(self: DbSpatialServices, geometryValue: DbGeometry, otherGeometry: DbGeometry, matrix: str) -> bool """
        ...

    def SpatialEquals(self, *__args) -> bool:
        """
        SpatialEquals(self: DbSpatialServices, geographyValue: DbGeography, otherGeography: DbGeography) -> bool
        SpatialEquals(self: DbSpatialServices, geometryValue: DbGeometry, otherGeometry: DbGeometry) -> bool
        """
        ...

    def SymmetricDifference(self, *__args) -> DbGeography:
        """
        SymmetricDifference(self: DbSpatialServices, geographyValue: DbGeography, otherGeography: DbGeography) -> DbGeography
        SymmetricDifference(self: DbSpatialServices, geometryValue: DbGeometry, otherGeometry: DbGeometry) -> DbGeometry
        """
        ...

    def Touches(self, geometryValue:DbGeometry, otherGeometry:DbGeometry) -> bool:
        """ Touches(self: DbSpatialServices, geometryValue: DbGeometry, otherGeometry: DbGeometry) -> bool """
        ...

    def Union(self, *__args) -> DbGeography:
        """
        Union(self: DbSpatialServices, geographyValue: DbGeography, otherGeography: DbGeography) -> DbGeography
        Union(self: DbSpatialServices, geometryValue: DbGeometry, otherGeometry: DbGeometry) -> DbGeometry
        """
        ...

    def Within(self, geometryValue:DbGeometry, otherGeometry:DbGeometry) -> bool:
        """ Within(self: DbSpatialServices, geometryValue: DbGeometry, otherGeometry: DbGeometry) -> bool """
        ...



