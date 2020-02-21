<template>
  <b-container class="form-width mt-5">
    <div>
      <b-card-header bg-variant="light" header-bg-variant="dark" header-text-variant="white">
        <h4>Sign In</h4>
      </b-card-header>
      <b-card class="text-center">
        <b-form @submit.prevent="signIn">
          <b-row>
            <!-- email field -->
            <b-form-group
              id="emailGroup"
              label="Email:"
              label-for="email"
              label-cols="2"
              class="input-label-text w-100 m-3">
              <b-form-input
                id="email"
                v-model="email"
                placeholder="John"
                aria-describedby="email-input-feedback"
                :state="validateState('email')"
                trim>
              </b-form-input>
              <b-form-invalid-feedback
                v-if="!this.$v.email.email || !this.$v.email.required && signInState.requested"
                align="left"
                :state="this.$v.email.required"
                id="email-input-feedback">
                {{ !this.$v.email.email ? '* Email is invalid' : '* Email is required ' }}
              </b-form-invalid-feedback>
            </b-form-group>
          </b-row>

          <b-row>
            <!-- password field -->
            <b-form-group
              id="passwordGroup"
              label="Password:"
              label-for="password"
              label-cols="2"
              class="input-label-text w-100 m-3">
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
              <b-form-invalid-feedback v-if="!this.$v.password.required && signInState.requested"
                align="left"
                :state="this.$v.password.required"
                id="password-input-feedback">
                * Password is required
              </b-form-invalid-feedback>
            </b-form-group>
          </b-row>
          <!-- Submit button -->
          <b-row class="justify-content-center mt-4 pl-3 pr-3">
            <b-button type="submit" variant="info">Sign In</b-button>
          </b-row>
        </b-form>
      </b-card>
    </div>
  </b-container>
</template>

<script>
  import axios from 'axios';
  import { required, email } from 'vuelidate/lib/validators';

  export default {
    name: 'SignIn',
    data() {
      return {
        email: '',
        password: '',
        signInState: {
          requested: false,
          success: false,
          response: null,
          invalidEmail: false,
          invalidPassword: false,
        }
      };
    },
    validations: {
      // errors:
       // No user found with this email. Try again.
      // No user found with this email.
      // Incorrect password. Try again.
      email: {
        required,
        email
      },
      password: {
        required
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
              // this.signInResponse = response.data;
              this.$set(this.signInState, 'response', response.data);
              console.log('sign in response: ', response.data);
              if (this.signInState.response.error === true) {
                this.setSignInState();
                // if (this.signInState.response.message.userNotFound === true) {
                //   this.signInState.invalidEmail = true;
                // } else if (this.signInState.response.message.passwordInvalid === true) {
                //   this.signInState.invalidPassword = true;
                // }
              } else {
                this.$set(this.signInState, 'success', true);
                this.setSignInState();
              }
          });
        }
      },
      requestUserSignIn() {
        const endpoint = 'http://localhost:5000/sign-in';
        return axios.post(endpoint, {
          email: this.email,
          password: this.password,
        });
      },
      setSignInState() {
        this.$set(
          this.signInState, 'invalidEmail', this.signInState.response.message.userNotFound
        );
        this.$set(
          this.signInState, 'invalidPassword',
          this.signInState.response.message.passwordInvalid
        );
      }
    },
  };
</script>

<style scoped>
  .form-width {
    width: 30vw;
  }

  .input-label-text {
    font-size: 0.9em;
  }
</style>
