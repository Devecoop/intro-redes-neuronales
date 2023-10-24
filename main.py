from PIL import Image, ImageDraw
import random
import os

from tensorflow import square

IMAGE_SIDE_SIZE = 38
NUM_IMAGES = 1000


def generate_image(size, square_size, position_x, position_y):
    """Generar imagen de un cuadro negro en un fondo blanco."""
    image = Image.new('L', size, color='white')
    draw = ImageDraw.Draw(image)
    
    x_min = position_x
    x_max = position_x + square_size
    y_min = position_y
    y_max = y_min + square_size
    
    draw.rectangle([x_min, y_min, x_max, y_max], fill='black')
    return image

def create_path(path_to_create):
    if not os.path.exists(path_to_create):
        os.mkdir(path_to_create)

def main():
    output_dir = "generated_images"
    left_dir = "left"
    right_dir = "right"
    left_dir_path = os.path.join(output_dir, left_dir)
    right_dir_path = os.path.join(output_dir, right_dir)

    create_path(output_dir)
    create_path(left_dir_path)
    create_path(right_dir_path)


    size = (IMAGE_SIDE_SIZE, IMAGE_SIDE_SIZE)
    left_images = right_images = NUM_IMAGES // 2

    for square_size in range(1,11):
        for i in range(left_images//10):
            position_x = random.randint(0, (IMAGE_SIDE_SIZE//2) - 1 - square_size)  # Generar posición para X del lado izquierdo
            position_y = random.randint(0, IMAGE_SIDE_SIZE - 1 - square_size)  # Generar posición Y
            image = generate_image(size, square_size, position_x, position_y)
            image.save(os.path.join(left_dir_path, f"{square_size}_{i + 1}.png"))

    for square_size in range(1,11):
        for i in range(right_images//10):
            position_x = random.randint(19, IMAGE_SIDE_SIZE - 1 - square_size)  # Generar posición X del lado derecho
            position_y = random.randint(0, IMAGE_SIDE_SIZE - 1  - square_size)  # Generar posición Y
            image = generate_image(size, square_size, position_x, position_y)
            image.save(os.path.join(right_dir_path, f"{square_size}_{i + 1}.png"))

if __name__ == "__main__":
    main()
