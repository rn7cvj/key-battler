<script setup lang="ts">

import {onMounted, Ref, ref} from 'vue';

import router from "../../router.ts";

import Button  from "primevue/button";
import Column from "primevue/column";
import DataTable from "primevue/datatable";
import Skeleton from "primevue/skeleton";
import Toast from "primevue/toast";

import {useToast} from "primevue/usetoast";
import SearchBar from "./components/SearchBar.vue";
import { ILeader } from "../../interface/leader.ts";


const back = () => {router.back()};

const toast = useToast();

let isLoading : Ref<boolean> = ref(true);

onMounted(() => fetchLeaderBoard() );

const fetchLeaderBoard = async  () => {

  isLoading.value = true;

  const url = "https://keybattler.poslam.ru/api/v1/rating/view";

  let response : Response | null = await fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    },
  }).catch(
      (error) => {

        console.log(error);

        toast.add(
            {
              severity: 'error',
              summary: 'Error',
              detail: 'Server is temporarily unavailable, can`t load leader board',
              group: 'bl',
              life: 1500
            }
        )

        return null;
      }
  )

  if (response == null) return;

  if (!response.ok)
  {
    toast.add(
        {
          severity: 'error',
          summary: 'Error',
          detail: 'Server is temporarily unavailable, can`t load leader board',
          group: 'bl',
          life: 1500
        }
    )
    return ;
  }

  let data = await  response.json();

  fullLeaderList = data.map((d :any) =>{
    let  leader : ILeader = {
      resultId : d['result_id'] ,
      nickName : d['nickname'],
      speed : d['speed'] ,
      correctRate : d['correct_rate'],
      score : d['score'],
    }
    return leader;
  });

  leaderList.value = fullLeaderList

  if (leaderList.value.length == 0){
    toast.add(
        {
          severity: 'info',
          summary: 'Info',
          detail: 'Leader board is empty',
          group: 'bl',
          life: 3000
        }
    )

  }

  isLoading.value = false;
}


let  fullLeaderList : ILeader[] = []
const leaderList : Ref<ILeader[]> = ref([])

const sortLeaderList = (nickName : string , speedRanger : number[] , correctionRange : number[] , scoreRange : number[]) : ILeader[] => {

  let sortedLeader  : ILeader[] = fullLeaderList;

  if (nickName != undefined &&  nickName.length != 0)  sortedLeader = sortedLeader.filter((l : ILeader) => l.nickName.includes(nickName))

  sortedLeader = sortedLeader.filter((l : ILeader) =>  speedRanger[0] <= l.speed && l.speed <= speedRanger[1]);
  sortedLeader = sortedLeader.filter((l : ILeader) =>  correctionRange[0] <= l.correctRate && l.correctRate <= correctionRange[1]);
  sortedLeader = sortedLeader.filter((l : ILeader) =>  scoreRange[0] <= l.score && l.score <= scoreRange[1]);

  return  sortedLeader
}

const searchLeaderList = (nickName : string , speedRanger : number[] , correctionRange : number[] , scoreRange : number[])  => {
  console.log(`Search\n\tNickName: ${nickName}\n\tSpeedRange: ${speedRanger}\n\tCorrectionRange: ${correctionRange}\n\tScoreRange: ${scoreRange}`)



  isLoading.value = true

  leaderList.value = sortLeaderList(nickName , speedRanger , correctionRange , scoreRange)


  if (leaderList.value.length == 0) {
    toast.add(
        {
          severity: 'info',
          summary: 'Info',
          detail: 'Leader board is empty',
          group: 'bl',
          life: 3000
        }
    )
  }

isLoading.value = false ;

}

</script>

<template>

  <Toast  position="bottom-left" group="bl" />


  <div style="width: 100%; height : 80px; align-items: center; display: flex; justify-content: space-between ">
    <Button type="button"
            label="Back"
            icon="pi pi-arrow-left"
            style="margin-left: 10px"
            @click="back" />

    <Button type="button"
            style="margin-right: 10px"
            label="Refresh"
            :icon = "isLoading ? 'pi pi-spinner pi-spin' : 'pi pi-refresh' "
            :disabled=isLoading
            @click="fetchLeaderBoard"/>
  </div>


  <div class="main-container leader-board-container">

    <h1>Leader Board</h1>


    <SearchBar
      :is-loading="isLoading"
      @search="searchLeaderList"
    />


    <div class="card" >

      <DataTable :value="[0 , 1 ,2 ,3]" tableStyle="width: 50vw;"  size="large" v-if="isLoading || leaderList.length == 0">
        <Column field="nickname" header="Nickname" style="width: 40%">
          <template #body>
            <Skeleton :animation="leaderList.length == 0 ? 'none' : 'wave'"/>
          </template>
        </Column>
        <Column field="speed" :sortable="true" header="Speed" style="width: 20%">
          <template #body>
            <Skeleton :animation="leaderList.length == 0 ? 'none' : 'wave'"/>
          </template>
        </Column>
        <Column field="correct_rate" :sortable="true"  header="Correction" style="width: 20%">
          <template #body>
            <Skeleton :animation="leaderList.length == 0 ? 'none' : 'wave'"/>
          </template>
        </Column>
        <Column field="score" :sortable="true" header="Score" style="width: 20%">
          <template #body>
            <Skeleton  :animation="leaderList.length == 0 ? 'none' : 'wave'" />
          </template>
        </Column>
      </DataTable>

      <DataTable :value="leaderList" tableStyle="width: 50vw;" size="large" v-if="!isLoading && leaderList.length > 0"  >
        <Column field="nickName" header="Nickname"></Column>
        <Column field="speed" :sortable="true"  header="Speed"></Column>
        <Column field="correctRate" :sortable="true" header="Correction"></Column>
        <Column field="score" :sortable="true" header="Score"></Column>
      </DataTable>


    </div>



  </div>

</template>

<style scoped>

.leader-board-container{
  justify-content: start;
  align-items: center;
}

.shimmer{

  display: flex;
  height : 220px;
  justify-content: space-between;
  flex-direction: column;

}

.card{
  background: var(--surface-card);

  border-radius: 10px;


  padding: 40px;
}


</style>