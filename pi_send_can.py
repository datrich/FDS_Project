import can
import time

# Set up CAN bus (socketcan uses 'can0')
bus = can.interface.Bus(channel='can0', bustype='socketcan')

# Continuous data loop
try:
    while True:
        left_right = 10    # example: right
        forward_back = 20  # example: forward
        stop_flag = 0      # 0 = running, 1 = stop

        # Construct and send the CAN message
        msg = can.Message(
            arbitration_id=0x12,
            data=[left_right, forward_back, stop_flag],
            is_extended_id=False
        )

        try:
            bus.send(msg)
            print(f"Sent: {msg.data}")
        except can.CanError:
            print("Message not sent")

        time.sleep(0.05)  # send every 50 ms

except KeyboardInterrupt:
    print("Stopped by user")
