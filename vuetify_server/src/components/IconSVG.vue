<template>
    
      <div v-html="svgContent" style="width:100px"></div>
    
</template>
  
<script>
import { defineComponent } from 'vue';

export default defineComponent({
name: 'IconSVG',

data() {
    return {
    svgContent: null,
    };
},
mounted() {
    this.loadSvg();
},
methods: {
    async loadSvg() {
    try {
        const response = await fetch('/src/assets/cst2.svg');
        this.svgContent = await response.text();
    } catch (error) {
        console.error('Error loading SVG:', error);
    }
    },
    changeColor() {
    // Example: Change the fill color of the circle to blue
    this.svgContent = this.svgContent.replace('fill="red"', 'fill="blue"');
    },
},
});
</script>