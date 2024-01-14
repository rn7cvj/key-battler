import { createApp  } from 'vue';

import './style.css';

import App from './App.vue'
import router from "./router";

import PrimeVue from 'primevue/config';
import ToastService from 'primevue/toastservice';
import ConfirmationService from 'primevue/confirmationservice';

import 'primeicons/primeicons.css'
import "primevue/resources/primevue.min.css";
import "primevue/resources/themes/lara-dark-green/theme.css";

const app  = createApp(App)

app.use(router)

app.use(PrimeVue)
app.use(ToastService)
app.use(ConfirmationService);

app.config.performance = true;

app.mount('#app')