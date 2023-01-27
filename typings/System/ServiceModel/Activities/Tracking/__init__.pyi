# encoding: utf-8
# module System.ServiceModel.Activities.Tracking calls itself Tracking
# from System.ServiceModel.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Guid

from System.Activities.Tracking import CustomTrackingRecord


# no functions
# classes

class ReceiveMessageRecord(CustomTrackingRecord): # skipped bases: <type 'object'>
    """ ReceiveMessageRecord(name: str) """
    @property
    def E2EActivityId(self) -> Guid:
        """ Get: E2EActivityId(self: ReceiveMessageRecord) -> Guid """
        ...

    @property
    def MessageId(self) -> Guid:
        """ Get: MessageId(self: ReceiveMessageRecord) -> Guid """
        ...



class SendMessageRecord(CustomTrackingRecord): # skipped bases: <type 'object'>
    """ SendMessageRecord(name: str) """
    @property
    def E2EActivityId(self) -> Guid:
        """
        Get: E2EActivityId(self: SendMessageRecord) -> Guid
        Set: E2EActivityId(self: SendMessageRecord) = value
        """
        ...



# variables with complex values

