<template>
  <v-app class="pa-md-4">
    <v-main>
      <section id="tiles" v-if="window.width > 700">
        <v-item-group>
          <v-row justify="center">
        <v-card width="31%" min-width="200px" style="margin: 1.5%;">
          <v-card-title class="text-h4">4.50</v-card-title>
          <v-card-subtitle>Przewidywana średnia</v-card-subtitle>
        </v-card>
        <v-card width="30%" min-width="200px"  style="margin: 1.5%;">
          <v-card-title class="text-h4">--.--</v-card-title>
          <v-card-subtitle>Końcowa średnia</v-card-subtitle>
        </v-card>
        <v-card width="30%" min-width="200px"  style="margin: 1.5%;">
          <v-img src="#"/>
          <v-card-subtitle>Wykres ilości 6, 5, ...</v-card-subtitle>
        </v-card>
        <v-expansion-panels style="width: 98%;">
            <v-expansion-panel v-for="item in subjects" v-bind:key="item.id">
              <v-expansion-panel-header>
                {{ item.name || 'Błąd wczytywania' }}
                <v-row style="text-align: right;">
                  <v-col class="text--secondary">
                    Średnia: {{ item.average || 'Brak średniej'}}
                    <span style="margin: 10px;" />
                    Ocen: {{ item.grades || 'Brak ocen' }}
                  </v-col>
                </v-row>
              </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-list>
                <v-item-group>
                  <v-row>
                <v-dialog max-width="500" v-model="dialog">
                  <template v-slot:activator="{ on, attrs }">
                <v-list-item link v-bind="attrs" v-on="on" @click="dialog = true">
                  <v-card style="margin-right: 10px;">
                    <v-avatar color="green">
                      <span class="white--text">6</span>
                    </v-avatar>
                  </v-card>
                  <v-list-item-content>
                    <v-list-item-title>Kartkówka</v-list-item-title>
                    <v-list-item-subtitle>11.06.2021r. Waga: 2,00</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                  </template>
                  <v-card max-width="500">
                    <section id="detailsGrade">
                    <v-card-title class="text-h5">
                      <strong>Matematyka</strong>
                    </v-card-title>
                    <v-card-text class="subtitle-1">Kartkówka</v-card-text>
                    <v-card-title class="subtitle-2 grey--text text--darken-2">Date</v-card-title>
                    <v-card-subtitle class="subtitle-1 black--text">11.05.2020r.</v-card-subtitle>
                    <v-card-title class="subtitle-2 grey--text text--darken-2">
                      Teacher
                      </v-card-title>
                    <v-card-subtitle class="subtitle-1 black--text">
                      Marcin Kowalski
                      </v-card-subtitle>
                    <v-card-title class="subtitle-2 grey--text text--darken-2">Color</v-card-title>
                    <v-card-subtitle class="subtitle-1 black--text">Black</v-card-subtitle>
                    </section>
                    <v-card-actions>
                      <v-spacer />
                      <v-btn text color="red darken-2" @click="dialog = false">Close</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
                  </v-row>
                </v-item-group>
              </v-list>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
          </v-row>
      </v-item-group>
      </section>
      <section id="tiles" v-if="window.width < 699">
        <v-item-group>
          <v-row justify="center">
        <v-card width="90%" min-width="200px">
          <v-card-title class="text-h4">4.50</v-card-title>
          <v-card-subtitle>Przewidywana średnia</v-card-subtitle>
        </v-card>
        <v-card width="90%" min-width="200px"  style="margin: 1.5%;">
          <v-card-title class="text-h4">--.--</v-card-title>
          <v-card-subtitle>Końcowa średnia</v-card-subtitle>
        </v-card>
        <v-card width="90%" min-width="200px"  style="margin: 1.5%;">
          <v-img src="#"/>
          <v-card-subtitle>Nie mam pomyślu na ten kafel</v-card-subtitle>
        </v-card>
          </v-row>
      </v-item-group>
    </section>
  </v-main>
</v-app>
</template>
<script>
export default {
  data() {
    return {
      dialog: false,
      subjects: [
        {
          id: 1,
          name: 'Matematyka',
          average: 3.56,
          grades: 0,
        },
      ],
      windowWidth: '',
      window: {
        width: 0,
        height: 0,
      },
    };
  },
  created() {
    window.addEventListener('resize', this.handleResize);
    this.handleResize();
  },
  destroyed() {
    window.removeEventListener('resize', this.handleResize);
  },
  methods: {
    getLoading() {
      return this.$store.state.isLoading;
    },
    handleResize() {
      this.window.width = window.innerWidth;
      this.window.height = window.innerHeight;
    },
  },
};
</script>
