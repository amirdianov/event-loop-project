<template>
    <a-alert v-if="this.error" :message="this.error" type="error"/>
    <a-row type="flex" justify="center" align="middle" style="min-height: 550px">
        <a-col :span="10">
            <RegistrationComponent></RegistrationComponent>
        </a-col>
    </a-row>
</template>

<script>
import LayoutNav from "@/components/LayoutNav.vue";
import RegistrationComponent from "@/containers/user/RegistrationComponent.vue";
import {mapState} from "vuex";

export default {
    name: "RegistrationView",
    components: {RegistrationComponent},
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

<style scoped>

</style>