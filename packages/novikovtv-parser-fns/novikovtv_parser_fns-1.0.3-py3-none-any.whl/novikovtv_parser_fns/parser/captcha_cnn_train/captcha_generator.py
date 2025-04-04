import asyncio
import math
import os
import random
import time

import aiohttp
import cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from bs4 import BeautifulSoup, Tag

from novikovtv_parser_fns.parser.captcha.solver import CaptchaSolver

path_ = r"C:\Users\isupov\Desktop\train2"
OUTPUT_FOLDER = r"C:\Users\isupov\Desktop\extracted1"
counts = {}

for filename in os.listdir(OUTPUT_FOLDER):
    path_digit = os.path.join(OUTPUT_FOLDER, filename)
    last_elem = os.listdir(path_digit)[-1]
    counts[filename] = int(last_elem.split(".")[0])


def generate_captcha(i):
    # Размеры изображения
    width, height = 200, 100
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    color = (15, 86, 164)
    background_color = (222, 225, 230)

    sin_image = Image.new('RGBA', (width, height), color=(255, 255, 255))
    sin_draw = ImageDraw.Draw(sin_image)

    _amplitude = 3
    _period = 5
    for x in range(width * _period):
        for y in range(0, height, 5):
            f = int(y + _amplitude * math.sin(x / _period))
            sin_draw.point((x, f), fill=background_color)
            sin_draw.point((x, f + 1), fill=background_color)
    sin_image = sin_image.filter(ImageFilter.GaussianBlur(radius=1))
    image.paste(sin_image, (0, 0), sin_image)

    for _ in range(random.randint(10, 15)):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        if random.choice([True, False]):
            draw.line((x1, y1, x2, y1), fill=color)
        else:
            draw.line((x1, y1, x1, y2), fill=color)

    try:
        font = ImageFont.truetype("arial.ttf", 55)
    except IOError:
        font = ImageFont.load_default()

    numbers = [str(random.randint(0, 9)) for _ in range(6)]
    captcha_text = ''.join(numbers)

    x_offset = 0
    for num in numbers:
        num_image = Image.new('RGBA', (60, 60), (255, 255, 255, 0))
        num_draw = ImageDraw.Draw(num_image)

        for dx in range(-2, 1):
            for dy in range(-2, 1):
                num_draw.text((dx, dy), num, font=font, fill=color)

        angle = random.randint(-20, 20)
        rotated_num = num_image.rotate(angle, expand=1)

        y_offset = random.randint(-15, 15) + 10
        image.paste(rotated_num, (x_offset, y_offset), rotated_num)
        x_offset += 30

    print(i, captcha_text)
    yield image, captcha_text


async def main():
    captcha_url = "https://pb.nalog.ru/captcha-dialog.html"
    index = 0
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(captcha_url) as resp:
                    html_text = await resp.text()

                    soup = BeautifulSoup(html_text, 'html.parser')
                    captcha: Tag = soup.find('img')
                    if captcha is None:
                        print("captcha not found")
                        continue

                    captcha_token: str = captcha['src'].split('&')[0].replace('/static/captcha.bin?a=', '')

            if not captcha_token:
                continue

            captcha_res: str = ""
            async with aiohttp.ClientSession() as session:
                async with session.get("https://pb.nalog.ru" + captcha['src']) as resp:
                    captcha_img = await resp.read()
                    # with open(f'kapcha.png', 'wb') as img:
                    #     img.write(captcha_img)
                    captcha_solver = CaptchaSolver(captcha_img)
                    captcha_res = captcha_solver.solve()
            print(captcha_res, end=" ")
            if not captcha_res:
                continue

            index += 1

            async with aiohttp.ClientSession() as session:
                async with session.post("https://pb.nalog.ru/captcha-proc.json", params={
                    'captcha': captcha_res,
                    "captchaToken": captcha_token,
                }) as resp:
                    if not resp.ok:
                        print("captcha not found")
                        continue

                    print(await resp.json())

                    cv2.imwrite(os.path.join(r"C:\Users\isupov\Desktop\train2",
                                             f"{captcha_res}_{round(time.time())}.jpg"), captcha_solver.image)
                    # for letter_text, letter_image in zip(list(captcha_res), captcha_solver.letter_images):
                    #     save_path = os.path.join(OUTPUT_FOLDER, letter_text)
                    #     if not os.path.exists(save_path):
                    #         os.makedirs(save_path)
                    #
                    #     count = counts.get(letter_text, 1)
                    #     p = os.path.join(save_path, "{}.jpg".format(str(count).zfill(6)))
                    #     counts[letter_text] = count + 1
                    #     cv2.imwrite(p, letter_image)
        except Exception as e:
            print(e)
            continue


if __name__ == '__main__':
    asyncio.run(main())
    # pass
    # [[image.save(os.path.join(path_, f"{text}_{time.time()}.jpg")) for image, text in generate_captcha(i)]
    #  for i in range(50000)]
