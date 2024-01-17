<template>
  <v-container>
   
    <v-data-iterator :items-per-page="itemsPerPage"  :search="search" :items="products">
      <template v-slot:header="{ page, pageCount,  prevPage, nextPage }">
        <v-toolbar class="bg-surface mb-3">
         
          <v-row no-gutters justify="space-between">
            <v-btn class="me-8" variant="text" @click="onClickSeeAll">
              <span class="text-decoration-underline text-none">See all</span>
            </v-btn>
            <h1 class="text-center text-h4 lex">Company Store</h1>
            <div class="d-inline-flex ma-1">
              <v-btn
                :disabled="page === 1"
                icon="mdi-arrow-left"
                size="small"
                variant="tonal"
                class="me-2"
                @click="prevPage"
              ></v-btn>

              <v-btn
              :disabled="page === pageCount"
                icon="mdi-arrow-right"
                size="small"
                variant="tonal"
                @click="nextPage"
              ></v-btn>
            </div>
          </v-row>
        
        </v-toolbar>
        <v-row no-gutters>
            <v-text-field
            v-model="search"
            clearable
            density="comfortable"
            hide-details
            placeholder="Search"
            prepend-inner-icon="mdi-magnify"
            style="max-width: 300px;"
            variant="solo"
          ></v-text-field>
          </v-row>
      </template>

        <template v-slot:default="{ items }">
          <v-row>
            <v-col
            v-for="(item, i) in items"
            :key="i"
            cols="12"
            sm="6"
            xl="3"
            >
            <v-sheet border>
              <router-link :to="{ name: 'store-detail', params: { id: item.raw.id }  }">
                <v-img
                :gradient="`to top right, rgba(255, 255, 255, .1), rgba(${color}, .15)`"
                :src="item.raw.picture_1"
                
                height="150"
                ></v-img>
              </router-link>
          

            <v-list-item
              :title="item.raw.title"
              lines="two"
              density="comfortable"
              :subtitle="item.raw.description"
            >
              <template v-slot:title>
                <strong class="text-h6">
                  {{ item.raw.title }}
                </strong>
              </template>
            </v-list-item>
            <v-table density="compact" class="text-caption">
              <tbody>
                <tr align="right">
                  <th># in Stock :</th>

                  <td> {{item.raw.stock}} </td>
                </tr>
             

                <tr align="right">
                  <th>Price:</th>

                  <td>${{ item.raw.price }}</td>
                </tr>
                <tr align="right">
                  <th>Order Now:</th> 

                  <td><v-btn :to="{ name:'order', params: { id: item.raw.id }}">Order</v-btn></td>
                </tr>
              </tbody>
            </v-table>
          </v-sheet>
            </v-col>
          </v-row>
         
          
        </template>

        <template v-slot:footer="{ page, pageCount }">
        <v-footer color="surface-variant" class="justify-space-between text-body-2 mt-4">
          total products: {{ products.length }}
          <div>
            Page {{ page }} of {{ pageCount }}
          </div>
        </v-footer>
      </template>
        
    </v-data-iterator>
  </v-container> 
</template>

<script setup>
import { ref, onMounted } from 'vue';
import * as apiService from '@/assets/js/apiService';

const color = ref("12,44,265");
const itemsPerPage = ref(4);
const products = ref([]);


const onClickSeeAll = () => {
  itemsPerPage.value = itemsPerPage.value === 4 ? products.length : 4;
};

const fetchData = async () => {
  try {
    const response = await apiService.fetchProductList()
    products.value = response.data;
  } catch (error) {
    alert(error)
    console.error('Error fetching product list:', error);
  }
};



onMounted(() => {
  fetchData();
});
</script>

