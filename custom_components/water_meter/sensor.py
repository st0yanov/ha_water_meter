"""Water Meter sensor entity."""
from homeassistant.components.integration.sensor import IntegrationSensor
from homeassistant.const import UnitOfVolume
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.util import slugify

from .const import DOMAIN, CONF_SOURCE_SENSOR, CONF_FRIENDLY_NAME


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Water Meter sensor."""
    if discovery_info is None:
        return

    source_sensor = discovery_info.get(CONF_SOURCE_SENSOR)
    friendly_name = discovery_info.get(CONF_FRIENDLY_NAME)
    async_add_entities([WaterMeter(hass, source_sensor, friendly_name)], True)


class WaterMeter(IntegrationSensor):
    """Integrates flow rate into total water usage."""

    def __init__(self, hass, source_sensor: str, friendly_name: str):
        slug_name = slugify(friendly_name)
        super().__init__(
            hass=hass,
            name=f"{slug_name}_meter",
            source_entity=source_sensor,
            round_digits=2,
            unit_time="min",
            method="left",
        )
        self._attr_unique_id = f"{slug_name}_meter_{source_sensor}"
        self._attr_name = friendly_name
        self._attr_icon = "mdi:water-pump"
        self._attr_device_class = "water"
        self._attr_native_unit_of_measurement = UnitOfVolume.CUBIC_METERS
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, source_sensor)},
            name=f"{friendly_name} Meter",
            manufacturer="Custom",
            model="Integration-based Meter",
        )