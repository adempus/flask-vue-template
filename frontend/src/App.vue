<!-- This is the entry point for the different components to be shown -->
<template>
  <div id="app">
    <div>
      <b-container fluid class="p-0 m-0">
        <b-card title="Home Title" no-body>
          <b-card-header header-tag="nav">
            <b-nav card-header pills class="pl-3">
              <b-nav-item to="/" exact exact-active-class="active">Home</b-nav-item>
              <b-nav-item to="/test-page" exact exact-active-class="active">Test Page</b-nav-item>
              <b-nav-item to="/sign-in" class="ml-auto" exact exact-active-class="active">Sign In</b-nav-item>
<!--              <b-nav-item to="/sign-up" exact exact-active-class="active">Sign Up</b-nav-item>-->
            </b-nav>

          </b-card-header>
          <b-card-body class="text-center align-content-center vh-100 mt-5">
            <!-- corresponding templates for routes are injected into <router-view/> at runtime. -->
            <router-view/>
          </b-card-body>
        </b-card>
      </b-container>
    </div>
  </div>
</template>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  .navColor {
    /**/
  }

  #nav {
    padding: 30px;
  }

  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }

  .b-nav-item {
    color: #42b983 !important;
  }

  #nav a.router-link-exact-active {
    color: #42b983 !important;
  }
</style>
