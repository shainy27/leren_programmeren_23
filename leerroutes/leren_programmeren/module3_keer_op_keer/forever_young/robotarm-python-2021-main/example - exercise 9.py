from turtle import left
from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = 2
moves = 4
for x in range(3):
    robotArm.moveRight()
for y in range(4):
    for i in range(moves):
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    robotArm.moveLeft()
    moves = moves - 1