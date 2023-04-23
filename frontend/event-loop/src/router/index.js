import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/general/HomeView.vue'
import store from "@/store";
import {getTokens} from "../../services/storage";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView,
            meta: {unauthorizedAccess: true}
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/general/LoginView.vue'),
            meta: {unauthorizedAccess: true}
        },
        {
            path: '/profile',
            name: 'profile',
            component: () => import('../views/user/ProfileView.vue')
        },
        {
            path: '/about',
            name: 'about',
            component: () => import('../views/general/AboutView.vue'),
            meta: {unauthorizedAccess: true}
        },
        {
            path: '/support',
            name: 'support',
            component: () => import('../views/general/SupportView.vue'),
            meta: {unauthorizedAccess: true}

        },
        {
            path: '/registration',
            name: 'registration',
            component: () => import('../views/general/RegistrationView.vue'),
            meta: {unauthorizedAccess: true}

        },
        {
            path: '/my-events',
            name: 'my-events',
            component: () => import('../views/user/UsersEventsView.vue'),
            meta: {unauthorizedAccess: true}

        }
    ]
})

router.beforeEach((to, from) => {
    const authOnly = !to.meta?.unauthorizedAccess === true;
    console.log(store.getters["login/isAuth"])
    // if (!store.getters["login/isAuth"] && authOnly && from.name !== 'login') {
    //     return {name: "login"};
    // }
    if (getTokens().access === 'null' && authOnly && from.name !== 'login') {
        return {name: "login"};
    }
    if (getTokens().access !== 'null' && (to.name === 'login' || to.name === 'registration')) {
        return {name: "profile"};
    }
})
export default router
