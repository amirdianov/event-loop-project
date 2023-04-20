import {createStore} from "vuex"
import {loginModule} from "@/store/loginModule";
import {profileModule} from "@/store/profileModule";

export default createStore({
    modules: {login: loginModule, profile: profileModule}
})