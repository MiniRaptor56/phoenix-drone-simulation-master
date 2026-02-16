## This code was written by Gemini AI for code that allows crazyflie to fly in a circle

import time
import cflib.crtp
from cflib.crazyflie.syncronous import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

# URI to the Crazyflie to connect to
# Update this to your Crazyflie's URI
URI = 'radio://0/80/2M/E7E7E7E7E7'

if __name__ == '__main__':
    # Initialize the Crazyflie drivers
    cflib.crtp.init_drivers()

    print(f'Connecting to {URI}')
    # Connect to the Crazyflie
    with SyncCrazyflie(URI, cf=Cflib.Crazyflie()) as scf:
        # Use the MotionCommander class for simplified movement commands
        with MotionCommander(scf) as mc:
            print('Taking off!')
            time.sleep(1) # Wait briefly after the "take-off" command is sent

            # Fly a circle to the right
            # Arguments: radius (meters), velocity (m/s), angle_degrees
            print('Doing a 270 degree circle to the right with a 0.5m radius')
            mc.circle_right(0.5, velocity=0.5, angle_degrees=270)

            # The MotionCommander automatically handles landing when it goes out of scope
            print('Landing!')
