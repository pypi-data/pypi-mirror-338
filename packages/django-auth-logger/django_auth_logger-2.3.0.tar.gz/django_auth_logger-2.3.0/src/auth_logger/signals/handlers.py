from typing import Any
import logging

from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.core.handlers.wsgi import WSGIRequest
from django.utils import timezone
from ipware import get_client_ip

logger = logging.getLogger(__name__)


def build_auth_log_string(
    message: str,
    username: str | None,
    email: str | None,
    request: WSGIRequest | None,
) -> str:
    """
    Build a string with user and auth info for logging
    """
    client_ip, is_routable = "", False
    if request:
        client_ip, is_routable = get_client_ip(request)
    msg = "{message} username:[{username}] email:[{email}] ip:[{ipaddr}] datetime:[{now}]".format(
        message=message,
        username=username or "",
        email=email or "",
        ipaddr=client_ip,
        now=timezone.now(),
    )
    return msg


def handle_user_logged_in(
    sender: type[User],
    user: User | None = None,
    request: WSGIRequest | None = None,
    **kwargs: Any,
) -> None:
    username, email = (None, None) if user is None else (user.username, user.email)
    log_string = build_auth_log_string(
        "User Login Successful", username, email, request
    )
    logger.info(log_string)


def handle_user_login_failed(
    sender: str,
    credentials: dict[str, str],
    request: WSGIRequest | None = None,
    **kwargs: Any,
) -> None:
    username = credentials.get("username", None)
    email = credentials.get("email", None)
    log_string = build_auth_log_string("User Login Failed", username, email, request)
    logger.info(log_string)


user_logged_in.connect(handle_user_logged_in)
user_login_failed.connect(handle_user_login_failed)
