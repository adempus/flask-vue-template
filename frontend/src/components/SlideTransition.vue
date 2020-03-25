<template>
  <transition appear name="slide-fade">
    <slot></slot>
  </transition>
</template>

<script>
    export default {
        name: 'SlideTransition'
    };
</script>

<style scoped>
  .slide-fade-enter-active {
    transition: all .3s ease;
  }
  .slide-fade-leave-active {
    transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
  }
  .slide-fade-enter, .slide-fade-leave-to
    /* .slide-fade-leave-active below version 2.1.8 */ {
    transform: translateY(25px);
    opacity: 0;
  }
</style>
