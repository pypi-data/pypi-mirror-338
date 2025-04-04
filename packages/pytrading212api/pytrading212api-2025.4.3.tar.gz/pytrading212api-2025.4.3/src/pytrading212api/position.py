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
        self._average_price = data["averagePrice"]
        self._current_price = data["currentPrice"]
        self._ppl = data["ppl"]
        self._fxPpl = data["fxPpl"]
        self._initial_fill_date = datetime.fromisoformat(data["initialFillDate"])
        self._frontend = data["frontend"]
        self._max_buy = data["maxBuy"]
        self._max_sell = data["maxSell"]
        self._pie_quantity = data["pieQuantity"]
        self._buy_value = self._average_price * self._quantity
        self._current_value = self._current_price * self._quantity
        self._percent_change = round(((self._current_value-(self._average_price * self._quantity))/(self._average_price * self._quantity))*100,2)

    @property
    def ticker(self) -> str:
        return self._ticker

    @property
    def quantity(self) -> float:
        return self._quantity

    @property
    def average_price(self) -> float:
        return self._average_price

    @property
    def api(self) -> Trading212API:
        return self._api

    @property
    def current_price(self) -> float:
        return self._current_price

    @property
    def ppl(self) -> int:
        return self._ppl

    @property
    def fxPpl(self) -> int:
        return self._fxPpl

    @property
    def initial_fill_date(self) -> datetime:
        return self._initial_fill_date

    @property
    def frontend(self) -> str:
        return self._frontend

    @property
    def max_buy(self) -> float:
        return self._max_buy

    @property
    def max_sell(self) -> float:
        return self._max_sell

    @property
    def pie_quantity(self) -> int:
        return self._pie_quantity
    
    @property
    def buy_value(self) -> float:
        return self._buy_value
    
    @property
    def current_value(self) -> float:
        return self._current_value
    
    @property
    def percent_change(self) -> float:
        return self._percent_change

    async def update_position(self, data: dict[str : Union[str, int, float]]) -> None:
        self._ticker = data["ticker"]
        self._quantity = data["quantity"]
        self._average_price = data["averagePrice"]
        self._current_price = data["currentPrice"]
        self._ppl = data["ppl"]
        self._fxPpl = data["fxPpl"]
        self._initial_fill_date = datetime.fromisoformat(data["initialFillDate"])
        self._frontend = data["frontend"]
        self._max_buy = data["maxBuy"]
        self._max_sell = data["maxSell"]
        self._pie_quantity = data["pieQuantity"]
        self._buy_value = self._average_price * self._quantity
        self._current_value = self._current_price * self._quantity
        self._percent_change = round(((self._current_value-(self._average_price * self._quantity))/(self._average_price * self._quantity))*100,2)

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
