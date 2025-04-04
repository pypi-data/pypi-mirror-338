import httpx
import swcpy_sdk.swc_config as config
from .schemas import League, Team, Player, Performance, Counts
from typing import List
import backoff
import logging

logger = logging.getLogger(__name__)

class SWCClient:
    """Interacts with the Sports World Central API."""

    HEALTH_CHECK_ENDPOINT = "/"
    LIST_LEAGUES_ENDPOINT = "/v0/leagues/"
    LIST_PLAYERS_ENDPOINT = "/v0/players/"
    LIST_PERFORMANCES_ENDPOINT = "/v0/performances/"
    LIST_TEAMS_ENDPOINT = "/v0/teams/"
    GET_COUNTS_ENDPOINT = "/v0/counts/"

    def __init__(self, input_config: config.SWCConfig):
        """Class constructor that sets variables from configuration object."""
        logger.debug(f"Input config: {input_config}")

        self.swc_base_url = input_config.swc_base_url
        self.backoff = input_config.swc_backoff
        self.backoff_max_time = input_config.swc_backoff_max_time

        if self.backoff:
            self.call_api = backoff.on_exception(
                wait_gen=backoff.expo,
                exception=(httpx.RequestError, httpx.HTTPStatusError),
                max_time=self.backoff_max_time,
                jitter=backoff.random_jitter,
            )(self.call_api)

    def call_api(self, api_endpoint: str, api_params: dict = None) -> httpx.Response:
        """Makes API call and logs errors."""
        if api_params:
            api_params = {key: val for key, val in api_params.items() if val is not None}

        try:
            with httpx.Client(base_url=self.swc_base_url) as client:
                logger.debug(f"Calling API: {self.swc_base_url}{api_endpoint} with params: {api_params}")
                response = client.get(api_endpoint, params=api_params)
                response.raise_for_status()
                return response
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error: {e.response.status_code} {e.response.text}")
            raise
        except httpx.RequestError as e:
            logger.error(f"Request error: {str(e)}")
            raise

    def get_health_check(self) -> httpx.Response:
        """Checks if API is running and healthy."""
        return self.call_api(self.HEALTH_CHECK_ENDPOINT)

    def list_leagues(self, skip: int = 0, limit: int = 100, minimum_last_changed_date: str = None, league_name: str = None) -> List[League]:
        params = {"skip": skip, "limit": limit, "minimum_last_changed_date": minimum_last_changed_date, "league_name": league_name}
        response = self.call_api(self.LIST_LEAGUES_ENDPOINT, params)
        return [League(**league) for league in response.json()]

    def get_league_by_id(self, league_id: int) -> League:
        response = self.call_api(f"{self.LIST_LEAGUES_ENDPOINT}{league_id}")
        return League(**response.json())

    def get_counts(self) -> Counts:
        response = self.call_api(self.GET_COUNTS_ENDPOINT)
        return Counts(**response.json())

    def list_teams(self, skip: int = 0, limit: int = 100, minimum_last_changed_date: str = None, team_name: str = None, league_id: int = None):
        params = {"skip": skip, "limit": limit, "minimum_last_changed_date": minimum_last_changed_date, "team_name": team_name, "league_id": league_id}
        response = self.call_api(self.LIST_TEAMS_ENDPOINT, params)
        return [Team(**team) for team in response.json()]

    def list_players(self, skip: int = 0, limit: int = 100, minimum_last_changed_date: str = None, first_name: str = None, last_name: str = None):
        params = {"skip": skip, "limit": limit, "minimum_last_changed_date": minimum_last_changed_date, "first_name": first_name, "last_name": last_name}
        response = self.call_api(self.LIST_PLAYERS_ENDPOINT, params)
        return [Player(**player) for player in response.json()]

    def get_player_by_id(self, player_id: int):
        response = self.call_api(f"{self.LIST_PLAYERS_ENDPOINT}{player_id}")
        return Player(**response.json())

    def list_performances(self, skip: int = 0, limit: int = 100, minimum_last_changed_date: str = None):
        params = {"skip": skip, "limit": limit, "minimum_last_changed_date": minimum_last_changed_date}
        response = self.call_api(self.LIST_PERFORMANCES_ENDPOINT, params)
        return [Performance(**performance) for performance in response.json()]
