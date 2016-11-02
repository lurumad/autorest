# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class PolymorphicrecursiveOperations(object):
    """PolymorphicrecursiveOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get_valid(
            self, custom_headers=None, raw=False, **operation_config):
        """Get complex types that are polymorphic and have recursive references.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`Fish
         <Fixtures.AcceptanceTestsBodyComplex.models.Fish>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<Fixtures.AcceptanceTestsBodyComplex.models.ErrorException>`
        """
        # Construct URL
        url = '/complex/polymorphicrecursive/valid'

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Fish', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def put_valid(
            self, complex_body, custom_headers=None, raw=False, **operation_config):
        """Put complex types that are polymorphic and have recursive references.

        :param complex_body: Please put a salmon that looks like this:
         {
         "fishtype": "salmon",
         "species": "king",
         "length": 1,
         "age": 1,
         "location": "alaska",
         "iswild": true,
         "siblings": [
         {
         "fishtype": "shark",
         "species": "predator",
         "length": 20,
         "age": 6,
         "siblings": [
         {
         "fishtype": "salmon",
         "species": "coho",
         "length": 2,
         "age": 2,
         "location": "atlantic",
         "iswild": true,
         "siblings": [
         {
         "fishtype": "shark",
         "species": "predator",
         "length": 20,
         "age": 6
         },
         {
         "fishtype": "sawshark",
         "species": "dangerous",
         "length": 10,
         "age": 105
         }
         ]
         },
         {
         "fishtype": "sawshark",
         "species": "dangerous",
         "length": 10,
         "age": 105
         }
         ]
         },
         {
         "fishtype": "sawshark",
         "species": "dangerous",
         "length": 10,
         "age": 105
         }
         ]
         }
        :type complex_body: :class:`Fish
         <Fixtures.AcceptanceTestsBodyComplex.models.Fish>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<Fixtures.AcceptanceTestsBodyComplex.models.ErrorException>`
        """
        # Construct URL
        url = '/complex/polymorphicrecursive/valid'

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'Fish')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
