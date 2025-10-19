"""Config flow for Water Meter integration."""
from homeassistant import config_entries
from homeassistant.helpers import selector
import voluptuous as vol

from .const import DOMAIN, CONF_SOURCE_SENSOR, CONF_FRIENDLY_NAME


class WaterMeterConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Water Meter."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_FRIENDLY_NAME],
                data=user_input,
            )

        schema = vol.Schema(
            {
                vol.Required(CONF_SOURCE_SENSOR): selector.EntitySelector(
                    selector.EntitySelectorConfig(domain="sensor")
                ),
                vol.Required(CONF_FRIENDLY_NAME): str,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )
