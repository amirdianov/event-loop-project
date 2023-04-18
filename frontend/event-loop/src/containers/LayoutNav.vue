<template>
    <a-layout style="height: 100vh">
        <a-layout-header class="header" style="background-color: #002a29;">
            <div class="logo"/>
            <a-menu
                    v-model:selectedKeys="selectedKeys1"
                    theme="dark"
                    mode="horizontal"
                    style="background-color: #002a29;"
            >
                <a-menu-item>
                    <RouterLink to="/">Главная страница</RouterLink>
                </a-menu-item>
                <a-menu-item>
                    <RouterLink to="/about">О нас</RouterLink>
                </a-menu-item>
                <a-menu-item>
                    <RouterLink to="/support">Поддержка</RouterLink>
                </a-menu-item>
                <a-menu-item v-if="user === null">
                    <RouterLink to="/login">Войти | Зарегистрироваться</RouterLink>
                </a-menu-item>
            </a-menu>
        </a-layout-header>
        <a-layout>
            <a-layout-sider width="200" style="background: #fff" v-if="user!== null">
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
                        <a-menu-item key="2">Мои мероприятия</a-menu-item>
                        <a-menu-item key="3">Мой календарь</a-menu-item>
                        <a-menu-item key="4">Посещенные мероприятия</a-menu-item>
                    </a-sub-menu>
                    <a-sub-menu key="sub2">
                        <template #title>
              <span>
                <laptop-outlined/>
                Мероприятия
              </span>
                        </template>
                        <a-menu-item key="5">Вебинары</a-menu-item>
                        <a-menu-item key="6">Курсы</a-menu-item>
                        <a-menu-item key="7">Мастер-классы</a-menu-item>
                        <a-menu-item key="8">Развлечения</a-menu-item>
                    </a-sub-menu>
                </a-menu>
            </a-layout-sider>
            <a-layout style="padding: 20px">
                <a-layout-content
                        :style="{ background: '#fff', padding: '24px', margin: 0}">
                    <slot/>
                </a-layout-content>
            </a-layout>
        </a-layout>
    </a-layout>
</template>
<script>
import {LaptopOutlined, NotificationOutlined, UserOutlined} from '@ant-design/icons-vue';
import {defineComponent, ref} from 'vue';
import {mapState} from "vuex";

export default defineComponent({
    components: {
        UserOutlined,
        LaptopOutlined,
        NotificationOutlined,
    },
    setup() {
        return {
            selectedKeys1: ref(['2']),
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