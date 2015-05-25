%include frontend/_header.html.tpl

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

  %include frontend/_photoswipe.html.tpl
</div><!--/.container-->

<script src="/static/application.js"></script>

% include frontend/_footer.html.tpl
