<template>
<div id="App">
  <v-row align="center">
    <v-col cols="12">
    </v-col>
    <v-col cols="12">
        <v-text-field color="red" v-model="login" :disabled="inputDisabled"
        label="E-mail" outlined></v-text-field>
        <v-select color="red" v-model="select"
        label="Wybierz odmianę dziennika UONET+" outlined :items="item"
        v-on:change="itemSelected()" item-color="red"></v-select>
        <v-btn id="buttonOne" text color="red" elevation="2"
        outlined @click="back()"
        >Cofnij</v-btn>
        <v-btn id="buttonTwo" dark color="red" elevation="2"
        @click="chooseClicked()"
        >Dalej</v-btn>
    </v-col>
  </v-row>
</div>
</template>

<script>
export default {
  name: 'ResetPassword',
  data() {
    return {
      email: '',
      select: '',
      item: [
        'Vulcan',
        'Fakelog'
      ]
    };
  },
  methods: {

  },
};
</script>

<style>
    #nag{
    text-align: center;
    font-weight: 300;
    font-size: 1.3pc;
    margin-bottom: 1pc;
  }

    #App{
    padding: 10px;
  }

  #buttonTwo{
    margin-left: auto;
    display: block;
  }

  #buttonOne{
    margin-right: auto;
    display: block;
    float: left;
  }
</style>
