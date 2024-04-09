#import csv
from random import choice
from time import sleep
import pyxel

#pyxel edit PYXEL_RESOURCE_FILE


class Le2048:
    def __init__(self, larg, haut):
        self.plateau = self.__construction_plateau(larg, haut)
        self.point = 0
        self.screen_size = 256
        self.size = [larg, haut]
        self.win = False
        self.show = False
        #self.classement = False
        pyxel.init(self.screen_size, self.screen_size, title="2048 2.0", fps=60)
        pyxel.camera(0, 0)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    @staticmethod
    def __construction_plateau(larg, haut):
        """Renvoie le plateau de jeu initialisé"""
        plat = []
        for hauteur in range(haut):
            plat.append([])
            for _ in range(larg):
                plat[hauteur].append(0)
        return plat

    def d(self):
        """fonction qui range tout les chiffres à droite du tableaudans l'ordre"""
        for i in self.plateau:
            j = len(i) - 1
            k = len(i) - 1
            while j >= 0:
                if i[j] == 0:
                    j = j - 1
                else:
                    save = i[k]
                    i[k] = i[j]
                    i[j] = save
                    j = j - 1
                    k = k - 1

    def q(self):
        """fonction qui range les chiffres à gauche du tableau dans l'ordre"""
        for i in self.plateau:
            j = 0
            k = 0
            while j < len(i):
                if i[j] == 0:
                    j = j + 1
                else:
                    """
                    save = i[k]
                    i[k] = i[j]
                    i[j] = save
                    """
                    i[k], i[j] = i[j], i[k]
                    j = j + 1
                    k = k + 1

    def s(self):
        """fonction qui met tout les chiffres en bas du tableau dans l'ordre """
        for i in range(len(self.plateau)):
            for j in range(len(self.plateau[i])):
                if not i == len(self.plateau) and not self.plateau[i][j] == 0:
                    t = i
                    while not t == len(self.plateau) - 1 and self.plateau[t + 1][j] == 0:
                        self.plateau[t + 1][j] = self.plateau[t][j]
                        self.plateau[t][j] = 0
                        t = t + 1

    def s4(self):
        for i in range(len(self.plateau) - 2, -1, -1):
            for j in range(len(self.plateau[i])):
                place = i
                while place < len(self.plateau) - 1 and self.plateau[place][j] != 0 and self.plateau[place + 1][j] == 0:
                    self.plateau[place + 1][j] = self.plateau[place][j]
                    self.plateau[place][j] = 0
                    place += 1

    def z(self):
        """fonction qui met tout les chiffres en hauts du tableau dans l'ordre """
        for i in range(len(self.plateau)):
            for j in range(len(self.plateau[i])):
                if not i == 0 and not self.plateau[i][j] == 0:
                    t = i
                    while not t == 0 and self.plateau[t - 1][j] == 0:
                        self.plateau[t - 1][j] = self.plateau[t][j]
                        self.plateau[t][j] = 0
                        t = t - 1

    def q_plus(self):
        """fonction qui aditionne les chiffres pousser vers la gauche"""
        for p in self.plateau:
            i = 0
            while i < len(p) - 1:
                if p[i + 1] == p[i]:
                    p[i + 1] = p[i] + p[i + 1]
                    p[i] = 0
                    i = i + 1
                i = i + 1

    def d_plus(self):
        """fonction qui aditionne les chiffres pousser vers la droite"""
        for p in self.plateau:
            i = len(p) - 1
            while i > 0:
                if p[i - 1] == p[i]:
                    p[i] = p[i] + p[i - 1]
                    p[i - 1] = 0
                    i = i - 1
                i = i - 1

    def z_plus(self):
        """fonction qui additionne les chiffres pousser vers le haut"""
        for i in range(len(self.plateau)):
            for j in range(len(self.plateau[i]) - 1):
                if self.plateau[j + 1][i] == self.plateau[j][i]:
                    self.plateau[j][i] = self.plateau[j + 1][i] + self.plateau[j][i]
                    self.plateau[j + 1][i] = 0

    def s_plus(self):
        """fonction qui additionne les chiffres pousser vers le bas"""
        for i in range(len(self.plateau)):
            j = len(self.plateau) - 1
            while j > 0:
                if self.plateau[j][i] == self.plateau[j - 1][i]:
                    self.plateau[j - 1][i] = self.plateau[j][i] + self.plateau[j - 1][i]
                    self.plateau[j][i] = 0
                    j = j - 1
                j = j - 1

    def new_tuiles(self):
        """fonction qui ajoute une nouvels tuiles de valeur 2 ou 4"""
        vide = choice(self.explore(self.plateau))
        self.plateau[vide[0]][vide[1]] = choice([4, 2, 2])
        self.point = self.plateau[vide[0]][vide[1]] + self.point

    @staticmethod
    def explore(plateau):
        """fonction qui explore le tableau et renvoie une liste de toutes les case vides"""
        vide = []
        for i in range(len(plateau)):
            for j in range(len(plateau[i])):
                if plateau[i][j] == 0:
                    vide.append([i, j])
        return vide

    def winrate(self):
        """indique si une tuiiles avec 2048 est apparue sur le plateau et le plus grand chiffre dans le tableau"""
        win = False
        for i in range(len(self.plateau)):
            for j in range(len(self.plateau[i])):
                if self.plateau[i][j] == 2048:
                    win = True
        return win

    def test(self):
        return self.plateau

    #def best_player(self,etat):
    #    """Enregistre et lit le fichier 2048_best_player.txt en gérant le classement des meilleurs joueurs
    #    prend en paramètre r pour lire et w pour mettre à jour le fichier"""
    #    donnees = ""
    #    if etat == "r" :
    #        with open("2048_best_player.txt", etat, newline="", encoding='utf-8') as csvfile:
    #            lecteur = csv.reader(csvfile,delimiter = ";")
    #            for enreg in lecteur:
    #                donnees += enreg[0] + "\n"
    #    return donnees

    def update(self):
        if pyxel.btnp(pyxel.KEY_E):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_UP):
            self.z()
            self.z_plus()
            self.z()
            self.new_tuiles()
        elif pyxel.btnp(pyxel.KEY_Q) or pyxel.btnp(pyxel.KEY_LEFT):
            self.q()
            self.q_plus()
            self.q()
            self.new_tuiles()
        elif pyxel.btnp(pyxel.KEY_S) or pyxel.btnp(pyxel.KEY_DOWN):
            self.s4()
            self.s_plus()
            self.s4()
            self.new_tuiles()
        elif pyxel.btnp(pyxel.KEY_D) or pyxel.btnp(pyxel.KEY_RIGHT):
            self.d()
            self.d_plus()
            self.d()
            self.new_tuiles()
        elif pyxel.btnp(pyxel.KEY_H):
            if self.show:
                self.show = False
            else:
                self.show = True
       #elif pyxel.btnp(pyxel.KEY_B):
       #    if self.classement:
       #        self.classement = False
       #    else:
       #        self.classement = True


    def draw(self):
        pyxel.cls(0)
        xy = self.screen_size // 4
        taille_tuiles = 25
        if self.show:
            pyxel.text(self.screen_size // 2 - 20, 10, 'The 2048', 10)
            pyxel.text(xy + 25, xy + 25, "Up or Z to go up"+ 2 * "\n" + "Left or Q to go left " + 2 * "\n" +
                       "Down or S to go down" + 2 * "\n" + "Right or D to go right" + 2 * "\n" +
                       "E to exit the game", 7)
            pyxel.text(10, 240, "\nPress H to exit how to play", 3)
        #elif self.classement:
        #    pyxel.text(self.screen_size // 2 - 20, 10, 'The 2048', 10)
        #    pyxel.text(xy + 25, xy + 25,self.best_player("r") , 7)
        #    pyxel.text(10, 240, "Press E to exit the game \nPress H to see how to play", 3)
        else:
            pyxel.rect(xy, xy, taille_tuiles * self.size[0], taille_tuiles * self.size[1], 1)
            pyxel.text(10, 240, "Press E to exit the game \nPress H to see how to play", 3)
            pyxel.text(self.screen_size//2 + 25, self.screen_size//4 - 10, str(self.point) + ": points",7)
            pyxel.text(self.screen_size//2 - 20, 10, 'The 2048', 10)
            lst_couleur = [7, 6, 12, 5, 3, 11, 15, 10, 9, 8]
            if not self.win and self.winrate():
                pyxel.text(xy - 15, xy, "You Win ! ^0^", 10)
                sleep(5)
                self.win = True
            for i in range(len(self.plateau)):
                for j in range(len(self.plateau[i])):
                    if 0 < self.plateau[i][j] < 2048:
                        color = 0
                        t = self.plateau[i][j]
                        while color < len(lst_couleur) - 1 and t != 2:
                            t = t // 2
                            color += 1
                        pyxel.rect(taille_tuiles * j + xy, taille_tuiles * i + xy, taille_tuiles, taille_tuiles, lst_couleur[color])
                        pyxel.text(taille_tuiles * j + xy + 25 // 2 - len(str(self.plateau[i][j])), taille_tuiles * i + xy +25//2 - len(str(self.plateau[i][j])), str(self.plateau[i][j]), 0)
                    elif self.plateau[i][j] == 2048:
                        pyxel.rect(taille_tuiles * j + xy, taille_tuiles * i + xy, taille_tuiles, taille_tuiles, 0)
                        pyxel.text(taille_tuiles * j + xy + 25 // 2 - len(str(self.plateau[i][j])), taille_tuiles * i + xy + 25 // 2 - len(str(self.plateau[i][j])), str(self.plateau[i][j]),7)
                    elif self.plateau[i][j] != 0:
                        pyxel.rect(taille_tuiles * j + xy, taille_tuiles * i + xy, taille_tuiles, taille_tuiles, self.plateau[i][j]%15 + 1)
                        pyxel.text(taille_tuiles * j + xy + 25 // 2 - len(str(self.plateau[i][j])), taille_tuiles * i + xy + 25 // 2 - len(str(self.plateau[i][j])), str(self.plateau[i][j]),0)


Le2048(5, 5)
