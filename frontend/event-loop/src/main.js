import {createApp} from 'vue'
import {createPinia} from 'pinia'
import Antd from 'ant-design-vue';

import App from './App.vue'
import store from './store/index'
import router from './router'
import './antd.less'
// import 'vuetify/styles'
// import {createVuetify} from 'vuetify'
// import * as components from 'vuetify/components'
// import * as directives from 'vuetify/directives'
//
// const vuetify = createVuetify({
//     components,
//     directives,
// })
//
// import {initNotifications} from "../services/notifications";
// initNotifications();

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(Antd)
app.use(store)
// app.use(vuetify)
app.mount('#app')
