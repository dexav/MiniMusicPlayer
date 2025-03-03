
# Projekt-Dokumentation

Xavier Nursiwat, Filip Mitrovic

| Datum | Version | Zusammenfassung                                              |
| ----- | ------- | ------------------------------------------------------------ |
|   10.01.2025    |  0.0.1  |       Dokumentation angefangen und Planen des Projektes.                            |
|    17.01.2025   | 0.0.2   |       Dokumentation erweitert und wieter geplant                                                       |
|    31.11.2025   | 1.0.0   |       Begonnen mit Implementation,   Integration der Audiofunktion mit einer Bibliothek. Wiedergabe von lokalen Audiodateien.        |
|    21.02.2025   | 1.0.1   |        Implementierung, Erstellung von Playlisten. Implementierung von Hinzufügen und Löschen von Songs in einer Playlist.                       |
|    28.02.2025   | 1.0.2   |                                Implementierung von Zufallswiedergabe der Playlists. Programm getestet und Fehler behoben                               |
|    07.03.2025   | 2.0.0   |                                    Portfolio Erstellen und abgeben                          |


## 1 Informieren

### 1.1 Ihr Projekt

Ein einfacher, leichtgewichtiger Musik-Player mit grafischer Benutzeroberfläche (GUI), der in Python entwickelt wurde. Der Musik-Player bietet grundlegende Funktionen zur Wiedergabe von Musikdateien und eine intuitive Benutzererfahrung.



### 1.2 User Stories

| US-№ | Verbindlichkeit | Typ           | Beschreibung                                         |
| ---- | --------------- | ------------- | --------------------------------------------------- |
| 1    | Muss            | Funktional    | Als ein Nutzer möchte ich Musikdateien abspielen können, damit ich meine Lieblingssongs hören kann. |
| 2    | Muss            | Funktional    | Als ein Nutzer möchte ich die Wiedergabe pausieren und fortsetzen können, damit ich die Kontrolle über die Musik habe. |
| 3    | Muss            | Funktional    | Als ein Nutzer möchte ich die Lautstärke anpassen können, damit ich die Musik leiser oder lauter machen kann. |
| 4    | Muss            | Funktional    | Als ein Nutzer möchte ich eine Playlist erstellen können, damit ich mehrere Songs hintereinander abspielen kann. |
| 5    | Muss            | Funktional    | Als ein Nutzer möchte ich Songs aus der Playlist entfernen können, damit ich nur die gewünschten Songs höre. |
| 6    | Kann            | Funktional    | Als ein Nutzer möchte ich die zufällige Wiedergabe aktivieren können, damit ich Songs in einer zufälligen Reihenfolge hören kann. |
| 7    | Kann            | Funktional    | Als ein Nutzer möchte ich Songinformationen wie Titel und Dauer sehen können, damit ich weiß, welcher Song gerade gespielt wird. |
| 8    | Kann            | Qualität      | Als ein Nutzer möchte ich eine einfache und übersichtliche Benutzeroberfläche haben, damit die Bedienung intuitiv ist. |




### 1.3 Testfälle

| TC-№ | Ausgangslage                                 | Eingabe                                  | Erwartete Ausgabe                                  |
| ---- | ------------------------------------------- | --------------------------------------- | ------------------------------------------------- |
| 1.1  | Die App ist gestartet, keine Musik läuft.   | Nutzer wählt eine Musikdatei aus.       | Die ausgewählte Musikdatei wird abgespielt.       |
| 2.1  | Eine Musikdatei wird abgespielt.            | Nutzer drückt auf "Pause".              | Die Wiedergabe wird pausiert.                     |
| 2.2  | Die Wiedergabe ist pausiert.                | Nutzer drückt auf "Play".               | Die Wiedergabe wird fortgesetzt.                  |
| 3.1  | Eine Musikdatei wird abgespielt.            | Nutzer ändert die Lautstärke mit dem Slider. | Die Lautstärke ändert sich entsprechend der Eingabe. |
| 4.1  | Die Playlist ist leer.                      | Nutzer fügt Songs zur Playlist hinzu.   | Die Songs erscheinen in der Playlist.            |
| 5.1  | Eine Playlist mit mehreren Songs existiert. | Nutzer entfernt einen Song.             | Der ausgewählte Song wird aus der Playlist entfernt. |
| 6.1  | Playlist enthält mehrere Songs.             | Nutzer aktiviert die Zufallswiedergabe. | Songs werden in zufälliger Reihenfolge abgespielt. |
| 7.1  | Ein Song wird abgespielt.                   | Grünen Play Button drücken                                       | Songinformationen wie Titel und Dauer werden angezeigt. |
| 8.1  | Die App ist gestartet.                      | Programm ausführen in vsc                                      | Die Benutzeroberfläche ist übersichtlich und bedienbar. |


### 1.4 Diagramme

✍️Fügen Sie hier ein Use Case-Diagramm mit mindestens 3 Anwendungsfällen ein; und eine Skizze davon, wie Ihre Netzseite aussehen sollte.

## 2 Planen

| AP-№ | Frist     | Zuständig | Beschreibung                                          | geplante Zeit |
| ---- | --------- | --------- | ---------------------------------------------------- | ------------- |
| 1.A  | Tag 1     | Xavier    | Basis-GUI mit Tkinter erstellen (Fenster, Buttons, Layout) | 45'          |
| 1.B  | Tag 1     | Filip     | Integration der Pygame-Bibliothek zur Audioverarbeitung | 45'          |
| 2.A  | Tag 1     | Xavier    | Play-, Pause- und Stop-Funktionen implementieren und testen | 45'          |
| 2.B  | Tag 1     | Filip     | Erstellung eines Testplans für die Grundfunktionen   | 45'          |
| 3.A  | Tag 2     | Xavier    | Lautstärkeregler (Slider) in die GUI integrieren     | 45'          |
| 3.B  | Tag 2     | Filip     | Verbindung des Lautstärkereglers mit der Pygame-Logik | 45'          |
| 4.A  | Tag 2     | Xavier    | Playlist-Funktionalität (Songs hinzufügen und anzeigen) implementieren | 45' |
| 4.B  | Tag 2     | Filip     | Funktion zum Entfernen von Songs aus der Playlist erstellen | 45' |
| 5.A  | Tag 3     | Xavier    | Songinformationen (Titel und Dauer) in der GUI anzeigen | 45'         |
| 6.A  | Tag 3     | Filip     | Zufallswiedergabe implementieren                     | 45'          |
| 7.A  | Tag 4     | Xavier    | Benutzertests durchführen und Feedback sammeln       | 45'          |
| 8.A  | Tag 4     | Filip     | Feinschliff der Benutzeroberfläche und Bugfixes      | 45'          |


**Gesamtzeit:** 1080 Minuten



## 3 Entscheiden

Wir haben uns entschieden, eine Funktion für die Zufallswiedergabe zu erstellen, da wir diese auch im privaten Leben häufig nutzen und sie als sehr nützlich empfinden. Sie verhindert, dass Lieder immer in der gleichen Reihenfolge abgespielt werden, und sorgt so für mehr Abwechslung.



## 4 Realisieren  

| AP-№ | Datum  | Zuständig | geplante Zeit | tatsächliche Zeit |
| ---- | ------ | --------- | ------------- | ----------------- |
| 1.A  | Tag 1  | Xavier    | 45'           | 40'               |
| 1.B  | Tag 1  | Filip     | 45'           | 45'               |
| 2.A  | Tag 1  | Xavier    | 45'           | 60'               |
| 2.B  | Tag 1  | Filip     | 45'           | 40'               |
| 3.A  | Tag 2  | Xavier    | 45'           | 30'               |
| 3.B  | Tag 2  | Filip     | 45'           | 45'               |
| 4.A  | Tag 2  | Xavier    | 45'           | 60'               |
| 4.B  | Tag 2  | Filip     | 45'           | 40'               |
| 5.A  | Tag 3  | Xavier    | 45'           | 40'               |
| 6.A  | Tag 3  | Filip     | 45'           | 50'               |
| 7.A  | Tag 4  | Xavier    | 45'           | 20'               |
| 8.A  | Tag 4  | Filip     | 45'           | 20'               |




✍️ Tragen Sie jedes Mal, wenn Sie ein Arbeitspaket abschließen, hier ein, wie lang Sie effektiv dafür hatten.

Hier ist die **Kontrollieren-Phase** im gewünschten Format mit den bestandenen Tests:  

## 5 Kontrollieren  

| TC-№ | Datum  | Resultat  | Tester               |
| ---- | ------ | --------- | -------------------- |
| 1.1  |  28.02.2025  | Bestanden | Mitrovic + Nursiwat |
| 1.2  |  28.02.2025  | Bestanden | Mitrovic + Nursiwat |
| 2.1  |  28.02.2025  | Bestanden | Mitrovic + Nursiwat |
| 2.2  |  28.02.2025  | Bestanden | Mitrovic + Nursiwat |
| 3.1  |  28.02.2025  | Bestanden | Mitrovic + Nursiwat |
| 3.2  |  28.02.2025  | Bestanden | Mitrovic + Nursiwat |
| 4.1  |  28.02.2025  | Bestanden | Mitrovic + Nursiwat |
| 4.2  |  28.02.2025  | Bestanden | Mitrovic + Nursiwat |
| 5.1  |  28.02.2025 | Bestanden | Mitrovic + Nursiwat |
| 6.1  |  28.02.2025  | Bestanden | Mitrovic + Nursiwat |
| 7.1  |  28.02.2025  | Bestanden | Mitrovic + Nursiwat |
| 8.1  |  28.02.2025  | Bestanden | Mitrovic + Nursiwat |
| 8.2  | 28.02.2025  | Bestanden | Mitrovic + Nursiwat |


*Fazit:*
Alles vom Programm funktioniert einwandfrei und wir sind stolz drauf.

## 6 Auswerten

✍️ Fügen Sie hier eine Verknüpfung zu Ihrem Lern-Bericht ein.
