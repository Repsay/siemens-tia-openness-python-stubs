# encoding: utf-8
# module Microsoft.Win32.SafeHandles calls itself SafeHandles
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Runtime.InteropServices import (CriticalHandle, SafeBuffer, 
    SafeHandle)

"""The following names are not found in the module: field#
"""

# no functions
# classes

class CriticalHandleMinusOneIsInvalid(CriticalHandle): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    handle = ...


class CriticalHandleZeroOrMinusOneIsInvalid(CriticalHandle): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    handle = ...


class SafeAccessTokenHandle(SafeHandle): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ SafeAccessTokenHandle(handle: IntPtr) """
    @property
    def InvalidHandle(self) -> SafeAccessTokenHandle:
        """ Get: InvalidHandle() -> SafeAccessTokenHandle """
        ...


    handle = ...


class SafeHandleZeroOrMinusOneIsInvalid(SafeHandle): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    handle = ...


class SafeFileHandle(SafeHandleZeroOrMinusOneIsInvalid): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ SafeFileHandle(preexistingHandle: IntPtr, ownsHandle: bool) """
    handle = ...


class SafeHandleMinusOneIsInvalid(SafeHandle): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    handle = ...


class SafeMemoryMappedFileHandle(SafeHandleZeroOrMinusOneIsInvalid): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    handle = ...


class SafeMemoryMappedViewHandle(SafeBuffer): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    handle = ...


class SafeNCryptHandle(SafeHandleZeroOrMinusOneIsInvalid): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    def ReleaseNativeHandle(self, *args): #cannot find CLR method
        """ ReleaseNativeHandle(self: SafeNCryptHandle) -> bool """
        ...

    handle = ...


class SafeNCryptKeyHandle(SafeNCryptHandle): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    SafeNCryptKeyHandle()
    SafeNCryptKeyHandle(handle: IntPtr, parentHandle: SafeHandle)
    """
    handle = ...


class SafeNCryptProviderHandle(SafeNCryptHandle): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ SafeNCryptProviderHandle() """
    handle = ...


class SafeNCryptSecretHandle(SafeNCryptHandle): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ SafeNCryptSecretHandle() """
    handle = ...


class SafePipeHandle(SafeHandleZeroOrMinusOneIsInvalid): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ SafePipeHandle(preexistingHandle: IntPtr, ownsHandle: bool) """
    handle = ...


class SafeProcessHandle(SafeHandleZeroOrMinusOneIsInvalid): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ SafeProcessHandle(existingHandle: IntPtr, ownsHandle: bool) """
    handle = ...


class SafeRegistryHandle(SafeHandleZeroOrMinusOneIsInvalid): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ SafeRegistryHandle(preexistingHandle: IntPtr, ownsHandle: bool) """
    handle = ...


class SafeWaitHandle(SafeHandleZeroOrMinusOneIsInvalid): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ SafeWaitHandle(existingHandle: IntPtr, ownsHandle: bool) """
    handle = ...


class SafeX509ChainHandle(SafeHandleZeroOrMinusOneIsInvalid): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    handle = ...


