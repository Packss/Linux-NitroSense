PAYLOAD_SIZE = 16
CHARACTER_DEVICE = "/dev/acer-gkbbl-0"
PAYLOAD_SIZE_STATIC_MODE = 4
CHARACTER_DEVICE_STATIC = "/dev/acer-gkbbl-static-0"


def set_mode(mode, zone, speed, brightness, direction, red, green, blue):
    if mode == 0:
        _set_static_mode(zone, red, green, blue)
    else:
        _set_dynamic_mode(mode, speed, brightness, direction, red, green, blue)


def _set_static_mode(zone, red, green, blue):
    if zone == 0:
        for i in range(1, 5):
            _write_to_device(
                CHARACTER_DEVICE_STATIC, _create_static_payload(i, red, green, blue)
            )
    else:
        _write_to_device(
            CHARACTER_DEVICE_STATIC, _create_static_payload(zone, red, green, blue)
        )
    _write_to_device(CHARACTER_DEVICE, _create_brightness_payload())


def _set_dynamic_mode(mode, speed, brightness, direction, red, green, blue):
    payload = [0] * PAYLOAD_SIZE
    payload[0] = mode
    payload[1] = speed
    payload[2] = brightness
    payload[3] = 8 if mode == 3 else 0
    payload[4] = direction
    payload[5] = red
    payload[6] = green
    payload[7] = blue
    payload[9] = 1
    _write_to_device(CHARACTER_DEVICE, payload)


def _create_static_payload(zone, red, green, blue):
    payload = [0] * PAYLOAD_SIZE_STATIC_MODE
    payload[0] = 1 << (zone - 1)
    payload[1] = red
    payload[2] = green
    payload[3] = blue
    return payload


def _create_brightness_payload():
    payload = [0] * PAYLOAD_SIZE
    payload[2] = 0  # Default brightness value
    payload[9] = 1
    return payload


def _write_to_device(device, payload):
    with open(device, "wb") as cd:
        cd.write(bytes(payload))
