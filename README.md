# ps-device-distance-script

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)


## Installation

Download the `device_distance_script.py.py` file and put it in your /config/python_scripts directory or install via HACS.

Add ```https://github.com/H89P/ps-device_distance_script``` as a custom repo to the hacs installation with type python_script

## Script arguments

| key |	required |	type |	description |
| ------------- | ------------- | ------------- | ------------- |
| device_1:  | true | string | Name of the first device_tracker e.g. phone
| device_2:  | true | string | Name of the econd device_tracker e.g. car
| unit:  | true | string | metric or imperial

### Usage:

```yaml
device_id_1: <name of device_tracker device 1>
device_id_2: <name of device_tracker device 2>
unit: metric
```

#### Example:
```yaml
device_id_1: phone
device_id_2: car
unit: metric
```

#### Result:
A result a sensor is created:
```yaml
sensor.distance_<name of device_tracker device 1>_<name of device_tracker device 1>
state: <distance>
icon: mdi:map-marker-distance
friendly_name: Distance between <name of device_tracker device 1> and <name of device_tracker device 2>
unit_of_measurement: mi
devices: <name of device_tracker device 1> & <name of device_tracker device 2>
```

and for the example:

```yaml
sensor.phone_cr
state: 62.23
icon: mdi:map-marker-distance
friendly_name: Distance between phone and car
unit_of_measurement: m
devices: phone & car
```


#### Example Automation to update the sensor:

```yaml
automation:
- alias: Update Phone in Car Sensor
  trigger:
  - platform: time_pattern
    minutes: "/5"
  action:
  - service: python_script.device_distance_script
    data:
      device_id_1: phone
      device_id_2: car
      unit: metric
```

## Credits
- Calculation logic gathered from [Stackoverflow](https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude)
