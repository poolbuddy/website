<template>
    <v-form  >
       <v-container>
        
        <v-text-field type="email" v-model="email" label="Email" prepend-icon="mdi-account"></v-text-field>
        <v-text-field type="password" v-model="password" label="Password" prepend-icon="mdi-lock"></v-text-field>
        <v-sheet v-if="errors.length">
            <p
                v-for="error in errors"
                v-bind:key="error"
            >
                {{ error.message }}
            </p>
           
        </v-sheet>
        <v-row no-gutters> 
            <v-btn @click.prevent="submit">
                Login
            </v-btn> 
            <v-btn :to="{ name: 'reset'}">
              Sign Up
            </v-btn> 
            <v-btn :to="{ name: 'reset'}">
              Forgot Password
            </v-btn>  
        </v-row>
    </v-container>
    
    </v-form>
</template>
<script setup>
import axios from 'axios'
import { useUser } from '@/store/user'
import { ref, watchEffect } from 'vue';
import { useRouter } from 'vue-router';
import * as apiService from '@/assets/js/apiService';

const email = ref(null)
const password = ref(null)
const errors = ref([])
const router = useRouter()

const store = useUser()
const token = ref(null)
const data1 = ref(null)
const data2 = ref(null)

const submit = async () => {
  try {
    errors.value = []

    const loginData = {
      email: email.value,
      password: password.value
    }

    data1.value = await apiService.fetchLogin(loginData)
    data2.value = await apiService.fetchCustomerProfile(loginData.email)


  } catch (error) {
    // Handle errors
    if (error.response) {
      for (const property in error.response.data) {
        errors.push(`${property}: ${error.response.data[property]}`)
      }
    } else if (error.message) {
      console.log(JSON.stringify(error.message))
    } else {
      console.log(JSON.stringify(error))
    }
  }
}

watchEffect(() => {
  if (data1.value !== null && data2.value !== null) {
    token.value = data1.value.data.auth_token
    store.setToken(token.value)
    store.email = email.value
    store.profile = data2.value.data[0]

     // Perform subsequent API call
     apiService.add_last_login(data2.value.data[0].id)
      .then((addLoginResponse) => {
      
      })
      .catch((error) => {
       
      });
    
    axios.defaults.headers.common["Authorization"] = "Token " + token.value
    localStorage.setItem("token", token.value)
    localStorage.setItem("email", email.value)
    localStorage.setItem("profile", JSON.stringify(data2.value.data[0]) )

    router.push('/Dashboard')
  }
});
</script>
