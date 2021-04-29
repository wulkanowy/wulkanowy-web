<template>
  <div>
    <div>
      <v-app-bar
        app
        color="primary"
        dark>
        <v-app-bar-nav-icon @click="changeDrawerState()"></v-app-bar-nav-icon>
        <v-toolbar-title>Wulkanowy - {{ this.$store.state.appbarTitle }}</v-toolbar-title>
        <v-spacer></v-spacer>
          <v-menu offset-y class="text-center" style="width: 200px">
            <template v-slot:activator="{ on }">
                <v-avatar
                  v-on="on">
                  <v-img src="https://cdn.discordapp.com/avatars/227024178488934400/050b9a94fe416c581249d1ca79bd18a4.webp?size=128"/>
                </v-avatar>
            </template>
            <v-list>
              <v-list-item link>
                <v-icon>mdi-account-arrow-right</v-icon>
                <v-list-item-title>Change Student</v-list-item-title>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item link>
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
  },
};
</script>

<style scoped>

</style>
