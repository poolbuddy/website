 
<template>
    <v-container
        color="secondary"
      >
      <h1 class="text-center my-10">{{ selectedItem.name }}</h1>
      <v-row no-gutters justify="center">
        <v-img 
        max-width="400"
        :src=" selectedItem.image "
        class="rounded-circle" 
       ></v-img>
      </v-row>
     


  <v-row no-gutters justify="center">
    <v-col>
        <h3 class="text-center my-10">{{ selectedItem.description }}
      </h3>
    </v-col>

  </v-row>
     <v-row justify="center">
        <v-btn :to="{name:'repair'}">Back</v-btn>
        <v-btn :to="{name:'book', params: { service: selectedItem.name } }">Book Now</v-btn>
        <v-btn :to="{ name: 'get-estimate', params: { service: selectedItem.name } }">Get Estimate</v-btn>
     </v-row>

    </v-container>
  </template>
  <script>
import { repair_list2 } from '@/assets/js/Lists';  
  export default{

    computed: {
        selectedItem() {
          // Retrieve the selected item from the store or API based on the route parameter
          const itemId = this.$route.params.id;
          // Replace this with your actual logic to fetch the item details
          // For demonstration, using a mock data array
          const items = repair_list2
          return items.find(item => item.id == itemId) || {};
        },

    },
    data() {
    return {
      slides: ['First', 'Second', 'Third'],
      colors: ['red', 'green', 'blue'],
    };
  },

  }
  </script>