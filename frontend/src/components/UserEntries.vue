<template>
  <div>
    <b-row align-v="start">
      <h2 class="mx-5 mb-5">Log Entries </h2>
    </b-row>
    <div v-if="userEntries !== null">
      <div v-if="userEntries.length > 0">
        <div v-for="entry in userEntries">
          <b-card class="mx-5 my-4 w-50 pt-2 text-capitalize" body-class="text-left"
                  v-bind:title="entry.title === null ? 'Untitled' : entry.title">
            <b-icon icon="x-circle"
                    v-bind:id="entry.id"
                    v-on:click="displayDeleteConfirmation(entry)"
                    class="h5 position-relative float-right mt-n5"></b-icon>
            <b-card-text con>{{ entry.content }}</b-card-text>
            <b-card-text class="small text-muted">{{ entry.date }}</b-card-text>
          </b-card>
        </div>
      </div>
      <div v-else>
        <p>You have 0 log entries.</p>
        <router-link to="/user/:userId/new-entry" class="small" >Create a new entry.</router-link>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  import { BIcon } from 'bootstrap-vue';

  export default {
    name: 'UserEntries',
    components: {
      BIcon
    },
    mounted() {
      this.initUserEntries();
    },
    data() {
      return {
        userEntries: [],
        deletionTarget: null,
        deletionResponse: null,
        boxTwo: null,
      };
    },
    methods: {
      initUserEntries() {
        this.fetchEntries().then((response) => {
          const res = response;
          if (!res.data.error) {
            this.userEntries = res.data.data;
          }
        });
      },
      fetchEntries() {
        const endpoint = 'http://localhost:5000/get-user-entries';
        return axios.get(endpoint, {
          headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
        });
      },
      hoverDeleteIcon(hovered) {
        this.isMouseoverDeleteIcon = hovered;
      },
      mouseOverDeleteAction(entry) {
        this.deletionTarget = entry;
      },
      deleteEntry() {
        const endpoint = 'http://localhost:5000/delete-user-entry';
        return axios.delete(endpoint, {
          data: this.deletionTarget,
          headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
        });
      },
      displayDeleteConfirmation(entry) {
        this.deletionTarget = entry;
        this.showMsgBoxTwo();
      },
      showMsgBoxTwo() {
        this.boxTwo = '';
        this.$bvModal.msgBoxConfirm(`Are you sure you want to delete:\n "${this.deletionTarget.title}"`, {
          title: 'Delete Log?',
          size: 'sm',
          buttonSize: 'sm',
          okVariant: 'danger',
          okTitle: 'Yes',
          cancelTitle: 'Cancel',
          footerClass: 'p-2',
          hideHeaderClose: false,
          centered: true,
        })
          .then((value) => {
            this.boxTwo = value;
            if (this.boxTwo) {
              this.deleteEntry()
                .then((response) => {
                  console.log('response: ', response);
                  this.deletionResponse = response;
                  if (!this.deletionResponse.data.error) {
                    this.userEntries = this.userEntries.filter((entry) => {
                      return entry.id !== this.deletionTarget.id;
                    });
                    console.log('array post filter: ', this.userEntries);
                  }
                });
              console.log('deleted log: ', this.deletionTarget);
            }
          })
          .catch((err) => {
            // An error occurred
          });
      }
    }
  };
</script>

<style scoped>
  .deleteHover {
    background-color: #000000;
    color: #ffffff;
  }
</style>
