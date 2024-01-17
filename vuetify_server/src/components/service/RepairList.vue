
<template>
    <v-container
        color="secondary"
      >
      <h1 class="text-center">Repairs</h1>
  
      <h3 class="text-center">This is not an exhaustive list of what we are capable of repairing so 
        if you have something you would like looked at be sure to let us know.  Click 
        the learn more button to get a description of the repair.
      </h3>
      <v-row no-gutters >
        <v-col v-for="(repair, index) in repairs" :key="index" class="d-flex justify-center">
          <v-card 
           height="300"
           width="300"
           class="my-2"
            link
            :to="{ name: 'repair-detail', params: { id: repair.id } }">
            <v-img :src="repair.image"></v-img>
            <v-card-title>{{ repair.name }}</v-card-title>
            <v-card-sub-title class="text-center">{{ repair.blurb }}</v-card-sub-title>
    
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