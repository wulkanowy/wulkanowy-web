<template>CRLF
  <div id="App">
    <v-row align="center">
      <v-col cols="12">
              <div id="nag">Zaloguj się za pomocą konta ucznia lub rodzica</div>
              <v-text-field color="red" v-model="login" :disabled="inputDisabled"
              label="E-mail" outlined></v-text-field>
              <v-text-field color="red" v-model="password" :disabled="inputDisabled"
              label="Hasło" outlined type="password"></v-text-field>
              <v-text-field color="red" v-model="symbol" :disabled="inputDisabled"
              label="Symbol" outlined></v-text-field>
              <v-select color="red" v-model="selectedSymbol" :disabled="inputDisabled"
              label="Wybierz odmianę dziennika Vulcan" outlined :items="item"
              v-on:change="itemSelected()" item-color="red"></v-select>
              <v-btn id="buttonOne" text color="red" elevation="2" 
              outlined :disabled="inputDisabled">Nie pamiętam hasła</v-btn>
              <v-btn id="buttonTwo" dark color="red" elevation="2" 
              @click="loginUser()">Zaloguj się</v-btn>
      </v-col>
    </v-row>
  </div>
</template>
<script>
import Vue from 'vue';
import SelectStudentVue from './SelectStudent.vue';
// Wywaliłem "import login from '../../api/login';" bo ciągle wywalał
// błąd "Expected 1 empty line after import statement not followed by another import"
export default {
  name: 'UserLogin',
  data() {
    return {
      inputDisabled: false,
      login: '',
      password: '',
      selectedSymbol: '',
      item: [
        'Vulcan',
        'Fakelog',
      ],
    }
  },
  methods: {
    async loginUser() {
      this.inputDisabled = true;
      if (this.login === '' || this.password === '' || this.symbol === '' || this.selectedSymbol === '') {
        this.inputDisabled = false;
        alert('Uzupełnij wszystkie pola!');
      } else {
        alert('To działa');
        Vue.set(this.$store.state, 'isLoading', true);
        const response = await this.login.register(this.login, this.password, this.selectedSymbol);
        this.$store.state.loginData = response.data;
        console.log(this.$store.state.loginData);
        if (this.$store.state.loginData.data.students.data.length > 1) {
          this.$store.state.isLoading = false;
          this.$store.state.showStudentsList = true;
        }
      }
    },
  },
  itemSelected() {
    alert("to działa")
    if (this.selectedSymbol === 'Fakelog') {
      this.login = 'jan@fakelog.cf';
      this.password = 'jan123';
      this.symbol = 'powiatwulkanowy';
    }
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

    #buttonTwo{
    margin-left: auto;
    display: block;
  }
</style>
