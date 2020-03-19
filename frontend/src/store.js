import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    // reactive equivalent to vue instance data attributes
    isSignedIn: false,
    userId: null,
  },
  mutations: {
    // used to commit and track changes to state.
    // Enables time traveling to rollback state changes.
    setSignInState(currentState, newState) {
      currentState.isSignedIn = newState;
    },
    setUserId(currentState, newState) {
      currentState.userId = newState;
    }
  },
  actions: {
    // used to call mutations to update state directly
    setStateSignedIn(context) {
      context.commit('setSignInState', true);
    },
    setStateSignedOut(context) {
      context.commit('setSignInState', false);
      context.commit('setUserId', null);
    },
    updateSignInValidation(context) {
      if (localStorage.getItem('token') !== null) {
        const endpoint = 'http://localhost:5000/authenticate';
        axios.get(endpoint, {
          headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
        }).then((response) => {
          console.log('Auth response: ', response);
          const res = response.data;
          if (res.error) {
            console.log('authentication error response');
            context.commit('setSignInState', false);
            context.commit('setUserId', null);
          } else {
            context.commit('setSignInState', true);
            context.commit('setUserId', res.data.user.id);
          }
          console.log('Auth response: ', response);
        });
      }
    },
  },
  getters: {
    // accesses state
    isSignedIn(state) {
      return state.isSignedIn;
    },
    userId(state) {
      return state.userId;
    }
  }
});

export default store;
