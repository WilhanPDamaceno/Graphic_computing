from PIL import Image
import math

def manipulate_image(image_path):
    img = Image.open(image_path)
    width, height = img.size

    # 1. Escala (reduzida em 30%)
    new_width_scaled = int(width * 0.7)
    new_height_scaled = int(height * 0.7)
    img_scaled = img.resize((new_width_scaled, new_height_scaled), Image.Resampling.LANCZOS)
    img_scaled.save('/home/ubuntu/scaled_image.png')

    # 2. Translação (50px para esquerda, 80px para cima)
    # Criar uma nova imagem com fundo transparente para a translação
    img_translated = Image.new('RGBA', img.size, (0, 0, 0, 0))
    # Calcular a nova posição para colar a imagem (x, y)
    # x = 0 - 50 = -50 (para a esquerda)
    # y = 0 - 80 = -80 (para cima)
    # Como não podemos colar em coordenadas negativas, vamos ajustar o canvas ou considerar que a imagem será cortada.
    # Para manter a imagem visível, vamos criar um canvas maior ou ajustar a translação para dentro dos limites.
    # Para este exemplo, vamos transladar dentro do canvas original, o que significa que partes da imagem podem sair do quadro.
    # Se a intenção é que a imagem inteira seja visível, o canvas precisaria ser maior.
    # Considerando que a translação é relativa ao canto superior esquerdo da imagem original.
    # Para mover 50px para a esquerda, o canto superior esquerdo da imagem original vai para (0-50, 0).
    # Para mover 80px para cima, o canto superior esquerdo da imagem original vai para (0, 0-80).
    # Se a imagem for colada em (0,0) e a translação for aplicada ao conteúdo, é mais complexo.
    # A forma mais simples com Pillow é colar a imagem em uma nova posição no canvas.
    # Para transladar 50px para a esquerda e 80px para cima, a imagem original deve ser colada em (-50, -80) no novo canvas.
    # No entanto, Pillow não permite colar em coordenadas negativas. Vamos simular a translação movendo o conteúdo da imagem.
    # Uma maneira de fazer isso é criar um canvas maior e colar a imagem transladada nele.
    # Ou, para simplificar e focar na transformação, vamos assumir que a translação é relativa ao canto superior esquerdo do canvas.
    # Se a translação é para a esquerda e para cima, a imagem se move para fora do canvas.
    # Para que a imagem permaneça visível, vamos considerar a translação como um deslocamento do ponto de origem da imagem.
    # Ou seja, a imagem será colada em (50, 80) no novo canvas, mas isso seria para baixo e para a direita.
    # Para esquerda e para cima, teríamos que cortar a imagem ou expandir o canvas.
    # Vamos criar um canvas maior para acomodar a translação para a esquerda e para cima.
    # Novo tamanho do canvas para acomodar a translação:
    # Largura: width + abs(dx)
    # Altura: height + abs(dy)
    # Onde dx = -50, dy = -80
    # A imagem original será colada em (abs(dx), abs(dy)) no novo canvas.
    # A imagem transladada será então o recorte da área de interesse.

    # Para translação de -50px (esquerda) e -80px (cima), a imagem original será colada em (50, 80) em um canvas maior.
    # E então, a imagem transladada será o recorte a partir de (0,0) do novo canvas.
    # Isso efetivamente move a imagem para a esquerda e para cima, cortando as partes que saem do canvas original.

    # Para translação, o método `transform` ou `paste` com offset é mais adequado.
    # Usaremos `paste` em um novo canvas.
    # A translação é (dx, dy). Se dx é negativo, move para a esquerda. Se dy é negativo, move para cima.
    # Para colar a imagem original em um novo canvas de forma que ela pareça transladada:
    # Se dx = -50, dy = -80, a imagem original deve ser colada em (0-dx, 0-dy) = (50, 80) em um canvas do mesmo tamanho.
    # Isso fará com que a imagem se mova para a direita e para baixo.
    # Para mover para a esquerda e para cima, precisamos de um canvas maior ou cortar a imagem.

    # Vamos usar o método `transform` para translação, que é mais direto.
    # `transform` takes a 6-tuple (a, b, c, d, e, f) for an affine transform:
    # x_new = a*x + b*y + c
    # y_new = d*x + e*y + f
    # For translation, a=1, b=0, d=0, e=1. c is dx, f is dy.
    # So, (1, 0, dx, 0, 1, dy)
    # dx = -50 (left), dy = -80 (up)
    img_translated = img.transform(img.size, Image.AFFINE, (1, 0, -50, 0, 1, -80))
    img_translated.save('/home/ubuntu/translated_image.png')

    # 3. Rotacionada (90°)
    # Expand=True para que a imagem rotacionada não seja cortada
    img_rotated = img.rotate(90, expand=True)
    img_rotated.save('/home/ubuntu/rotated_image.png')

if __name__ == '__main__':
    manipulate_image('/home/ubuntu/base_image.png')