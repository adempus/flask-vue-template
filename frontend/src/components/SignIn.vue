<template>
  <b-container class="form-width mt-2">
    <div v-if="signInState.pending" class="pt-5">
      <b-spinner class="mt-5" variant="primary" style="width: 3rem; height: 3rem;"></b-spinner>
    </div>
    <div v-else>
      <SlideTransition>
        <div>
          <b-card-header bg-variant="light" header-bg-variant="dark" header-text-variant="white">
            <h4>Sign In</h4>
          </b-card-header>
          <b-card class="text-center px-4 pt-2 shadow rounded">
            <b-form @submit.prevent="signIn">
              <!-- email field -->
              <b-row>
                <b-form-group
                  id="emailGroup"
                  label="Email:"
                  label-for="email"
                  label-cols="true"
                  label-align="left"
                  class="input-label-text w-100">
                  <b-form-input
                    id="email"
                    v-model="email"
                    placeholder="email@domain.com"
                    aria-describedby="email-input-feedback"
                    :state="validateState('email')"
                    trim>
                  </b-form-input>
                  <!-- required email error feedback -->
                  <b-form-invalid-feedback
                    v-if="!this.$v.email.email || !this.$v.email.required && signInState.requested"
                    align="left"
                    :state="this.$v.email.required"
                    id="email-input-feedback">
                    {{ !this.$v.email.email ? '* Email is invalid' : '* Email is required ' }}
                  </b-form-invalid-feedback>
                  <!-- email not found error feedback  -->
                  <b-form-invalid-feedback
                    v-if="this.$v.email.email && this.$v.email.required && signInState.requested"
                    align="left"
                    :state="this.$v.email.emailNotFound"
                    id="email-input-feedback">
                    * There is no user with this email. Try again.
                  </b-form-invalid-feedback>
                </b-form-group>
              </b-row>

              <!-- password field -->
              <b-row>
                <b-form-group
                  id="passwordGroup"
                  label="Password:"
                  label-for="password"
                  label-cols="true"
                  label-align="left"
                  class="input-label-text w-100">
                  <b-form-input
                    id="password"
                    v-model="password"
                    type="password"
                    placeholder=""
                    aria-describedby="password-input-feedback"
                    :state="validateState('password')"
                    trim>
                  </b-form-input>
                  <!-- password required feedback -->
                  <b-form-invalid-feedback
                    v-if="!this.$v.password.required && signInState.requested"
                    align="left"
                    :state="this.$v.password.required"
                    id="password-input-feedback">
                    * Password is required
                  </b-form-invalid-feedback>
                  <!-- incorrect password feedback -->
                  <b-form-invalid-feedback
                    v-if="this.$v.password.required && signInState.requested"
                    align="left"
                    :state="this.$v.password.incorrectPassword"
                    id="password-input-feedback">
                    * Incorrect password, try again.
                  </b-form-invalid-feedback>
                </b-form-group>
              </b-row>
              <!-- Submit button -->
              <b-row class="justify-content-center mt-3 pl-3 pr-3">
                <b-button type="submit" variant="info">Sign In</b-button>
              </b-row>
              <b-row>
                <router-link to="/sign-up" class="pt-3 mr-4 mb-n2 sign-up-link mx-auto">
                  Don't have an account? Sign Up
                  <b-icon-chevron-right></b-icon-chevron-right>
                </router-link>
              </b-row>
            </b-form>
          </b-card>
        </div>
      </SlideTransition>
    </div>
<!-- debug messages -->
<!--<p class="mt-4">sign in status: {{ this.signInState.success ? "success" : "failed" }}</p>-->
<!--      <p class="text-break">-->
<!--        sign in response: {{ JSON.stringify(this.signInState.response, undefined, 1) }}-->
<!--      </p>-->
  </b-container>
</template>

<script>
  import axios from 'axios';
  import { required, email } from 'vuelidate/lib/validators';

  const emailNotFound = (value, vm) => !vm.signInState.invalidEmail;
  const incorrectPassword = (value, vm) => !vm.signInState.invalidPassword;

  export default {
    name: 'SignIn',
    data() {
      return {
        email: '',
        password: '',
        signInState: {
          requested: false,
          success: false,
          response: { error: false, message: null },
          invalidEmail: false,
          invalidPassword: false,
          attemptedEmail: '',
          attemptedPassword: '',
          pending: false
        }
      };
    },
    validations: {
      email: {
        required,
        email,
        emailNotFound
      },
      password: {
        required,
        incorrectPassword
      },
    },
    methods: {
      validateState(value) {
        const { $dirty, $error } = this.$v[value];
        return $dirty ? !$error : null;
      },
      async signIn() {
        this.$set(this.signInState, 'requested', true);
        this.$v.$touch();
        if (this.$v.$invalid) {
          console.log('invalid sign-in credentials provided.');
        } else {
          this.requestUserSignIn()
            .then((response) => {
              this.$set(this.signInState, 'pending', true);
              this.$set(this.signInState, 'response', response.data);
              console.log('sign in response: ', response.data);
              if (this.signInState.response.error) {
                this.$set(this.signInState, 'pending', false);
                this.$set(this.signInState, 'attemptedEmail', this.email);
                this.$set(this.signInState, 'attemptedPassword', this.password);
              } else {
                this.$set(this.signInState, 'success', true);
              }
              this.setSignInState();
            });
        }
      },
      requestUserSignIn() {
        // const endpoint = 'http://localhost:5000/sign-in';
        const endpoint = 'http://192.168.1.158:5000/sign-in';
        return axios.post(endpoint, {
          email: this.email,
          password: this.password,
        });
      },
      setSignInState() {
        this.$set(
          this.signInState,
          'invalidEmail',
          this.signInState.response.message.userNotFound
        );
        this.$set(
          this.signInState,
          'invalidPassword',
          this.signInState.response.message.passwordInvalid
        );
      }
    },
    watch: {
      email() {
        console.log('Email input has been changed: ');
        if (this.signInState.response.error) {
          if (this.signInState.response.message.userNotFound) {
            this.$set(
              this.signInState,
              'invalidEmail',
              this.signInState.attemptedEmail.toUpperCase() === this.email.toUpperCase()
            );
          }
        }
      },
      password() {
        if (this.signInState.response.error) {
          if (this.signInState.response.message.passwordInvalid) {
            this.$set(
              this.signInState,
              'invalidPassword',
              this.signInState.attemptedPassword === this.password
            );
          }
        }
      },
      signInState: {
        handler: function (value) {
          if (value.success) {
            console.log('sign in success: ', value.success);
            const token = this.signInState.response.token;
            const userId = this.signInState.response.data.id;
            localStorage.setItem('token', token);
            this.$store.dispatch('setStateSignedIn');
            window.location.href = `/user/${userId}`;
          }
        },
        deep: true
      },
    }
  };
</script>

<style scoped>
  .form-width {
    width: 25vw;
  }

  .input-label-text {
    font-size: 0.9em;
  }
  .sign-up-link {
    font-size: 0.75em;
    color: #707579;
  }
  @media (max-width: 1024px) {
    .form-width {
      width: 50vw;
    }
  }
  @media (max-width: 750px) {
    .form-width {
      width: 90vw;
    }
  }
</style>
