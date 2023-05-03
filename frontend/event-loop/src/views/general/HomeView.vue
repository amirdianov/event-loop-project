<template>
    <div class="main" style="min-height: 550px">
        <h1>Домашная страница для всех</h1>
        <img src="@/assets/images/home-sunset.jpg" width="400" height="500">
    </div>
</template>
<script>
import {mapState} from "vuex";
import LayoutNav from "@/components/LayoutNav.vue";

export default {
    components: {LayoutNav},
    data() {
        return {}
    },
    computed: {
        ...mapState({
            user: state => state.login.user
        }),
    }

}
</script>