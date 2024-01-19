#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import xlrd
from tkinter import *
from xlutils.copy import copy
import smtplib

def new_booking(name, mobno, on, emailid):
    rb = xlrd.open_workbook("OBS.xls")
    wb = copy(rb)
    data = wb.get_sheet('Booking')
    first_sheet = rb.sheet_by_name('Booking')

    print("The Grounds That We Have Are")
    tg = int(input("1)Cricket\n2)Football\n3)Hockey\n4)Basketball\n5)Badminton"))
    if tg not in [1, 2, 3, 4, 5]:
        return

    month = int(input("Enter 10)October   11)November   12)December"))
    if month not in [10, 11, 12]:
        return

    ground = get_ground_name(tg)

    while True:
        print("Enter The Date on which you want {} ground".format(ground))
        reqdate = input()
        date = str(month) + '/' + str(reqdate) + '2019'
        rowv = int(reqdate)
        if month == 10:
            rowv += 1
        elif month == 11:
            rowv += 32
        elif month == 12:
            rowv += 62
        x = first_sheet.cell(rowv, tg).value
        if x == 'Vacant':
            print("The Date you choose is available for booking....")
            yn = int(input("1)Yes    2)No"))
            if yn == 1:
                z = mobno + name
                print(z)
                data.write(rowv, tg, z)
                print("Booking successful")
                sender = "Asdfgh@gmail.com"  # Our Email ID
                password = "Xyz@12365489"  # Our Password
                obj = smtplib.SMTP("smtp.gmail.com", 587)
                obj.starttls()
                obj.login(sender, password)
                obj.sendmail(sender, emailid,
                            "Dear " + name + ", Booking Succesful for " + ground + " ground for date " + reqdate + "/" + str(
                                month) + "/2024")
                obj.quit()
                wb.save("OBS.xls")
                break
            else:
                return
        else:
            print("Sorry The Date You Have Chosen Was Not Available.....")


def cancel_booking(name, mobno, emailid):
    print("Cancel Booking")
    rb = xlrd.open_workbook("OBS.xls")
    wb = copy(rb)
    data = wb.get_sheet('Booking')
    first_sheet = rb.sheet_by_name('Booking')

    print("The Grounds That We Have Are")
    tg = int(input("1)Cricket\n2)Football\n3)Hockey\n4)Basketball\n5)Badminton"))
    if tg not in [1, 2, 3, 4, 5]:
        return

    month = int(input("Enter 10)October   11)November   12)December"))
    if month not in [10, 11, 12]:
        return

    ground = get_ground_name(tg)

    while True:
        print("Enter The Date on which you want {} ground".format(ground))
        reqdate = input()
        date = str(month) + '/' + str(reqdate) + '2019'
        rowv = int(reqdate)
        if month == 10:
            rowv += 1
        elif month == 11:
            rowv += 32
        elif month == 12:
            rowv += 62
        x = first_sheet.cell(rowv, tg).value
        y = x[0:10:]
        print(y)
        if y == mobno:
            print("Do you Want To Proceed With Cancellation ....?")
            yn = int(input("1)Yes    2)No"))
            if yn == 1:
                data.write(rowv, tg, 'Vacant')
                print("Cancellation successful")
                sender = "Asdfgh@gmail.com"  # Our Email ID
                password = "Xyz@12365489"  # Our Password
                obj = smtplib.SMTP("smtp.gmail.com", 587)
                obj.starttls()
                obj.login(sender, password)
                obj.sendmail(sender, emailid,
                            "Dear " + name + ", Cancellation Successful for " + ground + " ground for date " + reqdate + "/" + str(
                                month) + "/2024")
                obj.quit()
                wb.save("OBS.xls")
                break
            else:
                return
        else:
            print("Sorry The Date You Have Given Wrong Info For Cancellation.....Please Start The Process From The Beginning......")
            break


def get_ground_name(tg):
    if tg == 1:
        return 'Cricket'
    elif tg == 2:
        return 'Football'
    elif tg == 3:
        return 'Hockey'
    elif tg == 4:
        return 'Basketball'
    else:
        return 'Badminton'


while True:
    import tkinter.messagebox

    tkinter.messagebox.showinfo("Welcome", " * * * * * Welcome To Online Play Ground Booking System * * * * *")

    ans = tkinter.messagebox.askquestion("New To Portal?")
    if ans == 'yes':
        on = 1

    else:
        on = 2

    ans1 = tkinter.messagebox.askquestion("New Booking?")
    if ans1 == 'yes':
        bc = 1
    else:
        bc = 2
    name = input("Please Enter Your Name::")
    mobno = input("Please Enter Your Mobile Number::")
    emailid = input("Please Enter Your Email ID::")

    if bc == 1:
        new_booking(name, mobno, on, emailid)
    elif bc == 2:
        cancel_booking(name, mobno, emailid)



# In[2]:


import unittest
import os
from unittest.mock import patch
from io import StringIO
from booking_system import new_booking, cancel_booking  # Adjust the module name accordingly

class TestBookingSystem(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = "test_OBS.xls"

    def tearDown(self):
        # Clean up the temporary file
        try:
            os.remove(self.temp_file)
        except OSError:
            pass

    def test_new_booking_successful(self):
        # Simulate user input
        user_input = "1\n10\n15\n1\n"

        # Redirect stdin to simulate user input
        with patch("builtins.input", side_effect=user_input.split("\n")):
            # Redirect stdout to capture print statements
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                new_booking("John Doe", "1234567890", 1, "john.doe@example.com", self.temp_file)

                # Verify that the output contains the expected success message
                self.assertIn("Booking successful", mock_stdout.getvalue())

    def test_cancel_booking_successful(self):
        # Simulate user input
        user_input = "1\n10\n15\n1\n"

        # Redirect stdin to simulate user input
        with patch("builtins.input", side_effect=user_input.split("\n")):
            # Redirect stdout to capture print statements
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                cancel_booking("John Doe", "1234567890", "john.doe@example.com", self.temp_file)

                # Verify that the output contains the expected success message
                self.assertIn("Cancellation successful", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()


# In[ ]:




