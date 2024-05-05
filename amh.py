from tkinter import *
import tkinter.messagebox as tmsg
from datetime import datetime
from datetime import date


# THIS PROGRAM IS DEVELOPED BY HAMZA MAHMOOD(413603), ABDUL RAHMAN(408651) AND MOEEZ MASOOD(414737)
# DOCTOR'S DEFAULT PASSWORD IS 1234


# ALL FUNCTIONS

# GOING BACK TO MAIN
def back_to_main():
    main()


dot = "•"  # DECLARING A DOT


# WRITING FEES ON THE TEXT FILE

def writing_fees():
    if fees_var.get().strip().isnumeric():
        f = open("doctor_fees.txt", 'w')
        f.truncate()
        f.write(f"{fees_var.get().strip()}")
        f.close()
        j = open("doctor_fees.txt", 'r')
        line = j.readline()
        j.close()
        fees_var.set('')
        tmsg.showinfo("SUCCESS", "Fees updated successfully!")
        fees_label.config(text=f"Your current fees is Rs.{line}")
        return
    else:
        tmsg.showerror("ERROR", "Invalid Entries!")


# TOTAL EARNINGS
def total_earnings():
    rectangle_doc = Canvas(root, bg="lightblue", height=700, width=1300)
    rectangle_doc.place(x=249, y=130)
    rectangle_doc.create_rectangle(0, 0, 2500, 2500)
    rectangle_doc.create_line(0, 2, 5000, 2)
    Label(rectangle_doc, text="TOTAL EARNINGS:", font=('calibri', 30), bg="lightblue").place(x=400, y=20)
    Label(rectangle_doc, text="Date:", font=('calibre bold', 15), bg="lightblue").place(x=100, y=120)
    Label(rectangle_doc, text="Earnings:", font=('calibre bold', 15), bg="lightblue").place(x=350, y=120)
    sby = Scrollbar(rectangle_doc)
    sby.place(x=1200, y=150)

    # SHOWING EARNINGS ON THE SCREEN

    app_list = Listbox(rectangle_doc, height=20, width=110, font="calibri 15", yscrollcommand=sby.set, bg="lightblue")
    f = open("earnings.txt", 'r')
    f.seek(0)
    while 1:
        data = f.readline()
        app_list.insert(END, data + '\n')
        if not data:
            break
    f.close()
    app_list.place(x=100, y=150)
    sby.config(command=app_list.yview)
    Button(rectangle_doc, text="Logout", font="calibri 11", command=doctor_logout).place(x=0, y=2)


# TOTAL PATIENTS

def total_patients():
    rectangle_doc = Canvas(root, bg="lightblue", height=700, width=1300)
    rectangle_doc.place(x=249, y=130)
    rectangle_doc.create_rectangle(0, 0, 2500, 2500)
    rectangle_doc.create_line(0, 2, 5000, 2)
    Label(rectangle_doc, text="TOTAL PATIENTS:", font=('calibri', 30), bg="lightblue").place(x=400, y=20)
    Label(rectangle_doc, text="Date:", font=('calibre bold', 15), bg="lightblue").place(x=100, y=120)
    Label(rectangle_doc, text="Patients:", font=('calibre bold', 15), bg="lightblue").place(x=350, y=120)

    # SETTING A SCROLLBAR

    sby = Scrollbar(rectangle_doc)
    sby.place(x=1200, y=150)
    app_list = Listbox(rectangle_doc, height=20, width=110, font="calibri 15", yscrollcommand=sby.set, bg="lightblue")
    f = open("no_of_patients.txt", 'r')
    f.seek(0)
    while 1:
        data = f.readline()
        app_list.insert(END, data + '\n')
        if not data:
            break
    f.close()
    app_list.place(x=100, y=150)
    sby.config(command=app_list.yview)
    Button(rectangle_doc, text="Logout", font="calibri 11", command=doctor_logout).place(x=0, y=2)


# TO RESET THE SYSTEM

def reset_system():
    choice = tmsg.askquestion("RESET", "Are you sure you want to reset the system?")
    if choice == 'yes':
        f = open('appointment_timings.txt', 'r')
        count = 0
        while 1:
            line = f.readline()
            data = line.split()
            if '(reserved)' in data:
                count += 1
            if not line:
                break
        f.close()
        j = open("doctor_fees.txt", 'r')
        line = j.readline()
        j.close()
        d1 = date.today()
        d1 = d1.strftime("%d-%b-%Y")

        # WRITING THE TOTAL NO OF PATIENTS IN A DAY

        n = open("no_of_patients.txt", 'a')
        n.write(f"{d1}________________{str(count)}\n")
        n.close()

        # WRITING THE TOTAL EARNINGS IN A DAY

        m = open("earnings.txt", 'a')
        m.write(f"{d1}________________Rs:{str(count * int(line.strip()))}\n")
        m.close()
        tmsg.showinfo("RESET", "SYSTEM RESET SUCCESSFULLY !")
        return
    else:
        return


# SHOWING RECENT APPOINTMENTS TO THE PATIENT

def recent_appointments():
    rectangle_doc = Canvas(root, bg="lightblue", height=700, width=1300)
    rectangle_doc.place(x=249, y=130)
    rectangle_doc.create_line(0, 2, 5000, 2)
    Label(rectangle_doc, text="YOUR RECENT APPOINTMENTS", font=('calibri', 30), bg="lightblue").place(x=400, y=20)
    sby = Scrollbar(rectangle_doc)
    sby.place(x=1200, y=150)
    mylist = Listbox(rectangle_doc, height=20, width=110, font="calibri 15", yscrollcommand=sby.set, bg="lightblue")

    # SHOWING RECENT APPOINTMENTS ON THE SCREEN THROUGH TEXT FILE

    f = open('patient_detailed_records.txt', 'r')
    app = 0
    while 1:
        index = 0
        data = f.readline()
        data1 = data.split('******')
        if pat_cnic_var.get().strip() in data1:
            app += 1
            mylist.insert(END, ' ')
            mylist.insert(END, f"APPOINTMENT {app} :-\n")
            for i in data1:
                detail_list = ['CNIC:', 'NAME:', 'MOBILE no:', 'DATE', 'TIME:', 'DISEASE:', 'PRESCRIPTION:', 'HEIGHT:',
                               'BLOOD GROUP:', 'WEIGHT:', 'Age:']
                mylist.insert(END, f"{detail_list[index]} {i}\n")
                index += 1
        if not data:
            break
    f.close()
    mylist.place(x=100, y=150)
    sby.config(command=mylist.yview)
    Button(rectangle_doc, text="Logout", font="calibri 11", command=patient_logout).place(x=0, y=2)


# Logging out doctor

def doctor_logout():
    choice = tmsg.askquestion("Log out", "Do you want to logout?")
    if choice == 'yes':
        doctor()
    else:
        return


# IF DOCTOR WANTS TO CHANGE HIS FEES

def change_fees():
    rectangle_doc = Canvas(root, bg="lightblue", height=700, width=1300)
    rectangle_doc.place(x=249, y=130)
    rectangle_doc.create_rectangle(0, 0, 2500, 2500)
    rectangle_doc.create_line(0, 2, 5000, 2)
    Label(rectangle_doc, text="CURRENT FEES:", font=('calibre', 30), bg="lightblue").place(x=400, y=20)

    # SHOWING THE CURRENT FEES OF DOCTOR

    f = open("doctor_fees.txt", "r")
    f.seek(0)
    line = f.readline()
    f.close()
    global fees_label
    fees_label = Label(rectangle_doc, text=f"Your current fees is Rs.{line}", font=('calibre bold', 25), bg="lightblue")
    fees_label.place(x=50, y=150)
    Label(rectangle_doc, text=f"____________________________________________________________", font=('calibre bold', 10)
          , bg="lightblue").place(x=50, y=185)
    line = Canvas(rectangle_doc, width=1300, height=5, bg='black')
    line.place(x=0, y=250)
    line.create_line(0, 10, 2500, 10, fill='black')

    # IF DOCTOR WANTS TO CHANGE THE FEES

    global fees_var
    fees_var = StringVar()
    Label(rectangle_doc, text="New Fees:", font=('calibri', 24), bg="lightblue").place(x=50, y=400)
    Entry(rectangle_doc, textvariable=fees_var, width=30, font=20).place(x=350, y=405)
    Label(rectangle_doc, text="CHANGE FEES:", font=('calibre', 30), bg="lightblue").place(x=400, y=300)
    Button(rectangle_doc, text="Change", font="calibri 11", command=writing_fees).place(x=630, y=434)
    Button(rectangle_doc, text="Logout", font="calibri 11", command=doctor_logout).place(x=0, y=2)


# LOGGING OUT PATIENT

def patient_logout():
    choice = tmsg.askquestion("Log out", "Do you want to logout?")
    if choice == 'yes':
        patient()
    else:
        return


# WRITING DETAILS ON TEXT FILE

def writing_details():
    d1 = date.today()
    d1 = d1.strftime("%d-%b-%Y")
    if str(cnic_det_var.get()).strip().isnumeric() and len(str(cnic_det_var.get().strip())) == 13:
        f = open('patient_app_record.txt', 'r')
        f.seek(0)
        flag = 0
        while 1:
            line = f.readline()
            data = line.split('******')
            if cnic_det_var.get().strip() in data and d1 in data:
                flag = 1
                f.close()
                break
            if not line:
                f.close()
                break
        if flag == 1:
            line = list(line)
            len1 = len(line)
            line[len1 - 1] = '*'
            line.append('*****')
            line = "".join(line)
            b = open("patient_detailed_records.txt", "a")
            b.write(
                f"{line}{disease_var.get().strip()}******{prescription_var.get().strip()}******{blood_group_var.get().strip()}******{height_var.get().strip()}******{weight_var.get().strip()}******{age_var.get().strip()}\n")
            b.close()
            tmsg.showinfo("DETAILS", "Details added successfully!")

            # SETTING THE ENTRIES EMPTY AGAIN

            disease_var.set('')
            prescription_var.set('')
            blood_group_var.set('')
            height_var.set('')
            weight_var.set('')
            cnic_det_var.set('')
            age_var.set('')
            return
        else:
            tmsg.showinfo("SORRY", "Patient not found!")
            return
    else:
        tmsg.showerror("ERROR", "Invalid entries!")
        return


# ADDING PRESCRIPTION DISEASE

def add_prescription_disease():
    rectangle_doc = Canvas(root, bg="lightblue", height=700, width=1300)
    rectangle_doc.place(x=249, y=130)
    rectangle_doc.create_rectangle(0, 0, 2500, 2500)
    rectangle_doc.create_line(0, 2, 5000, 2)
    global weight_var
    global blood_group_var
    global height_var
    global prescription_var
    global disease_var
    global cnic_det_var
    global age_var

    # INITIALIZING THE STRING VARIABLES

    weight_var = StringVar()
    blood_group_var = StringVar()
    height_var = StringVar()
    prescription_var = StringVar()
    disease_var = StringVar()
    cnic_det_var = StringVar()
    age_var = StringVar()
    Label(rectangle_doc, text="CNIC:", font=('calibri', 24), bg="lightblue").place(x=50, y=100)
    Label(rectangle_doc, text="Disease:", font=('calibri', 24), bg="lightblue").place(x=50, y=150)
    Label(rectangle_doc, text="Prescription:", font=('calibri', 24), bg="lightblue").place(x=50, y=200)
    Label(rectangle_doc, text="Height:", font=('calibri', 24), bg="lightblue").place(x=50, y=250)
    Label(rectangle_doc, text="Blood group:", font=('calibri', 24), bg="lightblue").place(x=50, y=300)
    Label(rectangle_doc, text="Weight:", font=('calibri', 24), bg="lightblue").place(x=50, y=350)
    Label(rectangle_doc, text="Age:", font=('calibri', 24), bg="lightblue").place(x=50, y=400)
    Label(rectangle_doc, text="Add Prescription etc :", font=('calibri', 30), bg="lightblue").place(x=400, y=20)

    # MAKING ENTRIES FOR THE DETAILS

    cnic_det_entry = Entry(rectangle_doc, textvariable=cnic_det_var, width=30, font=20).place(x=280, y=110)
    disease_entry = Entry(rectangle_doc, textvariable=disease_var, width=30, font=20).place(x=280, y=160)
    prescription_entry = Entry(rectangle_doc, textvariable=prescription_var, width=30, font=20).place(x=280, y=210)
    blood_group_entry = Entry(rectangle_doc, textvariable=blood_group_var, width=30, font=20).place(x=280, y=260)
    height_entry = Entry(rectangle_doc, textvariable=height_var, width=30, font=20).place(x=280, y=310)
    weight_entry = Entry(rectangle_doc, textvariable=weight_var, width=30, font=20).place(x=280, y=360)
    age_entry = Entry(rectangle_doc, textvariable=age_var, width=30, font=20).place(x=280, y=410)
    Button(rectangle_doc, text='Add', font="calibri 11", command=writing_details).place(x=578, y=440)
    Button(rectangle_doc, text="Logout", font="calibri 11", command=doctor_logout).place(x=0, y=2)


# AVAILABLE APPOINTMENTS

def available_appointments():
    rectangle_doc = Canvas(root, bg="lightblue", height=700, width=1300)
    rectangle_doc.place(x=249, y=130)
    rectangle_doc.create_rectangle(0, 0, 2500, 2500)
    rectangle_doc.create_line(0, 2, 5000, 2)
    Label(rectangle_doc, text="AVAILABLE APPOINTMENTS:", font=('calibri', 30), bg="lightblue").place(x=400, y=20)
    sby = Scrollbar(rectangle_doc)
    sby.place(x=1200, y=150)
    app_list = Listbox(rectangle_doc, height=20, width=110, font="calibri 15", yscrollcommand=sby.set, bg="lightblue")

    # SHOWING RECENT APPOINTMENTS ON THE SCREEN THROUGH A TEXT FILE

    f = open("appointment_timings.txt", 'r')
    f.seek(0)
    while 1:
        data = f.readline()
        app_list.insert(END, data + '\n')
        if not data:
            break
    f.close()
    app_list.place(x=100, y=150)
    sby.config(command=app_list.yview)
    Button(rectangle_doc, text="Logout", font="calibri 11", command=doctor_logout).place(x=0, y=2)


# WRITING APPOINTMENTS IN THE TEXT FILE

def appointment_writing():
    if str(cnic_app_var.get()).strip().isnumeric() and len(str(cnic_app_var.get().strip())) == 13 and str(
            appointment_var.get().strip()).isnumeric():
        flag = 0
        l = open('appointment_timings.txt', 'r+')
        l.seek(0)
        while 1:
            app = l.readline()
            app1 = app.split()
            if appointment_var.get().strip() in app1 and '(reserved)' not in app1:
                cursor_location = l.tell()
                l.seek(cursor_location - 12)
                l.write("(reserved)")
                l.close()
                time_today = datetime.now()
                d1 = time_today.strftime('%d-%b-%Y******%I:%M:%S_%p')
                f = open('patient_app_record.txt', 'a')
                f.write(f'{cnic_app_var.get()}******{name_app_var.get()}******{mob_app_var.get()}******{d1}\n')
                f.close()
                flag = 1
                break
            if not app:
                tmsg.showerror("ERROR", "Invalid Entries!")
                break
            if appointment_var.get() in app1 and '(reserved)' in app1:
                tmsg.showinfo('SORRY', 'Appointment already reserved!')
                break
        if flag == 1:
            tmsg.showinfo("APPOINTMENT", 'Appointment reserved successfully!')
            cnic_app_var.set('')
            name_app_var.set('')
            mob_app_var.set('')
            appointment_var.set('')
            appointment_list.delete(0, END)
            f = open("appointment_timings.txt", 'r')
            f.seek(0)
            while 1:
                data = f.readline()
                appointment_list.insert(END, data + '\n')
                if not data:
                    break
            f.close()

        return
    else:
        tmsg.showerror("ERROR", 'Invalid entries!')
        return


# TO CHANGE THE APPOINTMENT TIMINGS

def appointment_update():
    if str(start_time.get().strip()).isnumeric() and str(end_time.get().strip()).isnumeric() and int(
            start_time.get().strip()) <= 24 and int(end_time.get().strip()) > int(start_time.get().strip()):
        start = int(start_time.get().strip())
        end = int(end_time.get().strip())
        f = open('appointment_timings.txt', 'w+')
        f.seek(0)
        f.truncate()
        f.seek(0)
        temp = start
        count = 1
        for n in range((end - start)):
            time_count = '00'
            for i in range(4):
                if time_count != 45:
                    f.write(
                        f"{count} . {str(temp)}:{str(time_count)} to {str(temp)}:{str(int(time_count) + 15)} ----------\n")
                else:
                    f.write(f"{count} . {str(temp)}:{str(time_count)} to {str(temp + 1)}:00 ----------\n")

                time_count = int(time_count) + 15
                count = count + 1
            temp = temp + 1
        f.close()
        tmsg.showinfo("TIMINGS", "Appointment timings updated successfully!")
        start_time.set('')
        end_time.set('')
        return
    else:
        tmsg.showerror("ERROR", "Invalid entries!")
        return


# TO ADD TIMING OF DOCTOR

def add_timing():
    doctor_rectangle = Canvas(root, bg="lightblue", height=700, width=1300)
    doctor_rectangle.place(x=249, y=130)
    doctor_rectangle.create_rectangle(0, 0, 2500, 2500)
    doctor_rectangle.create_line(0, 2, 5000, 2)
    Label(text="Update timings for tomorrow:", font=("calibri", 35), bg='lightblue').place(x=500, y=150)
    global start_time
    global end_time
    start_time = StringVar()
    end_time = StringVar()
    Label(doctor_rectangle, text="From:", font=('calibri', 24), bg="lightblue").place(x=50, y=200)
    Label(doctor_rectangle, text="To:", font=('calibri', 24), bg="lightblue").place(x=300, y=200)
    Entry(doctor_rectangle, textvariable=start_time, width=10, font=20).place(x=150, y=205)
    Entry(doctor_rectangle, textvariable=end_time, width=10, font=20).place(x=400, y=205)
    Button(doctor_rectangle, text="Update", font="calibri 11", command=appointment_update).place(x=530, y=205)
    Button(doctor_rectangle, text="Logout", font="calibri 11", command=doctor_logout).place(x=0, y=2)


# FIXING APPOINTMENT FOR PATIENT

def fix_appointment():
    doctor_rectangle = Canvas(root, bg="lightblue", height=700, width=1300)
    doctor_rectangle.place(x=249, y=130)
    doctor_rectangle.create_rectangle(0, 0, 2500, 2500)
    doctor_rectangle.create_line(0, 2, 5000, 2)
    Label(text="PATIENT DATA ENTRY", font=("calibri", 35), bg='lightblue').place(x=500, y=150)
    Label(doctor_rectangle, text="CNIC:", font=('calibri', 24), bg="lightblue").place(x=50, y=100)
    Label(doctor_rectangle, text="Name:", font=('calibri', 24), bg="lightblue").place(x=50, y=150)
    Label(doctor_rectangle, text="Mobile number:", font=('calibri', 24), bg="lightblue").place(x=50, y=200)
    Label(doctor_rectangle, text="Appointment no:", font=('calibri', 24), bg="lightblue").place(x=50, y=250)
    global cnic_app_var
    global name_app_var
    global mob_app_var
    global appointment_var
    global cnic_app_entry
    global name_app_entry
    global mob_app_entry

    cnic_app_var = StringVar()
    name_app_var = StringVar()
    appointment_var = StringVar()
    mob_app_var = StringVar()
    cnic_app_entry = Entry(doctor_rectangle, textvariable=cnic_app_var, width=30, font=20)
    cnic_app_entry.place(x=280, y=110)
    name_app_entry = Entry(doctor_rectangle, textvariable=name_app_var, width=30, font=20)
    name_app_entry.place(x=280, y=160)
    mob_app_entry = Entry(doctor_rectangle, textvariable=mob_app_var, width=30, font=20)
    mob_app_entry.place(x=280, y=210)
    app_entry = Entry(doctor_rectangle, textvariable=appointment_var, width=30, font=20)
    app_entry.place(x=280, y=260)
    Label(doctor_rectangle, text="Available appointments:", font=('calibri', 24), bg="lightblue").place(x=700, y=100)
    Button(doctor_rectangle, text="Submit", font="calibri 11", command=appointment_writing).place(x=557, y=290)
    sb = Scrollbar(doctor_rectangle)
    sb.place(x=1150, y=150)
    global appointment_list
    appointment_list = Listbox(doctor_rectangle, height=20, width=45, font="calibri 15", yscrollcommand=sb.set,
                               bg="lightblue")
    f = open("appointment_timings.txt", 'r')
    f.seek(0)
    while 1:
        data = f.readline()
        appointment_list.insert(END, data + '\n')
        if not data:
            break
    f.close()
    appointment_list.place(x=700, y=150)
    sb.config(command=appointment_list.yview())
    Button(doctor_rectangle, text="Logout", font="calibri 11", command=patient_logout).place(x=0, y=2)


# PATIENT'S PAGE

def patient_page():
    rectangle_doc = Canvas(root, bg="lightblue", height=700, width=1300)
    rectangle_doc.place(x=249, y=130)
    rectangle_doc.create_line(0, 2, 5000, 2)
    frame = Canvas(root, height=800, width=247, bg="NavyBlue")
    frame.place(x=0, y=0)
    b1 = Button(frame, fg='black', text="Fix Appointment", font=('Calibri', 20), width=17, command=fix_appointment)
    b2 = Button(frame, fg='black', text="Recent Appointments", font=('Calibri', 20), width=17,
                command=recent_appointments)
    b1.place(x=0, y=190)
    b2.place(x=0, y=250)
    Button(rectangle_doc, text="Logout", font="calibri 11", command=patient_logout).place(x=0, y=2)


# PATIENT'S VERIFICATION

def patient_verification():
    flag = 0
    if str(pat_cnic_var.get()).isnumeric() and len(str(pat_cnic_var.get().strip())) == 13:
        j = open('patient_accounts.txt', 'r')
        j.seek(0)
        while 1:
            data = j.readline()
            data1 = data.split('******')
            if pat_cnic_var.get().strip() == data1[0] and pat_pass_var.get().strip() == data1[1].strip('\n'):
                flag = 1
                break
            if not data:
                tmsg.showinfo("Login", "Patient not found!")
                break
        j.close()
        if flag == 1:
            patient_page()
        return
    else:
        tmsg.showerror("Login", "Invalid entries!")
        return


# CREATING PATIENT'S ACCOUNT

def create_account():
    flag = 1
    c = open('patient_accounts.txt', 'a+')
    if str(new_pat_cnic.get()).strip().isnumeric() and len(
            str(new_pat_cnic.get().strip())) == 13 and '*' not in new_pat_pass.get().strip():
        c.seek(0)
        while 1:
            line = c.readline()
            data1 = line.split('******')
            if not line:
                break
            if new_pat_cnic.get().strip() == data1[0].strip():
                flag = 0
                break

        if flag == 0:
            tmsg.showinfo("Account", "Account already exists!")
            new_pat_cnic.set('')
            new_pat_pass.set('')
            return
        else:
            c.write(f"{new_pat_cnic.get().strip()}******{new_pat_pass.get().strip()}\n")
            c.close()
            tmsg.showinfo("Account", "Account created successfully!")
            new_pat_cnic.set('')
            new_pat_pass.set('')
            return
    else:
        tmsg.showerror("Error", "Invalid Entries!\nYou cannot use * in your Password")
        return


# SEARCHING PATIENT BY DISEASE

def search_by_disease():
    flag = 0
    if disease_var.get().strip() == '':
        tmsg.showerror("Error", "Invalid Entries!")
        return
    app_list.delete(0, END)
    f = open('patient_detailed_records.txt', 'r')
    patient_count = 0
    while 1:
        index = 0
        line = f.readline()
        if disease_var.get().lower().strip() in line.lower():
            flag = 1
            patient_count += 1
            data = line.split('******')
            app_list.insert(END, ' ')
            app_list.insert(END, f"PATIENT {patient_count} :-\n")
            for i in data:
                detail_list = ['CNIC:', 'NAME:', 'MOBILE no:', 'DATE:', 'TIME:', 'DISEASE:', 'PRESCRIPTION:', 'HEIGHT:',
                               'BLOOD GROUP:', 'WEIGHT:', 'Age:']
                app_list.insert(END, f"{detail_list[index]} {i}\n")
                index += 1
        if not line:
            break
    if flag == 0:
        tmsg.showinfo("Sorry", "Patient not found!")
    return


# SEARCHING BY CNIC

def search_by_cnic():
    flag = 0
    if len(str(cnic1_var.get().strip())) != 13:
        tmsg.showerror("Error", "Invalid Entries!")
        return
    app_list.delete(0, END)
    f = open('patient_detailed_records.txt', 'r')
    patient_count = 0
    while 1:
        index = 0
        line = f.readline()
        data = line.split('******')
        if cnic1_var.get().strip() in data:
            flag = 1
            patient_count += 1
            app_list.insert(END, ' ')
            app_list.insert(END, f"APPOINTMENT {patient_count} :-\n")
            for i in data:
                detail_list = ['CNIC:', 'NAME:', 'MOBILE no:', 'DATE:', 'TIME:', 'DISEASE:', 'PRESCRIPTION:', 'HEIGHT:',
                               'BLOOD GROUP:', 'WEIGHT:', 'Age:']
                app_list.insert(END, f"{detail_list[index]} {i}\n")
                index += 1
        if not line:
            break
    if flag == 0:
        tmsg.showinfo("Sorry", "Patient not found!")
    return


# SEARCHING PATIENT HISTORY

def search_button():
    search_rectangle = Canvas(root, bg="lightblue", height=700, width=1300)
    search_rectangle.place(x=249, y=130)
    search_rectangle.create_rectangle(0, 0, 2500, 2500)
    search_rectangle.create_line(0, 2, 5000, 2)
    Label(search_rectangle, text="SEARCH\nBY CNIC:", font=('calibri', 24), bg='lightblue').place(x=50, y=20)
    Label(search_rectangle, text="SEARCH\n   BY DISEASE:", font=('calibri', 24), bg='lightblue').place(x=520, y=20)
    global cnic1_var
    global disease_var
    global cnic1_entry
    global disease_entry
    cnic1_var = StringVar()
    disease_var = StringVar()
    cnic1_entry = Entry(search_rectangle, textvariable=cnic1_var, width=30, font=20)
    cnic1_entry.place(x=200, y=40)
    disease_entry = Entry(search_rectangle, textvariable=disease_var, width=30, font=20)
    disease_entry.place(x=700, y=40)
    Button(search_rectangle, text="Search", font="calibri 11", command=search_by_disease).place(x=980, y=70)
    Button(search_rectangle, text="Search", font="calibri 11", command=search_by_cnic).place(x=480, y=70)
    Button(search_rectangle, text="Logout", font="calibri 11", command=doctor_logout).place(x=0, y=2)
    sby = Scrollbar(search_rectangle)
    sby.place(x=1200, y=150)
    global app_list
    app_list = Listbox(search_rectangle, height=20, width=110, font="calibri 15", yscrollcommand=sby.set,
                       bg="lightblue")
    app_list.place(x=100, y=150)
    sby.config(command=app_list.yview)


# DOCTOR'S PAGE

def doctor_page():
    doctor_rectangle = Canvas(root, bg="lightblue", height=700, width=1300)
    doctor_rectangle.place(x=249, y=130)
    doctor_rectangle.create_rectangle(0, 0, 2500, 2500)
    doctor_rectangle.create_line(0, 2, 5000, 2)
    frame = Canvas(root, height=800, width=247, bg="NavyBlue")
    frame.place(x=0, y=0)
    b1 = Button(fg='black', text="Add timings", width=17, font=('Calibri', 20), command=add_timing)
    b1.place(x=0, y=205)
    b2 = Button(fg='black', text="Search Patient History", width=17, font=('Calibri', 20), command=search_button)
    b2.place(x=0, y=265)
    b3 = Button(fg="black", text="Available slots\nfor appointments", width=17, font=('Calibri', 20),
                command=available_appointments)
    b3.place(x=0, y=325)
    b5 = Button(fg="black", text="Total Patients", width=17, font=('Calibri', 20), command=total_patients)
    b5.place(x=0, y=418)
    b6 = Button(fg="black", text="Total Earnings", width=17, font=('Calibri', 20), command=total_earnings)
    b6.place(x=0, y=478)
    b7 = Button(fg='black', text="Reset system", width=17, font=("Calibri", 20), command=reset_system)
    b7.place(x=0, y=538)
    b8 = Button(fg='black', text="Add Prescription/\nDisease", width=17, font=("Calibri", 20),
                command=add_prescription_disease)
    b9 = Button(fg='black', text="Change Fees", width=17, font=("Calibri", 20), command=change_fees)
    b8.place(x=0, y=598)
    b9.place(x=0, y=691)
    Button(doctor_rectangle, text="Logout", font="calibri 11", command=doctor_logout).place(x=0, y=2)


# CHANGING DOCTOR'S PASSWORD

def change_doc_pass():
    f = open("doctor_password.txt", 'r')
    f.seek(0)
    docpassword = f.readline()
    f.seek(0)
    if old_pass.get().strip() == docpassword.strip():
        f.close()
        n = open('doctor_password.txt', 'w+')
        n.close()
        m = open("doctor_password.txt", 'w')
        m.seek(0)
        m.write(new_pass.get().strip())
        m.close()
        tmsg.showinfo("Password", "Password changed successfully!")
        old_pass.set('')
        new_pass.set('')
    else:
        f.close()
        tmsg.showinfo("Password", "Password did not match!")


# DOCTOR LOGIN

def doctor_login():
    n = open('doctor_password.txt', 'r')
    n.seek(0)
    doc_pass_data = n.readline()
    if doc_password.get() == doc_pass_data.strip():
        doctor_page()
    else:
        tmsg.showinfo("Login", "Incorrect password!")
    n.close()


# If DOCTOR

def doctor():
    root.title("Doctor Log in")
    rectangle_doc = Canvas(root, bg="lightblue", height=700, width=1300)
    rectangle_doc.place(x=249, y=130)
    rectangle_doc.create_rectangle(0, 0, 2500, 2500)
    rectangle_doc.create_line(0, 2, 5000, 2)
    frame = Canvas(root, height=800, width=247, bg="NavyBlue")
    frame.place(x=0, y=0)
    Label(rectangle_doc, text="Password:", font=('calibri', 24), bg="lightblue").place(x=50, y=150)
    global doc_password
    global pass_entry
    global old_pass
    global new_pass
    doc_password = StringVar()
    pass_entry = Entry(rectangle_doc, textvariable=doc_password, width=30, font=20, show=dot)
    pass_entry.place(x=350, y=160)
    Button(rectangle_doc, text="Log in", font="calibri 11", command=doctor_login).place(x=635, y=190)
    Label(rectangle_doc, text="DOCTOR LOGIN", font=('calibri', 30), bg="lightblue").place(x=350, y=20)

    # If DOCTOR WANTS TO CHANGE PASSWORD

    line = Canvas(rectangle_doc, width=1300, height=5, bg='black')
    line.place(x=0, y=250)
    line.create_line(0, 10, 2500, 10, fill='black')
    Label(rectangle_doc, text="CHANGE PASSWORD", font=('calibri', 30), bg="lightblue").place(x=300, y=300)
    Label(rectangle_doc, text="Old Password:", font=('calibri', 24), bg="lightblue").place(x=50, y=400)
    Label(rectangle_doc, text="New Password:", font=('calibri', 24), bg="lightblue").place(x=50, y=450)
    old_pass = StringVar()
    new_pass = StringVar()
    Entry(rectangle_doc, textvariable=old_pass, width=30, font=20, show=dot).place(x=350, y=405)
    Entry(rectangle_doc, textvariable=new_pass, width=30, font=20, show=dot).place(x=350, y=455)
    Button(rectangle_doc, text="Change", font="calibri 11", command=change_doc_pass).place(x=625, y=487)
    Button(rectangle_doc, text="Back", font="calibri 11", command=back_to_main).place(x=0, y=2)


# IF PATIENT

def patient():
    root.title("Patient Log in")
    rectangle_doc = Canvas(root, bg="lightblue", height=700, width=1300)
    rectangle_doc.place(x=249, y=130)
    rectangle_doc.create_rectangle(0, 0, 2500, 2500)
    rectangle_doc.create_line(0, 2, 5000, 2)
    frame = Canvas(root, height=800, width=247, bg="NavyBlue")
    frame.place(x=0, y=0)
    Label(rectangle_doc, text="Password:", font=('calibri', 24), bg="lightblue").place(x=50, y=150)
    Label(rectangle_doc, text="CNIC:", font=('calibri', 24), bg="lightblue").place(x=50, y=100)
    global pat_pass_var
    global pat_cnic_var
    pat_pass_var = StringVar()
    pat_cnic_var = StringVar()
    Entry(rectangle_doc, textvariable=pat_pass_var, width=30, font=20, show=dot).place(x=350, y=160)
    Entry(rectangle_doc, textvariable=pat_cnic_var, width=30, font=20).place(x=350, y=110)
    Button(rectangle_doc, text="Log in", font="calibri 11", command=patient_verification).place(x=635, y=192)
    Label(rectangle_doc, text="PATIENT LOGIN", font=('calibri', 30), bg="lightblue").place(x=400, y=20)

    # If PATIENT WANTS TO CREATE ACCOUNT

    global new_pat_cnic
    global new_pat_pass

    # CREATING A LINE BETWEEN THE TWO ENTRIES

    line = Canvas(rectangle_doc, width=1300, height=5, bg='black')
    line.place(x=0, y=250)
    line.create_line(0, 10, 2500, 10, fill='black')
    Label(rectangle_doc, text="DON'T HAVE AN  ACCOUNT? CREATE ONE.", font=('calibri', 30), bg="lightblue").place(x=200,
                                                                                                                 y=300)
    Label(rectangle_doc, text="CNIC:", font=('calibri', 24), bg="lightblue").place(x=50, y=400)
    Label(rectangle_doc, text="Password:", font=('calibri', 24), bg="lightblue").place(x=50, y=450)
    new_pat_cnic = StringVar()
    new_pat_pass = StringVar()
    Entry(rectangle_doc, textvariable=new_pat_cnic, width=30, font=20).place(x=350, y=405)
    Entry(rectangle_doc, textvariable=new_pat_pass, width=30, font=20, show=dot).place(x=350, y=455)
    Button(rectangle_doc, text="Create", font="calibri 11", command=create_account).place(x=630, y=487)
    Button(rectangle_doc, text="Back", font="calibri 11", command=back_to_main).place(x=0, y=2)


# MAIN PAGE  - Doctor or Patient?


def main():
    frame = Canvas(root, height=800, width=247, bg="NavyBlue")
    frame.place(x=0, y=0)
    text_label = Label(text="CLINIC MANAGEMENT SYSTEM ", font=("calibre", 30))
    text_label.place(x=645, y=30)
    rectangle_doc = Canvas(root, bg="lightblue", height=700, width=1300)
    rectangle_doc.place(x=249, y=130)
    rectangle_doc.create_rectangle(0, 0, 2500, 2500)
    rectangle_doc.create_line(0, 2, 5000, 2)
    Label(root, text="INNOVATING THE TECH                      ", font="calibre 15 bold", fg='NavyBlue').place(x=460,
                                                                                                               y=80)
    Label(root, text=" AMH  ", font=" calibre 40 bold", fg='NavyBlue').place(x=460, y=18)
    Button(rectangle_doc, text="DOCTOR", font="calibre 35", command=doctor).place(x=150, y=200)
    Button(rectangle_doc, text="PATIENT", font="calibre 35", command=patient).place(x=470, y=200)


# CREATING A TEMPORARY FUNCTION

def temp():
    # CREATING THE MAIN WINDOW

    global root
    root = Tk()
    root.geometry("1500x800")
    root.title("Doctor or Patient?")
    root.iconbitmap("doctor.ico")

    # ADDING THE LOGO IMAGE

    photo = PhotoImage(file='logo.png')
    photo_label = Label(image=photo)
    photo_label.place(x=300, y=5)
    main()
    root.mainloop()


temp()
