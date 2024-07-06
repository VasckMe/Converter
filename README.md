# Converter

Program do konwersji danych obsługujący formaty: .xml, .json i .yml (.yaml)
Sposób użycia: program.exe pathFile1.x pathFile2.y
gdzie x i y to jeden z formatów .xml, .json i .yml (.yaml).
Powyższe wywołanie programu powinno prawidłowo rozpoznać format, pobrać dane z pathFile1.x, a
następnie utworzyć nowy plik pathFile2.y i przekonwertować dane zgodnie z nowym formatem

# Opis zadan

- Task0: w katalogu projektu utworzyć pusty skrypt (bash, python, batch, powershell, inny dowolny), np.
installResources.ps1, przy każdej instalacji przez PIP, należy taką samą komendę umieścić w tym skrypcie.
Taki skrypt, zawierający listę potrzebnych komponentów pythona będzie niezbędny na etapie konfiguracji
automatycznego budowania projektu.
- Task1: parsowanie argumentów przekazywanych przy uruchomieniu programu
- Task2: wczytywanie do obiektu z pliku .json i weryfikacja poprawności składni pliku
- Task3: zapis danych z obiektu do pliku w formacie i zgodnie ze składnią .json
