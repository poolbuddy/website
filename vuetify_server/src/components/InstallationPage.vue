<template>
    <v-container
      color="secondary"
    >
    <h1 class="text-center">Installs</h1>

    <h3 class="text-center">This is not an exhaustive list of what we are capable of installing so 
      if you have an idea at be sure to let us know.  Click 
      the learn more button to get a description of the repair.
    </h3>
    <v-row no-gutters >
      <v-col v-for="(install, index) in installs" :key="index" class="d-flex justify-center">
        <v-card 
         height="300"
         width="300"
         class="my-2"
          link
          :to="{ name: 'install-detail', params: { id: install.id } }">
          <v-img :src="install.image"></v-img>
          <v-card-title>{{ install.name }}</v-card-title>
          <v-card-sub-title>{{ install.blerb }}</v-card-sub-title>
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
<script>
import {installation_list} from "@/assets/js/Lists"
export default{
    name:'InstallationPage',
    data: () => ({
    installs: installation_list
    
  }),
  
  }
  </script>