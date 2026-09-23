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
2. 运行示例（自动生成一个示例图并显示）：
   ```bash
   python image_flip.py
   ```
3. 处理指定图片：
   ```bash
   python image_flip.py input.jpg -o output.jpg
   ```
4. 批量处理整个文件夹：
   ```bash
   python image_flip.py images_folder -o flipped_images
   ```
   说明：程序会读取 `images_folder` 中所有支持的图片文件，并保存到 `flipped_images` 文件夹中，文件名会自动加上 `_flipped` 后缀。
5. 也可以直接调用函数：
   ```python
   from PIL import Image
   from image_flip import flip_left_right, show_original_and_flipped, process_batch

   img = Image.open("input.jpg")
   flipped = flip_left_right(img)
   flipped.save("output.jpg")

   # 在屏幕中显示原始图和翻转后图
   show_original_and_flipped(img, output_path="output.jpg")

   # 批量处理一整个目录
   process_batch("images_folder", "flipped_images")
   ```

## 说明

`flip_left_right` 使用 PIL 的 `Image.FLIP_LEFT_RIGHT` 进行水平镜像处理，生成左右翻转后的图片。`show_original_and_flipped` 会把原图和翻转后图并排展示；如果当前环境没有图形界面，则会自动保存一张对比图，确保功能仍可用。`process_batch` 则允许批量处理一个目录中的多张图片。
