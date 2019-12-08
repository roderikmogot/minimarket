from tkinter import *
import tkinter.messagebox
import time
import tkinter.ttk as ttk

class minimarket:
    def __init__(self,root):
        self.root = root
        self.root.title("Mini Market App")  # nama aplikasi

        #create Menu
        menu = Menu(self.root)
        self.root.config(menu=menu)

        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Exit", command=self.quit)

        Label(text="").pack()

        #judul app
        label_judul = Label(self.root, text="Mini Market Application", font=("Arial", 18, "bold")) #create label/text
        label_judul.pack() #center output

        label_greeting = Label(self.root, text="Welcome to our App!\n\n", font=("Arial", 14,"italic"))
        label_greeting.pack()

        #login button
        Label(text="Sudah daftar?", font=('Arial',14)).pack()
        button_login = Button(text="Login", height="2", width="30", command=self.window_login).pack()
        Label(text="\n\n\n").pack()

        Label(text="Belum daftar?", font=('Arial', 14)).pack()

        #register button
        button_register = Button(text="Register", height="2", width="30", command=self.window_register).pack()

        Button(text="Customer", height=2, width=30, command=self.belanja).pack()

    def quit(self): #exit!!!
        exit_program = tkinter.messagebox.askquestion("Exit","Are you sure you want to exit?")

        if exit_program == 'yes':
            self.root.destroy()

    def window_register(self):
        global register_screen
        register_screen = Toplevel()

        register_screen.resizable(False, False)  # disable fullscreen

        window_height = 350
        window_width = 700

        screen_width = register_screen.winfo_screenwidth()
        screen_height = register_screen.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        register_screen.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        ##########################

        register_screen.title("Minimarket - Register")

        global username_register
        global password_register
        username_register = StringVar()
        password_register = StringVar()

        global user_register_entry
        global password_register_entry

        login_judul = Label(register_screen, text="Mini Market Application", font=("Arial", 18, "bold")) #create label/text
        login_judul.pack() #center output

        login_greeting = Label(register_screen, text="Register data\n\n", font=("Arial", 14,"italic"))
        login_greeting.pack()

        #buat form
        user_entry_label = Label(register_screen, text="Username: ").pack()  #username label
        user_register_entry = Entry(register_screen,textvariable=username_register).pack()  #username box

        password_entry_label = Label(register_screen, text="Password: ").pack()  #PasswordLabel
        password_register_entry = Entry(register_screen, textvariable=password_register, show='*').pack()  # Password box

        register_butt = Button(register_screen, text="Register", height="2",width="10", command=self.register_user).pack()  # login button

    def register_user(self):
        username_data = username_register.get()
        password_data = password_register.get()


        if username_data == "" or password_data == "":
            tkinter.messagebox.showinfo('Error', 'Wajib diisi semuanya!')
        else:
            file = open("saved_id.txt","a")
            temp = username_data+";"+password_data
            file.write(temp + "\n")
            file.close()

            tkinter.messagebox.showinfo('Sukses', 'Sukses menambahkan!')
            register_screen.destroy()

    def window_login(self):
        global login_screen
        login_screen = Toplevel()

        login_screen.resizable(False, False)  # disable fullscreen

        window_height = 350
        window_width = 700

        screen_width = login_screen.winfo_screenwidth()
        screen_height = login_screen.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        login_screen.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        ##########################

        login_screen.title("Minimarket - Login")

        global username_verify
        global password_verify

        username_verify = StringVar()
        password_verify = StringVar()

        global user_login_entry
        global password_login_entry

        login_judul = Label(login_screen, text="Mini Market Application", font=("Arial", 18, "bold"))
        login_judul.pack()

        login_greeting = Label(login_screen, text="Please enter your information!\n\n", font=("Arial", 14,"italic"))
        login_greeting.pack()


        user_entry_label = Label(login_screen, text="Username: ").pack()
        user_login_entry = Entry(login_screen, textvariable=username_verify).pack()

        password_entry_label = Label(login_screen, text="Password: ").pack()
        password_login_entry = Entry(login_screen, textvariable=password_verify, show='*').pack()

        login_butt = Button(login_screen, text="Sign In", height="2",width="10", command=self.proses_Login).pack()

    def proses_Login(self):
        user_verify = username_verify.get()
        pass_verify = password_verify.get()

        username_id = []
        password_id = []
        try:
            file = open("saved_id.txt","r")
        except FileNotFoundError:
            tkinter.messagebox.showinfo('Error','File tidak ditemukan')
        else:
            for line in file:
                fields = line.split(";")
                username_id.append(fields[0])
                password_id.append(fields[1])

            for i in range(len(password_id)):
                kata_password = password_id[i]
                global hasil_kata_password
                hasil_kata_password = kata_password.replace("\n","")
                password_id.remove(kata_password)
                password_id.insert(i, hasil_kata_password)

            if user_verify and pass_verify != ' ':
                if user_verify in username_id:
                    dapet_index_username = username_id.index(user_verify)
                    if pass_verify in password_id[dapet_index_username]:

                        global login_username

                        login_username = username_id[dapet_index_username]

                        tkinter.messagebox.showinfo('Sukses','Login berhasil..')
                        self.session_login()
                        self.root.withdraw()
                    else:
                        tkinter.messagebox.showinfo('Error','Salah password!')
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

        session_login.title("Minimarket - Index")

        Label(session_login, text="Selamat datang,  "+ login_username +". \nAnda login sebagai admin.", anchor='w').pack(fill='both')

        nama_barang = []
        jumlah_barang = []

        show_table = Button(session_login, text="Report/Transaksi Penjualan", height=2, width=20, command=self.tabel_transaksi).pack(side=BOTTOM)

    def tabel_transaksi(self):
        global transaksi_screen
        transaksi_screen = Toplevel()

        # transaksi_screen.resizable(False, False)  # disable fullscreen

        window_height = 350
        window_width = 700

        screen_width = transaksi_screen.winfo_screenwidth()
        screen_height = transaksi_screen.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))

        transaksi_screen.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
        ##########################

        transaksi_screen.title("Minimarket - List Barang")

        global id_barang
        global nama_barang
        global harga_barang
        global stock_barang

        id_barang = []
        nama_barang = []
        harga_barang = []
        stock_barang = []

        try:
            f = open('transaksi.txt','r')
        except FileNotFoundError:
            tkinter.messagebox.showinfo('Error','File tidak ditemukan!')
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

            global tabel_transaksi
            tabel_transaksi = ttk.Treeview(transaksi_screen)
            tabel_transaksi["columns"] = ("one", "two", "three")
            tabel_transaksi.column("#0", width=100, minwidth=100)
            tabel_transaksi.column("one", width=300, minwidth=300)
            tabel_transaksi.column("two", width=200, minwidth=200)
            tabel_transaksi.column("three", width=97, minwidth=97)

            tabel_transaksi.heading("#0", text="No")
            tabel_transaksi.heading("one", text="Nama Barang")
            tabel_transaksi.heading("two", text="Harga Barang")
            tabel_transaksi.heading("three", text="Stock")

            for i in range(len(id_barang)):
                tabel_transaksi.insert("",i,text=str(i+1).center(20), values=(nama_barang[i].center(75), str(harga_barang[i]).center(50), str(stock_barang[i]).center(20)))

            tabel_transaksi.pack()
            #######
            ttk.Style().configure('green/black.TButton', foreground='green', background='black') #configure dlu!
            ttk.Button(transaksi_screen, text="Add data", style="green.black.TButton",command=self.add_data).pack(side="top", fill="both",expand=True)#command

            ttk.Button(transaksi_screen, text="Delete data", style="green.black.TButton", command=self.delete_data).pack()#command

            ttk.Button(transaksi_screen, text="Edit data", style="green.black.TButton").pack()#command

    def add_data(self):
        global tambah_data
        tambah_data = Toplevel()

        tambah_data.resizable(False, False)  # disable fullscreen

        window_height = 350
        window_width = 700

        screen_width = tambah_data.winfo_screenwidth()
        screen_height = tambah_data.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))

        tambah_data.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
        ##########################

        tambah_data.title("Minimarket - Add data")

        Label(tambah_data, text='Nama barang :').pack()
        #nama barang
        global tambah_barang_data
        tambah_barang_data = StringVar()
        tambah_barang = Entry(tambah_data,textvariable=tambah_barang_data).pack()

        Label(tambah_data, text='Harga barang :').pack()
        #harga barang
        global tambah_harga_data
        tambah_harga_data = StringVar()
        tambah_harga = Entry(tambah_data, textvariable=tambah_harga_data).pack()

        Label(tambah_data, text='Stock barang :').pack()
        #stock barang
        global tambah_stock_data
        tambah_stock_data = StringVar()
        tambah_stock = Entry(tambah_data, textvariable=tambah_stock_data).pack()

        Button(tambah_data, text="Add data!",command=self.proses_add_data).pack()

    def proses_add_data(self):
        proses_tambah_data = tambah_barang_data.get()
        proses_harga_data = tambah_harga_data.get()
        proses_stock_data = tambah_stock_data.get()

        if proses_tambah_data != ' ' and proses_harga_data != ' ' and proses_stock_data != ' ':
            try:
                i = int(proses_harga_data)
                j = int(proses_stock_data)
            except ValueError:
                tkinter.messagebox.showinfo("Error", "Harga dan stock data wajib dalam bentuk angka!")
            else:
                try:
                    f = open('transaksi.txt','a')
                except FileNotFoundError:
                    tkinter.messagebox.showinfo('Error', 'File tidak ditemukan')
                else:
                    a = len(id_barang)
                    b = a + 1
                    temp = str(b) + ";" + proses_tambah_data +";"+ proses_harga_data +";"+ proses_stock_data
                    f.write(temp+"\n")
                    f.close()

                    tkinter.messagebox.showinfo('Sukses!', 'Menambahkan data sukses!')
                    tambah_data.destroy()
        else:
            tkinter.messagebox.showinfo('Error', 'Semua wajib di isi!')

    def delete_data(self):
        global delete_screen
        delete_screen = Toplevel()

        delete_screen.resizable(False, False)  # disable fullscreen

        window_height = 350
        window_width = 700

        screen_width = delete_screen.winfo_screenwidth()
        screen_height = delete_screen.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))

        delete_screen.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
        ##########################

        delete_screen.title("Minimarket - Delete data")

        Label(delete_screen, text='Masukkan nama barang yg akan di hapus :').pack()
        # nama barang
        global delete_barang
        delete_barang = StringVar()
        delete_barang_entry = Entry(delete_screen, textvariable=delete_barang).pack()

        Button(delete_screen, text="Delete data!", command=self.proses_delete_data).pack()

    def proses_delete_data(self):
        del_data = delete_barang.get()
        if del_data != ' ':
            if del_data in nama_barang:
                with open("transaksi.txt", "r") as f:
                    lines = f.readlines()
                with open("transaksi.txt", "w") as f:
                    for line in lines:
                        if del_data not in line:
                            f.write(line)
                tkinter.messagebox.showinfo("Error","Data sukses dihapus!")
                delete_screen.destroy()
        else:
            tkinter.messagebox.showinfo("Error", "Entry wajib diisi!")

    def belanja(self):
        global belanja_screen
        belanja_screen = Toplevel()

        belanja_screen.resizable(False, False)  # disable fullscreen

        window_height = 350
        window_width = 700

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
            f = open('transaksi.txt', 'r')
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
            tabel_barang.column("#0", width=100, minwidth=100)
            tabel_barang.column("one", width=300, minwidth=300)
            tabel_barang.column("two", width=200, minwidth=200)

            tabel_barang.heading("#0", text="No")
            tabel_barang.heading("one", text="Nama Barang")
            tabel_barang.heading("two", text="Harga Barang")

            for i in range(len(id_barang)):
                tabel_barang.insert("", i, text=str(i + 1).center(20), values=(
                nama_barang[i].center(75), str(harga_barang[i]).center(50), str(stock_barang[i]).center(20)))

            tabel_barang.pack()

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
            f = open('transaksi.txt', 'r')
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

        barang_checkout = barang_mau_di_beli.get()
        jumlah_barang_checkout = jumlah_barang_yg_mau_dibeli.get()

        if barang_checkout != ' ' and jumlah_barang_checkout != ' ':
            try:
                a = int(jumlah_barang_checkout)
            except ValueError:
                tkinter.messagebox.showinfo("Error", "Jumlah barang wajib dalam bentuk angka!")
                pembayaran_screen.destroy()
            else:
                try:
                    barang_exist = nama_barang.index(barang_checkout)
                except ValueError:
                    tkinter.messagebox.showinfo("Error", "Barang "+barang_checkout+" tidak ada!")
                    pembayaran_screen.destroy()
                else:
                    if jumlah_barang_checkout != 0:
                        if int(jumlah_barang_checkout) <= int(stock_barang[barang_exist]):
                            global total_harga_barang
                            total_harga_barang = int(harga_barang[barang_exist]) * int(jumlah_barang_checkout)

                            Label(pembayaran_screen,text="Anda akan melakukan pembelian barang "+str(barang_checkout)+" dengan total harga Rp"+str(total_harga_barang)+".").pack()
                            Label(pembayaran_screen, text="Masukkan jumlah yg harus dibayar:").pack()

                            global uang_dibayar
                            uang_dibayar = StringVar()
                            Entry(pembayaran_screen,textvariable=uang_dibayar).pack()
                            Button(pembayaran_screen, text="Bayar",command=self.proses_pembayaran).pack()

                        else:
                            tkinter.messagebox.showinfo("Maaf","Jumlah barang yg ada kurang dari permintaan!")
                    else:
                        tkinter.messagebox.showinfo("Error","Stock wajib >0!")

    def proses_pembayaran(self):
        try:
            jumlah_yg_dibayar = int(uang_dibayar.get())
        except ValueError:
            Label(pembayaran_screen, text="Pembayaran gagal!").pack()
        else:
            if int(total_harga_barang) <= int(jumlah_yg_dibayar):
                if int(total_harga_barang) - int(jumlah_yg_dibayar) == 0:
                    Label(pembayaran_screen, text="Pembayaran sukses!").pack()
                    Label(pembayaran_screen, text="Terima kasih sudah berbelanja!").pack()
                else:
                    Label(pembayaran_screen, text="Pembayaran sukses, dengan kembalian sebesar Rp "+str(int(jumlah_yg_dibayar) - int(total_harga_barang))+".").pack()
                    Label(pembayaran_screen, text="Terima kasih sudah berbelanja!").pack()
            else:
                Label(pembayaran_screen, text="Pembayaran gagal!").pack()

if __name__ == '__main__':
    #######################
    root = Tk()

    root.resizable(False, False)  # disable fullscreen

    window_height = 350
    window_width = 700

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    ##########################

    application = minimarket(root)#access class

    root.mainloop() #loop supaya app jalan terus