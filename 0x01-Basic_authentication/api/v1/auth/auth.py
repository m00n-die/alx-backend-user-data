#!/usr/bin/env python3
"""Auth class to manage authentication"""
from typing import List, TypeVar
from flask import request


class Auth():
    """The authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth function"""
        return False
    
    def authorization_header(self, request=None) -> str:
        """function that adds authorization header"""
        return None
    
    def current_user(self, request=None) -> TypeVar('User'): # type: ignore
        """gets current user"""
        return None
