"""Config flow for Water Meter integration."""
from homeassistant import config_entries
import voluptuous as vol
from homeassistant.helpers import entity_registry as er
from homeassistant.core import HomeAssistant
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

        hass: HomeAssistant = self.hass
        entity_registry = er.async_get(hass)
        sensor_entities = [
            entity.entity_id
            for entity in entity_registry.entities.values()
            if entity.entity_id.startswith("sensor.")
        ]

        schema = vol.Schema(
            {
                vol.Required(CONF_SOURCE_SENSOR): vol.In(sorted(sensor_entities)),
                vol.Required(CONF_FRIENDLY_NAME): str
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )
