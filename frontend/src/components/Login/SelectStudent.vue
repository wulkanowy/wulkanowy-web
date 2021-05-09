<template>
<div id="App">
  <v-row align="center">
    <v-col cols="12">
      <div id="nag">Wybierz ucznia</div>
      <v-radio-group>
        <v-radio
          v-model="selectedStudent"
          v-for="student in this.$store.state.loginData.data.students.data"
          :key="student.UczenPelnaNazwa"
          :label="student.UczenPelnaNazwa">
        </v-radio>
      </v-radio-group>
    </v-col>
    <v-col cols="12">
      <v-btn id="buttonOne" text color="red" elevation="2"
        outlined :disabled="inputDisabled" @click="back()"
      >Cofnij</v-btn>
      <v-btn id="buttonTwo" dark color="red" elevation="2"
        @click="chooseClicked()" :disabled="inputDisabled"
      >Wybierz</v-btn>
    </v-col>
  </v-row>
</div>
</template>

<script>
export default {
  name: 'SelectStudent',
  data() {
    return {
      s: '',
      radioGroup: 1,
      selectedStudent: '',
      studentList: {
        type: Array,
      },
    };
  },
  beforeMount() {
    console.log(this.$store.state.loginData.data.students.data[0]);
  },
  methods: {
    async chooseClicked() {
      this.$store.state.selectedUser = this.selectedStudent;
      this.$store.state.showStudentsList = true;
      await this.$router.push('/user');
    },
    back() {
      this.$store.state.showStudentsList = false;
    },
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
