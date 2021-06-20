<template>
  <div id="Summary" style="margin: 1% 2%; width: 95%;">
    <v-card flat v-if="this.grades.length < 1">
      <v-row>
      <v-card-title>
        <v-icon class="text-h3" color="black">mdi-numeric-6-box-multiple-outline</v-icon>
      </v-card-title>
      <v-card-title>
        No grades
      </v-card-title>
      </v-row>
    </v-card>
    <v-card>
      <v-simple-table class="elevation-0">
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">
                Subject
              </th>
              <th class="text-left">
                Calculated average
              </th>
              <th class="text-left">
                Predicted average
              </th>
              <th class="text-left">
                Final average
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="item in grades"
              :key="item.Pozycja"
            >
              <td>{{ item.Przedmiot || ''}}</td>
              <td>{{ item.Srednia || ''}}</td>
              <td>{{ item.ProponowanaOcenaRoczna || ''}}</td>
              <td>{{ item.OcenaRoczna || ''}}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
      grades: [
        {
          Przedmiot: 'Zajęcia z wywchowawcą',
          Pozycja: 1,
          OcenyCzastkowe: [
            {
              Nauczyciel: 'Karolina Kowalska',
              Wpis: 3,
              NazwaKolumny: 'Aktywność',
              KodKolumny: 'Akt',
              DataOceny: '14.09.2018',
              KolorOceny: 0,
              dialog: false,
            },
            {
              Nauczyciel: 'Karolina Kowalska',
              Wpis: 4,
              Waga: 5,
              NazwaKolumny: 'Aktywność',
              KodKolumny: 'Akt',
              DataOceny: '29.09.2018',
              KolorOceny: 0,
              dialog: false,
            },
          ],
          ProponowanaOcenaRoczna: 4,
          OcenaRoczna: 4,
          ProponowanaOcenaRocznaPunkty: 1,
          OcenaRocznaPunkty: 2,
          Srednia: 4.13,
          SumaPunktow: '123/200 (61,5%)',
          WidocznyPrzedmiot: false,
        },
        {
          Przedmiot: 'Język polski',
          Pozycja: 3,
          OcenyCzastkowe: [
            {
              Nauczyciel: 'Zofia Czerwińska',
              Wpis: 3,
              Waga: 5,
              NazwaKolumny: '',
              KodKolumny: 'Kart',
              DataOceny: '15.09.2018',
              KolorOceny: 7261447,
              dialog: false,
            },
            {
              Nauczyciel: 'Zofia Czerwińska',
              Wpis: 3,
              Waga: 6,
              NazwaKolumny: 'Egzamin próbny',
              KodKolumny: 'Spr',
              DataOceny: '30.09.2018',
              KolorOceny: 15748172,
              dialog: false,
            },
            {
              Nauczyciel: 'Zofia Czerwińska',
              Wpis: 4,
              Waga: 3,
              NazwaKolumny: '',
              KodKolumny: 'Kart',
              DataOceny: '15.10.2018',
              KolorOceny: 7261447,
              dialog: false,
            },
            {
              Nauczyciel: 'Zofia Czerwińska',
              Wpis: 4,
              Waga: 1,
              NazwaKolumny: '',
              KodKolumny: 'Akt',
              DataOceny: '15.10.2018',
              KolorOceny: 0,
              dialog: false,
            },
          ],
          ProponowanaOcenaRoczna: 3,
          OcenaRoczna: 5,
          ProponowanaOcenaRocznaPunkty: 3.5,
          OcenaRocznaPunkty: 5,
          Srednia: 4.1,
          SumaPunktow: '234/300 (78%)',
          WidocznyPrzedmiot: false,
        },
      ],
    };
  },
};
</script>
