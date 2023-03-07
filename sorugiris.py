import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askyesno
from tkinter import filedialog
from PIL import Image, ImageOps, ImageTk, ImageFilter


import os
import openpyxl
import mysql.connector

mydb = mysql.connector.connect(host="sql7.freesqldatabase.com",
  port="3306",
  user="sql7602430",
  password="ePbVUdumsC",
  database="sql7602430"
)

#commit test edildi

def enter_data():
    question = question_entry.get("1.0", "end-1c")
    aopt = a_option_entry.get()
    bopt = b_option_entry.get()
    copt = c_option_entry.get()
    dopt = d_option_entry.get()
    correct = correct_answer_combobox.get()

    if len(question) == 0:
        tkinter.messagebox.showwarning(
            title="Kayıt Başarısız", message="Soru Boş Bırakılamaz")
    elif not aopt:
        tkinter.messagebox.showwarning(
            title="Kayıt Başarısız", message="A Şıkkı Boş Bırakılamaz")
    elif not bopt:
        tkinter.messagebox.showwarning(
            title="Kayıt Başarısız", message="B Şıkkı Boş Bırakılamaz")
    elif not copt:
        tkinter.messagebox.showwarning(
            title="Kayıt Başarısız", message="C Şıkkı Boş Bırakılamaz")
    elif not dopt:
        tkinter.messagebox.showwarning(
            title="Kayıt Başarısız", message="D Şıkkı Boş Bırakılamaz")
    elif not correct:
        tkinter.messagebox.showwarning(
            title="Kayıt Başarısız", message="Doğru Şık Boş Bırakılamaz")
    else:        
        print("Soru1:", question)
        print("A.", aopt, "B.", bopt)
        print("C.", copt, "D.", dopt)
        print("Doğru Yanıt:", correct)        
        query = unit_combobox.get()

        # 5. Sınıf

        if query == "1.Ünite: Güneş, Dünya ve Ay":
            
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif5unite1 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif5unite1 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()
            
            print(mycursor.rowcount, "record inserted.")

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "2.Ünite: Canlılar Dünyası":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif5unite2 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif5unite2 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "3.Ünite: Kuvvetin Ölçülmesi ve Sürtünme":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif5unite3 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif5unite3 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "4.Ünite: Madde ve Değişim":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif5unite4 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif5unite4 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "5.Ünite: Işığın Yayılması":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif5unite5 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif5unite5 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "6.Ünite: İnsan ve Çevre":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif5unite6 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif5unite6 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "7.Ünite: Elektrik Devre Elemanları":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif5unite7 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif5unite7 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        # 6. Sınıf

        elif query == "1.Ünite: Güneş Sistemi ve Tutulmalar":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif6unite1 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif6unite1 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "2.Ünite: Vücudumuzdaki Sistemler":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif6unite2 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif6unite2 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "3.Ünite: Kuvvet ve Hareket":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif6unite3 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif6unite3 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "4.Ünite: Madde ve Isı":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif6unite4 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif6unite4 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "5.Ünite: Ses ve Özellikleri":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif6unite5 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif6unite5 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "6.Ünite: Vücudumuzdaki Sistemler ve Sağlığı":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif6unite6 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif6unite6 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "7.Ünite: Elektriğin İletimi":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif6unite7 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif6unite7 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        # 7. Sınıf

        elif query == "1.Ünite: Güneş Sistemi ve Ötesi":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif7unite1 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif7unite1 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()
            
            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "2.Ünite: Hücre ve Bölünmeler":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif7unite2 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif7unite2 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "3.Ünite: Kuvvet ve Enerji":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif7unite3 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif7unite3 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "4.Ünite: Saf Madde ve Karışımlar":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif7unite4 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif7unite4 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "5.Ünite: Işığın Madde ile Etkileşimi":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif7unite5 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif7unite5 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "6.Ünite: Canlılarda Üreme, Büyüme ve Gelişme":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif7unite6 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif7unite6 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "7.Ünite: Elektrik Devreleri":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif7unite7 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif7unite7 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        # 8. Sınıf

        elif query == "1.Ünite: Mevsimler ve İklim":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif8unite1 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif8unite1 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "2.Ünite: DNA ve Genetik Kod":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif8unite2 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif8unite2 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "3.Ünite: Basınç":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif8unite3 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif8unite3 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

        elif query == "4.Ünite: Madde ve Endüstri":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif8unite4 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif8unite4 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "5.Ünite: Basit Makineler":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif8unite5 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif8unite5 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "6.Ünite: Enerji Dönüşümleri ve Çevre Bilimi":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif8unite6 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif8unite6 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")
            
        elif query == "7.Ünite: Elektrik Yükleri ve Elektrik Enerjisi":
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS sinif8unite7 (question VARCHAR(45), aopt VARCHAR(45), bopt VARCHAR(45), copt VARCHAR(45), dopt VARCHAR(45), correct VARCHAR(45))")
            
            sql = "INSERT INTO sinif8unite7 (question, aopt, bopt, copt, dopt, correct) VALUES(%s,%s,%s,%s,%s,%s)" 
            data_insert_tuple = (question, aopt, bopt, copt, dopt, correct)
            
            mycursor.execute(sql,data_insert_tuple)
            mydb.commit()

            tkinter.messagebox.showwarning(
                title="Başarılı", message="Kayıt Başarılı")        
        
        #Error

        else:
            tkinter.messagebox.showwarning(title="Kayıt Başarısız", message="Ünite Seçiniz")

        question_entry.delete('1.0',"end")
        a_option_entry.delete('0',"end")
        b_option_entry.delete('0',"end")
        c_option_entry.delete('0',"end")
        d_option_entry.delete('0',"end")
        correct_answer_combobox.current(0)
        
        

def confirm():
    answer = askyesno(title='Çıkış',
                    message='Çıkmak İstediğinden Emin Misin?')
    if answer:
        window.destroy()

# Window
window = tkinter.Tk()
window.title("Soru Giris Ekranı")

# Frame
frame = tkinter.Frame(window, bd=10)
frame.pack(side="left", fill="y")

frameRight = tkinter.Frame(window, bd=10)
frameRight.pack()

def pick_grade(e):
    if grade_combobox.get() == "5":
        unit_combobox.config(value=unitsfive)
        unit_combobox.current(0)
    elif grade_combobox.get() == "6":
        unit_combobox.config(value=unitssix)
        unit_combobox.current(0)
    elif grade_combobox.get() == "7":
        unit_combobox.config(value=unitsseven)
        unit_combobox.current(0)
    elif grade_combobox.get() == "8":
        unit_combobox.config(value=unitseight)
        unit_combobox.current(0)
    elif grade_combobox.get() == "Lütfen sınıf seçiniz":
        unit_combobox.config(value=gradeempty)
        unit_combobox.current(0)


file_path = ""

def add_image():
    global file_path
    file_path = filedialog.askopenfilename(initialdir="")
    image = Image.open(file_path)
    width, height = int(image.width / 10), int(image.height / 10)
    image = image.resize((width,height), Image.LANCZOS)
    blob_image_canvas.config(width=image.width, height= image.height)
    image = ImageTk.PhotoImage(image)
    blob_image_canvas.image = image
    blob_image_canvas.create_image(0,0, image = image, anchor="nw")
    
        
# Sınıf-Ünite Seçim
grade_unit_frame = tkinter.Frame(frame)
grade_unit_frame.grid(row=0, column=0, padx=20, pady=0, sticky="news")

# Sınıf listesi
grades = ["Lütfen Sınıf Seçiniz", "5", "6", "7", "8"]

# Üniteler listesi
unitsfive = ["Lütfen Ünite Seçiniz","1.Ünite: Güneş, Dünya ve Ay", "2.Ünite: Canlılar Dünyası", "3.Ünite: Kuvvetin Ölçülmesi ve Sürtünme",
             "4.Ünite: Madde ve Değişim", "5.Ünite: Işığın Yayılması", "6.Ünite: İnsan ve Çevre", "7.Ünite: Elektrik Devre Elemanları"]
unitssix = ["Lütfen Ünite Seçiniz","1.Ünite: Güneş Sistemi ve Tutulmalar", "2.Ünite: Vücudumuzdaki Sistemler", "3.Ünite: Kuvvet ve Hareket",
            "4.Ünite: Madde ve Isı", "5.Ünite: Ses ve Özellikleri", "6.Ünite: Vücudumuzdaki Sistemler ve Sağlığı", "7.Ünite: Elektriğin İletimi"]
unitsseven = ["Lütfen Ünite Seçiniz","1.Ünite: Güneş Sistemi ve Ötesi", "2.Ünite: Hücre ve Bölünmeler", "3.Ünite: Kuvvet ve Enerji", "4.Ünite: Saf Madde ve Karışımlar",
              "5.Ünite: Işığın Madde ile Etkileşimi", "6.Ünite: Canlılarda Üreme, Büyüme ve Gelişme", "7.Ünite: Elektrik Devreleri"]
unitseight = ["Lütfen Ünite Seçiniz","1.Ünite: Mevsimler ve İklim", "2.Ünite: DNA ve Genetik Kod", "3.Ünite: Basınç", "4.Ünite: Madde ve Endüstri",
              "5.Ünite: Basit Makineler", "6.Ünite: Enerji Dönüşümleri ve Çevre Bilimi", "7.Ünite: Elektrik Yükleri ve Elektrik Enerjisi"]

gradeempty = ["Lütfen Ünite Seçiniz"]

# Sınıf Seçimi
grade_combobox = ttk.Combobox(grade_unit_frame, values=grades)
grade_combobox.current(0)
grade_combobox.grid(row=0, padx=5, pady=5)

# Atama
grade_combobox.bind("<<ComboboxSelected>>", pick_grade)

# Ünite Seçimi
unit_combobox = ttk.Combobox(grade_unit_frame, value=gradeempty, width=60)
unit_combobox.current(0)
unit_combobox.grid(row=1, padx=5, pady=5)



#BLOB İmaj Giriş FRAME
blob_image_frame = tkinter.LabelFrame(frameRight, text="Görüntü", width=200, height=200, labelanchor='n', bd=0)
blob_image_frame.grid(row=1)

#BLOB İmaj Giriş
blob_image_upload_button = tkinter.Button(blob_image_frame, text="İmaj Ekle", command=add_image)
blob_image_upload_button.grid(row=1)

#Blob İmaj Görüntüle
blob_image_canvas = tkinter.Canvas(blob_image_frame, width=200, height=200, background="white")
blob_image_canvas.grid(row=0, padx=10, pady=10)



# Soru Giriş Frame
question_frame = tkinter.LabelFrame(frame, text="Soru", labelanchor='n', bd=0)
question_frame.grid(row=2, column=0, padx=20, pady=0, sticky="news")

question_entry = tkinter.Text(
    question_frame, relief="sunken", height=10, width="50")
question_entry.grid(row=1, column=0)

# Soru Giriş
# Options
options_frame = tkinter.LabelFrame(frame, text="Şıklar", labelanchor='n', bd=0)
options_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

# A Option
a_option_label = tkinter.Label(options_frame, text="A.")
a_option_label.grid(row=0, column=0)

a_option_entry = tkinter.Entry(options_frame, width=32)
a_option_entry.grid(row=1, column=0)

# B Option
b_option_label = tkinter.Label(options_frame, text="B.")
b_option_label.grid(row=0, column=1)

b_option_entry = tkinter.Entry(options_frame, width=32)
b_option_entry.grid(row=1, column=1)

# C Option
c_option_label = tkinter.Label(options_frame, text="C.")
c_option_label.grid(row=3, column=0)

c_option_entry = tkinter.Entry(options_frame, width=32)
c_option_entry.grid(row=4, column=0)

# D Option
d_option_label = tkinter.Label(options_frame, text="D.")
d_option_label.grid(row=3, column=1)

d_option_entry = tkinter.Entry(options_frame, width=32)
d_option_entry.grid(row=4, column=1)


# Doğru Yanıt Frame
correct_answer_frame = tkinter.LabelFrame(
    frame, text="Doğru Yanıt", labelanchor='n', bd=0)
correct_answer_frame.grid(row=4, column=0, sticky="news", padx=20, pady=10)


# Doğru Yanıt
correct_answer_label = tkinter.Label(correct_answer_frame)
correct_answer_label.grid(row=0, column=0)

correct_answer_combobox = ttk.Combobox(correct_answer_frame, values=["Cevabı Seçin","A", "B", "C", "D"], width=55, validate='all')
correct_answer_combobox.current(0)
correct_answer_combobox.grid(row=0, column=0, padx=20, pady=5, sticky="news")


# Buttons Frame
buttons_frame = tkinter.Frame(frame)
buttons_frame.grid()


# Buttons
#Kaydet
button_save = tkinter.Button(buttons_frame, text="Kaydet", command=enter_data, width="10", height="2")
button_save.grid(row=0, column=0)

#Çıkış
button_quit = tkinter.Button(buttons_frame, text="Çıkış", command=confirm, width="10", height="2")
button_quit.grid(row=0, column=1, padx=10, pady=10)


window.mainloop()
