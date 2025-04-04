from typing import Union

from ._session import Session
from ._session_cxn_type import SessionCxnType
from ._session_type import SessionType
from ..._tools import urljoin, fill


class DesktopSession(Session):
    type = SessionType.DESKTOP

    def __init__(
        self,
        app_key,
        on_state=None,
        on_event=None,
        name="default",
        base_url=None,
        platform_path_rdp=None,
        platform_path_udf=None,
        handshake_url=None,
        token=None,
        dacs_position=None,
        dacs_application_id=None,
        proxies: Union[str, dict] = None,
        app_name: str = None,
    ):
        super().__init__(
            app_key=app_key,
            on_state=on_state,
            on_event=on_event,
            token=token,
            dacs_position=dacs_position,
            dacs_application_id=dacs_application_id,
            name=name,
            proxies=proxies,
            app_name=app_name,
        )
        from os import getenv

        self._port = None
        self._udf_url = None
        self._timeout = self.http_request_timeout_secs

        # Detect DP PROXY url from CODEBOOK environment to manage multi user mode
        self._dp_proxy_base_url = getenv("DP_PROXY_BASE_URL")
        if self._dp_proxy_base_url:
            self._base_url = self._dp_proxy_base_url
        else:
            self._base_url = base_url

        self._platform_path_rdp = platform_path_rdp
        self._platform_path_udf = platform_path_udf
        self._handshake_url = handshake_url

        #   uuid is retrieved in CODEBOOK environment,
        #   it's used for DP-PROXY to manage multi-user mode
        self._uuid = getenv("REFINITIV_AAA_USER_ID")

        self._is_debug() and self._logger.debug(
            "".join(
                [
                    f"DesktopSession created with following parameters:",
                    f' app_key="{app_key}", name="{name}"',
                    f' base_url="{base_url}"' if base_url is not None else "",
                    f' platform_path_rdp="{platform_path_rdp}"' if platform_path_rdp else "",
                    f' platform_path_udf="{platform_path_udf}"' if platform_path_udf else "",
                    f' handshake_url="{handshake_url}"' if handshake_url else "",
                ]
            )
        )

    def __str__(self) -> str:
        return "\n".join(
            [
                self.classname,
                fill(
                    name=self.name,
                    connection=self._connection,
                    stream_auto_reconnection=self.stream_auto_reconnection,
                    handshake_url=self._get_handshake_url(),
                    state=self._state,
                    session_id=self.session_id,
                    logger_name=self._logger.name,
                    template="\t\t{} = {}",
                    delim="\n",
                ),
            ]
        )

    def _get_session_cxn_type(self) -> SessionCxnType:
        return SessionCxnType.DESKTOP

    def _get_udf_url(self):
        """
        Returns the url to request data to udf platform.
        """
        return urljoin(self._base_url, self._platform_path_udf)

    def _get_handshake_url(self):
        """
        Returns the url to handshake with the proxy.
        """
        return urljoin(self._base_url, self._handshake_url)

    def _get_base_url(self):
        return self._base_url

    def _get_rdp_url_root(self) -> str:
        return urljoin(self._base_url, self._platform_path_rdp)

    def set_timeout(self, timeout):
        """
        Set the timeout for requests.
        """
        self._timeout = timeout

    def get_timeout(self):
        """
        Returns the timeout for requests.
        """
        return self._timeout

    def set_port_number(self, port_number):
        """
        Set the port number to reach Desktop API proxy.
        """
        self._port = port_number
        if port_number:
            try:
                protocol, path, default_port = self._base_url.split(":")
            except ValueError:
                protocol, path, *_ = self._base_url.split(":")
                default_port = ""

            try:
                url = ":".join([protocol, path, str(self._port)])
            except TypeError:
                url = ":".join([protocol, path, default_port])

            self._base_url = url
        else:
            self._udf_url = None

    def get_port_number(self):
        """
        Returns the port number
        """
        return self._port

    def __eq__(self, other: "Session"):
        if self.type != other.type:
            return False
        return self.app_key == other.app_key

    def __hash__(self):
        return super().__hash__()
