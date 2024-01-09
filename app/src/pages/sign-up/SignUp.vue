<script setup lang="ts">


// import {defineComponent} from "vue";
import {Ref, ref} from 'vue';
import Button from "primevue/button";
import Password from "primevue/password";
import InputText from "primevue/inputtext";
import router from "../../router.ts";
import {useToast} from "primevue/usetoast";
import Toast from "primevue/toast";


let userName : Ref<string>= ref("");
let password : Ref<string> = ref("");

let isLoading : Ref<boolean> = ref(false);

const toast = useToast();

const login = async () => {
  isLoading.value = true;
  console.log(`Login with\nUserName: ${userName.value} Password:${password.value}`)


  const url = "https://keybattler.poslam.ru/api/v1/auth/signup";
  const data = {
    nickname: userName.value,
    password: password.value
  };

  let response: Response | null = await fetch(url, {
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
          life: 900
        });

        return null;

      });


  isLoading.value = false;

  if (response == null) return;

  if (response.status == 400){


    toast.add({
      severity: 'warn',
      summary: 'UserName',
      detail: 'Username is already taken',
      group: 'bl',
      life: 900
    });

    return;
  }

}

const  openLogin = () => {
  router.push("/");
}


</script>

<template>

  <div class="main-container">

    <Toast  position="bottom-left" group="bl" />
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