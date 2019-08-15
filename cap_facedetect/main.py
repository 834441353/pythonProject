# coding=utf-8
import cv2
import time
import numpy as np
import tensorflow as tf
import detect_face


def to_rgb(img):
    w, h = img.shape
    ret = np.empty((w, h, 3), dtype=np.uint8)
    ret[:, :, 0] = ret[:, :, 1] = ret[:, :, 2] = img
    return ret


class MTCNN_Face():
    def __init__(self):
        try:
            tf.Graph().as_default()
            gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.5)
            sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
            try:
                sess.as_default()
                self.pnet, self.rnet, self.onet = detect_face.create_mtcnn(sess, None)
            except:
                pass
        except:
            pass
        self.minsize = 20  # minimum size of face
        self.threshold = [0.6, 0.6, 0.7]  # three steps's threshold
        self.factor = 0.709  # scale factor
        self.bb = np.zeros(4, dtype=np.int32)
        self.eye_bb = np.zeros(10, dtype=np.int32)
        self.shapebb = np.zeros(136, dtype=np.int32)

    def detectFeature(self, img):
        if img is None:
            return None
        else:
            if img.ndim == 2:
                img = to_rgb(img)
            img = img[:, :, 0:3]

            bounding_boxes, points = detect_face.detect_face(img, self.minsize, self.pnet, self.rnet, self.onet,
                                                             self.threshold, self.factor)
            # 检测到人脸的个数
            nrof_faces = bounding_boxes.shape[0]
            # print(bounding_boxes)
            for i in range(nrof_faces):

                det = bounding_boxes[i, :]
                if float(det[4]) >= float(0.95):
                    det = bounding_boxes[i]

                    # spoint = points[:, i]
                    # print(points, '---', spoint)

                    # cv2.putText(img, str(np.round(det[4], 2)), (int(det[0]), int(det[1])), cv2.FONT_HERSHEY_TRIPLEX,
                    #             1, color=(255, 0, 255))
                    cv2.rectangle(img, (int(det[0]), int(det[1])), (int(det[2]), int(det[3])), (0, 0, 255))
                    # for kk in range(5):
                    #     cv2.circle(img, (spoint[kk], spoint[kk + 5]), 2, (0, 255, 255), -1)
                    #     cv2.putText(img, "%d" % (kk), (spoint[kk], spoint[kk + 5]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5,(255, 255, 0))
            return img


if __name__ == '__main__':
    cv2.namedWindow("camera", 1)

    # video = "http://admin:admin@192.168.3.6:8081/"
    # http: // [fe80::fc8c: c9ff:fee3: 4c1f]:8081

    video = "http://admin:admin@[fe80::8f3:c17b:aa74:556a]:8081"
    capture = cv2.VideoCapture(video)

    print(capture)
    mtf = MTCNN_Face()

    num = 0
    while True:
        success, img = capture.read()
        img = mtf.detectFeature(img)
        cv2.imshow("camera", img)

        key = cv2.waitKey(10)

        if key == 27:
            # esc键退出
            print("esc break...")
            break
        if key == ord(' '):
            # 保存一张图像
            num = num + 1
            filename = "frames_%s.jpg" % num
            cv2.imwrite(filename, img)

    capture.release()
    cv2.destroyWindow("camera")
