<script setup lang="ts">


import  {ref , Ref} from "vue";

import { useConfirm } from "primevue/useconfirm";

import router from "../../router.ts";

import Button from "primevue/button";
import Rating from "primevue/rating";
import ConfirmDialog from  'primevue/confirmdialog';
import OverlayPanel from "primevue/overlaypanel";


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

const typingTestSetupOp = ref();
const opneTypeingTestSetup = (event :Event)  => {
  typingTestSetupOp.value.toggle(event);
}


const textRating : Ref<number> = ref(1);

</script>

<template>

  <ConfirmDialog/>

  <div class="main-container">

    <h1 class="text-center p-5">Welcome to Key Battler</h1>

      <Button type="button"
              label="Start typing test"
              style="width : 550px; margin-bottom : 25px;"
              @click="opneTypeingTestSetup"/>

    <OverlayPanel ref="typingTestSetupOp">
      <div style="width: 510px; display: flex; flex-direction: row; align-items: center; justify-content: space-between">
        <div style="display: flex; flex-direction: row;">
          <div style="margin-right: 20px">Select text raiting: </div>
          <Rating v-model="textRating" :cancel="false" />
        </div>
        <Button
        type="button"
        label="Start"
        />

      </div>
    </OverlayPanel>


    <Button type="button"  label="Open leader board"  @click="openLeaderBoard" style="width : 550px; margin-bottom : 25px;" />

      <div style="width : 550px; display :flex;  justify-content: end; flex-direction: row;">

        <Button label="Logout" @click="logout"  severity="secondary" />

      </div>


  </div>

</template>

<style scoped>




</style>