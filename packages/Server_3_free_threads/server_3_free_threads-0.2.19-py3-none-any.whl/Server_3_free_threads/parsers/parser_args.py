import sys
import logging
import re
from Server_3_free_threads.parsers.base import BaseMixin
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(filename)s:%(funcName)s] %(message)s')
log = logging.getLogger(__name__)


class ParserCommandLineArgs(BaseMixin):

    """
    Класс реализующий парсинг параметров командной строки
    """

    def __init__(self):
        self._port = None
        self._app = None
        self._config_file = None
        # self.port_re = re.compile(r'port=(?P<port>\d{0,4})')
        # self.app_re = re.compile(r'app=(?P<app>.+)')
        self.config_re = re.compile(r'configfile=(?P<configfile>.+)')
        self.all_param = sys.argv[1:]

    # @property
    # def port(self):
    #     return self._port
    #
    # @property
    # def app(self):
    #     return self._app

    @property
    def configfile(self) -> bool:
        return self._config_file

    def check_args(self):

        """
        Проверяется существования параметров
        """

        if not self.all_param and self.find_args() == False:
            return False
        else:
            return True


    def find_args(self):
        for param in self.all_param:
            # result_port = self.pars_func(param=param, group='port', re_pattern=self.port_re)
            # result_app = self.pars_func(param=param, group='app', re_pattern=self.app_re)
            result_configfile = self.pars_func(param=param, group='configfile', re_pattern=self.config_re)

            # if result_port:
            #     self._port = result_port
            #
            # if result_app:
            #     self._app = result_app

            if result_configfile:
                self._config_file = result_configfile
        else:
            return False
