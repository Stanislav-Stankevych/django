<template>
  <a :href="href" class="social-link">
    <slot></slot>
  </a>
</template>

<script>
export default {
  name: "SocialLink",
  props: {
    href: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
.social-link {
  transition: all 0.3s ease;
}
.social-link:hover {
  transform: scale(1.1);
  color: #0077b6;
}
</style>
