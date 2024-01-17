<template>
    <v-container>

        <v-form>

             <v-card width="350" class="mx-auto">
                <v-img
                :gradient="`to top right, rgba(255, 255, 255, .1), rgba(${color}, .15)`"
                :src="product.picture_1"
                cover
                height="150"
                ></v-img>


                <v-radio-group v-model="form.payment_method" class="d-flex justify-center mb-3" label="How do you want to pay for the product?">
                <v-divider></v-divider>
                <v-radio class="mb-2" label="Use the card on file" value="card"></v-radio>
                <v-divider></v-divider>
                <v-radio class="mb-2" label="Email me an invoice" value="invoice"></v-radio>
                <v-divider></v-divider>
                <v-radio label="Store Credit" value="store_credit"></v-radio>
                <v-divider></v-divider>
                </v-radio-group>


                <v-radio-group v-model="form.delivery_type" class="d-flex justify-center my-3" label="How do you want the product delivered?">
                
                <v-divider></v-divider>
                <v-radio label="Mail it to me" value="mail"></v-radio>
                <v-divider></v-divider>
                <div>
                <v-radio label="Get it ready and put it in the pool" value="in_pool">
                </v-radio>
                <p class="text-caption text-red">*Active Regular Maintenance Customers Only*</p>
                </div>
                <v-divider></v-divider>
                <div>
                <v-radio label="Put it in the shed { or some other designated storage area }" value="in_shed">
                </v-radio>
                <p class="text-caption text-red">*Active Regular Maintenance Customers Only*</p>
                </div>
                <v-divider></v-divider>
                

                </v-radio-group>


                <v-radio-group v-model="form.speed" class="d-flex justify-center my-3" label="Speed of Delivery-Contingent on payment">
                <v-divider></v-divider>
                <v-radio class="mb-2" label="1-3 days - $35" value="1_3_days"></v-radio>
                <v-divider></v-divider>
                <v-radio label="1 week - $0" value="week"></v-radio>
                <v-divider></v-divider>

                </v-radio-group>


                <v-row justify="center" class="ma-2" no-gutters>
                    <div class="d-flex align-end text-overline"> left in stock </div>
                    <v-text-field label="How many do you want?" v-model="form.quantity" prepend-icon="mdi-counter" class="w-25"></v-text-field>
                </v-row>
             </v-card>
             <v-row no-gutters justify="end">
                    <v-btn @click="submit">order</v-btn>
                </v-row>

        </v-form>
    </v-container>
</template>
    
<script setup>
import { useUser } from '@/store/user';
    import { ref, onMounted } from 'vue';
    import { useRoute, useRouter } from 'vue-router';
    import * as apiService from '@/assets/js/apiService';

    
    const product = ref('');
    const store = useUser();
    const wrapped_product = ref(null);
    const route = useRoute()
    const router = useRouter()
    const form = ref({
        speed: 'loo',
        delivery_type: 'loo',
        payment: 'loo',
        email: 'admin@admin.com',
        product: 1,
        quantity: 1,
        payment_method: 'admin'

    })
    
    const fetchData = async (pk) => {
        const response = await apiService.fetchProduct(pk);
        product.value = response.data;
    };

    const order = async (formData) => {
        formData.customer_email = store.email
        formData.product = product.value
        const response2 = await apiService.addItemProductList(formData.value);

        if(response2.status === 200){
          
            await router.push(`/order-confirm/${response2.data.id}/`)
        }
      
    };

    const submit = async () => {
        
        await order(form)
       
    }
    
    onMounted(() => {
        fetchData(route.params.id)
        });
    </script>