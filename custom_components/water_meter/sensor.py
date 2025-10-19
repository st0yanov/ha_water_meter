"""Water Meter sensor entity."""
from homeassistant.components.integration.sensor import IntegrationSensor
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import UnitOfVolume
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.util import slugify

from .const import DOMAIN, CONF_SOURCE_SENSOR, CONF_FRIENDLY_NAME


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up Water Meter sensor from config entry."""
    source_sensor = entry.data[CONF_SOURCE_SENSOR]
    friendly_name = entry.data[CONF_FRIENDLY_NAME]

    async_add_entities([WaterMeter(hass, source_sensor, friendly_name)], True)


class WaterMeter(IntegrationSensor):
    """Integrates flow rate into total water usage."""

    def __init__(self, hass, source_sensor: str, friendly_name: str):
        slug_name = slugify(friendly_name)
        unique_id = f"{slug_name}_meter"

        super().__init__(
            hass=hass,
            name=friendly_name,
            unique_id=unique_id,
            source_entity=source_sensor,
            round_digits=2,
            unit_time="min",
            unit_prefix=None,
            integration_method="left",
            max_sub_interval=None
        )

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, unique_id)},
            name=f"{friendly_name} Meter",
            manufacturer="Custom",
            model="Integration-based Meter",
        )

    @property
    def device_class(self) -> SensorDeviceClass:
        """Return the sensor device class."""
        return SensorDeviceClass.WATER

    @property
    def icon(self) -> str:
        """Return the icon for this sensor."""
        return "mdi:water-pump"

    @property
    def native_unit_of_measurement(self) -> str:
        """Return the unit of measurement for this sensor."""
        return UnitOfVolume.LITERS
