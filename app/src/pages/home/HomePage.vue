<script setup lang="ts">

import Button from "primevue/button";
import  ConfirmDialog from  'primevue/confirmdialog';

import { useConfirm } from "primevue/useconfirm";
import router from "../../router.ts";

const confirm = useConfirm();

const logout = () => {
  confirm.require({
    message: 'Are you convinced that you want to go out?',
    header: 'Logout',
    icon: 'pi pi-sign-out',
    accept: () => {
      localStorage.removeItem("token");
      router.replace("/")
    },
    reject: () => {}
  });
};

const openLeaderBoard = () => {
  router.push("/leader-board");
}

</script>

<template>

  <ConfirmDialog/>

  <div class="main-container">

    <h1 class="text-center p-5">Welcome to Key Battler</h1>

      <Button type="button" label="Start typing test"   style="width : 550px; margin-bottom : 25px;" />

      <Button type="button"  label="Open leader board"  @click="openLeaderBoard" style="width : 550px; margin-bottom : 25px;" />

      <div style="width : 550px; display :flex;  justify-content: end; flex-direction: row;">

        <Button label="Logout" @click="logout"  severity="secondary" />

      </div>


  </div>

</template>

<style scoped>



</style>