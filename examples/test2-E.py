"""
Example script that allows a user to "push" the Crazyflie 2.x around
using your hands while it's hovering.

This examples uses the Flow and Multi-ranger decks to measure distances
in all directions and tries to keep away from anything that comes closer
than 0.2m by setting a velocity in the opposite direction.

The demo is ended by either pressing Ctrl-C or by holding your hand above the
Crazyflie.
"""
## This code was written by Gemini AI while searching for Flow Deck specific example code
import logging
import sys
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils.multiranger import Multiranger

URI = 'radio://0/80/2M'

if len(sys.argv) > 1:
    URI = sys.argv[1]

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)


def is_close(range):
    MIN_DISTANCE = 0.2  # m

    if range is None:
        return False
    else:
        return range < MIN_DISTANCE


if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    cf = Crazyflie(rw_cache='./cache')
    with SyncCrazyflie(URI, cf=cf) as scf:
        # Arm the Crazyflie
        scf.cf.platform.send_arming_request(True)
        time.sleep(1.0)

        with MotionCommander(scf) as mc:

            mc.up(0.5, velocity=1)
            time.sleep(1)

            # Move forward 0.5 meters at 0.5 m/s
            mc.forward(20, velocity=5)
            time.sleep(1)

            # Fly a circle to the right
            # Arguments: radius (meters), velocity (m/s), angle_degrees
            print('Doing a 270 degree circle to the right with a 0.5m radius')
            mc.circle_right(1, velocity=5, angle_degrees=180)

            # Move forward 0.5 meters at 0.5 m/s
            print('Moving forward 2m')
            mc.forward(20, velocity=5)
            time.sleep(1)
            
            # Land
            print('Landing!')
            mc.land()
            time.sleep(1)