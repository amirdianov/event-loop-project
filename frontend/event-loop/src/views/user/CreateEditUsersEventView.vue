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
import CreateEditEventInformationComponent from "@/containers/CreateEditEventInformationComponent.vue";
import {mapState} from "vuex";


export default defineComponent({
    name: "CreateEditUsersEventView",
    components: {CreateEditEventInformationComponent},
    computed: {
        ...mapState({
            isLoading: state => state.login.isLoading,
            error: state => state.login.error,
        })
    },

});
</script>