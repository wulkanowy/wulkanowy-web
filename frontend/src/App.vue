<template>
  <v-app>
    <router-view />
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "App",

  beforeMount() {
    let dark_theme = localStorage.getItem("dark_theme");
    if (dark_theme) {
      if (dark_theme == "true") {
        this.$vuetify.theme.dark = true;
      } else {
        this.$vuetify.theme.dark = false;
      }
    } else {
      localStorage.setItem("dark_theme", "false");
    }
  },
  created() {
    window.addEventListener("resize", this.handleResize);
    this.handleResize();
  },
  destroyed() {
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
    handleResize() {
      const screen_width = window.innerWidth;
      this.$store.state.small_ui = screen_width < 1264;
    },
  },
});
</script>

<style lang="scss">
.v-card__text,
.v-card__title {
  word-break: normal !important;
}
</style>
