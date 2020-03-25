<template>
<!-- This component checks to see if a user is signed in before loading any <slot>'ed user related
     components, else an error is shown. -->
  <div v-if="this.$store.getters.isSignedIn">
    <slot></slot>
  </div>
  <div v-else>
    <NotSignedInError></NotSignedInError>
  </div>
</template>

<script>
  export default {
    name: 'UserSession',
  };
</script>

<style scoped>

</style>
