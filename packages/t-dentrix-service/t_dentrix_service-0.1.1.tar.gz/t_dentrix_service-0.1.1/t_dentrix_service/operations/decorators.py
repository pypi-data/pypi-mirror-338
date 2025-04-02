"""Module that contains a variety of decorators to be used in the main process."""

import time
from typing import Callable
from requests.exceptions import HTTPError

from SeleniumLibrary.errors import ElementNotFound
from selenium.common import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)

from t_dentrix_service.exceptions import (
    NotLoggedInError,
    InvalidRequestException,
    ConnectionRefusedException,
    NotFoundException,
    ConnectionTimeoutException,
    RateLimitExceededException,
    UnexpectedServerError,
)

SELENIUM_RETRY_EXCEPTIONS = (
    StaleElementReferenceException,
    ElementClickInterceptedException,
    NoSuchElementException,
    ElementNotInteractableException,
    ElementNotFound,
    AssertionError,
    TimeoutException,
)


def custom_selenium_retry(
    exceptions: tuple = (), tries: int = 3, delay: int = 5, ignore_exception: tuple = None
) -> Callable:
    """Base decorator to retry if specified exceptions occur."""
    ignore_exception = () if ignore_exception is None else ignore_exception
    exceptions += SELENIUM_RETRY_EXCEPTIONS

    def decorator(func: Callable) -> Callable:
        def wrapper(self: Callable, *args, **kwargs) -> Callable:
            exception = None
            result = None
            for _ in range(tries):
                try:
                    result = func(self, *args, **kwargs)
                    break
                except ignore_exception:
                    pass
                except exceptions as e:
                    exception = e
                    if isinstance(e, TimeoutException):
                        time.sleep(60)
                    else:
                        time.sleep(delay)
            else:
                if exception:
                    raise exception
            return result

        return wrapper

    return decorator


def dentrix_request_handling(func: Callable):
    """A decorator for handling general HTTP exceptions from Dentrix."""

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except HTTPError as e:
            match e.response.status_code:
                case 401:
                    raise NotLoggedInError("Please log into Dentrix before attempting any operation.")
                case _:
                    raise e

    return wrapper


def ascend_request_handling(func: Callable):
    """A de corator for handling general HTTP exceptions from Ascend API."""

    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except HTTPError as e:
            match e.response.status_code:
                case 400:
                    raise InvalidRequestException("The request was invalid or cannot be processed")
                case 401:
                    raise NotLoggedInError("Authentication is required and has failed or has not been provided")
                case 403:
                    raise ConnectionRefusedException(
                        "The request is understood, but it has been refused or access is not allowed"
                    )
                case 404:
                    raise NotFoundException("The requested resource is either missing or does not exist")
                case 408:
                    raise ConnectionTimeoutException("The server timed out while processing the request")
                case 429:
                    raise RateLimitExceededException("Rate limit exceeded")
                case 500:
                    raise UnexpectedServerError("An unexpected error occurred")
                case _:
                    raise e

    return wrapper
