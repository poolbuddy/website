<template>
    <v-form @submit.prevent="submitForm">
       <v-container>
        
        <v-text-field type="email" v-model="email" label="Email" prepend-icon="mdi-email"></v-text-field>
        <v-text-field type="password" v-model="password" label="Password" prepend-icon="mdi-lock"></v-text-field>
        <v-sheet v-if="errors.length">
            <p
                v-for="error in errors"
                v-bind:key="error"
            >
                {{ error }}
            </p>
        </v-sheet>
        <v-row no-gutters> 
            <v-btn type="submit">
                Sign Up
            </v-btn>    
        </v-row>
    </v-container>
    </v-form>
</template>
<script>
import axios from 'axios'
export default {
    name:'EmailPasswordForm',
    data () {
        return {
            email: '',
            password: '',
            errors: []
        }
    },
    methods: {
        submitForm(e) {
            const formData = {
                email: this.email,
                password: this.password
            }
            axios 
                .post("http://localhost:8000/auth/users/", formData)
                .then(response => {
                   
                    this.$router.push('/Login')
                })
                .catch(error => {
                    if (error.response){
                        for (const property in error.response.data){
                            this.errors.push( `${property}: ${error.response.data[property]}`
                            )
                        }
                    }else if (error.message){
                        console.log(JSON.stringify(error.message))
                    } else {
                        console.log(JSON.stringify(error))
                    }
                })
               
        }
    },
}
</script>