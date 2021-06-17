import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    drawer: true,
    group: 1,
    mini: true,
    appbarTitle: 'Grades',
    selectedStudent: 0,
    semestr: 1,
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  },
});
