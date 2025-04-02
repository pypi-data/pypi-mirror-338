from .basesdk import BaseSDK
from atoma_sdk import crypto_utils, models, utils
from atoma_sdk._hooks import HookContext
from atoma_sdk.types import OptionalNullable, UNSET
from atoma_sdk.utils import get_security_from_env
from typing import Any, Dict, List, Mapping, Optional, Union
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
import json

class ConfidentialChat(BaseSDK):
    r"""Atoma's API confidential chat completions v1 endpoint"""

    def create(
        self,
        *,
        messages: Union[
            List[models.ChatCompletionMessage],
            List[models.ChatCompletionMessageTypedDict],
        ],
        model: str,
        frequency_penalty: OptionalNullable[float] = UNSET,
        function_call: Optional[Any] = None,
        functions: OptionalNullable[List[Any]] = UNSET,
        logit_bias: OptionalNullable[Dict[str, float]] = UNSET,
        max_tokens: OptionalNullable[int] = UNSET,
        n: OptionalNullable[int] = UNSET,
        presence_penalty: OptionalNullable[float] = UNSET,
        response_format: Optional[Any] = None,
        seed: OptionalNullable[int] = UNSET,
        stop: OptionalNullable[List[str]] = UNSET,
        stream: OptionalNullable[bool] = False,
        temperature: OptionalNullable[float] = UNSET,
        tool_choice: Optional[Any] = None,
        tools: OptionalNullable[List[Any]] = UNSET,
        top_p: OptionalNullable[float] = UNSET,
        user: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ChatCompletionResponse:
        r"""Create confidential chat completion

        This handler processes chat completion requests in a confidential manner, providing additional
        encryption and security measures for sensitive data processing. It supports both streaming and
        non-streaming responses while maintaining data confidentiality through AEAD encryption and TEE hardware,
        for full private AI compute.

        :param messages: A list of messages comprising the conversation so far
        :param model: ID of the model to use
        :param frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far
        :param function_call: Controls how the model responds to function calls
        :param functions: A list of functions the model may generate JSON inputs for
        :param logit_bias: Modify the likelihood of specified tokens appearing in the completion
        :param max_tokens: The maximum number of tokens to generate in the chat completion
        :param n: How many chat completion choices to generate for each input message
        :param presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far
        :param response_format: The format to return the response in
        :param seed: If specified, our system will make a best effort to sample deterministically
        :param stop: Up to 4 sequences where the API will stop generating further tokens
        :param stream: Whether to stream back partial progress. Must be false for this request type.
        :param temperature: What sampling temperature to use, between 0 and 2
        :param tool_choice: Controls which (if any) tool the model should use
        :param tools: A list of tools the model may call
        :param top_p: An alternative to sampling with temperature
        :param user: A unique identifier representing your end-user
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        ################## Our code starts here #########################################################
        # Add encryption
        try:
            chat_completions_request_body = models.CreateChatCompletionRequest(
                frequency_penalty=frequency_penalty,
                function_call=function_call,
                functions=functions,
                logit_bias=logit_bias,
                max_tokens=max_tokens,
                messages=utils.get_pydantic_model(
                    messages, List[models.ChatCompletionMessage]
                ),
                model=model,
                n=n,
                presence_penalty=presence_penalty,
                response_format=response_format,
                seed=seed,
                stop=stop,
                stream=stream,
                temperature=temperature,
                tool_choice=tool_choice,
                tools=tools,
                top_p=top_p,
                user=user,
            )

            client_dh_private_key = X25519PrivateKey.generate()

            # Encrypt the message
            node_dh_public_key, salt, encrypted_message = crypto_utils.encrypt_message(sdk=self, client_dh_private_key=client_dh_private_key, request_body=chat_completions_request_body, model=model)

        except Exception as e:
            raise models.APIError(
                f"Failed to prepare confidential chat request: {str(e)}",
                500,
                str(e),
                None
            )
        ##################################################################################################

        request = encrypted_message

        req = self._build_request(
            method="POST",
            path="/v1/confidential/chat/completions",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.ConfidentialComputeRequest
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="confidential_chat_completions_create",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            ##################################################################################################
            encrypted_response = utils.unmarshal_json(
                http_res.text, models.ConfidentialComputeResponse
            )
            # Decrypt the response
            try:
                decrypted_response = crypto_utils.decrypt_message(
                    client_dh_private_key=client_dh_private_key,
                    node_dh_public_key=node_dh_public_key,
                    salt=salt,
                    encrypted_message=encrypted_response
                )
                return utils.unmarshal_json(
                    decrypted_response.decode('utf-8'),
                    models.ChatCompletionResponse
                )
            except Exception as e:
                raise models.APIError(
                    f"Failed to decrypt response: {str(e)}",
                    500,
                    str(e),
                    http_res
                )
            ##################################################################################################
        if utils.match_response(http_res, ["400", "401", "4XX", "500", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def create_async(
        self,
        *,
        messages: Union[
            List[models.ChatCompletionMessage],
            List[models.ChatCompletionMessageTypedDict],
        ],
        model: str,
        frequency_penalty: OptionalNullable[float] = UNSET,
        function_call: Optional[Any] = None,
        functions: OptionalNullable[List[Any]] = UNSET,
        logit_bias: OptionalNullable[Dict[str, float]] = UNSET,
        max_tokens: OptionalNullable[int] = UNSET,
        n: OptionalNullable[int] = UNSET,
        presence_penalty: OptionalNullable[float] = UNSET,
        response_format: Optional[Any] = None,
        seed: OptionalNullable[int] = UNSET,
        stop: OptionalNullable[List[str]] = UNSET,
        stream: OptionalNullable[bool] = False,
        temperature: OptionalNullable[float] = UNSET,
        tool_choice: Optional[Any] = None,
        tools: OptionalNullable[List[Any]] = UNSET,
        top_p: OptionalNullable[float] = UNSET,
        user: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ChatCompletionResponse:
        r"""Create confidential chat completion

        This handler processes chat completion requests in a confidential manner, providing additional
        encryption and security measures for sensitive data processing. It supports both streaming and
        non-streaming responses while maintaining data confidentiality through AEAD encryption and TEE hardware,
        for full private AI compute.

        :param messages: A list of messages comprising the conversation so far
        :param model: ID of the model to use
        :param frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far
        :param function_call: Controls how the model responds to function calls
        :param functions: A list of functions the model may generate JSON inputs for
        :param logit_bias: Modify the likelihood of specified tokens appearing in the completion
        :param max_tokens: The maximum number of tokens to generate in the chat completion
        :param n: How many chat completion choices to generate for each input message
        :param presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far
        :param response_format: The format to return the response in
        :param seed: If specified, our system will make a best effort to sample deterministically
        :param stop: Up to 4 sequences where the API will stop generating further tokens
        :param stream: Whether to stream back partial progress. Must be false for this request type.
        :param temperature: What sampling temperature to use, between 0 and 2
        :param tool_choice: Controls which (if any) tool the model should use
        :param tools: A list of tools the model may call
        :param top_p: An alternative to sampling with temperature
        :param user: A unique identifier representing your end-user
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        ################## Our code starts here #########################################################
        # Add encryption
        try:
            chat_completions_request_body = models.CreateChatCompletionRequest(
                frequency_penalty=frequency_penalty,
                function_call=function_call,
                functions=functions,
                logit_bias=logit_bias,
                max_tokens=max_tokens,
                messages=utils.get_pydantic_model(
                    messages, List[models.ChatCompletionMessage]
                ),
                model=model,
                n=n,
                presence_penalty=presence_penalty,
                response_format=response_format,
                seed=seed,
                stop=stop,
                stream=stream,
                temperature=temperature,
                tool_choice=tool_choice,
                tools=tools,
                top_p=top_p,
                user=user,
            )

            client_dh_private_key = X25519PrivateKey.generate()

            # Encrypt the message
            node_dh_public_key, salt, encrypted_message = crypto_utils.encrypt_message(sdk=self, client_dh_private_key=client_dh_private_key, request_body=chat_completions_request_body, model=model)

        except Exception as e:
            raise models.APIError(
                f"Failed to prepare confidential chat request: {str(e)}",
                500,
                str(e),
                None
            )
        #########################################################################################################

        request = encrypted_message

        req = self._build_request_async(
            method="POST",
            path="/v1/confidential/chat/completions",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.ConfidentialComputeRequest
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="confidential_chat_completions_create",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            ##################################################################################################
            encrypted_response = utils.unmarshal_json(
                http_res.text, models.ConfidentialComputeResponse
            )
            # Decrypt the response
            try:
                decrypted_response = crypto_utils.decrypt_message(
                    client_dh_private_key=client_dh_private_key,
                    node_dh_public_key=node_dh_public_key,
                    salt=salt,
                    encrypted_message=encrypted_response
                )
                return utils.unmarshal_json(
                    decrypted_response.decode('utf-8'),
                    models.ChatCompletionResponse
                )
            except Exception as e:
                raise models.APIError(
                    f"Failed to decrypt response: {str(e)}",
                    500,
                    str(e),
                    http_res
                )
            ##################################################################################################
        if utils.match_response(http_res, ["400", "401", "4XX", "500", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def create_stream(
        self,
        *,
        messages: Union[
            List[models.ChatCompletionMessage],
            List[models.ChatCompletionMessageTypedDict],
        ],
        model: str,
        frequency_penalty: OptionalNullable[float] = UNSET,
        function_call: Optional[Any] = None,
        functions: OptionalNullable[List[Any]] = UNSET,
        logit_bias: OptionalNullable[Dict[str, float]] = UNSET,
        max_tokens: OptionalNullable[int] = UNSET,
        n: OptionalNullable[int] = UNSET,
        presence_penalty: OptionalNullable[float] = UNSET,
        response_format: Optional[Any] = None,
        seed: OptionalNullable[int] = UNSET,
        stop: OptionalNullable[List[str]] = UNSET,
        stream: Optional[bool] = True,
        temperature: OptionalNullable[float] = UNSET,
        tool_choice: Optional[Any] = None,
        tools: OptionalNullable[List[Any]] = UNSET,
        top_p: OptionalNullable[float] = UNSET,
        user: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> utils.eventstreaming.EventStream[models.ChatCompletionStreamResponse]:
        r"""Create confidential chat completion with streaming

        This handler processes streaming chat completion requests in a confidential manner, providing additional
        encryption and security measures for sensitive data processing. Each streamed chunk is individually
        encrypted and decrypted while maintaining data confidentiality through AEAD encryption and TEE hardware.

        :param messages: A list of messages comprising the conversation so far
        :param model: ID of the model to use
        :param frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far
        :param function_call: Controls how the model responds to function calls
        :param functions: A list of functions the model may generate JSON inputs for
        :param logit_bias: Modify the likelihood of specified tokens appearing in the completion
        :param max_tokens: The maximum number of tokens to generate in the chat completion
        :param n: How many chat completion choices to generate for each input message
        :param presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far
        :param response_format: The format to return the response in
        :param seed: If specified, our system will make a best effort to sample deterministically
        :param stop: Up to 4 sequences where the API will stop generating further tokens
        :param stream: Whether to stream back partial progress. Must be true for this request type.
        :param temperature: What sampling temperature to use, between 0 and 2
        :param tool_choice: Controls which (if any) tool the model should use
        :param tools: A list of tools the model may call
        :param top_p: An alternative to sampling with temperature
        :param user: A unique identifier representing your end-user
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        ################## Our code starts here #########################################################
        # Add encryption
        try:
            chat_completions_request_body = models.CreateChatCompletionStreamRequest(
                frequency_penalty=frequency_penalty,
                function_call=function_call,
                functions=functions,
                logit_bias=logit_bias,
                max_tokens=max_tokens,
                messages=utils.get_pydantic_model(
                    messages, List[models.ChatCompletionMessage]
                ),
                model=model,
                n=n,
                presence_penalty=presence_penalty,
                response_format=response_format,
                seed=seed,
                stop=stop,
                stream=stream,
                temperature=temperature,
                tool_choice=tool_choice,
                tools=tools,
                top_p=top_p,
                user=user,
            )

            client_dh_private_key = X25519PrivateKey.generate()

            # Encrypt the message
            node_dh_public_key, salt, encrypted_message = crypto_utils.encrypt_message(sdk=self, client_dh_private_key=client_dh_private_key, request_body=chat_completions_request_body, model=model)

        except Exception as e:
            raise models.APIError(
                f"Failed to prepare confidential chat stream request: {str(e)}",
                500,
                str(e),
                None
            )
        ##################################################################################################

        request = encrypted_message

        req = self._build_request(
            method="POST",
            path="/v1/confidential/chat/completions#stream",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="text/event-stream",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.ConfidentialComputeRequest
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="confidential_chat_completions_create_stream",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "500", "5XX"],
            stream=True,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "text/event-stream"):
            ##################################################################################################
            # Create a decryption wrapper function for each chunk
            def decrypt_chunk(raw_chunk):
                try:
                    encrypted_chunk = utils.unmarshal_json(raw_chunk, models.ConfidentialComputeStreamResponse)
                    decrypted_chunk = crypto_utils.decrypt_message(
                        client_dh_private_key=client_dh_private_key,
                        node_dh_public_key=node_dh_public_key,
                        salt=salt,
                        encrypted_message=encrypted_chunk.data
                    )
                    # The decrypted JSON is a ChatCompletionChunk
                    decrypted_json = json.loads(decrypted_chunk.decode('utf-8'))
                    # Skip chunks with empty choices
                    if not decrypted_json.get('choices'):
                        return None
                    # Wrap the chunk in a StreamResponse to maintain consistent API
                    return models.ChatCompletionStreamResponse(data=models.ChatCompletionChunk.model_validate(decrypted_json))
                except Exception as e:
                    raise models.APIError(f"Failed to decrypt stream chunk: {str(e)}", 500, str(e), None)

            return utils.eventstreaming.EventStream(
                http_res,
                decrypt_chunk,
                sentinel="[DONE]"
            )
            ##################################################################################################
        if utils.match_response(http_res, ["400", "401", "4XX", "500", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def create_stream_async(
        self,
        *,
        messages: Union[
            List[models.ChatCompletionMessage],
            List[models.ChatCompletionMessageTypedDict],
        ],
        model: str,
        frequency_penalty: OptionalNullable[float] = UNSET,
        function_call: Optional[Any] = None,
        functions: OptionalNullable[List[Any]] = UNSET,
        logit_bias: OptionalNullable[Dict[str, float]] = UNSET,
        max_tokens: OptionalNullable[int] = UNSET,
        n: OptionalNullable[int] = UNSET,
        presence_penalty: OptionalNullable[float] = UNSET,
        response_format: Optional[Any] = None,
        seed: OptionalNullable[int] = UNSET,
        stop: OptionalNullable[List[str]] = UNSET,
        stream: Optional[bool] = True,
        temperature: OptionalNullable[float] = UNSET,
        tool_choice: Optional[Any] = None,
        tools: OptionalNullable[List[Any]] = UNSET,
        top_p: OptionalNullable[float] = UNSET,
        user: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> utils.eventstreaming.EventStreamAsync[models.ChatCompletionStreamResponse]:
        r"""Create confidential chat completion with streaming

        This handler processes streaming chat completion requests in a confidential manner, providing additional
        encryption and security measures for sensitive data processing. Each streamed chunk is individually
        encrypted and decrypted while maintaining data confidentiality through AEAD encryption and TEE hardware.

        :param messages: A list of messages comprising the conversation so far
        :param model: ID of the model to use
        :param frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far
        :param function_call: Controls how the model responds to function calls
        :param functions: A list of functions the model may generate JSON inputs for
        :param logit_bias: Modify the likelihood of specified tokens appearing in the completion
        :param max_tokens: The maximum number of tokens to generate in the chat completion
        :param n: How many chat completion choices to generate for each input message
        :param presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far
        :param response_format: The format to return the response in
        :param seed: If specified, our system will make a best effort to sample deterministically
        :param stop: Up to 4 sequences where the API will stop generating further tokens
        :param stream: Whether to stream back partial progress. Must be true for this request type.
        :param temperature: What sampling temperature to use, between 0 and 2
        :param tool_choice: Controls which (if any) tool the model should use
        :param tools: A list of tools the model may call
        :param top_p: An alternative to sampling with temperature
        :param user: A unique identifier representing your end-user
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        ################## Our code starts here #########################################################
        # Add encryption
        try:
            chat_completions_request_body = models.CreateChatCompletionStreamRequest(
                frequency_penalty=frequency_penalty,
                function_call=function_call,
                functions=functions,
                logit_bias=logit_bias,
                max_tokens=max_tokens,
                messages=utils.get_pydantic_model(
                    messages, List[models.ChatCompletionMessage]
                ),
                model=model,
                n=n,
                presence_penalty=presence_penalty,
                response_format=response_format,
                seed=seed,
                stop=stop,
                stream=stream,
                temperature=temperature,
                tool_choice=tool_choice,
                tools=tools,
                top_p=top_p,
                user=user,
            )

            client_dh_private_key = X25519PrivateKey.generate()

            # Encrypt the message
            node_dh_public_key, salt, encrypted_message = crypto_utils.encrypt_message(sdk=self, client_dh_private_key=client_dh_private_key, request_body=chat_completions_request_body, model=model)

        except Exception as e:
            raise models.APIError(
                f"Failed to prepare confidential chat stream request: {str(e)}",
                500,
                str(e),
                None
            )
        ##################################################################################################

        request = encrypted_message

        req = self._build_request_async(
            method="POST",
            path="/v1/confidential/chat/completions#stream",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="text/event-stream",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.ConfidentialComputeRequest
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="confidential_chat_completions_create_stream",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "4XX", "500", "5XX"],
            stream=True,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "text/event-stream"):
            ##################################################################################################
            # Fix: Create a synchronous wrapper for the async decrypt_chunk function
            # This is needed because EventStreamAsync expects a sync function that returns the value directly
            def decrypt_chunk_wrapper(raw_chunk):
                try:
                    # Parse the raw JSON string directly
                    parsed_data = json.loads(raw_chunk)

                    # Create a simple class to hold the encrypted data with attributes
                    class EncryptedData:
                        def __init__(self, ciphertext, nonce, signature, response_hash):
                            self.ciphertext = ciphertext
                            self.nonce = nonce
                            self.signature = signature
                            self.response_hash = response_hash

                    # Instantiate this class with the data from the JSON
                    encrypted_data = EncryptedData(
                        ciphertext=parsed_data["data"]["ciphertext"],
                        nonce=parsed_data["data"]["nonce"],
                        signature=parsed_data["data"]["signature"],
                        response_hash=parsed_data["data"]["response_hash"]
                    )

                    # Now pass this properly structured object to decrypt_message
                    decrypted_chunk = crypto_utils.decrypt_message(
                        client_dh_private_key=client_dh_private_key,
                        node_dh_public_key=node_dh_public_key,
                        salt=salt,
                        encrypted_message=encrypted_data
                    )

                    decrypted_json = json.loads(decrypted_chunk.decode('utf-8'))

                    # Skip chunks with empty choices
                    if not decrypted_json.get('choices'):
                        return None

                    # Wrap the chunk in a StreamResponse
                    return models.ChatCompletionStreamResponse(data=models.ChatCompletionChunk.model_validate(decrypted_json))
                except Exception as e:
                    raise models.APIError(f"Failed to decrypt stream chunk: {str(e)}", 500, str(e), None)

            return utils.eventstreaming.EventStreamAsync(
                http_res,
                decrypt_chunk_wrapper,
                sentinel="[DONE]"
            )
            ##################################################################################################
        if utils.match_response(http_res, ["400", "401", "4XX", "500", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
