## Written by: Chris Sesock
## on March 12th, 2020
##

import wx, sqlite3
import wx.lib.mixins.listctrl as mixlist

class MyListCtrl(wx.ListCtrl, mixlist.TextEditMixin, mixlist.ListCtrlAutoWidthMixin):

    def __init__(self, parent, id, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):

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
        
        self.DeleteAllItems()
 
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
