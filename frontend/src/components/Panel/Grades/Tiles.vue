<template>
  <div id="Tiles" class="pa-md-4">
    <v-item-group id="Normal" v-if="this.$store.state.windowWidth > 1000">
      <v-row justify="center">
        <v-card width="30%" style="margin: 1.5%" height="100px">
          <v-card-title class="text-h4">4.60</v-card-title>
          <v-card-subtitle>Calculated average</v-card-subtitle>
        </v-card>
        <v-card width="30%" style="margin: 1.5%" height="100px">
          <v-card-title class="text-h4">--.--</v-card-title>
          <v-card-subtitle>
            Final average
            <v-btn icon @click="dialog = true">
              <v-icon>mdi-help-circle-outline</v-icon>
            </v-btn>
          </v-card-subtitle>
        </v-card>
        <v-card width="30%" style="margin: 1.5%" height="100px">
          <v-card-title class="text-h4">6</v-card-title>
          <v-card-subtitle>Latest grade</v-card-subtitle>
        </v-card>
      </v-row>
    </v-item-group>
    <!-- jeśli to znalazłeś to masz szczęście -->
    <v-item-group id="Mobile" v-if="this.$store.state.windowWidth < 1001" class="mt-3">
      <v-row justify="center">
        <v-card width="40%" flat style="margin: 5%;">
          <v-card-subtitle class="text-center black--text">Calculated average</v-card-subtitle>
          <v-card-text class="text-h4 text-center black--text">4.50</v-card-text>
        </v-card>
        <v-card width="40%" flat style="margin: 5%;">
            <v-card-subtitle class="text-center black--text">
              Final average
            <v-btn icon @click="dialog = true" style="width: 20px; height: 20px;">
                <v-icon color="black" size="20">mdi-help-circle-outline</v-icon>
              </v-btn>
            </v-card-subtitle>
            <v-card-text class="text-h4 text-center black--text">--.--</v-card-text>
        </v-card>
        </v-row>
    </v-item-group>
      <v-dialog v-model="dialog" max-width="700">
        <v-card>
          <v-card-title>
            How the final average is calculated?
          </v-card-title>
          <v-card-text>
            Średnia końcowa jest obliczna ze wszystkich ocen końcowych
            <strong>dotychczas wystawionych</strong>
            z drugiego semestru, dwóch semestrów lub wszystkich ocen z całego roku.
            Domyślnie średnia końcowa jest obliczna z ocen końcowych z drugiego semestru.
            <br>
            <strong>Aby to zmienić wejdź w</strong>
            <v-icon>mdi-cog</v-icon><strong> Ustawienia</strong>
            <v-icon>mdi-chevron-right</v-icon>
            <strong>Zaawansowane</strong>
            <v-icon>mdi-chevron-right</v-icon>
            <strong>Obliczanie średniej końcoworocznej</strong>.
          </v-card-text>
          <v-card-title>Przykłady</v-card-title>
            <v-card-text>
              <strong>Jeżeli średnia końcowa jest obliczona ze
                wszystkich ocen końcowych
              z drugiego lub dwóch semestrów:</strong><br>
              5 + 3 + 6 (wszystkie wystawione oceny końcowe) : 3 (ilość ocen) = 4.66
              (wynik, średnia końcowa)<br><br>
               <strong>Jeżeli średnia końcowa jest obliczona ze wszystkich
              ocen z całego roku:</strong><br>
            5 + 4 + 2 + 5 + 2 (wszystkie wystawione oceny podczas całego roku) :
            5 (ilośc ocen podczas całego roku) = 3.60 (wynik, średnia końcowa)
            </v-card-text>
          <v-card-actions>
            <v-spacer/>
            <v-btn text @click="dialog = !dialog" color="primary darken-2">
              Close
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
  </div>
</template>
<script>
export default {
  data() {
    return {
      dialog: false,
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
