"""
Module for dictionary mapping of standard success responses.

Based on Mozilla Developer Network (MDN) HTTP response status codes documentation:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status#successful_responses
"""

from typing import Dict


OK: dict[str, str] = {
    "message": "The request succeeded. For GET: resource fetched, POST/PUT: action result transmitted, HEAD: headers only, TRACE: request echo."
}

CREATED: dict[str, str] = {
    "message": "The request succeeded and a new resource was created. Typically sent after POST requests or some PUT requests."
}

ACCEPTED: dict[str, str] = {
    "message": "The request has been received but not yet acted upon. Another process or server will handle the request asynchronously."
}

NON_AUTHORITATIVE_INFORMATION: dict[str, str] = {
    "message": "The returned metadata is from a cached copy rather than the origin server. Prefer 200 OK unless specifically dealing with cached resources."
}

NO_CONTENT: dict[str, str] = {
    "message": "The request was successful, but there is no content to send. The client may update its cached headers for this resource."
}

RESET_CONTENT: dict[str, str] = {
    "message": "The request was successful. The client should reset the document that sent this request."
}

PARTIAL_CONTENT: dict[str, str] = {
    "message": "The server is sending a partial response to a valid range request. The response includes the requested parts of the resource."
}

MULTI_STATUS: dict[str, str] = {
    "message": "The response conveys information about multiple resources where multiple status codes may be appropriate (WebDAV)."
}

ALREADY_REPORTED: dict[str, str] = {
    "message": "The members of a WebDAV binding have already been enumerated in a preceding part of the response (WebDAV)."
}

IM_USED: dict[str, str] = {
    "message": "The server has fulfilled a GET request and the response represents the result of instance-manipulations applied to the current instance (HTTP Delta encoding)."
}


http_success_mapping: Dict[int, dict] = {
    200: OK,
    201: CREATED,
    202: ACCEPTED,
    203: NON_AUTHORITATIVE_INFORMATION,
    204: NO_CONTENT,
    205: RESET_CONTENT,
    206: PARTIAL_CONTENT,
    207: MULTI_STATUS,
    208: ALREADY_REPORTED,
    226: IM_USED,
}
"""
Mapping of all default HTTP success responses with their corresponding messages.
""" 