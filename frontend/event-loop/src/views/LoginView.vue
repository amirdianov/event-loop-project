<template>
    <div class="about">
        <LayoutNav>
            <a-row type="flex" justify="center" align="middle" style="height: 100%">
                <a-col :span="10">
                    <LoginComponent></LoginComponent>
                </a-col>
            </a-row>
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