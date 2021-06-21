<template>
<v-app>
  <div>
    <div id="appbar">
      <Appbar></Appbar>
      <Drawer></Drawer>
    </div>
    <v-main>
      <div id="Grades" v-if="this.$store.state.group === 1" @load="getOs()">
            <v-tabs-items v-model="$store.state.tabGrades">
              <v-tab-item>
                <GradesTiles v-if="this.$store.state.windowWidth > 1000"></GradesTiles>
                <GradesDetails></GradesDetails>
              </v-tab-item>
              <v-tab-item>
                <GradesTiles></GradesTiles>
                <GradesSummary></GradesSummary>
              </v-tab-item>
              <v-tab-item>
                <GradesTiles v-if="this.$store.state.windowWidth > 1000"></GradesTiles>
                <GradesClass></GradesClass>
              </v-tab-item>
            </v-tabs-items>
      </div>
    </v-main>
  </div>
</v-app>
</template>

<script>
import Appbar from '../components/Panel/Appbar.vue';
import Drawer from '../components/Panel/Drawer.vue';
import GradesTiles from '../components/Panel/Grades/Tiles.vue';
import GradesDetails from '../components/Panel/Grades/Details.vue';
import GradesSummary from '../components/Panel/Grades/Summary.vue';
import GradesClass from '../components/Panel/Grades/Class.vue';

export default {
  name: 'Panel',
  components: {
    Appbar,
    Drawer,
    GradesTiles,
    GradesDetails,
    GradesSummary,
    GradesClass,
  },
  data() {
    return {
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
      this.$store.state.windowWidth = window.innerWidth;
    },
  },
};
</script>
