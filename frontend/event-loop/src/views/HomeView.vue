<template>
    <h1 v-if="this.user != null">Домашнаяя страница {{ this.user.email }}</h1>
    <h1 v-else>Общая страница</h1>
</template>
<script>
import {mapState} from "vuex";

export default {
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