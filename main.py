import bitstring, time, os
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.messagebox as mb
chunk_size=int()
input_file_name=''
out_file_name=''
in_lb=int()
out_lb=int()
invert_state=int()

def byte_inverter_state():
    global invert_state
    if(var1.get()==1):
        invert_state=1
    if(var1.get()==0):
        invert_state=0
    return

def dn_packer(input_file, out_file, in_lb, out_lb, chunk_size):
    global invert_state
    data_stream=bitstring.ConstBitStream(input_file)
    start_time = time.time()
    while True:
        try:
            data=data_stream.read(int(chunk_size)).bin
        except bitstring.ReadError:
            out_file.close()
            break
        chunks = [data[i:i+int(in_lb)] for i in range(0, len(data), int(in_lb))]
        chunks = [str[:-int(int(in_lb)-int(out_lb))] for str in chunks]
        if(invert_state==1):
            data=bitstring.BitArray(bin=''.join(chunks))
            data.invert()
            data.tofile(out_file)
        if(invert_state==0):
            bitstring.BitArray(bin=''.join(chunks)).tofile(out_file)
    total_time = str(time.time()-start_time)
    mb.showinfo("", str("Done! Total time: "+str(total_time)))
    return

def up_packer(input_file, out_file, in_lb, out_lb, chunk_size):
    global invert_state
    data_stream=bitstring.ConstBitStream(input_file)
    start_time = time.time()
    while True:
        try:
            data=data_stream.read(int(chunk_size)).bin
        except bitstring.ReadError:
            out_file.close()
            break
        chunks = [data[i:i+int(in_lb)] for i in range(0, len(data), int(in_lb))]
        chunks = [str1+str('0'*int(int(out_lb)-int(in_lb))) for str1 in chunks]
        if(invert_state==1):
            data=bitstring.BitArray(bin=''.join(chunks))
            data.invert()
            data.tofile(out_file)
        if(invert_state==0):
            bitstring.BitArray(bin=''.join(chunks)).tofile(out_file)
    total_time = str(time.time()-start_time)
    mb.showinfo("", str("Done! Total time: "+total_time))
    return

def input_file_dialog():
    global input_file_name
    txt1.delete(0,END)
    filename_input = askopenfilename()
    txt1.insert(0,str(filename_input))
    input_file_name=txt1.get()
    s_f=os.path.getsize(str(input_file_name))
    window.title("Bits Repacker 1.3 by UB1QBJ ["+str(int(s_f/1048576))+" Mb]")
    return

def out_file_dialog():
    global out_file_name
    txt2.delete(0,END)
    filename_out = asksaveasfilename()
    txt2.insert(0,str(filename_out))
    out_file_name=txt2.get()
    return

def find_size():
    a=int(txt4.get())
    b=int(txt5.get())
    d = 1 
    while(d%a!=0 or d%b!=0 or d%8!=0):
        d+=1
    txt3.delete(0,END)
    txt3.insert(0,str(d))
    return

def main():
    global input_file_name, out_file_name
    in_lb=txt4.get()
    out_lb=txt5.get()
    chunk_size=txt3.get()
    input_file=open(str(input_file_name), 'rb')
    out_file=open(str(out_file_name), 'ab')
    if(int(in_lb)>int(out_lb)):
        dn_packer(input_file=input_file, chunk_size=chunk_size, in_lb=in_lb, out_lb=out_lb, out_file=out_file)
    if(int(in_lb)<int(out_lb)):
        up_packer(input_file=input_file, chunk_size=chunk_size, in_lb=in_lb, out_lb=out_lb, out_file=out_file)
    if(int(in_lb)==int(out_lb)):
        mb.showinfo("", str("Bad values! Bits for input bytes = Bits for output bytes!"))

if(__name__ == '__main__'):
    window = Tk()
    var1 = IntVar()
    icon = PhotoImage(file="icon.png")
    window.iconphoto(True, icon)
    window.title("Bits Repacker 1.3 by UB1QBJ")
    window.geometry('478x99')
    window.resizable(width=False, height=False)
    lbl = Label(window, text="Input file:")
    lbl.grid(column=0, row=0, sticky='e')
    txt1 = Entry(window,width=50)
    txt1.grid(column=1, row=0, columnspan=3)
    btns = Button(window, text="Open", command=input_file_dialog, width=8)
    btns.grid(column=4, row=0, sticky='w')
    lbl1 = Label(window, text="Output file:")
    lbl1.grid(column=0, row=1, sticky='e')
    txt2 = Entry(window,width=50)
    txt2.grid(column=1, row=1, columnspan=3)
    btns1 = Button(window, text="Select", command=out_file_dialog, width=8)
    btns1.grid(column=4, row=1, sticky='w')
    lbl3 = Label(window, text="Bits for input bytes:")
    lbl3.grid(column=0, row=2, sticky='e')
    txt4 = Entry(window,width=13)
    txt4.grid(column=1, row=2, sticky='w')
    lbl4 = Label(window, text="Bits for output bytes:")
    lbl4.grid(column=2, row=2, sticky='e', columnspan=2)
    txt5 = Entry(window,width=10)
    txt5.grid(column=4, row=2, sticky='w')
    lbl2 = Label(window, text="Chunk size (bits):")
    lbl2.grid(column=0, row=3, sticky='e')
    txt3 = Entry(window,width=13)
    txt3.grid(column=1, row=3, sticky='w')
    btns3 = Button(window, text="Find chunk size", command=find_size, width=13)
    btns3.grid(column=2, row=3)
    c1 = Checkbutton(window, text='Invert output bits',variable=var1, onvalue=1, offvalue=0, command=byte_inverter_state)
    c1.grid(column=3, row=3, sticky='e')
    btns2 = Button(window, text="Start", command=main, width=8)
    btns2.grid(column=4, row=3, sticky='w')
    window.mainloop()