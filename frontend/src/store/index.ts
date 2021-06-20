import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    drawer: false,
    group: 1,
    mini: true,
    appbarTitle: 'Grades',
    selectedStudent: 0,
    semestr: 0,
    tabGrades: 3,
    windowWidth: 0,
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  },
});
