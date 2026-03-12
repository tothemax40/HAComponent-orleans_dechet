import requests
from bs4 import BeautifulSoup
from datetime import datetime
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CONF_API_KEY

async def async_setup_entry(hass, entry, async_add_entities):
    api_key = entry.data[CONF_API_KEY]
    sensor = OrleansDechetSensor(api_key)
    async_add_entities([sensor], True)

class OrleansDechetSensor(SensorEntity):
    def __init__(self, api_key):
        self._api_key = api_key
        self._state = None
        self._attributes = {}

    @property
    def name(self):
        return "Orléans Déchet"

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    async def async_update(self):
        url = f"https://api.orleans-metropole.fr/dechets?key={self._api_key}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Parse the data and update self._state and self._attributes