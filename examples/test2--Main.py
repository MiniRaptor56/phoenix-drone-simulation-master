## This code was written by Gemini AI while searching for Flow Deck specific example code

import time
import cflib.crtp
from cflib.positioning.motion_commander import MotionCommander
import cflib.utils.callbacks
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

# URI to the Crazyflie to be controlled
uri = 'radio://0/80/250K'

# Initialize Crazyflie
cflib.crtp.init_drivers()
cflib.crtp.init_drivers(enable_debug_driver=False)

cf = Crazyflie(rw_cache='./cache')
with SyncCrazyflie(uri, cf=cf) as scf:
    # Arm the Crazyflie
    scf.cf.platform.send_arming_request(True)
    time.sleep(1.0)

    with MotionCommander(scf) as mc:
        # Take off to a height of 20 cm
        print('Taking off!')
        mc.take_off(0.2)
        time.sleep(1)

        # Move forward 0.5 meters at 0.5 m/s
        print('Moving forward 0.5m')
        mc.forward(0.5)
        time.sleep(1)

        # Move backward 0.5 meters at 0.5 m/s
        print('Moving backward 0.5m')
        mc.back(0.5)
        time.sleep(1)

        # Turn 90 degrees clockwise at 10 degrees/s
        print('Turning 90 degrees clockwise')
        mc.turn_left(90, velocity=10)
        time.sleep(1)

        # Move 0.5 meters up at 0.5 m/s
        print('Moving up 0.5m')
        mc.up(0.5)
        time.sleep(1)
        
        # Land
        print('Landing!')
        mc.land()
        time.sleep(1)
    
# Disconnect from Crazyflie
print("Disconnecting from Crazyflie.")
cf.close_link()

