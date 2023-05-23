<template>
    <MessageComponent v-if="this.isSuccess" typeMessage="success" messageText="Вы зарегистрированы"/>
    <MessageComponent v-if="this.error" typeMessage="error" messageText="Ошибка" :messageDescription="this.error"/>
    <a-row type="flex" justify="center" align="middle" style="min-height: 550px">
        <a-col :span="10">
            <RegistrationComponent></RegistrationComponent>
        </a-col>
    </a-row>
</template>

<script>
import RegistrationComponent from "@/containers/user/RegistrationComponent.vue";
import {mapState} from "vuex";
import MessageComponent from "@/components/MessageComponent.vue";

export default {
    name: "RegistrationView",
    components: {MessageComponent, RegistrationComponent},
    data() {
        return {}
    },
    computed: {
        ...mapState({
            error: state => state.login.error,
            isSuccess: state => state.login.isSuccess
        })
    }
}
</script>

<style scoped>

</style>