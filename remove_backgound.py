from rembg import remove
from PIL import Image
import easygui

print("Ожидайте...")
input_path = easygui.fileopenbox("Выберите изображение для обработки.")
Output_path = easygui.filesavebox("Куда бы Вы хотели сохранить обработанное изображение?")

my_img = Image.open(input_path)
print("Обрабатываю...")
rem = remove(my_img)

save = rem.save(Output_path)
print("Успешное завершение работы. Проверьте указанную папку!")

