<template>
  <div>
    <my-form></my-form>
  </div>
</template>
  <script>
  import EstimateRequestForm from '@/components/account/EstimateRequestGenForm.vue';
  export default {
   
    components: {
    'my-form': EstimateRequestForm,
  },
  }
  </script>