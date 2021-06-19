<template>
  <div id="app">
    <ul class="list-group" v-if="poisData" style="text-align: center;">
      <li class="list-group-item" v-for="poi in poisData" :key="poi.id">id: {{ poi.id }}
        | distance (meters): {{ poi.poi_info.properties.distance }}
        | coordinates: {{ poi.poi_info.geometry.coordinates }}</li>
    </ul>
    <h3 v-else-if="poisLoading">Loading POIs</h3>
    <h3 v-else-if="poisLoadingFailed">Failed loading POIs. Refresh page later</h3>
  </div>
</template>

<script>
import axios from 'axios';
import { API_BASE_URL } from '@/config';

export default {
  name: 'App',
  data() {
    return {
      poisData: null,
      poisLoading: false,
      poisLoadingFailed: false,
    }
  },
  methods: {
    loadAllPois() {
      this.poisLoading = true;
      this.poisLoadingFailed = false;
      return axios.get(`${API_BASE_URL}/api/pois/`)
          .then(response => {
            this.poisData = response.data;
          })
          .catch(() => {
            this.poisLoadingFailed = true;
          })
    },
  },
  created() {
    this.loadAllPois();
  }
};
</script>

<style>
</style>
