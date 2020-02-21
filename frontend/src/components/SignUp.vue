<template>
  <b-container class="form-width mt-5">
    <div>
<!--      <p>sign up status: {{ this.signUpSuccess ? "success" : "failed" }}</p>-->
<!--      <p>sign up response: {{ this.signUpResponse }}</p>-->
      <b-card-header bg-variant="light" header-bg-variant="dark" header-text-variant="white">
        <h4>Sign Up</h4>
      </b-card-header>
      <b-card class="text-center">
      <b-form @submit.prevent="submit">
        <b-row>
          <!-- First name-->
          <b-col>
            <b-form-group
              id="firstNameGroup"
              label="First Name:"
              label-for="first-name"
              label-align="left"
              class="input-label-text">
              <b-form-input
                id="first-name"
                v-model="firstName"
                placeholder="John"
                aria-describedby="first-name-input-feedback"
                :state="validateState('firstName')"
                trim>
              </b-form-input>
              <!-- first name invalid feedback-->
              <div v-if="!this.$v.firstName.required && submitClicked">
                <b-form-invalid-feedback
                  align="left"
                  :state="this.$v.firstName.required"
                  id="first-name-input-feedback">
                  * First name is required
                </b-form-invalid-feedback>
              </div>
            </b-form-group>
          </b-col>
          <!-- Last name-->
          <b-col>
            <b-form-group
              id="lastNameGroup"
              label="Last Name:"
              label-for="last-name"
              label-align="left"
              class="input-label-text">
              <b-form-input
                id="last-name"
                v-model="lastName"
                placeholder="Doe"
                aria-describedby="last-name-input-feedback"
                :state="validateState('lastName')"
                trim>
              </b-form-input>
              <!-- last name invalid feedback -->
               <b-form-invalid-feedback v-if="!this.$v.lastName.required && submitClicked"
                align="left"
                :state="this.$v.lastName.required"
                id="last-name-input-feedback">
                * Last name is required
               </b-form-invalid-feedback>
            </b-form-group>
          </b-col>
        </b-row>
        <!-- username -->
        <b-form-group
          id="usernameGroup"
          label="Username"
          label-for="user-name"
          label-align="left"
          class="input-label-text">
          <b-form-input
            id="user-name"
            v-model="username"
            placeholder="Enter a username"
            @input="modifyUsername()"
            :state="validateState('username')"
            aria-describedby="username-input-feedback"
            trim>
          </b-form-input>
            <!-- username name requirement invalid feedback -->
            <b-form-invalid-feedback v-if="!this.$v.username.required && submitClicked"
              align="left"
              :state="this.$v.username.required"
              id="username-input-feedback">
              * Username name is required
            </b-form-invalid-feedback>
          <!-- username name minimum length invalid feedback -->
          <b-form-invalid-feedback v-if="!this.$v.username.minLength && submitClicked"
              align="left"
              :state="this.$v.username.minLength"
              id="username-input-feedback">
              * Must be 2 or more characters
            </b-form-invalid-feedback>
          <!-- username name exsits feedback -->
          <b-form-invalid-feedback
            v-if="this.$v.username.required && !this.$v.email.usernameUnique && submitClicked"
            align="left"
            :state="this.$v.username.usernameUnique"
            id="username-input-feedback">
            * This username is already in use
          </b-form-invalid-feedback>
        </b-form-group>
        <!-- email -->
        <b-form-group
          id="emailGroup"
          label="Email:"
          label-for="email"
          label-align="left"
          class="input-label-text">
          <b-form-input
            id="email"
            v-model="email"
            placeholder="useremail@domain.com"
            aria-describedby="email-input-feedback"
            @input="modifyEmail()"
            :state="validateState('email')"
            trim>
          </b-form-input>
          <!-- email invalid feedback -->
          <b-form-invalid-feedback v-if="!this.$v.email.required && submitClicked"
            align="left"
            :state="this.$v.email.required"
            id="email-input-feedback">
            * Email is required
          </b-form-invalid-feedback>
          <!-- exsiting email feedback -->
          <b-form-invalid-feedback
            v-if="this.$v.email.required && submitClicked && !this.$v.email.emailUnique"
            align="left"
            :state="this.$v.email.emailUnique"
            id="email-input-feedback">
            * This email is already in use
          </b-form-invalid-feedback>
        </b-form-group>
        <b-row>
        <!-- Password -->
          <b-col>
            <b-form-group
              id="password"
              label="Password:"
              label-for="password-input"
              label-align="left"
              class="input-label-text">
              <b-form-input
                id="password-input"
                v-model="password"
                type="password"
                aria-describedby="password-input-feedback">
              </b-form-input>
              <!-- password required feedback -->
              <b-form-invalid-feedback v-if="!this.$v.password.required && submitClicked"
                align="left"
                :state="this.$v.password.required"
                id="password-input-feedback">
                * Password is required
              </b-form-invalid-feedback>
              <b-form-invalid-feedback v-if="!this.$v.password.minLength && submitClicked"
                align="left"
                :state="this.$v.password.minLength"
                id="password-input-feedback">
                * Password must be 7 character or more
              </b-form-invalid-feedback>
            </b-form-group>
          </b-col>
          <!-- Confirm Password -->
          <b-col>
            <b-form-group
              id="checkedPassword"
              label="Confirm Password"
              label-for="checked-pass"
              label-align="left"
              class="input-label-text">
              <b-form-input
                id="checked-pass"
                v-model="checkedPassword"
                type="password"
                aria-describedby="checked-password-input-feedback">
              </b-form-input>
              <!-- checkedPassword match feedback -->
              <b-form-invalid-feedback
                v-if="!this.$v.checkedPassword.sameAsPassword && submitClicked"
                align="left"
                :state="this.$v.checkedPassword.sameAsPassword"
                id="checked-password-input-feedback">
                * Must match password
              </b-form-invalid-feedback>
            </b-form-group>
          </b-col>
        </b-row>
        <!-- Submit button -->
        <b-row class="justify-content-end mt-4 pl-3 pr-3">
          <b-button type="submit" block variant="info">Submit</b-button>
        </b-row>
        <b-row>
          <b-link href="/sign-in" class="pt-3 mr-4 mb-n2 sign-in-link mx-auto">
            Already a user? Sign in
            <b-icon-chevron-right></b-icon-chevron-right>
          </b-link>
        </b-row>
      </b-form>
      </b-card>
    </div>
  </b-container>
</template>

<script>
  import axios from 'axios';
  import _ from 'lodash';
  import Vue from 'vue';
  import { required, minLength, sameAs, email } from 'vuelidate/lib/validators';

  const emailUnique = (value, vm) => !vm.isExistingEmail
    && (value.toUpperCase() !== vm.attemptedEmail.toUpperCase());
  const usernameUnique = (value, vm) => !vm.isExistingUsername
    && value.toUpperCase() !== vm.attemptedUsername.toUpperCase();

  export default {
    name: 'SignUp',

    data: () => ({
      firstName: '',
      lastName: '',
      email: '',
      username: '',
      password: '',
      checkedPassword: '',
      signUpForm: {

      },
      submitClicked: false,
      signUpSuccess: false,
      isExistingUsername: false,
      isExistingEmail: false,
      attemptedEmail: '',
      attemptedUsername: '',
      signUpResponse: null,
    }),

    validations: {
      firstName: {
        required
      },
      lastName: {
        required
      },
      username: {
        required,
        minLength: minLength(2),
        usernameUnique,
      },
      email: {
        required,
        email,
        emailUnique,
      },
      password: {
        required,
        minLength: minLength(7)
      },
      checkedPassword: {
        required,
        sameAsPassword: sameAs('password')
      }
    },

    methods: {
      validateState(value) {
        const { $dirty, $error } = this.$v[value];
        return $dirty ? !$error : null;
      },
      modifyUsername() {
        this.$v.username.$touch();
        if (this.$v.username.$invalid) {
          if (this.attemptedUsername.toLowerCase() !== this.username.toLowerCase()) {
            this.isExistingUsername = false;
          }
        }
      },
      modifyEmail() {
        this.$v.email.$touch();
        if (this.$v.email.$invalid) {
          if (this.attemptedEmail.toLowerCase() !== this.email.toLowerCase()) {
            this.isExistingEmail = false;
          }
        }
      },
      determineError() {
        if (_.has(this.signUpResponse, 'message.emailExists')) {
          this.isExistingEmail = this.signUpResponse.message.emailExists;
          if (this.isExistingEmail) {
            this.attemptedEmail = this.email;
          }
          this.$v.email.$reset();
        }
        if (_.has(this.signUpResponse, 'message.usernameExists')) {
          this.isExistingUsername = this.signUpResponse.message.usernameExists;
          if (this.isExistingUsername) {
            this.attemptedUsername = this.username;
          }
          this.$v.username.$reset();
        }
      },
      requestUserSignUp() {
        const endpoint = 'http://localhost:5000/sign-up';
        return axios.post(endpoint, {
          firstName: this.firstName,
          lastName: this.lastName,
          userName: this.username,
          email: this.email,
          password: this.password
        });
      },
      submit() {
        this.submitClicked = true;
        this.$v.$touch();
        if (this.$v.$invalid) {
          console.log('Invalid credentials provided');
        } else {
          this.requestUserSignUp().then((response) => {
            console.log('response:', response);
            this.signUpResponse = response.data;
            if (this.signUpResponse.error === true) {
              this.signUpSuccess = false;
              this.determineError();
            } else {
              this.signUpSuccess = true;
            }
          }).catch((error) => {
            this.signUpSuccess = false;
            console.log('An error occurred.');
            console.error(error);
          });
        }
      },
    },
  };
</script>

<style scoped>
  .input-label-text {
    font-size: 0.9em;
  }

  .form-width {
    width: 35vw;
  }

  .sign-in-link {
    font-size: 0.75em;
    color: #343A40;
  }

  @media (max-width: 1320px) {
    .form-width {
      width: 100vw;
    }
  }
</style>
