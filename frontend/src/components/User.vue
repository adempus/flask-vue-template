<template>
    <UserSession>
      <div>
        <h1>Welcome {{ username }}</h1>
        <h2>First name: {{ firstName }}</h2>
      </div>
    </UserSession>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'User',
    created() {
      this.getUserData();
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
      getUserData() {
        if (localStorage.token) {
          const endpoint = `${this.$root.root}${this.$route.fullPath}`;
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
