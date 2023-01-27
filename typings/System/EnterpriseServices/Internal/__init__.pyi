# encoding: utf-8
# module System.EnterpriseServices.Internal calls itself Internal
# from System.EnterpriseServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, MarshalByRefObject

from System.Reflection import StrongNameKeyPair

from typing import Tuple as Tuple_

"""The following names are not found in the module: (IAppDomainHelper, 
    IAssemblyLocator)
"""

# no functions
# classes

class AppDomainHelper(IAppDomainHelper): # skipped bases: <type 'object'>
    """ AppDomainHelper() """
    pass

class AssemblyLocator(MarshalByRefObject, IAssemblyLocator): # skipped bases: <type 'object'>
    """ AssemblyLocator() """
    pass

class ClientRemotingConfig: # skipped bases: <type 'object'>, <type 'object'>
    """ ClientRemotingConfig() """
    @staticmethod
    def Write(DestinationDirectory:str, VRoot:str, BaseUrl:str, AssemblyName:str, TypeName:str, ProgId:str, Mode:str, Transport:str) -> bool:
        """ Write(DestinationDirectory: str, VRoot: str, BaseUrl: str, AssemblyName: str, TypeName: str, ProgId: str, Mode: str, Transport: str) -> bool """
        ...


class ClrObjectFactory(IClrObjectFactory): # skipped bases: <type 'object'>
    """ ClrObjectFactory() """
    pass

class ComManagedImportUtil(IComManagedImportUtil): # skipped bases: <type 'object'>
    """ ComManagedImportUtil() """
    pass

class ComSoapPublishError: # skipped bases: <type 'object'>, <type 'object'>
    """ ComSoapPublishError() """
    @staticmethod
    def Report(s:str): # -> 
        """ Report(s: str) """
        ...


class GenerateMetadata(IComSoapMetadata): # skipped bases: <type 'object'>
    """ GenerateMetadata() """
    def GenerateMetaData(self, strSrcTypeLib:str, outPath:str, PublicKey:Array, KeyPair:StrongNameKeyPair) -> str:
        """ GenerateMetaData(self: GenerateMetadata, strSrcTypeLib: str, outPath: str, PublicKey: Array[Byte], KeyPair: StrongNameKeyPair) -> str """
        ...

    @staticmethod
    def SearchPath(path:str, fileName:str, extension:str, numBufferChars:int, buffer:str, filePart:Array) -> int:
        """ SearchPath(path: str, fileName: str, extension: str, numBufferChars: int, buffer: str, filePart: Array[int]) -> int """
        ...


class IClrObjectFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateFromAssembly(self, assembly:str, type:str, mode:str) -> object:
        """ CreateFromAssembly(self: IClrObjectFactory, assembly: str, type: str, mode: str) -> object """
        ...

    def CreateFromMailbox(self, Mailbox:str, Mode:str) -> object:
        """ CreateFromMailbox(self: IClrObjectFactory, Mailbox: str, Mode: str) -> object """
        ...

    def CreateFromVroot(self, VrootUrl:str, Mode:str) -> object:
        """ CreateFromVroot(self: IClrObjectFactory, VrootUrl: str, Mode: str) -> object """
        ...

    def CreateFromWsdl(self, WsdlUrl:str, Mode:str) -> object:
        """ CreateFromWsdl(self: IClrObjectFactory, WsdlUrl: str, Mode: str) -> object """
        ...


class IComManagedImportUtil: # skipped bases: <type 'object'>
    """ no doc """
    def GetComponentInfo(self, assemblyPath, numComponents, componentInfo) -> Tuple_[str, str]:
        """ GetComponentInfo(self: IComManagedImportUtil, assemblyPath: str) -> (str, str) """
        ...

    def InstallAssembly(self, filename:str, parname:str, appname:str): # -> 
        """ InstallAssembly(self: IComManagedImportUtil, filename: str, parname: str, appname: str) """
        ...


class IComSoapIISVRoot: # skipped bases: <type 'object'>
    """ no doc """
    def Create(self, RootWeb, PhysicalDirectory, VirtualDirectory, Error) -> str:
        """ Create(self: IComSoapIISVRoot, RootWeb: str, PhysicalDirectory: str, VirtualDirectory: str) -> str """
        ...

    def Delete(self, RootWeb, PhysicalDirectory, VirtualDirectory, Error) -> str:
        """ Delete(self: IComSoapIISVRoot, RootWeb: str, PhysicalDirectory: str, VirtualDirectory: str) -> str """
        ...


class IComSoapMetadata: # skipped bases: <type 'object'>
    """ no doc """
    def Generate(self, SrcTypeLibFileName:str, OutPath:str) -> str:
        """ Generate(self: IComSoapMetadata, SrcTypeLibFileName: str, OutPath: str) -> str """
        ...

    def GenerateSigned(self, SrcTypeLibFileName, OutPath, InstallGac, Error) -> Tuple_[str, str]:
        """ GenerateSigned(self: IComSoapMetadata, SrcTypeLibFileName: str, OutPath: str, InstallGac: bool) -> (str, str) """
        ...


class IComSoapPublisher: # skipped bases: <type 'object'>
    """ no doc """
    def CreateMailBox(self, RootMailServer, MailBox, SmtpName, Domain, PhysicalPath, Error) -> Tuple_[str, str, str, str]:
        """ CreateMailBox(self: IComSoapPublisher, RootMailServer: str, MailBox: str) -> (str, str, str, str) """
        ...

    def CreateVirtualRoot(self, Operation, FullUrl, BaseUrl, VirtualRoot, PhysicalPath, Error) -> Tuple_[str, str, str, str]:
        """ CreateVirtualRoot(self: IComSoapPublisher, Operation: str, FullUrl: str) -> (str, str, str, str) """
        ...

    def DeleteMailBox(self, RootMailServer, MailBox, Error) -> str:
        """ DeleteMailBox(self: IComSoapPublisher, RootMailServer: str, MailBox: str) -> str """
        ...

    def DeleteVirtualRoot(self, RootWebServer, FullUrl, Error) -> str:
        """ DeleteVirtualRoot(self: IComSoapPublisher, RootWebServer: str, FullUrl: str) -> str """
        ...

    def GacInstall(self, AssemblyPath:str): # -> 
        """ GacInstall(self: IComSoapPublisher, AssemblyPath: str) """
        ...

    def GacRemove(self, AssemblyPath:str): # -> 
        """ GacRemove(self: IComSoapPublisher, AssemblyPath: str) """
        ...

    def GetAssemblyNameForCache(self, TypeLibPath, CachePath) -> str:
        """ GetAssemblyNameForCache(self: IComSoapPublisher, TypeLibPath: str) -> str """
        ...

    def GetTypeNameFromProgId(self, AssemblyPath:str, ProgId:str) -> str:
        """ GetTypeNameFromProgId(self: IComSoapPublisher, AssemblyPath: str, ProgId: str) -> str """
        ...

    def ProcessClientTlb(self, ProgId, SrcTlbPath, PhysicalPath, VRoot, BaseUrl, Mode, Transport, AssemblyName, TypeName, Error) -> Tuple_[str, str, str]:
        """ ProcessClientTlb(self: IComSoapPublisher, ProgId: str, SrcTlbPath: str, PhysicalPath: str, VRoot: str, BaseUrl: str, Mode: str, Transport: str) -> (str, str, str) """
        ...

    def ProcessServerTlb(self, ProgId, SrcTlbPath, PhysicalPath, Operation, AssemblyName, TypeName, Error) -> Tuple_[str, str, str]:
        """ ProcessServerTlb(self: IComSoapPublisher, ProgId: str, SrcTlbPath: str, PhysicalPath: str, Operation: str) -> (str, str, str) """
        ...

    def RegisterAssembly(self, AssemblyPath:str): # -> 
        """ RegisterAssembly(self: IComSoapPublisher, AssemblyPath: str) """
        ...

    def UnRegisterAssembly(self, AssemblyPath:str): # -> 
        """ UnRegisterAssembly(self: IComSoapPublisher, AssemblyPath: str) """
        ...


class IISVirtualRoot(IComSoapIISVRoot): # skipped bases: <type 'object'>
    """ IISVirtualRoot() """
    pass

class IServerWebConfig: # skipped bases: <type 'object'>
    """ no doc """
    def AddElement(self, FilePath, AssemblyName, TypeName, ProgId, Mode, Error) -> str:
        """ AddElement(self: IServerWebConfig, FilePath: str, AssemblyName: str, TypeName: str, ProgId: str, Mode: str) -> str """
        ...

    def Create(self, FilePath, FileRootName, Error) -> str:
        """ Create(self: IServerWebConfig, FilePath: str, FileRootName: str) -> str """
        ...


class ISoapClientImport: # skipped bases: <type 'object'>
    """ no doc """
    def ProcessClientTlbEx(self, progId:str, virtualRoot:str, baseUrl:str, authentication:str, assemblyName:str, typeName:str): # -> 
        """ ProcessClientTlbEx(self: ISoapClientImport, progId: str, virtualRoot: str, baseUrl: str, authentication: str, assemblyName: str, typeName: str) """
        ...


class ISoapServerTlb: # skipped bases: <type 'object'>
    """ no doc """
    def AddServerTlb(self, progId, classId, interfaceId, srcTlbPath, rootWebServer, baseUrl, virtualRoot, clientActivated, wellKnown, discoFile, operation, assemblyName, typeName) -> Tuple_[str, str]:
        """ AddServerTlb(self: ISoapServerTlb, progId: str, classId: str, interfaceId: str, srcTlbPath: str, rootWebServer: str, baseUrl: str, virtualRoot: str, clientActivated: str, wellKnown: str, discoFile: str, operation: str) -> (str, str) """
        ...

    def DeleteServerTlb(self, progId:str, classId:str, interfaceId:str, srcTlbPath:str, rootWebServer:str, baseUrl:str, virtualRoot:str, operation:str, assemblyName:str, typeName:str): # -> 
        """ DeleteServerTlb(self: ISoapServerTlb, progId: str, classId: str, interfaceId: str, srcTlbPath: str, rootWebServer: str, baseUrl: str, virtualRoot: str, operation: str, assemblyName: str, typeName: str) """
        ...


class ISoapServerVRoot: # skipped bases: <type 'object'>
    """ no doc """
    def CreateVirtualRootEx(self, rootWebServer, inBaseUrl, inVirtualRoot, homePage, discoFile, secureSockets, authentication, operation, baseUrl, virtualRoot, physicalPath) -> Tuple_[str, str, str]:
        """ CreateVirtualRootEx(self: ISoapServerVRoot, rootWebServer: str, inBaseUrl: str, inVirtualRoot: str, homePage: str, discoFile: str, secureSockets: str, authentication: str, operation: str) -> (str, str, str) """
        ...

    def DeleteVirtualRootEx(self, rootWebServer:str, baseUrl:str, virtualRoot:str): # -> 
        """ DeleteVirtualRootEx(self: ISoapServerVRoot, rootWebServer: str, baseUrl: str, virtualRoot: str) """
        ...

    def GetVirtualRootStatus(self, rootWebServer, inBaseUrl, inVirtualRoot, exists, secureSockets, windowsAuth, anonymous, homePage, discoFile, physicalPath, baseUrl, virtualRoot) -> Tuple_[str, str, str, str, str, str, str, str, str]:
        """ GetVirtualRootStatus(self: ISoapServerVRoot, rootWebServer: str, inBaseUrl: str, inVirtualRoot: str) -> (str, str, str, str, str, str, str, str, str) """
        ...


class ISoapUtility: # skipped bases: <type 'object'>
    """ no doc """
    def GetServerBinPath(self, rootWebServer, inBaseUrl, inVirtualRoot, binPath) -> str:
        """ GetServerBinPath(self: ISoapUtility, rootWebServer: str, inBaseUrl: str, inVirtualRoot: str) -> str """
        ...

    def GetServerPhysicalPath(self, rootWebServer, inBaseUrl, inVirtualRoot, physicalPath) -> str:
        """ GetServerPhysicalPath(self: ISoapUtility, rootWebServer: str, inBaseUrl: str, inVirtualRoot: str) -> str """
        ...

    def Present(self): # -> 
        """ Present(self: ISoapUtility) """
        ...


class Publish(IComSoapPublisher): # skipped bases: <type 'object'>
    """ Publish() """
    @staticmethod
    def GetClientPhysicalPath(CreateDir:bool) -> str:
        """ GetClientPhysicalPath(CreateDir: bool) -> str """
        ...

    @staticmethod
    def ParseUrl(FullUrl, BaseUrl, VirtualRoot) -> Tuple_[str, str]:
        """ ParseUrl(FullUrl: str) -> (str, str) """
        ...


class ServerWebConfig(IServerWebConfig): # skipped bases: <type 'object'>
    """ ServerWebConfig() """
    pass

class SoapClientImport(ISoapClientImport): # skipped bases: <type 'object'>
    """ SoapClientImport() """
    pass

class SoapServerTlb(ISoapServerTlb): # skipped bases: <type 'object'>
    """ SoapServerTlb() """
    pass

class SoapServerVRoot(ISoapServerVRoot): # skipped bases: <type 'object'>
    """ SoapServerVRoot() """
    pass

class SoapUtility(ISoapUtility): # skipped bases: <type 'object'>
    """ SoapUtility() """
    pass

