<template>
  <div>
    <h1>{{ message }}</h1>
    <button @click="loadMessage">Обновить</button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const message = ref("Загрузка...");

async function loadMessage() {
  try {
    const response = await axios.get("api/hello");
    message.value = response.data.message;
  } catch (e) {
    console.error(e);
    message.value = "Ошибка соединения";
  }
}

loadMessage();
</script>
