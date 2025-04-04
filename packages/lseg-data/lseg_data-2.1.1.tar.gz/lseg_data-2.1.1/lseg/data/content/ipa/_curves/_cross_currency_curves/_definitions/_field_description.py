from typing import TYPE_CHECKING

from ...._object_definition import ObjectDefinition

if TYPE_CHECKING:
    from ......_types import OptStrings


class FieldDescription(ObjectDefinition):
    """
    Creates the Cross Currency curve definition with the definition provided.

    Parameters
    ----------
    historical_fid_priority : string, optional
        The list of historical fid (field identifier) name used to get the market data.
    real_time_fid_priority : string, optional
        The list of real-time fid (field identifier) name used to get the market data.
    """

    def __init__(
        self,
        historical_fid_priority: "OptStrings" = None,
        real_time_fid_priority: "OptStrings" = None,
    ) -> None:
        super().__init__()
        self.historical_fid_priority = historical_fid_priority
        self.real_time_fid_priority = real_time_fid_priority

    @property
    def historical_fid_priority(self):
        """
        The list of historical fid (field identifier) name used to get the market data.
        :return: list string
        """
        return self._get_list_parameter(str, "historicalFidPriority")

    @historical_fid_priority.setter
    def historical_fid_priority(self, value):
        self._set_list_parameter(str, "historicalFidPriority", value)

    @property
    def real_time_fid_priority(self):
        """
        The list of real-time fid (field identifier) name used to get the market data.
        :return: list string
        """
        return self._get_list_parameter(str, "realTimeFidPriority")

    @real_time_fid_priority.setter
    def real_time_fid_priority(self, value):
        self._set_list_parameter(str, "realTimeFidPriority", value)
