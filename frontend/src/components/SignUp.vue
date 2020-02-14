<template>
  <b-container class="form-width mt-5">
    <div>
      <b-card-header bg-variant="light" header-bg-variant="dark" header-text-variant="white">
        <h4>Sign Up</h4>
      </b-card-header>
      <b-card class="text-center">
      <b-form>
        <b-row>
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
                required
                placeholder="John"
                trim
              ></b-form-input>
            </b-form-group>
          </b-col>
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
                required
                placeholder="Doe"
                trim
              ></b-form-input>
            </b-form-group>
          </b-col>
        </b-row>
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

        <b-form-group
          id="emailGroup"
          label="Email:"
          label-for="email"
          label-align="left"
          class="input-label-text"
        >
          <b-form-input
            v-validate="'required|email'" name="email"
            id="email"
            v-model="email"
            required
            placeholder="useremail@domain.com"
            trim
          ></b-form-input>
        </b-form-group>

        <b-row>
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
        <b-row class="justify-content-end mt-4 pl-3 pr-3">
          <b-button type="submit" block variant="info">Submit</b-button>
        </b-row>
      </b-form>
      </b-card>
    </div>
  </b-container>
</template>

<script>
  export default {
    data: () => ({
      firstName: '',
      lastName: '',
      email: '',
      username: '',
      password: '',
      checkedPassword: '',
    }),

    methods: {
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
