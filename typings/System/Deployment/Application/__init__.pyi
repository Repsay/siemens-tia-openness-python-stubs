# encoding: utf-8
# module System.Deployment.Application calls itself Application
# from System.Deployment, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (ActivationContext, ApplicationIdentity, AsyncCallback, 
    DateTime, Enum, IAsyncResult, IDisposable, Int64, MulticastDelegate, 
    SystemException, Uri, Version)

from System.Collections import IList

from System.ComponentModel import (AsyncCompletedEventArgs, 
    ProgressChangedEventArgs)

from System.Runtime.Remoting import ObjectHandle

from System.Xml import XmlReader

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class ApplicationDeployment: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ActivationUri(self) -> Uri:
        """ Get: ActivationUri(self: ApplicationDeployment) -> Uri """
        ...

    @property
    def CurrentDeployment(self) -> ApplicationDeployment:
        """ Get: CurrentDeployment() -> ApplicationDeployment """
        ...

    @property
    def CurrentVersion(self) -> Version:
        """ Get: CurrentVersion(self: ApplicationDeployment) -> Version """
        ...

    @property
    def DataDirectory(self) -> str:
        """ Get: DataDirectory(self: ApplicationDeployment) -> str """
        ...

    @property
    def IsFirstRun(self) -> bool:
        """ Get: IsFirstRun(self: ApplicationDeployment) -> bool """
        ...

    @property
    def IsNetworkDeployed(self) -> bool:
        """ Get: IsNetworkDeployed() -> bool """
        ...

    @property
    def TimeOfLastUpdateCheck(self) -> DateTime:
        """ Get: TimeOfLastUpdateCheck(self: ApplicationDeployment) -> DateTime """
        ...

    @property
    def UpdatedApplicationFullName(self) -> str:
        """ Get: UpdatedApplicationFullName(self: ApplicationDeployment) -> str """
        ...

    @property
    def UpdatedVersion(self) -> Version:
        """ Get: UpdatedVersion(self: ApplicationDeployment) -> Version """
        ...

    @property
    def UpdateLocation(self) -> Uri:
        """ Get: UpdateLocation(self: ApplicationDeployment) -> Uri """
        ...


    def CheckForDetailedUpdate(self, persistUpdateCheckResult:bool = ...) -> UpdateCheckInfo:
        """
        CheckForDetailedUpdate(self: ApplicationDeployment) -> UpdateCheckInfo
        CheckForDetailedUpdate(self: ApplicationDeployment, persistUpdateCheckResult: bool) -> UpdateCheckInfo
        """
        ...

    def CheckForUpdate(self, persistUpdateCheckResult:bool = ...) -> bool:
        """
        CheckForUpdate(self: ApplicationDeployment) -> bool
        CheckForUpdate(self: ApplicationDeployment, persistUpdateCheckResult: bool) -> bool
        """
        ...

    def CheckForUpdateAsync(self): # -> 
        """ CheckForUpdateAsync(self: ApplicationDeployment) """
        ...

    def CheckForUpdateAsyncCancel(self): # -> 
        """ CheckForUpdateAsyncCancel(self: ApplicationDeployment) """
        ...

    def DownloadFileGroup(self, groupName:str): # -> 
        """ DownloadFileGroup(self: ApplicationDeployment, groupName: str) """
        ...

    def DownloadFileGroupAsync(self, groupName:str, userState:object = ...): # -> 
        """ DownloadFileGroupAsync(self: ApplicationDeployment, groupName: str)DownloadFileGroupAsync(self: ApplicationDeployment, groupName: str, userState: object) """
        ...

    def DownloadFileGroupAsyncCancel(self, groupName:str): # -> 
        """ DownloadFileGroupAsyncCancel(self: ApplicationDeployment, groupName: str) """
        ...

    def IsFileGroupDownloaded(self, groupName:str) -> bool:
        """ IsFileGroupDownloaded(self: ApplicationDeployment, groupName: str) -> bool """
        ...

    def Update(self) -> bool:
        """ Update(self: ApplicationDeployment) -> bool """
        ...

    def UpdateAsync(self): # -> 
        """ UpdateAsync(self: ApplicationDeployment) """
        ...

    def UpdateAsyncCancel(self): # -> 
        """ UpdateAsyncCancel(self: ApplicationDeployment) """
        ...

    CheckForUpdateCompleted = ...
    CheckForUpdateProgressChanged = ...
    DownloadFileGroupCompleted = ...
    DownloadFileGroupProgressChanged = ...
    UpdateCompleted = ...
    UpdateProgressChanged = ...


class CheckForUpdateCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AvailableVersion(self) -> Version:
        """ Get: AvailableVersion(self: CheckForUpdateCompletedEventArgs) -> Version """
        ...

    @property
    def IsUpdateRequired(self) -> bool:
        """ Get: IsUpdateRequired(self: CheckForUpdateCompletedEventArgs) -> bool """
        ...

    @property
    def MinimumRequiredVersion(self) -> Version:
        """ Get: MinimumRequiredVersion(self: CheckForUpdateCompletedEventArgs) -> Version """
        ...

    @property
    def UpdateAvailable(self) -> bool:
        """ Get: UpdateAvailable(self: CheckForUpdateCompletedEventArgs) -> bool """
        ...

    @property
    def UpdateSizeBytes(self) -> Int64:
        """ Get: UpdateSizeBytes(self: CheckForUpdateCompletedEventArgs) -> Int64 """
        ...



class CheckForUpdateCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CheckForUpdateCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:CheckForUpdateCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: CheckForUpdateCompletedEventHandler, sender: object, e: CheckForUpdateCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: CheckForUpdateCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:CheckForUpdateCompletedEventArgs): # -> 
        """ Invoke(self: CheckForUpdateCompletedEventHandler, sender: object, e: CheckForUpdateCompletedEventArgs) """
        ...


class CompatibleFramework: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Profile(self) -> str:
        """ Get: Profile(self: CompatibleFramework) -> str """
        ...

    @property
    def SupportedRuntime(self) -> str:
        """ Get: SupportedRuntime(self: CompatibleFramework) -> str """
        ...

    @property
    def TargetVersion(self) -> str:
        """ Get: TargetVersion(self: CompatibleFramework) -> str """
        ...



class DeploymentException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DeploymentException()
    DeploymentException(message: str)
    DeploymentException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class DependentPlatformMissingException(DeploymentException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DependentPlatformMissingException()
    DependentPlatformMissingException(message: str)
    DependentPlatformMissingException(message: str, innerException: Exception)
    DependentPlatformMissingException(message: str, supportUrl: Uri)
    """
    @property
    def SupportUrl(self) -> Uri:
        """ Get: SupportUrl(self: DependentPlatformMissingException) -> Uri """
        ...


    SerializeObjectState = ...


class CompatibleFrameworkMissingException(DependentPlatformMissingException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CompatibleFrameworkMissingException()
    CompatibleFrameworkMissingException(message: str)
    CompatibleFrameworkMissingException(message: str, innerException: Exception)
    """
    @property
    def CompatibleFrameworks(self) -> CompatibleFrameworks:
        """ Get: CompatibleFrameworks(self: CompatibleFrameworkMissingException) -> CompatibleFrameworks """
        ...


    SerializeObjectState = ...


class CompatibleFrameworks: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Frameworks(self) -> IList:
        """ Get: Frameworks(self: CompatibleFrameworks) -> IList[CompatibleFramework] """
        ...

    @property
    def SupportUrl(self) -> Uri:
        """ Get: SupportUrl(self: CompatibleFrameworks) -> Uri """
        ...



class DeploymentDownloadException(DeploymentException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DeploymentDownloadException()
    DeploymentDownloadException(message: str)
    DeploymentDownloadException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class DeploymentProgressChangedEventArgs(ProgressChangedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BytesCompleted(self) -> Int64:
        """ Get: BytesCompleted(self: DeploymentProgressChangedEventArgs) -> Int64 """
        ...

    @property
    def BytesTotal(self) -> Int64:
        """ Get: BytesTotal(self: DeploymentProgressChangedEventArgs) -> Int64 """
        ...

    @property
    def Group(self) -> str:
        """ Get: Group(self: DeploymentProgressChangedEventArgs) -> str """
        ...

    @property
    def State(self) -> DeploymentProgressState:
        """ Get: State(self: DeploymentProgressChangedEventArgs) -> DeploymentProgressState """
        ...



class DeploymentProgressChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DeploymentProgressChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DeploymentProgressChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DeploymentProgressChangedEventHandler, sender: object, e: DeploymentProgressChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DeploymentProgressChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DeploymentProgressChangedEventArgs): # -> 
        """ Invoke(self: DeploymentProgressChangedEventHandler, sender: object, e: DeploymentProgressChangedEventArgs) """
        ...


class DeploymentProgressState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DeploymentProgressState, values: DownloadingApplicationFiles (2), DownloadingApplicationInformation (1), DownloadingDeploymentInformation (0) """
    DownloadingApplicationFiles: DeploymentProgressState = ...
    DownloadingApplicationInformation: DeploymentProgressState = ...
    DownloadingDeploymentInformation: DeploymentProgressState = ...
    value__ = ...


class DeploymentServiceCom: # skipped bases: <type 'object'>, <type 'object'>
    """ DeploymentServiceCom() """
    def ActivateApplicationExtension(self, textualSubId:str, deploymentProviderUrl:str, targetAssociatedFile:str): # -> 
        """ ActivateApplicationExtension(self: DeploymentServiceCom, textualSubId: str, deploymentProviderUrl: str, targetAssociatedFile: str) """
        ...

    def ActivateDeployment(self, deploymentLocation:str, isShortcut:bool): # -> 
        """ ActivateDeployment(self: DeploymentServiceCom, deploymentLocation: str, isShortcut: bool) """
        ...

    def ActivateDeploymentEx(self, deploymentLocation:str, unsignedPolicy:int, signedPolicy:int): # -> 
        """ ActivateDeploymentEx(self: DeploymentServiceCom, deploymentLocation: str, unsignedPolicy: int, signedPolicy: int) """
        ...

    def CheckForDeploymentUpdate(self, textualSubId:str): # -> 
        """ CheckForDeploymentUpdate(self: DeploymentServiceCom, textualSubId: str) """
        ...

    def CleanOnlineAppCache(self): # -> 
        """ CleanOnlineAppCache(self: DeploymentServiceCom) """
        ...

    def EndServiceRightNow(self): # -> 
        """ EndServiceRightNow(self: DeploymentServiceCom) """
        ...

    def MaintainSubscription(self, textualSubId:str): # -> 
        """ MaintainSubscription(self: DeploymentServiceCom, textualSubId: str) """
        ...


class DownloadApplicationCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LogFilePath(self) -> str:
        """ Get: LogFilePath(self: DownloadApplicationCompletedEventArgs) -> str """
        ...

    @property
    def ShortcutAppId(self) -> str:
        """ Get: ShortcutAppId(self: DownloadApplicationCompletedEventArgs) -> str """
        ...



class DownloadFileGroupCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Group(self) -> str:
        """ Get: Group(self: DownloadFileGroupCompletedEventArgs) -> str """
        ...



class DownloadFileGroupCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DownloadFileGroupCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DownloadFileGroupCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DownloadFileGroupCompletedEventHandler, sender: object, e: DownloadFileGroupCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DownloadFileGroupCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DownloadFileGroupCompletedEventArgs): # -> 
        """ Invoke(self: DownloadFileGroupCompletedEventHandler, sender: object, e: DownloadFileGroupCompletedEventArgs) """
        ...


class DownloadProgressChangedEventArgs(ProgressChangedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BytesDownloaded(self) -> Int64:
        """ Get: BytesDownloaded(self: DownloadProgressChangedEventArgs) -> Int64 """
        ...

    @property
    def State(self) -> DeploymentProgressState:
        """ Get: State(self: DownloadProgressChangedEventArgs) -> DeploymentProgressState """
        ...

    @property
    def TotalBytesToDownload(self) -> Int64:
        """ Get: TotalBytesToDownload(self: DownloadProgressChangedEventArgs) -> Int64 """
        ...



class GetManifestCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActivationContext(self) -> ActivationContext:
        """ Get: ActivationContext(self: GetManifestCompletedEventArgs) -> ActivationContext """
        ...

    @property
    def ApplicationIdentity(self) -> ApplicationIdentity:
        """ Get: ApplicationIdentity(self: GetManifestCompletedEventArgs) -> ApplicationIdentity """
        ...

    @property
    def ApplicationManifest(self) -> XmlReader:
        """ Get: ApplicationManifest(self: GetManifestCompletedEventArgs) -> XmlReader """
        ...

    @property
    def DeploymentManifest(self) -> XmlReader:
        """ Get: DeploymentManifest(self: GetManifestCompletedEventArgs) -> XmlReader """
        ...

    @property
    def IsCached(self) -> bool:
        """ Get: IsCached(self: GetManifestCompletedEventArgs) -> bool """
        ...

    @property
    def LogFilePath(self) -> str:
        """ Get: LogFilePath(self: GetManifestCompletedEventArgs) -> str """
        ...

    @property
    def ProductName(self) -> str:
        """ Get: ProductName(self: GetManifestCompletedEventArgs) -> str """
        ...

    @property
    def SubscriptionIdentity(self) -> str:
        """ Get: SubscriptionIdentity(self: GetManifestCompletedEventArgs) -> str """
        ...

    @property
    def SupportUri(self) -> Uri:
        """ Get: SupportUri(self: GetManifestCompletedEventArgs) -> Uri """
        ...

    @property
    def Version(self) -> Version:
        """ Get: Version(self: GetManifestCompletedEventArgs) -> Version """
        ...



class InPlaceHostingManager(IDisposable): # skipped bases: <type 'object'>
    """
    InPlaceHostingManager(deploymentManifest: Uri, launchInHostProcess: bool)
    InPlaceHostingManager(deploymentManifest: Uri)
    """
    def AssertApplicationRequirements(self, grantApplicationTrust:bool = ...): # -> 
        """ AssertApplicationRequirements(self: InPlaceHostingManager)AssertApplicationRequirements(self: InPlaceHostingManager, grantApplicationTrust: bool) """
        ...

    def CancelAsync(self): # -> 
        """ CancelAsync(self: InPlaceHostingManager) """
        ...

    def DownloadApplicationAsync(self): # -> 
        """ DownloadApplicationAsync(self: InPlaceHostingManager) """
        ...

    def Execute(self) -> ObjectHandle:
        """ Execute(self: InPlaceHostingManager) -> ObjectHandle """
        ...

    def GetManifestAsync(self): # -> 
        """ GetManifestAsync(self: InPlaceHostingManager) """
        ...

    @staticmethod
    def UninstallCustomAddIn(subscriptionId:str): # -> 
        """ UninstallCustomAddIn(subscriptionId: str) """
        ...

    @staticmethod
    def UninstallCustomUXApplication(subscriptionId:str): # -> 
        """ UninstallCustomUXApplication(subscriptionId: str) """
        ...

    DownloadApplicationCompleted = ...
    DownloadProgressChanged = ...
    GetManifestCompleted = ...


class InvalidDeploymentException(DeploymentException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidDeploymentException()
    InvalidDeploymentException(message: str)
    InvalidDeploymentException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SupportedRuntimeMissingException(DependentPlatformMissingException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SupportedRuntimeMissingException()
    SupportedRuntimeMissingException(message: str)
    SupportedRuntimeMissingException(message: str, innerException: Exception)
    """
    @property
    def SupportedRuntimeVersion(self) -> str:
        """ Get: SupportedRuntimeVersion(self: SupportedRuntimeMissingException) -> str """
        ...


    SerializeObjectState = ...


class TrustNotGrantedException(DeploymentException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TrustNotGrantedException()
    TrustNotGrantedException(message: str)
    TrustNotGrantedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class UpdateCheckInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AvailableVersion(self) -> Version:
        """ Get: AvailableVersion(self: UpdateCheckInfo) -> Version """
        ...

    @property
    def IsUpdateRequired(self) -> bool:
        """ Get: IsUpdateRequired(self: UpdateCheckInfo) -> bool """
        ...

    @property
    def MinimumRequiredVersion(self) -> Version:
        """ Get: MinimumRequiredVersion(self: UpdateCheckInfo) -> Version """
        ...

    @property
    def UpdateAvailable(self) -> bool:
        """ Get: UpdateAvailable(self: UpdateCheckInfo) -> bool """
        ...

    @property
    def UpdateSizeBytes(self) -> Int64:
        """ Get: UpdateSizeBytes(self: UpdateCheckInfo) -> Int64 """
        ...



