from enum import Enum


class RuntimeType(Enum):
    DEV = 0,
    CLIENT = 1,
    TRUFFLE = 2

def determine_runtime() -> RuntimeType:
    try:
        from truffle.runtime.proprietary import TruffleRuntime
        return RuntimeType.TRUFFLE
    except ImportError:
        from truffle.runtime.public import TruffleClientRuntime
        return RuntimeType.CLIENT

