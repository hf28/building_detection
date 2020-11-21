#!/usr/bin/env python

import rosbag
from cv_bridge import CvBridge
from nav_msgs.msg import Odometry
import pandas as pd
import csv
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()
print(args.file)


xs = []
ys = []
zs = []
odom_cnt = 0

bagFile = args.file
bag = rosbag.Bag(bagFile)

for topic, msg, t in bag.read_messages(topics=['/gazebo/model_states']):

   if topic == '/gazebo/model_states':
       odom_cnt += 1
       # print("odom: ", odom_cnt)
       # print('---------------------------------------------')
       # print(msg.pose[9].position.x)
       xs.append(msg.pose[9].position.x)
       ys.append(msg.pose[9].position.y)
       zs.append(msg.pose[9].position.z)


# print(bagFile[:-4]+'_x')
#
xName = 'bagfile_'+bagFile[:-4]+'_x'
yName = 'bagfile_'+bagFile[:-4]+'_y'
zName = 'bagfile_'+bagFile[:-4]+'_z'


dict = {xName: xs, yName: ys, zName: zs}
#
df = pd.DataFrame(dict)
#
# # saving the dataframe
fileName = 'position_'+bagFile[:-4]+'.csv'

df.to_csv(fileName)
