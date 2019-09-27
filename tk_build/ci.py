# -*- coding: utf-8 -*-
# Copyright (c) 2019 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import os


def is_in_ci_environment():
    """
    Returns ``True`` if in a CI environment, ``False`` otherwise.
    """
    return "CI" in os.environ


def get_ci_name():
    """
    """
    if is_travis():
        return "Travis"
    elif is_appveyor():
        return "AppVeyor"
    else:
        raise RuntimeError("This CI service is not supported!")


def is_travis():
    return "TRAVIS" in os.environ


def is_appveyor():
    return "APPVEYOR" in os.environ


def get_cloned_folder_root():
    """
    Returns the folder into which the tested repository has been cloned in.
    """
    if is_travis():
        return os.environ["TRAVIS_BUILD_DIR"]
    elif is_appveyor():
        return os.environ["APPVEYOR_BUILD_FOLDER"]
    else:
        raise RuntimeError("This CI service is not supported!")


def is_pull_request():
    return os.environ.get("TRAVIS_PULL_REQUEST", "false") != "false"


def get_pull_request_id():
    """
    Returns the current pull request id or None if this is not a pull
    request build.
    """
    return int(os.environ["TRAVIS_PULL_REQUEST"])


def get_pull_request_slug():
    return os.environ["TRAVIS_REPO_SLUG"]
