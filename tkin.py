from main import *
from tkinter import *
import threading
from time import sleep



root = Tk()
root.config(bg="#7fb2f5")
root.title("Top-100")
root.geometry("600x550+400+200")
root.resizable(width=True, height=True)
root.minsize(width=600, height=550)
root.config(pady=20)



    



def page_ittiration_btn(even):
    wait.config(text = 'Otinish kute turynyz...')
    
    t = threading.Thread(target=page_ittiration_text, args=(10,))
    t.start()
    
def page_ittiration_text(n):
    
    p = page_ittiration(n)
    text['state'] = 'normal'
    
    text.delete(1.0, 'end')
    
    text.insert(1.0, p) # added text with maked in function <p> 
    
    
    wait.config(text = 'Kuttyqtaimyn Tapsyrma Satti Otti')
    text['state'] = 'disabled'
    
    

    
    




label = Label(text="Sanau ushin batyrmany basynsyz", 
              bg="#69a8fa",
              fg="#fff",
              font=("Alexandria", 20 , "bold"),
              padx=20,
              width=25)
btn = Button(text="Esepteu",
             bg="#3483eb",
             fg="#fff",
             font=("Alexandria", 20 , "bold"),
             padx=20,
             width=25)
wait = Label(text="-----------------------" ,
             bg="#69a8fa",
             fg="#fff",
             font=("Alexandria", 20 , "bold"),
             padx=20,
             width=25)
# copyButton = Button(text="Koshiru",
#              bg="#3483eb",
#              fg="#fff",
#              font=("Arial", 20 , "bold"),
#              padx=20,
#              width=25,
#              command=lambda:copy_select())
text = Text(width=28, height=8,
            font=("Alexandria",17,"bold"),
            padx=20,)




# text['state'] = 'disabled'
   




btn.bind('<Button-1>', page_ittiration_btn)




for c in range(1): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r, weight=1)

label.grid(row=0, column=0)
btn.grid(row=1, column=0)
wait.grid(row=2, column=0)
text.grid(row=3, column=0)





root.mainloop()

