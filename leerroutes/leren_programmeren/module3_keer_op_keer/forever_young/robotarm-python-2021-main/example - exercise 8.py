from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.moveRight()
for moves in range(7):
    robotArm.grab()
    for i in range(8):
        robotArm.moveRight()
    robotArm.drop()
    if moves <6:
        for i in range(8):
            robotArm.moveLeft()
robotArm.wait()