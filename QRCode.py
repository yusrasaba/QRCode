import pyqrcode
import png
import tkinter
from pyqrcode import QRCode
code = pyqrcode.create("Hey you...!! yes you..\n Believe me you are beautiful just the way you are and don't ever let anyone take away your precious smile..! \n Have a wondrous day..!")
code_xbm = code.xbm(scale=3)
top = tkinter.Tk()
code_bmp = tkinter.BitmapImage(data=code_xbm)
code_bmp.config(foreground="cyan")
code_bmp.config(background="grey")
label = tkinter.Label(image=code_bmp)
label.pack()
code.svg("myqr.svg", scale=4)
code.png("myqr.png",scale=4)
print("Congratulations.!")
print("Your QR Code has been generated..!!")
