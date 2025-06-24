import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/isha/repos/autonomy-diagnostic-dashboard/vac_robot/install/vac_robot'
