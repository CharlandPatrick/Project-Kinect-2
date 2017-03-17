import pyautogui, os

clear = lambda: os.system('cls')

def mouseClick(bouton):
    if bouton == 1:
        pyautogui.click(button='left')
    elif bouton == 2:
        pyautogui.click(button='middle')
    elif bouton == 3:
        pyautogui.click(button='right')
        
def mouseMove(x, y):
    if pyautogui.onScreen(x,y):
        pyautogui.moveTo(int(x),int(y))

choix = 0
while choix!='3':   
    print('1 - Déplacer la souris')
    print('2 - Cliquez')
    print('3 - Quitter')
    choix = input('Votre choix = ')
    if choix == '1':
        nouvelleposition = input('Position x,y : ')
        x, y = nouvelleposition.split(',')
        mouseMove(int(x), int(y))

    if choix == '2':
        bouton = input('Quel bouton ?(1=gauche, 2=milieu, 3=droite) : ')
        mouseClick(int(bouton))



