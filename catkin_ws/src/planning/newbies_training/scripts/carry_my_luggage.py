#!/usr/bin/env python3
import rospy
import rospkg
import time
from juskeshino_tools.JuskeshinoNavigation import JuskeshinoNavigation
from juskeshino_tools.JuskeshinoVision import JuskeshinoVision
from juskeshino_tools.JuskeshinoHardware import JuskeshinoHardware
from juskeshino_tools.JuskeshinoSimpleTasks import JuskeshinoSimpleTasks
from juskeshino_tools.JuskeshinoHRI import JuskeshinoHRI
from juskeshino_tools.JuskeshinoManipulation import JuskeshinoManipulation
from juskeshino_tools.JuskeshinoKnowledge import JuskeshinoKnowledge
from std_msgs.msg import Bool, Float32
from vision_msgs.msg import HumanCoordinatesArray

def get_by_name(data, goal):
    for human in data.coordinates_array:
        counter = 0
        names = []
        for kpoint in human.keypoints_array:
            names.append(kpoint.keypoint_name)
            if kpoint.keypoint_name == goal:
                return [
                        kpoint.keypoint_coordinates.position.x,
                        kpoint.keypoint_coordinates.position.y,
                        kpoint.keypoint_coordinates.position.z
                ]
            counter += 1
    print("Error, goal doesnt exist, these're the possible names:")
    for name in names:
        print(name)
    return [None, None, None]

def human_callback(data):
    r_elb = get_by_name(data, "r_elb")
    r_sho = get_by_name(data, "r_sho")
    r_wri = get_by_name(data, "r_wri")
    r_hip = get_by_name(data, "r_hip")
    l_elb = get_by_name(data, "l_elb")
    l_sho = get_by_name(data, "l_sho")
    l_wri = get_by_name(data, "l_wri")
    l_hip = get_by_name(data, "l_hip")
    neck = get_by_name(data, "neck")
    x_mean = (neck[2] + r_hip[2] + l_hip[2]) / 3
    delta_r = r_wri[0] - x_mean
    delta_l = l_wri[0] - x_mean
    print(x_mean)
    if delta_r > delta_l:
        print("Right wrist's farest")
    elif delta_l > delta_r:
        print("Left wrist's farest")
    else:
        print("IDK")
    """
    print(
            [
                r_elb,
                r_sho,
                r_wri,
                r_hip,
                l_elb,
                l_sho,
                l_wri,
                l_hip,
                neck
                ]
            )
    """

def main():
    rospy.init_node("carry_my_luggage")
    rate = rospy.Rate(10)
    rospack = rospkg.RosPack()
    JuskeshinoNavigation.setNodeHandle()
    JuskeshinoVision.setNodeHandle()
    JuskeshinoHardware.setNodeHandle()
    JuskeshinoSimpleTasks.setNodeHandle()
    JuskeshinoHRI.setNodeHandle()
    JuskeshinoManipulation.setNodeHandle()
    JuskeshinoKnowledge.setNodeHandle()
    rospy.Subscriber("/vision/human_pose/human_pose_array", HumanCoordinatesArray, human_callback)
    rospy.spin()

if __name__ == "__main__":
    main()