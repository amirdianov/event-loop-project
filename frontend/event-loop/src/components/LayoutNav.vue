<template>
    <a-layout>
        <a-layout-header class="header" style="background-color: #002a29;">
            <div class="logo"/>
            <a-menu
                    v-model:selectedKeys="selectedKeys1"
                    theme="dark"
                    mode="horizontal"
                    style="background-color: #002a29;"
                    @click="keyDefaultSet"
            >
                <a-menu-item key="1">
                    <RouterLink to="/">Главная страница</RouterLink>
                </a-menu-item>
                <a-menu-item key="2">
                    <RouterLink to="/about">О нас</RouterLink>
                </a-menu-item>
                <a-menu-item key="3">
                    <RouterLink to="/support">Поддержка</RouterLink>
                </a-menu-item>
                <a-menu-item key="4" v-if="user === null">
                    <RouterLink to="/login">Войти | Зарегистрироваться</RouterLink>
                </a-menu-item>
                <a-menu-item key="5" v-if="user !== null">
                    <a-dropdown trigger="click">
                        <a class="ant-dropdown-link" @click.prevent>
                            <strong>{{ this.user.name }}</strong>
                            <DownOutlined/>
                        </a>
                        <template #overlay>
                            <a-menu>
                                <a-menu-item>
                                    <RouterLink to="/profile">Личный кабинет</RouterLink>
                                </a-menu-item>
                                <a-menu-item @click="logout_click">
                                    <span>Выйти</span>
                                </a-menu-item>
                            </a-menu>
                        </template>
                    </a-dropdown>
                </a-menu-item>
            </a-menu>
        </a-layout-header>
        <a-layout>
            <a-layout-sider width="200" style="background: #fff" v-if="user!== null &
            this.$route.name !== 'home' & this.$route.name !== 'about' & this.$route.name !== 'support'">
                <a-menu
                        v-model:selectedKeys="selectedKeys2"
                        v-model:openKeys="openKeys"
                        mode="inline"
                        :style="{ height: '100%', borderRight: 0 }"
                >
                    <a-sub-menu key="sub1">
                        <template #title>
              <span>
                <user-outlined/>
                Личный кабинет
              </span>
                        </template>
                        <a-menu-item key="1">
                            <RouterLink to="/profile">
                                Профиль
                            </RouterLink>
                        </a-menu-item>
                        <a-menu-item key="2">
                            <RouterLink to="/my-events">
                                Мои мероприятия
                            </RouterLink>
                        </a-menu-item>
                        <a-menu-item key="3">
                            <RouterLink to="/calendar">Мой календарь</RouterLink>
                        </a-menu-item>
                        <a-menu-item key="4">Список</a-menu-item>
                    </a-sub-menu>
                    <a-sub-menu key="sub2">
                        <template #title>
              <span>
                <laptop-outlined/>
                Мероприятия
              </span>
                        </template>
                        <a-menu-item key="5">
                            <RouterLink :to="{name: 'events', params: {slug: 'lesson'}}">Уроки</RouterLink>
                        </a-menu-item>
                        <a-menu-item key="6">
                            <RouterLink :to="{name: 'events', params: {slug: 'webinar'}}">Вебинары</RouterLink>
                        </a-menu-item>
                        <a-menu-item key="7">
                            <RouterLink :to="{name: 'events', params: {slug: 'masterclass'}}">Мастер-классы</RouterLink>
                        </a-menu-item>
                        <a-menu-item key="8">
                            <RouterLink :to="{name: 'events', params: {slug: 'entertainments'}}">Развлечения
                            </RouterLink>
                        </a-menu-item>
                    </a-sub-menu>
                </a-menu>
            </a-layout-sider>
            <a-layout style="padding: 24px 24px;">
                <a-layout-content
                        :style="{ background: '#fff', padding: '24px', margin: 0, minHeight: '600px' }"
                >
                    <slot/>
                </a-layout-content>

            </a-layout>
        </a-layout>
    </a-layout>
</template>
<script>
import {DownOutlined, LaptopOutlined, NotificationOutlined, UserOutlined} from '@ant-design/icons-vue';
import {defineComponent, ref} from 'vue';
import {mapActions, mapState} from "vuex";
import EventsView from "@/views/events/EventsView.vue";

export default defineComponent({
    components: {
        EventsView,
        UserOutlined,
        LaptopOutlined,
        NotificationOutlined,
        DownOutlined,
    },
    setup() {
        return {
            selectedKeys1: ref(['1']),
            selectedKeys2: ref(['1']),
            collapsed: ref(false),
            openKeys: ref(['sub1']),
        };
    },
    computed: {
        ...mapState({
            user: state => state.login.user
        })
    },
    methods: {
        ...mapActions({logout: 'login/logout'}),
        logout_click() {
            this.logout()
            this.$router.push({name: "home"});
        },
        keyDefaultSet() {
            this.selectedKeys2 = ref(['1'])
        }
    },
});
</script>
<style>

#components-layout-demo-top-side-2 .logo {
    float: left;
    width: 120px;
    height: 31px;
    margin: 16px 24px 16px 0;
    background: rgba(255, 255, 255, 0.3);
}

.ant-row-rtl #components-layout-demo-top-side-2 .logo {
    float: right;
    margin: 16px 0 16px 24px;
}

.site-layout-background {
    background: #fff;
}

</style>