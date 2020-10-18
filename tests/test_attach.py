# @Time : 2020/10/18 0:29 
# @Author : yangyan
# @File : test_attach.py 
# @Software: PyCharm
import allure


def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)
    pass


def test_attach_html():
    allure.attach("<body>这是一个html</body>", "HTML测试", attachment_type=allure.attachment_type.HTML)
    pass


def test_attach_photo():
    allure.attach.file("D:\workspace\工作笔记\工作笔记\唯品会笔记\image\image-20201018002802585.png", "这是一个图片",
                       attachment_type=allure.attachment_type.PNG)
    pass

# def test_attach_video():
#     allure.attach.file("D:\workspace\工作笔记\工作笔记\唯品会笔记\image\image-20201018002802585", "这是一个视频",
#                        attachment_type=allure.attachment_type.MP4)
#     pass
