<template>
    <div class="main">
        <LayoutNav>
            <h1>Домашная страница для всех</h1>
        </LayoutNav>
    </div>
</template>
<script>
import {mapState} from "vuex";
import LayoutNav from "@/containers/LayoutNav.vue";

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