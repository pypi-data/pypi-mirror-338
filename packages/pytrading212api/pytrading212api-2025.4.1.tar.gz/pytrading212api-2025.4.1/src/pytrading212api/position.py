import logging
from logging import Logger
from datetime import datetime
from .api import Trading212API
from typing import Union

logger: Logger = logging.getLogger(__package__)


class Position:
    """
    Class representing a Trading212 position

    Methods
    -------
    update_properties
        uses the Tradin212 object to call the Trading212 aPI and return the current position.
    """

    def __init__(
        self, api: Trading212API, data: dict[str : Union[str, int, float]]
    ) -> None:
        """
        Constructs an Trading212 Position object representing the generation asset

        Parameters
        ----------
        api (Trading212):Trading212API object used to call the Trading212 API
        data (dict):Data returned from the Tradin212 API showing the details of the position
        """
        self._api = api
        self._ticker = data["ticker"]
        self._quantity = data["quantity"]
        self._averagePrice = data["averagePrice"]
        self._currentPrice = data["currentPrice"]
        self._ppl = data["ppl"]
        self._fxPpl = data["fxPpl"]
        self._initialFillDate = datetime.fromisoformat(data["initialFillDate"])
        self._frontend = data["frontend"]
        self._maxBuy = data["maxBuy"]
        self._maxSell = data["maxSell"]
        self._pieQuantity = data["pieQuantity"]

    @property
    def ticker(self) -> str:
        return self._ticker

    @property
    def quantity(self) -> float:
        return self._quantity

    @property
    def average_price(self) -> str:
        return self._averagePrice

    @property
    def api(self) -> Trading212API:
        return self._api

    @property
    def current_price(self) -> str:
        return self._currentPrice

    @property
    def ppl(self) -> str:
        return self._ppl

    @property
    def fxPpl(self) -> str:
        return self._fxPpl

    @property
    def initial_fill_date(self) -> datetime:
        return self._initialFillDate

    @property
    def frontend(self) -> str:
        return self._frontend

    @property
    def max_buy(self) -> str:
        return self._maxBuy

    @property
    def max_sell(self) -> str:
        return self._maxSell

    @property
    def pie_quantity(self) -> dict:
        return self._pieQuantity

    async def update_position(self, data: dict[str : Union[str, int, float]]) -> None:
        self._ticker = data["ticker"]
        self._quantity = data["quantity"]
        self._averagePrice = data["averagePrice"]
        self._currentPrice = data["currentPrice"]
        self._ppl = data["ppl"]
        self._fxPpl = data["fxPpl"]
        self._initialFillDate = datetime.fromisoformat(data["initialFillDate"])
        self._frontend = data["frontend"]
        self._maxBuy = data["maxBuy"]
        self._maxSell = data["maxSell"]
        self._pieQuantity = data["pieQuantity"]

    async def update_data(
        self,
    ) -> None:
        """
        Calls the Trading 212 api to update the position.

        Returns
        -------
        None
        """
        logging.info(f"Updating position for {self.ticker}")
        data = await self._api.get_positions(ticker=self._ticker)

        await self.update_position(data)
