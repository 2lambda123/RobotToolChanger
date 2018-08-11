import pygame
from time import sleep
from yumipy import YuMiRobot
import datetime
import pickle
from autolab_core import RigidTransform
import tf
import math
import threading

yumi = YuMiRobot()
pygame.display.init()
pygame.joystick.init()
pygame.joystick.Joystick(0).init()


def disconnect_tool(pos_num):
    while True:
        pygame.event.pump()
        btn_y = pygame.joystick.Joystick(0).get_button(4)
        # btn_a = pygame.joystick.Joystick(0).get_button(0)
        if btn_y == 1:
            break
    X = 0
    Y = 0
    H = 0
    V = 0
    pos = RigidTransform()
    pos.from_frame = 'robot'

    h0 = 0.1453
    h1 = 0.097

    x0 = 0.394  # y = -0.4303
    x1 = 0.4967  # y = -0.4324
    x2 = 0.5533  # y = -0.4332
    x3 = x2
    x4 = 0.4949  # y = -0.4353
    x5 = 0.394

    y = -0.4365

    rot0 = 180
    rot1 = 155

    v_very_slow = 50
    v_slow = 100
    v = 200

    if pos_num == 0:
        X, Y, H, ROT, V = x5, y, h1, rot1, v
    elif pos_num == 1:
        X, Y, H, ROT, V = x4, y, h1, rot1, v_very_slow
    elif pos_num == 2:
        X, Y, H, ROT, V = x3, y, h1, rot1, v_very_slow
    elif pos_num == 3:
        X, Y, H, ROT, V = x2, y, h0, rot1, v_slow
    elif pos_num == 4:
        X, Y, H, ROT, V = x1, y, h0, rot1, v_slow
    elif pos_num == 5:
        X, Y, H, ROT, V = x0, y, h0, rot1, v

    pos.translation = X, Y, H
    quat = tf.transformations.quaternion_from_euler(math.radians(ROT), math.radians(0), math.radians(180))
    pos.quaternion[0:3] = quat[0:3]
    pos.rotation = RigidTransform.rotation_from_quaternion(quat)
    yumi.set_v(V)
    yumi.right.goto_pose(pos)
    sleep(.3)


def connect_tool(pos_num):
    while True:
        pygame.event.pump()
        btn_y = pygame.joystick.Joystick(0).get_button(4)
        # btn_a = pygame.joystick.Joystick(0).get_button(0)
        if btn_y == 1:
            break
            # connect_tool(pos_num)
            # pos_num = pos_num + 1
        # if pos_num == 6:
        #     pos_num = 0
        # if btn_a == 1:
        #     break

    X = 0
    Y = 0
    H = 0
    V = 0
    pos = RigidTransform()
    pos.from_frame = 'robot'

    h0 = 0.1453
    h1 = 0.095

    x0 = 0.394  # y = -0.4303
    x1 = 0.4967  # y = -0.4324
    x2 = 0.5533  # y = -0.4332
    x3 = x2
    x4 = 0.4949  # y = -0.4353
    x5 = 0.394

    y = -0.4365

    rot0 = 180
    rot1 = 155

    v_very_slow = 50
    v_slow = 100
    v = 200

    if pos_num == 0:
        X, Y, H, ROT, V = x0, y, h0, rot0, v
    elif pos_num == 1:
        X, Y, H, ROT, V = x1, y, h0, rot0, v_slow
    elif pos_num == 2:
        X, Y, H, ROT, V = x2, y, h0, rot1, v_very_slow
    elif pos_num == 3:
        X, Y, H, ROT, V = x3, y, h1, rot1, v_slow
    elif pos_num == 4:
        X, Y, H, ROT, V = x4, y, h1, rot1, v_slow
    elif pos_num == 5:
        X, Y, H, ROT, V = x5, y, h1, rot1, v

    pos.translation = X, Y, H
    quat = tf.transformations.quaternion_from_euler(math.radians(ROT), math.radians(0), math.radians(180))
    pos.quaternion[0:3] = quat[0:3]
    pos.rotation = RigidTransform.rotation_from_quaternion(quat)
    yumi.set_v(V)
    yumi.right.goto_pose(pos)
    sleep(.3)

def main():

    pos_num = 0
    while True:
        for i in range(0,5,1):
            connect_tool(i)

        for i in range(0, 5, 1):
            disconnect_tool(i)

    yumi.stop()

if __name__ == '__main__':
    main()
