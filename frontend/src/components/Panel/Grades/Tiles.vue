<template>
  <div id="Tiles" class="pa-md-4">
    <v-item-group id="Normal" v-if="window.width > 1000">
      <v-row justify="center">
        <v-card width="30%" style="margin: 1.5%;" height="100px">
          <v-card-title class="text-h4">4.50</v-card-title>
          <v-card-subtitle>Calculated average</v-card-subtitle>
        </v-card>
        <v-card width="30%" style="margin: 1.5%;" height="100px">
          <v-card-title class="text-h4">--.--</v-card-title>
          <v-card-subtitle>
            Final average
            <v-btn icon @click="dialog = true">
              <v-icon>mdi-help-circle-outline</v-icon>
            </v-btn>
          </v-card-subtitle>
        </v-card>
        <v-card width="30%" style="margin: 1.5%;" height="100px">
          <v-card-title class="text-h4">6</v-card-title>
          <v-card-subtitle>Latest grade</v-card-subtitle>
        </v-card>
      </v-row>
    </v-item-group>
    <!-- jeśli to znalazłeś to masz szczęście -->
    <v-item-group id="Mobile" v-if="window.width < 1001">
          <v-row justify="center">
        <v-card width="90%" min-width="200px" style="margin: 1.5%;">
          <v-card-title class="text-h4">4.50</v-card-title>
          <v-card-subtitle>Calculated average</v-card-subtitle>
        </v-card>
        <v-card width="90%" min-width="200px"  style="margin: 1.5%;">
          <v-card-title class="text-h4">--.--</v-card-title>
          <v-card-subtitle>
            Final average
            <v-btn icon @click="dialog = true">
              <v-icon>mdi-help-circle-outline</v-icon>
            </v-btn>
          </v-card-subtitle>
        </v-card>
        <v-card width="90%" min-width="200px"  style="margin: 1.5%;">
          <v-card-title class="text-h4">6</v-card-title>
          <v-card-subtitle>Latest grade</v-card-subtitle>
        </v-card>
          </v-row>
      </v-item-group>
      <v-dialog v-model="dialog" width="700">
        <v-card>
          <v-card-title>
            How the final average is calculated?
          </v-card-title>
          <v-card-text>Kurde sam nie wiem</v-card-text>
          <v-card-actions>
            <v-spacer/>
            <v-btn text @click="dialog = !dialog" color="red">
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
