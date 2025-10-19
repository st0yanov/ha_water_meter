"""Initialize the Water Meter integration."""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Water Meter from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a Water Meter config entry."""
    return await hass.config_entries.async_forward_entry_unload(entry, "sensor")
