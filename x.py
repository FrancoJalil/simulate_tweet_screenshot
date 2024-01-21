from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap
from cleantext import clean


def multiline_text_with_custom_line_height(draw, position, text, font, fill, line_height):
    lines = text.splitlines()
    y = position[1]

    for line in lines:
        
        line = clean(line, no_emoji=True, lower=False, to_ascii=False)
        wrapped_line = textwrap.fill(line, width=55)  # Ajusta el ancho según sea necesario
      
        draw.text((position[0], y), wrapped_line, font=font, fill=fill)
        y += line_height



def crear_tweet(nombre, usuario, contenido, nombre_archivo):
    # Crear una imagen en blanco con resolución de 1024x1024
    img = Image.new('RGB', (1024, 1024), color='#010101')

    # Obtener el objeto ImageDraw
    draw = ImageDraw.Draw(img)

    # Fuente para el nombre y el usuario
    font_nombre_usuario = ImageFont.truetype("arial.ttf", 24)
    font_contenido = ImageFont.truetype("arial.ttf", 28)

    rectangulo_size = (800, 400)  # Ancho x Alto
    rectangulo_pos = ((1024 - rectangulo_size[0]) // 2, (1024 - rectangulo_size[1]) // 2)

    # Dibujar rectángulo en el centro
    width, height = 300, 200
    rect_coords = [(10, 10), (width - 10, height - 10)]
    border_radius = 16
    #draw.rounded_rectangle([rectangulo_pos,  (rectangulo_pos[0] + rectangulo_size[0], rectangulo_pos[1] + rectangulo_size[1])], fill="#0a0a0a", radius=border_radius, outline="#282828",width=2)



    # Cargar la imagen y ajustar su tamaño si es necesario
    imagen_path = "l.png"  # Ajusta la ruta a tu imagen
    imagen = Image.open(imagen_path)
    imagen = imagen.resize((80, 80))  # Ajusta el tamaño según sea necesario

    # Crear una máscara para hacer la imagen circular
    mascara = Image.new("L", imagen.size, 0)
    draw_mascara = ImageDraw.Draw(mascara)
    draw_mascara.ellipse((0, 0, imagen.width, imagen.height), fill=255)

    # Pegar la imagen en la máscara
    imagen = Image.composite(imagen, Image.new("RGB", imagen.size, 0), mascara)

    # Pegar la imagen a la izquierda del nombre dentro del rectángulo
    img.paste(imagen, (rectangulo_pos[0] + 30, rectangulo_pos[1] + 30), mascara)

  

    nombre_pos = (rectangulo_pos[0] + 130, rectangulo_pos[1] + 40)
    usuario_pos = (rectangulo_pos[0] + 130, rectangulo_pos[1] + 70)
    
    # Establecer la posición y tamaño del rectángulo del contenido
    contenido_rect_pos = (rectangulo_pos[0] + 40, rectangulo_pos[1] + 140)

    # Dibujar nombre y usuario
    draw.text(nombre_pos, nombre, font=font_nombre_usuario, fill='#f0f0f0', stroke_width=1)
    draw.text(usuario_pos, f"@{usuario}", font=font_nombre_usuario, fill='#f0f0f0')

    # Crear un objeto ImageDraw para el contenido del tweet
    draw_contenido = ImageDraw.Draw(img)

    # Aplicar wrap al contenido del tweet
    contenido_wrapped = textwrap.fill(contenido, width=55)  # Ajusta el ancho según sea necesario

    # Dibujar el contenido del tweet con wrap y line_height personalizado
    multiline_text_with_custom_line_height(draw_contenido, contenido_rect_pos, contenido_tweet, font=font_contenido, fill='#fff', line_height=40)



    
    # Guardar la imagen como un archivo PNG
    img.save(nombre_archivo, format='PNG')

# Ejemplo de uso
nombre_tweet = "John Doe"
usuario_tweet = "johndoe123"
contenido_tweet = "Hey students! 📚 Twitter rocks for marketing! 🚀\nIt's where brands create buzz. 🐝\nConnects with customers & spreads word fast. 💬📢\nPerfect for promos & updates. 🔥\n#MarketingMagic #BrandBuzz #TwitterPower ✨"

crear_tweet(nombre_tweet, usuario_tweet, contenido_tweet, "tweet.png")
