import os, sys
import wx


#Do a scheenshot
app = wx.App()  # Need to create an App instance before doing anything
screen = wx.ScreenDC()
size = screen.GetSize()
bmp = wx.Bitmap(size[0], size[1])
mem = wx.MemoryDC(bmp)
mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
del mem  # Release bitmap
bmp.SaveFile('pedazo.png', wx.BITMAP_TYPE_PNG)
#Change folder path to Dropbox
print("Scheenshot image saved as pedazo.png")
#End


#Update excel file

#Filtrar por row = 10 que contienen los nombres de las casas


