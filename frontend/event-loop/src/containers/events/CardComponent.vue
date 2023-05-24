<template>
    <a-card hoverable style="width: 285px">
        <template #cover>
            <img
                    alt="example"
                    :src=event_info.photo
                    @click="this.$router.push({name: name, params: {id: this.event_info.id, slug: this.slug}})"
                    width="300" height="300"
            />
        </template>
        <template #actions>
            <edit-outlined v-if="name==='my-event-page'" key="edit" style="font-size: 30px"
                           @click="this.$router.push({name: 'my-event-page-edit', params: {id: event_info.id, slug: slug}})">
            </edit-outlined>
            <delete-outlined v-if="name==='my-event-page'" key="delete" style="font-size: 30px"
                             @click="deleteEvent"
            ></delete-outlined>
            <a-rate v-if="name==='event-page' && !isLoading" :value="this.rate" disabled allow-half/>
            <div v-if="name==='event-page' && isLoading">
                <LoadingOutlined></LoadingOutlined>
            </div>
            <SubscribeComponent
                    v-if="name==='event-page' && !event_info.price && !this.organizators.includes(this.user.id)"
                    :event_info="event_info">
                <template v-slot:default="slotProps">
                    <carry-out-outlined v-if="slotProps.showConfirmIcon" style="font-size: 30px"
                                        @click="slotProps.callShowConfirm"/>
                    <check-outlined v-else style="font-size: 30px"/>
                </template>

            </SubscribeComponent>
            <PaymentSubscribeComponent
                    v-if="name==='event-page' && event_info.price && !this.organizators.includes(this.user.id)"
                    :event_info="event_info">
                <template v-slot:default="slotProps">
                    <pay-circle-outlined v-if="slotProps.showConfirmIcon" style="font-size: 30px"
                                         @click="slotProps.callShowConfirm"/>
                    <check-outlined v-else style="font-size: 30px"/>
                </template>

            </PaymentSubscribeComponent>

        </template>
        <a-card-meta :title=event_info.title
                     :description="event_info.price ? `Платный доступ` : `Посещение свободное`"
                     @click="this.$router.push({name: name, params: {id: event_info.id, slug: slug}})">
        </a-card-meta>
        <div v-if="!isLoading" style="display: inline-block; margin-top:10px; ">
            <a-tag v-for="(tag, index) in event_info.tags" :key="index">
                {{ tag }}
            </a-tag>
        </div>
    </a-card>
</template>
<script>
import {
    CarryOutOutlined,
    CheckOutlined,
    DeleteOutlined,
    EditOutlined,
    LoadingOutlined,
    PayCircleOutlined
} from '@ant-design/icons-vue';
import {defineComponent} from 'vue';
import {getEventRate} from "../../../services/api/rate";
import {mapActions, mapState} from "vuex";
import SubscribeComponent from "@/components/SubscribeComponent.vue";
import PaymentSubscribeComponent from "@/components/PaymentSubscribeComponent.vue";
import {delete_event} from "../../../services/api/event";

export default defineComponent({
    name: "CardComponent",
    data() {
        return {
            isLoading: false,
            rate: 0,
            organizators: [],
            sessionId: null,

        }
    },
    components: {
        CheckOutlined,
        PaymentSubscribeComponent,
        SubscribeComponent,
        EditOutlined, CarryOutOutlined, PayCircleOutlined, LoadingOutlined, DeleteOutlined
    },
    props: {
        event_info: {},
        name: {},
        slug: {},
    },
    computed: {
        ...mapState({
            user: state => state.login.user,
        }),
    },
    methods: {
        ...mapActions({loadUsersEvents: "events/loadUsersEvents"}),
        async getRate() {
            this.isLoading = true
            const obj = await getEventRate(this.event_info.id)
            console.log(obj)
            this.rate = obj['rate']
            this.isLoading = false
        },
        async deleteEvent() {
            this.isLoading = true
            await delete_event(this.event_info.id)
            await this.loadUsersEvents()
            this.isLoading = false
        }
    },
    created() {
        this.event_info.organizer.forEach((element) => {
            this.organizators.push(element.user)
        })
        if (this.name === 'event-page') {
            this.getRate()
        }
    }
})
;

</script>

<style scoped>

</style>