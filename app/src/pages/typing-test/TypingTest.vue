<script setup lang="ts">

import {Ref, ref, onMounted, watch} from "vue";
import {useStopwatch} from 'vue-timer-hook';
import {useToast} from "primevue/usetoast";

import Knob from "primevue/knob";
import Card from "primevue/card";
import Toast from "primevue/toast";
import Rating from "primevue/rating";
import Skeleton from "primevue/skeleton";
import ProgressBar from "primevue/progressbar";
import {isLetter, isPunctuation} from "./scripts/isLetter.ts";
import Button from "primevue/button";
import router from "../../router.ts";
import Result from "./components/Result.vue";


const stopwatch = useStopwatch(0, false);

watch(
    stopwatch.seconds,
    (second: number) => {
      let totalSecond: number = stopwatch.minutes.value * 60 + second + 1;

      let keyPerSecond: number = correctTypedKeys / totalSecond;

      speedValue.value = Math.round(keyPerSecond * 60);
    }
)

const toast = useToast();

const typedText: Ref<String> = ref("")
const untypedText: Ref<String> = ref("")
const isLoading: Ref<Boolean> = ref(true);
const isTypingTestStart: Ref<Boolean> = ref(false);
const isTypingTestEnd: Ref<Boolean> = ref(false);

const typingProgressValue: Ref<number> = ref(0);
const correctionValue: Ref<number> = ref(0);
const speedValue: Ref<number> = ref(0);

let totalTypedKeys: number = 0;
let correctTypedKeys: number = 0;

let textId: number = -1;

const letterTyped = (key: string) => {

  if (isTypingTestEnd.value) return;

  if (isLoading.value || (!isLetter(key) && !isPunctuation(key))) return;

  if (!stopwatch.isRunning.value) {

    isTypingTestStart.value = true;
    stopwatch.start();
  }

  totalTypedKeys += 1;

  if (key != untypedText.value.charAt(0)) {

    correctionValue.value = Math.round((correctTypedKeys / totalTypedKeys) * 100)

    let totalSecond: number = stopwatch.minutes.value * 60 + stopwatch.seconds.value + 1;

    let keyPerSecond: number = correctTypedKeys / totalSecond;

    speedValue.value = Math.round(keyPerSecond * 60);

    return;
  }

  correctTypedKeys += 1;


  typedText.value += untypedText.value.charAt(0)
  untypedText.value = untypedText.value.substring(1)

  typingProgressValue.value = (correctTypedKeys / (typedText.value.length + untypedText.value.length)) * 100

  correctionValue.value = Math.round((correctTypedKeys / totalTypedKeys) * 100)

  let totalSecond: number = stopwatch.minutes.value * 60 + stopwatch.seconds.value + 1;

  let keyPerSecond: number = correctTypedKeys / totalSecond;

  speedValue.value = Math.round(keyPerSecond * 60);

  if (untypedText.value.length === 0) {
    onTypingTestEnd()
  }

}

const props = defineProps({
  // text : { type : String , required : true } ,
  textRating: {type: Number, required: true}
})

onMounted(async () => {



  await fetchText();
  // fetchMockText();
  window.addEventListener('keydown', (ev: KeyboardEvent) => letterTyped(ev.key));


})

// const fetchMockText = () => {
//   isLoading.value = false;
//   untypedText.value = 'qwerty';
// }

const fetchText = async () => {


  let mapTextRating = {
    3 : 1 ,
    2 : 2 ,
    1 : 3
  }

  let textRatingQ = mapTextRating[props.textRating]

  const url = `https://keybattler.poslam.ru/api/v1/text/generate?tier=${textRatingQ}`
  const token = localStorage.getItem('token') ?? ""

  let response: Response | null = await fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'auth': token
    }
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


  if (response == null) return;

  if (!response.ok) {
    toast.add({
      severity: 'warn',
      summary: '',
      detail: 'Can`t load new text',
      group: 'bl',
      life: 3000
    })

    untypedText.value = "Разнообразный и богатый опыт постоянный количественный рост и сфера нашей активности влечет за собой процесс внедрения и модернизации системы обучения кадров, соответствует насущным потребностям. Задача организации, в особенности же начало повседневной работы по формированию позиции представляет собой интересный эксперимент проверки существенных финансовых и административных условий.";

    isLoading.value = false;

    return;
  }

  let result = await response.json();

  textId = result["id"]
  untypedText.value = result["text"]

  isLoading.value = false;
}

const onTypingTestEnd = () => {

  stopwatch.pause();
  isTypingTestStart.value = false;
  isTypingTestEnd.value = true;

  console.log(`Typing test end with result\n\tSpeed: ${speedValue.value}\n\tCorrection: ${correctionValue.value}\n\tTextId: ${textId}`)

}

const back = () => {
  router.back()
};


</script>

<template>

  <Toast position="bottom-left" group="bl"/>


  <div
      style="width: 100%; height : 80px; align-items: center; display: flex; flex-direction: row;  justify-content: space-between ">

    <Button type="button"
            label="Back"
            icon="pi pi-arrow-left"
            style="margin-left: 10px"
            @click="back"/>

    <div style="display: flex; flex-direction: row; margin-right: 10px">
      <h2 style="margin-right: 20px">Typing test rating:</h2>
      <Rating :stars="3" :model-value="props.textRating" readonly :cancel="false"/>
    </div>
  </div>

  <div class="main-container">

    <div v-if="!isTypingTestEnd" style="width: 100%; display: flex; flex-direction: column; align-items : center; justify-content: center; ">

      <span style="width: 90%" v-if="!isLoading">

      <p> Text typing progress</p>
      <ProgressBar :value="typingProgressValue"
                   style="height: 10px; width: 100%; margin-bottom:40px"> {{}}</ProgressBar>

    </span>

      <Skeleton width="90%" height="200px" v-if="isLoading"/>

      <Card style=" width: 90%;  text-align: center;" v-if="!isLoading">

        <template #title> You`r text</template>
        <template #subtitle v-if="!isTypingTestStart"> Press any key to start</template>
        <template #content>
          <h2 style="margin-bottom: 40px">
          <span class="typed-text">
            {{ typedText }}
          </span>
            <span class="untyped-text">
            {{ untypedText }}
          </span>

          </h2>
        </template>

      </Card>

      <div style="display: flex; flex-direction: row; justify-content: space-evenly; width: 50%; padding-top: 40px;">

        <div style="text-align: center">
          <Knob v-model="correctionValue" readonly/>
          <p>Correction</p>
        </div>

        <div style="text-align: center">
          <Knob v-model="speedValue" :min="0" :max="400" readonly/>
          <p>Speed</p>
        </div>

      </div>

    </div>

    <div v-if="isTypingTestEnd">

      <Result :correction="correctionValue"
              :speed="speedValue"
              :text-id="textId" />

    </div>

  </div>

</template>

<style scoped>

.typed-text {
  color: var(--primary-color)
}

.untyped-text {

}

</style>