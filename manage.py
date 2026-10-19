#!/usr/bin/env python3
"""
Django command-line utility for administrative tasks.
"""

import os
import sys


DEFAULT_SETTINGS_MODULE = "urlshortner.settings"


def main() -> None:
    """Run Django administrative commands."""

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        DEFAULT_SETTINGS_MODULE,
    )

    try:
        from django.core.management import execute_from_command_line

    except ImportError as exc:
        raise ImportError(
            "Django could not be imported.\n"
            "Make sure your virtual environment is activated "
            "and the project dependencies are installed.\n\n"
            "Install dependencies using:\n"
            "python -m pip install -r requirements.txt"
        ) from exc

    try:
        execute_from_command_line(sys.argv)

    except ModuleNotFoundError as exc:
        if exc.name == "urlshortner" or (
            exc.name and exc.name.startswith("urlshortner.")
        ):
            raise ModuleNotFoundError(
                "The Django project package 'urlshortner' "
                "could not be found.\n\n"
                "Verify that your project contains:\n"
                "  urlshortner/__init__.py\n"
                "  urlshortner/settings.py\n"
                "  urlshortner/urls.py\n"
                "  urlshortner/wsgi.py\n\n"
                "Make sure you are running this command "
                "from the project root directory."
            ) from exc

        raise


if __name__ == "__main__":
    main()
