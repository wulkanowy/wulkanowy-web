<template>
<div id="Details" style="width: 93.5%; margin: 1.5% 3%;">
  <v-row justify="center">
    <v-card flat v-if="this.grades.length < 1">
      <v-row>
      <v-card-title>
        <v-icon color="black" class="text-h3">mdi-numeric-6-box-multiple-outline</v-icon>
      </v-card-title>
      <v-card-title>
        No grades
      </v-card-title>
      </v-row>
    </v-card>
    <v-expansion-panels min-width="200px" v-if="this.$store.state.windowWidth > 1000">
      <v-expansion-panel v-for="item in grades" v-bind:key="item.Pozycja">
        <v-expansion-panel-header>
          {{ item.Przedmiot }}
          <span class="text--secondary ml-3">
            <!-- Nie zrobione obliczanie średniej gdy szkoła wyłączy -->
            Average: {{ item.Srednia || 'no'}}
            <!-- Nie zrobione -->
            Grades: 2
          </span>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-list>
            <v-list-item v-for="ites in item.OcenyCzastkowe"
            v-bind:key="ites.Wpis" @click="ites.dialog = true" link>
              <v-card class="mr-2" flat>
                <v-avatar :class="'G' + ites.Wpis">
                    <span class="white--text">{{ ites.Wpis }}</span>
                </v-avatar>
              </v-card>
              <v-list-item-content>
                <v-list-item-title>
                  {{ ites.NazwaKolumny || ites.KodKolumny || 'no' }}
                </v-list-item-title>
                <v-list-item-subtitle>
                  Date: {{ ites.DataOceny || 'no'  }}
                  <span class="mr-2" />
                  Waga: {{ ites.Waga || 'no'  }}
                </v-list-item-subtitle>
              </v-list-item-content>
              <v-dialog max-width="500" v-model="ites.dialog">
                <v-card>
                  <v-card-title class="text-h5 black--text">
                    <strong>
                      {{ item.Przedmiot || 'no'  }}
                    </strong>
                  </v-card-title>
                  <v-card-text class="subtitle-1">
                    {{ ites.NazwaKolumny || ites.KodKolumny || 'no'  }}
                  </v-card-text>
                  <v-card-title class="subtitle-2 grey--text text--darken-2">
                    Column Code
                  </v-card-title>
                  <v-card-subtitle class="subtitle-1 black--text">
                    {{ ites.KodKolumny || 'no'  }}
                  </v-card-subtitle>
                  <v-card-title class="subtitle-2 grey--text text--darken-2">
                    Date
                  </v-card-title>
                  <v-card-subtitle class="subtitle-1 black--text">
                    {{ ites.DataOceny || 'no'  }}
                  </v-card-subtitle>
                  <v-card-title class="subtitle-2 grey--text text--darken-2">
                    Teacher
                  </v-card-title>
                  <v-card-subtitle class="subtitle-1 black--text">
                    {{ ites.Nauczyciel || 'no'  }}
                  </v-card-subtitle>
                  <v-card-title class="subtitle-2 grey--text text--darken-2">
                    Waga
                  </v-card-title>
                  <v-card-subtitle class="subtitle-1 black--text">
                    {{ ites.Waga || 'no' }}
                  </v-card-subtitle>
                  <v-card-actions>
                    <v-spacer />
                    <v-btn text color="primary darken-2" @click="ites.dialog = false">Close</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-list-item>
          </v-list>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
    <v-expansion-panels min-width="200px"
    class="mt-4 elevation-0" v-if="this.$store.state.windowWidth < 1001" flat>
      <v-expansion-panel v-for="item in grades" v-bind:key="item.Pozycja">
        <v-expansion-panel-header>
          {{ item.Przedmiot }}
          <span class="text--secondary ml-3">
            <!-- Nie zrobione obliczanie średniej gdy szkoła wyłączy -->
            Average: {{ item.Srednia || 'no'}}
            <!-- Nie zrobione -->
            Grades: 2
          </span>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-list>
            <v-list-item v-for="ites in item.OcenyCzastkowe"
            v-bind:key="ites.Wpis" @click="ites.dialog = true" link>
              <v-card class="mr-2" flat>
                <v-avatar :class="'G' + ites.Wpis">
                    <span class="white--text">{{ ites.Wpis }}</span>
                </v-avatar>
              </v-card>
              <v-list-item-content>
                <v-list-item-title>
                  {{ ites.NazwaKolumny || ites.KodKolumny || 'no' }}
                </v-list-item-title>
                <v-list-item-subtitle>
                  Date: {{ ites.DataOceny || 'no'  }}
                  <span class="mr-2" />
                  Waga: {{ ites.Waga || 'no'  }}
                </v-list-item-subtitle>
              </v-list-item-content>
              <v-dialog max-width="500" v-model="ites.dialog">
                <v-card>
                  <v-card-title class="text-h5 black--text">
                    <strong>
                      {{ item.Przedmiot || 'no'  }}
                    </strong>
                  </v-card-title>
                  <v-card-text class="subtitle-1">
                    {{ ites.NazwaKolumny || ites.KodKolumny || 'no' }}
                  </v-card-text>
                  <v-card-title class="subtitle-2 grey--text text--darken-2">
                    Column Code
                  </v-card-title>
                  <v-card-subtitle class="subtitle-1 black--text">
                    {{ ites.KodKolumny || 'no'  }}
                  </v-card-subtitle>
                  <v-card-title class="subtitle-2 grey--text text--darken-2">
                    Date
                  </v-card-title>
                  <v-card-subtitle class="subtitle-1 black--text">
                    {{ ites.DataOceny || 'no'  }}
                  </v-card-subtitle>
                  <v-card-title class="subtitle-2 grey--text text--darken-2">
                    Teacher
                  </v-card-title>
                  <v-card-subtitle class="subtitle-1 black--text">
                    {{ ites.Nauczyciel || 'no'  }}
                  </v-card-subtitle>
                  <v-card-title class="subtitle-2 grey--text text--darken-2">
                    Waga
                  </v-card-title>
                  <v-card-subtitle class="subtitle-1 black--text">
                    {{ ites.Waga || 'no' }}
                  </v-card-subtitle>
                  <v-card-actions>
                    <v-spacer />
                    <v-btn text color="primary darken-2" @click="ites.dialog = false">Close</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-list-item>
          </v-list>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-row>
</div>
</template>
<script>
export default {
  data() {
    return {
      window: {
        width: 0,
        height: 0,
      },
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
          ProponowanaOcenaRoczna: 3,
          OcenaRoczna: 5,
          ProponowanaOcenaRocznaPunkty: 3.5,
          OcenaRocznaPunkty: 5,
          Srednia: 4.1,
          SumaPunktow: '234/300 (78%)',
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
        },
      ],
      dialog: false,
      info: false,
    };
  },
};
</script>
<style>
  .G1{
    background-color: #d43f3f;
  }
  .G2{
    background-color: #ff774d;
  }
  .G3{
    background-color: #ffb940;
  }
  .G4{
    background-color: #a0c431;
  }
  .G5{
    background-color: #4caf50;
  }
  .G6{
    background-color: #3dbbf5;
  }
</style>
