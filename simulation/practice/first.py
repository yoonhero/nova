import cv2
import random
import matplotlib.pyplot as plt
import time
import argparse
import sys
import os
import glob

try:
    sys.path.append(glob.glob('../carla/dist/carla-%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    print("?")
    pass

import carla

from carla import ColorConverter as cc




def main():
    actorList = []
    try:
        client = carla.Client("localhost",2000)
        client.set_timeout(10.0)
        world = client.load_world("Town02")
        print(client.get_available_maps())

        blueprintLibrary = world.get_blueprint_library()
        vechile_bp = blueprintLibrary.filter('cybertruck')[0]
        transform = carla.Transform(carla.Location(x=130, y=195, z=40), carla.Rotation(yaw=180))
        vechile = world.spawn_actor(vechile_bp, transform)
        actorList.append(vechile)
        
        camera_bp = blueprintLibrary.find('sensor.camera.rgb')
        camera_bp.set_attribute('image_size_x', str(800))
        camera_bp.set_attribute('image_size_y', str(600))
        camera_bp.set_attribute('fov', str(90))
        camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
        camera = world.spawn_actor(camera_bp,camera_transform, attach_to=vechile)
        # camera.listen(lambda image: image.save_to_disk('output/%d064.png'%image.frame))

        transform.rotation.yaw = -180 
        for _ in range(0, 10):
            transform.location.x += 8
            bp = blueprintLibrary.filter('cybertruck')[0]
            npc = world.try_spawn_actor(bp, transform)

            if npc is not None:
                actorList.append(npc)
                npc.set_autopilot = True
                print('craeted%s'%npc.type_id)
        
        time.sleep(15)
        
    finally:
        print("delete actorList")
        client.apply_batch([carla.command.DestroyActor(x) for x in actorList])

if __name__ == '__main__':
    main()