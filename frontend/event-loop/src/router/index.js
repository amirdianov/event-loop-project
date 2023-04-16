import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import {getTokens} from "../../services/storage";
import store from "@/store";

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
            component: () => import('../views/LoginView.vue'),
            meta: {unauthorizedAccess: true}
        },
        {
            path: '/profile',
            name: 'profile',
            component: () => import('../views/ProfileView.vue')
        },
        {
            path: '/about',
            name: 'about',
            component: () => import('../views/AboutView.vue'),
            meta: {unauthorizedAccess: true}
        },
        {
            path: '/support',
            name: 'support',
            component: () => import('../views/SupportView.vue'),
            meta: {unauthorizedAccess: true}

        },
        {
            path: '/registration',
            name: 'registration',
            component: () => import('../views/RegistrationView.vue'),
            meta: {unauthorizedAccess: true}

        }
    ]
})

router.beforeEach((to, from) => {
    const authOnly = !to.meta?.unauthorizedAccess === true;
    console.log(store.state.login.user)
    if (getTokens().access === 'null' && authOnly && from.name !== 'login') {
        return {name: "login"};
    }
    if (getTokens().access !== 'null' && (to.name === 'login' || to.name === 'registration')) {
        return {name: "profile"};
    }
})
export default router
