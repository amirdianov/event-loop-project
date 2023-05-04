<template>
    <a-alert v-if="this.error" :message="this.error" type="error"/>
    <a-row type="flex" justify="center" align="middle" style="min-height: 550px">
        <a-col :span="10">
            <LoginComponent></LoginComponent>
            <button @click="redirectToYandex()">Авторизоваться через Яндекс</button>
        </a-col>
    </a-row>
</template>
<style>

</style>
<script>
import LoginComponent from "@/containers/user/LoginComponent.vue";
import LayoutNav from "@/components/LayoutNav.vue";
import {mapState} from "vuex";
export default {

    components: {LayoutNav, LoginComponent},
    data() {
        return {}
    },
    computed: {
        ...mapState({
            error: state => state.login.error
        })
    },
    methods: {
        redirectToYandex() {
            window.location.href = 'https://oauth.yandex.ru/authorize?response_type=code&client_id=bcc383a7ee3541b991461e2167192397&redirect_uri=http://localhost:5173/'
        },
    },

}

</script>
