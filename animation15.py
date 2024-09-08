import pygame
import sys

pygame.init()
width, high = 1200, 600
screen = pygame.display.set_mode((width, high))
pygame.display.set_caption("The_Major_Number")
colors = {
    "background": (230, 240, 255),  
    "text": (47, 79, 79),  
    "border": (70, 130, 180),  
    "highlight": (255, 165, 0), 
    "box_fill": (230, 230, 250), 
    "candidate": (144, 238, 144)  
}

def create_array(array):
    x, y = 20, 100
    for i in range(len(array)):
        pygame.draw.rect(screen, colors["border"], (x, y, 60, 40), 3)
        font = pygame.font.Font(None, 36)
        text = font.render(str(array[i]), True, colors["text"])
        screen.blit(text, (x + 30, y + 10))
        x += 55
    font = pygame.font.Font(None, 40)
    text = font.render("The Major Number Problem Code:", True, colors["text"])
    screen.blit(text, (700, 250))
    
   
    pygame.draw.rect(screen, colors["border"], (690, 290, 460, 180), 2, border_radius=15)
    
    font = pygame.font.Font(None, 25)
    code_lines = [
        "def The_Major_Number(numbers):",
        "    candidate = None",
        "    counter = 0",
        "    for num in numbers:",
        "        if counter == 0:",
        "            candidate = num",
        "        counter += 1 if num == candidate else -1",
        "    return candidate"
    ]
    for i, line in enumerate(code_lines):
        text = font.render(line, True, colors["text"])
        screen.blit(text, (700, 300 + i * 20))

def create_the_candidate(candidate, counter):
    pygame.draw.rect(screen, colors["candidate"], (120, 300, 350, 200))
    pygame.draw.rect(screen, colors["border"], (120, 300, 350, 200), 4)
    font = pygame.font.Font(None, 50)
    text = font.render("The candidate is: " + str(candidate), True, colors["text"])
    screen.blit(text, (140, 320))
    text = font.render("The counter is: " + str(counter), True, colors["text"])
    screen.blit(text, (140, 380))

def the_algo(array):
    candidate = None
    counter = 0
    x, y = 20, 100
    for num in array:
        if counter == 0:
            candidate = num
        counter += 1 if num == candidate else -1
        
        screen.fill(colors["background"])  
        create_array(array)
        
        pygame.draw.rect(screen, colors["highlight"], (x, y, 60, 40))
        font = pygame.font.Font(None, 36)
        text = font.render(str(num), True, colors["text"])
        screen.blit(text, (x + 30, y + 10))
        x += 55
        
        create_the_candidate(candidate, counter)
        
        pygame.display.flip()
        pygame.time.delay(1000)  

    font = pygame.font.Font(None, 50)
    text = font.render("The winning candidate is: " + str(candidate), True, colors["text"])
    screen.blit(text, (120, 515))
    pygame.display.flip()
    pygame.time.delay(5000)  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(colors["background"])
    the_algo([1,8,2, 2, 3, 2, 2, 3, 2, 3, 3, 2, 3, 3, 6,3,2,3,3,3])
    pygame.display.flip()
    pygame.quit()
    sys.exit()