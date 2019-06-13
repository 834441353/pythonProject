# -*- coding: UTF-8 -*-
import os
import tensorflow as tf
import numpy as np
import cv2
import detect_face
import dlib


def to_rgb(img):
    w, h = img.shape
    ret = np.empty((w, h, 3), dtype=np.uint8)
    ret[:, :, 0] = ret[:, :, 1] = ret[:, :, 2] = img
    return ret


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.144])


class MtcnnDlib():
    predictor_path = "./modleData/shape_predictor_68_face_landmarks.dat"

    def __init__(self):

        try:
            tf.Graph().as_default()
            gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.5)  # args.gpu_memory_fraction
            sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
            try:
                sess.as_default()
                self.pnet, self.rnet, self.onet = detect_face.create_mtcnn(sess, None)
            except:
                pass
        except:
            pass
        self.detector = dlib.get_frontal_face_detector()

        self.landmark_predictor = dlib.shape_predictor(MtcnnDlib.predictor_path)

        self.minsize = 20  # minimum size of face
        self.threshold = [0.6, 0.6, 0.7]  # three steps's threshold
        self.factor = 0.709  # scale factor
        self.bb = np.zeros(4, dtype=np.int32)
        self.eye_bb = np.zeros(10, dtype=np.int32)
        self.shapebb = np.zeros(136, dtype=np.int32)
        # self.shape

    def detectFeature(self, path):

        if os.path.isfile(path):  # and '0_Light' in image_path:
            print(path)
            img = cv2.imread(path, cv2.IMREAD_COLOR)  # cv2.IMREAD_GRAYSCALE  cv2.IMREAD_COLOR

            if img is None:
                return None, None
            else:
                imgcopy = img.copy()
                if img.ndim < 2:
                    # MtcnnDlib.text_file.write('erro %s\n' % (self.image_path))   ####
                    return img, imgcopy
                if img.ndim == 2:
                    img = to_rgb(img)
                img = img[:, :, 0:3]
                # pdb.set_trace()
                bounding_boxes, points = detect_face.detect_face(img, self.minsize, self.pnet, self.rnet, self.onet,
                                                                 self.threshold, self.factor)
                # nrof_faces = bounding_boxes.shape[0]
                # for i in range(nrof_faces):
                #     spoint = points[:, i]
                #     for kk in range(2):
                #         cv2.circle(img, (spoint[kk], spoint[kk + 5]), 2, (0, 255, 255), -1)

                return imgcopy, points

                # return 1
        else:
            return None
