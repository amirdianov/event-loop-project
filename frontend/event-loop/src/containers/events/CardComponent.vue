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
            <a-rate v-if="name==='event-page' && !isLoading" :value="this.rate" disabled allow-half/>
            <div v-if="name==='event-page' && isLoading">
                <LoadingOutlined></LoadingOutlined>
            </div>
            <SubscribeComponent
                    v-if="name==='event-page' && !event_info.price && !this.organizators.includes(this.user.id)"
                    :event_info="event_info">
            </SubscribeComponent>
            <!--            TODO pay component-->
            <pay-circle-outlined
                    v-if="name==='event-page' && event_info.price && !this.organizators.includes(this.user.id)"
                    style="font-size: 30px" @click="handleCheckout"/>
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
import {CarryOutOutlined, EditOutlined, LoadingOutlined, PayCircleOutlined} from '@ant-design/icons-vue';
import {defineComponent} from 'vue';
import {getEventRate, payEvent} from "../../../services/api";
import {mapState} from "vuex";
import SubscribeComponent from "@/components/SubscribeComponent.vue";
import {loadStripe} from "@stripe/stripe-js";

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
        SubscribeComponent,
        EditOutlined, CarryOutOutlined, PayCircleOutlined, LoadingOutlined
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
        async getRate() {
            this.isLoading = true
            const obj = await getEventRate(this.event_info.id)
            console.log(obj)
            this.rate = obj['rate']
            this.isLoading = false
        },
        async handleCheckout() {
            const stripePromise = loadStripe('pk_test_51N8KlCBJtD2zRVv8FPFS8pcAzwuwflNLoXZktp9b599Fz7Wr0a6sT1gvTYHqngFvdLU3S5qGxxHqZ0CYWia2Vvhy00yqGxaYE9');
            // Получите sessionId с сервера
            try {
                const response = await payEvent(this.event_info.id);
                console.log(response)
                this.sessionId = response.sessionId;

                if (this.sessionId) {
                    const stripe = await stripePromise;
                    const {error} = await stripe.redirectToCheckout({
                        sessionId: this.sessionId,
                    });

                    if (error) {
                        console.error(error);
                    }
                } else {
                    console.error('sessionId is undefined');
                }
            } catch (error) {
                console.error(error);
            }
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
});

</script>

<style scoped>

</style>