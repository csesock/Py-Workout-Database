import sqlite3, wx
import sys

connection1 = sqlite3.connect('workout.sqlite')
cursor1 = connection1.cursor()

workout = '''CREATE TABLE workout (
            Date DATETIME PRIMARY KEY,
            Push_Up INTEGER(3),
            Chest_Press INTEGER(3),
            Squats INTEGER(3),
            Lunges INTEGER(3),
            Vertical_Press INTEGER(3),
            Pullup INTEGER(3),
            Dumbell_Row INTEGER(3),
            Bicep_Curl INTEGER(3),
            Preacher_Curl INTEGER(3),
            Tricep_Lift INTEGER(3),
            Tricep_Pushup INTEGER(3),
            Situp INTEGER(3),
            Crunches INTEGER(3),
            Planks INTEGER(3)
        '''

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
        wx.StaticText(self, -1, 'Preacher Curls', pos = (180, 410))

        self.tricep_lifts = wx.TextCtrl(self, -1, pos = (50, 450))
        wx.StaticText(self, -1, 'Tricep Lifts', pos = (180, 450))

        self.tricep_pushups = wx.TextCtrl(self, -1, pos = (50, 490))
        wx.StaticText(self, -1, 'Tricep Pushups', pos = (180, 490))

        self.situps = wx.TextCtrl(self, -1, pos = (50, 530))
        wx.StaticText(self, -1, 'Situps', pos = (180, 530))

        self.crunches = wx.TextCtrl(self, -1, pos = (50, 580))
        wx.StaticText(self, -1, 'Crunches', pos = (180, 580))

        self.planks = wx.TextCtrl(self, -1, pos = (50, 620))
        wx.StaticText(self, -1, 'Planks', pos = (180, 620))

        ok_button = wx.Button(self, id = wx.ID_OK, pos = (50, 670))




# class to build the frame and data list for the program
class DataList(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (1200, 500))
        panel = wx.Panel(self, -1)
##        ico = wx.Icon("program3-icon.png")
##        self.SetIcon(ico)
        self.list = wx.ListCtrl(panel, -1, style = wx.LC_REPORT, pos = (20, 30), size = (1110, 350))

        # build the columns for the list control
        self.list.InsertColumn(0, 'Date', width = 80)
        self.list.InsertColumn(1, 'Push Ups', width = 70)
        self.list.InsertColumn(2, 'Chest Press', width = 90)
        self.list.InsertColumn(3, 'Squats', width = 60)
        self.list.InsertColumn(4, 'Lunges', width = 60)
        self.list.InsertColumn(5, 'Vertical Press', width = 90)
        self.list.InsertColumn(6, 'Pullups', width = 60)
        self.list.InsertColumn(7, 'Dumbell Row', width = 90)
        self.list.InsertColumn(8, 'Bicep Curl', width = 70)
        self.list.InsertColumn(9, 'Preacher Curl', width = 90)
        self.list.InsertColumn(10, 'Tricep Lift', width = 70)
        self.list.InsertColumn(11, 'Tricep Pushup', width = 95)
        self.list.InsertColumn(12, 'Situps', width = 50)
        self.list.InsertColumn(13, 'Crunches', width = 70)
        self.list.InsertColumn(14, 'Planks', width = 70)


        # build the buttons for the list control
        display_button = wx.Button(panel, -1, 'Display', size = (-1, 30), pos = (40, 410))
        display_button.Bind(wx.EVT_BUTTON, self.OnDisplay)
        
        insert_button = wx.Button(panel, -1,  'Insert Data', size = (-1, 30), pos = (150, 410))
        insert_button.Bind(wx.EVT_BUTTON, self.OnAdd)

        update_button = wx.Button(panel, -1, 'Update Data', size = (-1, 30), pos = (270, 410))
        update_button.Bind(wx.EVT_BUTTON, self.OnUpdate)
        
        close_button = wx.Button(panel, -1, 'Close', size =(-1, 30), pos = (380, 410))
        close_button.Bind(wx.EVT_BUTTON, self.OnClose)

        




    # display the database within the list control
    def OnDisplay(self, event):
        try:
            # delete all items from the list 
            self.list.DeleteAllItems()
            
            con = sqlite3.connect('workout.sqlite')
            cur = con.cursor()

            cur.execute('SELECT * FROM workout')
            result = cur.fetchall()
            
            for row in result:
                self.list.Append(row)

            cur.close()
            con.close()

        except sqlite3.Error:
            print("Error")


    def OnAdd(self, event):

        self.OnDisplay(None)
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

                self.OnDisplay(None) # re-display the database with new entry

            except sqlite3.Error:
                dlg = wx.MessageDialog(self, str(error), 'Error occured')
                dlg.ShowModal()        # display error message
        
        dlg.Destroy() # destroy the dialog box


    def OnUpdate(self, event):

        self.OnDisplay(None)

        # display combo box, prompt for date to edit

        dlg = MyDialog('Update Workout Data')
        btnID = dlg.ShowModal()
        date_to_edit = dlg.date.GetValue()

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

                sql2 = '''UPDATE workout 
                          SET Date = ?, 'Push Ups' = ?, 'Chest Press' = ?, Squats = ?, Lunges = ?, 'Vertical Press' = ?, Pullups = ?, 'Dumbell Row' = ?,
                          'Bicep Curl' = ?, 'Preacher Curl' = ?, 'Tricep Lift' = ?, 'Tricep Pushup' = ?, Situp = ?, Crunches = ?, Planks = ?
                          WHERE Date = date_to_edit'''

                cur.execute(sql2, (current_date, pushups, chest_press, squats, lunges, vertical_press, pullups, dumbell_row, bicep_curls, 
                            preacher_curls, tricep_lifts, tricep_pushups, situps, crunches, planks))
                con.commit()

                self.OnDisplay(None) # re-display the database with new entry

            except sqlite3.Error:
                dlg = wx.MessageDialog(self, str(error), 'Error occured')
                dlg.ShowModal()        # display error message
        
        dlg.Destroy() # destroy the dialog box
                

    def OnClose(self, event):
        self.Close()

        


if __name__ == '__main__':
    app = wx.App()
    dl = DataList(None, -1, 'Workout Database')
    dl.Show()
    app.MainLoop()

