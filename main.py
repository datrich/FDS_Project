import cv2 
import os 
from astra_camera import Camera

def data_collection(cam):
    try:
        output_folder = 'data/Part_1'
        frame = 1
        while True:
            _, rgb = cam.get_depth_and_color()
            rgb = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
            filename = f'img_{frame}.jpg'
            filepath = os.path.join(output_folder, filename)
            if frame % 2 ==0: 
                cv2.imwrite(filepath, rgb)
            frame += 1
            cv2.imshow('RGB Image', rgb)
            key = cv2.waitKey(1)
            if key == 27: 
                break 
    except Exception as e:
        print(e)
    finally: 
        cam.unload()

cam = Camera()
data_collection(cam)