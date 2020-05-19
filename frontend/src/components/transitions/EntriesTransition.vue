<template>
  <transition appear mode="in-out"
                    enter-active-class="animated entries-transition fadeInUp faster"
                    leave-active-class="animated fadeOutDown slow"
                    >
    <slot></slot>
  </transition>
</template>

<script>
    export default {
        name: 'EntriesTransition'
    };
</script>

<style scoped>
  .entries-transition {
    animation-duration: 400ms;
    /*animation-delay: 1ms;*/
    /*animation-iteration-count: infinite;*/
  }
</style>
