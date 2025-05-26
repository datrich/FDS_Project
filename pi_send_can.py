import can

bus = can.interface.Bus(channel='can0', bustype='socketcan')

msg = can.Message(arbitration_id=0x12, data=[10, 20, 1], is_extended_id=False)

try:
    bus.send(msg)
    print("Message sent")
except can.CanError:
    print("Message failed")
