# coding: utf-8

"""
    Python SDK for Opsgenie REST API

    Python SDK for Opsgenie REST API  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@opsgenie.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SnoozeAlertPayloadAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'end_time': 'datetime'
    }

    attribute_map = {
        'end_time': 'endTime'
    }

    def __init__(self, end_time=None):  # noqa: E501
        """SnoozeAlertPayloadAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._end_time = None
        self.discriminator = None

        self.end_time = end_time

    @property
    def end_time(self):
        """Gets the end_time of this SnoozeAlertPayloadAllOf.  # noqa: E501

        Date and time that snooze will lose effect  # noqa: E501

        :return: The end_time of this SnoozeAlertPayloadAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SnoozeAlertPayloadAllOf.

        Date and time that snooze will lose effect  # noqa: E501

        :param end_time: The end_time of this SnoozeAlertPayloadAllOf.  # noqa: E501
        :type: datetime
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SnoozeAlertPayloadAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
