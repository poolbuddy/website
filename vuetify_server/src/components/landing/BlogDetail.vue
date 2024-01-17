<template>

    <div>
        <h2>Item Detail</h2>
        <p>{{ selectedItem.name }}</p>
        <!-- Display other details as needed -->
      </div>
        
    </template>
    <script>
    export default {
        name: 'BlogDetail',
    
        computed: {
            selectedItem() {
              // Retrieve the selected item from the store or API based on the route parameter
              const itemId = this.$route.params.id;
              // Replace this with your actual logic to fetch the item details
              // For demonstration, using a mock data array
              const items = [
                { id: 1, name: 'Item 1', description: 'Details of Item 1' },
                { id: 2, name: 'Item 2', description: 'Details of Item 2' },
                { id: 3, name: 'Item 3', description: 'Details of Item 3' },
                { id: 4, name: 'Item 4', description: 'Details of Item 4' },
                { id: 5, name: 'Item 5', description: 'Details of Item 5' },
                { id: 6, name: 'Item 6', description: 'Details of Item 6' },
                { id: 7, name: 'Item 7', description: 'Details of Item 7' },
                { id: 8, name: 'Item 8', description: 'Details of Item 8' },
                { id: 9, name: 'Item 9', description: 'Details of Item 9' },
                { id: 10, name: 'Item 10', description: 'Details of Item 10' },
              ];
              return items.find(item => item.id == itemId) || {};
            },
    
        },
      }
      </script>
      