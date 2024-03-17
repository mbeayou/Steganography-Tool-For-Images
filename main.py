from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from io import BytesIO
import os



class Stegnography_test:

    output_image_size = 0

    def main(self,root):
        root.title('Steganography tool test')
        root.geometry('400x400')
        root.resizable(width =False, height=False)
        f = Frame(root)

        title = Label(f,text='Basic Steganography tool')
        title.config(font=('arial',23))
        title.grid(pady=10)

        hide_btn = Button(f,text="Hide text",command= lambda :self.win1_hide(f), padx=14)
        hide_btn.config(font=('arial',14))
        reveal_btn = Button(f, text="reveal text",padx=14,command=lambda :self.win1_reveal(f))
        reveal_btn.config(font=('arial',14))
        reveal_btn.grid(pady=12)

        ascii_art = Label(f,text= '''(⓿_⓿)''')
        ascii_art.config(font=('arial',60))

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        f.grid()
        title.grid(row=1)
        hide_btn.grid(row=2)
        reveal_btn.grid(row=3)
        ascii_art.grid(row=4,pady=10)
    def win1_reveal(self,f):
        f.destroy()
        d_f2 = Frame(root)
        label_art = Label(d_f2, text='(^‿^)')
        label_art.config(font=('arial',60))
        label_art.grid(row =1,pady=50)
        l1 = Label(d_f2, text='Select the Image')
        l1.config(font=('arial',18))
        l1.grid()
        bws_btn = Button(d_f2, text='Select', command=lambda :self.win2_reveal(d_f2))
        bws_btn.config(font=('arial',18))
        bws_btn.grid()
        back_btn = Button(d_f2, text='back', command=lambda : Stegnography_test.home(self,d_f2))
        back_btn.config(font=('arial',18))
        back_btn.grid(pady=15)
        back_btn.grid()
        d_f2.grid()
    def win2_reveal(self,d_f2):
        d_f3 = Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have to select an image!")
        else:
            myimg = Image.open(myfile, 'r')
            root.geometry('400x500') #increasing window size

            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            l4= Label(d_f3,text='Selected Image :')
            l4.config(font=('arial',18))
            l4.grid()
            panel = Label(d_f3, image=img)
            panel.image = img
            panel.grid()
            hidden_data = self.reveal_fun(myimg)
            l2 = Label(d_f3, text='Hidden data is :')
            l2.config(font=('arial',18))
            l2.grid(pady=10)
            txt_area = Text(d_f3, width=45, height=7)
            txt_area.insert(INSERT, hidden_data)
            txt_area.configure(state='disabled')
            txt_area.grid()
            back_btn = Button(d_f3, text='Cancel', command= lambda :self.exit(d_f3))
            back_btn.config(font=('arial',11))
            back_btn.grid(pady=15)
            back_btn.grid()
            d_f3.grid(row=1)
            d_f2.destroy()
    def win1_hide(self,f):
        f.destroy()
        f2 = Frame(root)
        label_art = Label(f2, text='U_U')
        label_art.config(font=('arial',70))
        label_art.grid(row =1,pady=50)
        l1= Label(f2,text='Select the Image in which \nyou want to hide text :')
        l1.config(font=('arial',18))
        l1.grid()

        bws_btn = Button(f2,text='Select',command=lambda : self.win2_hide(f2))
        bws_btn.config(font=('arial',18))
        bws_btn.grid()
        back_btn = Button(f2, text='Cancel', command=lambda : Stegnography_test.home(self,f2))
        back_btn.config(font=('arial',18))
        back_btn.grid(pady=15)
        back_btn.grid()
        f2.grid()
    def win2_hide(self,f2):
        ep= Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((200,200))
            img = ImageTk.PhotoImage(myimage)
            root.geometry('400x500') #increasing window size
            l3= Label(ep,text='Selected Image')
            l3.config(font=('arial',18))
            l3.grid()
            panel = Label(ep, image=img)
            panel.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel.grid()
            l2 = Label(ep, text='Enter the message')
            l2.config(font=('arial',18))
            l2.grid(pady=15)
            text_area = Text(ep, width=40, height=5)
            text_area.grid()
            hide_btn = Button(ep, text='back', command=lambda : Stegnography_test.home(self,ep))
            hide_btn.config(font=('arial',11))
            data = text_area.get("1.0", "end-1c")
            back_btn = Button(ep, text='Hide', command=lambda : [self.hide_fun(text_area,myimg),Stegnography_test.home(self,ep)])
            back_btn.config(font=('arial',13))
            back_btn.grid(pady=15)
            hide_btn.grid()
            ep.grid(row=1)
            f2.destroy()

    def home(self,frame):
            frame.destroy()
            self.main(root)
    def reveal_fun(self, image):
        data = ''
        imgdata = iter(image.getdata())

        while (True):
            pixels = [value for value in imgdata.__next__()[:3] +
                      imgdata.__next__()[:3] +
                      imgdata.__next__()[:3]]
            binstr = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if pixels[-1] % 2 != 0:
                return data

    def toBinary(self,data):
        newd = []
        for i in data:
            #ord converts text to Unicode code
            #while format  08b represent it in binary form
            #Character 'H': Unicode code point is 72, which in binary is '1001000'.
            newd.append(format(ord(i), '08b'))
        return newd
    def StegnoPix(self,pix, data):
        datalist = self.toBinary(data)
        lendata = len(datalist)
        imdata = iter(pix)
        for i in range(lendata):
            # Extracting 3 pixels at a time
            pix = [value for value in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]]

            for j in range(0, 8):
                if (datalist[i][j] == '0') and (pix[j] % 2 != 0):

                    if (pix[j] % 2 != 0):
                        pix[j] -= 1

                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1

            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]
    def hide_fun(self,text_area,myimg):
        data = text_area.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo("Alert","there is no text")
        else:
            newimg = myimg.copy()
            w = newimg.size[0]
            (x, y) = (0, 0)
            for pixel in self.StegnoPix(newimg.getdata(), data):
                # Putting modified pixels in the new image
                newimg.putpixel((x, y), pixel)
                if (x == w - 1):
                    x = 0
                    y += 1
                else:
                    x += 1
            my_file = BytesIO()
            temp=os.path.splitext(os.path.basename(myimg.filename))[0]
            newimg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('png', '*.png')]),defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newimg.size
            messagebox.showinfo("Success","hidding text done Successfully")

    def exit(self,frame):
        frame.destroy()
        self.main(root)

root = Tk()
o = Stegnography_test()
o.main(root)
root.mainloop()
