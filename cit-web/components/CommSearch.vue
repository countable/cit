<template>
  <div>
    {{ commSearch }}
    <v-autocomplete
      v-model="commSearch"
      :items="communities"
      item-value="id"
      item-text="place_name"
      :label="label"
      append-icon="mdi-map-search"
      :solo="solo"
      hide-details
      placeholder="Community Name"
      :dense="dense"
      :outlined="outlined"
      @input="handleChange"
    ></v-autocomplete>
  </div>
</template>

<script>
import { Vue, Component, namespace, Prop } from 'nuxt-property-decorator'
const commModule = namespace('communities')
@Component
export default class CommSearch extends Vue {
  @Prop({ default: 'black', type: String }) color
  @Prop({ default: 'Community Name', type: String }) label
  @Prop({ default: false, type: Boolean }) dense
  @Prop({ default: false, type: Boolean }) solo
  @Prop({ default: false, type: Boolean }) outlined
  commSearch = null
  communities = []
  @commModule.Getter('getCommunities') communities

  handleChange(cid) {
    if (!cid) {
      return
    }
    this.$router.push({
      path: `/community/${cid}`,
    })
    this.$nextTick(() => {
      this.commSearch = null
    })

    this.$emit('changed')
  }
}
</script>
