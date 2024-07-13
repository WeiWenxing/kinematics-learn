from servo_control import IK_Control
from hardware_interface import Servo
hardware_interface = Servo()
theta = -2.356194490192345
gamma = 1.5707963267948966
delta = 0.02
ik = IK_Control([theta, gamma], delta)
ik.InProgress = True
ik.runLoop(hardware_interface)