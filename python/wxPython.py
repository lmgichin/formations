# -*- coding: utf-8 -*-

import wx


# ####################################################################################################
# test d'affichage d'une frame
# ####################################################################################################

def testAffichageFrame():

    app = wx.App(False)
    frame = wx.Frame(None,wx.ID_ANY, u"Ma première frame")
    frame.Show(True)
    app.MainLoop()


# ####################################################################################################
# test d'un éditeur (MultiLine Edit)
# ####################################################################################################

def testEditor():
    app = wx.App(False)
    MyTextEditor(None, u'Mon premier éditeur')
    app.MainLoop()


class MyTextEditor(wx.Frame):

    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title)
        txtCtrl = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        self.CreateStatusBar()

        menu = wx.Menu()
        mnAbout = menu.Append(wx.ID_ABOUT, "&About", u"Information à propos du programme")
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, "E&xit", "On sort...")
        menubar = wx.MenuBar()
        menubar.Append(menu,"&Fichier")

        self.Bind ( wx.EVT_MENU, self.OnAbout, mnAbout)

        self.SetMenuBar(menubar)
        self.Show(True)

    def OnAbout(self,event):
        dlg = wx.MessageDialog ( self, u"Ma première application", u"A propos", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()


# ####################################################################################################
# test d'utilisation d'un sizer avec plusieurs contrôles
# ####################################################################################################

def testSizer():
    app = wx.App(False)
    fgsSizer(None, u'Mon premier sizer')
    app.MainLoop()

class fgsSizer(wx.Frame):

    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title)

        panel = wx.Panel(self)
        vbox = wx.BoxSizer (wx.VERTICAL)
        fgs = wx.FlexGridSizer(3,2,9,25)

        titre = wx.StaticText(panel, label=u"Titre ééé")
        auteur = wx.StaticText(panel,label=u"Auteur ààà")
        comment = wx.StaticText(panel,label='Commentaires')

        self.tc_t = wx.TextCtrl(panel)
        self.tc_a = wx.TextCtrl(panel)
        self.tc_c = wx.TextCtrl(panel,style=wx.TE_MULTILINE)

        fgs.AddMany([(titre), (self.tc_t,1,wx.EXPAND), (auteur),(self.tc_a,1,wx.EXPAND), (comment,1,wx.EXPAND), (self.tc_c,1,wx.EXPAND) ])
        fgs.AddGrowableRow (2, 1)
        fgs.AddGrowableCol (1, 1)
        vbox.Add(fgs, proportion=1,flag=wx.ALL|wx.EXPAND, border=10)
        panel.SetSizer(vbox)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        bok = wx.Button(panel,wx.ID_OK)
        bcn = wx.Button(panel,wx.ID_CANCEL)
        hbox.Add ( bok, flag = wx.ALL, border = 5)
        hbox.Add ( bcn, flag = wx.ALL, border = 5)

        vbox.Add(hbox, flag=wx.BOTTOM|wx.RIGHT|wx.ALIGN_RIGHT, border = 10)

        self.Bind ( wx.EVT_BUTTON, self.onclick, bok)
        self.Bind ( wx.EVT_BUTTON, self.onclick, bcn)
        self.Bind ( wx.EVT_CLOSE, self.OnCloseWindow)

        self.Show(True)


    def onclick(self,event):

        if event.GetId() == wx.ID_CANCEL:
            self.Close()
        else:
            self.tc_c.AppendText("%s\n%s" % (self.tc_t.GetValue(),self.tc_a.GetValue()))

    def OnCloseWindow(self,event):

        dial = wx.MessageDialog(None, 'Voulez-vous vraiment quitter ?', 'Question importante',
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)

        ret = dial.ShowModal()

        if ret == wx.ID_YES:
            self.Destroy()

# ###############################################################################################


# testAffichageFrame()
# testEditor()
testSizer()
