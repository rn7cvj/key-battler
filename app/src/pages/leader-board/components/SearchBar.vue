<script setup lang="ts">

import {Ref  , ref} from "vue";

import InputText from "primevue/inputtext";
import Button from "primevue/button";
import OverlayPanel from "primevue/overlaypanel";
import Slider from "primevue/slider";

let nickName : Ref<string> = ref("")


const speedRangeOp = ref();
const speedRangeMinMax : number[] = [0 , 400];
const speedRange : Ref<number[]> = ref(speedRangeMinMax);
const  openSpeedRangeDialog = (event : Event) => {
  speedRangeOp.value.toggle(event);
}

const correctionRangeOp = ref();
const correctionRangeMinMax : number[] = [0 , 100]
const correctionRange : Ref<number[]> = ref(correctionRangeMinMax)

const  openCorrectionRangeDialog = (event:  Event) => {
  correctionRangeOp.value.toggle(event);
}

const scoreRangeOp = ref();
const scoreRangeMinMax : number[]  = [0 , 1000];
const scoreRange : Ref<number[]> = ref(scoreRangeMinMax);
const  openScoreRangeDialog = (event:  Event) => {
  console.log(event)
  scoreRangeOp.value.toggle(event);
}


interface ISearchBarProps {
  isLoading : boolean,
}


const props = defineProps<ISearchBarProps>()

const emits = defineEmits<{
  (e : 'search' , nickName : string , speedRange : Array<number> , correctionRange: Array<number> , scoreRange : Array<number> ) : void
}>()


</script>

<template>

  <div class="search-bar">

    <span class="p-input-icon-left p-float-label"  style="width: 400px; margin: 20px">
      <i class="pi pi-search" />
      <InputText v-model="nickName" id="nickname" style="width: 100% "  :disabled="props.isLoading"/>
      <label for="nickname">Nickname</label>
    </span>

    <Button
      label="Speed Range"
      severity="secondary"
      style="margin: 20px"
      :disabled="props.isLoading"
      @click="openSpeedRangeDialog"
    />

    <OverlayPanel ref="speedRangeOp">
      <div style="width: 300px; text-align: center">
        <div class="range-dialog-header" style=" ">
          <div  >Current speed range </div>
          <div>{{speedRange[0]}} :  {{speedRange[1]}} </div>
        </div>

        <Slider v-model="speedRange" range :min="speedRangeMinMax[0]" :max="speedRangeMinMax[1]" />
      </div>
    </OverlayPanel>

    <Button
        label="Correction Range"
        severity="secondary"
        style="margin: 20px"
        :disabled="props.isLoading"
        @click="openCorrectionRangeDialog"
    />

    <OverlayPanel ref="correctionRangeOp">
      <div style="width: 300px; text-align: center">
        <div class="range-dialog-header" style=" ">
          <div  >Current correction range </div>
          <div>{{correctionRange[0]}} :  {{correctionRange[1]}} </div>
        </div>

        <Slider v-model="correctionRange" range :min="correctionRangeMinMax[0]" :max="correctionRangeMinMax[1]" />
      </div>
    </OverlayPanel>

    <Button
        label="Score Range"
        severity="secondary"
        style="margin: 20px"
        :disabled="props.isLoading"
        @click="openScoreRangeDialog"
    />

    <OverlayPanel ref="scoreRangeOp">
      <div style="width: 300px; text-align: center">
        <div class="range-dialog-header" style=" ">
          <div  >Current correction range </div>
          <div>{{scoreRange[0]}} :  {{scoreRange[1]}} </div>
        </div>

        <Slider v-model="scoreRange" range :min="scoreRangeMinMax[0]" :max="scoreRangeMinMax[1]" />
      </div>
    </OverlayPanel>

    <Button icon="pi pi-search"
            severity="info"
            style="margin: 20px"
            :disabled="props.isLoading"
            @click="emits('search' , nickName , speedRange , correctionRange , scoreRange)"
    />

  </div>


</template>

<style scoped>

.search-bar{


  padding-top: 20px;
  padding-bottom: 40px;

  display: flex;

  flex-direction: row;

  justify-content: center;
  align-items: center;


  flex-wrap: wrap;

}

.range-dialog-header {
  padding-bottom: 20px;

  display: flex;

  flex-direction: row;
  justify-content: space-between;

}

</style>