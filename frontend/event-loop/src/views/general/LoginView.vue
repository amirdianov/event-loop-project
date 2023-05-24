<template>
    <MessageComponent v-if="this.error" typeMessage="error" messageText="Ошибка" :messageDescription="this.error"/>
    <a-row type="flex" justify="center" align="middle" style="min-height: 550px">
        <a-col :span="10">
            <LoginComponent></LoginComponent>
        </a-col>
    </a-row>
</template>
<style>

</style>
<script>
import LoginComponent from "@/containers/user/LoginComponent.vue";
import LayoutNav from "@/components/LayoutNav.vue";
import {mapState} from "vuex";
import MessageComponent from "@/components/MessageComponent.vue";

export default {

    components: {MessageComponent, LayoutNav, LoginComponent},
    data() {
        return {}
    },
    computed: {
        ...mapState({
            error: state => state.login.error,
            isSuccess: state => state.login.isSuccess,

        })
    },

}

</script>
