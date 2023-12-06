import { createRouter, createWebHistory } from 'vue-router';
import HomePage from "./pages/home/HomePage.vue";
import LeaderBoard from "./pages/leader-board/LeaderBoard.vue";
import TypingTest from "./pages/typing-test/TypingTest.vue";

export default createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/home',
            component: HomePage,
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
