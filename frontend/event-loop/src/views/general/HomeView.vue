<template>
    <div class="container">
        <img src="@/assets/images/logo3.0.png" width="700" height="157"
             alt="Логотип">
        <h1 class="title">Добро пожаловать на наш сайт!</h1>
        <h2 class="subtitle">Здесь вы найдете много интересного</h2>

    </div>
</template>


<script>
import {mapActions, mapState} from "vuex";
import LayoutNav from "@/components/LayoutNav.vue";
import axios from "axios";
import qs from 'qs';
import {storageTokens} from "../../../services/storage";
import store from "@/store";
import {yandexToken} from "../../../services/api/user";

export default {
    components: {LayoutNav},
    data() {
        return {}
    },
    methods: {
        ...mapActions({
            loadUser: 'login/loadUser',
        })
    },
    computed: {
        ...mapState({
            user: state => state.login.user,
            isLoading: state => state.login.isLoading,
        }),
    },

    async created() {
        const code = new URLSearchParams(window.location.search).get('code')
        if (code) {
            try {
                const res_new_tokens = await yandexToken({code: code})
                console.log(res_new_tokens)
                storageTokens(res_new_tokens.access, res_new_tokens.refresh);
                store.state.login.tokens = {
                    access: res_new_tokens.access,
                    refresh: res_new_tokens.refresh
                }
            } catch (error) {
                console.error()
            }
            try {
                console.log('Давай грузи')
                await this.loadUser()
            } catch (e) {
                console.log()
            }
        }
    }

}
</script>
<style>
.container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 550px;
    background-color: #f5f5f5;
}

.title {
    font-size: 4rem;
    font-weight: bold;
    color: #976f4f;
    margin-bottom: 0.5rem;
}

.subtitle {
    font-size: 2rem;
    font-weight: bold;
    color: #976f4f;
    margin-bottom: 1rem;
}

.description {
    font-size: 1.5rem;
    color: #333;
    max-width: 500px;
    text-align: center;
    margin-bottom: 2rem;
}

.title:hover {
    animation: shake 0.5s;
}

@keyframes shake {
    0% {
        transform: translateX(0);
    }
    25% {
        transform: translateX(-5px);
    }
    50% {
        transform: translateX(5px);
    }
    75% {
        transform: translateX(-5px);
    }
    100% {
        transform: translateX(0);
    }
}
</style>