<!-- This is the entry point for the different components to be shown -->
<template>
  <div id="app">
    <div>
      <b-container fluid class="p-0 m-0">
        <b-card title="Home Title" no-body class="border-bottom-0">
          <b-card-header header-tag="nav" class="position-fixed w-100 mt-n1 shadow-sm"
                         style="z-index: 100;"
                         header-bg-variant="white">
            <Navbar></Navbar>
          </b-card-header>
          <b-card-body rowspan="8" class="text-center align-content-center mt-5 pt-5 ">
            <BasicTransition>
              <!-- corresponding templates for routes are injected into <router-view/> at runtime. -->
              <router-view/>
            </BasicTransition>
          </b-card-body>
        </b-card>
      </b-container>
    </div>
  </div>
</template>

<style>
  @import "https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.css";
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  .navColor {

  }

  #nav {
    padding: 30px;
  }

  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }
  body {
    /*overflow-y: auto;*/
  }


  .b-nav-item {
    color: #42b983 !important;
  }

  #nav a.router-link-exact-active {
    color: #42b983 !important;
  }
</style>
<script>
  import Navbar from './components/Navbar.vue';

  export default {
    components: { Navbar },
  };
</script>
