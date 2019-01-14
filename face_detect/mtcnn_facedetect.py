import os
import detect_face
import numpy as np
import cv2
import tensorflow as tf
import time

img_path = './pic/'
img_save_path = './img_face/'
txt_save_path = './txt/'

showPic = 0


def to_rgb(img):
    w, h = img.shape
    ret = np.empty((w, h, 3), dtype=np.uint8)
    ret[:, :, 0] = ret[:, :, 1] = ret[:, :, 2] = img
    return ret


class Mtcnn_faced():
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
        self.minsize = 20  # minimum size of face
        self.threshold = [0.6, 0.6, 0.7]  # three steps's threshold
        self.factor = 0.709  # scale factor
        self.bb = np.zeros(4, dtype=np.int32)
        self.eye_bb = np.zeros(10, dtype=np.int32)
        self.shapebb = np.zeros(136, dtype=np.int32)

    def detectFeature(self, path):
        if os.path.isfile(path):  # and '0_Light' in image_path

            name = path.split('/')[2].split('.')[0]
            # print(name)
            img = cv2.imread(path, cv2.IMREAD_COLOR)  # cv2.IMREAD_GRAYSCALE  cv2.IMREAD_COLOR

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
                        imgN, det = self.tailor(img, det)

                        filename = img_save_path + name + '_' + str(i) + '.jpg'
                        self.saveImg(filename, imgN)
                        self.writeTxt(filename, det)

                        # spoint = points[:, i]
                        # print(points, '---', spoint)

                        # cv2.putText(img, str(np.round(det[4], 2)), (int(det[0]), int(det[1])), cv2.FONT_HERSHEY_TRIPLEX,
                        #             1, color=(255, 0, 255))
                        # cv2.rectangle(img, (int(det[0]), int(det[1])), (int(det[2]), int(det[3])), (0, 0, 255))
                        # for kk in range(5):
                        #     cv2.circle(img, (spoint[kk], spoint[kk + 5]), 2, (0, 255, 255), -1)
                        #     cv2.putText(img, "%d" % (kk), (spoint[kk], spoint[kk + 5]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5,(255, 255, 0))
                return img

        else:
            return None

    def tailor(self, img, rect):
        left = rect[0]
        top = rect[1]
        right = rect[2]
        bottom = rect[3]
        fw = (right - left) / 2
        fh = (bottom - top) / 2
        leftN = left - fw
        rect[0] = fw
        if leftN < 0:
            leftN = 0
            rect[0] = left
        rightN = right + fw
        topN = top - fh
        rect[1] = fh
        if topN < 0:
            topN = 0
            rect[1] = top
        bottomN = bottom + fh
        imgN = img[int(topN):int(bottomN), int(leftN):int(rightN)]
        rect[2] = 3 * fw
        rect[3] = 3 * fh
        if showPic == 1:
            cv2.imshow('mtcnn imgN', imgN)
            cv2.waitKey(0)
        return imgN, rect

    def saveImg(self, filename, img):
        if img is not None:
            if not os.path.exists(img_save_path):
                os.makedirs(img_save_path)
            cv2.imwrite(filename, img)
            return 1
        else:
            return 0

    def writeTxt(self, imgpath, rect):
        try:
            if not os.path.exists(txt_save_path):
                os.makedirs(txt_save_path)
            filename = txt_save_path + 'face_rect.txt'
            f = open(filename, 'a')
            info = imgpath + '  ' + str(rect[0]) + ' ' + str(rect[1]) + ' ' + str(rect[2]) + ' ' + str(rect[3])
            f.write(str(info) + '\n')
            f.close()
        except Exception as e:
            print("Error:没有找到文件或读取文件失败！！%s" % e)
            return 0
        else:
            return 1


if __name__ == '__main__':
    tface = Mtcnn_faced()
    file_name = os.listdir(img_path)
    file_list = [os.path.join(img_path, file) for file in file_name]
    print(file_list)
    for i in file_list:
        time1 = time.time()
        img = tface.detectFeature(i)
        time2 = time.time()
        print('耗时: %f'%(time2-time1))
        # if img is not None:
        #     cv2.imshow('mtcnn img', img)
        #     cv2.waitKey(0)

    del tface
