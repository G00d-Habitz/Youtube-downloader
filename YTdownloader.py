from pytube import YouTube
from sys import exit


link = input("Podaj link: ")
resolution = input("Podaj pożądaną rozdzielczość: ")

try:
    video = YouTube(link)
except:
    print("Błąd w linku")
    exit()

print("Tytuł: ", video.title)
print("Wyświetlenia: ", video.views)

try:
    print("Pobieram w rozdzielczości: ", resolution)
    file = video.streams.get_by_resolution(resolution)
    file.download("./downloads")
except:
    print("Nie znalazłem rozdzielczości, pobieram najwyższą jaką widzę...")
    file = video.streams.get_highest_resolution()
    file.download("./downloads")