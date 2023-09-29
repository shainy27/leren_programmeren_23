from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
teller = 9
for x in range(0,9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for x in range(0,teller):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(0,teller):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()
    teller -=1
robotArm.wait()