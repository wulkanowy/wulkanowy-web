import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

interface State {
  loading: boolean;
  loginData: any;
  logged_in: boolean;
  selected_student: number;
  small_ui: boolean;
  view: string;
  drawer: {
    show: boolean;
    mini: boolean;
  };
  error: {
    show: boolean;
    description: string;
    details: string;
  };
}

export default new Vuex.Store({
  state: (): State => ({
    loading: false,
    loginData: [],
    logged_in: false,
    selected_student: 0,
    small_ui: false,
    view: "dashboard",
    drawer: {
      show: true,
      mini: false,
    },
    error: {
      show: false,
      description: "",
      details: "",
    },
  }),
  mutations: {},
  actions: {},
  modules: {},
});
