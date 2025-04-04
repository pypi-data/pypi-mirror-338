from .module_imports import key
from uplink.retry.when import status_5xx
from uplink import (
    get as http_get,
    Consumer,
    returns,
    headers,
    retry,
    Query,
)


@headers({"Ocp-Apim-Subscription-Key": key})
@retry(max_attempts=20, when=status_5xx())
class _Analysis(Consumer):
    """Inteface to API Info resource for the RockyRoad API."""

    def __init__(self, Resource, *args, **kw):
        self._base_url = Resource._base_url
        super().__init__(base_url=Resource._base_url, *args, **kw)

    @returns.json
    @http_get("analysis/forms/results")
    def form_results(self, form_type: Query = None, model: Query = None):
        """Return list of form results"""

    @returns.json
    @http_get("analysis/forms/columns")
    def form_columns(self, form_type: Query = None, model: Query = None):
        """Return list of form columns."""
