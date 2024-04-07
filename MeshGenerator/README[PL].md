# Program Generatora Siatki

## Opis Programu

Program Generatora Siatki został zaprojektowany w celu generowania i manipulowania siatkami do różnych symulacji inżynierskich i naukowych. Umożliwia użytkownikom tworzenie siatek składających się z trójkątów lub czworokątów, zapisywanie ich do plików oraz wczytywanie istniejących siatek w celu dalszej modyfikacji.

### Przegląd Kodu

### Klasa Node

Klasa `Node` reprezentuje pojedynczy punkt w siatce. Posiada dwa atrybuty, `x` i `y`, które określają jego współrzędne w przestrzeni 2D.

### Klasa Element

Klasa `Element` reprezentuje element geometryczny w siatce, takie jak trójkąt lub czworokąt. Zawiera listę indeksów węzłów definiujących wierzchołki elementu.

### Klasa Application

Klasa `Application` jest głównym komponentem programu. Zarządza generowaniem, zapisywaniem i wczytywaniem siatek. Oto przegląd jej metod:

- `generate_triangles(n, x0, y0, x1, y1, num_x, num_y)`: Generuje siatkę składającą się z trójkątów w określonej dziedzinie prostokątnej zdefiniowanej przez `(x0, y0)` i `(x1, y1)` z podaną liczbą elementów wzdłuż osi x i y.
- `generate_quads(n, x0, y0, x1, y1, num_x, num_y)`: Generuje siatkę składającą się z czworokątów w określonej dziedzinie prostokątnej.
- `save_mesh(filename)`: Zapisuje wygenerowaną siatkę do pliku określonego przez `filename`.
- `load_mesh(filename)`: Wczytuje siatkę z pliku określonego przez `filename`.
- `run()`: Rozpoczyna proces generowania siatki poprzez pytanie użytkownika o dane wejściowe i generowanie siatki zgodnie z nimi.

### Funkcja Główna

Funkcja `main()` tworzy instancję klasy `Application` i zapewnia prosty interfejs wiersza poleceń do interakcji z programem. Umożliwia użytkownikom wybór między utworzeniem nowej siatki, wczytaniem istniejącej siatki lub wyjściem z programu.

## Typy Siatek

### Siatka Trójkątna

Siatka trójkątna składa się z elementów w kształcie trójkątów. Każdy trójkąt jest definiowany przez trzy węzły, a sąsiednie trójkąty dzielą węzły wzdłuż swoich krawędzi. Siatki trójkątne są powszechnie używane w analizie metody elementów skończonych i dynamice płynów komputerowej.

### Siatka Czworokątna

Siatka czworokątna składa się z elementów w kształcie czworokątów. Każdy czworokąt jest definiowany przez cztery węzły, a sąsiednie czworokąty dzielą węzły wzdłuż swoich krawędzi. Siatki czworokątne są często używane w analizie strukturalnej i metodach objętości skończonej do rozwiązywania równań różniczkowych cząstkowych.

Oba typy siatek są szeroko stosowane w różnych symulacjach naukowych i inżynieryjnych ze względu na swoją prostotę i efektywność w reprezentowaniu złożonych geometrii.

## Autor

Ten projekt został stworzony przez ([MaksKubiczek](https://github.com/MaksKubiczek)).

## Licencja

Ten projekt jest objęty licencją [MIT]. Więcej informacji znajduje się w pliku LICENSE.