Vue.component('tl_img', {
  props: {
    tl_src: String
  }
  templates: "<img :src="tl_src" alt="">"
})

Vue.component('tl_speech', {
  props: {
    tl_side: String
  }
  templates:
  `
  <div :class="tl_side">
    <div id="character">
      <img :src="chara" alt="">
    </div>
    <div class="talk">
      <p class='border-top'>Bonjour cher habitant de la résidence <em>Shangri-La</em> !<br> Vous avez un nouveau message 🌟 !</p>
    </div>
  </div>
  `
})
