<template>
  <v-app>
    <v-app-bar app color="primary" dark></v-app-bar>
    <div class="content">
      <v-content>
        <router-view></router-view>
      </v-content>
    </div>
    <footer class="footer">
      Sticky Footer
    </footer>
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "App"
});
</script>

<style lang="scss" scoped>
html,
body {
  height: 100%;
}
body {
  display: flex;
  flex-direction: column;
}
.content {
  flex: 1 0 auto;
}
.footer {
  flex-shrink: 0;
}
</style>
