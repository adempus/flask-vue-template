<template>
  <UserSession>
    <b-alert fade class="successAlert position-absolute"
             :show="hideAlertTimer"
             variant="success"
             @dismiss-count-down="updateCountdown">
      Log Submitted Successfully!
    </b-alert>
    <b-container fluid>
      <div class="ml-5 mt-4">
        <b-row align-v="start">
          <h2 class="mb-5">New Log Entry</h2>
        </b-row>
        <b-row align-v="start">
          <b-form @submit.prevent="submit()">
            <!-- title input  -->
            <b-form-group
              id="entry-title-group"
              label="Title: "
              label-for="entry-title"
              label-align="left"
            >
              <b-form-input
                id="entry-title"
                v-model="entryForm.title"
                type="text"
                placeholder="Captain's Log 0243"
                class="w-100"
              ></b-form-input>
            </b-form-group>

            <!-- entry input  -->
            <b-form-group
              id="entry-content-group"
              label="Entry:"
              label-for="entry-content"
              label-align="left"
            >
              <b-form-textarea
                id="entry-content"
                v-model="entryForm.content"
                placeholder="Enter some text here..."
                rows="4"
                no-resize
              ></b-form-textarea>
              <b-form-invalid-feedback
                align="left"
                v-if="this.submitClicked && this.$v.entryForm.content"
                :state="this.$v.entryForm.content.required">
                Entry field cannot be empty.
              </b-form-invalid-feedback>
            </b-form-group>
            <b-row class="d-flex justify-content-start pl-3 pt-3">
              <b-button type="submit" variant="primary">Submit</b-button>
            </b-row>
          </b-form>
        </b-row>
      </div>
    </b-container>
  </UserSession>
</template>

<script>
  import axios from 'axios';
  import { required } from 'vuelidate/lib/validators';

  export default {
    name: 'NewEntry',
    data() {
      return {
        entryForm: {
          title: '',
          content: ''
        },
        submitResponse: null,
        submitClicked: false,
        secsBeforeHideAlert: 2,
        hideAlertTimer: 0,
      };
    },
    validations: {
      entryForm: {
        content: { required }
      }
    },
    methods: {
      submit() {
        this.submitClicked = true;
        if (this.$v.$invalid) {
          console.log('Entry field empty');
        } else {
          this.postEntry()
            .then((response) => {
              this.submitResponse = response.data;
              if (!this.submitResponse.error) {
                Object.assign(this.$data, this.$options.data.apply(this));
                this.showSuccessAlert();
              }
            })
            .catch((error) => {
              console.log('An error occurred: ', error);
            });
        }
      },
      postEntry() {
        const endpoint = this.$root.postEntry;
        const headerConfig = {
          headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
        };
        return axios.post(endpoint, {
          userId: this.$store.getters.userId,
          title: this.entryForm.title,
          entry: this.entryForm.content,
        }, headerConfig);
      },
      showSuccessAlert() {
        this.hideAlertTimer = this.secsBeforeHideAlert;
      },
      updateCountdown(value) {
        this.hideAlertTimer = value;
      }
    },
  };
</script>

<style scoped>
  body {
    overflow-x: hidden;
    overflow-y: hidden;
  }
  .input-width {
    width: 30vw;
  }
  .successAlert {
    /*top: 5vh;*/
    top: 11.5%;
    left: 0;
    width: 100%;
  }
</style>
