import {createStore} from "vuex"
import {loginModule} from "@/store/loginModule";
import {profileModule} from "@/store/profileModule";
import {eventsModule} from "@/store/eventsModule";

export default createStore({
    modules: {login: loginModule, profile: profileModule, events: eventsModule}
})