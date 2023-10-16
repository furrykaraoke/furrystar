# furrystar
Aplikacja webowa do listy utworów karaoke, oparta na technologiach django, bootstrap-table, sqlite3 (tymczasowo, bo wiem że lepiej do takich rzeczy użyć postgressa)
# Instalacja
Potrzebujesz pythona na pewno. W wersji 3.10 wyżej bodajże.<br>
Sklonuj repo <br>
`git clone -b dev https://github.com/TheRustedWolf/FURRYSTAR/`<br>
Pobierz zależności z requirements.txt<br>
`pip install -r requirements.txt`<br>
Wygeneruj klucz sekretny, którego sobie użyjesz później w furrystar/settings.py w zmiennej SECRET_KEY w te gwiazdki wklej wygenerowany klucz<br>
`python3 generatesecret.py`<br>
Utwórz bazę danych<br>
`python3 manage.py makemigrations`<br>
`python3 manage.py migrate`<br>
Zrób usera/admina<br>
`python3 manage.py createsuperuser`<br>
Odpal appkę <br>
`python3 manage.py runserver 0.0.0.0:2137`<br>
Lokalnie powinna być na http://localhost:2137 jak mnie pamięć nie myli
# Docker
Zbuduj kontener<br>
`docker build -t furrystar:dev .`
<br>Po zbudowaniu kontenera sobie odpal aplikacje, montując jednocześnie gdzieś tam katalog z bazą danych którą sobie wygenerujesz z bazą piosenek<br>
`docker run -v /app/furrystar/db:/furrystar/db --name=furrystar -d furrystar:dev`<br>
Gdzie /app/furrystar/db to twoja ścieżka fizyczna na komputerze z plikiem db.sqlite3.<br>
Wygeneruj se baze po odpaleniu kontenera <br>
`docker exec -it furrystar python /furrystar/manage.py makemigrations`<br>
`docker exec -it furrystar python /furrystar/manage.py migrate`<br>
Stwórz superusera<br>
`docker exec -it furrystar python /furrystar/manage.py createsuperuser`<br>
Sproxuj sobie tam ulubionym menadżerem proxy port 2137 z kontenera. Znajdziesz go za pomocą komendy<br>
`docker inspect furrystar`<br>pole ip address jak mnie pamięć nie myli<br>
# Administracja
http://adresiplubdomena/admin
# Licencja
MIT