<template>
  <div>
    <div id="appbar">
      <Appbar></Appbar>
      <Drawer></Drawer>
    </div>
    <v-main>
      <div id="Grades" v-if="this.$store.state.group === 1">
          <GradesTiles></GradesTiles>
          <v-row justify="center">
            <GradesDetails></GradesDetails>
          </v-row>
      </div>
    </v-main>
  </div>
</template>

<script>
import Appbar from '../components/Panel/Appbar.vue';
import Drawer from '../components/Panel/Drawer.vue';
import GradesTiles from '../components/Panel/Grades/Tiles.vue';
import GradesDetails from '../components/Panel/Grades/Details.vue';

export default {
  name: 'Panel',
  components: {
    Appbar,
    Drawer,
    GradesTiles,
    GradesDetails,
  },
};
</script>

<style scoped>

</style>
