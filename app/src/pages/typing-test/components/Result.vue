<script setup lang="ts">

import Card from "primevue/card";
import Button from "primevue/button";
import {Ref , ref} from "vue";
import {useToast} from "primevue/usetoast";

const toast = useToast();
const isSending : Ref<boolean> = ref(false);

const props = defineProps({
  textId: {type: Number, required: true,},
  speed: {type: Number, required: true,},
  correction: {type: Number, required: true,},
})

const sendResult = async  () => {

  const url = `https://keybattler.poslam.ru/api/v1/rating/add_result`
  const token = localStorage.getItem('token') ?? ""

  const data = {
    text_id: props.textId,
    speed: props.speed,
    correct_rate: props.correction
  }



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
      <Button label="Send result"
              :loading="isSending"
              @click="sendResult"

      />
    </template>

  </Card>

</template>

<style scoped>

</style>