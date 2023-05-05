<template>
    <div v-if="!isLoading" class="main" style="min-height: 550px">
        <h1>Домашная страница для всех</h1>
        <img src="@/assets/images/home-sunset.jpg" width="400" height="500">
    </div>
</template>
<script>
import {mapActions, mapState} from "vuex";
import LayoutNav from "@/components/LayoutNav.vue";
import axios from "axios";
import qs from 'qs';
import {storageTokens} from "../../../services/storage";
import store from "@/store";

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
        const data = {
            grant_type: 'authorization_code',
            code: code,
            client_id: 'bcc383a7ee3541b991461e2167192397',
            client_secret: '130783013ba04c969ebc5aa321612462',
            redirect_uri: 'http://localhost:5173/'
        };

        const serializedData = qs.stringify(data);
        if (code) {
            try {
                const response = await axios.post('https://oauth.yandex.ru/token', serializedData, {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }
                })
                const resp = response.data
                const user_information = await axios.get(`https://login.yandex.ru/info?oauth_token=${resp.access_token}`)
                const res_new_tokens = await axios.post(`http://127.0.0.1:8000/api/yandex_token/`, user_information.data)
                storageTokens(res_new_tokens.data.access, res_new_tokens.data.refresh);
                store.state.login.tokens = {
                    access: res_new_tokens.data.access,
                    refresh: res_new_tokens.data.refresh
                }
            } catch (error) {
                console.error()
            }
            try {
                await this.loadUser(data)
            } catch (e) {
                console.log()
            }
        }
    }

}
</script>