import time
import random
from lrclib import LrcLibAPI

api = LrcLibAPI(user_agent="my-app/0.0.1")

username = "kuek"
wait = random.randint(1, 3)
track_id = int

def lyric_search():
   try:
      track_id = int(input("Ingrese la id: "))
   except TypeError as kuek:
      print(f"Error: La id deben ser numeros enteros.")
   
   
      try:
         lyrics_id()
      except AttributeError as kuek:
         print(f"Ocurrio un error: {kuek}")




def search_track():
  results = api.search_lyrics(
      track_name=str(input("Ingrese el nombre de la cancion: ")),
  )
  for result in results[:5]:
      duration_minutes = int(result.duration / 60)
      duration_seconds = int(result.duration - (duration_minutes * 60))
      print(f"{result.artist_name} - {result.track_name} ({result.album_name}), {duration_minutes}:{duration_seconds} , id:{result.id}")


def lyrics_id():
    lyrics = api.get_lyrics_by_id(track_id)

    found_lyrics = lyrics.synced_lyrics or lyrics.plain_lyrics
    print("\n".join(found_lyrics.split("\n")))


while True:
   print(f"Bienvenido {username} al sistema de letras y busqueda de canciones")
   op1 = int(input('''Seleccione una opcion:
                   1. Buscar cancion
                   2. Buscar letra con id
                   '''))
   match op1:
      case 1:
         print("Cargando buscador de canciones...")
         time.sleep(wait)
         search_track()

      case 2:
            print("Cargando buscador de letras...")
            time.sleep(wait)
            lyric_search()
         




