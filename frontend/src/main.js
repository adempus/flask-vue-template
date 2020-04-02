import Vue from 'vue';
import Vuelidate from 'vuelidate';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import App from './App.vue';
import router from './router/routes';
import endpoints from './router/endpoints';
import store from './store';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import Navbar from './components/Navbar.vue';
import UserSession from './components/UserSession.vue';
import BasicTransition from './components/transitions/BasicTransition.vue';
import SignInOutTransition from './components/transitions/SignInOutTransition.vue';
import EntriesTransition from './components/transitions/EntriesTransition.vue';
import NotSignedInError from './components/errors/NotSignedInError.vue';

Vue.config.productionTip = false;
Vue.use(Vuelidate);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

Vue.component('navbar', Navbar);
Vue.component('NotSignedInError', NotSignedInError);
Vue.component('UserSession', UserSession);
Vue.component('SignInOutTransition', SignInOutTransition);
Vue.component('BasicTransition', BasicTransition);
Vue.component('EntriesTransition', EntriesTransition);

const vm = new Vue({
  router,
  data: endpoints,
  store,
  render: (h) => h(App),
}).$mount('#app');

// export default vm;
