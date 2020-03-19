<template>
  <b-container fluid>
    <div v-if="!isSignedIn">
      <h1>Error</h1>
      <p>Not signed in</p>
    </div>
    <div v-else class="ml-5">
      <b-row align-v="start" >
        <h2 class="mb-5">New Log Entry</h2>
      </b-row>
      <b-row align-v="start">
        <b-form @submit.prevent="submitEntry">
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
              class="input-width"
            ></b-form-input>
          </b-form-group>

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
</template>

<script>
  import axios from 'axios';
  import { required } from 'vuelidate/lib/validators';

  export default {
      name: 'NewEntry',
      data() {
        return {
          submitClicked: false,
          entryForm: {
            title: '',
            content: ''
          },
          submitResponse: null,
        };
      },
    validations: {
        entryForm: {
          content: { required }
        }
      },
      methods: {
        submitEntry() {
          this.submitClicked = true;
          if (this.$v.$invalid) {
            console.log('Entry field empty');
          } else {
            const endpoint = 'http://localhost:5000/post-new-entry';
            const headerConfig = { headers: { Authorization: `Bearer ${localStorage.getItem('token')}` } };
            axios.post(endpoint, {
              userId: this.$store.getters.userId,
              title: this.entryForm.title,
              entry: this.entryForm.content,
            }, headerConfig)
              .then((response) => {
                this.submitResponse = response.data;
                if (!this.submitResponse.error) {
                  Object.assign(this.$data, this.$options.data.apply(this));
                }
                // console.log('response: ', response);
            });
          }
        }
      },
      computed: {
        isSignedIn() {
          return this.$store.getters.isSignedIn;
        },
      }
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
</style>
