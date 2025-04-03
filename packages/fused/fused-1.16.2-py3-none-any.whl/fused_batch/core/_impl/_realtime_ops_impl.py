from typing import Literal, Optional

from fused_batch._options import options as OPTIONS
from fused_batch.api import AUTHORIZATION, FusedAPI


def make_realtime_url(client_id: Optional[str]) -> str:
    if client_id is None:
        api = FusedAPI()
        client_id = api._automatic_realtime_client_id()

        if client_id is None:
            raise ValueError("Failed to detect realtime client ID")

    return f"{OPTIONS.base_url}/realtime/{client_id}"


def make_shared_realtime_url(id: str) -> str:
    return f"{OPTIONS.base_url}/realtime-shared/{id}"


def get_recursion_factor() -> int:
    return 1


def default_run_engine() -> Literal["realtime", "batch", "local"]:
    if OPTIONS.default_udf_run_engine is not None:
        return OPTIONS.default_udf_run_engine
    return "realtime"
