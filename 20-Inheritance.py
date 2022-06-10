class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected")


printer = Device("Printer", "USB")
print(printer)

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by) #Herando os metodos da classe pai
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def prin(self, pages):
        if not self.connected:
            print("Your printe is not connected!")
            return

        print(f"Pringint {pages} pages.")
        self.remaining_pages -= pages

printer = Printer("Printer", "USB", 500)

printer.prin(20)

print(printer)

printer.disconnect()