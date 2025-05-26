import can
import struct

bus = can.interface.Bus(channel='can0', bustype='socketcan')
speed = 50        # signed int16
steering = 90     # signed int16

# Pack the speed and steering into 4 bytes
data = struct.pack('>hh', speed, steering)  # '>hh' means big-endian two int16

msg = can.Message(arbitration_id=0x21, data=data, is_extended_id=False)
bus.send(msg)
