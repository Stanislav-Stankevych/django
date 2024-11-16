//hei det er stas
import { createApp } from 'vue';
import SocialLink from './SocialLink.vue';

const app = createApp({});
app.component('social-link', SocialLink);
app.mount('#footer1-app');


console.log('Vue is working!');