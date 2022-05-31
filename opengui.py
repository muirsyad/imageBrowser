from tkinter import*
from tkinter import filedialog
import cv2 as cv

def openFile():
    path = filedialog.askopenfilename()
    print(path)
    img = cv.imread(path)
    cv.imshow("image",img)
    cv.waitKey(0)
    cv.destroyAllWindows()
window = Tk()
button = Button(text="Open", command=openFile)
button.pack()
window.mainloop()