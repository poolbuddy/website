<template>
    <v-container>
      <h2>Blog</h2>
      <v-row no-gutters>
        <v-col>
      <v-list>
      <v-list-item v-for="item in items" 
        :key="item.id"
        link
        :to="{ name: 'blog-detail', params: { id: item.id } }">
        <div :class="['pa-2', item.id % 2 === 0 ? 'bg-grey-lighten-2' : '']">
          Item #{{ item.name }}
        </div>
        <template v-slot:prepend-avatar>
  
        </template>
      </v-list-item>
      </v-list>
    </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
  
    name: 'BlogView',
    data: () => ({
      items: [
            { id: 1, name: 'Item 1' },
            { id: 2, name: 'Item 2' },
            { id: 3, name: 'Item 3' },
            { id: 4, name: 'Item 4' },
            { id: 5, name: 'Item 5' },
            { id: 6, name: 'Item 6' },
            { id: 7, name: 'Item 7' },
            { id: 8, name: 'Item 8' },
            { id: 9, name: 'Item 9' },
            { id: 10, name: 'Item 10' },
            // Add more items...
          ],
      }),
  
      methods: {
        load ({ done }) {
          setTimeout(() => {
            this.items.push(...Array.from({ length: 10 }, (k, v) => v + this.items.at(-1) + 1))
  
            done('ok')
          }, 1000)
        },
      },
  
  }
  </script>