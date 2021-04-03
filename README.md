# python-demo-android-test
Python学习：利用python及airtest测试框架、pytesseract图像识别控制手机

## main.py 当前功能：
1. 连接安卓手机
2. 打印手机应用列表
3. 获取设置屏幕信息
4. 打开设置应用
5. 通过图像识别找到设置应用中的搜索框
6. 在搜索框中输入 "USB"，搜索出USB相关设置
7. 通过图像识别在搜索结果中找到"验证应用"设置项的位置
8. 模拟点击事件进入7中找到的设置项
9. 切换该设置项的开关
10. [TODO]通过图像差异识别进行结果验证


## 相关资料：

### python语法手册
菜鸟教程：https://www.runoob.com/python3/python3-tutorial.html

### 测试框架: airtest
文档：https://airtest.readthedocs.io/en/latest/wiki/device/android_zh.html#id7

### 图像识别: pytesseract
GitHub: https://github.com/madmaze/pytesseract
    
    底层依赖 tesseract: brew install tesseract

### 行为树: py-trees
文档： https://py-trees.readthedocs.io/en/devel/index.html

GitHub: https://github.com/splintered-reality/py_trees


