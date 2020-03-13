## Written by: Chris Sesock on May 3rd, 2020
##

import sqlite3, wx
import wx.lib.mixins.listctrl as mixlist


# build the structure for the table
##workout = '''CREATE TABLE workout (
##            Date DATETIME PRIMARY KEY,
##            Push_Up INTEGER(3),
##            Chest_Press INTEGER(3),
##            Squats INTEGER(3),
##            Lunges INTEGER(3),
##            Vertical_Press INTEGER(3),
##            Pullup INTEGER(3),
##            Dumbell_Row INTEGER(3),
##            Bicep_Curl INTEGER(3),
##            Preacher_Curl INTEGER(3),
##            Tricep_Lift INTEGER(3),
##            Tricep_Pushup INTEGER(3),
##            Situp INTEGER(3),
##            Crunches INTEGER(3),
##            Planks INTEGER(3)
##        '''



class MyDialog(wx.Dialog):

    def __init__(self, title):
        wx.Dialog.__init__(self, None, title = title, size = (320, 750))

        con = sqlite3.connect('workout.sqlite')
        cur = con.cursor()

        self.date = wx.TextCtrl(self, -1, pos = (50, 40))
        wx.StaticText(self, -1, 'Date', pos = (180, 40))
        self.pushups = wx.TextCtrl(self, -1, pos = (50, 90))
        wx.StaticText(self, -1, 'Pushups', pos = (180, 90))
        self.chest_press = wx.TextCtrl(self, -1, pos = (50, 130))
        wx.StaticText(self, -1, 'Chest Press', pos = (180, 130))
        self.squats = wx.TextCtrl(self, -1, pos = (50, 170))
        wx.StaticText(self, -1, 'Squats', pos = (180, 170))
        self.lunges = wx.TextCtrl(self, -1, pos = (50, 210))
        wx.StaticText(self, -1, 'Lunges', pos = (180, 210))
        self.vertical_press = wx.TextCtrl(self, -1, pos = (50, 250))
        wx.StaticText(self, -1, 'Vertical Press', pos = (180, 250))
        self.pullups = wx.TextCtrl(self, -1, pos = (50, 290))
        wx.StaticText(self, -1, 'Pullups', pos = (180, 290))
        self.dumbell_row = wx.TextCtrl(self, -1, pos = (50, 330))
        wx.StaticText(self, -1, 'Dumbell Rows', pos = (180, 330))
        self.bicep_curls = wx.TextCtrl(self, -1, pos = (50, 370))
        wx.StaticText(self, -1, 'Bicep Curls', pos = (180, 370))
        self.preacher_curls = wx.TextCtrl(self, -1, pos = (50, 410))
        wx.StaticText(self, -1, 'Hammer Curls', pos = (180, 410))
        self.tricep_lifts = wx.TextCtrl(self, -1, pos = (50, 450))
        wx.StaticText(self, -1, 'Tricep Lifts', pos = (180, 450))
        self.tricep_pushups = wx.TextCtrl(self, -1, pos = (50, 490))
        wx.StaticText(self, -1, 'Tricep Pushups', pos = (180, 490))
        self.situps = wx.TextCtrl(self, -1, pos = (50, 530))
        wx.StaticText(self, -1, 'Situps', pos = (180, 530))
        self.crunches = wx.TextCtrl(self, -1, pos = (50, 570))
        wx.StaticText(self, -1, 'Crunches', pos = (180, 570))
        self.planks = wx.TextCtrl(self, -1, pos = (50, 610))
        wx.StaticText(self, -1, 'Planks', pos = (180, 610))

        self.pushups.SetValue('0')
        self.chest_press.SetValue('0')
        self.squats.SetValue('0')
        self.lunges.SetValue('0')
        self.vertical_press.SetValue('0')
        self.pullups.SetValue('0')
        self.dumbell_row.SetValue('0')
        self.bicep_curls.SetValue('0')
        self.preacher_curls.SetValue('0')
        self.tricep_lifts.SetValue('0')
        self.tricep_pushups.SetValue('0')
        self.situps.SetValue('0')
        self.crunches.SetValue('0')
        self.planks.SetValue('0')

        ok_button = wx.Button(self, id = wx.ID_OK, pos = (50, 670))
        


class MyListCtrl(wx.ListCtrl, mixlist.TextEditMixin, mixlist.ListCtrlAutoWidthMixin):

    def __init__(self, parent, id, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0):

        wx.ListCtrl.__init__(self, parent, id, pos, size, style)
        mixlist.TextEditMixin.__init__(self)
        mixlist.ListCtrlAutoWidthMixin.__init__(self)

        self.InsertColumn(0, 'Date', width = 80)
        self.InsertColumn(1, 'Push Ups', width = 70)
        self.InsertColumn(2, 'Chest Press', width = 90)
        self.InsertColumn(3, 'Squats', width = 60)
        self.InsertColumn(4, 'Lunges', width = 60)
        self.InsertColumn(5, 'Vertical Press', width = 90)
        self.InsertColumn(6, 'Pullups', width = 60)
        self.InsertColumn(7, 'Dumbell Row', width = 90)
        self.InsertColumn(8, 'Bicep Curl', width = 70)
        self.InsertColumn(9, 'Hammer Curl', width = 90)
        self.InsertColumn(10, 'Tricep Lift', width = 70)
        self.InsertColumn(11, 'Tricep Pushup', width = 95)
        self.InsertColumn(12, 'Situps', width = 50)
        self.InsertColumn(13, 'Crunches', width = 70)
        self.InsertColumn(14, 'Planks', width = 70)

        self.populate_list()


        

    def populate_list(self):

        self.DeleteAllItems() # clear all rows in list 
 
        try: 
            con = sqlite3.connect('workout.sqlite') 
            cur = con.cursor() 
 
            cur.execute("SELECT * FROM workout")
            results = cur.fetchall() 
 
            count = 0 
            for row in results: 
                self.Append(row) 
                if count % 2: 
                    self.SetItemBackgroundColour(count, "white") 
                else: 
                    self.SetItemBackgroundColour(count, (200, 200, 200)) 
                count += 1 
 
            cur.close() 
            con.close() 
 
        except sqlite3.Error: 
            dlg = wx.MessageDialog(self, str(error), 'Error occured') 
            dlg.ShowModal() 



class MyFrame(wx.Frame):

    def __init__(self, parent, id = wx.ID_ANY, title = "Workout Database", pos = wx.DefaultPosition, 
                    size = (1200, 540), style = wx.DEFAULT_FRAME_STYLE, name = "MyFrame"):
        super(MyFrame, self).__init__(parent, id, title, pos, size, style, name)

        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour((200, 200, 200))
        ico = wx.Icon('workout-icon.png')
        self.SetIcon(ico)

        ########################################################## MENU/STATUS BAR

        menubar = wx.MenuBar()
        file_menu = wx.Menu()
        file_menu.Append(101, '&Insert New Record\tCtrl+N', 'Insert a new workout record')
        file_menu.Append(102, '&Exit\tCtrl+Q', 'Close the program')
        file_menu.AppendSeparator()

        tools_menu = wx.Menu()
        #tools_menu.Append(201, '&Change Theme', "Change the current theme")

        submenu = wx.Menu()
        submenu.Append(301, 'White/Gray', kind = wx.ITEM_RADIO)
        submenu.Append(302, 'Blue/White', kind = wx.ITEM_RADIO)
        submenu.Append(303, 'Green/Blue', kind = wx.ITEM_RADIO)

        #tools_menu.AppendMenu(201, 'Change Theme', submenu)
        tools_menu.Append(202, '&Refresh Database\tF5', 'Re-display database with updated data')
        tools_menu.AppendSeparator()

        preferences_menu = wx.Menu()
        preferences_menu.AppendMenu(201, 'Change Theme', submenu)
        
        help_menu = wx.Menu()
        help_menu.Append(401, '&About Workout Manager', 'About this program')
        help_menu.AppendSeparator()

        self.Bind(wx.EVT_MENU, self.OnClose, id = 102)
        self.Bind(wx.EVT_MENU, self.callDialog, id = 401)
        self.Bind(wx.EVT_MENU, self.OnAdd, id = 101)
        #self.Bind(wx.EVT_MENU, MyListCtrl.populate_list, id = 202)

        menubar.Append(file_menu, "&File")
        menubar.Append(tools_menu, "&Tools")
        menubar.Append(preferences_menu, "&Preferences")
        menubar.Append(help_menu, "&Help")

        self.SetMenuBar(menubar)
        self.CreateStatusBar()

        ###########################################################

        self.list = MyListCtrl(panel, -1, style = wx.LC_REPORT, pos = (20, 30), size = (1110, 350))

        self.calculate_calories_button = wx.Button(panel, -1, label = "Caculate Calories", pos = (20, 400))
        #self.calculate_calories_button.Bind(wx.EVT_BUTTON, self.

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
        fields = ['date', 'pushups', 'chest_press', 'squats', 'lunges', 'vertical_press', 'pullups', 'dumbell_row', 'bicep_curls', 'preacher_curls',
                  'tricep_lifts', 'tricep_pushups', 'situps', 'crunches', 'planks']

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

        # if 'ok' button is pressed
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
        if (current_date != "" and pushups != "" and chest_press != "" and squats != "" and lunges != "" and vertical_press != "" and pullups != "" and
            dumbell_row != "" and bicep_curls != "" and preacher_curls != "" and tricep_lifts != "" and tricep_pushups != "" and situps != "" and
            crunches != "" and planks != ""):

            try:
                con = sqlite3.connect('workout.sqlite')  # connect to the database
                cur = con.cursor()
                
                sql = "INSERT INTO workout VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" # insert new data (parameterized query)

                cur.execute(sql, (current_date, pushups, chest_press, squats, lunges, vertical_press, pullups, dumbell_row, bicep_curls, 
                            preacher_curls, tricep_lifts, tricep_pushups, situps, crunches, planks))
                con.commit()


            except sqlite3.Error:
                dlg = wx.MessageDialog(self, str(error), 'Error occured')
                dlg.ShowModal()        # display error message
        
        dlg.Destroy() # destroy the dialog box






        

    def callDialog(self, event):                              
        dlg = OpenedDialog(1)
        btnID = dlg.ShowModal()

        if btnID == wx.ID_OK:
            dlg.Destroy()





class OpenedDialog(wx.Dialog):
    def __init__(self, d_state):
        wx.Dialog.__init__(self, None, title = "About Workout Manager", size = (370, 200))
                                        

        about_text = '''Workout Manager is a front-end program that manages \na database used to track the number and growth of \nspecific excersizes over time, as well as calculate \ncalories, and help plan for your future gains.'''

        self.about_label = wx.StaticText(self, -1, about_text, pos = (30, 30))

        self.ok_button = wx.Button(self, id = wx.ID_OK, pos = (150, 120))




if __name__ == "__main__":
    app = wx.App()
    MyFrame(None, -1, "Workout Manager v0.2")
    app.MainLoop()



















    
