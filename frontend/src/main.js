import Vue from 'vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import VeeValidate from 'vee-validate';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.config.productionTip = false;

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
// Vue.use(VeeValidate);

new Vue({
  router,
  VeeValidate,
  render: (h) => h(App),
}).$mount('#app');
