<template>
    <div class="main">
        <h1>Домашная страница для всех</h1>
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