from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap
from cleantext import clean

def multiline_text_with_custom_line_height(draw, position, text, font, fill, line_height):
    lines = text.splitlines()
    y = position[1]

    for line in lines:
        line = clean(line, no_emoji=True, lower=False, to_ascii=False)
        wrapped_line = textwrap.fill(line, width=55)
        draw.text((position[0], y), wrapped_line, font=font, fill=fill)
        y += line_height

def create_tweet(name, username, content, file_name):
    # Create a blank image with a resolution of 1024x1024
    img = Image.new('RGB', (1024, 1024), color='#010101')

    # Get the ImageDraw object
    draw = ImageDraw.Draw(img)

    # Font for the name and username
    font_name_username = ImageFont.truetype("arial.ttf", 24)
    font_content = ImageFont.truetype("arial.ttf", 28)

    rectangle_size = (800, 400)  # Width x Height
    rectangle_pos = ((1024 - rectangle_size[0]) // 2, (1024 - rectangle_size[1]) // 2)

    # Draw a rectangle in the center
    width, height = 300, 200
    rect_coords = [(10, 10), (width - 10, height - 10)]
    border_radius = 16

    # Optional: Draw a rounded rectangle
    #draw.rounded_rectangle([rectangle_pos, (rectangle_pos[0] + rectangle_size[0], rectangle_pos[1] + rectangle_size[1])], fill="#0a0a0a", radius=border_radius, outline="#282828", width=2)

    # Load the image and resize if necessary
    image_path = "l.png"  # Adjust the path to your image
    image = Image.open(image_path)
    image = image.resize((80, 80))  # Adjust the size as needed

    # Create a mask to make the image circular
    mask = Image.new("L", image.size, 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, image.width, image.height), fill=255)

    # Paste the image onto the mask
    image = Image.composite(image, Image.new("RGB", image.size, 0), mask)

    # Paste the image to the left of the name within the rectangle
    img.paste(image, (rectangle_pos[0] + 30, rectangle_pos[1] + 30), mask)

    name_pos = (rectangle_pos[0] + 130, rectangle_pos[1] + 40)
    username_pos = (rectangle_pos[0] + 130, rectangle_pos[1] + 70)

    # Set the position and size of the content rectangle
    content_rect_pos = (rectangle_pos[0] + 40, rectangle_pos[1] + 140)

    # Draw name and username
    draw.text(name_pos, name, font=font_name_username, fill='#f0f0f0', stroke_width=1)
    draw.text(username_pos, f"@{username}", font=font_name_username, fill='#f0f0f0')

    # Create an ImageDraw object for the tweet content
    draw_content = ImageDraw.Draw(img)

    # Draw the tweet content with wrap and custom line height
    multiline_text_with_custom_line_height(draw_content, content_rect_pos, content, font=font_content, fill='#fff', line_height=40)

    # Save the image as a PNG file
    img.save(file_name, format='PNG')

# Example usage
tweet_name = "John Doe"
tweet_username = "johndoe123"
tweet_content = "Hey students! 📚 Twitter rocks for marketing! 🚀\nIt's where brands create buzz. 🐝\nConnects with customers & spreads word fast. 💬📢\nPerfect for promos & updates. 🔥\n#MarketingMagic #BrandBuzz #TwitterPower ✨"

create_tweet(tweet_name, tweet_username, tweet_content, "tweet.png")
