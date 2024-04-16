#!/usr/bin/env python3
"""Auth class to manage authentication"""
from typing import List, TypeVar
from flask import request


class Auth():
    """The authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth function"""
        path = str(path)
        path = path.rstrip("/")
        excluded_paths = [ep.rstrip("/") for ep in excluded_paths] \
            if excluded_paths else []

        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for ex_path in excluded_paths:
            if path == ex_path:
                return False

    def authorization_header(self, request=None) -> str:
        """function that adds authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """gets current user"""
        return None
