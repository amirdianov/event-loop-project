<template>
    <div class="login">
        <LayoutNav>
            <a-row type="flex" justify="center" align="middle" style="height: 100%">
                <a-col :span="10">
                    <RegistrationComponent></RegistrationComponent>
                </a-col>
            </a-row>
        </LayoutNav>
    </div>
</template>

<script>
import LayoutNav from "@/containers/LayoutNav.vue";
import RegistrationComponent from "@/components/RegistrationComponent.vue";
import LoginComponent from "@/components/LoginComponent.vue";

export default {
    name: "RegistrationView",
    components: {LoginComponent, LayoutNav, RegistrationComponent}
}
</script>

<style scoped>

</style>