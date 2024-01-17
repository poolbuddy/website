<template>
<v-container>
<h4>{{ product }} = {{ $route.params.id }}</h4>
</v-container>    
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import * as apiService from '@/assets/js/apiService';
const product = ref('');
const route = useRoute()

const fetchData = async (pk) => {
    const response = await apiService.fetchCustomersProduct(pk);
    product.value = response.data;
};

onMounted(() => {
    fetchData(route.params.id)
    });
</script>