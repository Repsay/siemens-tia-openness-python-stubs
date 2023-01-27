# encoding: utf-8
# module System.ServiceModel.ComIntegration calls itself ComIntegration
# from System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import ContextBoundObject

from System.EnterpriseServices import IProcessInitializer

from System.ServiceModel.Activation import ServiceHostFactoryBase

"""The following names are not found in the module: IExtensibleDataObject, T
"""

# no functions
# classes

class DllHostInitializer(IProcessInitializer): # skipped bases: <type 'object'>
    """ DllHostInitializer() """
    pass

class IChannelCredentials: # skipped bases: <type 'object'>
    """ no doc """
    def SetClientCertificateFromFile(self, fileName:str, password:str, keyStorageFlags:str): # -> 
        """ SetClientCertificateFromFile(self: IChannelCredentials, fileName: str, password: str, keyStorageFlags: str) """
        ...

    def SetClientCertificateFromStore(self, storeLocation:str, storeName:str, findType:str, findValue:object): # -> 
        """ SetClientCertificateFromStore(self: IChannelCredentials, storeLocation: str, storeName: str, findType: str, findValue: object) """
        ...

    def SetClientCertificateFromStoreByName(self, subjectName:str, storeLocation:str, storeName:str): # -> 
        """ SetClientCertificateFromStoreByName(self: IChannelCredentials, subjectName: str, storeLocation: str, storeName: str) """
        ...

    def SetDefaultServiceCertificateFromFile(self, fileName:str, password:str, keyStorageFlags:str): # -> 
        """ SetDefaultServiceCertificateFromFile(self: IChannelCredentials, fileName: str, password: str, keyStorageFlags: str) """
        ...

    def SetDefaultServiceCertificateFromStore(self, storeLocation:str, storeName:str, findType:str, findValue:object): # -> 
        """ SetDefaultServiceCertificateFromStore(self: IChannelCredentials, storeLocation: str, storeName: str, findType: str, findValue: object) """
        ...

    def SetDefaultServiceCertificateFromStoreByName(self, subjectName:str, storeLocation:str, storeName:str): # -> 
        """ SetDefaultServiceCertificateFromStoreByName(self: IChannelCredentials, subjectName: str, storeLocation: str, storeName: str) """
        ...

    def SetIssuedToken(self, localIssuerAddres:str, localIssuerBindingType:str, localIssuerBinding:str): # -> 
        """ SetIssuedToken(self: IChannelCredentials, localIssuerAddres: str, localIssuerBindingType: str, localIssuerBinding: str) """
        ...

    def SetServiceCertificateAuthentication(self, storeLocation:str, revocationMode:str, certificationValidationMode:str): # -> 
        """ SetServiceCertificateAuthentication(self: IChannelCredentials, storeLocation: str, revocationMode: str, certificationValidationMode: str) """
        ...

    def SetUserNameCredential(self, userName:str, password:str): # -> 
        """ SetUserNameCredential(self: IChannelCredentials, userName: str, password: str) """
        ...

    def SetWindowsCredential(self, domain:str, userName:str, password:str, impersonationLevel:int, allowNtlm:bool): # -> 
        """ SetWindowsCredential(self: IChannelCredentials, domain: str, userName: str, password: str, impersonationLevel: int, allowNtlm: bool) """
        ...


class PersistStreamTypeWrapper(IExtensibleDataObject): # skipped bases: <type 'object'>
    """ PersistStreamTypeWrapper() """
    def GetObject(self, obj): # -> T # Not found arg types: {'obj': 'T'}
        """ GetObject[T](self: PersistStreamTypeWrapper, obj: T) -> T """
        ...

    def SetObject(self, obj): # ->  # Not found arg types: {'obj': 'T'}
        """ SetObject[T](self: PersistStreamTypeWrapper, obj: T) """
        ...


class ServiceMoniker(ContextBoundObject): # skipped bases: <type 'object'>
    """ ServiceMoniker() """
    pass

class WasHostedComPlusFactory(ServiceHostFactoryBase): # skipped bases: <type 'object'>
    """ WasHostedComPlusFactory() """
    pass

