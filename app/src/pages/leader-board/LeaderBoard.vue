<script  lang="ts">

import {defineComponent} from "vue";


export default defineComponent(
    {
      data(){
        return {
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
      }
    }
)

</script>

<template>
  <div style="width: 100vh">

    <h1>Leader Board</h1>

    <ul class="list-group">
      <li v-for="leader in leaderList" class="list-group-item">{{leader.name}} :  {{leader.score}}</li>

    </ul>
  </div>
</template>

<style scoped>

</style>