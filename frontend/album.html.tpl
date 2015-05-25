%include frontend/header.html.tpl

<nav class="navbar navbar-inverse">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <img src="/static/Logo.svg" class="navbar-brand">
    </div>
    <div id="navbar" class="collapse navbar-collapse">
      <ul class="nav navbar-nav">
        <li><a href="#invite_friends"><span class="icn icn-add-friends"></span>Invite friends</a></li>
        <li><a href="" class="js-download-all"><span class="icn icn-download"></span>Download as zip</a></li>
        <li><a href="#memory_tunes"><span class="icn icn-soundcloud"></span>Memory tunes</a></li>
      </ul>
    </div><!--/.nav-collapse -->
  </div>
</nav>

<div class="container">

  <h1 class="heading album-title"></h1>

  <form action=""
        class="dropzone"
        id="my-awesome-dropzone">
  </form>

  <h1 class="heading album-pictures"></h1>

  <div class="album" itemscope itemtype="http://schema.org/ImageGallery">
  </div>

  <h1 class="heading" id="invite_friends">Invite friends</h1>

  Invite more friends to share their photos. They'll receive and email with a link to this PhotoBasket.

  <form id="frmOptions" method="post" class="span12 invite-form">
    <div class="row-fluid">
      <div class="form-group">
        <label class="control-label" for="email">Email address</label>
        <div class="input-group ">
          <input id="email" type="email" class="form-control" placeholder="john.doe@example.com">
          <a class="input-group-btn btn btn-primary js-invite"><span class="icn icn-add-friends"></span></a>
        </div>
      </div>
    </div>
  </form>

  There are already <span class="js-number-of-friends"></span> friends in this basket.

  <h1 class="heading" id="memory_tunes">Memory tunes</h1>

  <span class="js-soundcloud"></span>

  <!-- Root element of PhotoSwipe. Must have class pswp. -->
  <div class="pswp" tabindex="-1" role="dialog" aria-hidden="true">

    <!-- Background of PhotoSwipe.
    It's a separate element, as animating opacity is faster than rgba(). -->
    <div class="pswp__bg"></div>

    <!-- Slides wrapper with overflow:hidden. -->
    <div class="pswp__scroll-wrap">

      <!-- Container that holds slides. PhotoSwipe keeps only 3 slides in DOM to save memory. -->
      <!-- don't modify these 3 pswp__item elements, data is added later on. -->
      <div class="pswp__container">
        <div class="pswp__item"></div>
        <div class="pswp__item"></div>
        <div class="pswp__item"></div>
      </div>

      <!-- Default (PhotoSwipeUI_Default) interface on top of sliding area. Can be changed. -->
      <div class="pswp__ui pswp__ui--hidden">

        <div class="pswp__top-bar">

          <!--  Controls are self-explanatory. Order can be changed. -->

          <div class="pswp__counter"></div>

          <button class="pswp__button pswp__button--close" title="Close (Esc)"></button>

          <button class="pswp__button pswp__button--share" title="Share"></button>

          <button class="pswp__button pswp__button--fs" title="Toggle fullscreen"></button>

          <button class="pswp__button pswp__button--zoom" title="Zoom in/out"></button>

          <!-- Preloader demo http://codepen.io/dimsemenov/pen/yyBWoR -->
          <!-- element will get class pswp__preloader--active when preloader is running -->
          <div class="pswp__preloader">
            <div class="pswp__preloader__icn">
              <div class="pswp__preloader__cut">
                <div class="pswp__preloader__donut"></div>
              </div>
            </div>
          </div>
        </div>

        <div class="pswp__share-modal pswp__share-modal--hidden pswp__single-tap">
          <div class="pswp__share-tooltip"></div>
        </div>

        <button class="pswp__button pswp__button--arrow--left" title="Previous (arrow left)">
        </button>

        <button class="pswp__button pswp__button--arrow--right" title="Next (arrow right)">
        </button>

        <div class="pswp__caption">
          <div class="pswp__caption__center"></div>
        </div>
      </div>
    </div>
  </div>
</div>
<script src="/static/application.js"></script>

% include frontend/footer.html.tpl
