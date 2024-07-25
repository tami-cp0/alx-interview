#!/usr/bin/python3
"""
Module
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Determines if the given data set represents a valid UTF-8 encoding.
    Returns:
        True if data is a valid UTF-8 encoding, else return False
    """
    if any(data) > 255:
        return False