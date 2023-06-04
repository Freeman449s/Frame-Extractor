# MIT License
#
# Copyright (c) 2023 Freeman449s
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os, cv2 as cv


def error(message: str):
    print(message)
    input("按下[回车]退出")
    exit(0)


# 打印欢迎信息
print("(C) 2023, Gordon Freeman Tang")
print("License under the MIT license.")
print("欢迎使用视频帧提取器")

# 读取视频
filePath = input("视频路径：")
if not os.path.exists(filePath):
    error("错误：视频不存在")
fileName = filePath.split("/")[-1]
fileName = fileName.split("\\")[-1]
fileName = fileName.split(".")[0]  # 提取视频文件名
cap = cv.VideoCapture(filePath)

# 读取帧
frameNo = input("需要提取的帧序号（从1开始）：")
try:
    frameNo = int(frameNo)
except ValueError as e:
    error(f"错误：无法将\"{frameNo}\"转换为数字")
if frameNo > cap.get(cv.CAP_PROP_FRAME_COUNT) or frameNo < 1:
    error("错误：请求的帧序号超出范围")
frameNo -= 1
cap.set(cv.CAP_PROP_POS_FRAMES, frameNo)
success, frame = cap.read()
if not success:
    error("错误：读取帧时发生错误")

# 输出帧
imagePath = input("图像输出路径（默认命名为\"<视频文件名-帧序号>.bmp\"）：")
if len(imagePath) < 1:
    imagePath = fileName + "-" + str(frameNo + 1) + ".bmp"
cv.imwrite(imagePath, frame, [cv.IMWRITE_JPEG_QUALITY, 100])
cap.release()
input("提取成功，按下[回车]退出")
