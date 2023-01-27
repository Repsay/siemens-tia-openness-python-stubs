# encoding: utf-8
# module System.Configuration.Assemblies calls itself Assemblies
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, ICloneable

"""The following names are not found in the module: field#
"""

# no functions
# classes

class AssemblyHash(ICloneable): # skipped bases: <type 'object'>
    """
    AssemblyHash(value: Array[Byte])
    AssemblyHash(algorithm: AssemblyHashAlgorithm, value: Array[Byte])
    """
    @property
    def Algorithm(self) -> AssemblyHashAlgorithm:
        """
        Get: Algorithm(self: AssemblyHash) -> AssemblyHashAlgorithm
        Set: Algorithm(self: AssemblyHash) = value
        """
        ...


    def GetValue(self) -> Array:
        """ GetValue(self: AssemblyHash) -> Array[Byte] """
        ...

    def SetValue(self, value:Array): # -> 
        """ SetValue(self: AssemblyHash, value: Array[Byte]) """
        ...

    Empty: AssemblyHash = ...


class AssemblyHashAlgorithm(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AssemblyHashAlgorithm, values: MD5 (32771), None (0), SHA1 (32772), SHA256 (32780), SHA384 (32781), SHA512 (32782) """
    MD5: AssemblyHashAlgorithm = ...
    SHA1: AssemblyHashAlgorithm = ...
    SHA256: AssemblyHashAlgorithm = ...
    SHA384: AssemblyHashAlgorithm = ...
    SHA512: AssemblyHashAlgorithm = ...
    value__ = ...


class AssemblyVersionCompatibility(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AssemblyVersionCompatibility, values: SameDomain (3), SameMachine (1), SameProcess (2) """
    SameDomain: AssemblyVersionCompatibility = ...
    SameMachine: AssemblyVersionCompatibility = ...
    SameProcess: AssemblyVersionCompatibility = ...
    value__ = ...


