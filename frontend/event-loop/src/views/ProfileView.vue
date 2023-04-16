<template>
    <LayoutNav>
        <div v-if="this.user != null">
            <h1>Имя {{ this.user.name }}</h1>
            <h2>Почта {{ this.user.email }}</h2>
            <a-button @click="logout_click">Выйти</a-button>
        </div>
    </LayoutNav>
</template>

<script>
import LayoutNav from "@/containers/LayoutNav.vue";
import {mapActions, mapState} from "vuex";

export default {
    name: "ProfileView",
    components: {LayoutNav},
    computed: {
        ...mapState(
            {
                user: state => state.login.user
            }
        )
    },
    methods: {
        ...mapActions({logout: 'login/logout'}),
        logout_click() {
            this.logout()
            this.$router.push({name: "home"});
        }
    }
}
</script>

<style scoped>

</style>