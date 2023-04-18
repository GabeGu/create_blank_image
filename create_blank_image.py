from PIL import Image

# name: value, min_value, max_value
values_rangs = {
    'width': (0, 1, 4096),
    'height': (0, 1, 4096),
    'red': (0, 0, 255),
    'green': (0, 0, 255),
    'blue': (0, 0, 255)
}

# 整数值参数输入交互，直到获取正确的值
for value_name, (value, min_value, max_value) in values_rangs.items():
    while True: 
        value = int(input(f"请指定图片的{value_name}值({min_value}~{max_value}): "))
        values_rangs[value_name] = (value, min_value, max_value)
        if min_value <= value <= max_value:
            break;
        else:
            print(f"输入的{value_name}值{value}不在{min_value}~{max_value}内，请重新输入！")

width = values_rangs['width'][0]
height = values_rangs['height'][0]
red = values_rangs['red'][0]
green = values_rangs['green'][0]
blue = values_rangs['blue'][0]

values_rangs[value_name][0];
# Create a blank image with the specified dimensions and color
image = Image.new('RGB', (width, height), (red, green, blue))

# use the f-string
filename = f"blank_image_{width}_{height}_[{red},{green},{blue}].png"

# save the image as a PNG file
image.save(filename)
(f"图片已保存为：{filename}")
