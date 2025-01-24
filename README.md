
# Projekt-Dokumentation

Xavier Nursiwat, Filip Mitrovic

| Datum | Version | Zusammenfassung                                              |
| ----- | ------- | ------------------------------------------------------------ |
|       | 0.0.1   | ✍️ Jedes Mal, wenn Sie an dem Projekt arbeiten, fügen Sie hier eine neue Zeile ein und beschreiben in *einem* Satz, was Sie erreicht haben. |
|       | ...     |                                                              |
|       | 1.0.0   |                                                              |

## 1 Informieren

### 1.1 Ihr Projekt

Ein einfacher, leichtgewichtiger Musik-Player mit grafischer Benutzeroberfläche (GUI), der in Python entwickelt wurde. Der Musik-Player bietet grundlegende Funktionen zur Wiedergabe von Musikdateien und eine intuitive Benutzererfahrung.


✍️ Erklären Sie genauer in 50 bis 100 Wörtern, was genau Sie in diesem Projekt erreichen möchten, und was Sie dabei zu lernen hoffen.

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
| 7.1  | Ein Song wird abgespielt.                   | -                                       | Songinformationen wie Titel und Dauer werden angezeigt. |
| 8.1  | Die App ist gestartet.                      | -                                       | Die Benutzeroberfläche ist übersichtlich und bedienbar. |


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
| 8.B  | Tag 5     | Xavier    | Projektdokumentation und Vorbereitung der Präsentation | 45'         |

**Gesamtzeit:** 1125 Minuten

✍️ Die Nummer hat das Format `N.m`, wobei `N` die Nummer der User Story ist, auf die sich das Arbeitspaket bezieht, und `m` von `A` an nach oben buchstabiert. Beispiel: Das dritte Arbeitspaket, das die zweite User Story betrifft, hat also die Nummer `2.C`.

✍️ Ein Arbeitspaket sollte etwa 45' für eine Person in Anspruch nehmen. Die totale Anzahl Arbeitspakete sollte etwa Folgendem entsprechen: `Anzahl R-Sitzungen` ╳ `Anzahl Gruppenmitglieder` ╳ `4`. Wenn Sie also zu dritt an einem Projekt arbeiten, für welches zwei R-Sitzungen geplant sind, sollten Sie auf `2` ╳ `3` ╳`4` = `24` Arbeitspakete kommen. Sollten Sie merken, dass Sie hier nicht genügend Arbeitspakte haben, denken Sie sich weitere "Kann"-User Stories für Kapitel 1.2 aus.

## 3 Entscheiden

✍️ Dokumentieren Sie hier Ihre Entscheidungen und Annahmen, die Sie im Bezug auf Ihre User Stories und die Implementierung getroffen haben.

## 4 Realisieren

| AP-№ | Datum | Zuständig | geplante Zeit | tatsächliche Zeit |
| ---- | ----- | --------- | ------------- | ----------------- |
| 1.A  |       |           |               |                   |
| ...  |       |           |               |                   |

✍️ Tragen Sie jedes Mal, wenn Sie ein Arbeitspaket abschließen, hier ein, wie lang Sie effektiv dafür hatten.

## 5 Kontrollieren

| TC-№ | Datum | Resultat | Tester |
| ---- | ----- | -------- | ------ |
| 1.1  |       |          |        |
| ...  |       |          |        |

✍️ Vergessen Sie nicht, ein Fazit hinzuzufügen, welches das Test-Ergebnis einordnet.

## 6 Auswerten

✍️ Fügen Sie hier eine Verknüpfung zu Ihrem Lern-Bericht ein.
