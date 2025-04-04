import math
import logging

logging.disable(logging.DEBUG)
logging.disable(logging.WARNING)

from paddleocr import PaddleOCR as OCR

_paddleOcr = OCR(use_angle_cls=True, lang="ch")


class Rect():
    """
        此类用于 ocr 识别
        在这里定义的变量会成为 类 级别变量. 若要定义 类实例 级别的变量，需要在 __init__里. 且变量名前需要 双下划线
    """
    def __init__(self, x1, y1, x2, y2):
        # 左上角(第1个顶点)， 右下角(第2个顶点)
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    @property
    def x1(self):
        return self.__x1

    @property
    def y1(self):
        return self.__y1

    @property
    def x2(self):
        return self.__x2

    @property
    def y2(self):
        return self.__y2


class Intersect():

    def __init__(self):
        self.__cache = []

    def add_intersect(self, another):
        self.__cache.append(another)

    @property
    def has_intersect(self):
        return len(self.__cache) > 0

    @property
    def intersects(self):
        return self.__cache


class PaddleOCR_Text_Block(Rect, Intersect):

    def __init__(self, wordsBlock):
        """
            调用父类的初始化
            __init__(....)
            https://blog.csdn.net/LittleSeedling/article/details/122798938
        """
        self.__words = wordsBlock[1][0]
        points = wordsBlock[0]
        # 注意下面的2个方法的调用， 参考上面的连接
        super(PaddleOCR_Text_Block, self).__init__(points[0][0], points[0][1], points[2][0], points[2][1])
        super(Rect, self).__init__()

    def append(self, words):
        self.__words = self.__words + words

    @property
    def words(self):
        if self.has_intersect:
            for c in self.intersects:
                self.__words = self.__words + c.words
        return self.__words

    def __str__(self):
        return f'words: {self.__words}, x1={self.x1}, y1={self.y1}, x2={self.x2}, y2={self.y2}'


def get_min_line_height_and_min_y_and_lineCount(ocr_line):
    """
        取得最小行高 与 最小y值, 行数
    """
    min_line_height = 1000
    # 最小y值
    min_y = 1000
    max_y = 0
    # 1. 遍历所有的文字块， 取出最小的文本行高
    for wordsBlock in ocr_line:
        points = wordsBlock[0]
        h = points[2][1] - points[0][1]
        if h < min_line_height:
            min_line_height = h
        if min_y > points[0][1]:
            min_y = points[0][1]
        if max_y < points[3][1]:
            max_y = points[3][1]

    # print(f'min_words_height={min_line_height}, min_y={min_y}, max_y={max_y}')
    return min_line_height, min_y, math.ceil((max_y - min_y), min_line_height)


def ocr_line_to_array(ocr_line) -> list[PaddleOCR_Text_Block]:
    """
        将 ocr 结果的文字块 转换为 PaddleOCR_Text_Block 列表(数组)<br>
        list[PaddleOCR_Text_Block] 指定了存储的类型
    """
    result = []
    for block in ocr_line:
        result.append(PaddleOCR_Text_Block(block))
    return result


def is_intersect(rect1: Rect, rect2: Rect, vertical_space) -> bool:
    """
        判断 2 个矩形是否相交 <br>
        https://www.cnblogs.com/avril/archive/2013/04/01/2993875.html <br>
        vertical_space 行间距
    """
    x1 = max(rect1.x1, rect2.x1)
    y1 = max(rect1.y1, rect2.y1)

    x2 = min(rect1.x2, rect2.x2)
    y2 = min(rect1.y2, rect2.y2)

    ret = x1 <= x2 and (y1 <= y2 or y1 - vertical_space <= y2)
    return ret


def re_pack(blocks: list[PaddleOCR_Text_Block], vertical_space):
    """
        遍历 blocks, 找出有相交的矩形
    """
    if blocks is None or len(blocks) <= 1:
        return blocks

    copied = blocks.copy()
    removed = []
    ret = []

    # 逐个遍历原始的 blocks
    for block in blocks:
        if block in removed:
            continue

        # 将 block 与 复制项 逐个比较
        for c in copied:
            # 如果 不是同一个， 且， 有相交
            if block != c and is_intersect(block, c, vertical_space):
                # 把相交的取出
                block.add_intersect(c)

        copied.remove(block)
        # 如果有相交
        if block.has_intersect:
            for t in block.intersects:
                removed.append(t)
                copied.remove(t)
        # 保留 相交项
        ret.append(block)

    return ret


class PaddleOCR():
    def extract_from_single_text_block(self, np_array, vertical_space=5):
        """
            从单个文件块内识别文字
        """
        ocr_result = _paddleOcr.ocr(np_array, cls=True)
        if len(ocr_result) == 1 and ocr_result[0] is None:
            return False, None

        ocr_line = ocr_result[0]
        blocks = ocr_line_to_array(ocr_line)
        blocks.sort(key=lambda block: block.x1)
        blocks = re_pack(blocks, vertical_space)
        return True, blocks[0].words

    def extract_from_multi_text_block(self, np_array, vertical_space=5):
        """
            从多个文件块内识别文字
        """
        ocr_result = _paddleOcr.ocr(np_array, cls=True)
        # None 表示识别一个空白图像, 即: 图像中没有文字
        if len(ocr_result) == 1 and ocr_result[0] is None:
            return False, None

        ocr_line = ocr_result[0]
        # 将 ocr 结果的文字块 转换为对象
        blocks = ocr_line_to_array(ocr_line)
        # 按 x 坐标排序
        blocks.sort(key=lambda block: block.x1)
        # 查找相交项s
        blocks = re_pack(blocks, vertical_space)
        words = []
        for block in blocks:
            words.append(block.words)
        return True, words
