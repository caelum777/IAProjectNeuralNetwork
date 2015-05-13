import pygame.font, pygame.event, pygame.draw
from PIL import Image
from Models import neural_network as neu_net
import pickle as pck
from os.path import abspath, exists
import glob

def Process_image(image):
    row = image.size[0]
    col = image.size[1]
    #t=top r=right b=bottom l=left
    to = ri = bo = le = 0
    flag = 0
    pixels = image.load()
    #/top edge/
    for x in range(row):
        for y in range(col):
            r = pixels[x, y][0]
            g = pixels[x, y][1]
            b = pixels[x, y][2]
            if(((r+g+b)/3)<=200):
                flag = 1
                to = x
                break
        if(flag==1):
            flag = 0
            break
    #/bottom edge/
    for x in range(row-1, 0, -1):
        for y in range(col):
            r = pixels[x, y][0]
            g = pixels[x, y][1]
            b = pixels[x, y][2]
            if(((r+g+b)/3)<=200):
                flag = 1
                bo = x
                break
        if(flag==1):
            flag = 0
            break
    #/left edge/

    for y in range(col):
        for x in range(row):
            r = pixels[x, y][0]
            g = pixels[x, y][1]
            b = pixels[x, y][2]
            if(((r+g+b)/3)<=200):
                flag = 1
                le = y
                break
        if(flag==1):
            flag = 0
            break

    #/right edge/
    for y in range(col-1, 0, -1):
        for x in range(row):
            r = pixels[x, y][0]
            g = pixels[x, y][1]
            b = pixels[x, y][2]
            if(((r+g+b)/3)<=200):
                flag = 1
                ri = y
                break
        if(flag==1):
            flag = 0
            break
    box = (to, le, bo, ri)
    img = image.crop(box)
    img.save("crop_image2.png", "PNG")
    img = img.resize((15, 15), Image.ANTIALIAS)
    img.save("resize_image2.png", "PNG")
    pixels = img.load()
    list = []
    for i in range(img.size[0]):    # for every pixel:
        for j in range(img.size[1]):
            r = pixels[j,i][0]
            g = pixels[j,i][1]
            b = pixels[j,i][2]
            if(((r+g+b)/3)>230):
                list.append(1)
                pixels[j,i] = (255,255,255)
            elif(((r+g+b)/3)<=230):
                list.append(0)
                pixels[j,i] = (0,0,0)

    #img.save("image.png", 'PNG')
    return list

def main():
    """Main method. Draw interface"""
    net = neu_net.NeuralNetwork()
    try:
        net.W1 = read_list("Weights\W1.w")
        net.W2 = read_list("Weights\W2.w")
    except:
        net.variable_initialization()
        save_list(net.W1, "Weights\W1.w")
        save_list(net.W2, "Weights\W2.w")
    list1 = read_list("Images\.imgs15x15")
    global screen
    pygame.init()
    screen = pygame.display.set_mode((350, 350))
    #menu = pygame.display.set_mode((350, 500))
    pygame.display.set_caption("Handwriting recognition")

    background = pygame.Surface((350,350))
    background.fill((255, 255, 255))

    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (0, 0, 0)
    lineWidth = 22
    pygame.display.update()

    while keepGoing:

        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:

                lineEnd = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    #pygame.draw.line(background, drawColor, lineStart, lineEnd, lineWidth)
                    pygame.draw.circle(background, drawColor, lineStart, lineWidth, 0)

                lineStart = lineEnd
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    data = pygame.image.tostring(background, 'RGB')
                    img = Image.fromstring('RGB', (350,350), data)
                    list = Process_image(img)
                    net.feed_forward(list, False)
                    #save_list(net.W1, "..\w1")
                    #save_list(net.W1, "..\w2")
                if event.key == pygame.K_c:
                    background = pygame.Surface((350, 350))
                    background.fill((255, 255, 255))
                if event.key == pygame.K_t:
                    #crop_resize(net)
                    for iteration in range(0, 60):
                        for i in range(len(list1)):
                            net.outputs[i] = 1
                            print "Image training: %s" %net.results[i]
                            for j in range(len(list1[i])):
                                net.feed_forward(list1[i][j], True)
                            net.outputs[i] = 0
                        print "Iteration #%s complete..." %iteration
                    print "Training done."
                    save_list(net.W1, "Weights\W1.w")
                    save_list(net.W2, "Weights\W2.w")


                        #print net.W2[0][0:6]
                    #print "Second net: ", net.W2[0]
                    """print "Plis w8 loading images"
                    for x in range(1, 37):
                        list_images =[]
                        path = "E:\Users\Lesmed\Downloads\EnglishHnd\English\Hnd\Img\Sample0"
                        path += str(x)
                        files = glob.glob(path+"\*.png")
                        print x-1
                        net.outputs[0][x-1] = 1

                        for file in files:
                            img = Image.open(file.title())
                            img = Process_image(img)
                            list_images.append(img)

                        all_images.append(list_images[:])
                        net.outputs[0][x-1] = 0

                    #print "All images: " + str(all_images)
                    #save_list(all_images, "..\.imgs")
                    #lista = read_list("..\.imgs")
                    #print lista, "read"
                    #net.outputs[x-1] = 0
                    print "Loading images complete"
                    if net.W1 == []:
                        net.variable_initialization(list_images)
                    for i in len(net.outputs[0]):
                        net.outputs[i] = 1
                        for ele in list_images:
                            net.feed_forward([ele])

                        net.outputs[i] = 0"""
        screen.blit(background, (0, 0))
        pygame.display.flip()


def crop_resize(net):
    print "Plis w8 loading images"
    all_images =[]
    for x in range(1, 37):
        list_images =[]
        path = "E:\Users\Lesmed\Downloads\EnglishHnd\English\Hnd\Img\Sample0"
        path += str(x)
        files = glob.glob(path+"\*.png")
        print x-1
        for file in files:
            img = Image.open(file.title())
            img = Process_image(img)
            list_images.append(img)
        all_images.append(list_images[:])
    print "All images: " + str(all_images)
    save_list(all_images, "Images\.imgs15x15")
    #lista = read_list("..\.imgs")
    #print lista, "read"
    print "Loading images complete"








def save_list(itemlist, outfile):
    #f_path = abspath(outfile)

    with open(outfile, 'w') as f:
        #print f_path
        pck.dump(itemlist, f)

def read_list(infile):
    #f_path = abspath(infile)
    with open(infile, 'r') as f:
        #print f_path
        item_list = pck.load(f)
    return item_list




