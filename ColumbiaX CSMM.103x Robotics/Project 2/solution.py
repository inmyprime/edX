#!/usr/bin/env python  
import rospy

import numpy as np

import tf
import tf2_ros
import geometry_msgs.msg

def message_from_transform(T):
 	msg = geometry_msgs.msg.Transform()
 	q = tf.transformations.quaternion_from_matrix(T)
 	translation = tf.transformations.translation_from_matrix(T)
 	msg.translation.x = translation[0]
 	msg.translation.y = translation[1]
 	msg.translation.z = translation[2]
 	msg.rotation.x = q[0]
 	msg.rotation.y = q[1]
 	msg.rotation.z = q[2]
 	msg.rotation.w = q[3]
 	return msg

def publish_transforms():
 	# base -> object
    object_transform = geometry_msgs.msg.TransformStamped()
    object_transform.header.stamp = rospy.Time.now()
    object_transform.header.frame_id = "base_frame"
    object_transform.child_frame_id = "object_frame"
    
    T1 = tf.transformations.concatenate_matrices(tf.transformations.euler_matrix(0.79, 0.0, 0.79), tf.transformations.translation_matrix((0.0, 1.0, 1.0)))
    object_transform.transform = message_from_transform(T1)
    br.sendTransform(object_transform)

    # base -> robot
    robot_transform = geometry_msgs.msg.TransformStamped()
    robot_transform.header.stamp = rospy.Time.now()
    robot_transform.header.frame_id = "base_frame"
    robot_transform.child_frame_id = "robot_frame"
    
    T2 = tf.transformations.concatenate_matrices(tf.transformations.rotation_matrix(1.5, (0, 0, 1)), tf.transformations.translation_matrix((0.0, -1.0, 0.0)))
    robot_transform.transform = message_from_transform(T2)
    br.sendTransform(robot_transform)
 
 	# robot -> camera
    camera_transform = geometry_msgs.msg.TransformStamped()
    camera_transform.header.stamp = rospy.Time.now()
    camera_transform.header.frame_id = "robot_frame"
    camera_transform.child_frame_id = "camera_frame"
    
    
    T_rc = tf.transformations.translation_matrix((0.0, 0.1, 0.1))
    # Transformation matrix from camera to object
    T_co = np.dot(tf.transformations.inverse_matrix(np.dot(T2, T_rc)), T1)
    # Get the vector pointing from camera origin to object origin
    v_original = tf.transformations.translation_from_matrix(T_co)
    # Normalise it
    v = v_original / np.linalg.norm(v_original)
    # x axis
    x = [1,0,0]
    angle = np.arccos(np.dot(x, v))
    w = np.cross(x, v)
    T3 = tf.transformations.concatenate_matrices(T_rc, tf.transformations.rotation_matrix(angle, w))
    
    camera_transform.transform = message_from_transform(T3)
    br.sendTransform(camera_transform)

if __name__ == '__main__':
    rospy.init_node('project2_solution')

    br = tf2_ros.TransformBroadcaster()
    rospy.sleep(0.5)

    while not rospy.is_shutdown():
        publish_transforms()
        rospy.sleep(0.05)
