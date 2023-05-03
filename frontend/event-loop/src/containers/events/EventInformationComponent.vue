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
                <div v-if="!isLoading">
                    <a-button v-if="showConfirmButton">Подписаться на мероприятие</a-button>
                </div>

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
import {setRate, subscribers} from "../../../services/api";

export default {
    name: "EventInformationComponent",
    data() {
        return {
            showRatingToRate: true,
            showRating: false,
            showConfirmButton: true,
            value: 0,
            users_value: 0,
            organizators: [],
            isLoading: false
        }
    },
    computed: {
        ...mapState({
            error: state => state.login.error,
            isSuccess: state => state.profile.isSuccess,
            userEvents: state => state.events.userEvents,
            user: state => state.login.user
        }),
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
        },
        async loadSubscribers() {
            this.isLoading = true
            const all_subscribers = await subscribers(this.event.id)
            this.isLoading = false
            return all_subscribers
        }

    },
    async created() {
        // проверка на то, является ли пользователь создателем
        this.event.organizer.forEach((element) => {
            this.organizators.push(element.user)
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
        // проверка на то, является ли пользователь подписчиком
        const all_subscribers = await this.loadSubscribers()
        all_subscribers.forEach((element) => {
            console.log('Я тут')
            if (element.user === this.user.id) {
                this.showConfirmButton = false
            }
        })
    }
}
</script>

<style scoped>

</style>