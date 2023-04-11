import {createApp} from 'vue'
import {createPinia} from 'pinia'
import Antd from 'ant-design-vue';

import App from './App.vue'
import store from './store/index'
import router from './router'
import 'ant-design-vue/dist/antd.css';


const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(Antd)
app.use(store)
app.mount('#app')
