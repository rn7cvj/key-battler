<script setup lang="ts">

import {Ref , ref} from "vue";

import InputText from "primevue/inputtext";
import Button from "primevue/button";
import OverlayPanel from "primevue/overlaypanel";
import Slider from "primevue/slider";

let nickName : Ref<string> = ref("")


const  speedRangeOp = ref();
const speedRange : Ref<number[]> = ref([0 , 300]);
const  openSpeedRangeDialog = (event) => {
  speedRangeOp.value.toggle(event);
}

const  correctionRangeOp = ref();
let correctionRange : Ref<number[]> = ref([0 , 100]);

const  openCorrectionRangeDialog = (event) => {
  correctionRangeOp.value.toggle(event);
}

const  scoreRangeOp = ref();
let scoreRange : Ref<number[]> = ref([0 , 1000]);
const  openScoreRangeDialog = (event) => {
  scoreRangeOp.value.toggle(event);
}


</script>

<template>

  <div class="search-bar">

    <span class="p-input-icon-left p-float-label"  style="width: 35%; ">
      <i class="pi pi-search" />
      <InputText :v-model="nickName" id="nickname" style="width: 100% " />
      <label for="nickname">Nickname</label>
    </span>

    <Button
      label="Speed Range"
      severity="secondary"
      @click="openSpeedRangeDialog"
    />

    <OverlayPanel ref="speedRangeOp">
      <div style="width: 250px; text-align: center">
        <div class="range-dialog-header" style=" ">
          <div  >Current speed range </div>
          <div>{{speedRange[0]}} :  {{speedRange[1]}} </div>
        </div>

        <Slider v-model="speedRange" range />
      </div>
    </OverlayPanel>

    <Button
        label="Correction Range"
        severity="secondary"
        @click="openCorrectionRangeDialog"
    />

    <OverlayPanel ref="correctionRangeOp">
      <div style="width: 250px; text-align: center">
        <div class="range-dialog-header" style=" ">
          <div  >Current correction range </div>
          <div>{{correctionRange[0]}} :  {{correctionRange[1]}} </div>
        </div>

        <Slider v-model="correctionRange" range />
      </div>
    </OverlayPanel>

    <Button
        label="Score Range"
        severity="secondary"
        @click="openScoreRangeDialog"
    />

    <OverlayPanel ref="scoreRangeOp">
      <div style="width: 250px; text-align: center">
        <div class="range-dialog-header" style=" ">
          <div  >Current correction range </div>
          <div>{{scoreRange[0]}} :  {{scoreRange[1]}} </div>
        </div>

        <Slider v-model="scoreRange" range />
      </div>
    </OverlayPanel>

  </div>


</template>

<style scoped>

.search-bar{

  width: 50vw;

  padding-top: 20px;
  padding-bottom: 40px;

  display: flex;

  flex-direction: row;

  justify-content: space-evenly;
  align-items: center;

}

.range-dialog-header {
  padding-bottom: 20px;

  display: flex;

  flex-direction: row;
  justify-content: space-between;
}

</style>