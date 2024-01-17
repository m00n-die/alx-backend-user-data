#!/usr/bin/env python3
"""Authentication module
"""
import re
from typing import List, TypeVar
from flask import request


class Auth:
    """Authentication class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a path requires authentication.
        """
        if path is not None and excluded_paths is not None:
            for excluded in map(lambda x: x.strip(), excluded_paths):
                exp = ''
                if excluded[-1] == '*':
                    exp = '{}.*'.format(excluded[0:-1])
                elif excluded[-1] == '/':
                    exp = '{}/*'.format(excluded[0:-1])
                else:
                    exp = '{}/*'.format(excluded)
                if re.match(exp, path):
                    return False
            return True

    def authorization_header(self, request=None) -> str:
        """Gets the authorization header field from the request.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user from the request.
        """
        return None
