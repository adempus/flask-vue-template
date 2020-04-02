<template>
  <div>
    <h1>{{ header }}</h1>
    <div>
      <ul>
        <li v-for='item in testItems' v-bind:key="item">{{ item }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'TestPage',

    created() {
      this.getTestData();
    },

    data() {
      return {
        header: 'Test Data',
        testItems: {},
      };
    },
    methods: {
      getTestData() {
        const testEndpoint = this.$root.test;
        axios.get(testEndpoint)
          .then((response) => {
            console.log('response: ', response);
            this.testItems = response.data;
          })
          .catch((error) => { console.log('Error occurred.', error); });
      },
    },
  };
</script>

<style scoped>
  li {
    list-style: none;
  }
</style>
