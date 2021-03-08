import { Vue } from "jupyter-vue";
import RemoteComponent from "vue-remote-component";

export function activate(app, widget) {
  // Register <remote-component/> as a tag with Vue.js.
  Vue.component("remote-component", RemoteComponent);
}
