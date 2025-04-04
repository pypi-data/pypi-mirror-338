from appAuto.common.singleton import global_singleton_class
import cv2
import os


@global_singleton_class
class ImgCache:

    def __init__(self):
        self.__cache = {}

    def getImg(self, image_file: str):
        """
        获取图片
        """
        assert image_file is not None, '图像文件路径不能为空'
        assert os.path.exists(image_file), '文件 "%s" 不存在' % image_file
        image_file = image_file.lower()
        if image_file in self.__cache:
            return self.__cache[image_file]

        img = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
        self.__cache[image_file] = img
        return img


# 在模块加载时就创建一个实例
imgCache = ImgCache()
