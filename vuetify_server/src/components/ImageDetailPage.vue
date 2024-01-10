<template>
    <v-sheet>
        <v-img
            :src="route.params.src"
            max-height="125"
            class="bg-grey-lighten-2"
        ></v-img>
        <v-btn :to="{name:'dashboard'}">back</v-btn>
    </v-sheet>
</template>
<script setup>
import { ref } from 'vue';
import { useRoute} from 'vue-router';

const route = useRoute()
const image = ref()
</script>