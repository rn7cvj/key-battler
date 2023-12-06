<script  lang="ts">

import {defineComponent} from "vue";


export default defineComponent(
    {

      data(){
        window.addEventListener('keydown' , (ev : KeyboardEvent ) => {
          this.letterType(ev.key)
        });
        return {
          typedText : "",
          untypedText  : "Путешествия - это один из самых увлекательных видов отдыха. Они позволяют увидеть новые места, познакомиться с разными культурами и традициями, а также отдохнуть от повседневной суеты и стресса. Путешествия помогают расширить кругозор и получить новые впечатления.",
        }
      },

      methods:{
        letterType(  key : string ){
          if (key != this.untypedText.charAt(0)){
            return;
          }
          this.typedText += this.untypedText.charAt(0);
          this.untypedText = this.untypedText.substring(1 );
        }
      }
    }
)


</script>

<template>
    <div>
      <h1 class="p-5">Typing test</h1>

      <h4>
        <span class="text-primary">
          {{typedText}}
        </span>
        <span class="text-muted">
          {{untypedText}}
        </span>

      </h4>

    </div>
</template>

<style scoped>

</style>