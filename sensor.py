# sensor.py
from homeassistant.helpers.entity import Entity
from homeassistant.components.sensor import SensorEntity

class OrleansDechetsSensor(SensorEntity):
    def __init__(self, data):
        self._data = data
        self._state = None

    @property
    def name(self):
        return "Prochaine collecte des déchets"

    @property
    def state(self):
        return self._data["prochaine_date"]

    @property
    def extra_state_attributes(self):
        return {
            "type": self._data["type_de_dechet"],
            "adresse": self._data["adresse"]
        }

    def update(self):
        # Ici, tu appelles ta fonction pour récupérer les données
        self._data = recuperer_dates_dechets()