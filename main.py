import bitstring
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
chunk_size=int()
input_file_name=''
out_file_name=''
in_lb=int()
out_lb=int()

def dn_packer(input_file, out_file, in_lb, out_lb, chunk_size):
    data_stream=bitstring.ConstBitStream(input_file)
    while True:
        try:
            data=data_stream.read(int(chunk_size)).bin
        except bitstring.ReadError:
            out_file.close()
            break
        chunks = [data[i:i+int(in_lb)] for i in range(0, len(data), int(in_lb))]
        chunks = [str[:-int(int(in_lb)-int(out_lb))] for str in chunks]
        bitstring.BitArray(bin=''.join(chunks)).tofile(out_file)

def up_packer(input_file, out_file, in_lb, out_lb, chunk_size):
    data_stream=bitstring.ConstBitStream(input_file)
    while True:
        try:
            data=data_stream.read(int(chunk_size)).bin
        except bitstring.ReadError:
            out_file.close()
            break
        chunks = [data[i:i+int(in_lb)] for i in range(0, len(data), int(in_lb))]
        chunks = [str1+str('0'*int(int(out_lb)-int(in_lb))) for str1 in chunks]
        bitstring.BitArray(bin=''.join(chunks)).tofile(out_file)
        

def input_file_dialog():
    global input_file_name
    txt1.delete(0,END)
    filename_input = askopenfilename()
    txt1.insert(0,str(filename_input))
    input_file_name=txt1.get()
    return

def out_file_dialog():
    global out_file_name
    txt2.delete(0,END)
    filename_out = asksaveasfilename()
    txt2.insert(0,str(filename_out))
    out_file_name=txt2.get()
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
        None

if(__name__ == '__main__'):
    window = Tk()
    window.title("Form1")
    window.geometry('380x100')
    window.resizable(width=False, height=False)
    lbl = Label(window, text="Input file:")
    lbl.grid(column=0, row=0)
    txt1 = Entry(window,width=33)
    txt1.grid(column=1, row=0, columnspan=2)
    btns = Button(window, text="Open", command=input_file_dialog, width=8) #command=input_file_dialog -> text to txt1
    btns.grid(column=3, row=0)
    lbl1 = Label(window, text="Output file:")
    lbl1.grid(column=0, row=1)
    txt2 = Entry(window,width=33)
    txt2.grid(column=1, row=1, columnspan=2)
    btns1 = Button(window, text="Select", command=out_file_dialog, width=8) #command=out_file_dialog -> text to txt2
    btns1.grid(column=3, row=1)
    lbl2 = Label(window, text="Chunk size (bits):")
    lbl2.grid(column=0, row=3)
    txt3 = Entry(window,width=10)
    txt3.grid(column=1, row=3)
    lbl3 = Label(window, text="Bits for input bytes:")
    lbl3.grid(column=0, row=2)
    txt4 = Entry(window,width=10)
    txt4.grid(column=1, row=2)
    lbl4 = Label(window, text="Bits for output bytes:")
    lbl4.grid(column=2, row=2)
    txt5 = Entry(window,width=10)
    txt5.grid(column=3, row=2)
    btns2 = Button(window, text="Start", command=main, width=8) #command=start
    btns2.grid(column=3, row=3)
    lbl5 = Label(window, text="Bits repacker [by UB1QBJ]")
    lbl5.grid(column=2, row=3)
    window.mainloop()