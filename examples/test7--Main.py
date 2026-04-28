import time
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.sync import SyncLogger

# URI of the Crazyflie
uri = 'radio://0/80/2M/E7E7E7E7E7'

def simple_log_async(scf, logconf_name, variable):
    cf = scf.cf
    log_conf = LogConfig(name=logconf_name, period_in_ms=100)
    log_conf.add_variable(variable, 'float')

    with SyncLogger(scf, log_conf) as logger:
        for log_entry in logger:
            data = log_entry[1]
            # range.zrange is in meters
            print(f'{variable}: {data[variable]:.3f} m')
            
            # Exit after a while
            if time.time() > time.time() + 10: 
                break

if __name__ == '__main__':
    cflib.crtp.init_drivers()
    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        # 'range.zrange' is direct sensor data, 'stateEstimate.z' is Kalman filtered
        simple_log_async(scf, 'Range', 'range.zrange')
