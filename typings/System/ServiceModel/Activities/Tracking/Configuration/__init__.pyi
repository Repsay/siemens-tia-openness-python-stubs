# encoding: utf-8
# module System.ServiceModel.Activities.Tracking.Configuration calls itself Configuration
# from System.ServiceModel.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Activities.Tracking import ImplementationVisibility

from System.Collections.ObjectModel import Collection

from System.Configuration import (ConfigurationElement, 
    ConfigurationElementCollection, ConfigurationSection)

"""The following names are not found in the module: TConfigurationElement
"""

# no functions
# classes

class TrackingConfigurationElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ElementKey(self) -> object:
        """ Get: ElementKey(self: TrackingConfigurationElement) -> object """
        ...


    def GetStringPairKey(self, *args): #cannot find CLR method
        """ GetStringPairKey(value1: str, value2: str) -> str """
        ...


class TrackingQueryElement(TrackingConfigurationElement): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Annotations(self) -> AnnotationElementCollection:
        """ Get: Annotations(self: TrackingQueryElement) -> AnnotationElementCollection """
        ...


    def NewTrackingQuery(self, *args): #cannot find CLR method
        """ NewTrackingQuery(self: TrackingQueryElement) -> TrackingQuery """
        ...

    def UpdateTrackingQuery(self, *args): #cannot find CLR method
        """ UpdateTrackingQuery(self: TrackingQueryElement, trackingQuery: TrackingQuery) """
        ...


class ActivityScheduledQueryElement(TrackingQueryElement): # skipped bases: <type 'object'>
    """ ActivityScheduledQueryElement() """
    @property
    def ActivityName(self) -> str:
        """
        Get: ActivityName(self: ActivityScheduledQueryElement) -> str
        Set: ActivityName(self: ActivityScheduledQueryElement) = value
        """
        ...

    @property
    def ChildActivityName(self) -> str:
        """
        Get: ChildActivityName(self: ActivityScheduledQueryElement) -> str
        Set: ChildActivityName(self: ActivityScheduledQueryElement) = value
        """
        ...



class ActivityScheduledQueryElementCollection(TrackingConfigurationCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ActivityScheduledQueryElementCollection() """
    pass

class ActivityStateQueryElement(TrackingQueryElement): # skipped bases: <type 'object'>
    """ ActivityStateQueryElement() """
    @property
    def ActivityName(self) -> str:
        """
        Get: ActivityName(self: ActivityStateQueryElement) -> str
        Set: ActivityName(self: ActivityStateQueryElement) = value
        """
        ...

    @property
    def Arguments(self) -> ArgumentElementCollection:
        """ Get: Arguments(self: ActivityStateQueryElement) -> ArgumentElementCollection """
        ...

    @property
    def States(self) -> StateElementCollection:
        """ Get: States(self: ActivityStateQueryElement) -> StateElementCollection """
        ...

    @property
    def Variables(self) -> VariableElementCollection:
        """ Get: Variables(self: ActivityStateQueryElement) -> VariableElementCollection """
        ...



class ActivityStateQueryElementCollection(TrackingConfigurationCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ActivityStateQueryElementCollection() """
    pass

class AnnotationElement(TrackingConfigurationElement): # skipped bases: <type 'object'>
    """ AnnotationElement() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: AnnotationElement) -> str
        Set: Name(self: AnnotationElement) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: AnnotationElement) -> str
        Set: Value(self: AnnotationElement) = value
        """
        ...



class AnnotationElementCollection(TrackingConfigurationCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ AnnotationElementCollection() """
    pass

class ArgumentElement(TrackingConfigurationElement): # skipped bases: <type 'object'>
    """ ArgumentElement() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: ArgumentElement) -> str
        Set: Name(self: ArgumentElement) = value
        """
        ...



class ArgumentElementCollection(TrackingConfigurationCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ArgumentElementCollection() """
    pass

class BookmarkResumptionQueryElement(TrackingQueryElement): # skipped bases: <type 'object'>
    """ BookmarkResumptionQueryElement() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: BookmarkResumptionQueryElement) -> str
        Set: Name(self: BookmarkResumptionQueryElement) = value
        """
        ...



class BookmarkResumptionQueryElementCollection(TrackingConfigurationCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ BookmarkResumptionQueryElementCollection() """
    pass

class CancelRequestedQueryElement(TrackingQueryElement): # skipped bases: <type 'object'>
    """ CancelRequestedQueryElement() """
    @property
    def ActivityName(self) -> str:
        """
        Get: ActivityName(self: CancelRequestedQueryElement) -> str
        Set: ActivityName(self: CancelRequestedQueryElement) = value
        """
        ...

    @property
    def ChildActivityName(self) -> str:
        """
        Get: ChildActivityName(self: CancelRequestedQueryElement) -> str
        Set: ChildActivityName(self: CancelRequestedQueryElement) = value
        """
        ...



class CancelRequestedQueryElementCollection(TrackingConfigurationCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ CancelRequestedQueryElementCollection() """
    pass

class CustomTrackingQueryElement(TrackingQueryElement): # skipped bases: <type 'object'>
    """ CustomTrackingQueryElement() """
    @property
    def ActivityName(self) -> str:
        """
        Get: ActivityName(self: CustomTrackingQueryElement) -> str
        Set: ActivityName(self: CustomTrackingQueryElement) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CustomTrackingQueryElement) -> str
        Set: Name(self: CustomTrackingQueryElement) = value
        """
        ...



class CustomTrackingQueryElementCollection(TrackingConfigurationCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ CustomTrackingQueryElementCollection() """
    pass

class FaultPropagationQueryElement(TrackingQueryElement): # skipped bases: <type 'object'>
    """ FaultPropagationQueryElement() """
    @property
    def FaultHandlerActivityName(self) -> str:
        """
        Get: FaultHandlerActivityName(self: FaultPropagationQueryElement) -> str
        Set: FaultHandlerActivityName(self: FaultPropagationQueryElement) = value
        """
        ...

    @property
    def FaultSourceActivityName(self) -> str:
        """
        Get: FaultSourceActivityName(self: FaultPropagationQueryElement) -> str
        Set: FaultSourceActivityName(self: FaultPropagationQueryElement) = value
        """
        ...



class FaultPropagationQueryElementCollection(TrackingConfigurationCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ FaultPropagationQueryElementCollection() """
    pass

class ProfileElement(TrackingConfigurationElement): # skipped bases: <type 'object'>
    """ ProfileElement() """
    @property
    def ImplementationVisibility(self) -> ImplementationVisibility:
        """
        Get: ImplementationVisibility(self: ProfileElement) -> ImplementationVisibility
        Set: ImplementationVisibility(self: ProfileElement) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ProfileElement) -> str
        Set: Name(self: ProfileElement) = value
        """
        ...

    @property
    def Workflows(self) -> ProfileWorkflowElementCollection:
        """ Get: Workflows(self: ProfileElement) -> ProfileWorkflowElementCollection """
        ...



class ProfileElementCollection(TrackingConfigurationCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class ProfileWorkflowElement(TrackingConfigurationElement): # skipped bases: <type 'object'>
    """ ProfileWorkflowElement() """
    @property
    def ActivityDefinitionId(self) -> str:
        """
        Get: ActivityDefinitionId(self: ProfileWorkflowElement) -> str
        Set: ActivityDefinitionId(self: ProfileWorkflowElement) = value
        """
        ...

    @property
    def ActivityScheduledQueries(self) -> ActivityScheduledQueryElementCollection:
        """ Get: ActivityScheduledQueries(self: ProfileWorkflowElement) -> ActivityScheduledQueryElementCollection """
        ...

    @property
    def ActivityStateQueries(self) -> ActivityStateQueryElementCollection:
        """ Get: ActivityStateQueries(self: ProfileWorkflowElement) -> ActivityStateQueryElementCollection """
        ...

    @property
    def BookmarkResumptionQueries(self) -> BookmarkResumptionQueryElementCollection:
        """ Get: BookmarkResumptionQueries(self: ProfileWorkflowElement) -> BookmarkResumptionQueryElementCollection """
        ...

    @property
    def CancelRequestedQueries(self) -> CancelRequestedQueryElementCollection:
        """ Get: CancelRequestedQueries(self: ProfileWorkflowElement) -> CancelRequestedQueryElementCollection """
        ...

    @property
    def CustomTrackingQueries(self) -> CustomTrackingQueryElementCollection:
        """ Get: CustomTrackingQueries(self: ProfileWorkflowElement) -> CustomTrackingQueryElementCollection """
        ...

    @property
    def FaultPropagationQueries(self) -> FaultPropagationQueryElementCollection:
        """ Get: FaultPropagationQueries(self: ProfileWorkflowElement) -> FaultPropagationQueryElementCollection """
        ...

    @property
    def StateMachineStateQueries(self) -> StateMachineStateQueryElementCollection:
        """ Get: StateMachineStateQueries(self: ProfileWorkflowElement) -> StateMachineStateQueryElementCollection """
        ...

    @property
    def WorkflowInstanceQueries(self) -> WorkflowInstanceQueryElementCollection:
        """ Get: WorkflowInstanceQueries(self: ProfileWorkflowElement) -> WorkflowInstanceQueryElementCollection """
        ...



class ProfileWorkflowElementCollection(TrackingConfigurationCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ProfileWorkflowElementCollection() """
    pass

class StateElement(TrackingConfigurationElement): # skipped bases: <type 'object'>
    """ StateElement() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: StateElement) -> str
        Set: Name(self: StateElement) = value
        """
        ...



class StateElementCollection(TrackingConfigurationCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ StateElementCollection() """
    pass

class StateMachineStateQueryElement(TrackingQueryElement): # skipped bases: <type 'object'>
    """ StateMachineStateQueryElement() """
    @property
    def ActivityName(self) -> str:
        """
        Get: ActivityName(self: StateMachineStateQueryElement) -> str
        Set: ActivityName(self: StateMachineStateQueryElement) = value
        """
        ...



class StateMachineStateQueryElementCollection(TrackingConfigurationCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ StateMachineStateQueryElementCollection() """
    pass

class TrackingConfigurationCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ TrackingConfigurationCollection[TConfigurationElement]() """
    def Add(self, element): # ->  # Not found arg types: {'element': 'TConfigurationElement'}
        """ Add(self: TrackingConfigurationCollection[TConfigurationElement], element: TConfigurationElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: TrackingConfigurationCollection[TConfigurationElement]) """
        ...

    def IndexOf(self, element) -> int: # Not found arg types: {'element': 'TConfigurationElement'}
        """ IndexOf(self: TrackingConfigurationCollection[TConfigurationElement], element: TConfigurationElement) -> int """
        ...

    def Remove(self, element): # ->  # Not found arg types: {'element': 'TConfigurationElement'}
        """ Remove(self: TrackingConfigurationCollection[TConfigurationElement], element: TConfigurationElement) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: TrackingConfigurationCollection[TConfigurationElement], index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class TrackingSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ TrackingSection() """
    @property
    def Profiles(self) -> ProfileElementCollection:
        """ Get: Profiles(self: TrackingSection) -> ProfileElementCollection """
        ...

    @property
    def TrackingProfiles(self) -> Collection:
        """ Get: TrackingProfiles(self: TrackingSection) -> Collection[TrackingProfile] """
        ...



class VariableElement(TrackingConfigurationElement): # skipped bases: <type 'object'>
    """ VariableElement() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: VariableElement) -> str
        Set: Name(self: VariableElement) = value
        """
        ...



class VariableElementCollection(TrackingConfigurationCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ VariableElementCollection() """
    pass

class WorkflowInstanceQueryElement(TrackingQueryElement): # skipped bases: <type 'object'>
    """ WorkflowInstanceQueryElement() """
    @property
    def States(self) -> StateElementCollection:
        """ Get: States(self: WorkflowInstanceQueryElement) -> StateElementCollection """
        ...



class WorkflowInstanceQueryElementCollection(TrackingConfigurationCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ WorkflowInstanceQueryElementCollection() """
    pass

