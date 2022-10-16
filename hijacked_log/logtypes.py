# COLORS!
import colorama as col

from enum import Enum
import dataclasses

col.deinit()                        # breaks some windows systems but fixes other windows systems
col.init(strip=False, convert=True) # see https://github.com/tartley/col/issues/217

RESET_COLORS = col.Back.RESET + col.Fore.RESET

@dataclasses.dataclass(frozen=True)
class LogType:
    color:  col.ansi.AnsiCodes
    name:   str
    level:  int

class LogTypes(Enum):
    DBG_:  LogType = LogType(color=col.Fore.LIGHTMAGENTA_EX,      name='_DEBUG_', level=0)
    INFO:  LogType = LogType(color=col.Fore.WHITE,                name='_INFO__', level=1)
    WARN:  LogType = LogType(color=col.Fore.YELLOW,               name='WARNING', level=2)
    ERR_:  LogType = LogType(color=col.Fore.RED,                  name='_ERROR_', level=3)
    FATAL: LogType = LogType(color=col.Back.RED + col.Fore.BLACK, name='_FATAL_', level=4)
