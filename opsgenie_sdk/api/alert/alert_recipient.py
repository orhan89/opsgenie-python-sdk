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


class AlertRecipient(object):
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
        'user': 'AlertUserMeta',
        'state': 'str',
        'method': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'user': 'user',
        'state': 'state',
        'method': 'method',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, user=None, state=None, method=None, created_at=None, updated_at=None):  # noqa: E501
        """AlertRecipient - a model defined in OpenAPI"""  # noqa: E501

        self._user = None
        self._state = None
        self._method = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if state is not None:
            self.state = state
        if method is not None:
            self.method = method
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this AlertRecipient.  # noqa: E501


        :return: The user of this AlertRecipient.  # noqa: E501
        :rtype: AlertUserMeta
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AlertRecipient.


        :param user: The user of this AlertRecipient.  # noqa: E501
        :type: AlertUserMeta
        """

        self._user = user

    @property
    def state(self):
        """Gets the state of this AlertRecipient.  # noqa: E501


        :return: The state of this AlertRecipient.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AlertRecipient.


        :param state: The state of this AlertRecipient.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def method(self):
        """Gets the method of this AlertRecipient.  # noqa: E501


        :return: The method of this AlertRecipient.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this AlertRecipient.


        :param method: The method of this AlertRecipient.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def created_at(self):
        """Gets the created_at of this AlertRecipient.  # noqa: E501


        :return: The created_at of this AlertRecipient.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AlertRecipient.


        :param created_at: The created_at of this AlertRecipient.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AlertRecipient.  # noqa: E501


        :return: The updated_at of this AlertRecipient.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AlertRecipient.


        :param updated_at: The updated_at of this AlertRecipient.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, AlertRecipient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
