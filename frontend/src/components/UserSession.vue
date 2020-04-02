<template>
<!-- This component checks to see if a user is signed in before loading any <slot>'ed user related
     components, else an error is shown. -->
  <keep-alive>
    <div v-if="this.$store.getters.isSignedIn">
      <slot></slot>
    </div>
    <div v-else>
      <NotSignedInError></NotSignedInError>
    </div>
  </keep-alive>
</template>

<script>
  export default {
    name: 'UserSession',
    mounted() {
      this.checkLoginStatus();
    },
    updated() {
      this.$nextTick().then(() => { this.checkLoginStatus(); });
    },

    methods: {
      checkLoginStatus() {
        this.$store.dispatch('updateSignInValidation');
      }
    }
  };
</script>

<style scoped>

</style>
