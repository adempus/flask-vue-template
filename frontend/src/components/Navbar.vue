<template>
    <div v-if="!isSignedIn">
      <b-nav card-header pills sticky class="pl-3">
        <b-nav-item to="/" exact exact-active-class="active">Home</b-nav-item>
        <b-nav-item to="/test-page" exact exact-active-class="active">Test Page</b-nav-item>
        <b-nav-item to="/sign-in" class="ml-auto" exact exact-active-class="active">Sign In</b-nav-item>
      </b-nav>
    </div>
    <div v-else>
      <b-nav card-header pills  class="pl-3">
        <b-nav-item exact exact-active-class="active" :to="{ name: 'User', params: { userId: userId }}">
          Home
        </b-nav-item>
          <b-nav-item-dropdown text="Entries" right class="entries-tab">
            <b-dropdown-item exact exact-active-class="active" :to="{ name: 'Entries' }">
              View Entries
            </b-dropdown-item>
            <b-dropdown-item  exact exact-active-class="active" :to="{ name: 'NewEntry' }">
              New Entry
            </b-dropdown-item>
          </b-nav-item-dropdown>
          <b-nav-item exact exact-active-class="active" :to="{ name: 'NewEntry' }" class="entry-buttons">
            New Entry
          </b-nav-item>
          <b-nav-item exact exact-active-class="active" :to="{ name: 'Entries' }" class="entry-buttons">
            Entries
          </b-nav-item>
        <div class="ml-auto">
          <b-nav-item v-on:click="signOutUser()" class="signOutBtn">Sign Out</b-nav-item>
        </div>
      </b-nav>
    </div>
</template>

<script>
  export default {
    name: 'Navbar',
    mounted() {
      this.$store.dispatch('updateSignInValidation');
    },
    data() {
      return {
      };
    },
    methods: {
      signOutUser() {
        console.log('User sign-out clicked.');
        if (localStorage.getItem('token') !== null) {
          localStorage.setItem('token', null);
          this.$store.dispatch('setStateSignedOut');
          this.$router.push({ name: 'SignIn' });
        }
      }
    },
    computed: {
      isSignedIn() {
        return this.$store.getters.isSignedIn;
      },
      userId() {
        return this.$store.getters.userId;
      },
    }
  };
</script>

<style scoped>
  @media (max-width: 399px) {
    .entries-tab {
      display: block;
    }
    .entry-buttons {
      display: none;
    }
  }
  @media (min-width: 400px) {
    .entry-buttons {
      display: block;
    }
    .entries-tab {
      display: none;
    }
  }

</style>
