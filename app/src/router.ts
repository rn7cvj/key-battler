import { createRouter, createWebHistory } from 'vue-router';
import HomePage from "./pages/home/HomePage.vue";
import LeaderBoard from "./pages/leader-board/LeaderBoard.vue";
import TypingTest from "./pages/typing-test/TypingTest.vue";
import LoginPage from "./pages/login/LoginPage.vue";
import SignUp from "./pages/sign-up/SignUp.vue";

export default createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/home',
            component: HomePage,
        },
        {
            path: "/",
            component: LoginPage,
        },{
            path: "/signup",
            component: SignUp,
        },
        {
            path: '/typing-test',
            component: TypingTest
        },
        {
            path: '/leader-board',
            component: LeaderBoard,
        },
    ],
})
