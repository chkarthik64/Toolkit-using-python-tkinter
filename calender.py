from tkinter import *
from tkcalendar import Calendar
 
class CalenderProg:
    # Create Object
    def __init__(self):
        self.root = Tk()
        
        # Set geometry
        self.root.geometry("400x400")
        
        # Add Calendar
        cal = Calendar(self.root, selectmode = 'day',
                    year = 2020, month = 5,
                    day = 22)
        
        cal.pack(pady = 20)
        
        def grad_date():
            date.config(text = "Selected Date is: " + cal.get_date())
        
        # Add Button and Label
        Button(self.root, text = "Get Date",
            command = grad_date).pack(pady = 20)
        
        date = Label(self.root, text = "")
        date.pack(pady = 20)
        
        # Execute Tkinter
        self.root.mainloop()
'''from tkinter import *
from tkcalendar import Calendar

class CalendarProg:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x400")

        self.cal = Calendar(self.root, date_pattern="yyyy-mm-dd")
        self.cal.pack(pady=20)

        Button(self.root, text="Get Date", command=self.get_selected_date).pack(pady=20)

        self.date_label = Label(self.root, text="")
        self.date_label.pack(pady=20)

        self.root.mainloop()

    def get_selected_date(self):
        selected_date = self.cal.get_date()
        self.date_label.config(text="Selected Date is: " + selected_date)

if __name__ == "__main__":
    calendar_program = CalendarProg()'''
