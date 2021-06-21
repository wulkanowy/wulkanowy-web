<template>
  <div id="Class" style="width: 93.5%; margin: 1.5% 3%;">
    <v-card v-if="this.$store.state.windowWidth < 1001" flat width="100%">
      <v-card-text>
        <v-radio-group row v-model="this.chart">
          <v-row justify="center">
            <v-radio label="Partial"></v-radio>
            <v-radio label="Semestr"></v-radio>
            <v-radio label="Points"></v-radio>
          </v-row>
        </v-radio-group>
      </v-card-text>
      <v-card-title>Język polski</v-card-title>
      <v-card flat v-if="this.chart === 0">
        <apexchart
        type="pie" width="100%" :options="MobilechartOptions" :series="series"></apexchart>
      </v-card>
      <v-card flat v-if="this.chart === 1">
        <apexchart
        type="pie" width="100%" :options="MobilechartOptions" :series="series"></apexchart>
      </v-card>
      <v-card flat v-if="this.chart === 2">
        <apexchart
        type="pie" width="100%" :options="MobilechartOptions" :series="series"></apexchart>
      </v-card>
    </v-card>
    <v-card v-if="this.$store.state.windowWidth > 1000">
      <v-card-text>
        <v-radio-group row v-model="chart">
          <v-row justify="center">
            <v-radio label="Partial"></v-radio>
            <v-radio label="Semestr"></v-radio>
            <v-radio label="Points"></v-radio>
          </v-row>
        </v-radio-group>
      </v-card-text>
      <v-card-title>Język polski</v-card-title>
      <v-card flat v-if="this.chart === 0">
        <apexchart
        type="donut" width="65%" :options="chartOptions" :series="series"></apexchart>
      </v-card>
      <v-card flat v-if="this.chart === 1">
        <apexchart
        type="donut" width="65%" :options="chartOptions" :series="series"></apexchart>
      </v-card>
      <v-card flat v-if="this.chart === 2">
        <apexchart
        type="donut" width="65%" :options="chartOptions" :series="series"></apexchart>
      </v-card>
    </v-card>
  </div>
</template>
<script>
import Vue from 'vue';
import VueApexCharts from 'vue-apexcharts';

Vue.use(VueApexCharts);
Vue.component('apexchart', VueApexCharts);

export default {
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      chart: 2,
      series: [5, 24, 42, 63, 65, 60],
      chartOptions: {
        colors: ['#3dbbf5', '#4caf50', '#a0c431', '#ffb940', '#ff774d', '#d43f3f'],
        chart: {
          height: '40vh',
          type: 'donut',
          animations: {
            enabled: false,
          },
          fontFamily: 'Roboto, sans-serif',
          label: true,
        },
        legend: {
          position: 'bottom',
          markers: {
            radius: 0,
          },
        },
        labels: ['6, 6-', '5, 5-, 5+', '4, 4-, 4+', '3, 3-, 3+', '2, 2-, 2+', '1, 1+'],
        plotOptions: {
          pie: {
            expandOnClick: false,
            donut: {
              size: '60%',
              labels: {
                show: true,
                value: {
                  show: true,
                  fontSize: '17px',
                  fontFamily: 'Helvetica, Arial, sans-serif',
                  color: undefined,
                  offsetY: 16,
                  formatter: (val) => val,
                },
                name: {
                  show: true,
                  fontSize: '13px',
                  fontFamily: 'Rubik',
                  color: '#dfsda',
                  offsetY: -10,
                },
                total: {
                  show: true,
                  label: 'Total',
                  color: '#373d3f',
                },
              },
            },
          },
        },
      },
      MobilechartOptions: {
        colors: ['#3dbbf5', '#4caf50', '#a0c431', '#ffb940', '#ff774d', '#d43f3f'],
        chart: {
          height: '40vh',
          type: 'donut',
          animations: {
            enabled: false,
          },
          fontFamily: 'Roboto, sans-serif',
          label: true,
        },
        legend: {
          position: 'bottom',
          markers: {
            radius: 0,
          },
        },
        labels: ['6, 6-', '5, 5-, 5+', '4, 4-, 4+', '3, 3-, 3+', '2, 2-, 2+', '1, 1+'],
      },
    };
  },
};
</script>
