from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.speed = 2
for i in range(8):
    robotArm.moveRight()
for box in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white" :
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    if box <8:
        robotArm.moveLeft()
robotArm.wait()