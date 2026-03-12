from homeassistant import config_entries
from homeassistant.const import CONF_API_KEY

class OrleansDechetConfigFlow(config_entries.ConfigFlow, domain="orleans_dechet"):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Orléans Déchet", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_API_KEY): str
            })
        )