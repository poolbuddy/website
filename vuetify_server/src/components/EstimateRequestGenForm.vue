<template>
  <v-container
        color="secondary"
        mode="manual"
      >
    
      <v-card>
        <v-form >
         
         <h1 class="pa-6 ma-6 text-center">Estimate Form </h1>
         <v-row no-gutter justify="center">
          <v-col  cols="12" md="6" class="">
            <h3 class="align-center d-flex pa-1 ma-1"> customers email : </h3>
            <v-text-field
            density="compact"
            hide-details="auto"
            disabled
            v-model="email"
            label="Email address"
          ></v-text-field>
          <h3 class="align-center d-flex  pa-1 ma-1" > Phone Number : </h3>
          <v-text-field
           v-model="phone"
           hide-details="auto"
           disabled
           label="Phone Number"
         ></v-text-field>
         <h3 class="align-center d-flex" > delivery method: </h3>
          <v-select
            v-model="delivery"
            :items="['Email', 'Sms', 'Both']"
            chips
            label="How Do You Want To Recieve Estimate"
            
          ></v-select>
          <h3 class="align-center d-flex" > Add Picture(s) for a more accurate estimate : </h3>
           <v-file-input
            v-model="picture_array"
            chips
            multiple
            label="File input w/ chips"
          ></v-file-input>
          <h3 class="align-center d-flex" > Requested Service(s) : </h3>
           <v-select
            v-model="service"
            :items="selectItems"
            chips
            label="Select Service(s)"
            multiple
          ></v-select>
          </v-col>
          </v-row>
         
          <v-row no-gutter justify="end">
            <v-btn  class="ma-8 pa-3" @click="onSubmit">Get1</v-btn>
          </v-row>
        </v-form>
      </v-card>
      <v-alert
        v-for="(error, index) in errors"
        :key="index"
        :color="error.type === 'success' ? 'success' : 'error'"
        :icon="error.type === 'success' ? '$success' : '$error'"
        :title="error.title"
        :text="error.text"
      ></v-alert>
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


const email = store.email
const service = ref([ route.params.service? route.params.service:null,])
const phone = store.profile.phone
const urgency = ref()
const flexibility = ref()
const someone_home = ref()
const do_start_at_time = ref()
const requested_date = ref(null)
const requested_time = ref(null)
const selectItems = ref([])
const delivery = ref(null)
const picture_array = ref(null)

      
  

  const onSubmit = () => {
      const formData = {
        user_email: email.value,
        user_phone: phone.value,
        services_of_interest: service.value,
        date_of_request: requested_date.value,
        date_given: null,
        photos: null,
        time_of_day: requested_time.value,
        call_asap: false,
        confirm_text: true,
        picture_array: null
      };

      errors.value.push({
              type: 'success',
              title: 'Success - You have updated your profile',
              text: 'You have created an account.',
            })
    }


onMounted(() => {

fetchServices();

});

const fetchServices = async () => {

  try {
  const response = await apiService.fetchServiceList();
  selectItems.value = response.data.map(item => item.name);

  } catch (error) {
  console.error('Error fetching estimates:', error);
  }
  };


</script>