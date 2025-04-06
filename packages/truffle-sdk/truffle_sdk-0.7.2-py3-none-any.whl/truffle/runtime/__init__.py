import typing
from truffle.common import get_logger
from .decs import tool_decorator, args_decorator, group_decorator


from .determine_runtime import determine_runtime, RuntimeType

HOST = determine_runtime()


logger = get_logger()

try:
    from .proprietary import TruffleRuntime
    logger.debug("Using proprietary runtime")
except ImportError:
    logger.debug("Using public runtime")
    from .public import TruffleClientRuntime as TruffleRuntime


def Runtime():
    return TruffleRuntime

def group(name: str, leader: bool = False):
    return group_decorator(name, leader)

def tool(description: str = None, icon: str = None, predicate: typing.Callable = None):
    return tool_decorator(description, icon, predicate)

def args(**kwargs):
    return args_decorator(**kwargs)
    
