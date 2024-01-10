<template>
    <v-form>
        <h1>address</h1>
        <v-text-field label="street" prepend-icon="mdi-maps"></v-text-field>
        <v-text-field label="city" prepend-icon="mdi-maps"></v-text-field>
        <v-text-field label="zip" prepend-icon="mdi-maps"></v-text-field>
        <h1>Phone Number</h1>
        <v-text-field label="Phone Number" prepend-icon="mdi-phone"></v-text-field>
    </v-form>
</template>
<script>

export default {
    name:'AddressForm',
    data() {
    return {
      
      street: null,
      city: null,
      zip: null,
      phone: null,
      
     
    }
},

};
</script>
