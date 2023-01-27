# encoding: utf-8
# module System.Data.Common.CommandTrees.ExpressionBuilder.Spatial calls itself Spatial
# from System.Data.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Data.Common.CommandTrees import (DbExpression, 
    DbFunctionExpression)


# no functions
# classes

class SpatialEdmFunctions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Area(spatialValue:DbExpression) -> DbFunctionExpression:
        """ Area(spatialValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def AsBinary(spatialValue:DbExpression) -> DbFunctionExpression:
        """ AsBinary(spatialValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def AsGml(spatialValue:DbExpression) -> DbFunctionExpression:
        """ AsGml(spatialValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def AsText(spatialValue:DbExpression) -> DbFunctionExpression:
        """ AsText(spatialValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Centroid(geometryValue:DbExpression) -> DbFunctionExpression:
        """ Centroid(geometryValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def CoordinateSystemId(spatialValue:DbExpression) -> DbFunctionExpression:
        """ CoordinateSystemId(spatialValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Distance(spatialValue1:DbExpression, spatialValue2:DbExpression) -> DbFunctionExpression:
        """ Distance(spatialValue1: DbExpression, spatialValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Elevation(spatialValue:DbExpression) -> DbFunctionExpression:
        """ Elevation(spatialValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def EndPoint(spatialValue:DbExpression) -> DbFunctionExpression:
        """ EndPoint(spatialValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def ExteriorRing(geometryValue:DbExpression) -> DbFunctionExpression:
        """ ExteriorRing(geometryValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeographyCollectionFromBinary(geographyCollectionWellKnownBinaryValue:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeographyCollectionFromBinary(geographyCollectionWellKnownBinaryValue: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeographyCollectionFromText(geographyCollectionWellKnownText:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeographyCollectionFromText(geographyCollectionWellKnownText: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeographyFromBinary(wellKnownBinaryValue:DbExpression, coordinateSystemId:DbExpression = ...) -> DbFunctionExpression:
        """
        GeographyFromBinary(wellKnownBinaryValue: DbExpression) -> DbFunctionExpression
        GeographyFromBinary(wellKnownBinaryValue: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression
        """
        ...

    @staticmethod
    def GeographyFromGml(geographyMarkup:DbExpression, coordinateSystemId:DbExpression = ...) -> DbFunctionExpression:
        """
        GeographyFromGml(geographyMarkup: DbExpression) -> DbFunctionExpression
        GeographyFromGml(geographyMarkup: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression
        """
        ...

    @staticmethod
    def GeographyFromText(wellKnownText:DbExpression, coordinateSystemId:DbExpression = ...) -> DbFunctionExpression:
        """
        GeographyFromText(wellKnownText: DbExpression) -> DbFunctionExpression
        GeographyFromText(wellKnownText: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression
        """
        ...

    @staticmethod
    def GeographyLineFromBinary(lineWellKnownBinaryValue:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeographyLineFromBinary(lineWellKnownBinaryValue: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeographyLineFromText(lineWellKnownText:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeographyLineFromText(lineWellKnownText: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeographyMultiLineFromBinary(multiLineWellKnownBinaryValue:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeographyMultiLineFromBinary(multiLineWellKnownBinaryValue: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeographyMultiLineFromText(multiLineWellKnownText:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeographyMultiLineFromText(multiLineWellKnownText: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeographyMultiPointFromBinary(multiPointWellKnownBinaryValue:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeographyMultiPointFromBinary(multiPointWellKnownBinaryValue: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeographyMultiPointFromText(multiPointWellKnownText:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeographyMultiPointFromText(multiPointWellKnownText: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeographyMultiPolygonFromBinary(multiPolygonWellKnownBinaryValue:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeographyMultiPolygonFromBinary(multiPolygonWellKnownBinaryValue: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeographyMultiPolygonFromText(multiPolygonWellKnownText:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeographyMultiPolygonFromText(multiPolygonWellKnownText: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeographyPointFromBinary(pointWellKnownBinaryValue:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeographyPointFromBinary(pointWellKnownBinaryValue: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeographyPointFromText(pointWellKnownText:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeographyPointFromText(pointWellKnownText: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeographyPolygonFromBinary(polygonWellKnownBinaryValue:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeographyPolygonFromBinary(polygonWellKnownBinaryValue: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeographyPolygonFromText(polygonWellKnownText:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeographyPolygonFromText(polygonWellKnownText: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeometryCollectionFromBinary(geometryCollectionWellKnownBinaryValue:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeometryCollectionFromBinary(geometryCollectionWellKnownBinaryValue: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeometryCollectionFromText(geometryCollectionWellKnownText:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeometryCollectionFromText(geometryCollectionWellKnownText: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeometryFromBinary(wellKnownBinaryValue:DbExpression, coordinateSystemId:DbExpression = ...) -> DbFunctionExpression:
        """
        GeometryFromBinary(wellKnownBinaryValue: DbExpression) -> DbFunctionExpression
        GeometryFromBinary(wellKnownBinaryValue: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression
        """
        ...

    @staticmethod
    def GeometryFromGml(geometryMarkup:DbExpression, coordinateSystemId:DbExpression = ...) -> DbFunctionExpression:
        """
        GeometryFromGml(geometryMarkup: DbExpression) -> DbFunctionExpression
        GeometryFromGml(geometryMarkup: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression
        """
        ...

    @staticmethod
    def GeometryFromText(wellKnownText:DbExpression, coordinateSystemId:DbExpression = ...) -> DbFunctionExpression:
        """
        GeometryFromText(wellKnownText: DbExpression) -> DbFunctionExpression
        GeometryFromText(wellKnownText: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression
        """
        ...

    @staticmethod
    def GeometryLineFromBinary(lineWellKnownBinaryValue:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeometryLineFromBinary(lineWellKnownBinaryValue: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeometryLineFromText(lineWellKnownText:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeometryLineFromText(lineWellKnownText: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeometryMultiLineFromBinary(multiLineWellKnownBinaryValue:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeometryMultiLineFromBinary(multiLineWellKnownBinaryValue: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeometryMultiLineFromText(multiLineWellKnownText:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeometryMultiLineFromText(multiLineWellKnownText: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeometryMultiPointFromBinary(multiPointWellKnownBinaryValue:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeometryMultiPointFromBinary(multiPointWellKnownBinaryValue: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeometryMultiPointFromText(multiPointWellKnownText:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeometryMultiPointFromText(multiPointWellKnownText: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeometryMultiPolygonFromBinary(multiPolygonWellKnownBinaryValue:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeometryMultiPolygonFromBinary(multiPolygonWellKnownBinaryValue: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeometryMultiPolygonFromText(multiPolygonWellKnownText:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeometryMultiPolygonFromText(multiPolygonWellKnownText: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeometryPointFromBinary(pointWellKnownBinaryValue:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeometryPointFromBinary(pointWellKnownBinaryValue: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeometryPointFromText(pointWellKnownText:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeometryPointFromText(pointWellKnownText: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeometryPolygonFromBinary(polygonWellKnownBinaryValue:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeometryPolygonFromBinary(polygonWellKnownBinaryValue: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def GeometryPolygonFromText(polygonWellKnownText:DbExpression, coordinateSystemId:DbExpression) -> DbFunctionExpression:
        """ GeometryPolygonFromText(polygonWellKnownText: DbExpression, coordinateSystemId: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def InteriorRingAt(geometryValue:DbExpression, indexValue:DbExpression) -> DbFunctionExpression:
        """ InteriorRingAt(geometryValue: DbExpression, indexValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def InteriorRingCount(geometryValue:DbExpression) -> DbFunctionExpression:
        """ InteriorRingCount(geometryValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def IsClosedSpatial(spatialValue:DbExpression) -> DbFunctionExpression:
        """ IsClosedSpatial(spatialValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def IsEmptySpatial(spatialValue:DbExpression) -> DbFunctionExpression:
        """ IsEmptySpatial(spatialValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def IsRing(geometryValue:DbExpression) -> DbFunctionExpression:
        """ IsRing(geometryValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def IsSimpleGeometry(geometryValue:DbExpression) -> DbFunctionExpression:
        """ IsSimpleGeometry(geometryValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def IsValidGeometry(geometryValue:DbExpression) -> DbFunctionExpression:
        """ IsValidGeometry(geometryValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Latitude(geographyValue:DbExpression) -> DbFunctionExpression:
        """ Latitude(geographyValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Longitude(geographyValue:DbExpression) -> DbFunctionExpression:
        """ Longitude(geographyValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def Measure(spatialValue:DbExpression) -> DbFunctionExpression:
        """ Measure(spatialValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def PointAt(spatialValue:DbExpression, indexValue:DbExpression) -> DbFunctionExpression:
        """ PointAt(spatialValue: DbExpression, indexValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def PointCount(spatialValue:DbExpression) -> DbFunctionExpression:
        """ PointCount(spatialValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def PointOnSurface(geometryValue:DbExpression) -> DbFunctionExpression:
        """ PointOnSurface(geometryValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialBoundary(geometryValue:DbExpression) -> DbFunctionExpression:
        """ SpatialBoundary(geometryValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialBuffer(spatialValue:DbExpression, distance:DbExpression) -> DbFunctionExpression:
        """ SpatialBuffer(spatialValue: DbExpression, distance: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialContains(geometryValue1:DbExpression, geometryValue2:DbExpression) -> DbFunctionExpression:
        """ SpatialContains(geometryValue1: DbExpression, geometryValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialConvexHull(geometryValue:DbExpression) -> DbFunctionExpression:
        """ SpatialConvexHull(geometryValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialCrosses(geometryValue1:DbExpression, geometryValue2:DbExpression) -> DbFunctionExpression:
        """ SpatialCrosses(geometryValue1: DbExpression, geometryValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialDifference(spatialValue1:DbExpression, spatialValue2:DbExpression) -> DbFunctionExpression:
        """ SpatialDifference(spatialValue1: DbExpression, spatialValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialDimension(spatialValue:DbExpression) -> DbFunctionExpression:
        """ SpatialDimension(spatialValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialDisjoint(spatialValue1:DbExpression, spatialValue2:DbExpression) -> DbFunctionExpression:
        """ SpatialDisjoint(spatialValue1: DbExpression, spatialValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialElementAt(spatialValue:DbExpression, indexValue:DbExpression) -> DbFunctionExpression:
        """ SpatialElementAt(spatialValue: DbExpression, indexValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialElementCount(spatialValue:DbExpression) -> DbFunctionExpression:
        """ SpatialElementCount(spatialValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialEnvelope(geometryValue:DbExpression) -> DbFunctionExpression:
        """ SpatialEnvelope(geometryValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialEquals(spatialValue1:DbExpression, spatialValue2:DbExpression) -> DbFunctionExpression:
        """ SpatialEquals(spatialValue1: DbExpression, spatialValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialIntersection(spatialValue1:DbExpression, spatialValue2:DbExpression) -> DbFunctionExpression:
        """ SpatialIntersection(spatialValue1: DbExpression, spatialValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialIntersects(spatialValue1:DbExpression, spatialValue2:DbExpression) -> DbFunctionExpression:
        """ SpatialIntersects(spatialValue1: DbExpression, spatialValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialLength(spatialValue:DbExpression) -> DbFunctionExpression:
        """ SpatialLength(spatialValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialOverlaps(geometryValue1:DbExpression, geometryValue2:DbExpression) -> DbFunctionExpression:
        """ SpatialOverlaps(geometryValue1: DbExpression, geometryValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialRelate(geometryValue1:DbExpression, geometryValue2:DbExpression, intersectionPatternMatrix:DbExpression) -> DbFunctionExpression:
        """ SpatialRelate(geometryValue1: DbExpression, geometryValue2: DbExpression, intersectionPatternMatrix: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialSymmetricDifference(spatialValue1:DbExpression, spatialValue2:DbExpression) -> DbFunctionExpression:
        """ SpatialSymmetricDifference(spatialValue1: DbExpression, spatialValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialTouches(geometryValue1:DbExpression, geometryValue2:DbExpression) -> DbFunctionExpression:
        """ SpatialTouches(geometryValue1: DbExpression, geometryValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialTypeName(spatialValue:DbExpression) -> DbFunctionExpression:
        """ SpatialTypeName(spatialValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialUnion(spatialValue1:DbExpression, spatialValue2:DbExpression) -> DbFunctionExpression:
        """ SpatialUnion(spatialValue1: DbExpression, spatialValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def SpatialWithin(geometryValue1:DbExpression, geometryValue2:DbExpression) -> DbFunctionExpression:
        """ SpatialWithin(geometryValue1: DbExpression, geometryValue2: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def StartPoint(spatialValue:DbExpression) -> DbFunctionExpression:
        """ StartPoint(spatialValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def XCoordinate(geometryValue:DbExpression) -> DbFunctionExpression:
        """ XCoordinate(geometryValue: DbExpression) -> DbFunctionExpression """
        ...

    @staticmethod
    def YCoordinate(geometryValue:DbExpression) -> DbFunctionExpression:
        """ YCoordinate(geometryValue: DbExpression) -> DbFunctionExpression """
        ...

    __all__: list = ...


