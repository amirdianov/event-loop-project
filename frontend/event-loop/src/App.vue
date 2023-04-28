<script setup>
import {RouterView} from 'vue-router'
import PageLoaderComponent from "@/components/PageLoaderComponent.vue";
import LayoutNav from "@/containers/LayoutNav.vue";
</script>

<template>
    <PageLoaderComponent v-if="isLoading"/>
    <LayoutNav>
        <RouterView/>
    </LayoutNav>
</template>

<script>

import {mapActions, mapState} from "vuex";

export default {
    name: "App",
    methods: {
        ...mapActions({
            loadUser: 'login/loadUser',
        })
    },
    created() {
        this.loadUser()
    },
    computed: {
        ...mapState({
            isLoading: state => state.login.isLoading
        })
    }
}
</script>