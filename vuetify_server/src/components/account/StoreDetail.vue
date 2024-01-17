<template>

    <v-container>
      <v-carousel>
        <v-carousel-item
          :src="product.picture_1"
          cover
        ></v-carousel-item>

        <v-carousel-item
        :src="product.picture_2"
          cover
        ></v-carousel-item>

        <v-carousel-item
        :src="product.picture_3"
          cover
        ></v-carousel-item>

        <v-carousel-item
        :src="product.picture_4"
          cover
        ></v-carousel-item>
      </v-carousel>
        <p  class="text-center">{{ product.description }}</p>
        <!-- Display other details as needed -->
      <v-row no-gutters>
        <v-col>
          <v-btn :to="{name: 'store'}">Back</v-btn>
 
        </v-col>
      </v-row>  
    </v-container>   
</template>
       
<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import * as apiService from '@/assets/js/apiService';
const product = ref('');
const route = useRoute()

const fetchData = async (pk) => {
    const response = await apiService.fetchProduct(pk);
    product.value = response.data;
};

onMounted(() => {
    fetchData(route.params.id)
    });
</script>