 
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
        <v-btn :to="{name:''}">Back</v-btn>
        <v-btn :to="{name:'', params: { service: selectedItem.name } }">Book Now</v-btn>
        <v-btn :to="{ name: '', params: { service: selectedItem.name } }">Get Estimate</v-btn>
     </v-row>

    </v-container>
  </template>
  <script setup>

     const slides = ['First', 'Second', 'Third']
     const colors = ['red', 'green', 'blue']
  </script>