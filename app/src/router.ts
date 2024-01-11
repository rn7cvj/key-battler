import {createRouter, createWebHistory} from 'vue-router';
import HomePage from "./pages/home/HomePage.vue";
import LeaderBoard from "./pages/leader-board/LeaderBoard.vue";
import TypingTest from "./pages/typing-test/TypingTest.vue";
import LoginPage from "./pages/login/LoginPage.vue";
import SignUp from "./pages/sign-up/SignUp.vue";

let baseUrl : string = import.meta.env.VITE_BASE_URL ?? "/web/";
console.log(`VITE_BASE_URL: ${baseUrl}`);

export default createRouter({

    // history: import.meta.env.IS_ELECTRON ? createWebHashHistory() : createWebHistory(),

    history: createWebHistory(baseUrl),

    routes: [

        {
            path: '/home',
            component: HomePage,
        },
        {
            path: "/",
            component: LoginPage,
        },
        {
            path: "/signup",
            component: SignUp,
        },
        {
            path: '/typing-test',
            component: TypingTest,
            props: route => ( {
                textRating : route.query.textRating
            })
        },
        {
            path: '/leader-board',
            component: LeaderBoard,
        },
    ],
})
