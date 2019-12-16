import tkinter.messagebox
import tkinter.ttk as ttk

from tkinter import *
from datetime import date

#yang masih kurang
#1. edit data,
#2. kurangin stock
#3.tampilan edit data kurang efisien

#-----yg udh selesai-------
#1. login selesai
#2. client melakukan pembelian
#3. list transaksi
#3. verifikasi add data jika ada yg sama
#3. sort data

class minimarket:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Market App")  # nama aplikasi

        # create Menu
        menu = Menu(self.root)
        self.root.config(menu=menu)

        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Exit", command=self.quit)

        # judul app
        Label(self.root, text="Minimarket", font=('Arial',20, 'bold')).place(x='20',y='10')
        Label(self.root, text='Application',font=('Arial',20,'italic')).place(x='130',y='10')

        Label(self.root, text="Welcome to our Application!",anchor='w').place(x='490',y='12')


        Button(self.root, text="Customer", font=('Helvetica',16,'bold'), height=10, width=25, command=self.belanja).place(x='80',y='100')

        Button(self.root, text="Admin",font=('Helvetica',16,'bold'),height=10, width=25, command=self.window_login).place(x='380',y='100')

    def window_login(self):
        global login_screen
        login_screen = Toplevel()

        login_screen.resizable(False, False)  # disable fullscreen

        window_height = 350
        window_width = 700

        screen_width = login_screen.winfo_screenwidth()
        screen_height = login_screen.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))

        login_screen.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
        ##########################

        login_screen.title("Minimarket - Login")


        # judul app
        Label(login_screen, text="Minimarket", font=('Arial',20, 'bold')).place(x='20',y='10')
        Label(login_screen, text='Application',font=('Arial',20,'italic')).place(x='130',y='10')

        Label(login_screen, text="Please enter your information!\n\n", font=("Arial", 14, "italic")).place(x='470',y='10')

        global username_verify
        global password_verify

        username_verify = StringVar()
        password_verify = StringVar()

        Label(login_screen, text="Username: ").place(x='320', y='80')
        Entry(login_screen, textvariable=username_verify).place(x='260',y='100')

        Label(login_screen, text="Password: ").place(x='323',y='140')
        Entry(login_screen, textvariable=password_verify, show='*').place(x='260',y='160')
        #
        Button(login_screen, text="Sign In", height="2", width="10", command=self.proses_Login).place(x='312',y='200')

    def proses_Login(self):
        user_verify = username_verify.get()
        pass_verify = password_verify.get()

        username_id = []
        password_id = []
        try:
            file = open("saved_id.txt", "r")
        except FileNotFoundError:
            tkinter.messagebox.showinfo('Error', 'File tidak ditemukan')
        else:
            for line in file:
                fields = line.split(";")
                username_id.append(fields[0])
                password_id.append(fields[1])

            for i in range(len(password_id)):
                kata_password = password_id[i]
                global hasil_kata_password
                hasil_kata_password = kata_password.replace("\n", "")
                password_id.remove(kata_password)
                password_id.insert(i, hasil_kata_password)

            if user_verify and pass_verify != ' ':
                if user_verify in username_id:
                    dapet_index_username = username_id.index(user_verify)
                    if pass_verify == password_id[dapet_index_username]:

                        global login_username

                        login_username = username_id[dapet_index_username]

                        tkinter.messagebox.showinfo('Sukses', 'Login berhasil..')
                        self.session_login()
                        self.root.withdraw()
                    else:
                        tkinter.messagebox.showinfo('Error', 'Salah password!')
                else:
                    tkinter.messagebox.showinfo('Error', 'Username tidak ditemukan!')
            else:
                tkinter.messagebox.showinfo('Error', 'Semua wajib diisi!')

    def session_login(self):
        login_screen.destroy()
        global session_login
        session_login = Toplevel()

        session_login.resizable(False, False)  # disable fullscreen

        window_height = 350
        window_width = 700

        screen_width = session_login.winfo_screenwidth()
        screen_height = session_login.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))

        session_login.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
        ##########################

        session_login.title("Minimarket - Admin")

        Label(session_login, text="Minimarket", font=('Arial',20, 'bold')).place(x='20',y='10')
        Label(session_login, text='Application',font=('Arial',20,'italic')).place(x='130',y='10')

        Label(session_login, text="Selamat datang,  " + login_username + ". \nAnda login sebagai admin.",anchor='w').place(x='500',y='8')

        Button(session_login, text="List Barang", font=('Helvetica',16,'bold'), height=10, width=25, command=self.tabel_list_barang).place(x='80',y='100')

        Button(session_login, text="Transaksi Penjualan",font=('Helvetica',16,'bold'),height=10, width=25, command=self.tabel_list_transaksi).place(x='380',y='100')

    def tabel_list_barang(self):
        global tabel_list_barang_screen
        tabel_list_barang_screen = Toplevel()

        tabel_list_barang_screen.resizable(False, False)  # disable fullscreen

        window_height = 400
        window_width = 1099

        screen_width = tabel_list_barang_screen.winfo_screenwidth()
        screen_height = tabel_list_barang_screen.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))

        tabel_list_barang_screen.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
        ##########################

        tabel_list_barang_screen.title("Minimarket - List Barang")

        global id_barang
        global nama_barang
        global harga_barang
        global stock_barang

        id_barang = []
        nama_barang = []
        harga_barang = []
        stock_barang = []

        try:
            f = open('list_barang.txt', 'r')
        except FileNotFoundError:
            tkinter.messagebox.showinfo('Error', 'File tidak ditemukan!')
            tabel_list_barang_screen.destroy()
        else:
            for line in f:
                fields = line.split(";")
                id_barang.append(fields[0])
                nama_barang.append(fields[1])
                harga_barang.append(fields[2])
                stock_barang.append(fields[3])

                for i in range(len(stock_barang)):
                    stock_barang[i] = stock_barang[i].replace('\n', '')

            Label(tabel_list_barang_screen,text="Nama barang",font=("Arial",14,"bold")).place(x='460',y='20',anchor='center')
            global listbox_tabel_nama_barang
            listbox_tabel_nama_barang = Listbox(tabel_list_barang_screen,width=50, height=10)
            for task in range(len(id_barang)):
                listbox_tabel_nama_barang.insert("end", nama_barang[task]+" "+harga_barang[task]+" "+stock_barang[task])
            listbox_tabel_nama_barang.place(x='550',y='120',anchor='center')

        ############# ADD DATA ##############
        Label(tabel_list_barang_screen, text='Add data', font=("Arial", 15,"bold")).place(x='150', y='220', anchor='center') #y vertical, x horizontal

        Label(tabel_list_barang_screen, text='Nama barang :').place(x='80',y='250',anchor='center')
        global tambah_barang_data
        tambah_barang_data = StringVar()
        Entry(tabel_list_barang_screen, textvariable=tambah_barang_data).place(x='220',y='250',anchor='center')

        Label(tabel_list_barang_screen, text='Harga barang :').place(x='80',y='280',anchor='center')
        global tambah_harga_data
        tambah_harga_data = StringVar()
        Entry(tabel_list_barang_screen, textvariable=tambah_harga_data).place(x='220',y='280',anchor='center')

        Label(tabel_list_barang_screen, text='Stock barang :').place(x='80',y='310',anchor='center')
        global tambah_stock_data
        tambah_stock_data = StringVar()
        Entry(tabel_list_barang_screen, textvariable=tambah_stock_data).place(x='220',y='310',anchor='center')

        Button(tabel_list_barang_screen, text="Add!", command=self.proses_add_data).place(x='150',y='340',anchor='center')

        ############# EDIT DATA ##############
        Label(tabel_list_barang_screen, text='Edit data', font=("Arial", 15, "bold")).place(x='500', y='220',anchor='center')  # y vertical, x horizontal
        Label(tabel_list_barang_screen, text='Masukkan nama barang :').place(x='420',y='250',anchor='center')
        global nama_barang_edit
        nama_barang_edit = StringVar()
        Entry(tabel_list_barang_screen, textvariable=nama_barang_edit).place(x='590',y='250',anchor='center')
        Button(tabel_list_barang_screen, text='Cari!', command=self.proses_edit_data).place(x='500', y='280',anchor='center')

        ############# DELETE DATA ##############
        Label(tabel_list_barang_screen, text='Delete data', font=("Arial", 15, "bold")).place(x='870', y='220',anchor='center')  # y vertical, x horizontal
        Label(tabel_list_barang_screen, text='Masukkan nama barang :').place(x='800',y='250',anchor='center')
        global delete_barang
        delete_barang = StringVar()
        Entry(tabel_list_barang_screen, textvariable=delete_barang).place(x='970',y='250',anchor='center')
        Button(tabel_list_barang_screen, text="Delete!", command=self.proses_delete_data).place(x='870',y='280',anchor='center')

        global b
        b = Button(tabel_list_barang_screen, text="Sort nama",height=2,width=10,command=self.sort_nama_barang)
        b.place(x='200',y='70',anchor='center')

        global c
        c = Button(tabel_list_barang_screen, text="Sort harga", height=2, width=10, command=self.sort_harga_barang)
        c.place(x='200', y='110', anchor='center')

        global d
        d = Button(tabel_list_barang_screen, text="Sort stock", height=2, width=10, command=self.sort_stock_barang)
        d.place(x='200', y='150', anchor='center')

        e = Button(tabel_list_barang_screen, text="Reverse", height=2, width=10, command=self.reverse_sort)
        e.place(x='100', y='110', anchor='center')

    def sort_nama_barang(self):
        self.clear_nama_barang_listbox()
        for i in range(len(nama_barang)-1,0,-1):
            for j in range(i):
                if nama_barang[j]>nama_barang[j+1]:
                    temp = nama_barang[j]
                    nama_barang[j] = nama_barang[j+1]
                    nama_barang[j+1] = temp

        # Button(tabel_list_barang_screen, text="Unsort", height=2, width=10, command=self.unsort_barang).place(x='200', y='70', anchor='center')

        # c.place_forget()
        # d.place_forget()

        for i in range(len(nama_barang)):
            listbox_tabel_nama_barang.insert("end", nama_barang[i]+" "+harga_barang[i]+" "+stock_barang[i])

    #masih error
    def sort_harga_barang(self):
        self.clear_nama_barang_listbox()
        for i in range(len(harga_barang) - 1, 0, -1):
            for j in range(i):
                if int(harga_barang[j]) > int(harga_barang[j + 1]):
                    temp = harga_barang[j]
                    harga_barang[j] = harga_barang[j + 1]
                    harga_barang[j + 1] = temp

        # Button(tabel_list_barang_screen, text="Unsort", height=2, width=10, command=self.unsort_barang).place(x='200', y='110', anchor='center')

        print(harga_barang)

        # b.place_forget()
        # d.place_forget()

        for i in range(len(harga_barang)):
            listbox_tabel_nama_barang.insert("end", nama_barang[i]+" "+harga_barang[i]+" "+stock_barang[i])

    def sort_stock_barang(self):
        self.clear_nama_barang_listbox()
        for i in range(len(stock_barang)-1,0,-1):
            for j in range(i):
                if int(stock_barang[j])>int(stock_barang[j+1]):
                    temp = stock_barang[j]
                    stock_barang[j] = stock_barang[j+1]
                    stock_barang[j+1] = temp

        # Button(tabel_list_barang_screen, text="Unsort", height=2, width=10, command=self.unsort_barang).place(x='200',y='150',anchor='center')

        for i in range(len(stock_barang)):
            listbox_tabel_nama_barang.insert("end", nama_barang[i]+" "+harga_barang[i]+" "+stock_barang[i])
        #
        # b.place_forget()
        # c.place_forget()

    # def unsort_barang(self):
    #     self.clear_nama_barang_listbox()
    #
    #     for i in range(len(id_barang)):
    #         listbox_tabel_nama_barang.insert("end", nama_barang[i]+" "+harga_barang[i]+" "+stock_barang[i])
    #
    #     Button(tabel_list_barang_screen, text="Sort nama",height=2,width=10,command=self.sort_nama_barang).place(x='200', y='70', anchor='center')
    #
    #     Button(tabel_list_barang_screen, text="Sort harga", height=2, width=10, command=self.sort_harga_barang).place(x='200', y='110', anchor='center')
    #
    #     Button(tabel_list_barang_screen, text="Sort stock", height=2, width=10, command=self.sort_stock_barang).place(x='200', y='150', anchor='center')

    def reverse_sort(self):
        self.clear_nama_barang_listbox()
        for i in range(len(id_barang)):
            listbox_tabel_nama_barang.insert("end", nama_barang[i]+" "+harga_barang[i]+" "+stock_barang[i])

    def proses_add_data(self):
        proses_tambah_data = tambah_barang_data.get()
        proses_harga_data = tambah_harga_data.get()
        proses_stock_data = tambah_stock_data.get()

        check_tambah_data = proses_tambah_data.isspace()
        check_harga_data = proses_tambah_data.isspace()
        check_stock_data = proses_stock_data.isspace()

        if check_tambah_data == False and check_harga_data == False and check_stock_data == False:
            try:
                i = int(proses_harga_data)
                j = int(proses_stock_data)
            except ValueError:
                tkinter.messagebox.showinfo("Error", "Harga dan stock data wajib dalam bentuk angka!")
            else:
                if int(proses_stock_data) > 0 and int(proses_harga_data) > 0:
                    if proses_tambah_data not in nama_barang:
                        try:
                            f = open('list_barang.txt', 'a')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Error', 'File tidak ditemukan')
                        else:
                            a = len(id_barang)
                            b = a + 1
                            temp = str(b) + ";" + proses_tambah_data.strip() + ";" + proses_harga_data.replace(" ", "") + ";" + proses_stock_data.replace(" ", "")
                            f.write(temp + "\n")
                            f.close()

                            nama_barang.append(proses_tambah_data)
                            harga_barang.append(proses_harga_data)
                            stock_barang.append(proses_stock_data)

                            tkinter.messagebox.showinfo('Sukses!', 'Menambahkan data sukses!')

                            self.clear_nama_barang_listbox()

                            for barang,harga,stock in nama_barang,harga_barang,stock_barang:
                                listbox_tabel_nama_barang.insert("end", barang+" "+harga+" "+stock)

                    else:
                        tkinter.messagebox.showinfo("Error", "Barang tersebut sudah terdaftar!")
                else:
                    tkinter.messagebox.showinfo("Error", "Stock and harga barang wajib diatas 0!")
        else:
            tkinter.messagebox.showinfo('Error', 'Semua wajib di isi!')

    def proses_edit_data(self):
        global get_edit_nama_barang
        get_edit_nama_barang = nama_barang_edit.get()
        if get_edit_nama_barang in nama_barang:
            get_index_barang = nama_barang.index(get_edit_nama_barang)

            global proses_edit_screen
            proses_edit_screen = Toplevel()

            proses_edit_screen.resizable(False, False)  # disable fullscreen

            window_height = 350
            window_width = 700

            screen_width = proses_edit_screen.winfo_screenwidth()
            screen_height = proses_edit_screen.winfo_screenheight()

            x_coordinate = int((screen_width / 2) - (window_width / 2))
            y_coordinate = int((screen_height / 2) - (window_height / 2))

            proses_edit_screen.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
            ##########################

            proses_edit_screen.title("Minimarket - Edit data")

            Label(proses_edit_screen, text='Anda akan edit barang "'+get_edit_nama_barang+'".').pack()

            harga_barang_edit = harga_barang[get_index_barang]
            stock_barang_edit = stock_barang[get_index_barang]

            global harga_barang_edit_final
            global stock_barang_edit_final
            harga_barang_edit_final = StringVar()
            stock_barang_edit_final = StringVar()

            Label(proses_edit_screen, text='Harga barang').pack()
            e = Entry(proses_edit_screen, textvariable=harga_barang_edit_final)
            e.insert(0, harga_barang_edit)
            e.pack()

            Label(proses_edit_screen, text='Stock barang').pack()
            f = Entry(proses_edit_screen, textvariable=stock_barang_edit_final)
            f.insert(0, stock_barang_edit)
            f.pack()

            Button(proses_edit_screen, text='Simpan barang', command=self.verifikasi_edit_data).pack()
        else:
            tkinter.messagebox.showinfo("Error","Barang tidak ditemukan!")

    def verifikasi_edit_data(self):
        harga_barang_verifikasi = harga_barang_edit_final.get()
        stock_barang_verifikasi = stock_barang_edit_final.get()

        try:
            a = int(harga_barang_verifikasi)
            b = int(stock_barang_verifikasi)
        except ValueError:
            tkinter.messagebox.showinfo('Error','Stock atau harga barang wajib dalam bentuk angka!')
        else:
            x = nama_barang.index(get_edit_nama_barang)  # ambil index id supaya keliatan di line berapa di dlm file
            with open("list_barang.txt", "r") as f:
                lines = f.readlines()
                tempp = str(int(id_barang[x]))+";"+get_edit_nama_barang + ";" + str(harga_barang[x]) + ";" + str(stock_barang[x]) #data sebelum nya
                temp_2 = str(int(x)+2)+";"+get_edit_nama_barang+";"+str(a)+";"+str(b) #data yang baru
                lines.remove(tempp)

                with open("temp_barang.txt", 'r') as f:
                    d = f.readlines()
                with open("temp_barang.txt", 'w') as output:
                    for i, line in enumerate(d):  # menggunakan enumerate untuk melihat index setiap baris
                        if i == x:  # check jika garis tersebut cocok dengan id barang datanya, maka
                            output.write(temp_2 + "\n")
                        output.write(line)

                with open("temp_barang.txt", "w") as new_f: #save di temp dlu
                    for line in lines:
                        new_f.write(line)
                    new_f.write(temp_2+"\n")

            with open("temp_barang.txt",'r') as f:
                c = f.readlines()
                with open("list_barang.txt",'w') as j:
                    for line in c:
                        j.write(line)

            self.clear_nama_barang_listbox()

            for barang in nama_barang:
                listbox_tabel_nama_barang.insert("end", barang)

            tkinter.messagebox.showinfo("Sukses", "Data sukses diubah!")
            proses_edit_screen.destroy()

    def proses_delete_data(self):
        del_data = delete_barang.get()
        if del_data != ' ':
            if del_data in nama_barang:
                with open("list_barang.txt", "r") as f:
                    lines = f.readlines()
                with open("list_barang.txt", "w") as f:
                    for line in lines:
                        if del_data not in line:
                            f.write(line)
                tkinter.messagebox.showinfo("Error", "Data sukses dihapus!")
        else:
            tkinter.messagebox.showinfo("Error", "Entry wajib diisi!")

    def tabel_list_transaksi(self):
        global tabel_list_penjualan_screen
        tabel_list_penjualan_screen = Toplevel()

        # transaksi_screen.resizable(False, False)  # disable fullscreen

        window_height = 500
        window_width = 1000

        screen_width = tabel_list_penjualan_screen.winfo_screenwidth()
        screen_height = tabel_list_penjualan_screen.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))

        tabel_list_penjualan_screen.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
        ##########################

        tabel_list_penjualan_screen.title("Minimarket - Penjualan")

        global id_transaksi
        global nama_barang_transaksi
        global total_harga_transaksi
        global stock_barang_transaksi

        id_transaksi = []
        nama_barang_transaksi = []
        total_harga_transaksi = []
        stock_barang_transaksi = []
        tanggal_transaksi = []

        try:
            f = open('transaksi.txt', 'r')
        except FileNotFoundError:
            tkinter.messagebox.showinfo('Error', 'File tidak ditemukan!')
        else:
            for line in f:
                fields = line.split(";")
                id_transaksi.append(fields[0])
                nama_barang_transaksi.append(fields[1])
                stock_barang_transaksi.append(fields[2])
                total_harga_transaksi.append(fields[3])
                tanggal_transaksi.append(fields[4])

            for ab in range(len(id_transaksi)):
                id_transaksi[ab] = int(id_transaksi[ab])

            for cb in range(len(total_harga_transaksi)):
                total_harga_transaksi[cb] = int(total_harga_transaksi[cb])

            for ac in range(len(stock_barang_transaksi)):
                stock_barang_transaksi[ac] = int(stock_barang_transaksi[ac])

            global tabel_list_transaksi
            tabel_list_transaksi = ttk.Treeview(tabel_list_penjualan_screen)
            tabel_list_transaksi["columns"] = ("one", "two", "three","four")
            tabel_list_transaksi.column("#0", width=100, minwidth=100)
            tabel_list_transaksi.column("one", width=300, minwidth=300)
            tabel_list_transaksi.column("two", width=200, minwidth=200)
            tabel_list_transaksi.column("three", width=97, minwidth=97)
            tabel_list_transaksi.column("four", width=110, minwidth=110)

            tabel_list_transaksi.heading("#0", text="No")
            tabel_list_transaksi.heading("one", text="Barang terjual")
            tabel_list_transaksi.heading("two", text="Total harga belanja")
            tabel_list_transaksi.heading("three", text="Jumlah yg dibeli")
            tabel_list_transaksi.heading("four", text="Tanggal transaksi")

            for i in range(len(id_transaksi)):
                tabel_list_transaksi.insert("", i, text=str(i + 1).center(25),
                        values=(nama_barang_transaksi[i].center(85), str(total_harga_transaksi[i]).center(60), str(stock_barang_transaksi[i]).center(33), str(tanggal_transaksi[i]).center(27)))

            tabel_list_transaksi.pack(fill='x')
            Label(tabel_list_penjualan_screen, text="Total penjualan : Rp " +str(sum(total_harga_transaksi))).pack()
            Label(tabel_list_penjualan_screen, text="Jumlah barang terbeli : " + str(sum(stock_barang_transaksi))).pack()
            Button(tabel_list_penjualan_screen, text='Go back', command=tabel_list_penjualan_screen.destroy).pack()
            #######

    def belanja(self):
        global belanja_screen
        belanja_screen = Toplevel()

        belanja_screen.resizable(False, False)  # disable fullscreen

        window_height = 400
        window_width = 1099

        screen_width = belanja_screen.winfo_screenwidth()
        screen_height = belanja_screen.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))

        belanja_screen.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
        ##########################

        belanja_screen.title("Minimarket - Belanja")

        id_barang = []
        nama_barang = []
        harga_barang = []
        stock_barang = []

        try:
            f = open('list_barang.txt', 'r')
        except FileNotFoundError:
            tkinter.messagebox.showinfo('Error', 'File tidak ditemukan!')
        else:
            for line in f:
                fields = line.split(";")
                id_barang.append(fields[0])
                nama_barang.append(fields[1])
                harga_barang.append(fields[2])
                stock_barang.append(fields[3])

            for ab in range(len(id_barang)):
                id_barang[ab] = int(id_barang[ab])

            for cb in range(len(harga_barang)):
                harga_barang[cb] = int(harga_barang[cb])

            for ac in range(len(stock_barang)):
                stock_barang[ac] = int(stock_barang[ac])

            global tabel_barang
            tabel_barang = ttk.Treeview(belanja_screen)
            tabel_barang["columns"] = ("one", "two", "three")
            tabel_barang.column("#0", width=100, minwidth=100, anchor='center')
            tabel_barang.column("one", width=300, minwidth=300, anchor='center')
            tabel_barang.column("two", width=200, minwidth=200, anchor='center')
            tabel_barang.column("three", width=100, minwidth=100, anchor='center')

            tabel_barang.heading("#0", text="No")
            tabel_barang.heading("one", text="Nama Barang")
            tabel_barang.heading("two", text="Harga Barang")
            tabel_barang.heading("three", text="Stock")

            for i in range(len(id_barang)):
                if int(stock_barang[i]) == 0:
                    tabel_barang.insert("", i, text=str(i + 1).center(20), values=(
                        nama_barang[i].center(75), str("Rp "+str(harga_barang[i])).center(50), "Habis".center(20)))
                else:
                    tabel_barang.insert("", i, text=str(i + 1).center(20), values=(
                    nama_barang[i].center(75), str("Rp "+str(harga_barang[i])).center(50), str(stock_barang[i]).center(20)))

            tabel_barang.pack(fill='x')

            Label(belanja_screen, text="Masukkan nama barang yang ingin di beli :").pack()
            global barang_mau_di_beli
            barang_mau_di_beli = StringVar()
            Entry(belanja_screen, textvariable=barang_mau_di_beli).pack()

            Label(belanja_screen, text="Masukkan jumlah barang yang ingin di beli :").pack()
            global jumlah_barang_yg_mau_dibeli
            jumlah_barang_yg_mau_dibeli = StringVar()
            Entry(belanja_screen, textvariable=jumlah_barang_yg_mau_dibeli).pack()

            Button(belanja_screen, text="Bayar", command=self.pembayaran).pack()

    def pembayaran(self):
        global pembayaran_screen
        pembayaran_screen = Toplevel()

        pembayaran_screen.resizable(False, False)  # disable fullscreen

        window_height = 350
        window_width = 700

        screen_width = pembayaran_screen.winfo_screenwidth()
        screen_height = pembayaran_screen.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))

        pembayaran_screen.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
        ##########################

        pembayaran_screen.title("Minimarket - Pembayaran")

        id_barang = []
        nama_barang = []
        harga_barang = []
        stock_barang = []

        try:
            f = open('list_barang.txt', 'r')
        except FileNotFoundError:
            tkinter.messagebox.showinfo('Error', 'File tidak ditemukan!')
        else:
            for line in f:
                fields = line.split(";")
                id_barang.append(fields[0])
                nama_barang.append(fields[1])
                harga_barang.append(fields[2])
                stock_barang.append(fields[3])

            for ab in range(len(id_barang)):
                id_barang[ab] = int(id_barang[ab])

            for cb in range(len(harga_barang)):
                harga_barang[cb] = int(harga_barang[cb])

            for ac in range(len(stock_barang)):
                stock_barang[ac] = int(stock_barang[ac])

        global barang_checkout
        global jumlah_barang_checkout
        barang_checkout = barang_mau_di_beli.get()
        jumlah_barang_checkout = jumlah_barang_yg_mau_dibeli.get()

        if barang_checkout != ' ' and jumlah_barang_checkout != ' ':
            try:
                a = int(jumlah_barang_checkout)
            except ValueError or TypeError:
                tkinter.messagebox.showinfo("Error", "Jumlah barang wajib dalam bentuk angka!")
                pembayaran_screen.destroy()
            else:
                try:
                    barang_exist = nama_barang.index(barang_checkout)
                except ValueError:
                    tkinter.messagebox.showinfo("Error", "Barang " + barang_checkout + " tidak ada!")
                    pembayaran_screen.destroy()
                else:
                    if a > 0:
                        if a <= int(stock_barang[barang_exist]):
                            global total_harga_barang
                            total_harga_barang = int(harga_barang[barang_exist]) * int(jumlah_barang_checkout)

                            Label(pembayaran_screen, text="Anda akan melakukan pembelian barang " + str(
                                barang_checkout) + " dengan total harga Rp" + str(total_harga_barang) + ".").pack()
                            Label(pembayaran_screen, text="Masukkan nominal uang anda:").pack()

                            global uang_dibayar
                            uang_dibayar = StringVar()
                            Entry(pembayaran_screen, textvariable=uang_dibayar).pack()
                            Button(pembayaran_screen, text="Bayar!", command=self.proses_pembayaran).pack()

                        else:
                            tkinter.messagebox.showinfo("Maaf", "Jumlah barang yg ada kurang dari permintaan!")
                            pembayaran_screen.destroy()
                    else:
                        tkinter.messagebox.showinfo("Error", "Stock wajib >0!")
                        pembayaran_screen.destroy()

    def proses_pembayaran(self):
        try:
            jumlah_yg_dibayar = int(uang_dibayar.get())
        except ValueError:
            tkinter.messagebox.showinfo("Error","Pembayaran gagal!\nPembayaran wajib dalam bentuk angka!")
        else:
            if int(total_harga_barang) <= int(jumlah_yg_dibayar):
                id_barang = []
                nama_barang = []
                harga_barang = []
                stock_barang = []

                try:
                    f = open("list_barang.txt", 'r')
                except FileNotFoundError:
                    tkinter.messagebox.showinfo("Error", "File tidak ditemukan!")
                else:
                    for line in f:
                        fields = line.split(";")
                        id_barang.append(fields[0])
                        nama_barang.append(fields[1])
                        harga_barang.append(fields[2])
                        stock_barang.append(fields[3])

                if int(total_harga_barang) - int(jumlah_yg_dibayar) == 0:
                    count = len(open("transaksi.txt").readlines())
                    temp = str(count + 1) + ";" + str(barang_checkout) + ";" + str(jumlah_barang_checkout) + ";" + str(
                        total_harga_barang) + ";" + str(date.today())

                    try:
                        f = open("transaksi.txt", "a")
                    except FileNotFoundError:
                        tkinter.messagebox.showinfo("Error", "File tidak diteumkan")
                    else:
                        f.write(temp + "\n")
                        f.close()

                        ambil_index = nama_barang.index(barang_checkout)
                        update_stock = int(stock_barang[ambil_index]) - int(jumlah_barang_checkout)
                        print("hoho")
                        with open("list_barang.txt", "r") as fh:
                            lines = fh.readlines()
                            tempp = str(int(id_barang[ambil_index])) + ";" + barang_checkout + ";" + str(
                                harga_barang[ambil_index]) + ";" + str(stock_barang[ambil_index])  # data sebelum nya
                            temp_2 = str(int(ambil_index) + 2) + ";" + barang_checkout + ";" + str(
                                harga_barang[ambil_index]) + ";" + str(update_stock)  # data yang baru
                            lines.remove(tempp)

                            with open("temp_barang.txt", 'r') as fhh:
                                e = fhh.readlines()
                            with open("temp_barang.txt", 'w') as output:
                                for i, line in enumerate(e):  # menggunakan enumerate untuk melihat index setiap baris
                                    if i == ambil_index:  # check jika garis tersebut cocok dengan id barang datanya, maka
                                        output.write(temp_2 + "\n")
                                    output.write(line)

                            with open("temp_barang.txt", "w") as new_f:  # save di temp dlu
                                for line in lines:
                                    new_f.write(line)
                                new_f.write(temp_2 + "\n")

                        with open("temp_barang.txt", 'r') as f:
                            g = f.readlines()
                            with open("list_barang.txt", 'w') as j:
                                for line in g:
                                    j.write(line)
                    tkinter.messagebox.showinfo("Sukses","Pembayaran berhasil!\nTerima kasih sudah berbelanja di kami!")
                    pembayaran_screen.destroy()
                    belanja_screen.destroy()
                else:
                    c = int(jumlah_yg_dibayar) - int(total_harga_barang)

                    count = len(open("transaksi.txt").readlines())
                    temp = str(count + 1) + ";" + str(barang_checkout) + ";" + str(jumlah_barang_checkout) + ";" + str(
                        total_harga_barang) + ";" + str(date.today())

                    try:
                        f = open("transaksi.txt", "a")
                    except FileNotFoundError:
                        tkinter.messagebox.showinfo("Error", "File tidak diteumkan")
                    else:
                        f.write(temp + "\n")
                        f.close()
                        ambil_index = nama_barang.index(barang_checkout)
                        update_stock = int(stock_barang[ambil_index]) - int(jumlah_barang_checkout)
                        print("hoho")
                        with open("list_barang.txt", "r") as fh:
                            lines = fh.readlines()
                            tempp = str(int(id_barang[ambil_index])) + ";" + barang_checkout + ";" + str(
                                harga_barang[ambil_index]) + ";" + str(stock_barang[ambil_index])  # data sebelum nya
                            temp_2 = str(int(ambil_index) + 2) + ";" + barang_checkout + ";" + str(
                                harga_barang[ambil_index]) + ";" + str(update_stock)  # data yang baru
                            lines.remove(tempp)

                            with open("temp_barang.txt", 'r') as fhh:
                                e = fhh.readlines()
                            with open("temp_barang.txt", 'w') as output:
                                for i, line in enumerate(e):  # menggunakan enumerate untuk melihat index setiap baris
                                    if i == ambil_index:  # check jika garis tersebut cocok dengan id barang datanya, maka
                                        output.write(temp_2 + "\n")
                                        print("oHH")
                                    output.write(line)

                            with open("temp_barang.txt", "w") as new_f:  # save di temp dlu
                                for line in lines:
                                    new_f.write(line)
                                new_f.write(temp_2 + "\n")

                        with open("temp_barang.txt", 'r') as f:
                            g = f.readlines()
                            with open("list_barang.txt", 'w') as j:
                                for line in g:
                                    j.write(line)
                    tkinter.messagebox.showinfo("Sukses", "Pembayaran berhasil, dengan kembalian sebesar Rp"+str(c)+".\nTerima kasih sudah berbelanja")
                    pembayaran_screen.destroy()
                    belanja_screen.destroy()
            else:
                Label(pembayaran_screen, text="Pembayaran gagal!").pack()

    def clear_nama_barang_listbox(dself):
        listbox_tabel_nama_barang.delete(0,"end")

    def quit(self):  # exit!!!
        exit_program = tkinter.messagebox.askquestion("Exit", "Are you sure you want to exit?")

        if exit_program == 'yes':
            self.root.destroy()

if __name__ == '__main__':
    #######################
    root = Tk()

    root.resizable(False, False)  # disable fullscreen

    window_height = 350
    window_width = 700

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
    ##########################

    application = minimarket(root)  # access class

    root.mainloop()
