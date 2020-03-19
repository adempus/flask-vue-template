import Vue from 'vue';
import Vuelidate from 'vuelidate';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import App from './App.vue';
import router from './router';
import store from './store';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import Navbar from './components/Navbar.vue';

Vue.config.productionTip = false;
Vue.use(Vuelidate);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

Vue.component('navbar', Navbar);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
