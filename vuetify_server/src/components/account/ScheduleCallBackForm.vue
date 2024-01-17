<template>
  <v-container
        color="secondary"
        mode="manual"
      >
    
      <v-card>
        <v-form>
         
         <h1 class="pa-6 ma-6 text-center">Get one of our techs to call you back to answer any of your questions</h1>
         <v-row no-gutter justify="center">
          <v-col sm="12" md="6">
            <h3 class="align-center d-flex pa-1 ma-1"> customers email : </h3>
            <v-text-field
            hide-details="auto"
            v-model="email"
            disabled
            label="Email Address"
          ></v-text-field>
          <h3 class="align-center d-flex pa-1 ma-1"> customers phone number : </h3>
            <v-text-field
            hide-details="auto"
            v-model="phone"
            disabled
            label="Phone Number"
          ></v-text-field>
            <h3 class="align-center d-flex pa-1 ma-1"> Services of interest : </h3>
            <v-select
            v-model="service"
            :items="selectItems"
            chips
            label="Select Service(s)"
            multiple
          ></v-select>
         
        </v-col>
         </v-row>
         
          <v-row no-gutters justify="center">
           <v-date-picker
              v-model="requested_date"
              color="primary"
              class="pa-6 ma-6 "
            ></v-date-picker>
           </v-row>
           <h1 class="pa-6 ma-6 text-center">What part of the day do you want us to call you ?</h1>
           <v-slider
            class="ma-16 pa-16"
            v-model="requested_time"
            :ticks="times"
            :max="3"
            step="1"
            show-ticks="always"
            tick-size="4"
          ></v-slider>
      
      <v-row no-gutters justify="end">
        <v-btn  class="ma-6" @click="submitForm">Give Me a Call</v-btn>
      </v-row>
      <v-alert
                v-for="(error, index) in errors"
                :key="index"
                :color="error.type === 'success' ? 'success' : 'error'"
                :icon="error.type === 'success' ? '$success' : '$error'"
                :title="error.title"
                :text="error.text"
              ></v-alert>
        </v-form>
      </v-card>
  </v-container>
</template>
<script setup>
import {useUser} from '@/store/user';
import { useRoute, useRouter } from 'vue-router';
import * as apiService from '@/assets/js/apiService';
import { ref, onMounted  } from 'vue';

const route = useRoute();
const router = useRouter();
const store = useUser();

const phone = store.profile.phone
const email = store.email
const service = ref([route.params.service? route.params.service:null,])
const requested_time = ref(null)
const requested_date = ref(null)
const selectItems = ref([])
const times = {
            0: '8-10',
            1: '10-12',
            2: '12-2',
            3: '2-4'
          }
     

const submitForm = () => {
      const formData = {
        email: email,
        service: service.value,
        requested_date: requested_date.value,
        requested_time: requested_time.value,
      };
      errors.value.push({
              type: 'success',
              title: 'Success - You have updated your profile',
              text: 'You have created an account.',
            })
     

    }
  
     




    
</script>