<template>
   
    <v-form ref="form">
      <h1>Personal Info</h1>
      <v-text-field
        v-model="name"
        type="input"
        label="First Name"
        required
      ></v-text-field>

      <v-text-field
        v-model="name"
        type="input"
        label="Last Name"
        required
      ></v-text-field>

      <v-text-field
        v-model="address"
        type="input"
        label="Mobile number"
        required
      ></v-text-field>

      <v-text-field
        v-model="address"
        type="input"
        label="Email"
        required
      ></v-text-field>

      <v-divider></v-divider>

      <h1>Mailing address</h1>

      <v-text-field
        v-model="name"
        type="input"
        label="Street"
        required
      ></v-text-field>

      <v-text-field
        v-model="name"
        type="input"
        label="City"
        required
      ></v-text-field>

      <v-text-field
        v-model="address"
        type="input"
        label="State"
        required
      ></v-text-field>

      <v-text-field
        v-model="address"
        type="input"
        label="Zip"
        required
      ></v-text-field>

      <h1>Transportation Info</h1>

      <v-switch
        v-model="people"
        color="primary"
        label="I currently have a NYS drivers license"
        value="John"
        hide-details
      ></v-switch>

      <v-switch
        v-model="people"
        color="primary"
        label="I have a vehicle"
        value="John"
        hide-details
      ></v-switch>

      <v-switch
        v-model="people"
        color="primary"
        label="I have a vehicle with a trailer hitch"
        value="John"
        hide-details
      ></v-switch>

      <h1>What are you looking to do?</h1>

      <v-checkbox
        v-model="checkbox1"
        label="Openings / Closings"
      ></v-checkbox>
      <v-checkbox
        v-model="checkbox2"
        label="Regular Maintenance"
      ></v-checkbox>
      <v-checkbox
        v-model="checkbox1"
        label="Power Vacuums"
      ></v-checkbox>
      <v-checkbox
        v-model="checkbox2"
        label="Service/Install Heaters"
      ></v-checkbox>
      <v-checkbox
        v-model="checkbox2"
        label="Service/Install Filters"
      ></v-checkbox>
      <v-checkbox
        v-model="checkbox2"
        label="Service/Install Pumps"
      ></v-checkbox>
      <v-checkbox
        v-model="checkbox2"
        label="Service/Install Safety Covers"
      ></v-checkbox>
      <v-checkbox
        v-model="checkbox2"
        label="Service Plumbing Lines"
      ></v-checkbox>
      <v-checkbox
        v-model="checkbox2"
        label="Water Chemistry Balancing"
      ></v-checkbox>
      
      <v-switch
        v-model="people"
        color="primary"
        label="I have past experience"
        value="John"
        hide-details
      ></v-switch>
      <v-switch
        v-model="people"
        color="primary"
        label="I have had professional experience"
        value="John"
        hide-details
      ></v-switch>
      <v-combobox
        label="Years of professional experience"
        :items="['1', '2', '3', '4', '5', '5+']"
      ></v-combobox>

      

      <div> I agree to The Pool Buddy's Terms of Use, and by clicking the box and proceeding, I agree that The Pool Buddy's Pool Service or its representatives may contact me by email, phone, or SMS (including by automatic telephone dialing system) at the email address or number I provide, including for marketing purposes.

      </div>
      <v-switch
        v-model="people"
        color="primary"
        label="I agree"
        value="John"
        hide-details
      >    </v-switch>
      <div class="d-flex flex-column">
        <v-btn
          color="success"
          class="mt-4"
          block
          @click="submit"
        >
        submit
        </v-btn>

      </div>
      <v-alert
        v-for="(error, index) in errors"
        :key="index"
        :color="error.type === 'success' ? 'success' : 'error'"
        :icon="error.type === 'success' ? '$success' : '$error'"
        :title="error.title"
        :text="error.text"
      ></v-alert>
    </v-form>


  
</template>
<script setup>
import {useUser} from '@/store/user';
import { useRoute, useRouter } from 'vue-router';
import * as apiService from '@/assets/js/apiService';
import { ref, onMounted  } from 'vue';

const svgContent = ref(null)


const submit = () => {
  errors.value.push({
              type: 'success',
              title: 'Success - You have updated your profile',
              text: 'You have created an account.',
            })
}
</script>