<template>
  <div>
    <div>
      <v-app-bar app color="red darken-1" dark>
        <v-app-bar-nav-icon
        @click.stop="changeDrawerState()">
        </v-app-bar-nav-icon>
        <v-toolbar-title>{{ this.$store.state.appbarTitle }}<br>
        </v-toolbar-title>

        <v-spacer/>
        <v-dialog v-model="DialogSemestr" max-width="300" class="pa-2"
        v-if="this.$store.state.group === 1">
          <v-card>
            <v-card-title>Change semestr</v-card-title>
            <v-radio-group class="pr-4 pl-4" v-model="this.$store.state.semestr">
              <v-radio label="Semestr 1" value="1" key="1" style="width: auto"></v-radio>
              <v-radio label="Semestr 2" value="2" key="2" style="width: auto"></v-radio>
            </v-radio-group>
            <v-card-actions>
              <v-spacer />
              <v-btn text color="primary darken-2" @click="DialogSemestr = false">Close</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
            <v-btn icon @click="DialogSemestr = true" class="mr-3">
            <v-icon>mdi-calendar-multiple</v-icon>
            </v-btn>
          <v-menu offset-y class="text-center" style="width: 200px">
            <template v-slot:activator="{ on }">
                <v-avatar
                  style="cursor: pointer;"
                  v-on="on"
                  color="blue"
                  size="48">
                  <span class="white--text headline">{{ initials }}</span>
                </v-avatar>
            </template>
            <v-list>
              <v-list-item @click="changeStudent" link>
                <v-icon>mdi-account-arrow-right</v-icon>
                <v-list-item-title>Change Student</v-list-item-title>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item @click="logout" link>
                <v-icon>mdi-logout</v-icon>
                <v-list-item-title>Logout</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
          <template v-slot:extension>
            <v-tabs
            v-model="$store.state.tabGrades"
            fixed-tabs
            >
          <v-tabs-slider></v-tabs-slider>

          <v-tab>
            DETAILS
          </v-tab>
          <v-tab>
            SUMMARY
          </v-tab>
          <v-tab>
            CLASS
          </v-tab>
        </v-tabs>
          </template>
      </v-app-bar>
    </div>
  </div>
</template>

<script>
import router from '../../router';

export default {
  name: 'Appbar',
  data: () => ({
    name: 'Dashboard',
    onAvatarClicked: false,
    initials: 'LE',
    DialogSemestr: false,
  }),
  beforeMount() {
    this.initials = this.getInitials();
  },
  methods: {
    changeDrawerState() {
      this.$store.state.drawer = !this.$store.state.drawer;
    },
    async logout() {
      document.cookie = '';
      this.$store.state.showStudentsList = false;
      this.$store.state.loginData = null;
      await router.push('/');
    },
    async changeStudent() {
      await router.push('/');
    },
    getInitials() {
      const index = this.$store.state.selectedStudent;
      return this.$store.state.loginData.data.students.data[index].UczenImie.charAt(0)
        + this.$store.state.loginData.data.students.data[index].UczenNazwisko.charAt(0);
    },
  },
};
</script>

<style scoped>

</style>
