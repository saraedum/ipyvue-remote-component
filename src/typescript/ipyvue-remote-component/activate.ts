import Vue from "vue";
import RemoteComponent from "vue-remote-component";

export default function activate() {
    Vue.component('remote-component', RemoteComponent);
}
