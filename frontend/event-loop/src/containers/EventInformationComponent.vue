<template>
    <a-row type="flex" justify="space-around" align="middle" style="height: 100%">
        <a-col :span="11" push="1">
            <div><img :src="event.photo" alt="Фотография" width="400" height="400"></div>

        </a-col>
        <a-col :span="13" pull="1">
            <div class="main_information">
                <h1><strong>{{ event.title }}</strong></h1>
                <p>{{ event.description }}</p>
            </div>
            <div class="time">
                <p><strong>Начало мероприятия:</strong> {{ event.start_time }}</p>
                <p><strong>Завершение мероприятия:</strong> {{ event.finish_time }}</p>
            </div>
            <div v-if="event.price && !this.organizators.includes(user.id)" class="payment">
                <p><strong>Стоимость мероприятия: {{ event.price }} р</strong></p>
                <a-button>Оплатить мероприятие</a-button>
            </div>
            <div v-if="!event.price && !this.organizators.includes(user.id)" class="payment">
                <p><strong>Посещение свободное</strong></p>
            </div>
            <div class="rate" v-if="showRatingToRate" style="margin-top: 10px" @click="rateEvent">
                <a-rate v-model:value="value"/>
            </div>
            <div class="rate" v-if="showRating" style="margin-top: 10px">
                <a-tooltip placement="bottom">
                    <template #title>Вы уже оценили
                    </template>
                    <a-rate v-model:value="users_value" disabled/>
                </a-tooltip>
            </div>
        </a-col>
    </a-row>

</template>

<script>
import {mapState} from "vuex";
import {setRate} from "../../services/api";

export default {
    name: "EventInformationComponent",
    data() {
        return {
            showRatingToRate: true,
            showRating: false,
            value: 0,
            users_value: 0,
            organizators: [],
        }
    },
    computed: {
        ...mapState({
            error: state => state.login.error,
            isSuccess: state => state.profile.isSuccess,
            isLoading: state => state.login.isLoading,
            userEvents: state => state.events.userEvents,
            user: state => state.login.user
        }),
    },
    created() {
        this.event.organizer.forEach((element) => {
            if (element.is_organizer === true) {
                this.organizators.push(element.user)
            }
        })
        if (!this.organizators.includes(this.user.id)) {
            this.event.rating_event.forEach((element) => {
                if (element.user === this.user.id) {
                    this.showRatingToRate = false
                    this.showRating = true
                    this.users_value = element.rating
                }
            })
        } else {
            this.showRatingToRate = false
        }
    },
    props: {
        event: {}
    },
    methods: {
        async rateEvent() {
            await setRate({user: this.user.id, event: this.event.id, rating: this.value})
            this.showRatingToRate = false
            this.showRating = true
            this.users_value = this.value
        }
    }

}
</script>

<style scoped>

</style>