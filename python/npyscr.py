# -*- coding: utf-8 -*-
import npyscreen

class MyAutoComplete(npyscreen.Autocomplete):

    colors = ["Jaune","Bleu","Rouge","Vert", "Vert foncé"]

    def auto_complete(self, input):

        choices = []

        for word in MyAutoComplete.colors:

            if word.startswith(self.value):
                choices.append(word)

        self.value = choices[self.get_choice(choices)]


class MyTitleAutoComplete(npyscreen.TitleText):
    _entry_type = MyAutoComplete

class MyScreen(npyscreen.NPSApp):

    def main(self):

        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        f = npyscreen.ActionForm(name = u"C'est ma fenêtre...")
        f.add(npyscreen.FixedText, value="Texte non modifiable...")
        nom = f.add(npyscreen.TitleText, name = "Saisir le nom", value ="<None>")

        rvalues = ["Option 1","Option 2", "Option 3"]
        radio = f.add(npyscreen.TitleSelectOne, max_height=len(rvalues)+1, value=[0], \
                      name="Choix :", values = rvalues, scroll_exit=False)

        cbox = f.add(npyscreen.TitleMultiSelect, max_height=len(rvalues)+1, value=[0], \
                      name="Choix :", values = rvalues, scroll_exit=False)

        tauto = f.add(MyTitleAutoComplete, name = "Couleur : ")
        f.edit()
        #npyscreen.notify_wait("Valeur saisie : " + nom.value, title="Check...")
        #npyscreen.notify_wait("Valeur saisie : " + radio.get_selected_objects()[0], title="Check radio...")
        #npyscreen.notify_wait("Valeur saisie : " + tauto.value, title="Check auto...")

        #lval = ""
        #for val in cbox.get_selected_objects():
        #    lval += val
        #npyscreen.notify_wait("Valeur saisie : " + lval, title="Check box...")

    def on_cancel(self):
        npyscreen.notify_wait("Valeur cancel", title="OK")

    def on_ok(self):
        npyscreen.notify_wait("Valeur ok", title="OK")



if __name__ == '__main__':

    app = MyScreen()
    app.run()