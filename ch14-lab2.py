#Joe Melia EET-107

class Computer:
    def __init__(self, cpu, ram, drive):
        self.__cpu = cpu
        self.__ram = ram
        self.__drive = drive

    def get_cpu(self):
        return self.__cpu
    def get_ram(self):
        return self.__ram
    def get_drive(self):
        return self.__drive

    def set_cpu(self, cpu):
        self.__cpu = cpu
    def set_ram(self, ram):
        self.__ram = ram
    def set_drive(self, drive):
        self.__drive = drive

    def __str__(self):
        return f"Computer(_Computer__cpu_speed={self.__cpu}, _Computer__ram_size={self.__ram}, _Computer__drive_size={self.__drive})"

def main():
    comp1 = Computer(20, 16, 2000)
    comp2 = Computer(50, 32, 5000)
    print(comp1)
    print(comp2)
main()
        
