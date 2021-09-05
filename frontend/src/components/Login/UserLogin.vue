<template>
  <div>
    <v-col cols="12">
      <p class="justify-center text-center headline font-weight-light">
        Zaloguj się za pomocą konta ucznia lub rodzica
      </p>
    </v-col>
    <v-col cols="12">
      <v-text-field
        color="red"
        v-model="login"
        :disabled="inputDisabled"
        label="E-mail"
        outlined
      />
      <v-text-field
        color="red"
        v-model="password"
        :disabled="inputDisabled"
        label="Hasło"
        outlined
        type="password"
      />
      <v-text-field
        color="red"
        v-model="symbol"
        :disabled="inputDisabled"
        label="Symbol"
        outlined
      />
      <v-select
        color="red"
        v-model="selectedSymbol"
        :disabled="inputDisabled"
        label="Wybierz odmianę dziennika UONET+"
        outlined
        :items="domains"
        v-on:change="fakelog()"
        item-color="red"
      />
    </v-col>
    <v-col cols="12">
      <v-btn
        dark
        color="red"
        elevation="2"
        @click="loginUser()"
        class="justify-end"
      >Zaloguj się</v-btn>
    </v-col>
  </div>
</template>
<script>
import Vue from 'vue';
import login from '../../api/login';

export default {
  name: 'UserLogin',
  data() {
    return {
      inputDisabled: false,
      login: '',
      password: '',
      selectedSymbols: '',
      symbols: '',
      domains: [
        'Vulcan',
        'Fakelog',
      ],
    };
  },
  methods: {
    async loginUser() {
      this.inputDisabled = true;
      Vue.set(this.$store.state, 'isLoading', true);
      const response = await login.register(this.login, this.password, this.selectedSymbol);
      this.$store.state.loginData = response.data;
      console.log(this.$store.state.loginData);
      if (this.$store.state.loginData.data.students.data.length > 1) {
        this.$store.state.showStudentsList = true;
        this.$store.state.isLoading = false;
      }
    },

    fakelog() {
      if (this.selectedSymbol === 'Fakelog') {
        this.login = 'jan@fakelog.cf';
        this.password = 'jan123';
        this.symbol = 'powiatwulkanowy';
      }
    },
  },
};
</script>
<style>
  #App{
    padding: 10px;
  }
  #nag{
    text-align: center;
    font-weight: 300;
    font-size: 1.3pc;
    margin-bottom: 1pc;
  }

  #buttonOne{
    margin-right: auto;
    display: block;
    float: left;
  }
</style>
