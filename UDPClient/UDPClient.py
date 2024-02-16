import socket
import time
import tkinter as tk
from tkinter import scrolledtext

class UDPClientGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("UDP Client GUI")

        self.text_area = scrolledtext.ScrolledText(self.master, width=40, height=15)
        self.text_area.pack(padx=10, pady=10)

        self.button_send = tk.Button(self.master, text="Send Ping", command=self.send_ping)
        self.button_send.pack(pady=5)

        self.button_exit = tk.Button(self.master, text="Exit", command=self.exit_program)
        self.button_exit.pack(pady=5)

        self.server_address = ('127.0.0.1', 12000)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(2)

    def send_ping(self):
        self.text_area.insert(tk.END, "-------------------------\n")
        self.text_area.insert(tk.END, "Starting Ping\n")
        self.text_area.insert(tk.END, "-------------------------\n")

        for i in range(0, 9):
            start = time.time()
            message = 'Ping ' + str(i) + " " + time.ctime(start)
            try:
                sent = self.socket.sendto(message.encode("utf-8"), self.server_address)
                self.text_area.insert(tk.END, "Sent " + message + "\n")
                data, server = self.socket.recvfrom(4096)
                received_message = data.decode("utf-8")
                self.text_area.insert(tk.END, "Received from server: " + received_message + "\n")
                end = time.time()
                elapsed = end - start
                self.text_area.insert(tk.END, "Time: " + str(elapsed * 1000) + " Milliseconds\n\n")
            except socket.timeout:
                self.text_area.insert(tk.END, "#" + str(i) + " Requested Time out\n\n")

    def exit_program(self):
        self.text_area.insert(tk.END, "Finish ping, closing socket\n")
        self.socket.close()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    client_gui = UDPClientGUI(root)
    root.mainloop()
