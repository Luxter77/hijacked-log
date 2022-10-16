from tqdm.auto import tqdm
from enum import Enum
import datetime as dt
import pprint
import sys
import os

from .logtypes import LogTypes, RESET_COLORS

class ProgrammingError(Exception):
    "Sos tonto, amigo"
    def __init__(self):
        super().__init__(self, 'You forgot to pass the exception to the exception handler you dummy')

class Logger:
    def __init__(self, log_dir: os.PathLike = '.', run_time: dt.datetime = dt.datetime.now(), log_level: LogTypes = LogTypes.INFO) -> None:
        self.params = {
            'run_time': run_time,
            'log_dir': log_dir,
        }

        self.log_level: LogTypes = log_level
        self.log_file = None

    def pprint(self, obj: object) -> str:
        if isinstance(obj, dict):
            obj = self._format_dict(obj)
        elif isinstance(obj, list):
            obj = self._format_list(obj)
        else:
            obj = self._format_default(obj)
        return obj

    def _format_dict(self, obj: object) -> str:
        out = '{\n'
        for key, value in obj.items():
            out += '\t[ ' + pprint.pformat(key, width=sys.maxsize) + ' ]:\t' + pprint.pformat(value, width=sys.maxsize) + '\n'
        out += '}'
        return out

    def _format_list(self, obj: object) -> str:
        out = '['
        for index, value in enumerate(obj):
            out += f'\t[ {index} ]:\t' + pprint.pformat(value, width=sys.maxsize) + '\n'
        out += ']'
        return out

    def _format_default(self, obj: object) -> str:
        return '\n'.join(pprint.pformat(obj).splitlines())

    def log(self, obj: object, do_print=True, do_pprint=True, logtype: LogTypes = None):
        "Writes OBJ data into log"

        if logtype is None:
            logtype = self.log_level

        n_lines = 0

        if logtype.value.level >= self.log_level.value.level:

            logtime = dt.datetime.now().isoformat()

            if self.log_file is None:
                self.log_file = open(os.path.join(self.params['log_dir'], self.params['run_time'].strftime("%Y%m%d-%H%M%S")+'.LOG'), 'w', encoding='utf-8')

            if do_pprint:
                obj = self.pprint(obj)

            obj = str(obj)

            lines = obj.splitlines()

            for line in lines:
                self.log_file.write(f"[{ logtime }][{ logtype.value.name }]: "   + line + "\n")
                if do_print: tqdm.write(logtype.value.color + logtype.value.name + ': ' + line + RESET_COLORS)

            n_lines = len(obj.splitlines())

            self.log_file.flush()
            os.fsync(self.log_file)

        return n_lines

    def display_exception(self, _ = None, ex: BaseException = ProgrammingError(), tb=None, fatal: bool = False):
        self.log(''.join(tb.format_exception(ex)), do_pprint=False, logtype=(LogTypes.FATAL if fatal else LogTypes.ERR_))

    def __bool__(self) -> bool:
        return True
