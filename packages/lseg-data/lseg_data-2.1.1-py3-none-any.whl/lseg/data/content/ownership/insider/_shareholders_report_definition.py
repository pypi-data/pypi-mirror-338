from typing import TYPE_CHECKING, Optional

from ..._content_data import Data
from ..._content_provider_layer import ContentUsageLoggerMixin
from ...._content_type import ContentType
from ...._tools import validate_types, validate_bool_value, try_copy_to_list
from ..._header_type import get_header_type_by_use_field_names_in_headers
from ....delivery._data._data_provider import DataProviderLayer, Response

if TYPE_CHECKING:
    from ...._types import ExtendedParams, StrStrings


class Definition(
    ContentUsageLoggerMixin[Response[Data]],
    DataProviderLayer[Response[Data]],
):
    """
    This class describe parameters to retrieve the insider shareholders/declarable stakes investment
    information in the requested company at the specified historical period.

    Parameters
    ----------
    universe: str, list of str
        The Universe parameter allows the user to define the companies for which the content is returned.

    limit: int, optional
        The limit parameter is used for paging. It allows users to select the number of records to be returned.

    use_field_names_in_headers: bool, optional
        Return field name as column headers for data instead of title

    extended_params : ExtendedParams, optional
        If necessary other parameters.

    Examples
    --------
    >>> from lseg.data.content import ownership
    >>> definition = ownership.insider.shareholders_report.Definition("TRI.N")
    >>> response = definition.get_data()
    """

    _USAGE_CLS_NAME = "Ownership.Insider.ShareholdersReportDefinition"

    def __init__(
        self,
        universe: "StrStrings",
        limit: Optional[int] = None,
        use_field_names_in_headers: bool = False,
        extended_params: "ExtendedParams" = None,
    ):
        validate_types(limit, [int, type(None)], "limit")
        validate_bool_value(use_field_names_in_headers)
        universe = try_copy_to_list(universe)
        header_type = get_header_type_by_use_field_names_in_headers(use_field_names_in_headers)

        super().__init__(
            ContentType.OWNERSHIP_INSIDER_SHAREHOLDERS_REPORT,
            universe=universe,
            limit=limit,
            header_type=header_type,
            extended_params=extended_params,
        )
