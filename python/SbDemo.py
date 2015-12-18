# -*- coding: utf8 -*-
__author__ = 'lucio le seul'

import wx


class Panel1(wx.Panel):
    # Pour la gestion du singleton
    instance = None

    def __new__(cls, parent):
        if Panel1.instance is None :
            Panel1.instance = object.__new__(cls, parent)
        return Panel1.instance

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)


class MenuFichier(wx.Menu):
    # Pour la gestionne du singleton
    instance = None

    def __new__(cls):
        if MenuFichier.instance is None:
            MenuFichier.instance = wx.Menu.__new__(cls)
        return MenuFichier.instance

    def __init__(self):
        wx.Menu.__init__(self)
        item_quitter = self.Append(wx.ID_EXIT, "&Quitter", "Quitte le programme")
        self.Bind(wx.EVT_MENU, self.item_quitter_execute, item_quitter)

    def item_quitter_execute(self, event):
        return 0


class MenuBar1(wx.MenuBar):
    # Pour la gestion du singleton
    instance = None

    def __new__(cls):
        if MenuBar1.instance is None:
            MenuBar1.instance = wx.MenuBar.__new__(cls)
        return MenuBar1.instance

    def __init__(self):
        wx.MenuBar.__init__(self)
        self.Append(MenuFichier(), "&Fichier")


class Frame1(wx.Frame):
    # Pour la gestion du singleton
    instance = None

    def __new__(cls, parent):
        if Frame1.instance is None:
            Frame1.instance = wx.Frame.__new__(cls, parent)
        return Frame1.instance

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title="Application de démonstration")
        Panel1(self)
        self.SetMenuBar(MenuBar1())
        self.CreateStatusBar()


class MonApplication(wx.App):
    def __init__(self, redirect=False, filename=None):

        wx.App.__init__(self, redirect, filename)
        Frame1(None).Show();

if __name__ == '__main__':
    application = MonApplication()
    application.MainLoop()
