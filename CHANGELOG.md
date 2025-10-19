# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.0.2] - 2025-10-19

### Added

- Config Flow updated to allow **UI-based selection of source sensor**.

### Fixed

- Updated `sensor.py` and `__init__.py`, removing deprecated `hass.helpers.discovery` calls.

## [0.0.1] - 2025-10-19

### Added

- Initial release of **Water Meter** custom integration.
- UI-based configuration flow:
  - Select any existing flow rate sensor.
  - Provide a custom name (e.g., “Hot water”, “Cold water”).
- Automatically creates a corresponding integration sensor:
  - Calculates total water usage over time.
  - Preconfigured with device class `water` and icon `mdi:water-pump`.
- Fully HACS-compatible structure and metadata.
