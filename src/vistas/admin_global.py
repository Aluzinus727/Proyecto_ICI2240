from tkinter import Frame, Label, Button, StringVar, Entry, ttk, END


class PageAdminGlobal(Frame):
    def __init__(self, master):
        self.controller = master.controller
        
        #Añade los botones de las distintas opciones
        Frame.__init__(self, master)
        self.configure(bg="#33353d")
        
        #Añade el texto del menú
        label1 = Label(self, text="MENÚ ADMINISTRADOR GLOBAL:", font='Helvetica 12 bold')
        label1.configure(bg="#33353d", fg="#cccccccff")
        label1.pack(pady=70)
        
        #Añade los botones de las distintas opciones
        boton1 = Button(self, text="Modificar administradores", font='Helvetica 10 bold', command=lambda:master.switch_frame(SubPageAdminGlobal))
        boton1.configure(bg="#cccccccff", fg="#1c1c1c")
        boton1.pack(pady=10)
        boton4 = Button(self, text="Modificar precios películas", font='Helvetica 10 bold', command=lambda:self.controller.boton_modificar_precios())
        boton4.configure(bg="#cccccccff", fg="#1c1c1c")
        boton4.pack(pady=10)
        boton5 = Button(self, text="Generar cupones de descuento", font='Helvetica 10 bold', command=lambda:master.switch_frame(PageGenerarCupones))
        boton5.configure(bg="#cccccccff", fg="#1c1c1c")
        boton5.pack(pady=10)

    
class SubPageAdminGlobal(Frame):
    def __init__(self, master):
        self.controller = master.controller
        
        Frame.__init__(self, master)
        self.configure(bg="#33353d")
        
        #Añade el texto del menú
        label1 = Label(self, text="SUBMENÚ MODIFICAR ADMINISTRADORES:", font='Helvetica 12 bold')
        label1.configure(bg="#33353d", fg="#cccccccff")
        label1.pack(pady=100)
        
        #Añade los botones de las distintas opciones
        boton1 = Button(self, text="Agregar administrador local", font='Helvetica 10 bold', command=lambda:self.controller.boton_agregar_local_adm())
        boton1.configure(bg="#cccccccff", fg="#1c1c1c")
        boton1.pack(pady=10)
        boton2 = Button(self, text="Eliminar administrador local", font='Helvetica 10 bold', command=lambda:self.controller.boton_eliminar_local_adm())
        boton2.configure(bg="#cccccccff", fg="#1c1c1c")
        boton2.pack(pady=10)


class PageEliminarAdmin(Frame):
    def __init__(self, master):
        self.controller = master.controller

        Frame.__init__(self, master)
        self.configure(bg="#33353d")

        label1 = Label(self, text="RUT a eliminar", font='Helvetica 10 bold')
        label1.configure(bg="#33353d", fg="#cccccccff")
        label1.grid(row=0, column=0, pady=(50, 0)) 
         
        rut = StringVar()
        entry_cantidad = Entry(self, width=20, textvariable=rut)
        entry_cantidad.configure(bg="#e6e1da")
        entry_cantidad.grid(row=0, column=1, columnspan=3, pady=(50, 0)) 

        boton_verificar = Button(self, text="Eliminar", 
                                command=lambda:self.controller.eliminar_admin(rut.get()), 
                                font='Helvetica 10 bold')
        boton_verificar.configure(bg="#cccccccff", fg="#1c1c1c")
        boton_verificar.grid(row=1, column=0, columnspan=4, pady=20)

        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="#33353d",
                fieldbackground="#33353d", foreground="#cccccccff")
        
        self.treeview = ttk.Treeview(self, columns=("RUT", "NOMBRE", "CINE"))

        self.treeview.heading("#0", text="RUT")
        self.treeview.heading("#1", text="NOMBRE")
        self.treeview.heading("#2", text="CINE")

        self.treeview.grid(row=2, column=0, rowspan=10, columnspan=10)

        boton_retroceder = Button(self, text="Atrás", font='Helvetica 10 bold',
                                 command=lambda:master.switch_frame(PageAdminGlobal))
        boton_retroceder.configure(bg="#ec646c", fg="#1c1c1c")
        boton_retroceder.grid(row=13, column=0, columnspan=4, pady=20)

    def set_admins(self, admins: list):
        for admin in admins:
            item = self.treeview.insert("", 
                                END, 
                                text=admin[0],
                                values=(admin[1], admin[2]),
                                tags=("selected"))

    def search_and_del_admin(self, rut: str):
        for child in self.treeview.get_children():
            item = self.treeview.item(child)

            if item['text'] == rut:
                self.treeview.delete(child)
                return item['values'][1]
            
        return None

class PageAgregarAdmin(Frame):
      def __init__(self, master):
        self.controller = master.controller

        Frame.__init__(self, master)
        self.configure(bg="#33353d")


        label1 = Label(self, text="Nombre", font='Helvetica 10 bold')
        label1.configure(bg="#33353d", fg="#cccccccff")
        label1.grid(row=0, column=0, pady=(100, 0)) 
         
        nombre = StringVar()
        entry_nombre = Entry(self, width=20, textvariable=nombre)
        entry_nombre.configure(bg="#e6e1da")
        entry_nombre.grid(row=0, column=1, columnspan=3, pady=(100, 0)) 
        
        label1 = Label(self, text="RUT", font='Helvetica 10 bold')
        label1.configure(bg="#33353d", fg="#cccccccff")
        label1.grid(row=1, column=0) 
         
        rut = StringVar()
        entry_rut = Entry(self, width=20, textvariable=rut)
        entry_rut.configure(bg="#e6e1da")
        entry_rut.grid(row=1, column=1, columnspan=3) 

        label2 = Label(self, text="Contraseña", font='Helvetica 10 bold')
        label2.configure(bg="#33353d", fg="#cccccccff")
        label2.grid(row=2, column=0) 
         
        contraseña = StringVar()
        entry_contraseña = Entry(self, width=20, textvariable=contraseña)
        entry_contraseña.configure(bg="#e6e1da")
        entry_contraseña.grid(row=2, column=1, columnspan=3) 

        label3 = Label(self, text="Cine", font='Helvetica 10 bold')
        label3.configure(bg="#33353d", fg="#cccccccff")
        label3.grid(row=3, column=0) 
         
        cine = StringVar()
        entry_cine = Entry(self, width=20, textvariable=cine)
        entry_cine.configure(bg="#e6e1da")
        entry_cine.grid(row=3, column=1, columnspan=3) 

        label1 = Label(self, text="Sueldo", font='Helvetica 10 bold')
        label1.configure(bg="#33353d", fg="#cccccccff")
        label1.grid(row=4, column=0) 
         
        sueldo = StringVar()
        entry_sueldo = Entry(self, width=20, textvariable=sueldo)
        entry_sueldo.configure(bg="#e6e1da")
        entry_sueldo.grid(row=4, column=1, columnspan=3) 

        boton_verificar = Button(self, text="Añadir", 
                                command=lambda:self.controller.agregar_admin(
                                    nombre.get(),
                                    rut.get(),
                                    contraseña.get(),
                                    cine.get(),
                                    sueldo.get()
                                    ), 
                                font='Helvetica 10 bold')
        boton_verificar.configure(bg="#cccccccff", fg="#1c1c1c")
        boton_verificar.grid(row=5, column=0, columnspan=4, pady=20)

        boton_retroceder = Button(self, text="Atrás", font='Helvetica 10 bold',
                                 command=lambda:master.switch_frame(PageAdminGlobal))
        boton_retroceder.configure(bg="#ec646c", fg="#1c1c1c")
        boton_retroceder.grid(row=6, column=0, columnspan=4, pady=20)
        

class PageGenerarCupones(Frame):        
    def __init__(self, master):
        self.controller = master.controller
        Frame.__init__(self, master)
        self.configure(bg="#33353d")
        
        title = Label(self)
        title.configure(bg="#33353d", fg="#cccccccff")
        title.pack(pady=50)
        
        label1 = Label(self, text="Ingrese la cantidad de cupones a generar", font='Helvetica 10 bold')
        label1.configure(bg="#33353d", fg="#cccccccff")
        label1.pack(pady=10) 
         
        cantidad = StringVar()
        entry_cantidad = Entry(self, width=20, textvariable=cantidad)
        entry_cantidad.configure(bg="#e6e1da")
        entry_cantidad.pack(pady=10) 

        label2 = Label(self, text="Ingrese el porcentaje de descuento (Rango: 0-100)", font='Helvetica 10 bold')
        label2.configure(bg="#33353d", fg="#cccccccff")
        label2.pack(pady=10) 
         
        descuento = StringVar()
        entry_descuento = Entry(self, width=20, textvariable=descuento)
        entry_descuento.configure(bg="#e6e1da")
        entry_descuento.pack(pady=10) 
        
        boton_verificar = Button(self, text="Generar", 
                                command=lambda:self.controller.generar_cupones(
                                                            cantidad.get(),
                                                            descuento.get()
                                                            ), 
                                font='Helvetica 10 bold')
        boton_verificar.configure(bg="#cccccccff", fg="#1c1c1c")
        boton_verificar.pack(pady=10)
        
        retroceder = Button(self, text="Confirmar", font='Helvetica 10 bold', command=lambda:master.switch_frame(PageAdminGlobal))
        retroceder.configure(bg="#ec646c", fg="#1c1c1c")
        retroceder.pack(pady=10)


class PageModificarPrecio(Frame): 
    def __init__(self, master):
        self.controller = master.controller
        self.selected_pelicula = None

        Frame.__init__(self, master)
        self.configure(bg="#33353d")

        self.texto_precio = Label(self, text="Nuevo precio:", font='Helvetica 12 bold')
        self.texto_precio.configure(bg="#33353d", fg="#cccccccff")
        self.texto_precio.grid(row=0, column=0, pady=(50,0))
        
        self.precio = StringVar()
        self.entry_precio = Entry(self, width=20, textvariable=self.precio)
        self.entry_precio.configure(bg="#e6e1da")
        self.entry_precio.grid(row=0, column=1, pady=(50,0))


        self.boton_modificar_precio = Button(self, 
                                            text="Modificar", 
                                            font='Helvetica 10 bold', 
                                            command=lambda:self.controller.modificar_precio(
                                                self.precio.get()
                                            ))
        self.boton_modificar_precio.configure(bg="#cccccccff", fg="#1c1c1c")
        self.boton_modificar_precio.grid(row=1, column=0, pady=20, columnspan=2)

        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="#33353d",
                fieldbackground="#33353d", foreground="#cccccccff")
        
        self.treeview = ttk.Treeview(self, columns=("ID LOCAL", "NOMBRE", "CINE", "FORMATO", "PRECIO"))
        self.treeview.tag_bind(
            "selected", "<<TreeviewSelect>>", self.item_selected)

        self.treeview.heading("#0", text="ID LOCAL")
        self.treeview.heading("#1", text="NOMBRE")
        self.treeview.heading("#2", text="CINE")
        self.treeview.heading("#3", text="FORMATO")
        self.treeview.heading("#4", text="PRECIO")

        self.treeview.grid(row=2, column=0, rowspan=10, columnspan=10)

        self.boton_retroceder = Button(self, text="Confirmar", font='Helvetica 10 bold', command=lambda:master.switch_frame(PageAdminGlobal))
        self.boton_retroceder.configure(bg="#ec646c", fg="#1c1c1c")
        self.boton_retroceder.grid(row=15, column=1, pady=40)
    
    def item_selected(self, event):
        curl_item = self.treeview.focus()

        self.selected_pelicula = (curl_item, self.treeview.item(curl_item), self.treeview.item(curl_item))

    def set_peliculas(self, peliculas: list):
        print(peliculas)

        for pelicula in peliculas:
            item = self.treeview.insert("", 
                                END, 
                                text=pelicula[0],
                                values=(pelicula[1], pelicula[2], pelicula[3], pelicula[4]),
                                tags=("selected"))

    def update_pelicula(self, pelicula, text, values):
        self.treeview.item(pelicula, text=text, values=values)


