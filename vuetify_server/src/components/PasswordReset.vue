<template>
    <v-form @submit.prevent="submitForm">
       <v-container>
        
        <v-text-field type="email" v-model="email" label="Email" prepend-icon="mdi-account"></v-text-field>
   
        <v-sheet v-if="errors.length">
            <p
                v-for="error in errors"
                v-bind:key="error"
            >
                {{ error.message }}
            </p>
           
        </v-sheet>
        <v-row no-gutters> 
            <v-btn type="submit">
                Reset
            </v-btn>    
        </v-row>
    </v-container>
    
    </v-form>
</template>
<script>
import axios from 'axios'
import { useUser } from '@/store/user'
export default {
    name:'PasswordResetForm',
    setup(){
        const store = useUser()
        return{
            store
        }
    },
    data () {
        return {
            email:'',
            errors: []
        }
    },
    methods: {
        
        
     submitForm(e) {
      try {
       alert("yooo")
        this.errors = []

        // Log in and get the auth token
        const resetResponse =  axios.post("http://localhost:8000/auth/users/reset_password/", {
          email: this.email
        })

        alert("after")
        console.log(resetResponse)
        

        // Redirect to the dashboard
        this.$router.push('/Dashboard')
      } catch (error) {
        // Handle errors
        if (error.response) {
          for (const property in error.response.data) {
            this.errors.push(`${property}: ${error.response.data[property]}`)
          }
        } else if (error.message) {
          console.log(JSON.stringify(error.message))
        } else {
          console.log(JSON.stringify(error))
        }
      }
    }
    },
}
</script>
