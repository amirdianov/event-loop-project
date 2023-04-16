<template>
    <div class="about">
        <LayoutNav>
            <LoginComponent></LoginComponent>
        </LayoutNav>
    </div>
</template>
<style>

</style>
<script>
import LoginComponent from "@/components/LoginComponent.vue";
import LayoutNav from "@/containers/LayoutNav.vue";

export default {
    components: {LayoutNav, LoginComponent},
    data() {
        return {}
    }
}
</script>