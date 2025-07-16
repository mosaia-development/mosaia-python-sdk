from typing import Optional
import re

def validate_identifier_name(value: Optional[str]) -> Optional[str]:
    if value is None:
        return value
    if not re.match(r'^[a-zA-Z0-9_-]+$', value):
        raise ValueError('Invalid name. Name can only contain letters, numbers, underscores, and hyphens')
    return value

def validate_email(value: Optional[str], field: str) -> Optional[str]:
    if value is None:
        return value
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
        raise ValueError(f'Invalid email address format. {field} must be a valid email address')
    return value

def validate_url(value: Optional[str], field: str) -> Optional[str]:
    if value is None:
        return value
    if not re.match(r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$', value):
        raise ValueError(f'Invalid URL format. {field} must be a valid HTTP(S) URL')
    return value