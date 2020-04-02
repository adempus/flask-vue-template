<template>
  <transition appear mode="out-in"
              enter-active-class="animated fadeIn faster"
              :duration="115">
    <slot></slot>
  </transition>
</template>

<script>
    export default {
        name: 'BasicTransition'
    };
</script>

<style scoped>

</style>
