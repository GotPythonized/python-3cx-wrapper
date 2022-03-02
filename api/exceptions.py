from requests import Response
import logging

logger = logging.getLogger()

class threeCXException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        logger.error(message)

class NoFQDNProvided(threeCXException):
    message = "No FQDN provided"

class RequestException(threeCXException):
    pass

class DNNumberCannotBeUsed(threeCXException):
    message = "WARNINGS.DN_NUMBER_CANNOT_BE_USED"

def request_error_msg(response: Response, payload):
    message = f"{response.request.method} {response.request.url} {response.status_code}"
    if response.reason:
        message.__add__(f'reason: {response.reason}')
    if response.text:
      message.__add__(f'reason: {response.text}')
    if payload:
        message.__add__(f'payload: {payload}')
    
    if "WARNINGS.DN_NUMBER_CANNOT_BE_USED" in response.text:
        message = "Extension DN number cannot be used, probably because it is already in use"
        return DNNumberCannotBeUsed(message)
    return RequestException(message)    