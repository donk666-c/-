# 图片左右翻转处理

这是一个 Python 示例项目，用于接收一张图片并输出左右翻转后的图片。

## 功能说明

- 输入：一张图片
- 输出：左右翻转后的图片
- 额外展示：同时在屏幕中显示原图和翻转后图像

## 代码文件

- [image_flip.py](image_flip.py)：包含 `flip_left_right` 和展示函数
- [test_image_flip.py](test_image_flip.py)：单元测试，用于验证左右翻转逻辑
- [requirements.txt](requirements.txt)：依赖库清单

## 使用方式

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 运行示例：
   ```bash
   python image_flip.py
   ```
3. 也可以直接调用函数：
   ```python
   from PIL import Image
   from image_flip import flip_left_right

   img = Image.open("input.jpg")
   flipped = flip_left_right(img)
   flipped.save("output.jpg")
   ```

## 说明

`flip_left_right` 使用 PIL 的 `Image.FLIP_LEFT_RIGHT` 进行水平镜像处理，生成左右翻转后的图片，同时通过 `matplotlib` 展示原图和翻转图，便于对比。
