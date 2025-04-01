from typing import Any, Literal, Union

from .._constants import (
    INTELLIGENT_PRODUCT_SEARCH_MAX_PAGE_SIZE,
    INTELLIGENT_PRODUCT_SEARCH_START_PAGE,
    MIN_PAGE_SIZE,
)
from .._dto import VTEXPaginatedItemsResponse
from .._sentinels import UNDEFINED, UndefinedSentinel
from .._types import OrderingDirectionType
from .._utils import omitting_undefined
from .base import BaseAPI


class IntelligentSearchAPI(BaseAPI):
    """
    Client for the Intelligent Search API.
    https://developers.vtex.com/docs/api-reference/intelligent-search-api
    """

    ENVIRONMENT = "vtexcommercestable"

    def search_products(
        self,
        product_ids: Union[list[str], UndefinedSentinel] = UNDEFINED,
        sku_ids: Union[list[str], UndefinedSentinel] = UNDEFINED,
        simulation_behavior: str = "skip",
        show_sponsored: bool = True,
        fuzzy: bool = True,
        operator: Literal["and", "or"] = "and",
        order_by_field: str = "release",
        order_by_direction: OrderingDirectionType = "desc",
        page: int = INTELLIGENT_PRODUCT_SEARCH_START_PAGE,
        page_size: int = INTELLIGENT_PRODUCT_SEARCH_MAX_PAGE_SIZE,
        **kwargs: Any,
    ) -> VTEXPaginatedItemsResponse[Any, Any]:
        """
        Search for products in the catalog.
        """
        if product_ids and sku_ids:
            raise ValueError("You can only search by product IDs or SKU IDs, not both.")

        q: Union[str, UndefinedSentinel] = UNDEFINED
        if isinstance(product_ids, list) and product_ids:
            q = f"product.id:{';'.join([str(id) for id in product_ids])}"
        elif isinstance(sku_ids, list) and sku_ids:
            q = f"sku.id:{';'.join([str(id) for id in sku_ids])}"

        return self._request(
            method="GET",
            endpoint="/api/io/_v/api/intelligent-search/product_search/",
            environment=self.ENVIRONMENT,
            params=omitting_undefined({
                "q": q,
                "simulationBehavior": simulation_behavior,
                "showSponsored": show_sponsored,
                "fuzzy": fuzzy,
                "operator": operator,
                "sort": f"{order_by_field}:{order_by_direction}",
                "page": max(page, INTELLIGENT_PRODUCT_SEARCH_START_PAGE),
                "count": max(
                    min(page_size, INTELLIGENT_PRODUCT_SEARCH_MAX_PAGE_SIZE),
                    MIN_PAGE_SIZE,
                ),
            }),
            config=self.client.config.with_overrides(**kwargs),
            response_class=VTEXPaginatedItemsResponse[Any, Any],
        )
