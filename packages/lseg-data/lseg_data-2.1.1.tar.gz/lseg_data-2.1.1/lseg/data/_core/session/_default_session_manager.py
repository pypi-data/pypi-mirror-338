from typing import TYPE_CHECKING, Any, Generic, TypeVar, Union

if TYPE_CHECKING:
    from . import Session


# --------------------------------------
# PUBLIC API
# --------------------------------------


def set_default(session: "Session") -> None:
    """
    Set the default session.

    Parameters
    ----------
    session: Session
        The logical session to the data platform.

    Returns
    -------
    """
    _rd_default_session_manager.set_default_session(session)


def get_default() -> "Session":
    """
    Gets the default session.

    Returns
    -------
    Session
    """
    return _rd_default_session_manager.try_get_default_session()


# --------------------------------------
# PRIVATE API
# --------------------------------------
class SessionManager:
    def __init__(self, arg: Union["Session", "Wrapper"] = None) -> None:
        if not isinstance(arg, Wrapper):
            arg = Wrapper(arg)
        self._session_wrapper: Wrapper = arg

    def close_default_session(self):
        if self._session_wrapper.get() is not None:
            self._session_wrapper.get().close()

    def clear_default_session(self):
        self.close_default_session()
        self._session_wrapper.set(None)

    def has_session(self):
        return self._session_wrapper.get() is not None


class RDDefaultSessionManager(SessionManager):
    def try_get_default_session(self):
        """
        Returns default session or raise exception if user didn't set default session.

        Raises
        ------
        Exception
            If user didn't set default session

        Returns
        ------
        Session object
        """
        if not self._session_wrapper.get():
            raise AttributeError("No default session created yet. Please create a session first!")
        return self._session_wrapper.get()

    def set_default_session(self, session) -> None:
        """
        Set default session.

        Parameters
        ----------
            session: Session
                session object

        Raises
        ----------
        Exception
            If user provided invalid data type
        """
        from . import Session

        if session is None:
            return self.clear_default_session()

        if not isinstance(session, Session):
            raise TypeError("Invalid argument")

        self._session_wrapper.set(session)

    def set_session(self, session):
        self._session_wrapper.set(session)


T = TypeVar("T")


class Wrapper(Generic[T]):
    def __init__(self, wrapped: T = None):
        self._wrapped: T = wrapped

    def get(self) -> T:
        return self._wrapped

    def set(self, value: T):
        self._wrapped = value


def get_valid_session(session: Any) -> "Session":
    if session is None:
        session = get_default()
    if session is None:
        raise AttributeError("A Session must be started")
    return session


_session_wrapper = Wrapper()
_rd_default_session_manager = RDDefaultSessionManager(_session_wrapper)
