<script setup lang="ts">


// import {defineComponent} from "vue";
import {Ref, ref} from 'vue';

import Toast from "primevue/toast";
import Button from "primevue/button";
import Password from "primevue/password";
import InputText from "primevue/inputtext";

import {useToast} from "primevue/usetoast";

import router from "../../router.ts";

let userName : Ref<string>= ref("");
let password : Ref<string> = ref("");

let isLoading : Ref<boolean> = ref(false);

const toast = useToast();

const login = async () => {
  isLoading.value = true;
  console.log(`Login with\nUserName: ${userName.value} Password:${password.value}`)


  const url = "https://keybattler.poslam.ru/api/v1/auth/login";
  const data = {
    nickname: userName.value,
    password: password.value
  };

  let response : Response | null = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  }).catch(
      (error) => {

        console.log(error);

        toast.add({
          severity: 'error',
          summary: 'Error',
          detail: 'Server is temporarily unavailable',
          group: 'bl',
          life: 1500
        });

        return null;

      });

  isLoading.value = false;

  if (response == null) return;

  if (response.status == 404) {
    toast.add({
      severity: 'warn',
      summary: '',
      detail: 'The username or password you entered is incorrect',
      group: 'bl',
      life: 1500
    })
    return;
  }

  let result = await response.json();

  localStorage.setItem("token" , result["token"])

  console.log(`New token: ${result["token"]}`)

   router.replace("/home")
}

const  openSignUp = () => {
  router.replace("/signup");
}


</script>

<template>

    <Toast  position="bottom-left" group="bl" />

    <div class="main-container card">


      <h1>Login to keybattler</h1>

      <span class="p-float-label" style="margin-top: 50px" >
        <InputText id="username"
                   v-model="userName"
                   :disabled="isLoading"
                   style="width: 550px" />
        <label for="username">Username</label>
      </span>

      <span class="p-float-label" style="margin-top: 50px">
        <Password v-model="password"
                  inputId="password"
                  :feedback="false"
                  :disabled="isLoading"
                  :inputStyle="{width : '550px'}"  />
        <label for="password">Password</label>
      </span>

      <div style="margin-top: 25px">

        <Button type="button" label="Login" :loading="isLoading" @click="login" style="width : 250px; margin-right : 25px;" />

        <Button label="Sign Up" link @click="openSignUp"  style="width : 250px; margin-left : 25px;" />


      </div>
    </div>


</template>

<style scoped>



</style>