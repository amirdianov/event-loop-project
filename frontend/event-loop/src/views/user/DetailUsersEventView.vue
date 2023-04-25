<template>
    <h1>{{ this.event }}</h1>
</template>

<script>
import LayoutNav from "@/containers/LayoutNav.vue";
import {mapActions, mapState} from "vuex";
import ProfileInformationComponent from "@/components/ProfileInformationComponent.vue";
import {UserOutlined} from "@ant-design/icons-vue";

export default {
    name: "ProfileView",
    components: {ProfileInformationComponent, LayoutNav, UserOutlined},
    data() {
        return {
           event: null
        }
    },
    methods: {
        ...mapActions({logout: 'login/logout'}),
        logout_click() {
            this.logout()
            this.$router.push({name: "home"});
        },

    },
    computed: {
        ...mapState({
            error: state => state.login.error,
            isSuccess: state => state.profile.isSuccess,
            isLoading: state => state.login.isLoading,
            userEvents: state => state.events.userEvents
        }),
    },
    created() {
        this.userEvents.forEach((event) => {
            console.log(event.id)
            console.log(this.$route.params.id)
            if (event.id == this.$route.params.id) {
                this.event = event
            }
        })
        console.log(this.event)
    }

}
</script>

<style scoped>

</style>