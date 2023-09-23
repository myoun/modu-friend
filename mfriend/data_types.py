import uuid
from sqlalchemy.dialects.mysql import BINARY
from sqlalchemy.types import TypeDecorator
from typing import Any

class BinaryUUID(TypeDecorator[uuid.UUID]):
    
    impl = BINARY(16)
    cache_ok = True
    
    def process_bind_param(self, value: Any, dialect):
        try:
            return value.bytes
        except AttributeError:
            try:
                return uuid.UUID(value).bytes
            except TypeError:
                # for some reason we ended up with the bytestring
                # ¯\_(ツ)_/¯
                # I'm not sure why you would do that,
                # but here you go anyway.
                return value
                
    def process_result_value(self, value, dialect):
        return uuid.UUID(bytes=value)