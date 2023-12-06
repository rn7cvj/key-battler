<script setup lang="ts">

</script>

<template>

    <div class="container" style="width: 30vw">
      <h1 class="p-5">Login</h1>

      <form>
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">UserName</label>
          <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Password</label>
          <input type="password" class="form-control" id="exampleInputPassword1">
        </div>
        <div>
          <a type="submit" class="btn btn-primary m-3" href="/home">Login</a>
<!--          <div class="p-2"/>-->
          <a type="submit" class="btn btn-secondary m-3" href="/signup">SignUp</a>
        </div>
      </form>
    </div>

</template>

<style scoped>

</style>