import tkinter as tk

root = tk.Tk()
root.geometry('500x400')
root.title('Tkinter Hub')

def home_page():
    home_frame = tk.Frame(main_frame)
    lb = tk.Label(home_frame,text='Home Page\n\nPage: 1',font=('Bold',30))
    lb.pack()
    home_frame.pack(pady=20)

def menu_page():
    menu_frame = tk.Frame(main_frame)
    lb = tk.Label(menu_frame,text='Menu Page\n\nPage: 2',font=('Bold',30))
    lb.pack()
    menu_frame.pack(pady=20)

def contact_page():
    contact_frame = tk.Frame(main_frame)
    lb = tk.Label(contact_frame,text='Contact Page\n\nPage: 3',font=('Bold',30))
    lb.pack()
    contact_frame.pack(pady=20)

def about_page():
    about_frame = tk.Frame(main_frame)
    lb = tk.Label(about_frame,text='About Page\n\nPage: 4',font=('Bold',30))
    lb.pack()
    about_frame.pack(pady=20)



def hide_indicators():
    home_indicate.config(bg='#c3c3c3')
    menu_indicate.config(bg='#c3c3c3')
    contact_indicate.config(bg='#c3c3c3')
    about_indicate.config(bg='#c3c3c3')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb,page) :
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page()

options_frame = tk.Frame(root, bg='#c3c3c3')

home_btn = tk.Button(options_frame, text='Home', font=('Bold',15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(home_indicate,home_page))
home_btn.place(x=10,y=50)
home_indicate = tk.Label(options_frame,text='', bg='#c3c3c3')
home_indicate.place(x=3,y=50,width=5,height=40)

menu_btn = tk.Button(options_frame, text='Menu', font=('Bold',15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(menu_indicate,menu_page))
menu_btn.place(x=10,y=100)
menu_indicate = tk.Label(options_frame,text='', bg='#c3c3c3')
menu_indicate.place(x=3,y=100,width=5,height=40)

contact_btn = tk.Button(options_frame, text='Contact', font=('Bold',15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(contact_indicate,contact_page))
contact_btn.place(x=10,y=150)
contact_indicate = tk.Label(options_frame,text='', bg='#c3c3c3')
contact_indicate.place(x=3,y=150,width=5,height=40)

about_btn = tk.Button(options_frame, text='About', font=('Bold',15), fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: indicate(about_indicate,about_page))
about_btn.place(x=10,y=200)
about_indicate = tk.Label(options_frame,text='', bg='#c3c3c3')
about_indicate.place(x=3,y=200,width=5,height=40)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=125,height=400)

main_frame = tk.Frame(root, highlightbackground='black',highlightthickness=2)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400,width=500)

root.mainloop()