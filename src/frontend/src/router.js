import { createRouter, createWebHistory } from "vue-router";
import AboutPage from "./pages/AboutPage.vue";
import HomePage from "./pages/HomePage.vue";

const routes = [
    { path: "/", component: HomePage },
    { path: "/about", component: AboutPage },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
