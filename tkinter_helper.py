from tkinter import *  # Первым делом импортируем tkinter

"""Объявляем функии"""

def func():  # Если функция работает без bind, то в скобках event не нужен
    print('func_1')


def func_2(event):  # А если с bind, то нужен
    print('func_2')

def func_3(event, f):  # А иногда надо даже вводить доп. аргументы
    print('func_3')

"""Ввод и объявление доп. данных"""

data = [123, 456, 789]
colours = {'#ff0000': 'Красный', '#ff7d00': 'Оранжевый',
           '#ffff00': 'Жёлтый', '#00ff00': 'Зелёный',
           '#007dff': 'Голубой', '#0000ff': 'Синий',
           '#7d00ff': 'Фиолетовый'}

"""Создание окон и виджетов"""

# Окно
master = Tk()

# Метка
label = Label(master,
              bg='yellow',
              fg='blue',
              bd=10,
              width=20,
              height=2,
              font="Arial 16",
              )

# Однострочное текстовое поле
entry = Entry(master,  # Фрейм или окно, к которому виджет относится  
              width=20,
              justify=LEFT  # Выравнивание
              )
# Кнопка
button = Button(master,
                text = 'Текст',
                width=20,
                height=2,
                bd=20,  # Границы
                bg='yellow',  # Цвет фона
                fg='blue',  # Цвет текста
                activebackground='#000000',  # Цвет фона при нажатии
                activeforeground='#ffffff',  # Цвет текста при нажатии
                font=("Comic Sans MS", 12, "bold"),
                command = func  # Функция, выполняющаяся при нажатии
                )

# Радиокнопки (Имеют смысл группами от двух и к ним нужна переменная)
rad_but = IntVar()  # Ещё есть DoubleVar, StringVar, BooleanVar
rad_but.set(0)  # Позёрская инкапсулированая переменная
radiobutton_1 = Radiobutton(master,
                            text='1',
                            variable=rad_but,  # При нажатии этой переменной...
                            value=1, # ...присваивается это значение
                            indicatoron=0,  # Радиокнопка похожа на обычную
                            command=func
                            )
radiobutton_2 = Radiobutton(master, text='2', variable=rad_but, value=2,
              indicatoron=1, command=func)

# Флажок (к нему тоже нужна переменная)
ch_but = BooleanVar()
checkbutton = Checkbutton(text='флажок',
                          variable=ch_but,  # Связанная переменная
                          onvalue=1,  # Значение при включённом
                          offvalue=0  # Значение при выключенном
                          )

# Рамка
frame = Frame(master)

# Рамка с подписью
labelframe = LabelFrame(master,
                        text='Текст')

# Многострочное текстовое поле
text = Text(frame,
            width=40,
            height=12,
            wrap=WORD  # Переносить слова на новую строку целиком, не по буквам
            )

scrollbar = Scrollbar(frame,
                      command=text.yview)

# Список, где можно нажиать на элементы                
listbox = Listbox(labelframe,
    selectmode=EXTENDED)  # Можно выбрать несколько элементов

"""Связывание виджетов и событий"""

button.bind('<Button-1>', func_2)
button.bind('<Button-3>', func_2)  # Правая кнопка мыши
# А вот так мы вызываем функцию с аргументами
entry.bind('<Return>', lambda event, f="Взлом Егора": func_3(event, f))
listbox.bind('<Double-Button-1>', func_2)

"""Расположение виджетов"""



label.pack(expand=1,  # Расширение. 0 или 1
           anchor=None,  # Якорь N S W E и комбинации
           )
#label.pack_forget()  #  Забыть виджет (можно потом снова его создать)
#label.destroy()  # виджет (больше его нельзя будет создать)
label.pack()
entry.pack()
button.pack()
radiobutton_1.pack()
radiobutton_2.pack()
checkbutton.pack()
frame.pack()
labelframe.pack()
listbox.pack()

# Сначала надо паковать scrollbar, а потом виджет, для которого этот scrollbar
scrollbar.pack(side=RIGHT,  # Сторона, куда цепляется виджет, может быть:
                            # TOP BOTTOM LEFT RIGHT
               fill=Y  # Заполение. NONE, BOTH, X, Y
               )
text.pack(padx=0,  # Внешний горизонтальный отступ 
          pady=10,  # Внешний вертикальный отступ
          ipadx=10,  # Внутренний горизонтальный отступ
          ipady=10  # Внутренний вертикальный отступ
          )



"""Действия с виджетами"""


entry.get()  # Получить текст из однострочного тектового поля
entry.insert(END, "Текст") # Вставить в поле
entry.delete(0, END)  # Удалить по индексу (можно срез)

# Многострочные поля. Числа дальше означают: Номер_строки.номер_символа
# 1.0 это самое начало (номер строки начинается с 1, символа с 0)
text.get(1.0, END)  # Получить текст из многострочного текстового поля
text.insert(1.0, "Текст\n текст")  # Вставить в многострочное поле
text.delete(1.7, END)  # Удалить
# К ним впридачу идут тэги
text.tag_add('title', 1.0, '1.end')
text.tag_config('title', font=('Verdana', 24, 'bold'), justify=CENTER)
# И ДАЖЕ, БЛИН, ВСТАВКА ДРУГИХ ВИДЖЕТОВ!!!
additional_label = Label(text='Взлом Егора', bg='blue')
text.window_create(INSERT, window=additional_label)
# INSERT это там, где курсор сейчас

# Получение значения переменной на радиокнопке
rad_but.get()

# Автоматическое включение и выключение флажка (или радиокнопки)
checkbutton.deselect()
checkbutton.select()

# Изменение одного аттрибута, как в словарях
label['text'] = 'Текст'
# Изменение одного или нескольких аттрибутов через метод .config()
button.config(text='К. текст', bg='#7d00ff')
text.config(yscrollcommand=scrollbar.set)  # text и scroll важно связывать так

# Вставить в список
listbox.insert(END,  # Позиция. индекс-число или константа END
               data)  # Что именно вставляем
get = listbox.get(0)  # Получить по индексу (можно срез)
listbox.delete(0)  # Удалить по индексу (можно срез)
select = listbox.curselection()  # Получить выделенные ячейки
# Удалить выделенные ячейки
for i in select[::-1]:
    listbox.delete(i)
                
master.mainloop()  # Запуск обработки событий
#master.destroy()  # Закрывает окно

"""

Примечания:

Эти наброски нельзя считать исчерпывающими. Экспериментируйте
Помимо менеджера pack, есть ещё grid и place, но тут их нет

"""

