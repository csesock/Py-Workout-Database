## Written by: Chris Sesock
## on March 3rd, 2020
##

import sqlite3, wx
import wx.lib.mixins.listctrl as mixlist
from ListControl import MyListCtrl
from InsertDialog import MyDialog


class MainFrame(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title="Workout Database", pos=wx.DefaultPosition, 
                    size = (1160, 540), style=wx.DEFAULT_FRAME_STYLE, name="MainFrame"):
        
        super(MainFrame, self).__init__(parent, id, title, pos, size, style, name)

        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour((200, 200, 200))
        ico = wx.Icon('../assets/workout-icon.png')
        self.SetIcon(ico)

        ########################################################## MENU/STATUS BAR

        menubar = wx.MenuBar()
        file_menu = wx.Menu()
        file_menu.Append(101, '&Insert New Record\tCtrl+N', 'Insert a new workout record')
        file_menu.AppendSeparator()
        file_menu.Append(102, '&Exit\tCtrl+Q', 'Close the program')

        tools_menu = wx.Menu()
        #tools_menu.Append(201, '&Change Theme', "Change the current theme")

        submenu = wx.Menu()
        submenu.Append(301, 'White/Gray', kind = wx.ITEM_RADIO)
        submenu.Append(302, 'Blue/White', kind = wx.ITEM_RADIO)
        submenu.Append(303, 'Green/Blue', kind = wx.ITEM_RADIO)

        #tools_menu.AppendMenu(201, 'Change Theme', submenu)
        tools_menu.Append(202, '&Refresh Database\tF5', 'Display database with updated data')

        preferences_menu = wx.Menu()
        preferences_menu.Append(201, 'Change Theme', submenu)
        
        help_menu = wx.Menu()
        help_menu.Append(401, '&About', 'About this program')
        help_menu.AppendSeparator()
        help_menu.Append(402, '&Contact', 'Contact the author')

        self.Bind(wx.EVT_MENU, self.OnClose, id = 102)
        self.Bind(wx.EVT_MENU, self.callDialog, id = 401)
        self.Bind(wx.EVT_MENU, self.OnAdd, id = 101)
        self.Bind(wx.EVT_MENU, self.callDialog2, id=402)

        menubar.Append(file_menu, "&File")
        menubar.Append(tools_menu, "&Tools")
        menubar.Append(preferences_menu, "&Preferences")
        menubar.Append(help_menu, "&Help")

        self.SetMenuBar(menubar)
        self.CreateStatusBar()

        ###########################################################

        self.list = MyListCtrl(panel, -1, style=wx.LC_REPORT, pos=(20, 30), size=(1110, 350))

        self.calculate_calories_button = wx.Button(panel, -1, label="Caculate Calories", pos=(20, 400))
        self.calculate_day_calories_button = wx.Button(panel, -1, label="Calculate Day", pos=(150, 400))
        self.calculate_range_calories_button = wx.Button(panel, -1, label="Calculate Range", pos=(260, 400))

        self.Bind(wx.EVT_LIST_END_LABEL_EDIT, self.OnEdit)
        self.Bind(wx.EVT_LIST_BEGIN_LABEL_EDIT, self.OnBeginEdit)

        self.Centre()
        self.Show(True)

    def OnBeginEdit(self, event):
        if event.GetColumn() == 0:
            event.Veto()

    def OnEdit(self, event):
        rowID = event.GetIndex()
        workoutID = self.list.GetItemText(rowID, 0)

        new_data = event.GetLabel()
        columnID = event.GetColumn()

        self.UpdateRecord(workoutID, columnID, new_data)
        self.list.populate_list()

    def UpdateRecord(self, workoutID, columnID, data):
        fields = ['date', 'pushups', 'chest_press', 'squats',
                  'lunges', 'vertical_press', 'pullups', 'dumbell_row',
                  'bicep_curls', 'preacher_curls', 'tricep_lifts',
                  'tricep_pushups', 'situps', 'crunches', 'planks']

        con = sqlite3.connect('workout.sqlite')
        cur = con.cursor()

        sql = "UPDATE workout SET " + fields[columnID] + "= ? WHERE date = ?"

        cur.execute(sql, (data, workoutID))
        con.commit()

        cur.close()
        con.close()

    def OnClose(self, event):
        self.Close()

    def OnAdd(self, event):

        #self.OnDisplay(None)
        dlg = MyDialog('Insert New Workout Data')
        btnID = dlg.ShowModal()

        if btnID == wx.ID_OK:
            current_date = dlg.date.GetValue()
            pushups = dlg.pushups.GetValue()
            chest_press = dlg.chest_press.GetValue()
            squats = dlg.squats.GetValue()
            lunges = dlg.lunges.GetValue()
            vertical_press = dlg.vertical_press.GetValue()
            pullups = dlg.pullups.GetValue()
            dumbell_row = dlg.dumbell_row.GetValue()
            bicep_curls = dlg.bicep_curls.GetValue()
            preacher_curls = dlg.preacher_curls.GetValue()
            tricep_lifts = dlg.tricep_lifts.GetValue()
            tricep_pushups = dlg.tricep_pushups.GetValue()
            situps = dlg.situps.GetValue()
            crunches = dlg.crunches.GetValue()
            planks = dlg.planks.GetValue()

        # check to see that no field is left empty
        if (current_date != "" and pushups != "" and chest_press != ""
            and squats != "" and lunges != "" and vertical_press != ""
            and pullups != "" and dumbell_row != "" and bicep_curls != ""
            and preacher_curls != "" and tricep_lifts != "" and tricep_pushups != ""
            and situps != "" and crunches != "" and planks != ""):

            try:
                con = sqlite3.connect('workout.sqlite')
                cur = con.cursor()
                
                sql = "INSERT INTO workout VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" # insert new data (parameterized query)

                cur.execute(sql, (current_date, pushups, chest_press, squats, lunges, vertical_press, pullups, dumbell_row,
                                  bicep_curls, preacher_curls, tricep_lifts, tricep_pushups, situps, crunches, planks))
                con.commit()

            except sqlite3.Error:
                dlg = wx.MessageDialog(self, str(error), 'Error occured')
                dlg.ShowModal()
        
        dlg.Destroy()

    def callDialog(self, event):                              
        dlg = OpenedAboutDialog(1)
        btnID = dlg.ShowModal()

        if btnID == wx.ID_OK:
            dlg.Destroy()

    def callDialog2(self, event):                              
        dlg = OpenedAboutDialogBox(1)
        btnID = dlg.ShowModal()

        if btnID == wx.ID_OK:
            dlg.Destroy()


class OpenedAboutDialog(wx.Dialog):
    def __init__(self, d_state):
        wx.Dialog.__init__(self, None, title = "About Workout Manager", size = (470, 250))                           

        about_text = '''\tWorkout Manager is a front-end program that manages \n
                        a database used to track the number and growth of \n
                        specific excersizes over time, as well as calculate \n
                        calories, and help plan for your future gains.'''

        self.about_label = wx.StaticText(self, -1, about_text, pos = (50, 30))
        self.ok_button = wx.Button(self, id = wx.ID_OK, pos = (200, 180))


class OpenedAboutDialogBox(wx.Dialog):
    def __init__(self, d_state):
        wx.Dialog.__init__(self, None, title = "Contact", size = (400, 250))                           

        about_text = '''\tQuestions or concerns? Reach out to us at \n
                        csesock@murraystate.edu'''

        self.about_label = wx.StaticText(self, -1, about_text, pos = (30, 30))
        self.ok_button = wx.Button(self, id = wx.ID_OK, pos = (180, 120))


if __name__ == "__main__":
    app = wx.App()
    MainFrame(None, -1, "Workout Manager")
    app.MainLoop()


