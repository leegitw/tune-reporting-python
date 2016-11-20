#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)
#  @namespace tune_reporting


from bs4 import BeautifulSoup

from .constants import (
    __USER_AGENT__
)

import sys

def base_class_name(obj):
    return obj.__class__.__name__


def full_class_name(obj):
    try:
        return obj.__module__ + "." + obj.__class__.__name__
    except Exception as ex:
        return obj.__class__.__name__


def convert_size(
    size,
    precision=2
):
    """Convert Size
    Args:
        size:
        precision:
    Returns:
    """
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
    suffixIndex = 0

    while size > 1024 and suffixIndex < 4:
        suffixIndex += 1  # increment the index of the suffix
        size = size / 1024.0  # apply the division

    suffix = suffixes[suffixIndex]
    if suffix == 'B':
        precision = 0

    return "%.*f %s" % (precision, size, suffix)

def requests_response_text_html(
    response
):
    """Get HTML Text only
    Args:
        response:
    Returns:
    """
    assert response

    response_content_html_lines = None
    response_content_type = response.headers.get('Content-Type', None)

    if response_content_type.startswith('text/html'):
        try:
            response_content_html = response.text
            soup = BeautifulSoup(response_content_html, 'html.parser')
            for elem in soup.findAll(['script', 'style']):
                elem.extract()
            response_content_html_text = soup.get_text()
            response_content_html_lines = response_content_html_text.splitlines()
            response_content_html_lines = \
                [item.strip() for item in response_content_html_lines]
            response_content_html_lines = \
                [x for x in response_content_html_lines if x != '']
        except Exception as ex:
            raise ValueError(
                "Failed to parse text/html",
                errors=ex
            )
    else:
        raise ValueError(
            "Unexpected 'Content-Type': '{}'".format(
                response_content_type
            )
        )

    return response_content_html_lines