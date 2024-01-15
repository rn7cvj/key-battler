<script setup lang="ts">


import Card from "primevue/card";
import Button from "primevue/button";
import {Ref , ref} from "vue";
import {useToast} from "primevue/usetoast";
import router from "../../../router.ts";

const toast = useToast();
const isSendAvalible  : Ref<boolean> = ref(true);
const isSending : Ref<boolean> = ref(false);

const props = defineProps({
  textId: {type: Number, required: true,},
  speed: {type: Number, required: true,},
  correction: {type: Number, required: true,},
})

const sendResult = async  () => {

  isSending.value = true;

  const url = `https://keybattler.poslam.ru/api/v1/rating/add_result`
  const token = localStorage.getItem('token') ?? ""

  const data = {
    text_id: props.textId,
    speed: props.speed,
    correct_rate: props.correction
  }

  let response : Response | null = await  fetch(url , {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'auth': token
    },
    body: JSON.stringify(data)
  }).catch((error) => {

    console.log(error);

    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: 'Can`t save result, try again',
      group: 'bl',
      life: 1500
    });

    return null;

  })

  isSending.value = false;

  if (response === null) return;

  if (!response.ok){
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: 'Can`t save result, try again',
      group: 'bl',
      life: 1500
    });
    return;
  }

  toast.add({
    severity: 'success',
    // summary: 'Error',
    detail: 'Successfully send result',
    group: 'bl',
    life: 1500
  });

  isSendAvalible.value = false;


}

const  goHome = () => {
  router.replace("/home")
}

</script>

<template>

  <Card style="width: 400px">
    <template #title>Your result</template>

    <template #content>
      <div style="display: flex; flex-direction: row; justify-content: space-between; font-size: 20px">

        <div>Speed:</div>

        <div  style="display: flex; flex-direction: row">
          <div style="color: var(--primary-color); padding-right: 5px">{{ props.speed }}</div>
          <div>keys/minute</div>
        </div>

      </div>

      <div style="display: flex; flex-direction: row; justify-content: space-between; font-size: 20px">

        <div>Correction:</div>

        <div  style="display: flex; flex-direction: row">
          <div  style="color: var(--primary-color); padding-right: 5px">{{ props.correction }}</div>
          <div>%</div>
        </div>
      </div>

    </template>

    <template #footer>
      <div style="display: flex; flex-direction: row; justify-content: space-between">
        <Button label="Send result"
                :loading="isSending"
                :disabled="!isSendAvalible"
                @click="sendResult"/>
        <Button label="Home"
                :disabled="isSending"
                @click="goHome"/>
      </div>
    </template>

  </Card>

</template>

<style scoped>

</style>