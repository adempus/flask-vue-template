<template>
  <b-container class="form-width mt-5">
    <div>
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
              class="input-label-text"
            >
              <b-form-input
                id="first-name"
                v-model="firstName"
                placeholder="John"
                aria-describedby="first-name-input-feedback"
                :state="validateState('firstName')"
                trim
              ></b-form-input>
              <div v-if="!this.$v.firstName.$dirty">
                <b-form-invalid-feedback
                  align="left"
                  :state="this.$v.firstName.required"
                  id="first-name-input-feedback">
                  First name is required
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
              class="input-label-text"
            >
              <b-form-input
                id="last-name"
                v-model="lastName"
                placeholder="Doe"
                trim
              ></b-form-input>
            </b-form-group>
          </b-col>
        </b-row>
        <!-- username -->
        <b-form-group
          id="usernameGroup"
          label="Username:"
          label-for="user-name"
          label-align="left"
          class="input-label-text"
        >
          <b-form-input
            id="user-name"
            v-model="username"
            required
            placeholder="Enter a username"
            trim
          ></b-form-input>
        </b-form-group>
        <!-- email -->
        <b-form-group
          id="emailGroup"
          label="Email:"
          label-for="email"
          label-align="left"
          class="input-label-text"
        >
          <b-form-input
            id="email"
            v-model="email"
            required
            placeholder="useremail@domain.com"
            trim
          ></b-form-input>
        </b-form-group>
        <b-row>
        <!-- Password -->
          <b-col>
            <b-form-group
              id="password"
              label="Password:"
              label-for="password-input"
              label-align="left"
              class="input-label-text"
            >
              <b-form-input
                id="password-input"
                v-model="password"
                required
                type="password"
              ></b-form-input>
            </b-form-group>
          </b-col>
          <!-- Confirm Password -->
          <b-col>
            <b-form-group
              id="checkedPassword"
              label="Confirm Password"
              label-for="checked-pass"
              label-align="left"
              class="input-label-text"
            >
              <b-form-input
                id="checked-pass"
                v-model="checkedPassword"
                required
                type="password"
              ></b-form-input>
            </b-form-group>
          </b-col>
        </b-row>
        <!-- Submit button -->
        <b-row class="justify-content-end mt-4 pl-3 pr-3">
          <b-button type="submit" block variant="info" v-on:click="submitClicked = true">
            Submit
          </b-button>
        </b-row>
      </b-form>
      </b-card>
    </div>
  </b-container>
</template>

<script>
  import { required, minLength } from 'vuelidate/lib/validators';

  export default {
    data: () => ({
      firstName: '',
      lastName: '',
      email: '',
      username: '',
      password: '',
      checkedPassword: '',
      submitClicked: false,
    }),

    validations: {
      firstName: {
        required
      },
    },

    methods: {
      validateState(value) {
        const { $dirty, $error } = this.$v[value];
        return $dirty ? !$error : null;
      },
      submit() {
        console.log('Submitted');
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
</style>
