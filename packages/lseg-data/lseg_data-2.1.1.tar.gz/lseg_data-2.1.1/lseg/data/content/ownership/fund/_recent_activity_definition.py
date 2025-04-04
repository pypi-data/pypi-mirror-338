from typing import Union, TYPE_CHECKING

from ..._content_data import Data
from ..._content_provider_layer import ContentUsageLoggerMixin
from ...._content_type import ContentType
from ...._tools import validate_bool_value, try_copy_to_list
from ..._header_type import get_header_type_by_use_field_names_in_headers
from ....delivery._data._data_provider import DataProviderLayer, Response

if TYPE_CHECKING:
    from .._enums import SortOrder
    from ...._types import ExtendedParams, StrStrings


class Definition(
    ContentUsageLoggerMixin[Response[Data]],
    DataProviderLayer[Response[Data]],
):
    """
    This class describe parameters to retrieve the latest 5 buy or sell activites for the requested company.

    Parameters
    ----------
    universe: str, list of str
        The Universe parameter allows the user to define the companies for which the content is returned.

    sort_order: str, SortOrder
        The sortOrder parameter specifies ascending (asc) or descending (desc) Sort Order.

    use_field_names_in_headers: bool, optional
        Return field name as column headers for data instead of title

    extended_params : ExtendedParams, optional
        If necessary other parameters.

    Examples
    --------
    >>> from lseg.data.content import ownership
    >>> definition = ownership.fund.recent_activity.Definition("TRI.N", ownership.SortOrder.ASCENDING)
    >>> response = definition..get_data()
    """

    _USAGE_CLS_NAME = "Ownership.Fund.RecentActivityDefinition"

    def __init__(
        self,
        universe: "StrStrings",
        sort_order: Union[str, "SortOrder"],
        use_field_names_in_headers: bool = False,
        extended_params: "ExtendedParams" = None,
    ):
        validate_bool_value(use_field_names_in_headers)
        universe = try_copy_to_list(universe)
        header_type = get_header_type_by_use_field_names_in_headers(use_field_names_in_headers)

        super().__init__(
            ContentType.OWNERSHIP_FUND_RECENT_ACTIVITY,
            universe=universe,
            sort_order=sort_order,
            header_type=header_type,
            extended_params=extended_params,
        )
