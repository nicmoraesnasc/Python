class DonwloadFile:

    file_size = 0
    internet_speed = 0

    def set_file_size(self, file_size):
        self.file_size = file_size

    def set_internet_speed(self, internet_speed):
        self.internet_speed = internet_speed

    def get_megabits(self) -> int:
        return (self.file_size * 8)
    
    def get_download_speed_seconds(self) -> float:
        return (self.get_megabits() / self.internet_speed)
    
    def get_download_speed_minutes(self) -> float:
        return "%.2f" % (self.get_download_speed_seconds() / 60)
    

download_file = DonwloadFile()
file_size = float(input("Digite o tamanho de um arquivo em MB (Megabytes): "))
internet_speed = float(input("Digite a velocidade de um link de internet em mbps (megabits por segundo): "))

download_file.set_file_size(file_size)
download_file.set_internet_speed(internet_speed)

print("Tempo estimado de download do arquivo: " + str(download_file.get_download_speed_minutes()) + " minutos")