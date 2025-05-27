import can
import struct
import socket  # dùng hton/ntoh

speed = 50
steer = 90

# chuyển sang big-endian chuẩn network
speed_be = socket.htons(speed)
steer_be = socket.htons(steer)

data = struct.pack('>HH', speed_be, steer_be)  # > là big-endian, H là uint16

msg = can.Message(arbitration_id=0x21, data=data, is_extended_id=False)
bus.send(msg)
