<script setup lang="ts">

import { useStopwatch } from 'vue-timer-hook';

const autoStart = true;
const stopwatch = useStopwatch( 0 , autoStart);

let minutes = stopwatch.minutes;

</script>

<template>

  <h2>
   {{minutes}}:{{stopwatch.seconds}}
  </h2>
</template>

<style scoped>

</style>