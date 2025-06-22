
# Настройки
class Settings(ctk.CTkFrame):
    def __init__(self, parent, controller, data):
        super().__init__(parent)
        self.controller = controller
        self.widgets()

    def widgets(self):
        global color
        logo = ctk.CTkFont(family="Impact", size=40)
        button_font = ctk.CTkFont(family="Impact", size=25)

        self.top_container = ctk.CTkFrame(self)
        self.top_container.pack(pady=(0, 0))

        self.label = ctk.CTkLabel(self.top_container, text="Во Все Испанские - Настройки", font=logo)
        self.label.grid(row=0, column=0, sticky='nsew')

        self.bottom_container = ctk.CTkFrame(self)
        self.bottom_container.pack(side="bottom", pady=(20, 650))

        self.color_select_green = ctk.CTkButton(self.bottom_container, text="Зеленый",
                                                command=lambda: self.color_change('green'), fg_color='green', width=300,
                                                height=50, font=button_font)
        self.color_select_green.grid(row=0, column=0, sticky='nsew')
        self.color_select_blue = ctk.CTkButton(self.bottom_container, text="Синий",
                                               command=lambda: self.color_change('blue'), fg_color='blue', width=300,
                                               height=50, font=button_font)
        self.color_select_blue.grid(row=1, column=0, sticky='nsew')

        self.back = ctk.CTkButton(self.bottom_container, text="Назад",
                                  command=lambda: self.controller.show_frame("MainMenu"), fg_color=color)
        self.back.grid(row=2, column=0, sticky='nsew')
        self.update_widgets()

    def update_widgets(self):
        global color
        self.back.configure(fg_color=color)

    def color_change(self, name):
        global color
        color = name
        self.update_widgets()
        self.controller.show_frame('MainMenu')

