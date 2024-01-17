<template>
  <v-container
        color="secondary"
        mode="manual"
      >
    
      <v-card>
        <v-form >
         
        <h1 class="pa-6 ma-6 text-center">Service Booking Form</h1>
        <v-row no-gutter>
        <v-row no-gutter justify="center">
        <v-col  sm="12" md="6" class="">
           
           <h3 class="align-center d-flex" > Service : </h3>


           <v-select
            v-model="service"
            :items="selectItems"
            chips
            label="Select Service(s)"
            multiple
          ></v-select>
         
          </v-col>
         
         </v-row>
          <v-row no-gutter justify="center">
          <v-col sm="12" md="6">
          <v-col  class=" ">
            <h3 class="align-center d-flex pa-1 ma-1"> customers email : </h3>
            <v-text-field
            hide-details="auto"
            v-model="email"
            disabled
            label="Email address"
          ></v-text-field>
          </v-col>
         
          <v-col  class="">
           <h3 class="align-center d-flex  pa-1 ma-1" > Phone Number : </h3>
           <v-text-field
           hide-details="auto"
           v-model="phone"
           disabled
           label="Phone Number"
         ></v-text-field>
         
          </v-col>
     
          <v-col  class=" ">
            <h3 class="align-center d-flex pa-1 ma-1"> Urgency : </h3>
            <v-radio-group inline v-model="urgency">
              <v-radio label="Urgent - I have an upcoming event and need the pool ready before a particular date" value="urgent"></v-radio>
              <v-divider></v-divider>
              <v-radio label="Mildly Ugent - Please I/my kids am/are really wanting to use it so I need it as soon as possible" value="mild"></v-radio>
              <v-divider></v-divider>
              <h1></h1>
              <v-radio label="No Urgency - Your earliest date you are in my area is fine" value="none"></v-radio>
            </v-radio-group>
          </v-col>
          <v-col  class="align-center d-flex flex-column ">
            <h2 class=" pa-1 ma-1">Appointment Flexibility</h2>
                      
            <v-radio-group inline v-model="flexibility">
              <v-radio label="Very Flexible I just want it done as soon as possible I dont care what day." value="very"></v-radio>
              <v-divider></v-divider>
              <v-radio label="Mildly Flexible - It has to be either at a particular times of day or particulars days of the week" value="midly"></v-radio>
              <v-divider></v-divider>
              <v-radio label="No Flexibilty I arranged my schedule for a particular day.  Also Inform me of any change in the appointment time." value="none"></v-radio>
            </v-radio-group>
            
            <v-switch label="Is someone going to be home during the appointment" v-model="someone_home"></v-switch>
            <v-switch label="Do you need the service to start at a particular time of the day?" v-model="do_start_at_time"></v-switch>
            
            
          </v-col>
        
        </v-col>
         </v-row>

         </v-row>
          <v-row no-gutters justify="center">
          
           <v-date-picker
              v-model="requested_date"
              color="primary"
              class="pa-6 ma-6 "
            ></v-date-picker>
           </v-row>
           <h2 class="pa-6 ma-6 text-center">What hours of the day?</h2>

           <v-slider
           class="ma-10 pa-10"
            v-model="requested_time"
            :ticks="times"
            :max="3"
            step="1"
            show-ticks="always"
            tick-size="4"
          ></v-slider>

      
      <v-row no-gutters justify="end">
        <v-btn  class="ma-6" @click="submit">Book it</v-btn>
      </v-row>
        </v-form>
        <v-alert
        v-for="(error, index) in errors"
        :key="index"
        :color="error.type === 'success' ? 'success' : 'error'"
        :icon="error.type === 'success' ? '$success' : '$error'"
        :title="error.title"
        :text="error.text"
      ></v-alert>
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
const errors = ref([])
const times = {
            0: '8-10',
            1: '10-12',
            2: '12-2',
            3: '2-4',
          }

  const submit = () => {
  
        const formData = {
            services_of_interest: service.value,
            user_email: email,
            user_phone: phone,
            urgency: urgency.value,
            appt_flexibility: flexibility.value,
            someone_willB_home: someone_home.value,
            requests_particular_time_of_day: do_start_at_time.value,
            requested_date: requested_date.value,
            time_of_day: requested_time.value,
            sent_estmiate: false,
            confirmed: false,
            confirmed_date: "2023-12-30"
        }
    
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
    errors.value.push('Error fetching estimates:', error);
  }
};


</script>