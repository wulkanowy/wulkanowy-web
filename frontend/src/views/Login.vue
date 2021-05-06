<template>
  <div id="login">
    <v-main style="width: 100%;">
      <img class="image" src="../assets/logo_login.svg" width="500" alt="Wulkanowy">
      <v-card
        :loading="this.$store.state.isLoading"
        elevation="24"
        id="login-form"
        class="mx-auto">
        <form>
          <v-container>
            <UserLogin v-if="!this.$store.state.showStudentsList"></UserLogin>
            <SelectStudent v-if="this.$store.state.showStudentsList"></SelectStudent>
          </v-container>
        </form>
      </v-card>
    </v-main>
  </div>
</template>

<script>
import UserLogin from '../components/Login/UserLogin.vue';
import SelectStudent from '../components/Login/SelectStudent.vue';

export default {
  name: 'Login',
  components: {
    SelectStudent,
    UserLogin,
  },
  methods: {
    getLoading() {
      return this.$store.state.isLoading;
    },
  },
};
</script>

<style>
::-webkit-scrollbar {
  display: none;
}

#login {
  text-align: center;
  background-position: center center;
  overflow: hidden;
  background-image: url("../assets/wallpaper.jpg");
  background-size: cover;
  height: 100%;
  width: 100%;
}

#login-form {
  width: 500px;
  top: 5%;
  bottom: 50%;
  margin-bottom: 200px;
}

.login-input {
  margin: 10px;
}

.login-button {
  margin: 10px;
}

.image{
  min-width: 350px;
}
</style>
