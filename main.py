# importing the required packages
from tkinter.ttk import Combobox
import pyautogui
import cv2
import numpy as np
from tkinter import *

window = Tk()

window.title("ScreenRecorder")

width, height = pyautogui.size()
# Specify resolution
resolution = (width, height)

window.geometry('200x80')
window.configure(bg='gray')
window.resizable(width=False, height=False)
lbl = Label(window, bg="gray", text="Grabar pantalla : ")

lbl.grid(column=1, row=1)

# txt = Entry(window, width=10, state='disabled')
# txt.insert(0, str(width)+'x'+str(height))
# txt.grid(column=0, row=2)

lblfp = Label(window, bg="gray", text="---------------")
lblst = Label(window, bg="gray", text="Stop = Ctrl + P ")
lblfp.grid(column=2, row=1)
lblst.grid(column=1, row=4)

chk_state = BooleanVar()

chk_state.set(True)  # set check state

chk = Checkbutton(window, bg="gray", text='Mostrar preview', var=chk_state)

chk.grid(column=1, row=3)


def clicked():
    if chk_state.get():
        print(str(chk_state.get()))
    # Specify video codec
    codec = cv2.VideoWriter_fourcc(*"XVID")

    # Specify name of Output file
    filename = "record.avi"

    # Specify frames rate. We can choose any
    # value and experiment with it
    fps = 60.0

    # Creating a VideoWriter object
    out = cv2.VideoWriter(filename, codec, fps, resolution)

    if chk_state.get():
        # Create an Empty window
        cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

        # Resize this window
        cv2.resizeWindow("Live", 480, 270)

    while True:
        # Take screenshot using PyAutoGUI
        img = pyautogui.screenshot()

        # Convert the screenshot to a numpy array
        frame = np.array(img)

        # Convert it from BGR(Blue, Green, Red) to
        # RGB(Red, Green, Blue)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Write it to the output file
        out.write(frame)

        if chk_state.get():
            # Optional: Display the recording screen
            cv2.imshow('Live', frame)

        # Stop recording when we press 'q'
        if cv2.waitKey(1) == 16:
            break

    # Release the Video writer
    out.release()

    # Destroy all windows
    cv2.destroyAllWindows()


btn = Button(window, text="Record", command=clicked, bg="orange", fg="red")

btn.grid(column=2, row=4)




window.mainloop()
