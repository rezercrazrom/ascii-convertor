import PIL
from PIL import Image


def image_to_ascii(image_path, output_width=180):
    img = Image.open(image_path)

    weight, height = img.size
    aspect_ratio = height / weight
    new_height = int(aspect_ratio * output_width * 0.55)
    img = img.resize((output_width, new_height))

    img = img.convert('L')

    chars = "█▓▒░ "

    pixels = img.get_flattened_data()

    ascii_array = ""
    for pixel in pixels:
        index = int((pixel / 255) * (len(chars) - 1))
        ascii_array += chars[index]

    ascii_img = ""
    for i in range(0, len(ascii_array), output_width):
        ascii_img += ascii_array[i:i+output_width] + "\n"

    return ascii_img



if __name__ == "__main__":
    result = image_to_ascii("")
    print(result)

    with open("ascii_art.txt", "w", encoding="utf-8") as f:
        f.write(result)