<template>
  <v-container
        color="secondary"
      >
   
        <h1 class="text-center">{{ selectedItem.name }}</h1>
        <v-img
        aspect-ratio="16/9"
        class="rounded-pill"
        max-height="600"
        
      :src="selectedItem.image"
      >

      </v-img>
      <h2 class="text-center">{{ selectedItem.blerb }}</h2>
  
        
        <v-row no-gutters>
          <v-btn :to="{name: 'install'}">Back</v-btn>
      
      <v-btn :to="{name:'book', params: { service: selectedItem.name } }">Book Now</v-btn>
        <v-btn :to="{ name: 'get-estimate', params: { service: selectedItem.name } }">Get Estimate</v-btn>
        </v-row>
    </v-container>
</template>
  <script setup>

  </script>