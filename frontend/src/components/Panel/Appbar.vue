<template>
  <div>
    <div>
      <v-app-bar
        app
        color="primary"
        dark>
        <v-app-bar-nav-icon
          @click="changeDrawerState">
        </v-app-bar-nav-icon>
        <v-toolbar-title>Wulkanowy - {{ this.$store.state.appbarTitle }}</v-toolbar-title>
        <v-spacer></v-spacer>
          <v-menu offset-y class="text-center" style="width: 200px">
            <template v-slot:activator="{ on }">
                <v-avatar
                  v-on="on">
                  <span class="white--text headline">CJ</span>
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
  }),
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
  },
};
</script>

<style scoped>

</style>
