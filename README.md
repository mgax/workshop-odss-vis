## Open Data Summer School - vizualizări


Set de date: [Achiziții publice 2010-2014](http://data.gov.ro/dataset/achizitii-publice-2010-2014-anunturi-de-participare)

Bibliotecă grafică: [Highcharts](http://www.highcharts.com/demo), [Highmaps](http://www.highcharts.com/maps/demo)

Server web local:

* python 2: `python -m SimpleHTTPServer`
* python 3: `python3 -m http.server`


### Exerciții - charts

Exemplu: [top10.py](top10.py), [top10.html](top10.html) ([demo](https://rawgit.com/mgax/workshop-odss-vis/master/top10.html))

1. Modifică codul astfel încât să facă calculele cu toate sumele convertite în
   EUR.

2. Desenează un grafic cu valoarea totală a proiectelor dintr-un județ - o
   valoare pentru fiecare an.

3. Desenează un grafic cu valoarea totală a proiectelor dintr-un județ - o
   valoare pentru fiecare lună, pentru toți cei 5 ani.

4. Desenează un grafic cu valoarea totală a proiectelor dintr-un județ pe 12
   luni - o valoare pentru fiecare lună, 5 serii de date, suprapuse.

5. Alege 5 coduri CPV și desenează o histogramă cu valoarea totală a
   proiectelor dintr-un județ, pentru fiecare din cele 5 coduri, într-un an.

6. Desenează un pie chart cu valorile totale pentru fonduri EU / non-EU într-un
   singur an.

7. Desenează valoarea totală a proiectelor, la nivel de lună, împărțite în două
   serii - EU și non-EU, ca stacked area chart.


### Exerciții - maps

Exemplu: [avgmap.py](avgmap.py), [avgmap.html](avgmap.html) ([demo](https://rawgit.com/mgax/workshop-odss-vis/master/avgmap.html))

1. Colorează județele în funcție de proporția de fonduri EU / non-EU într-un
   an.

2. Colorează județele în funcție de valoarea totală a proiectelor pe cap de
   locuitor. Va trebui să faci rost de un set de date cu populația județelor.


### Exerciții - extra

1. Desenează câte un sparkline pentru valoarea totală a proiectelor fiecărui
   județ, la nivel de lună, pe perioada celor 5 ani.
