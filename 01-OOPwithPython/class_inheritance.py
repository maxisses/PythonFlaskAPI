class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected.")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # self.name = name
        # self.connected_by = connected_by
        # self.connected = True
        # super does the above three things for me, it runs the super class init method
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
        print(f"Printing {pages} pages")
        self.remaining_pages -= pages        

printer = Printer("printer", "usb", 1000)  

printer.print(20)
print(printer)
printer.disconnect()