"""
Le programme ci-dessous permet de déterminer la date de notification en l'absence du confinement soit date prévue de la
notification - 165 jours

Éditeur : Laurent REYNAUD
Date : 04-11-2020
"""

from tkinter import *
from tkinter import messagebox
import datetime
import locale

root = Tk()
root.title("LR - Ma p'tite calculette CFIR !")
root.geometry('400x170')
root.resizable(width=False, height=False)


class MyMenu(Menu):
    """Menu"""

    def __init__(self, master, **kw):
        """Constructeur spécifique pour les menus de tkinter"""
        super().__init__(master, **kw)
        mainmenu = Menu(self.master)
        self.master.config(menu=mainmenu)

        """Menu 'à propos'"""
        self.about = Menu(mainmenu, tearoff=0)
        self.about.add_command(label='À propos...', command=self.message)

        """Lien avec le bouton de droite de la souris"""
        root.bind('<Button-3>', self.my_popup)

    def my_popup(self, e):
        """Fonction permettant d'afficher le menu dans la fenêtre selon l'endroit où on a cliqué avec le bouton de
        droite de la souris"""
        self.about.tk_popup(e.x_root, e.y_root)

    def message(self, *args):
        """Message qui apparaît après avoir cliqué sur le menu 'À propos    '"""
        version = messagebox.showinfo('À propos', "Date pour CFIR\n\n2020 - Laurent REYNAUD")
        Label(root, text=version).pack()


class Date_cfir(Frame):
    """Calcul de la date de notification dans confinement"""

    def __init__(self, master):
        """Constructeur"""
        super().__init__(master)
        self.pack()
        self.widgets()

    def calculate_date(self):
        """Détermination de la date de notification sans confinement"""

        self.error.delete(0, 'end')
        try:
            d = str(self.entry_date.get())
            my_list = d.split('/')  # conversion en liste
            dt = datetime.date(int(my_list[2]), int(my_list[1]),
                               int(my_list[0]))  # conversion format classe datetime.date
            locale.setlocale(locale.LC_TIME, 'FR')
            d_covid = dt - datetime.timedelta(165)  # date de notification - 165 jours
            self.var_entry_date2.set(d_covid.strftime('%d/%m/%Y'))
        except (IndexError, ValueError):
            self.var_error.set('Erreur de saisie')

    def widgets(self):
        """Configuration des widgets"""

        """Titre"""
        label_title = Label(self, text='CFIR - Date de notification & confinement')
        label_title.grid(row=0, column=0, columnspan=2, pady=10)

        """Date de notification"""
        label_date = Label(self, text='Date de notification (JJ/MM/AAAA) :')
        self.entry_date = Entry(self, justify='center')
        self.var_error = StringVar()
        self.error = Entry(self, bd=0, bg='#EFEFEF', textvariable=self.var_error, fg='red')
        label_date.grid(row=1, column=0, padx=10, pady=10)
        self.entry_date.grid(row=1, column=1)
        self.error.grid(row=2, column=0)

        """Bouton 'Calculer'"""
        btn_calculate = Button(self, text='Calculer', command=self.calculate_date)
        btn_calculate.grid(row=2, column=1)

        """Calcul de la date de notification hors confinement"""
        label_date2 = Label(self, text='Date de notification hors confinement :')
        self.var_entry_date2 = StringVar()
        entry_date2 = Entry(self, justify='center', bd=0, bg='#EFEFEF', textvariable=self.var_entry_date2)
        label_date2.grid(row=3, column=0)
        entry_date2.grid(row=3, column=1, padx=10, pady=10)

        """Bouton pour quitter l'application"""
        btn_exit = Button(self, text='Quitter', command=self.quit)
        btn_exit.grid(row=4, column=0, columnspan=2, pady=10)


mymenu = MyMenu(root)
date_cfir = Date_cfir(root)
root.mainloop()
