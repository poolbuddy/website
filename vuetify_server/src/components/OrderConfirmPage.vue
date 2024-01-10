<template>
    <v-container>
        <h1>Thank You!!</h1>
        <h4> 
                Confirmed {{ email }} - We have confirmed your order and sent a confirmation email to the email provided. 
             The speed of the delivery is applicaple after the product is paid for.  
             The order can also now can be viewed in the dashboard.
        </h4>
        <h4 v-if="payment_method==='invoice'">

        </h4>
        <h4 v-if="payment_method==='invoice'">

        </h4>
        <h4 v-if="payment_method==='invoice'">

        </h4>
        <h4 v-if="payment_method==='invoice'">

        </h4>
        <h4 v-if="delivery_type==='invoice'">

        </h4>
        <h4 v-if="delivery_type==='invoice'">

        </h4>
        <br>
        <h1>quantity: {{ quantity }}</h1>
       
        <h1>speed: {{ speed }}</h1>
        <h1>payment_method: {{ payment_method }}</h1>
        <h1>delivery_type: {{ delivery_type }}</h1>
        <h1>available store credit: {{ store.profile.store_credit }}</h1>
       
<v-row no-gutters><v-btn :to="{name: 'store'}">store</v-btn><v-btn :to="{name: 'dashboard'}">dashboard</v-btn></v-row>
    </v-container>
</template>
<script setup>
import { useRoute, useRouter } from 'vue-router';
import { ref, onMounted, watch  } from 'vue';
import { useUser } from '@/store/user';
import * as apiService from '@/assets/js/apiService';

const store = useUser()

const route = useRoute()
const product_list = ref()
const productNum = ref()
const email = ref()
const speed = ref()
const quantity = ref()
const payment_method = ref()
const delivery_type = ref()
const product = ref()
const productWrap = ref()

const fetchData = async (pk) => {

        const response = await apiService.fetchCustomersProductListPK(pk);
        product_list.value = response.data;
        const listNum = response.data.product.length;
        product_list.value = response.data;
        email.value = response.data.email;
        
        productWrap.value = response.data.product[listNum - 1];
        speed.value = response.data.product[listNum - 1].speed;
        quantity.value = response.data.product[listNum - 1].quantity;
        payment_method.value = response.data.product[listNum - 1].payment_method;
        delivery_type.value = response.data.product[listNum - 1].delivery_type;
        productNum.value = response.data.product[listNum - 1].product;
       
};

const fetchProductData = async () => {
    const response1 = await apiService.fetchProduct(productNum.value);
    product.value = response1.data
}

watch(productNum, fetchProductData);

    
onMounted(async() => {
    await fetchData(route.params.id)
});


</script>