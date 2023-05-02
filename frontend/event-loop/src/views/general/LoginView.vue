<template>
    <a-alert v-if="this.error" :message="this.error" type="error"/>
    <a-row type="flex" justify="center" align="middle" style="height: 100%">
        <a-col :span="10">
            <LoginComponent></LoginComponent>
        </a-col>
    </a-row>
</template>
<style>

</style>
<script>
import LoginComponent from "@/containers/LoginComponent.vue";
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
    }
}
</script>