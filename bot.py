import pyautogui as pg
import keyboard as kb
from time import sleep

class Instagram:
    def __init__(self):
        self.renda = 0.0010
        self.saldo = 0.0000
        self.errosbt1 = 0
        self.errosbt2 = 0
        self.errosbt3 = 0
        self.acertos = 0

        self.teste = 1

    def loop(self):
        if self.teste == 1:
            self.butao1()
            sleep(5)

        elif self.teste == 2:
            self.butao2()
            sleep(2)

        elif self.teste == 3:
            self.butao3()

    def butao1(self):
        falha = 0

        for _ in range(6):
            print('Procurando Seguir perfil')
            instabt = pg.locateOnScreen('instabt.png')

            if instabt:
                print('\nBotao 1 encontrado')
                pg.click(pg.center(instabt))
                self.acertos += 1
                self.teste += 1
                break

            elif falha >= 3:
                kb.press_and_release('f5')
                sleep(5)
            
            elif falha == 6:              
                pg.click(470, 40)
                pg.move(470, 400)

            self.errosbt1 += 1
            falha += 1
            print(falha)

    def butao2(self):
        falha = 0

        for _ in range(3):
            print('Procurando Seguir no intagram')
            seguirbt = pg.locateOnScreen('seguirbt.png')

            seguirbt2 = pg.locateOnScreen('seguirbt2.png')

            if seguirbt:
                print('Botao 2 encontrado')
                pg.click(pg.center(seguirbt))
                sleep(1)
                pg.click(470, 40)
                self.acertos += 1
                self.teste += 1
                break

            elif seguirbt2:
                print('Botao 2 encontrado')
                pg.click(pg.center(seguirbt2))
                sleep(1)
                pg.click(470, 40)
                self.acertos += 1
                self.teste += 1
                break

            elif falha == 2:
                self.teste = 3
                pg.click(470, 40)
                pg.move(470, 400)
                continue
            
            print(falha)
            falha += 1
            self.errosbt2 += 1
            sleep(2)

    def butao3(self):
        falha = 0

        for _ in range(3):
            print('Procurando botao proximo')
            proximo = pg.locateOnScreen('proximo.png')

            proximo2 = pg.locateOnScreen('proximo2.png')

            if proximo:
                pg.click(pg.center(proximo))
                print('Botao proximo encontrado')

                self.acertos += 1
                self.saldo += self.renda
                self.teste = 1
                print("Relatorio"
                      f"\nSaldo = {self.saldo}"
                      f"\nAcertos {self.acertos}"
                      f"\nErros no bt1 {self.errosbt1}"
                      f"\nErros no bt2 {self.errosbt2}"
                      f"\nErros no bt3 {self.errosbt3}")
                break

            elif proximo2:
                pg.click(pg.center(proximo2))

                self.acertos = 1
                self.saldo += self.renda
                self.teste = 1
                print("Relatorio"
                      f"\nSaldo = {self.saldo}"
                      f"\nAcertos {self.acertos}"
                      f"\nErros no bt1 {self.errosbt1}"
                      f"\nErros no bt2 {self.errosbt2}"
                      f"\nErros no bt3 {self.errosbt3}")
                break

            elif falha == 2:
                kb.press_and_release('f5')
                self.teste = 1
                break

            falha += 1
            self.errosbt3 += 1

bot = Instagram()
while True:
    for _ in range(20):
        bot.loop()
    kb.press_and_release('f5')
    sleep(4)
