<script setup lang="ts">


// import {defineComponent} from "vue";
import {Ref, ref} from 'vue';
import Button from "primevue/button";
import Password from "primevue/password";
import InputText from "primevue/inputtext";
import router from "../../router.ts";


let userName : Ref<string>= ref("");
let password : Ref<string> = ref("");

let isLoading : Ref<boolean> = ref(false);

const login = () => {
  isLoading.value = true;
  console.log(`Login with\nUserName: ${userName.value} Password:${password.value}`)


  const url = "https://keybattler.poslam.ru/api/v1/auth/login";
  const data = {
    nickname: userName.value,
    password: password.value
  };

  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
      .then(response => response.json())
      .then(data => {
        isLoading.value = false;
        console.log(data);
      })
      .catch(error => {
        isLoading.value = false;
        console.error(error);
      });


}

const  openLogin = () => {
  router.push("/");
}


</script>

<template>

  <div class="main-container">


    <h1>Sign up in keybattler</h1>

    <span class="p-float-label" style="margin-top: 50px" >
        <InputText id="username" v-model="userName"  style="width: 550px" />
        <label for="username">Username</label>
      </span>

    <span class="p-float-label" style="margin-top: 50px">
        <Password v-model="password"
                  inputId="password"
                  :feedback="true"
                  :inputStyle="{width : '550px'}"/>
        <label for="password">Password</label>
      </span>

    <div style="margin-top: 25px">

      <Button type="button" label="Sign Up" :loading="isLoading" @click="login" style="width : 250px; margin-right : 25px;" />

      <Button label="Login" link href="/signup" @click="openLogin"  style="width : 250px; margin-left : 25px;" />


    </div>
  </div>


</template>

<style scoped>

.main-container {

  height : 90vh;
  width : 100%;

  display: flex;
  justify-content: center;
  align-items: center;


  flex-direction: column;


}


</style>