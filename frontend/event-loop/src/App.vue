<script setup>
import {RouterView} from 'vue-router'
</script>

<template>
    <a-menu style="background-color: grey">
        <a-page-header>
            <a-breadcrumb>
                <a-breadcrumb-item>
                    <RouterLink to="/">Home</RouterLink>
                </a-breadcrumb-item>
                <a-breadcrumb-item>
                    <RouterLink to="/login">Login</RouterLink>
                </a-breadcrumb-item>
            </a-breadcrumb>
        </a-page-header>
    </a-menu>
    <RouterView/>

</template>

<style scoped>

</style>
