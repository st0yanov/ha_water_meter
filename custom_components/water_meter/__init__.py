"""Initialize the Water Meter integration."""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Water Meter from a config entry."""
    hass.async_create_task(
        hass.helpers.discovery.async_load_platform(
            "sensor", DOMAIN, {
                "source_sensor": entry.data["source_sensor"],
                "friendly_name": entry.data["friendly_name"]
            },
            entry
        )
    )
    return True
