<template>
<v-container>
<h4> {{ maintenance }} = {{ $route.params.id }}</h4>
</v-container>    
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import * as apiService from '@/assets/js/apiService';
const maintenance = ref('');
const route = useRoute()

const fetchData = async (pk) => {
    const response = await apiService.fetchMaintenance(pk);
    maintenance.value = response.data;
};

onMounted(() => {
    fetchData(route.params.id)
    });
</script>