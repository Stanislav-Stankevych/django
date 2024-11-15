<template>
    <div class="p-4 text-center">
      <h1 class="text-2xl font-bold mb-4">Добро пожаловать в Vue.js!</h1>
      <button @click="toggleMessage" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        {{ buttonLabel }}
      </button>
      <p v-if="showMessage" class="mt-4 text-gray-600">Привет, это интерактивный компонент Vue.js!</p>
    </div>
  </template>
  
  