import win32com.client
import tkinter as tk

# create an instance of the Remote Desktop ActiveX control
rdp = win32com.client.Dispatch("MsTscAx.MsTscAx")

def connect():
    # get user input from GUI
    server = server_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # set RDP connection properties
    rdp.Server = server
    rdp.UserName = username
    rdp.Domain = ""
    rdp.AdvancedSettings2.ClearTextPassword = password

    # set display properties
    rdp.DesktopWidth = 1024
    rdp.DesktopHeight = 768
    rdp.ColorDepth = 16

    # connect to remote computer
    rdp.Connect()

def disconnect():
    # disconnect from remote computer
    rdp.Disconnect()

# create GUI
root = tk.Tk()
root.title("RDP Client")

# server label and entry
server_label = tk.Label(root, text="Server:")
server_label.grid(row=0, column=0)
server_entry = tk.Entry(root)
server_entry.grid(row=0, column=1)

# username label and entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=1, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1)

# password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1)

# connect button
connect_button = tk.Button(root, text="Connect", command=connect)
connect_button.grid(row=3, column=0)

# disconnect button
disconnect_button = tk.Button(root, text="Disconnect", command=disconnect)
disconnect_button.grid(row=3, column=1)

# start GUI
root.mainloop()