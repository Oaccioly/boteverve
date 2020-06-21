import pyautogui as pg
import keyboard as kb
from time import sleep


def youtubeViews(vezes):
    coords = [(1102, 520),
              (471, 30),
              (678, 707)]

    for _ in range(vezes):
        print('Primeiro click')
        pg.click(coords[0])
        sleep(35)

        print('Fechando aba')
        pg.click(coords[1])
        sleep(5)

        print('Iniciando nova aba')
        pg.click(coords[2])
        sleep(2)


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

        for _ in range(5):
            print('Procurando Seguir perfil')
            instabt = pg.locateOnScreen('instabt.png',
                                        region=(1206, 840, 1528, 936))

            if instabt:
                print('\nBotao 1 encontrado')
                pg.click(pg.center(instabt))
                self.acertos += 1
                self.teste += 1
                break

            elif falha >= 3:
                kb.press_and_release('f5')
                sleep(5)

            self.errosbt1 += 1
            falha += 1
            print(falha)

    def butao2(self):
        falha = 0

        for _ in range(3):
            print('Procurando Seguir no intagram')
            seguirbt = pg.locateOnScreen('seguirbt.png',
                                         region=(288, 439, 527, 554))

            seguirbt2 = pg.locateOnScreen('seguirbt2.png',
                                         region=(288, 439, 527, 554))
            if seguirbt:
                print('Botao 2 encontrado')
                pg.click(pg.center(seguirbt))

                kb.press_and_release('ctrl+w')
                self.acertos += 1
                self.teste += 1
                break

            elif seguirbt2:
                print('Botao 2 encontrado')
                pg.click(pg.center(seguirbt))

                kb.press_and_release('ctrl+w')
                self.acertos += 1
                self.teste += 1
                break

            elif falha > 2:
                break

            self.errosbt2 += 1

    def butao3(self):
        falha = 0

        for _ in range(3):
            print('Procurando botao proximo')
            proximo = pg.locateOnScreen('proximo.png',
                                        region=(276, 753, 1355, 960))

            proximo2 = pg.locateOnScreen('proximo2.png',
                                         region=(276, 753, 1355, 960))

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

                try:
                    print('Try1 procurando')
                    pg.click('erro2.png')
                    pg.click('proximo2.png')
                    break
                except TypeError:
                    print('Atualizando pagina')
                    kb.press_and_release('f5')
                    sleep(3)
                    break

            falha += 1
            self.errosbt3 += 1


def regiao(x1, y1, x2, y2):
    pg.move(x1, y2)
    for _ in range(5):
        pg.moveTo(x2, y1, 1)
        pg.moveTo(x2, y2, 1)
        pg.moveTo(x1, y2, 1)
        pg.moveTo(x1, y1, 1)


bot = Instagram()
while True:
    for _ in range(20):
        bot.loop()
    kb.press_and_release('f5')
    sleep(4)
