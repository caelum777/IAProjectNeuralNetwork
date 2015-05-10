import pygame.font, pygame.event, pygame.draw
from PIL import Image
import main as logic
def main():
    """Main method. Draw interface"""

    global screen
    pygame.init()
    screen = pygame.display.set_mode((350, 350))
    pygame.display.set_caption("Handwriting recognition")

    background = pygame.Surface((350,350))
    background.fill((255, 255, 255))
    background2 = pygame.Surface((360,360))
    background2.fill((255, 255, 255))

    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (0, 0, 0)
    lineWidth = 5
    pygame.display.update()

    while keepGoing:

        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.line(background, drawColor, lineStart, lineEnd, lineWidth)
                lineStart = lineEnd
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    data = pygame.image.tostring(background, 'RGB')
                    img = Image.fromstring('RGB', (350,350), data)
                    img = img.resize((30, 30), Image.ANTIALIAS)
                    pixels = img.load()
                    print("0 = black / 1 = white")
                    matrix = []
                    for i in range(img.size[0]):    # for every pixel:
                        matrix.append([])
                        for j in range(img.size[1]):
                            r = pixels[j,i][0]
                            g = pixels[j,i][1]
                            b = pixels[j,i][2]
                            if(((r+g+b)/3)>200):
                                matrix[i].append(1)
                                pixels[j,i] = (255,255,255)
                            elif(((r+g+b)/3)<=200):
                                matrix[i].append(0)
                                pixels[j,i] = (0,0,0)

                    img.save("C:\Users\Pablo\PycharmProjects\Progra IA\imagen.png", 'PNG')
                    logic.feedforward(matrix)
                elif event.type == pygame.K_c:
                    background = pygame.Surface((350,350))

        screen.blit(background, (0, 0))
        pygame.display.flip()
main()