PAYLOAD_SIZE = 16
CHARACTER_DEVICE = "/dev/acer-gkbbl-0"

PAYLOAD_SIZE_STATIC_MODE = 4
CHARACTER_DEVICE_STATIC = "/dev/acer-gkbbl-static-0"


def set_mode(mode, zone, speed, brightness, direction, red, green, blue):
    if mode == 0:
        # Static coloring mode
        if zone == 0:       # All zones
            for i in range(1, 5):
                payload = [0] * PAYLOAD_SIZE_STATIC_MODE
                payload[0] = 1 << (i - 1)
                payload[1] = red
                payload[2] = green
                payload[3] = blue
                with open(CHARACTER_DEVICE_STATIC, 'wb') as cd:
                    cd.write(bytes(payload))
        else:
            payload = [0] * PAYLOAD_SIZE_STATIC_MODE
            payload[0] = 1 << (zone - 1)
            payload[1] = red
            payload[2] = green
            payload[3] = blue
            with open(CHARACTER_DEVICE_STATIC, 'wb') as cd:
                cd.write(bytes(payload))

        # Tell WMI To use STATIC coloring
        # Dynamic coloring mode
        payload = [0] * PAYLOAD_SIZE
        payload[2] = brightness
        payload[9] = 1
        with open(CHARACTER_DEVICE, 'wb') as cd:
            cd.write(bytes(payload))
    else:
        # Dynamic coloring mode
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

        with open(CHARACTER_DEVICE, 'wb') as cd:
            cd.write(bytes(payload))
