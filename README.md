# Water Meter (HACS Integration)

A flexible Home Assistant custom integration that creates a **virtual water meter** based on any flow rate sensor you choose.

## Features

- Select source sensor from UI
- Name your own water meter ("Hot water", "Cold water", etc.)
- Automatically integrates flow over time
- Device class and icon preconfigured (`mdi:water-pump`, `water`)

## Installation

1. Add this repository to HACS → Custom repositories → Type: Integration.
2. Install **Water Meter**.
3. Go to **Settings → Devices & Services → Add Integration → Water Meter**.
4. Choose your flow sensor and give your meter a name (e.g. "Hot water").
5. Done! A new entity like `sensor.hot_water_meter` will appear.
