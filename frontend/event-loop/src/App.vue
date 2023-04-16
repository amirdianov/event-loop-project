<script setup>
import {RouterView} from 'vue-router'
</script>

<template>
    <RouterView/>
</template>

<script>

import {mapActions} from "vuex";

export default {
    name: "App",
    methods: {
        ...mapActions({
            loadUser: 'login/loadUser'
        })
    },
    created() {
        this.loadUser()
    }
}
</script>