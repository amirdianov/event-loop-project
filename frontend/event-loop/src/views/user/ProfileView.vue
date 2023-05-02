<template>
    <a-alert v-if="this.isSuccess"
             message="Успешно"
             description="Информация обновлена!"
             type="success"
             show-icon
    />
    <a-alert v-if="this.error" :message="this.error" type="error"/>
    <a-row type="flex" justify="space-around" align="middle" style="height: 100%">
        <a-col :span="6">
            <a-avatar :size="400">
                <template #icon>
                    <UserOutlined/>
                </template>
            </a-avatar>
        </a-col>
        <a-col :span="14" v-if="!isLoading">
            <ProfileInformationComponent></ProfileInformationComponent>
        </a-col>
    </a-row>
</template>

<script>
import LayoutNav from "@/components/LayoutNav.vue";
import {mapActions, mapState} from "vuex";
import ProfileInformationComponent from "@/containers/ProfileInformationComponent.vue";
import {UserOutlined} from "@ant-design/icons-vue";

export default {
    name: "ProfileView",
    components: {ProfileInformationComponent, LayoutNav, UserOutlined},
    methods: {
        ...mapActions({logout: 'login/logout'}),
        logout_click() {
            this.logout()
            this.$router.push({name: "home"});
        }
    },
    computed: {
        ...mapState({
            error: state => state.login.error,
            isSuccess: state => state.profile.isSuccess,
            isLoading: state => state.login.isLoading,
        })
    }
}
</script>

<style scoped>

</style>