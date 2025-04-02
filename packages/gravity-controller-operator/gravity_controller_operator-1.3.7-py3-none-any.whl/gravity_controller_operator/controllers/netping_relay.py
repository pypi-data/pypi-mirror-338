from gravity_controller_operator.controllers_super import ControllerInterface, \
    RelayControllerInterface
from requests.auth import HTTPBasicAuth
from netping_contr import mixins
import netping_contr.main
import requests


class NetPingDevice(mixins.NetPingResponseParser):
    ip = None
    port = None
    username = None
    password = None
    index = None
    schema = "http://"
    status_on = 1
    status_off = 0

    def __init__(self, ip, port=80, index=None, username="visor",
                 password="ping", schema="http://", status_on=1, status_off=0):
        self.ip = ip
        self.port = port
        self.index = index
        self.username = username
        self.password = password
        self.schema = schema
        self.status_on = status_on
        self.status_off = status_off

    def get_full_url(self):
        return f"{self.schema}{self.ip}:{self.port}"

    def get_relay_info(self, relay_num=None):
        """
        Запрос состояния реле

        :param relay_num: номер реле
        :return:relay_result('ok')
                relay_result('error')
        """
        if not relay_num:
            relay_num = self.index
        return requests.get(
            url=f"{self.get_full_url()}/relay.cgi?r{relay_num}",
            auth=HTTPBasicAuth(self.username, self.password)
        )

    def get_all_relays_info(self, start=1):
        states = []
        for i in range(start, 5):
            response = self.get_relay_info(i)
            states.append(response)
        return states

    def get_all_relay_states(self):
        start = 1
        response = self.get_all_relays_info(start)
        states = {}
        for res in response:
            decoded = self.parse_relay_state(res)
            states[start] = decoded
            start += 1
        return states

    def change_relay_status(self, relay_num, status):
        """
        Управление реле

        :param relay_num: Номер реле
        :param status: Новое состояние реле (1 - включено, 0 - выключено)
        :return:relay_result('ok')
                relay_result('error')
        """
        return requests.get(
            url=f"{self.get_full_url()}/relay.cgi?r{relay_num}={status}",
            auth=HTTPBasicAuth(self.username, self.password)
        )

    def get_di_status(self, line_num=None):
        """
        Запрос состояния линии

        :param line_num: номер линии
        :return:io_result('error')
                io_result('ok', -1, 1, 339)

            Первый аргумент: всегда 'ok' (при ошибке запроса — 'error').
            Второй аргумент: всегда «-1», для расширения API в будущем.
            Третий аргумент: текущее моментальное состояние IO-линии,
            включая состояние сброса.
            Четвертый аргумент: счетчик импульсов на данной IO-линии,
            считается по фронту.
        """
        if not line_num:
            line_num = self.index
        return requests.get(
            url=f"{self.get_full_url()}/io.cgi?io{line_num}",
            auth=HTTPBasicAuth(self.username, self.password)
        )

    def get_all_di_status(self):
        """
        Запрос состояния всех линий

        :return:
        """
        return requests.get(
            url=f"{self.get_full_url()}/io.cgi?io",
            auth=HTTPBasicAuth(self.username, self.password))


class NetPing2ControllerDI(ControllerInterface):
    map_keys_amount = 5
    starts_with = 0

    def __init__(self, controller):
        super(NetPing2ControllerDI, self).__init__(controller)
        self.update_dict()

    def get_phys_dict(self, *args, **kwargs):
        """ Получить состояние входов или выходов с контроллера.
        Перед возвратом привести в вид словаря,
        где ключ - это номер реле или di, значение - 0 или 1.
        """
        response_raw = self.controller.get_all_di_status()
        response_parsed = self.controller.parse_all_lines_request(
            response_raw)
        return response_parsed


class NetPing2ControllerRelay(RelayControllerInterface):
    map_keys_amount = 5
    starts_with = 0
    controller = None

    def __init__(self, controller):
        super().__init__(controller)
        self.update_dict()

    def get_phys_dict(self, *args, **kwargs):
        """ Получить состояние входов или выходов с контроллера.
        Перед возвратом привести в вид словаря,
        где ключ - это номер реле или di, значение - 0 или 1.
        """
        response_parsed = self.controller.get_all_relay_states()
        return response_parsed

    def change_phys_relay_state(self, num, state: bool):
        response = self.controller.change_relay_status(relay_num=num,
                                                       status=state)
        while "error" in response:
            response = self.controller.change_relay_status(
                relay_num=num, status=state)


class NetPing2Controller:
    model = "netping_relay"

    def __init__(self, ip, port=80, username="visor", password="ping",
                 name="netping_relay2", *args, **kwargs):
        self.controller_interface = NetPingDevice(
            ip=ip,
            port=port,
            username=username,
            password=password
        )
        self.relay_interface = NetPing2ControllerRelay(
            self.controller_interface)
        self.di_interface = NetPing2ControllerDI(
            self.controller_interface)
