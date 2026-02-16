## This code was written by Gemini AI for code that allows crazyflie to fly in a circle

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
            print('Taking off!')
            time.sleep(1) # Wait briefly after the "take-off" command is sent

            # Fly a circle to the right
            # Arguments: radius (meters), velocity (m/s), angle_degrees
            print('Doing a 270 degree circle to the right with a 0.5m radius')
            mc.circle_right(0.25, velocity=1.5, angle_degrees=180)

            # The MotionCommander automatically handles landing when it goes out of scope
            print('Landing!')
