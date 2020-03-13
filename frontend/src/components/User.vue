<template>
  <div v-if="userPageState.response !== null">
    <div v-if="userPageState.response.error">
      <h1>Error</h1>
      <p>{{userPageState.response.message}}</p>
    </div>
    <!-- User data is displayed below if no errors are present. -->
    <div v-else>
      <h1>Welcome {{username}}</h1>
      <h2>First name: {{firstName}}</h2>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';

    export default {
      name: 'User',
      created() {
        this.requestUserData();
      },
      data() {
        return {
          userPageState: {
            response: null
          },
          username: '',
          firstName: '',
        };
      },
      methods: {
        requestUserData() {
          if (localStorage.token) {
            const endpoint = `http://localhost:5000/${this.$route.fullPath}`;
            console.log('curent url: ', this.$route.fullPath);
            axios.defaults.headers.common.Authorization = `Bearer ${localStorage.getItem('token')}`;
            axios.get(endpoint).then((res) => {
              this.userPageState.response = res.data;
              this.username = res.data.data.user.username;
              this.firstName = res.data.data.user.firstName;
              console.log('response: ', res);
            });
          }
        }
      },
    };
</script>

<style scoped>

</style>
