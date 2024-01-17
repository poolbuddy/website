<template>
  <v-container
        color="secondary"
      >
   
        <h1 class="text-center">Options for Remodel</h1>
        <h4 class="text-center">This isnt an exhaustive list of what we are capable of
           providing you are free to inquire if you want something that isnt on this list</h4>
  
        <v-row no-gutters >
          <v-col v-for="(service, index) in services" :key="index" class="d-flex justify-center">
          <!-- Product Card -->
          <v-card
            height="300"
            width="300"
            class="ma-2"
            link
            :to="{ name: 'remodel-detail', params: { id: service.id } }">
            <v-img :src="service.image"></v-img>
            <v-card-title>{{ service.name }}</v-card-title>
            <v-card-subtitle>Contact us today</v-card-subtitle>
         
          </v-card>
        </v-col>
        </v-row>
        <v-expansion-panels variant="popout" class="my-4">
          <v-expansion-panel
            title="Will it cost less if i get a repair on a opening or other service"
            text="Debris isnt really a problem what is the problem usually is the combination of large puddles of water 
            and the debri making it heavy and difficult by clogging the filter.  And if that water on the cover gets in that pool then 
            that could potentially make clearing the water more difficult.  So if there is no large puddles of water then there is 99% likelihood
            that there will be no extra fee."
          ></v-expansion-panel>
          <v-expansion-panel
            title="Faq"
            text=""
          ></v-expansion-panel>
          <v-expansion-panel
            title="faq2"
            text=""
          ></v-expansion-panel>
        </v-expansion-panels>
    </v-container>
</template>
<script setup>

  </script>