# SPDX-License-Identifier: AGPL-3.0-or-later
"""App configuration for the authentication module."""

from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    Configuration class for the authentication app.

    Sets the default auto field and app name for Django.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "authentication"
