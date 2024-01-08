import { createApp } from 'vue';

import App from './App.vue'
import router from "./router";

// import "bootstrap/dist/css/bootstrap.min.css"

import PrimeVue from 'primevue/config';

// import "primevue/resources/themes/saga-blue/theme.css"; //theme

import "primevue/resources/themes/lara-dark-green/theme.css";
import "primevue/resources/primevue.min.css"; //core CSS


const app = createApp(App)

app.use(router)

app.use(PrimeVue )
// app.component("Password" , Password)
// app.component("Button" , Button)


app.mount('#app')
