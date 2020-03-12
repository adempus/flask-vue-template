<template>
  <div>
    <h1>
      Welcome {{username}}
    </h1>
    <h2>First name: {{firstName}}</h2>
  </div>
</template>

<script>
  import axios from 'axios';

    export default {
      name: 'User',
      mounted() {
        this.requestUserData();
      },
      data() {
        return {
          username: '',
          firstName: '',
        };
      },
      methods: {
        requestUserData() {
          if (localStorage.token) {
            const endpoint = 'http://localhost:5000/user-data';
            axios.defaults.headers.common.Authorization = `Bearer ${localStorage.getItem('token')}`;
            axios.get(endpoint).then((res) => {
              this.username = res.data.data.user.username;
              this.firstName = res.data.data.user.firstName;
              console.log('response: ', res);
            });
          }
        }
      }
    };
</script>

<style scoped>

</style>
