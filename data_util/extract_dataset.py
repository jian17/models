from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import tensorflow as tf
import glob
import shutil

flags = tf.compat.v1.app.flags
flags.DEFINE_string('image_path','','Path to dataset')
flags.DEFINE_string('sorted_image_path','','Path to sorted images')
FLAGS = flags.FLAGS

def remove_unnecessary_files(image_path):
    regex = ['\**\*.csv', '\**\*depth.*']
    for r in regex:
        filelist = glob.glob(image_path + r, recursive=True)
        for filepath in filelist:
            if os.path.exists(filepath):
                os.remove(filepath)

def copy_files_to_destination(image_path, destination_path):
    i = 1
    gesture_labels = ['G' + str(i+1) for i in range(10)]
    for g in gesture_labels:
        filelist = glob.glob(image_path + '\**\{}\*.*'.format(g), recursive=True)
        for f in filelist:
            shutil.copy(f, destination_path + '\{}.jpg'.format(i))
            i+=1

def copy_file(image_path):

    r = '\**\G1\*.*'
    filelist = glob.glob(image_path + r, recursive=True)
    print(filelist)

def main(_):
    path = FLAGS.image_path
    remove_unnecessary_files(path)
    destination_path = path + '\images'
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    copy_files_to_destination(path, destination_path)

if __name__ == '__main__':
    tf.compat.v1.app.run()