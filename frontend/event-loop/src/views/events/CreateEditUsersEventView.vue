<template>
  <!--    <a-alert v-if="this.isSuccess"-->
  <!--             message="Успешно"-->
  <!--             description="Информация обновлена!"-->
  <!--             type="success"-->
  <!--             show-icon-->
  <!--    />-->
    <a-alert v-if="this.error" :message="this.error" type="error"/>
    <a-row type="flex" justify="space-around" align="middle" style="height: 100%">
        <a-col :span="18" v-if="!isLoading">
            <CreateEditEventInformationComponent></CreateEditEventInformationComponent>
        </a-col>
    </a-row>
</template>
<script>
import {defineComponent} from 'vue';
import CreateEditEventInformationComponent from "@/containers/events/CreateEditEventInformationComponent.vue";
import {mapActions, mapState} from "vuex";

export default defineComponent({
    name: "CreateEditUsersEventView",
    components: {CreateEditEventInformationComponent},
    computed: {
        ...mapState({
            error: state => state.login.error,
        })
    },
    data() {
        return {
            event: null,
            isLoading: false
        }
    },
    methods: {
        ...mapActions({getUserEvent: "events/getUserEvent"}),
        async loadUserEvent(event_id) {
            this.isLoading = true
            this.event = await this.getUserEvent(event_id)
            this.isLoading = false
        }
    },
    created() {
        if (this.$route.params.id) {
            this.loadUserEvent(this.$route.params.id)
        }
    }
});
</script>