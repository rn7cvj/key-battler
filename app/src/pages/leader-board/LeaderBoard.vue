<script  lang="ts">

import {defineComponent} from "vue";


export default defineComponent(
    {
      data(){
        this.fetchLeaderBoard()
        return {
          isLoading: true ,
          leaderList : [
          {
            "name" : "kirden04" ,
            "score" : "234",
          },
          {
            "name" : "rn7cvj" ,
            "score" : "224",
          },
        ]
      }
      } ,
      methods: {
        fetchLeaderBoard(){
          this.isLoading = true;

          let result =  fetch(
              "http://poslam.rn7cvj-dev.ru/api/v1/rating/view", {
                method: "GET",
              }
          );

          result.then((value) =>{
            value.json().then((data) => {
              console.log(data);

              this.leaderList = data.map((e) => { return  {"name" : e["nickname"] ,  score : e["score"]}});
            })
            this.isLoading = false;
          })



          // this.isLoading = false;
        }
      }
    }
)

</script>

<template>
  <div style="width: 100vh">

    <h1>Leader Board</h1>


    <div class="spinner-border" role="status" v-if="isLoading">
      <span class="visually-hidden">Loading...</span>
    </div>


    <ul v-if="!isLoading" class="list-group">
      <li v-for="leader in leaderList" class="list-group-item">{{leader.name}} :  {{leader.score}}</li>

    </ul>
  </div>
</template>

<style scoped>

</style>